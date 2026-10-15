"""Shared paths, cohort rules and data loaders for the ABIDE collaboration experiment."""

import hashlib
import json
import pathlib

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
GRAPH = ROOT / "graph"
QUERIES = ROOT / "queries"
DERIVED = DATA / "derived"
for _p in (RESULTS, FIGURES, GRAPH, QUERIES, DERIVED):
    _p.mkdir(parents=True, exist_ok=True)

S3 = "https://s3.amazonaws.com/fcp-indi/data/Projects/ABIDE_Initiative"
PHENO_PATH = DATA / "Phenotypic_V1_0b_preprocessed1.csv"
CC200_REL = "Outputs/cpac/filt_noglobal/rois_cc200/{fid}_rois_cc200.1D"
THICK_REL = "Outputs/ants/roi_thickness/{fid}_roi_thickness.txt"
RAW_BOLD_REL = "RawDataBIDS/{site}/sub-{sub:07d}/func/sub-{sub:07d}_task-rest_run-1_bold.nii.gz"
RAW_T1_REL = "RawDataBIDS/{site}/sub-{sub:07d}/anat/sub-{sub:07d}_T1w.nii.gz"

SEED = 42
N_ROI = 200

MOTION_RULES = {"v1": 0.2, "v2": 0.15}
FIQ_RANGE = (78.0, 138.0)
MIN_PER_GROUP_PER_SITE = 10


def sha256_bytes(data: bytes) -> str:
    """Return the hex SHA256 of a byte string."""
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: pathlib.Path) -> str:
    """Return the hex SHA256 of a file."""
    return sha256_bytes(path.read_bytes())


def load_pheno() -> pd.DataFrame:
    """Load the ABIDE Preprocessed phenotype table with its 1-based CSV data-row number."""
    d = pd.read_csv(PHENO_PATH)
    d["source_row"] = np.arange(2, len(d) + 2)
    return d


def cc200_path(fid: str) -> pathlib.Path:
    """Local path of a participant's CC200 ROI time series."""
    return DATA / CC200_REL.format(fid=fid)


def load_timeseries(fid: str) -> np.ndarray:
    """Load a CC200 time series as (timepoints, 200)."""
    return np.loadtxt(cc200_path(fid), skiprows=1)


def raw_bold_url(row: pd.Series) -> str:
    """S3 URL of the raw BIDS resting BOLD scan for a phenotype row."""
    site = row["FILE_ID"].rsplit("_", 1)[0]
    return f"{S3}/{RAW_BOLD_REL.format(site=site, sub=int(row['SUB_ID']))}"


def rater_qc_pass(d: pd.DataFrame) -> pd.Series:
    """Three-rater visual QC as used by nilearn.datasets.fetch_abide_pcp(quality_checked=True)."""
    return (
        (d.qc_rater_1 != "fail")
        & d.qc_anat_rater_2.isin(["OK", "maybe"])
        & d.qc_func_rater_2.isin(["OK", "maybe"])
        & (d.qc_anat_rater_3 == "OK")
        & (d.qc_func_rater_3 == "OK")
    )


def coverage_table() -> pd.DataFrame:
    """Per-FILE_ID time-series length and count of zero-variance ROIs (cached in data/derived)."""
    cache = DERIVED / "timeseries_coverage.csv"
    if cache.exists():
        return pd.read_csv(cache)
    d = load_pheno()
    rows = []
    for fid in sorted(d.loc[d.FILE_ID != "no_filename", "FILE_ID"]):
        x = load_timeseries(fid)
        rows.append(
            {
                "FILE_ID": fid,
                "n_timepoints": x.shape[0],
                "n_zero_variance_rois": int((x.std(0) < 1e-8).sum()),
                "timeseries_sha256": sha256_file(cc200_path(fid)),
            }
        )
    out = pd.DataFrame(rows)
    out.to_csv(cache, index=False)
    return out


def base_table() -> pd.DataFrame:
    """Phenotype joined to time-series coverage; one row per FILE_ID with data."""
    d = load_pheno()
    d = d[d.FILE_ID != "no_filename"].merge(coverage_table(), on="FILE_ID", how="left")
    d["full_roi_coverage"] = d.n_zero_variance_rois == 0
    d["rater_qc_pass"] = rater_qc_pass(d)
    d["dx"] = np.where(d.DX_GROUP == 1, "ASD", "TD")
    return d.reset_index(drop=True)


def cohort_b(d: pd.DataFrame, rule: str) -> pd.Series:
    """Analyst B: rater QC + full ROI coverage + shared motion rule."""
    return d.rater_qc_pass & d.full_roi_coverage & (d.func_mean_fd < MOTION_RULES[rule])


def cohort_a(d: pd.DataFrame, rule: str) -> pd.Series:
    """Analyst A: males, FIQ in range, rater QC, full coverage, shared motion rule, sites with >=10 per group."""
    m = (
        (d.SEX == 1)
        & d.FIQ.between(*FIQ_RANGE)
        & d.rater_qc_pass
        & d.full_roi_coverage
        & (d.func_mean_fd < MOTION_RULES[rule])
    )
    counts = d[m].groupby(["SITE_ID", "dx"]).size().unstack(fill_value=0)
    ok_sites = counts[(counts.get("ASD", 0) >= MIN_PER_GROUP_PER_SITE) & (counts.get("TD", 0) >= MIN_PER_GROUP_PER_SITE)].index
    return m & d.SITE_ID.isin(ok_sites)


def connectivity() -> tuple[np.ndarray, list[str]]:
    """Fisher-z correlation upper-triangle vectors for every full-coverage FILE_ID (cached)."""
    cache = DERIVED / "cc200_fisherz_upper.npz"
    if cache.exists():
        z = np.load(cache, allow_pickle=False)
        return z["X"], list(z["file_ids"])
    d = base_table()
    fids = sorted(d.loc[d.full_roi_coverage, "FILE_ID"])
    iu = np.triu_indices(N_ROI, 1)
    X = np.empty((len(fids), len(iu[0])), dtype=np.float32)
    for i, fid in enumerate(fids):
        r = np.corrcoef(load_timeseries(fid).T)[iu]
        X[i] = np.arctanh(np.clip(r, -0.999999, 0.999999))
    np.savez_compressed(cache, X=X, file_ids=np.array(fids))
    return X, fids


def edge_index() -> tuple[np.ndarray, np.ndarray]:
    """Upper-triangle ROI index pairs (0-based) in feature order."""
    return np.triu_indices(N_ROI, 1)


def roi_hemisphere() -> np.ndarray:
    """Hemisphere label per CC200 ROI from its centre-of-mass x coordinate (L if x<0, R if x>0, M if 0)."""
    lab = pd.read_csv(DATA / "Resources/CC200_ROI_labels.csv", skipinitialspace=True)
    x = lab["center of mass"].str.strip("()").str.split(";").str[0].astype(float).to_numpy()
    return np.where(x < 0, "L", np.where(x > 0, "R", "M"))


def write_json(name: str, obj: object) -> pathlib.Path:
    """Write a results JSON with stable formatting."""
    p = RESULTS / name
    p.write_text(json.dumps(obj, indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o)))
    return p
