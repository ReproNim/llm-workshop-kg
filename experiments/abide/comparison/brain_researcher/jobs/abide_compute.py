"""ABIDE I compute phase for the Brain Researcher arm of the comparison.

Not BR output: BR only returned the NITRC landing page; the fcp-indi S3 layout below is the
operator's prior knowledge. Cohort definitions are stated assumptions, written to results.json.

Analyst B (Abraham-style): phenotype row with FILE_ID + CC200 file + nilearn `quality_checked`
  rater filter (qc_rater_1=OK, qc_anat_rater_2 in OK/maybe, qc_func_rater_2 in OK/maybe,
  qc_anat_rater_3=OK, qc_func_rater_3=OK); leave-one-site-out, tangent connectivity + l2 logistic.
Analyst A (Di Martino-style): phenotype row with FILE_ID + CC200 file + func_mean_fd < 0.2 mm;
  edgewise OLS of Fisher-z correlation on DX + age + sex + mean FD + site, BH-FDR q<0.05.
Tightened QC: func_mean_fd < TIGHT (default 0.1 mm), sweep reported.
"""

import io
import json
import os
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

from joblib import Parallel, delayed

import numpy as np
import pandas as pd
import requests
from nilearn.connectome import ConnectivityMeasure
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

BASE = "https://s3.amazonaws.com/fcp-indi"
PREFIX = "data/Projects/ABIDE_Initiative"
PHENO_URL = f"{BASE}/{PREFIX}/Phenotypic_V1_0b_preprocessed1.csv"
ROI_URL = f"{BASE}/{PREFIX}/Outputs/cpac/filt_noglobal/rois_cc200/{{fid}}_rois_cc200.1D"
OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
TIGHT = float(os.environ.get("TIGHT_FD", "0.1"))
CACHE = os.path.join(OUT, "rois_cc200")
os.makedirs(CACHE, exist_ok=True)
results: dict = {"assumptions": __doc__, "tight_fd_mm": TIGHT, "urls": {"phenotype": PHENO_URL, "roi_template": ROI_URL}}


def s3_list(prefix: str) -> dict:
    """List one level of the public bucket (CommonPrefixes + first keys)."""
    r = requests.get(f"{BASE}/", params={"prefix": prefix, "delimiter": "/", "max-keys": "200"}, timeout=60)
    ns = {"s": "http://s3.amazonaws.com/doc/2006-03-01/"}
    root = ET.fromstring(r.content)
    return {
        "prefixes": [p.findtext("s:Prefix", namespaces=ns) for p in root.findall("s:CommonPrefixes", ns)],
        "keys": [k.findtext("s:Key", namespaces=ns) for k in root.findall("s:Contents", ns)][:50],
    }


def fetch_roi(fid: str):
    path = os.path.join(CACHE, f"{fid}_rois_cc200.1D")
    if not os.path.exists(path):
        r = requests.get(ROI_URL.format(fid=fid), timeout=120)
        if r.status_code != 200:
            return fid, None
        with open(path, "wb") as f:
            f.write(r.content)
    ts = np.loadtxt(path)
    return fid, ts


pheno = pd.read_csv(io.BytesIO(requests.get(PHENO_URL, timeout=120).content))
pheno.to_csv(os.path.join(OUT, "phenotype.csv"), index=False)
results["n_phenotype_rows"] = int(len(pheno))
pheno = pheno[pheno["FILE_ID"] != "no_filename"].copy()
results["n_with_file_id"] = int(len(pheno))

# Q3 provenance: what the bucket itself publishes about the pipeline
results["s3_listing"] = {p: s3_list(p) for p in [f"{PREFIX}/", f"{PREFIX}/Outputs/", f"{PREFIX}/Outputs/cpac/", f"{PREFIX}/Resources/"]}

with ThreadPoolExecutor(16) as ex:
    loaded = dict(ex.map(fetch_roi, pheno["FILE_ID"].tolist()))
pheno["has_cc200"] = pheno["FILE_ID"].map(lambda f: loaded.get(f) is not None)
results["n_with_cc200"] = int(pheno["has_cc200"].sum())
pheno = pheno[pheno["has_cc200"]].copy()

ok = lambda c, vals: pheno[c].astype(str).str.strip().str.upper().isin(vals)  # noqa: E731
qcB = (ok("qc_rater_1", {"OK"}) & ok("qc_anat_rater_2", {"OK", "MAYBE"}) & ok("qc_func_rater_2", {"OK", "MAYBE"})
       & ok("qc_anat_rater_3", {"OK"}) & ok("qc_func_rater_3", {"OK"}))
B = pheno[qcB].copy()
A = pheno[pheno["func_mean_fd"] < 0.2].copy()
A_tight = pheno[pheno["func_mean_fd"] < TIGHT].copy()
dx = {1: "ASD", 2: "TC"}
count = lambda d: {"total": int(len(d)), **{dx[k]: int(v) for k, v in d["DX_GROUP"].value_counts().sort_index().items()}}  # noqa: E731

# Q1
results["Q1_B_cohort"] = count(B)
results["Q1_B_by_site"] = B.groupby("SITE_ID")["DX_GROUP"].value_counts().unstack(fill_value=0).rename(columns=dx).to_dict("index")
# Q2
setA, setB, setAt = set(A.FILE_ID), set(B.FILE_ID), set(A_tight.FILE_ID)
excl = sorted(setB - setAt)
results["Q2"] = {
    "A_cohort": count(A), "A_tight_cohort": count(A_tight),
    "overlap_A_B": len(setA & setB), "A_only": len(setA - setB), "B_only": len(setB - setA),
    "overlap_Atight_B": len(setAt & setB),
    "B_excluded_by_tight_QC": count(B[B.FILE_ID.isin(excl)]),
    "B_excluded_by_tight_QC_by_site": B[B.FILE_ID.isin(excl)]["SITE_ID"].value_counts().to_dict(),
    "B_excluded_by_original_A_QC": len(setB - setA),
    "sweep_B_excluded": {str(t): int((B["func_mean_fd"] >= t).sum()) for t in [0.2, 0.15, 0.1, 0.08, 0.05]},
}
# Q3 example (gold FILE_ID unknown to this arm): first B participant
ex_fid = sorted(setB)[0]
results["Q3_example"] = {
    "FILE_ID": ex_fid, "row": B[B.FILE_ID == ex_fid].iloc[0].to_dict(),
    "cc200_url": ROI_URL.format(fid=ex_fid),
    "cc200_shape": list(loaded[ex_fid].shape),
}

# connectivity analyses (Q5/Q6) exclude subjects whose CC200 file has any constant ROI (partial coverage);
# Q1/Q2 cohort counts above are unaffected. All 200 ROIs are kept.
const = {f for f in pheno.FILE_ID if (loaded[f].std(0) < 1e-8).any()}
results["connectivity_exclusions"] = {"rule": "any CC200 ROI with zero variance", "n_in_A": len(setA & const),
                                      "n_in_A_tight": len(setAt & const), "n_in_B": len(setB & const)}
A, A_tight, B = (d[~d.FILE_ID.isin(const)].copy() for d in (A, A_tight, B))


# connectivity
def corr_z(ts):
    c = np.corrcoef(ts.T)
    iu = np.triu_indices_from(c, 1)
    return np.arctanh(np.clip(c[iu], -0.999999, 0.999999))


def edgewise(d):
    """OLS per edge: z ~ DX + age + sex + FD + site; returns t for ASD-TC, p, BH mask."""
    Z = np.vstack([corr_z(loaded[f]) for f in d.FILE_ID])
    X = pd.get_dummies(d["SITE_ID"], drop_first=True, dtype=float)
    X.insert(0, "dx", (d["DX_GROUP"] == 1).astype(float).values)
    X.insert(1, "age", d["AGE_AT_SCAN"].values)
    X.insert(2, "sex", d["SEX"].values.astype(float))
    X.insert(3, "fd", d["func_mean_fd"].values)
    X.insert(0, "icpt", 1.0)
    Xm = X.values
    beta, *_ = np.linalg.lstsq(Xm, Z, rcond=None)
    resid = Z - Xm @ beta
    dof = Xm.shape[0] - np.linalg.matrix_rank(Xm)
    s2 = (resid ** 2).sum(0) / dof
    cov = np.linalg.pinv(Xm.T @ Xm)[1, 1]
    t = beta[1] / np.sqrt(s2 * cov)
    p = 2 * stats.t.sf(np.abs(t), dof)
    q = stats.false_discovery_control(p)
    return t, p, q < 0.05


def group_summary(d):
    t, p, sig = edgewise(d)
    return {"n": count(d), "n_edges": int(t.size), "n_fdr_sig": int(sig.sum()),
            "n_sig_ASD_gt_TC": int((sig & (t > 0)).sum()), "n_sig_ASD_lt_TC": int((sig & (t < 0)).sum()),
            "min_p": float(p.min())}, t, sig


resA, tA, sigA = group_summary(A)
resAt, tAt, sigAt = group_summary(A_tight)
results["A_group_effect"] = resA
results["A_tight_group_effect"] = resAt
results["A_vs_A_tight_sig_edge_overlap"] = int((sigA & sigAt).sum())


def _fold(d, s):
    tr, te = d[d.SITE_ID != s], d[d.SITE_ID == s]
    cm = ConnectivityMeasure(kind="tangent", vectorize=True, discard_diagonal=True)
    Xtr = cm.fit_transform([loaded[f] for f in tr.FILE_ID])
    Xte = cm.transform([loaded[f] for f in te.FILE_ID])
    clf = make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=2000))
    clf.fit(Xtr, tr.DX_GROUP.values)
    return s, {"n_test": int(len(te)), "accuracy": round(float((clf.predict(Xte) == te.DX_GROUP.values).mean()), 4)}


def loso(d):
    """Leave-one-site-out tangent + l2 logistic; per-site accuracy."""
    sites = [s for s in sorted(d.SITE_ID.unique()) if (d.SITE_ID == s).any()]
    out = dict(Parallel(n_jobs=int(os.environ.get("N_JOBS", "4")))(delayed(_fold)(d, s) for s in sites))
    accs = [v["accuracy"] for v in out.values()]
    ns = [v["n_test"] for v in out.values()]
    return {"per_site": out, "mean_site_accuracy": round(float(np.mean(accs)), 4),
            "pooled_accuracy": round(float(np.average(accs, weights=ns)), 4)}


B_rev = B[~B.FILE_ID.isin(excl)].copy()
results["B_original"] = loso(B)
results["B_revised_tightQC"] = loso(B_rev)
# Q5: which per-site results must be reassessed (test set touched) and which changed
reassess = sorted(B[B.FILE_ID.isin(excl)].SITE_ID.unique())
changed = {s: {"before": results["B_original"]["per_site"][s]["accuracy"],
               "after": results["B_revised_tightQC"]["per_site"].get(s, {}).get("accuracy")}
           for s in results["B_original"]["per_site"]
           if results["B_original"]["per_site"][s]["accuracy"] != results["B_revised_tightQC"]["per_site"].get(s, {}).get("accuracy")}
results["Q5"] = {"sites_with_test_participants_excluded": reassess,
                 "note": "every fold's training set loses excluded participants, so every per-site result and the aggregate are in scope for reassessment",
                 "sites_whose_accuracy_changed": changed,
                 "aggregate_before_after": [results["B_original"]["mean_site_accuracy"], results["B_revised_tightQC"]["mean_site_accuracy"]]}

# Q6: A's effect derived without the held-out site, tested in that site's B participants
q6 = {}
for s in sorted(B.SITE_ID.unique()):
    tr = A[A.SITE_ID != s]
    t_tr, _, sig_tr = edgewise(tr)
    te = B[B.SITE_ID == s]
    if sig_tr.sum() == 0 or te.DX_GROUP.nunique() < 2:
        q6[s] = {"n_sig_train": int(sig_tr.sum()), "skipped": True}
        continue
    Zte = np.vstack([corr_z(loaded[f]) for f in te.FILE_ID])[:, sig_tr]
    asd, tc = te.DX_GROUP.values == 1, te.DX_GROUP.values == 2
    diff = Zte[asd].mean(0) - Zte[tc].mean(0)
    agree = float((np.sign(diff) == np.sign(t_tr[sig_tr])).mean())
    score = Zte @ np.sign(t_tr[sig_tr]) / sig_tr.sum()  # signed composite: higher = more ASD-like
    tt = stats.ttest_ind(score[asd], score[tc], equal_var=False)
    q6[s] = {"n_test": int(len(te)), "n_sig_train": int(sig_tr.sum()), "sign_agreement": round(agree, 3),
             "composite_t": round(float(tt.statistic), 3), "composite_p": float(tt.pvalue)}
valid = [v for v in q6.values() if not v.get("skipped")]
results["Q6"] = {"per_site": q6,
                 "n_sites_tested": len(valid),
                 "n_sites_composite_p_lt_05_same_direction": int(sum(v["composite_p"] < 0.05 and v["composite_t"] > 0 for v in valid)),
                 "n_sites_composite_t_positive": int(sum(v["composite_t"] > 0 for v in valid)),
                 "median_sign_agreement": float(np.median([v["sign_agreement"] for v in valid])) if valid else None}

with open(os.path.join(OUT, "results.json"), "w") as f:
    json.dump(results, f, indent=1, default=str)
print("DONE", json.dumps({k: results[k] for k in ["Q1_B_cohort", "Q2"]}, default=str)[:2000])
