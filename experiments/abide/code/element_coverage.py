"""Data-element-centred view: how many participants have each element, by diagnosis and site, and which
combinations limit each analysis. One set-returning SPARQL query per element over the Oxigraph store (core graph, volume view, ReproNim
simple2 graphs); a single query with a correlated EXISTS per participant took over 10 minutes.

Writes queries/Q14.rq, results/element_coverage.json, figures/element_coverage.{png,pdf}.

Usage: uv run python code/element_coverage.py
"""

import itertools
import json
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from common import FIGURES, QUERIES, write_json
from store import open_store

G = "urn:repronim:abide:graph/"
V = "urn:repronim:abide:variable/"
PHENO = ["AGE_AT_SCAN", "FIQ", "VIQ", "PIQ", "ADOS_TOTAL", "SRS_RAW_TOTAL", "func_mean_fd"]
TOOLS = {"ANTs": "http://stnava.github.io/ANTs/", "FSL": "http://purl.org/nidash/fsl#", "FreeSurfer": "https://surfer.nmr.mgh.harvard.edu/"}


PX = """PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
"""


def queries() -> dict[str, str]:
    """One set-returning query per element (participants that have it), plus the base table."""
    q = {"base": PX + f"SELECT ?p ?site ?dx WHERE {{ GRAPH <{G}core> {{ ?rec a nidm:AcquisitionObject ; ex:participant ?p ; <{V}DX_GROUP> ?dx . ?p ex:site ?site }} }}"}
    for v in PHENO:
        q[v] = PX + f"SELECT DISTINCT ?p WHERE {{ GRAPH <{G}core> {{ ?rec <{V}{v}> ?x ; ex:participant ?p }} }}"
    q["CC200_timeseries"] = PX + f"SELECT DISTINCT ?p WHERE {{ GRAPH <{G}core> {{ ?ts ex:fullRoiCoverage true ; ex:participant ?p }} }}"
    for t, iri in TOOLS.items():
        q[f"L_hippocampus_{t}"] = PX + (f"SELECT DISTINCT ?p WHERE {{ GRAPH <{G}view/volumes> {{ ?o ex:region <http://purl.obolibrary.org/obo/UBERON_0001954> ; "
                                        f"ex:tool <{iri}> ; ex:side ?sd ; ex:participant ?p . FILTER(STRENDS(STR(?sd), \"Left\")) }} }}")
    q["ReproNim_DX"] = PX + ("SELECT DISTINCT ?p WHERE { GRAPH ?sg { ?dxm a nidm:PersonalDataElement ; nidm:isAbout <http://ncitt.ncit.nih.gov/Diagnosis> . "
                             "?e ?dxm ?dxv ; prov:wasGeneratedBy ?act . ?act prov:qualifiedAssociation ?a . ?a prov:agent ?subj . ?subj ndar:src_subject_id ?id } "
                             f"GRAPH <{G}core> {{ ?p ndar:src_subject_id ?id }} FILTER(STRSTARTS(STR(?sg), \"urn:repronim:simple2:\")) }}")
    return q


def main() -> None:
    """Count, plot, record."""
    st = open_store()
    qs = queries()
    (QUERIES / "Q14.rq").write_text("\n\n".join(f"# {k}\n{v}" for k, v in qs.items()))
    t0 = time.time()
    base = st.query(qs.pop("base"))
    df = pd.DataFrame([{"p": s[0].value, "site": s[1].value, "dx": s[2].value} for s in base])
    per = {}
    for k, q in qs.items():
        t1 = time.time()
        members = {s[0].value for s in st.query(q)}
        df[k] = df.p.isin(members)
        per[k] = round(time.time() - t1, 3)
    secs = round(time.time() - t0, 3)
    els = list(qs)
    df["dx"] = np.where(df.dx.astype(float) == 1, "ASD", "TD")
    out = {"query": "queries/Q14.rq", "query_seconds": secs, "per_element_seconds": per, "participants": len(df), "elements": {}}
    for c in els:
        out["elements"][c] = {"n": int(df[c].sum()), "by_dx": df[df[c]].dx.value_counts().to_dict(),
                              "by_site": df[df[c]].site.value_counts().to_dict(),
                              "sites_with_none": sorted(set(df.site) - set(df[df[c]].site))}
    needs = {
        "Analyst A (age, FIQ, FD, CC200)": ["AGE_AT_SCAN", "FIQ", "func_mean_fd", "CC200_timeseries"],
        "Analyst B (age, FD, CC200)": ["AGE_AT_SCAN", "func_mean_fd", "CC200_timeseries"],
        "UMAP primary (age, FIQ, VIQ, PIQ)": ["AGE_AT_SCAN", "FIQ", "VIQ", "PIQ"],
        "UMAP + SRS": ["AGE_AT_SCAN", "FIQ", "VIQ", "PIQ", "SRS_RAW_TOTAL"],
        "UMAP + FreeSurfer IDP join": ["AGE_AT_SCAN", "FIQ", "VIQ", "PIQ", "L_hippocampus_FreeSurfer"],
        "ADOS-based analysis + CC200": ["ADOS_TOTAL", "CC200_timeseries"],
    }
    out["analysis_requirements"] = {}
    for name, req in needs.items():
        ok = df[req].all(axis=1)
        limiting = min(req, key=lambda c: df[c].sum())
        out["analysis_requirements"][name] = {"requires": req, "n": int(ok.sum()), "by_dx": df[ok].dx.value_counts().to_dict(),
                                              "n_sites": int(df[ok].site.nunique()), "limiting_element": limiting}
    upset_sets = ["CC200_timeseries", "func_mean_fd", "FIQ", "SRS_RAW_TOTAL", "ADOS_TOTAL", "L_hippocampus_FreeSurfer"]
    combos = df[upset_sets].apply(lambda r: tuple(bool(x) for x in r), axis=1).value_counts()
    out["upset_top"] = [{"elements": [s for s, b in zip(upset_sets, k) if b], "n": int(n)} for k, n in combos.head(12).items()]
    write_json("element_coverage.json", out)

    sites = sorted(df.site.unique())
    frac = np.array([[df[(df.site == s)][c].mean() for s in sites] for c in els])
    fig = plt.figure(figsize=(18, 11))
    gs = fig.add_gridspec(2, 2, width_ratios=[4, 1], height_ratios=[1.1, 1], hspace=0.45, wspace=0.05)
    ax = fig.add_subplot(gs[0, 0])
    im = ax.imshow(frac, cmap="viridis", vmin=0, vmax=1, aspect="auto")
    ax.set_yticks(range(len(els)), [e.replace("_", " ") for e in els], fontsize=9)
    ax.set_xticks(range(len(sites)), [f"{s}\n({(df.site == s).sum()})" for s in sites], fontsize=7, rotation=90)
    fig.colorbar(im, ax=ax, fraction=0.02, pad=0.01, label="fraction of site participants with a value")
    ax.set_title(f"Who has each data element, by site ({len(df)} ABIDE I participants; {len(els)} SPARQL queries, {secs} s)", fontsize=11)
    axb = fig.add_subplot(gs[0, 1], sharey=ax)
    tot_asd = [df[c][df.dx == "ASD"].sum() for c in els]
    tot_td = [df[c][df.dx == "TD"].sum() for c in els]
    axb.barh(range(len(els)), tot_asd, color="#DD8452", label="ASD")
    axb.barh(range(len(els)), tot_td, left=tot_asd, color="#4C72B0", label="TD")
    for i, (a, b) in enumerate(zip(tot_asd, tot_td)):
        axb.text(a + b + 10, i, str(a + b), va="center", fontsize=8)
    axb.set_xlim(0, 1350)
    axb.legend(frameon=False, fontsize=8, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2)
    plt.setp(axb.get_yticklabels(), visible=False)
    axb.set_xlabel("participants")
    au = fig.add_subplot(gs[1, :])
    top = out["upset_top"]
    x = np.arange(len(top))
    au.bar(x, [t["n"] for t in top], color="#555555")
    for i, t in enumerate(top):
        au.text(i, t["n"] + 5, str(t["n"]), ha="center", fontsize=8)
        for j, s in enumerate(upset_sets):
            au.scatter(i, -60 - 45 * j, s=60, color="#222222" if s in t["elements"] else "#DDDDDD", zorder=3)
    for j, s in enumerate(upset_sets):
        au.text(-0.7, -60 - 45 * j, s.replace("_", " "), ha="right", va="center", fontsize=8)
    au.set_ylim(-60 - 45 * len(upset_sets), max(t["n"] for t in top) * 1.15)
    au.set_xlim(-3.2, len(top) - 0.5)
    au.set_xticks([])
    au.set_yticks([])
    for sp in ("left", "right", "top", "bottom"):
        au.spines[sp].set_visible(False)
    req_text = "\n".join(f"{k}: {v['n']} (limited by {v['limiting_element']})" for k, v in out["analysis_requirements"].items())
    au.set_title("Exact combinations of six elements (top 12)\n" + req_text, fontsize=8.5)
    for ext in ("png", "pdf"):
        fig.savefig(FIGURES / f"element_coverage.{ext}", dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(json.dumps({k: v["n"] for k, v in out["elements"].items()}), json.dumps({k: (v["n"], v["limiting_element"]) for k, v in out["analysis_requirements"].items()}), secs)


if __name__ == "__main__":
    main()
