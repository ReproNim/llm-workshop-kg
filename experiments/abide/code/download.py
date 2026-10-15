"""Download the ABIDE Preprocessed inputs used by this experiment and record a hash manifest.

Usage: uv run python code/download.py
"""

import hashlib
import json
import pathlib
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
S3 = "https://s3.amazonaws.com/fcp-indi/data/Projects/ABIDE_Initiative"
PHENO = "Phenotypic_V1_0b_preprocessed1.csv"
RESOURCES = ["pipeline_config.yml", "CC200_ROI_labels.csv", "scan_parameters_abide.csv"]
CC200 = "Outputs/cpac/filt_noglobal/rois_cc200/{fid}_rois_cc200.1D"
THICK = "Outputs/ants/roi_thickness/{fid}_roi_thickness.txt"
PAPERS = {
    "papers/dimartino2014_PMC4162310.xml": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4162310/fullTextXML",
    "papers/abraham2017_arxiv1611.06066v1.pdf": "https://arxiv.org/pdf/1611.06066v1",
}
SIMPLE2 = "https://raw.githubusercontent.com/ReproNim/simple2_NIDM_examples/e0dff17629bd5031e246c05ff4bed174597552a2/"
SIMPLE2_SITES = ["CMU_a", "CMU_b", "Caltech", "KKI", "Leuven_1", "Leuven_2", "MaxMun_a", "MaxMun_b", "MaxMun_c", "MaxMun_d", "NYU", "OHSU", "Olin",
                 "Pitt", "SBL", "SDSU", "Stanford", "Trinity", "UCLA_1", "UCLA_2", "UM_1", "UM_2", "USM", "Yale"]
SIMPLE2_FILES = {f"repronim_simple2/datasets.datalad.org/abide/RawDataBIDS/{s}/nidm.ttl": SIMPLE2 + f"datasets.datalad.org/abide/RawDataBIDS/{s}/nidm.ttl" for s in SIMPLE2_SITES}
SIMPLE2_FILES.update({
    "repronim_simple2/queries/simple2_query.sparql": SIMPLE2 + "queries/simple2_query.sparql",
    "repronim_simple2/queries/get_volumes.sparql": SIMPLE2 + "queries/get_volumes.sparql",
    "repronim_simple2/queries/simple2_query_output.csv": SIMPLE2 + "queries/simple2_query_output.csv",
    "repronim_simple2/bids_nidm_scripts/abide_phenotypic_v1_0b_vars_to_terms_v5.json": SIMPLE2 + "bids_nidm_scripts/abide_phenotypic_v1_0b_vars_to_terms_v5.json",
    "repronim_simple2/bids_nidm_scripts/nidm_create_abide_v11.sh": SIMPLE2 + "bids_nidm_scripts/nidm_create_abide_v11.sh",
    "repronim_simple2/cde_tools/fs_cde.ttl": SIMPLE2 + "cde/fs_cde.ttl",
    "repronim_simple2/cde_tools/ants_cde.ttl": "https://raw.githubusercontent.com/ReproNim/ants_seg_to_nidm/97e6257b0827a0e6bcc78c179f83168c83397f39/ants_seg_to_nidm/mapping_data/ants_cde.ttl",
    "repronim_simple2/cde_tools/fsl_cde.ttl": "https://raw.githubusercontent.com/ReproNim/fsl_seg_to_nidm/54f91ec7c5c10837d1970bcbd2e39add6a5a3530/fsl_seg_to_nidm/mapping_data/fsl_cde.ttl",
})
EXPECTED = DATA / "expected_sha256.json"


def sha256(path: pathlib.Path) -> str:
    """Return the hex SHA256 of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch(rel: str, url: str | None = None) -> dict:
    """Fetch one key (S3 by default) into data/ unless present; return its manifest record."""
    dest = DATA / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = url or f"{S3}/{rel}"
    status = "present"
    if not dest.exists():
        try:
            urllib.request.urlretrieve(url, dest)
            status = "downloaded"
        except Exception as exc:  # noqa: BLE001
            return {"path": rel, "url": url, "status": f"missing: {exc}"}
    return {"path": rel, "url": url, "status": status, "sha256": sha256(dest), "bytes": dest.stat().st_size}


def main() -> None:
    """Download phenotype, resources, CC200 time series and ANTs ROI thickness for every FILE_ID."""
    records = [fetch(PHENO)] + [fetch(f"Resources/{r}") for r in RESOURCES]
    records += [fetch(rel, url) for rel, url in PAPERS.items()]
    with ThreadPoolExecutor(8) as pool:
        records += list(pool.map(lambda kv: fetch(*kv), SIMPLE2_FILES.items()))
    pheno = pd.read_csv(DATA / PHENO)
    fids = sorted(pheno.loc[pheno.FILE_ID != "no_filename", "FILE_ID"])
    rels = [CC200.format(fid=f) for f in fids] + [THICK.format(fid=f) for f in fids]
    with ThreadPoolExecutor(16) as pool:
        records += list(pool.map(fetch, rels))
    (DATA / "download_manifest.json").write_text(json.dumps(records, indent=1))
    missing = [r for r in records if r["status"].startswith("missing")]
    print(f"{len(records)} records, {len(missing)} missing")
    if "--write-expected" in sys.argv:
        EXPECTED.write_text(json.dumps({r["path"]: r["sha256"] for r in records if "sha256" in r}, indent=1, sort_keys=True))
        return
    if EXPECTED.exists():
        expected = json.loads(EXPECTED.read_text())
        got = {r["path"]: r.get("sha256") for r in records}
        bad = sorted(k for k in expected if got.get(k) != expected[k])
        print(f"hash check: {len(expected) - len(bad)}/{len(expected)} match")
        paper_drift = [k for k in bad if k in PAPERS]
        if paper_drift:
            print("WARNING: paper text changed upstream; quotes are re-verified by code/papers.py:", paper_drift)
        bad = [k for k in bad if k not in PAPERS]
        if bad or missing:
            print("MISMATCH:", bad[:20])
            sys.exit(1)


if __name__ == "__main__":
    main()
