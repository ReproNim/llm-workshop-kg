"""Step 6: slide figures (16:9, 1920 px wide at 144 dpi; text >= 16 pt) -> figures/*.png + *.svg."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch
from common import ROOT

SYN = json.load(open(ROOT / "results_synthesis.json"))
SP = json.load(open(ROOT / "search_provenance.json"))
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df"
BLUE, ORANGE, GRAY = "#2a78d6", "#eb6834", "#6f6e69"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 18, "svg.fonttype": "none",
                     "axes.edgecolor": MUTED, "text.color": INK, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2})
W, H, DPI = 13.333, 7.5, 144


def save(fig, name):
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"{name}.{ext}", dpi=DPI, facecolor="white")
    plt.close(fig)


def prisma():
    s = SYN["screening"]
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

    def box(x, y, w, h, text, fc="white", ec=MUTED, bold=False, size=17, color=INK):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=fc, ec=ec, lw=1.5))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, color=color,
                fontweight="bold" if bold else "normal", linespacing=1.25)

    def arrow(x1, y1, x2, y2):
        ax.annotate("", (x2, y2), (x1, y1), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.6, mutation_scale=18))

    ax.text(2, 95, "Which ABIDE papers were read", fontsize=26, fontweight="bold", va="center")
    ax.text(2, 88.5, "OpenAlex citation searches, 15 Oct 2026; open-access full texts only", fontsize=17, color=INK2, va="center")
    rows = [72, 59, 46, 33, 20, 6]
    h, mx, mw, sx, sw = 9, 3, 44, 56, 41
    nr = SP["not_retrieved_reasons"]
    main = [
        f"Records identified: {SP['total_identified']}\n(cite ABIDE I/II descriptor or Abraham 2017)",
        f"After duplicates removed: {SP['records_screened']}",
        f"Open-access primary records: {SP['records_screened'] - SP['records_excluded_title_abstract']}",
        f"Full texts sought: {SP['reports_sought']}",
        f"Assessed for eligibility: {s['assessed_for_eligibility']}\n({s['assessed_on']['full_text']} full text, {s['assessed_on']['abstract_only']} abstract only)",
        f"Included: {s['included']}",
    ]
    ex3 = s["excluded_reasons"]
    side = [
        (f"Duplicates: {SP['duplicates_removed']}", rows[0]),
        (f"Excluded on metadata: {SP['records_excluded_title_abstract']}\n(310 not open access, 4 not primary)", rows[1]),
        (f"Not sought: {SP['records_screened'] - SP['records_excluded_title_abstract'] - SP['reports_sought']}\n(outside top 200 by citations)", rows[2]),
        (f"Not retrieved: {SP['reports_not_retrieved']}\n(no OA PDF, bot-check pages, PMC blocked)", rows[3]),
        (f"Excluded: {s['excluded']}\n({list(ex3.values())[0]} no rs-fMRI analysis, {list(ex3.values())[1]} benchmark only)", rows[4]),
    ]
    for i, (t, y) in enumerate(zip(main, rows)):
        last = i == len(main) - 1
        box(mx, y, mw, h, t, fc="#eaf2fc" if last else "white", ec=BLUE if last else MUTED, bold=last, size=19 if last else 17)
        if i:
            arrow(mx + mw / 2, rows[i - 1], mx + mw / 2, y + h + 0.6)
    for t, y in side:
        box(sx, y, sw, h, t, color=INK2, size=16)
        arrow(mx + mw + 0.6, y + h / 2, sx - 0.6, y + h / 2)
    ct = SYN["claim_type"]
    ax.text(sx, rows[5] + h / 2, f"{ct['predictive']} predictive · {ct['both']} predictive + group difference\n"
            f"{ct['associational']} group difference · {ct['descriptor']} data descriptor",
            fontsize=17, color=INK2, va="center")
    save(fig, "prisma_flow")


def accuracy():
    ev = SYN["evaluation"]
    order = ["pooled k-fold CV", "single train/test split", "leave-one-subject-out CV", "within-site only",
             "external dataset", "leave-site-out"]
    labels = {"pooled k-fold CV": "Pooled k-fold CV\n(sites mixed)", "single train/test split": "Single\ntrain/test split",
              "leave-one-subject-out CV": "Leave-one-\nsubject-out", "within-site only": "Within one site",
              "external dataset": "External\ndataset", "leave-site-out": "Leave-site-out"}
    rows = [r for r in ev["accuracy_rows"] if r["scheme"] in order]
    fig, ax = plt.subplots(figsize=(W, H))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.78, bottom=0.22)
    ax.axvspan(len(order) - 1.5, len(order) - 0.5, color="#eaf2fc", zorder=0)
    pos = {}
    for i, sch in enumerate(order):
        pts = sorted([r for r in rows if r["scheme"] == sch], key=lambda r: r["accuracy_pct"])
        n = len(pts)
        for j, r in enumerate(pts):
            x = i + (j - (n - 1) / 2) * min(0.12, 0.6 / max(n - 1, 1))
            pos[(r["source_id"], sch)] = (x, r["accuracy_pct"])
            lso = sch == "leave-site-out"
            if r["leakage_flag"]:
                ax.scatter(x, r["accuracy_pct"], s=150, marker="o", facecolor="white", edgecolor=ORANGE, lw=2.6, zorder=4)
            else:
                ax.scatter(x, r["accuracy_pct"], s=150 if lso else 110, color=BLUE if lso else GRAY,
                           edgecolor="white", lw=1.5, zorder=4)
        if n:
            vals = sorted(r["accuracy_pct"] for r in pts)
            med = vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2
            ax.plot([i - 0.32, i + 0.32], [med, med], color=BLUE if sch == "leave-site-out" else INK, lw=2.5, zorder=3)
            ax.text(i + 0.36, med, f"{med:.0f}%", va="center", fontsize=16, color=INK)
    for sid in ("S-030", "S-072"):
        a, b = pos.get((sid, "pooled k-fold CV")), pos.get((sid, "leave-site-out"))
        if a and b:
            ax.annotate(f"{sid}: {a[1]:.0f}% pooled", (b[0], b[1]), xytext=(-14, 0), textcoords="offset points",
                        ha="right", va="center", fontsize=14, color=INK2)
    ax.set_xticks(range(len(order)))
    ax.set_xticklabels([f"{labels[s]}\nn={sum(1 for r in rows if r['scheme'] == s)}" for s in order], fontsize=16)
    ax.set_xlim(-0.6, len(order) - 0.4)
    ax.set_ylim(50, 100)
    ax.set_ylabel("Best reported accuracy (%)", fontsize=18)
    ax.yaxis.grid(True, color=GRID, lw=1); ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="y", labelsize=16)
    fig.text(0.08, 0.93, "Reported ABIDE accuracy is lower when whole sites are held out", fontsize=23, fontweight="bold")
    p, l = ev["accuracy_by_scheme"]["pooled k-fold CV"], ev["accuracy_by_scheme"]["leave-site-out"]
    fig.text(0.08, 0.855, f"{len(set(r['source_id'] for r in rows))} prediction papers, one dot per paper per scheme (best reported result).\nMedian {p['median']:.0f}% with sites mixed "
             f"(n={p['n_papers_with_accuracy']}), {l['median']:.0f}% with whole sites held out (n={l['n_papers_with_accuracy']}).", fontsize=16, color=INK2, va="center")
    handles = [Line2D([], [], marker="o", ls="", color=GRAY, markersize=11, label="Paper"),
               Line2D([], [], marker="o", ls="", color=BLUE, markersize=12, label="Leave-site-out"),
               Line2D([], [], marker="o", ls="", markerfacecolor="white", markeredgecolor=ORANGE, markeredgewidth=2.4,
                      markersize=12, label="Leakage flagged"),
               Line2D([], [], color=INK, lw=2.5, label="Median")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=4, frameon=False, fontsize=16,
              handletextpad=0.4, columnspacing=1.4)
    fig.text(0.98, 0.012, "Different papers, subsets and models: descriptive, not a controlled comparison. "
             "Two values are balanced accuracy.", ha="right", fontsize=14, color=MUTED)
    save(fig, "accuracy_by_evaluation")


if __name__ == "__main__":
    prisma()
    accuracy()
    print(sorted(p.name for p in OUT.iterdir()))
