"""Cross-review between the two illustrative analysts.

A reviews B: do B's most heavily weighted correlation edges overlap A's FDR-significant edges more
than chance (hypergeometric), and do their signs agree?
B reviews A: in each of B's held-out sites, does A's hypoconnectivity signature (mean Fisher z over
A's FDR-significant hypo edges) separate ASD from TD among participants NOT in A's cohort?

Usage: uv run python code/reviews.py v1
"""

import json
import sys

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from common import DERIVED, RESULTS, base_table, connectivity, write_json

TOP_FRACTION = 0.01


def cohen_d(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    """Cohen's d (a minus b) and its large-sample standard error."""
    na, nb = len(a), len(b)
    sp = np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
    d = (a.mean() - b.mean()) / sp
    return float(d), float(np.sqrt((na + nb) / (na * nb) + d**2 / (2 * (na + nb))))


def run(rule: str) -> dict:
    """Write results/reviews_<rule>.json."""
    a = json.loads((RESULTS / f"analyst_a_{rule}.json").read_text())
    b = json.loads((RESULTS / f"analyst_b_{rule}.json").read_text())
    edges = np.load(DERIVED / f"analyst_a_{rule}_edges.npz")
    sig, t = edges["sig"], edges["t"]
    hypo = sig & (t < 0)
    Xc, fids = connectivity()
    idx = pd.Series(range(len(fids)), index=fids)
    d = base_table().set_index("FILE_ID")

    sub_b = d.loc[b["members"]]
    Xb = Xc[idx[b["members"]].to_numpy()].astype(float)
    yb = (sub_b.dx == "ASD").to_numpy(int)
    clf = make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=5000)).fit(Xb, yb)
    coef = clf[-1].coef_[0]
    k = int(round(TOP_FRACTION * len(coef)))
    top = np.argsort(-np.abs(coef))[:k]
    overlap = int(sig[top].sum())
    expected = k * sig.mean()
    p_hyper = float(stats.hypergeom.sf(overlap - 1, len(sig), int(sig.sum()), k))
    shared = top[sig[top]]
    sign_agree = int((np.sign(coef[shared]) == np.sign(t[shared])).sum())
    a_review = {
        "reviewer": "Analyst A (illustrative)",
        "target": f"analyst_b_{rule} correlation model",
        "evidence": [f"analyst_a_{rule}.json FDR-significant edges", f"L2 logistic coefficients refit on all B_{rule} participants"],
        "top_k_edges": k,
        "overlap_with_A_significant": overlap,
        "expected_overlap_if_independent": float(expected),
        "hypergeometric_p": p_hyper,
        "sign_agreement_in_overlap": [sign_agree, len(shared)],
        "verdict": "overlap exceeds chance" if p_hyper < 0.05 else "overlap not above chance",
        "caveat": "Predictive weights in a multivariate model are not edgewise effects; overlap is a consistency check, not validation.",
    }

    sig_score = Xc[:, hypo].mean(1) if hypo.any() else np.zeros(len(fids))
    global_mean = Xc.mean(1)
    a_members = set(a["members"])
    per_site = []
    for fold in b["folds"]:
        s = fold["held_out_site"]
        ids = [f for f in b["members"] if d.at[f, "SITE_ID"] == s and f not in a_members]
        grp = d.loc[ids, "dx"].to_numpy()
        sc = sig_score[idx[ids].to_numpy()] if ids else np.array([])
        n_asd, n_td = int((grp == "ASD").sum()), int((grp == "TD").sum())
        rec = {"site": s, "n_independent_ASD": n_asd, "n_independent_TD": n_td, "in_A_cohort_site": s in a["sites"]}
        if n_asd >= 2 and n_td >= 2:
            rec["d"], rec["se"] = cohen_d(sc[grp == "ASD"], sc[grp == "TD"])
        per_site.append(rec)
    usable = [r for r in per_site if "d" in r]
    w = np.array([1 / r["se"] ** 2 for r in usable])
    dv = np.array([r["d"] for r in usable])
    pooled = float((w * dv).sum() / w.sum())
    pooled_se = float(np.sqrt(1 / w.sum()))
    ci = [pooled - 1.96 * pooled_se, pooled + 1.96 * pooled_se]
    held_ids = [f for f in b["members"] if f not in a_members]
    hid = idx[held_ids].to_numpy()
    b_review = {
        "reviewer": "Analyst B (illustrative)",
        "target": f"analyst_a_{rule} hypoconnectivity result",
        "evidence": [f"analyst_a_{rule}.json hypo edges", f"B_{rule} participants not in A_{rule}, grouped by held-out site"],
        "n_independent_participants": len(held_ids),
        "n_sites_usable": len(usable),
        "n_sites_direction_consistent": int((dv < 0).sum()),
        "pooled_d_fixed_effect": pooled,
        "pooled_d_95ci": ci,
        "per_site": per_site,
        "signature_vs_global_mean_connectivity_r": float(np.corrcoef(sig_score[hid], global_mean[hid])[0, 1]),
        "verdict": "direction holds in independent participants" if ci[1] < 0 else "not established in independent participants",
        "caveat": "Signature is dominated by whole-brain mean connectivity when the correlation is high; no global signal regression in filt_noglobal.",
    }
    out = {"motion_rule": rule, "A_reviews_B": a_review, "B_reviews_A": b_review}
    write_json(f"reviews_{rule}.json", out)
    return out


if __name__ == "__main__":
    o = run(sys.argv[1] if len(sys.argv) > 1 else "v1")
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "per_site"} for k, v in o.items() if isinstance(v, dict)}, indent=1))
