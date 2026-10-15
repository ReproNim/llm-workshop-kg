"""Analyst A: edgewise diagnosis contrast in CC200 Fisher-z connectivity.

Model per edge: z ~ DX + age + FIQ + mean FD + site (males only, so no sex term). Two-sided t-test on
the DX coefficient, Benjamini-Hochberg FDR q < 0.05. Participant bootstrap for the hypo/hyper
balance among FDR-significant edges.

Usage: uv run python code/analyst_a.py v1
"""

import sys

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

from common import DERIVED, SEED, base_table, cohort_a, connectivity, edge_index, roi_hemisphere, write_json

N_BOOT = 200
Q = 0.05


def design(sub: pd.DataFrame) -> np.ndarray:
    """Design matrix: intercept, ASD indicator, centred age, FIQ, mean FD, site dummies."""
    cols = [np.ones(len(sub)), (sub.dx == "ASD").astype(float)]
    for c in ("AGE_AT_SCAN", "FIQ", "func_mean_fd"):
        v = sub[c].to_numpy(float)
        cols.append(v - v.mean())
    sites = pd.get_dummies(sub.SITE_ID, drop_first=True).to_numpy(float)
    return np.column_stack(cols + [sites])


def dx_tstats(X: np.ndarray, Y: np.ndarray) -> tuple[np.ndarray, np.ndarray, int]:
    """OLS DX coefficient and t statistic for every column of Y."""
    xtx_inv = np.linalg.inv(X.T @ X)
    beta = xtx_inv @ X.T @ Y
    resid = Y - X @ beta
    dof = X.shape[0] - X.shape[1]
    sigma2 = (resid**2).sum(0) / dof
    se = np.sqrt(sigma2 * xtx_inv[1, 1])
    return beta[1], beta[1] / se, dof


def run(rule: str) -> dict:
    """Fit the edgewise model on cohort A under a motion rule and write results."""
    d = base_table()
    sub = d[cohort_a(d, rule)].sort_values("FILE_ID").reset_index(drop=True)
    Xc, fids = connectivity()
    idx = pd.Series(range(len(fids)), index=fids)
    Y = Xc[idx[sub.FILE_ID].to_numpy()].astype(float)
    X = design(sub)
    beta, t, dof = dx_tstats(X, Y)
    p = 2 * stats.t.sf(np.abs(t), dof)
    sig = multipletests(p, alpha=Q, method="fdr_bh")[0]
    hypo, hyper = sig & (t < 0), sig & (t > 0)
    d_eff = 2 * t / np.sqrt(dof)
    hemi = roi_hemisphere()
    i, j = edge_index()
    inter = hemi[i] != hemi[j]
    rng = np.random.default_rng(SEED)
    frac = []
    for _ in range(N_BOOT):
        b = rng.choice(len(sub), len(sub), replace=True)
        Xb = design(sub.iloc[b].reset_index(drop=True))
        if np.linalg.matrix_rank(Xb) < Xb.shape[1]:
            continue
        _, tb, dofb = dx_tstats(Xb, Y[b])
        sb = multipletests(2 * stats.t.sf(np.abs(tb), dofb), alpha=Q, method="fdr_bh")[0]
        if sb.sum():
            frac.append(float((sb & (tb < 0)).sum() / sb.sum()))
    np.savez_compressed(DERIVED / f"analyst_a_{rule}_edges.npz", beta=beta, t=t, p=p, sig=sig)
    out = {
        "analyst": "A (illustrative)",
        "motion_rule": rule,
        "n": len(sub),
        "by_dx": sub.dx.value_counts().to_dict(),
        "sites": sorted(sub.SITE_ID.unique()),
        "model": "z_edge ~ ASD + age + FIQ + meanFD + site; OLS; BH-FDR q<0.05",
        "n_edges": int(len(t)),
        "n_fdr_significant": int(sig.sum()),
        "n_hypo": int(hypo.sum()),
        "n_hyper": int(hyper.sum()),
        "hypo_fraction": float(hypo.sum() / max(sig.sum(), 1)),
        "hypo_fraction_bootstrap_95ci": [float(np.percentile(frac, 2.5)), float(np.percentile(frac, 97.5))] if frac else None,
        "n_bootstrap_used": len(frac),
        "interhemispheric_fraction_all_edges": float(inter.mean()),
        "interhemispheric_fraction_hypo_edges": float(inter[hypo].mean()) if hypo.any() else None,
        "interhemispheric_fraction_hyper_edges": float(inter[hyper].mean()) if hyper.any() else None,
        "median_abs_d_significant": float(np.median(np.abs(d_eff[sig]))) if sig.any() else None,
        "max_abs_d": float(np.abs(d_eff).max()),
        "members": list(sub.FILE_ID),
    }
    write_json(f"analyst_a_{rule}.json", out)
    return out


if __name__ == "__main__":
    o = run(sys.argv[1] if len(sys.argv) > 1 else "v1")
    print({k: v for k, v in o.items() if k != "members"})
