# /// script
# requires-python = ">=3.11"
# dependencies = ["matplotlib>=3.9", "networkx>=3.3", "pandas>=2.2"]
# ///
"""Three slide-specific figures, redrawn for legibility when projected.

Reuses the exact numbers from the packaged ABIDE_Collaboration_Experiment run (read-only
source): results/participant_ego.json, results/element_coverage.json, graph/resources.ttl
and results/resource_activity_log.jsonl (the same catalog + activity snapshot the original
figures/resource_map.png drew from, via code/figures.py:resource_map() and
code/find_resources.py:Q_LATEST). No numbers are recomputed or changed; layout, text size,
node count and panel choice are simplified for a slide rather than a paper figure.

Usage: uv run --with matplotlib --with networkx --with pandas python make_slide_figs.py
"""

import datetime as dt
import json
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch

SRC = Path(__file__).resolve().parents[2] / "experiments" / "abide"
OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)

RESULTS = SRC / "results"
GRAPH = SRC / "graph"

NAVY, TEAL, TERRACOTTA = "#17303F", "#0F7B7B", "#C0562B"
GREY_DARK, GREY_MID, GREY_LIGHT = "#555555", "#999999", "#DDDDDD"

plt.rcParams.update({
    "font.family": "sans-serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "svg.fonttype": "none",
})


def _png_width_px(path: Path) -> int:
    """Width from a PNG's IHDR chunk, no imaging library required."""
    data = path.read_bytes()
    return int.from_bytes(data[16:20], "big")


def save_fixed_canvas(fig, stem: str, width_in: float, height_in: float, dpi: float) -> None:
    """Write a PNG/SVG at an exact pixel canvas (no tight-bbox cropping, no rescaling).

    Used where the caller has already laid the figure out to fit a hard pixel target
    (e.g. 2400x600): bbox_inches="tight" would crop or rescale that deliberate layout.
    """
    fig.set_size_inches(width_in, height_in)
    png_path, svg_path = OUT / f"{stem}.png", OUT / f"{stem}.svg"
    fig.savefig(png_path, dpi=dpi, facecolor="white")
    fig.savefig(svg_path, dpi=dpi, facecolor="white")
    w, h = _png_width_px(png_path), None
    data = png_path.read_bytes()
    h = int.from_bytes(data[20:24], "big")
    assert (w, h) == (round(width_in * dpi), round(height_in * dpi)), (w, h)
    plt.close(fig)


def _check_text_artists(fig, dpi: float, width_px: int, height_px: int) -> list[str]:
    """Pixel-bounds + pairwise-overlap check for every Text artist, for a hard-canvas figure.

    dpi > 0 sets the figure to that dpi before measuring, so bbox pixels are commensurate with
    width_px/height_px (a figure's default dpi is 100; checking at 100 while comparing against a
    e.g. 218dpi target silently passes clipping that only shows up at the real resolution).
    dpi == 0 means "bounds don't apply yet" (e.g. a tight-bbox figure not pinned to a final size);
    callers in that mode filter this function's output down to the OVERLAP lines only.
    """
    if dpi:
        fig.set_dpi(dpi)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    boxes = []
    for ax in fig.axes:
        texts = ax.texts + list(ax.get_xticklabels()) + list(ax.get_yticklabels())
        texts += [ax.xaxis.label, ax.yaxis.label, ax.title]  # set_xlabel/set_ylabel/set_title live here, not in ax.texts
        for t in texts:
            if not t.get_text() or not t.get_visible():
                continue
            bb = t.get_window_extent(renderer)
            boxes.append((t.get_text(), bb.x0, bb.y0, bb.x1, bb.y1))
    for t in fig.texts:
        if not t.get_text() or not t.get_visible():
            continue
        bb = t.get_window_extent(renderer)
        boxes.append((t.get_text(), bb.x0, bb.y0, bb.x1, bb.y1))
    # legend entries, their colour-swatch handles, and the legend's own frame/box too - a legend
    # that is wide enough can clip at a handle or at its outer box before any single text label
    # bbox would show it.
    for leg in fig.legends + [a.get_legend() for a in fig.axes if a.get_legend()]:
        for t in leg.get_texts():
            if not t.get_visible():
                continue
            bb = t.get_window_extent(renderer)
            boxes.append((t.get_text(), bb.x0, bb.y0, bb.x1, bb.y1))
    # The legend's own outer box and its colour-swatch handles are checked for canvas bounds
    # only, separately from `boxes`: the box necessarily contains its own text/handles, and each
    # handle sits deliberately flush against its own label (handletextpad), so pairwise-overlap
    # checking either against the rest of `boxes` produces nothing but expected false positives.
    bounds_only = []
    for leg in fig.legends + [a.get_legend() for a in fig.axes if a.get_legend()]:
        bb = leg.get_window_extent(renderer)
        bounds_only.append(("<legend box>", bb.x0, bb.y0, bb.x1, bb.y1))
        handles = getattr(leg, "legend_handles", None) or getattr(leg, "legendHandles", [])
        for h in handles:
            if h is None or not h.get_visible():
                continue
            bb = h.get_window_extent(renderer)
            bounds_only.append(("<legend handle>", bb.x0, bb.y0, bb.x1, bb.y1))
    problems = []
    for label, x0, y0, x1, y1 in boxes + bounds_only:
        if x0 < -0.5 or y0 < -0.5 or x1 > width_px + 0.5 or y1 > height_px + 0.5:
            problems.append(f"OUT OF CANVAS: {label!r} ({x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f})")
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            la, ax0, ay0, ax1, ay1 = boxes[i]
            lb, bx0, by0, bx1, by1 = boxes[j]
            ox = min(ax1, bx1) - max(ax0, bx0)
            oy = min(ay1, by1) - max(ay0, by0)
            if ox > 1 and oy > 1:
                problems.append(f"OVERLAP: {la!r} x {lb!r} ({ox:.1f}x{oy:.1f}px)")
    return problems


def save(fig, stem: str, width_in: float, target_px: int = 2400) -> None:
    """Write a PNG exactly target_px wide plus a vector SVG, tight, white background.

    bbox_inches="tight" crops to content, so the saved width is not simply width_in * dpi.
    Render once to measure the actual tight width, then re-render at the dpi that hits
    target_px exactly.
    """
    png_path, svg_path = OUT / f"{stem}.png", OUT / f"{stem}.svg"
    dpi = target_px / width_in
    best_dpi, best_err = dpi, None
    for _ in range(12):
        fig.savefig(png_path, dpi=dpi, bbox_inches="tight", pad_inches=0.04, facecolor="white")
        measured = _png_width_px(png_path)
        err = abs(measured - target_px)
        if best_err is None or err < best_err:
            best_dpi, best_err = dpi, err
        if measured == target_px:
            break
        dpi *= target_px / measured
    if best_err:
        fig.savefig(png_path, dpi=best_dpi, bbox_inches="tight", pad_inches=0.04, facecolor="white")
    fig.savefig(svg_path, dpi=best_dpi, bbox_inches="tight", pad_inches=0.04, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 1: participant_ego_slide
# ---------------------------------------------------------------------------

def participant_ego_slide() -> None:
    """Radial summary of one participant: 8 grouped layers with counts, a few example leaves each."""
    d = json.loads((RESULTS / "participant_ego.json").read_text())
    rows = d["rows"]
    pid = d["participant"]
    ph = {r["var"].rsplit("/", 1)[-1]: r["value"] for r in rows["phenotype"]}
    n_phenotype = len(rows["phenotype"])
    n_missing = rows["missing"][0]["n"]
    n_scans = len(rows["scans"])
    n_qc = sum(1 for r in rows["phenotype"] if "qc" in r["var"].lower())
    n_derived = len(rows["derived"])
    vol = {r["tool"]: r["n"] for r in rows["volumes"]}
    tool_name = {"http://stnava.github.io/ANTs/": "ANTs", "http://purl.org/nidash/fsl#": "FSL",
                 "https://surfer.nmr.mgh.harvard.edu/": "FreeSurfer"}
    n_tools = len(vol)
    n_rois = sum(int(v) for v in vol.values())
    n_cohorts = len(rows["cohorts"])
    n_folds_test = len({r["fold"] for r in rows["folds"] if r["role"].startswith("held")})
    n_results = len(rows["results"])

    # 8 layer groups, named for a neuroimaging audience (no raw variable names):
    # (key, colour, short first-hop relation, box label, leaf labels)
    layers = [
        ("phenotype", TEAL, "questionnaires",
         f"Questionnaires and IQ\n{n_phenotype} values",
         [f"age at scan: {ph.get('AGE_AT_SCAN', '?')}", f"full-scale IQ: {ph.get('FIQ', '?')}"]),
        ("scans_qc", TEAL, "acquisition",
         f"Scans and head-motion QC\n{n_scans} scans, {n_qc} QC",
         ["T1w (cloud copy)", "rest BOLD (cloud copy)",
          f"head motion: {float(ph.get('func_mean_fd', 0)):.3f} mm"]),
        ("derivatives", NAVY, "derived",
         f"Derived data\n{n_derived} objects",
         ["200-region time series", "functional connectivity\n(19,900 edges)", "cortical thickness (ANTs)"]),
        ("idps", NAVY, "shared ID",
         f"Brain volumes\n(ANTs, FSL, FreeSurfer)",
         [f"{tool_name.get(t, t)}: {v} ROIs" for t, v in vol.items()]),
        ("cohorts_folds", TERRACOTTA, "cohort / fold",
         f"Cohorts and test folds\n{n_cohorts} cohorts, {n_folds_test} folds",
         ["cohort A_v1", "cohort B_v1", "held out B_v2\n(Munich)"]),
        ("results", TERRACOTTA, "input to",
         f"Results that used it\n{n_results} results\n(A: GLM · B: per-fold)",
         []),
        ("publication", GREY_DARK, "reconstructs",
         "Publication\n1 paper\n(Abraham 2017)",
         []),
        ("scope", GREY_DARK, "scope",
         "Consent: broad sharing ·\npond copy · link to\npublic release",
         ["egress: permitted", "lake: ABIDE Preprocessed"]),
    ]

    g = nx.DiGraph()
    g.add_node("P", kind="center", label=f"Participant\n{pid}\n(ABIDE I, Munich site)", color=NAVY)
    pos = {"P": np.array([0.0, 0.0])}
    n = len(layers)
    r1, r2 = 3.3, 4.8
    jitter_by_m = {1: [1.35], 2: [1.12, 1.26], 3: [1.32, 1.38, 1.46]}
    for i, (key, color, edge_label, box_label, leaves) in enumerate(layers):
        ang = np.pi / 2 - 2 * np.pi * i / n
        lx, ly = r1 * np.cos(ang), r1 * np.sin(ang)
        g.add_node(key, kind="layer", label=box_label, color=color)
        pos[key] = np.array([lx, ly])
        g.add_edge("P", key, label=edge_label)
        m = len(leaves)
        radius_jitter = jitter_by_m.get(m, [1.1] * m)
        for j, leaf in enumerate(leaves):
            spread = 0.34
            leaf_ang = ang + (j - (m - 1) / 2) * spread
            r2j = r2 * radius_jitter[j]
            lid = f"{key}:{j}"
            g.add_node(lid, kind="leaf", label=leaf, color=color)
            pos[lid] = np.array([r2j * np.cos(leaf_ang), r2j * np.sin(leaf_ang)])
            g.add_edge(key, lid, label="")

    fig, ax = plt.subplots(figsize=(7.3, 5.2))
    nx.draw_networkx_edges(g, pos, ax=ax, edge_color="#BBBBBB", arrows=False, width=0.9)
    # Both the centre box and every layer box sit ON the spoke line, so a label placed ON the
    # line (nx's default) ends up under one of them. Nudge each label off-axis (small angular
    # offset at a mid radius) into the open wedge beside its spoke instead.
    # The centre box is now 3 lines tall too, so the two purely-horizontal spokes (derivatives at
    # 0 deg, publication at 180 deg) have a tall box at BOTH ends; give those two extra angular
    # lift to clear both rather than tucking in toward the (no longer thin) centre box.
    radius_frac_override = {"derivatives": 0.48, "publication": 0.48}
    angle_offset_override = {"derivatives": 0.4, "publication": 0.4, "phenotype": 0.1}
    for i, (key, _color, edge_label, _box_label, _leaves) in enumerate(layers):
        if not edge_label:
            continue
        ang = np.pi / 2 - 2 * np.pi * i / n
        label_ang = ang + angle_offset_override.get(key, 0.24)
        frac = radius_frac_override.get(key, 0.5)
        x, y = (r1 * frac) * np.cos(label_ang), (r1 * frac) * np.sin(label_ang)
        ax.text(x, y, edge_label, fontsize=7.6, color="#444444", ha="center", va="center", rotation=0,
                bbox={"boxstyle": "round,pad=0.06", "fc": "white", "ec": "none", "alpha": 0.9}, zorder=5)
    for node, data in g.nodes(data=True):
        x, y = pos[node]
        kind = data["kind"]
        if kind == "center":
            ax.text(x, y, data["label"], ha="center", va="center", fontsize=8.6, color="white", weight="bold",
                    bbox={"boxstyle": "round,pad=0.35", "fc": NAVY, "ec": "none"})
        elif kind == "layer":
            ax.text(x, y, data["label"], ha="center", va="center", fontsize=8.4, color="white", weight="bold",
                    bbox={"boxstyle": "round,pad=0.26", "fc": data["color"], "ec": "black", "lw": 0.5})
        else:
            ax.text(x, y, data["label"], ha="center", va="center", fontsize=8.2, color=GREY_DARK,
                    bbox={"boxstyle": "round,pad=0.2", "fc": "white", "ec": data["color"], "lw": 1.0})
    half_w = 6.3
    half_h = half_w * 5.2 / 7.3
    ax.set_xlim(-half_w, half_w)
    ax.set_ylim(-half_h, half_h)
    ax.axis("off")

    # Canvas size isn't fixed yet here (save() picks the dpi after a tight-bbox crop), so only
    # the pairwise-overlap half of the check applies; bounds are passed as effectively infinite.
    problems = [p for p in _check_text_artists(fig, 0, 10**9, 10**9) if p.startswith("OVERLAP")]
    if problems:
        raise RuntimeError("participant_ego_slide text layout failed verification:\n" + "\n".join(problems))

    save(fig, "participant_ego_slide", width_in=7.3)


# ---------------------------------------------------------------------------
# Figure 2: element_coverage_slide (+ a sites x elements matrix kept as a backup slide)
# ---------------------------------------------------------------------------

ELEMENT_ORDER = ["AGE_AT_SCAN", "FIQ", "VIQ", "PIQ", "ADOS_TOTAL", "SRS_RAW_TOTAL", "func_mean_fd", "CC200_timeseries"]
ELEMENT_PLAIN_LABEL = {
    "AGE_AT_SCAN": "Age at scan",
    "FIQ": "Full-scale IQ",
    "VIQ": "Verbal IQ",
    "PIQ": "Performance IQ",
    "ADOS_TOTAL": "ADOS rating",
    "SRS_RAW_TOTAL": "SRS total",
    "func_mean_fd": "Head motion",
    "CC200_timeseries": "fMRI time series",
}
LIMITING_LABEL = {
    "CC200_timeseries": "time series limits",
    "VIQ": "verbal IQ limits",
    "SRS_RAW_TOTAL": "SRS limits",
}


def _element_site_category_counts() -> dict:
    """{element: {none,rare,partial,high: n_sites}} using the same thresholds as the matrix."""
    d = json.loads((RESULTS / "element_coverage.json").read_text())
    els_all = d["elements"]
    sites = sorted(els_all["AGE_AT_SCAN"]["by_site"])
    site_totals = {s: els_all["AGE_AT_SCAN"]["by_site"][s] for s in sites}
    counts = {}
    for k in ELEMENT_ORDER:
        by_site = els_all[k]["by_site"]
        c = {"none": 0, "rare": 0, "partial": 0, "high": 0}
        for s in sites:
            f = by_site.get(s, 0) / site_totals[s]
            if f <= 0:
                c["none"] += 1
            elif f < 0.10:
                c["rare"] += 1
            elif f < 0.90:
                c["partial"] += 1
            else:
                c["high"] += 1
        counts[k] = c
    return counts, len(sites)


def element_coverage_slide() -> None:
    """Landscape, exact 2400x1070px canvas (the slide's figure area is ~11x4.9in, so fitting by
    height like the matrix version shrinks text to ~4pt - this one is sized to fit by width
    instead). Left: the requirement funnel. Right: one stacked bar per element, segments = number
    of sites (of 20) in each coverage category, grouped Phenotype / Imaging-derived.
    """
    WIDTH_IN = 11.0
    HEIGHT_IN = 1070 / 2400 * WIDTH_IN
    DPI = 2400 / WIDTH_IN
    BODY = 46 * 72 / DPI
    HEAD = 52 * 72 / DPI

    d = json.loads((RESULTS / "element_coverage.json").read_text())
    req = d["analysis_requirements"]
    counts, n_sites_total = _element_site_category_counts()

    cat_order = ["none", "rare", "partial", "high"]
    cat_colors = {"none": GREY_LIGHT, "rare": TERRACOTTA, "partial": NAVY, "high": TEAL}
    cat_names = {"none": "none (0%)", "rare": "rare (<10%)", "partial": "partial (10–90%)", "high": "high (≥90%)"}

    fig = plt.figure(figsize=(WIDTH_IN, HEIGHT_IN))

    # This is a fixed-pixel canvas (no tight-bbox crop), so every margin below is reserved by
    # hand for a specific piece of overflow: y-tick labels and x-labels draw OUTSIDE their axes'
    # box, and at a 46px-floor font size that overflow is wide enough to need real inches, not
    # the few points matplotlib's own default margins assume. The legend lives in its own strip
    # at the very bottom, full figure width, rather than above the (narrower) right panel - a
    # single-row, 4-category legend at this font size is wider than that panel.
    legend_strip = 0.55   # the legend's own row, full figure width
    xlabel_strip = 0.65   # x tick numbers + xlabel, shared by both axes
    top_margin = 0.6      # headroom for "Phenotype" above row 0
    axes_bottom = legend_strip + xlabel_strip
    axes_height = HEIGHT_IN - axes_bottom - top_margin

    left_margin_funnel = 2.35   # room for funnel row labels ("Analyst B inputs", ...)
    funnel_width = 3.05         # the axes itself: bars + the two-line annotation past each bar
    gap = 0.15
    right_label_margin = 2.3    # room for the longest element row label ("fMRI time series")
    right_margin = 0.55         # room for the last x tick label ("20") to overflow past the axes

    # --- LEFT: the requirement funnel (same 4 bars/numbers as the matrix backup slide) ---
    axf = fig.add_axes([left_margin_funnel / WIDTH_IN, axes_bottom / HEIGHT_IN, funnel_width / WIDTH_IN,
                       axes_height / HEIGHT_IN])
    funnel = [
        ("All participants", d["participants"], n_sites_total, "baseline"),
        ("Analyst B inputs", req["Analyst B (age, FD, CC200)"]["n"], req["Analyst B (age, FD, CC200)"]["n_sites"],
         LIMITING_LABEL[req["Analyst B (age, FD, CC200)"]["limiting_element"]]),
        ("+ IQ + FreeSurfer", req["UMAP + FreeSurfer IDP join"]["n"], req["UMAP + FreeSurfer IDP join"]["n_sites"],
         LIMITING_LABEL[req["UMAP + FreeSurfer IDP join"]["limiting_element"]]),
        ("+ SRS", req["UMAP + SRS"]["n"], req["UMAP + SRS"]["n_sites"], LIMITING_LABEL[req["UMAP + SRS"]["limiting_element"]]),
    ]
    y = np.arange(len(funnel))[::-1]
    ns = [f[1] for f in funnel]
    axf.barh(y, ns, color=NAVY, height=0.52, zorder=3)
    text_x = max(ns) * 1.04
    axf.set_xlim(0, max(ns) * 1.95)
    for yi, (_label, n, n_sites, note) in zip(y, funnel):
        axf.text(text_x, yi, f"{n:,} at {n_sites} sites\n{note}", ha="left", va="center", fontsize=BODY, color=GREY_DARK)
    axf.set_yticks(y, [f[0] for f in funnel], fontsize=BODY)
    axf.set_xticks([])
    axf.set_xlabel("participants retained", fontsize=BODY)
    for sp in ("top", "right", "bottom"):
        axf.spines[sp].set_visible(False)
    axf.tick_params(length=0)
    axf.set_ylim(-0.65, len(funnel) - 0.35)

    # --- RIGHT: one stacked bar per element, segments = n sites in each category ---
    right_left = left_margin_funnel + funnel_width + gap + right_label_margin
    right_right = WIDTH_IN - right_margin
    ax = fig.add_axes([right_left / WIDTH_IN, axes_bottom / HEIGHT_IN, (right_right - right_left) / WIDTH_IN,
                       axes_height / HEIGHT_IN])

    phenotype_keys = ELEMENT_ORDER[:6]
    imaging_keys = ELEMENT_ORDER[6:]
    gap = 1.3
    y_pos = list(range(len(phenotype_keys))) + [len(phenotype_keys) - 1 + gap + 1 + i for i in range(len(imaging_keys))]
    row_order = phenotype_keys + imaging_keys

    for yi, k in zip(y_pos, row_order):
        left = 0.0
        c = counts[k]
        for cat in cat_order:
            n = c[cat]
            if n == 0:
                continue
            ax.barh(yi, n, left=left, color=cat_colors[cat], height=0.62, edgecolor="white", linewidth=0.8, zorder=3)
            if n >= 2:  # print the count only where the segment is wide enough to hold it legibly
                txt_color = "white" if cat in ("partial", "high") else GREY_DARK
                ax.text(left + n / 2, yi, str(n), ha="center", va="center", fontsize=BODY * 0.78, color=txt_color, zorder=4)
            left += n
    ax.set_yticks(y_pos, [ELEMENT_PLAIN_LABEL[k] for k in row_order], fontsize=BODY)
    ax.invert_yaxis()
    ax.set_xlim(0, n_sites_total)
    ax.set_xticks([0, 5, 10, 15, 20])
    ax.tick_params(axis="x", labelsize=BODY)
    ax.set_xlabel(f"number of sites (of {n_sites_total})", fontsize=BODY)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(length=0)

    # Group headers: plain, centred, no rotation - "Phenotype" sits in the top margin above row 0,
    # "Imaging-derived" sits in the gap row deliberately left between the two groups.
    ax.text(n_sites_total / 2, -0.55, "Phenotype", ha="center", va="bottom", fontsize=BODY, color=GREY_DARK,
            clip_on=False, style="italic")
    ax.text(n_sites_total / 2, len(phenotype_keys) - 1 + gap / 2 + 0.5, "Imaging-derived", ha="center", va="center",
            fontsize=BODY, color=GREY_DARK, clip_on=False, style="italic")

    # Figure-fraction placement (not axes-fraction): a fixed inch position in the dedicated
    # legend_strip at the very bottom, centred on the full figure width so a legend wider than
    # the (narrower) right-hand panel still has room either side.
    legend_handles = [plt.Rectangle((0, 0), 1, 1, fc=cat_colors[c], ec=GREY_DARK, lw=0.8) for c in cat_order]
    legend_cx = 0.5
    legend_cy = (legend_strip / 2) / HEIGHT_IN
    fig.legend(legend_handles, [cat_names[c] for c in cat_order], loc="center", bbox_to_anchor=(legend_cx, legend_cy),
              ncol=4, frameon=False, fontsize=BODY, handlelength=1.3, handletextpad=0.5, columnspacing=1.4)

    problems = _check_text_artists(fig, DPI, round(WIDTH_IN * DPI), round(HEIGHT_IN * DPI))
    if problems:
        raise RuntimeError("element_coverage_slide text layout failed verification:\n" + "\n".join(problems))

    save_fixed_canvas(fig, "element_coverage_slide", WIDTH_IN, HEIGHT_IN, DPI)


def element_coverage_matrix_backup_slide() -> None:
    """Backup slide: the full sites x elements categorical matrix. Portrait (2400x3229), so it
    is not the primary slide (that needs a landscape ~11x4.9in figure area) but is kept for
    anyone who wants the per-site, per-element detail instead of the aggregated bar view.
    """
    # Deck places this image at ~11in wide; every font size below is chosen so that, once the
    # fixed 2400px-wide PNG is displayed at that width, the physical text is >=14pt (we target
    # 46px body / 52px headings at generation dpi = 2400/11 = 218.18, i.e. ~15.3pt / ~17.3pt).
    WIDTH_IN = 11.0
    GEN_DPI = 2400 / WIDTH_IN
    BODY = 46 * 72 / GEN_DPI
    HEAD = 52 * 72 / GEN_DPI

    d = json.loads((RESULTS / "element_coverage.json").read_text())
    els_all = d["elements"]
    req = d["analysis_requirements"]
    keep = ["AGE_AT_SCAN", "FIQ", "VIQ", "PIQ", "ADOS_TOTAL", "SRS_RAW_TOTAL", "func_mean_fd", "CC200_timeseries"]
    plain_label = {
        "AGE_AT_SCAN": "Age at scan",
        "FIQ": "Full-scale IQ",
        "VIQ": "Verbal IQ",
        "PIQ": "Performance IQ",
        "ADOS_TOTAL": "ADOS (clinician rating)",
        "SRS_RAW_TOTAL": "SRS (social responsiveness)",
        "func_mean_fd": "Head motion (FD)",
        "CC200_timeseries": "fMRI time series",
    }
    limiting_label = {
        "CC200_timeseries": "time series limits it",
        "VIQ": "verbal IQ limits it",
        "SRS_RAW_TOTAL": "SRS only at 4 sites",
    }
    site_code = {  # 2-3 letter codes, so a 45-degree rotation stays within a narrow column
        "CALTECH": "CAL", "CMU": "CMU", "KKI": "KKI", "LEUVEN_1": "LE1", "LEUVEN_2": "LE2",
        "MAX_MUN": "MUN", "NYU": "NYU", "OHSU": "OHS", "OLIN": "OLN", "PITT": "PIT", "SBL": "SBL",
        "SDSU": "SDS", "STANFORD": "STF", "TRINITY": "TRI", "UCLA_1": "UC1", "UCLA_2": "UC2",
        "UM_1": "UM1", "UM_2": "UM2", "USM": "USM", "YALE": "YAL",
    }
    sites = sorted(els_all["AGE_AT_SCAN"]["by_site"])  # element present for every participant -> complete site list
    site_totals = {s: els_all["AGE_AT_SCAN"]["by_site"][s] for s in sites}
    n_sites_total = len(sites)

    # --- category thresholds for the matrix: coverage fraction per (element, site) ---
    # >=90%: near-complete for that site; 10-90%: partial; 0-10%: rare; 0%: none at that site.
    cat_colors = [GREY_LIGHT, TERRACOTTA, NAVY, TEAL]  # none, rare (<10%), partial (10-90%), high (>=90%)
    cat_names = ["none (0%)", "rare (<10%)", "partial (10–90%)", "high (≥90%)"]

    # Sites as ROWS, elements as COLUMNS: 20 short row labels need no rotation at all, and a
    # phenotype/imaging group bracket over 8 columns is a plain horizontal span - both sidestep
    # the rotated-label and vertical-bracket crowding a (elements x sites) layout runs into once
    # every label has to be >=46px tall. The extra rows are exactly where "height may grow" helps.
    cats = np.zeros((len(sites), len(keep)), dtype=int)
    for i, s in enumerate(sites):
        for j, k in enumerate(keep):
            f = els_all[k]["by_site"].get(s, 0) / site_totals[s]
            if f <= 0:
                cats[i, j] = 0
            elif f < 0.10:
                cats[i, j] = 1
            elif f < 0.90:
                cats[i, j] = 2
            else:
                cats[i, j] = 3

    cmap = matplotlib.colors.ListedColormap(cat_colors)
    norm = matplotlib.colors.BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], cmap.N)

    fig = plt.figure(figsize=(WIDTH_IN, 14.5))
    gs = fig.add_gridspec(2, 1, height_ratios=[1.42, 4.1], hspace=0.4)

    # --- TOP: the requirement funnel for four concrete analyses (the point of the slide), full width ---
    axf = fig.add_subplot(gs[0, 0])
    funnel = [
        ("All participants", d["participants"], n_sites_total, "starting population"),
        ("Analyst B inputs", req["Analyst B (age, FD, CC200)"]["n"], req["Analyst B (age, FD, CC200)"]["n_sites"],
         limiting_label[req["Analyst B (age, FD, CC200)"]["limiting_element"]]),
        ("+ IQ + FreeSurfer", req["UMAP + FreeSurfer IDP join"]["n"], req["UMAP + FreeSurfer IDP join"]["n_sites"],
         limiting_label[req["UMAP + FreeSurfer IDP join"]["limiting_element"]]),
        ("+ SRS", req["UMAP + SRS"]["n"], req["UMAP + SRS"]["n_sites"], limiting_label[req["UMAP + SRS"]["limiting_element"]]),
    ]
    row_pitch = 2.3  # generous: each bar's label is two BODY-sized lines, so rows need real room
    y = np.arange(len(funnel))[::-1] * row_pitch
    ns = [f[1] for f in funnel]
    axf.barh(y, ns, color=NAVY, height=row_pitch * 0.5, zorder=3)
    text_x = max(ns) * 1.04
    axf.set_xlim(0, max(ns) * 1.85)  # fixed room to the right of every bar for its (short) label
    for yi, (_label, n, n_sites, note) in zip(y, funnel):
        axf.text(text_x, yi, f"{n:,} at {n_sites} sites\n{note}", ha="left", va="center", fontsize=BODY, color=GREY_DARK)
    axf.set_yticks(y, [f[0] for f in funnel], fontsize=BODY)
    axf.set_xticks([])
    axf.set_xlabel("participants retained", fontsize=BODY)
    for sp in ("top", "right", "bottom"):
        axf.spines[sp].set_visible(False)
    axf.tick_params(length=0)
    axf.set_ylim(-row_pitch * 0.9, (len(funnel) - 1) * row_pitch + row_pitch * 0.9)

    # --- BOTTOM: per-site coverage of each element, as discrete categories, not a continuous scale ---
    ax = fig.add_subplot(gs[1, 0])
    ax.imshow(cats, cmap=cmap, norm=norm, aspect="auto")
    ax.set_yticks(range(len(sites)), [site_code[s] for s in sites], fontsize=BODY)
    ax.set_xticks(range(len(keep)), [plain_label.get(k, k) for k in keep], fontsize=BODY, rotation=75, ha="right",
                  rotation_mode="anchor")
    ax.set_ylabel("ABIDE I sites (short codes)", fontsize=BODY, labelpad=10)
    for sp in ("top", "right", "left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(length=0)

    # Column group bracket (phenotype: cols 0-5; imaging-derived: cols 6-7), drawn above row 0.
    bracket_y = -1.6
    for x0, x1, label in [(-0.5, 5.5, "Phenotype"), (5.5, 7.5, "Imaging-derived")]:
        ax.plot([x0 + 0.08, x0 + 0.08, x1 - 0.08, x1 - 0.08], [bracket_y + 0.35, bracket_y, bracket_y, bracket_y + 0.35],
                color=GREY_DARK, lw=1.3, clip_on=False)
        ax.text((x0 + x1) / 2, bracket_y - 0.35, label, ha="center", va="bottom", fontsize=BODY, color=GREY_DARK,
                clip_on=False)

    legend_handles = [plt.Rectangle((0, 0), 1, 1, fc=c, ec=GREY_DARK, lw=0.8) for c in cat_colors]
    ax.text(0.5, 1.12, "Share of site participants with a value", fontsize=HEAD, ha="center", va="bottom",
            transform=ax.transAxes, color="black")
    ax.legend(legend_handles, cat_names, loc="lower center", bbox_to_anchor=(0.5, 1.045), ncol=4,
             frameon=False, fontsize=BODY, handlelength=1.3, handletextpad=0.5, columnspacing=1.5,
             bbox_transform=ax.transAxes)

    problems = [p for p in _check_text_artists(fig, 0, 10**9, 10**9) if p.startswith("OVERLAP")]
    if problems:
        raise RuntimeError("element_coverage_matrix_backup_slide text layout failed verification:\n" + "\n".join(problems))

    save(fig, "element_coverage_matrix_backup", width_in=WIDTH_IN)


# ---------------------------------------------------------------------------
# Figure 3: resource_map_slide
# ---------------------------------------------------------------------------

STEPS = [
    "acquisition", "conversion_to_bids", "phenotype_assessment_schema", "containerized_execution",
    "provenance_capture", "preprocessing", "idp_extraction_to_nidm", "qc_to_nidm", "query_merge",
    "statistics_results", "data_source", "training", "agent_skills",
]
STEP_LABEL = {
    "acquisition": "acquisition", "conversion_to_bids": "BIDS conv.",
    "phenotype_assessment_schema": "phenotype", "containerized_execution": "contain.",
    "provenance_capture": "provenance", "preprocessing": "preproc.",
    "idp_extraction_to_nidm": "IDP extr.", "qc_to_nidm": "QC to NIDM", "query_merge": "qry/merge",
    "statistics_results": "statistics", "data_source": "data source", "training": "training",
    "agent_skills": "agent skills",
}


def _parse_resources_ttl(step_rank: dict) -> dict:
    """Minimal Turtle reader for graph/resources.ttl (id, name, usage, primary workflow step)."""
    text = (GRAPH / "resources.ttl").read_text()
    cat = {}
    for block in text.split("\n\n"):
        if not block.strip():
            continue
        flat = " ".join(block.split())
        m = re.match(r"<urn:repronim:abide:resource/([^>]+)>", flat)
        if not m:
            continue
        rid = m.group(1)
        name_m = re.search(r'schema1:name "((?:[^"\\]|\\.)*)"', flat) or re.search(r'rdfs:label "((?:[^"\\]|\\.)*)"', flat)
        usage_m = re.search(r'ex:usageInExperiment "([^"]*)"', flat)
        steps_m = re.search(r"ex:workflowStep\s+(.*?)\s*[;.]", flat)
        steps = re.findall(r"step/([a-zA-Z_]+)", steps_m.group(1)) if steps_m else []
        primary = min(steps, key=lambda s: step_rank.get(s, 999)) if steps else None
        cat[rid] = {"name": name_m.group(1) if name_m else rid, "usage": usage_m.group(1), "primary": primary}
    return cat


def _latest_activity() -> dict:
    """Latest (max generated_at) activity snapshot per resource from the refresh-activity log."""
    act = {}
    with (RESULTS / "resource_activity_log.jsonl").open() as f:
        for line in f:
            rec = json.loads(line)
            rid = rec["resource"]
            if rid not in act or rec["generated_at"] > act[rid]["generated_at"]:
                act[rid] = rec
    return act


def resource_map_slide() -> None:
    """Resources grouped by primary workflow step, dots coloured by staleness, executed ones named.

    Hard canvas: 2400x600 px (12x3 in at 200 dpi), no tight-bbox cropping/rescaling, so the
    layout below is placed by hand in inches rather than left to matplotlib's auto margins -
    every row's height is budgeted up front so a 14pt-minimum font never has to compete with
    an autoscaled figure size.
    """
    step_rank = {s: i for i, s in enumerate(STEPS)}
    cat = _parse_resources_ttl(step_rank)
    act = _latest_activity()

    def parse_t(s: str) -> dt.datetime:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))

    bin_color = {"fresh": TEAL, "aging": NAVY, "stale": TERRACOTTA, "none": GREY_LIGHT}
    for rid, c in cat.items():
        a = act.get(rid, {})
        ref = a.get("last_commit_default_branch") or a.get("last_push")
        if ref is None:
            c["bin"] = "none"
        else:
            days = (parse_t(a["generated_at"]) - parse_t(ref)).days
            c["bin"] = "fresh" if days <= 30 else ("aging" if days <= 365 else "stale")

    steps_used = [s for s in STEPS if any(v["primary"] == s for v in cat.values())]
    executed_by_step = {
        s: sorted((c["name"].split(" (")[0] for c in cat.values() if c["primary"] == s and c["usage"] == "executed"))
        for s in steps_used
    }
    executed_by_step = {s: names for s, names in executed_by_step.items() if names}

    WIDTH_IN, HEIGHT_IN, DPI = 12.0, 3.0, 200.0
    FS = 14  # the uniform text-size floor the slide requires, everywhere in this figure

    fig = plt.figure(figsize=(WIDTH_IN, HEIGHT_IN))

    # Row budget (inches, bottom to top): caption / main dot area / step headers / legend.
    cap_h, hdr_h, leg_h = 0.46, 0.30, 0.50
    margin = 0.04
    main_h = HEIGHT_IN - cap_h - hdr_h - leg_h - 2 * margin
    y_cap0 = margin
    y_main0 = y_cap0 + cap_h
    y_hdr0 = y_main0 + main_h
    y_leg0 = y_hdr0 + hdr_h
    assert abs((y_leg0 + leg_h) - (HEIGHT_IN - margin)) < 1e-6

    left, right = 0.65, WIDTH_IN - 0.65
    usable_w = right - left

    n_cols = len(steps_used)
    pitch_in = usable_w / (n_cols - 1)
    col_x_in = {s: left + i * pitch_in for i, s in enumerate(steps_used)}

    # --- main scatter axes, placed by hand in figure-fraction coordinates, data y-units == inches
    # (ylim set to exactly [0, main_h]) so dot diameters/row spacing can be reasoned about in inches.
    ax = fig.add_axes([left / WIDTH_IN, y_main0 / HEIGHT_IN, usable_w / WIDTH_IN, main_h / HEIGHT_IN])
    ax.set_xlim(left, right)
    ax.set_ylim(0, main_h)

    max_rows = max(sum(1 for c in cat.values() if c["primary"] == s) for s in steps_used)
    row_pad = 0.06
    row_h = (main_h - 2 * row_pad) / max_rows
    diam = 0.82 * row_h  # largest (executed) marker; stay clear of the next dot up
    marker_size = {"executed": (diam * 72) ** 2 * np.pi / 4, "data_source": (0.68 * diam * 72) ** 2 * np.pi / 4,
                   "pointer": (0.45 * diam * 72) ** 2 * np.pi / 4}
    edge_width = {"executed": 1.3, "data_source": 0.8, "pointer": 0.0}

    for s in steps_used:
        rs = sorted((c for c in cat.values() if c["primary"] == s), key=lambda c: (-marker_size[c["usage"]], c["name"]))
        x = col_x_in[s]
        for j, c in enumerate(rs):
            y = row_pad + j * row_h
            ax.scatter(x, y, s=marker_size[c["usage"]], color=bin_color[c["bin"]], edgecolor=GREY_DARK,
                      linewidth=edge_width[c["usage"]], zorder=3, clip_on=False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis("off")

    # --- step headers: a short, horizontal, single-line label centred over each column ---
    for s in steps_used:
        fig.text(col_x_in[s] / WIDTH_IN, y_hdr0 / HEIGHT_IN + 0.03, STEP_LABEL.get(s, s), fontsize=FS,
                 color="black", ha="center", va="bottom")

    # --- legend row: one line, five swatches, centred ---
    legend_elems = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=TEAL, markeredgecolor=GREY_DARK, markersize=11, label="≤ 30 d"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=NAVY, markeredgecolor=GREY_DARK, markersize=11, label="≤ 1 y"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=TERRACOTTA, markeredgecolor=GREY_DARK, markersize=11, label="> 1 y"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=GREY_LIGHT, markeredgecolor=GREY_DARK, markersize=11, label="no activity data"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor="white", markeredgecolor=GREY_DARK, markersize=12, markeredgewidth=1.6, label="executed here"),
    ]
    fig.legend(handles=legend_elems, loc="center", fontsize=FS, frameon=False, ncol=5,
              bbox_to_anchor=(0.5, (y_leg0 + leg_h / 2) / HEIGHT_IN), columnspacing=1.1, handletextpad=0.35)

    # --- caption row: executed-here names grouped by their step, one compact line ---
    parts = [f"{STEP_LABEL.get(s, s)}: " + ", ".join(names) for s, names in executed_by_step.items()]
    fig.text(0.5, (y_cap0 + cap_h / 2) / HEIGHT_IN, "executed here  —  " + "   ·   ".join(parts),
             fontsize=FS, color=GREY_DARK, ha="center", va="center")

    problems = _check_text_artists(fig, DPI, round(WIDTH_IN * DPI), round(HEIGHT_IN * DPI))
    if problems:
        raise RuntimeError("resource_map_slide text layout failed verification:\n" + "\n".join(problems))

    save_fixed_canvas(fig, "resource_map_slide", WIDTH_IN, HEIGHT_IN, DPI)


if __name__ == "__main__":
    participant_ego_slide()
    element_coverage_slide()
    element_coverage_matrix_backup_slide()
    resource_map_slide()
    print("wrote:", sorted(p.name for p in OUT.iterdir()))
