"""Analyst B: ASD vs TD classification with leave-one-site-out cross-validation.

Feature sets: demographic baseline (age, sex), nuisance baseline (age, sex, mean FD), CC200
correlation (Fisher z), CC200 tangent embedding (fit on training fold only). Classifier:
StandardScaler + L2 logistic regression (C=1), all fitted inside each training fold.

Usage: uv run python code/analyst_b.py v1
"""

import sys

import numpy as np
import pandas as pd
from nilearn.connectome import ConnectivityMeasure
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from common import DERIVED, SEED, base_table, cohort_b, connectivity, load_timeseries, write_json

N_BOOT = 1000
METHODS = ("demographic", "demographic_fd", "correlation", "tangent")


def wilson(k: int, n: int, z: float = 1.96) -> list[float]:
    """Wilson score interval for a proportion."""
    if n == 0:
        return [float("nan"), float("nan")]
    p = k / n
    den = 1 + z**2 / n
    c = (p + z**2 / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / den
    return [float(c - h), float(c + h)]


def model() -> object:
    """Classifier used for every feature set."""
    return make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=5000))


def fold_features(method, sub, train, test, corr, ts):
    """Return train/test matrices for one method, fitting any embedding on the training fold."""
    if method == "demographic":
        F = sub[["AGE_AT_SCAN", "SEX"]].to_numpy(float)
        return F[train], F[test]
    if method == "demographic_fd":
        F = sub[["AGE_AT_SCAN", "SEX", "func_mean_fd"]].to_numpy(float)
        return F[train], F[test]
    if method == "correlation":
        return corr[train], corr[test]
    cm = ConnectivityMeasure(kind="tangent", vectorize=True, discard_diagonal=True)
    tr = cm.fit_transform([ts[i] for i in train])
    test_ts = [ts[i] for i in test]
    te = cm.transform(test_ts + test_ts[:1] if len(test_ts) == 1 else test_ts)[: len(test_ts)]
    return tr, te


def run(rule: str) -> dict:
    """Leave-one-site-out evaluation of every method on cohort B under a motion rule."""
    d = base_table()
    sub = d[cohort_b(d, rule)].sort_values("FILE_ID").reset_index(drop=True)
    y = (sub.dx == "ASD").to_numpy(int)
    Xc, fids = connectivity()
    idx = pd.Series(range(len(fids)), index=fids)
    corr = Xc[idx[sub.FILE_ID].to_numpy()].astype(float)
    ts = [load_timeseries(f) for f in sub.FILE_ID]
    sites = sorted(sub.SITE_ID.unique())
    oof = {m: np.full(len(sub), np.nan) for m in METHODS}
    folds = []
    for s in sites:
        test = np.flatnonzero(sub.SITE_ID == s)
        train = np.flatnonzero(sub.SITE_ID != s)
        rec = {"held_out_site": s, "n_train": len(train), "n_test": len(test), "test_by_dx": sub.dx.iloc[test].value_counts().to_dict()}
        for m in METHODS:
            tr, te = fold_features(m, sub, train, test, corr, ts)
            clf = model().fit(tr, y[train])
            prob = clf.predict_proba(te)[:, 1]
            oof[m][test] = prob
            k = int(((prob >= 0.5).astype(int) == y[test]).sum())
            rec[m] = {
                "accuracy": k / len(test),
                "accuracy_95ci": wilson(k, len(test)),
                "auc": float(roc_auc_score(y[test], prob)) if len(set(y[test])) == 2 else None,
            }
        folds.append(rec)
        print(s, {m: round(rec[m]["accuracy"], 3) for m in METHODS}, flush=True)
    rng = np.random.default_rng(SEED)
    boots = [rng.choice(len(y), len(y), replace=True) for _ in range(N_BOOT)]
    pooled = {}
    for m in METHODS:
        pred = (oof[m] >= 0.5).astype(int)
        acc = [float((pred[b] == y[b]).mean()) for b in boots]
        auc = [float(roc_auc_score(y[b], oof[m][b])) for b in boots]
        site_acc = [f[m]["accuracy"] for f in folds]
        pooled[m] = {
            "accuracy": float((pred == y).mean()),
            "accuracy_95ci": [float(np.percentile(acc, 2.5)), float(np.percentile(acc, 97.5))],
            "auc": float(roc_auc_score(y, oof[m])),
            "auc_95ci": [float(np.percentile(auc, 2.5)), float(np.percentile(auc, 97.5))],
            "mean_site_accuracy": float(np.mean(site_acc)),
            "sd_site_accuracy": float(np.std(site_acc, ddof=1)),
        }
    diff = [float(roc_auc_score(y[b], oof["tangent"][b]) - roc_auc_score(y[b], oof["demographic_fd"][b])) for b in boots]
    np.savez_compressed(DERIVED / f"analyst_b_{rule}_oof.npz", file_ids=sub.FILE_ID.to_numpy(), y=y, **{m: oof[m] for m in METHODS})
    out = {
        "analyst": "B (illustrative)",
        "motion_rule": rule,
        "n": len(sub),
        "by_dx": sub.dx.value_counts().to_dict(),
        "cv": "leave-one-site-out over SITE_ID",
        "n_folds": len(sites),
        "classifier": "StandardScaler + LogisticRegression(C=1, L2), fit within training fold",
        "pooled": pooled,
        "tangent_minus_demographic_fd_auc": {"point": pooled["tangent"]["auc"] - pooled["demographic_fd"]["auc"], "bootstrap_95ci": [float(np.percentile(diff, 2.5)), float(np.percentile(diff, 97.5))]},
        "folds": folds,
        "members": list(sub.FILE_ID),
    }
    write_json(f"analyst_b_{rule}.json", out)
    return out


if __name__ == "__main__":
    o = run(sys.argv[1] if len(sys.argv) > 1 else "v1")
    print(o["pooled"], o["tangent_minus_demographic_fd_auc"])
