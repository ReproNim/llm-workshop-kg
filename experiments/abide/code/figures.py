"""Slide figures from the results JSONs (PNG + PDF in figures/).

Usage: uv run python code/figures.py
"""

import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from common import FIGURES, RESULTS

plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
BLUE, ORANGE, GREY = "#4C72B0", "#DD8452", "#8C8C8C"


def load(name: str) -> dict:
    """Load a results JSON."""
    return json.loads((RESULTS / name).read_text())


def save(fig, stem: str) -> None:
    """Write PNG and PDF."""
    for ext in ("png", "pdf"):
        fig.savefig(FIGURES / f"{stem}.{ext}", dpi=170, bbox_inches="tight")
    plt.close(fig)


def cohort_flow() -> None:
    """Horizontal bars: how each criterion narrows the sample, for both analysts and both rules."""
    c = load("cohorts.json")
    rows = [
        ("Phenotype rows", c["phenotype_rows"]),
        ("CC200 time series available", c["with_timeseries"]["n"]),
        ("All 200 ROIs have signal", c["full_roi_coverage"]["n"]),
        ("+ three-rater visual QC (Abraham reconstruction)", c["rater_qc_pass"]["n"]),
        ("B v1: + mean FD < 0.2 mm", c["B_v1"]["n"]),
        ("B v2: + mean FD < 0.15 mm", c["B_v2"]["n"]),
        ("A v1: B v1 ∩ males, FIQ 78-138, ≥10/group/site", c["A_v1"]["n"]),
        ("A v2: same with FD < 0.15 mm", c["A_v2"]["n"]),
    ]
    fig, ax = plt.subplots(figsize=(9, 4.2))
    cols = [GREY] * 4 + [ORANGE, ORANGE, BLUE, BLUE]
    y = np.arange(len(rows))[::-1]
    ax.barh(y, [r[1] for r in rows], color=cols)
    for yi, (lab, n) in zip(y, rows):
        ax.text(n + 8, yi, str(n), va="center", fontsize=10)
    ax.set_yticks(y, [r[0] for r in rows])
    ax.set_xlabel("participants")
    ax.set_xlim(0, 1250)
    ax.set_title("Same dataset, different cohorts: every count is a scoped query")
    save(fig, "cohort_flow")


def b_sites() -> None:
    """Per-site tangent accuracy for v1 and v2 with Wilson intervals, plus pooled AUC by method."""
    b1, b2 = load("analyst_b_v1.json"), load("analyst_b_v2.json")
    f2 = {f["held_out_site"]: f for f in b2["folds"]}
    sites = [f["held_out_site"] for f in b1["folds"]]
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(14, 4.6), gridspec_kw={"width_ratios": [3, 1.2]})
    x = np.arange(len(sites))
    for off, fold_map, col, lab in ((-0.17, {f["held_out_site"]: f for f in b1["folds"]}, ORANGE, "v1 (FD<0.2)"), (0.17, f2, BLUE, "v2 (FD<0.15)")):
        xs, acc, lo, hi = [], [], [], []
        for i, s in enumerate(sites):
            if s in fold_map:
                t = fold_map[s]["tangent"]
                xs.append(i + off)
                acc.append(t["accuracy"])
                lo.append(t["accuracy"] - t["accuracy_95ci"][0])
                hi.append(t["accuracy_95ci"][1] - t["accuracy"])
        ax.errorbar(xs, acc, yerr=[lo, hi], fmt="o", color=col, ms=4, capsize=2, label=lab)
    ax.axhline(0.5, color=GREY, lw=0.8, ls="--")
    ax.set_xticks(x, [f"{s}\n(n={b1['folds'][i]['n_test']})" for i, s in enumerate(sites)], rotation=90, fontsize=8)
    ax.set_ylabel("held-out site accuracy (tangent)")
    ax.set_ylim(0, 1.05)
    ax.legend(frameon=False)
    ax.set_title("Leave-one-site-out: per-site accuracy with 95% intervals")
    methods = ["demographic", "demographic_fd", "correlation", "tangent"]
    labels = ["age+sex", "age+sex+FD", "correlation", "tangent"]
    for off, b, col in ((-0.17, b1, ORANGE), (0.17, b2, BLUE)):
        aucs = [b["pooled"][m]["auc"] for m in methods]
        err = [[b["pooled"][m]["auc"] - b["pooled"][m]["auc_95ci"][0] for m in methods], [b["pooled"][m]["auc_95ci"][1] - b["pooled"][m]["auc"] for m in methods]]
        ax2.errorbar(np.arange(4) + off, aucs, yerr=err, fmt="o", color=col, capsize=3)
    ax2.axhline(0.5, color=GREY, lw=0.8, ls="--")
    ax2.set_xticks(range(4), labels, rotation=30)
    ax2.set_ylabel("pooled out-of-site AUC")
    ax2.set_ylim(0.35, 0.85)
    ax2.set_title("Pooled AUC (bootstrap 95% CI)")
    fig.tight_layout()
    save(fig, "analyst_b_sites")


def review_forest() -> None:
    """B's review of A: per held-out site effect of A's signature in participants not in A's cohort."""
    r = load("reviews_v1.json")["B_reviews_A"]
    rows = [s for s in r["per_site"] if "d" in s]
    fig, ax = plt.subplots(figsize=(6.5, 0.32 * len(rows) + 1.6))
    y = np.arange(len(rows))[::-1]
    for yi, s in zip(y, rows):
        ax.errorbar(s["d"], yi, xerr=1.96 * s["se"], fmt="o", color=BLUE if s["in_A_cohort_site"] else GREY, capsize=2)
    ax.errorbar(r["pooled_d_fixed_effect"], -1.2, xerr=[[r["pooled_d_fixed_effect"] - r["pooled_d_95ci"][0]], [r["pooled_d_95ci"][1] - r["pooled_d_fixed_effect"]]], fmt="D", color=ORANGE, capsize=3)
    ax.axvline(0, color=GREY, lw=0.8)
    ax.set_yticks(list(y) + [-1.2], [f"{s['site']} ({s['n_independent_ASD']}+{s['n_independent_TD']})" for s in rows] + ["pooled"])
    ax.set_xlabel("Cohen's d, ASD − TD, A's hypoconnectivity signature")
    ax.set_title(f"B reviews A on {r['n_independent_participants']} participants A never used\nblue: site also in A's cohort; grey: site new to A", fontsize=10)
    save(fig, "review_b_of_a_forest")


def revision() -> None:
    """Flagged by traversal vs materially changed after recomputation."""
    fl, im = load("revision_flags.json"), load("revision_impact.json")
    kinds = fl["flagged_by_kind"]
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(11, 3.8), gridspec_kw={"width_ratios": [1.2, 1]})
    names = ["fold_result", "pooled_result", "result", "claim_or_review"]
    ax.bar(range(4), [kinds.get(n, 0) for n in names], color=ORANGE)
    for i, n in enumerate(names):
        ax.text(i, kinds.get(n, 0) + 1, str(kinds.get(n, 0)), ha="center")
    ax.set_xticks(range(4), ["per-fold\nresults", "pooled\nresults", "A's\nresult", "claims &\nreviews"])
    ax.set_title(f"Flagged by graph traversal\n(all {fl['n_folds_total']} folds trained on an affected participant)", fontsize=10)
    ch = im["changes"]
    keys = list(ch)
    ax2.barh(range(len(keys))[::-1], [1] * len(keys), color=[ORANGE if ch[k]["material"] else "#DDDDDD" for k in keys])
    ax2.set_yticks(range(len(keys))[::-1], keys, fontsize=8)
    ax2.set_xticks([])
    ax2.set_title(f"Measured after recompute: {im['n_material_changes']} of {len(keys)} changed materially", fontsize=10)
    fig.tight_layout()
    save(fig, "revision_flagged_vs_changed")


def resource_map() -> None:
    """Resources as chips, one row per primary workflow step, coloured by days since last default-branch commit."""
    import datetime as dt

    from matplotlib.patches import FancyBboxPatch

    from find_resources import Q_LATEST, store
    from resources_catalog import R, STEPS

    st = store()
    latest = {r["r"].value.rsplit("/", 1)[-1]: r for r in st.query(Q_LATEST, use_default_graph_as_union=True)}
    steps = [x for x in STEPS if any(r["steps"][0] == x for r in R)]
    cmap = plt.get_cmap("viridis_r")
    edge = {"executed": ("#C0392B", 2.4), "data_source": ("#E67E22", 2.0), "pointer": ("#333333", 0.6)}
    per_row, w, h = 7, 1.0, 0.8
    rows = []
    for step in steps:
        rs = [r for r in R if r["steps"][0] == step]
        for i in range(0, len(rs), per_row):
            rows.append((step if i == 0 else "", rs[i:i + per_row]))
    fig, ax = plt.subplots(figsize=(16, 0.42 * len(rows) + 1.4))
    as_of = None
    for yi, (label, rs) in enumerate(rows):
        y = -yi
        ax.text(-0.15, y, label.replace("_", " "), ha="right", va="center", fontsize=9, weight="bold")
        for xi, r in enumerate(rs):
            a = latest.get(r["id"])
            days = None
            if a is not None:
                t = dt.datetime.fromisoformat(a["t"].value)
                as_of = t
                ref = a["lastCommit"] or a["push"]
                if ref is not None:
                    days = (t - dt.datetime.fromisoformat(ref.value.replace("Z", "+00:00"))).days
            col = cmap(min(days, 730) / 730) if days is not None else "#DDDDDD"
            ec, lw = edge[r["usage"]]
            ax.add_patch(FancyBboxPatch((xi * w * 1.05, y - h / 2 * 0.8), w, h * 0.8, boxstyle="round,pad=0.01,rounding_size=0.08",
                                        facecolor=col, edgecolor=ec, linewidth=lw))
            dark = days is not None and days > 300
            ax.text(xi * w * 1.05 + w / 2, y, r["name"][:24], ha="center", va="center", fontsize=6.8, color="white" if dark else "black")
    ax.set_xlim(-2.4, per_row * w * 1.05)
    ax.set_ylim(-len(rows) + 0.4, 0.6)
    ax.axis("off")
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 730))
    fig.colorbar(sm, ax=ax, label="days since last default-branch commit (grey: no repository)", fraction=0.02, pad=0.01)
    for k, (ec, lw) in edge.items():
        ax.plot([], [], "s", markerfacecolor="white", markeredgecolor=ec, markeredgewidth=lw, markersize=10, label=f"{k.replace('_', ' ')} here")
    ax.legend(frameon=False, loc="lower right", fontsize=8, ncol=3, bbox_to_anchor=(1.0, -0.06))
    ax.set_title(f"{len(R)} resources by primary workflow step; activity snapshot {as_of:%Y-%m-%d %H:%M} UTC", fontsize=11)
    save(fig, "resource_map")


if __name__ == "__main__":
    resource_map()
    cohort_flow()
    b_sites()
    review_forest()
    revision()
    print(sorted(p.name for p in FIGURES.iterdir()))
