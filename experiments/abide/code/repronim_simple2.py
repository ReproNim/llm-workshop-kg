"""Join ReproNim's simple2 ABIDE NIDM graphs to this experiment without rewriting them.

1. Load the 24 ABIDE nidm.ttl files from ReproNim/simple2_NIDM_examples and the three tool CDE files,
   each into its own named graph (Oxigraph).
2. Run their queries/simple2_query.sparql unmodified; compare with the output CSV they ship.
3. Build an explicit identity join ndar:src_subject_id -> ABIDE Preprocessed SUB_ID/FILE_ID and record
   every age/sex/diagnosis/FIQ disagreement.
4. Compare the same anatomical region (UBERON isAbout + laterality) across ANTs, FSL and FreeSurfer.
5. Export per-participant volumes for the UMAP join, and answer Q8.
Writes graph/repronim_simple2_link.ttl, results/simple2_*.json|csv, queries/simple2_*.rq, figures/tool_agreement.*

Usage: uv run python code/repronim_simple2.py
"""

import glob
import itertools
import json
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyoxigraph as ox
from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace, URIRef

from common import DATA, FIGURES, GRAPH, QUERIES, RESULTS, base_table, load_pheno, sha256_file, write_json

S2 = DATA / "repronim_simple2"
SIMPLE2_SHA = "e0dff17629bd5031e246c05ff4bed174597552a2"
SIMPLE2_RAW = f"https://raw.githubusercontent.com/ReproNim/simple2_NIDM_examples/{SIMPLE2_SHA}/"
CDE_SOURCES = {
    "cde_tools/ants_cde.ttl": "https://raw.githubusercontent.com/ReproNim/ants_seg_to_nidm/97e6257b0827a0e6bcc78c179f83168c83397f39/ants_seg_to_nidm/mapping_data/ants_cde.ttl",
    "cde_tools/fsl_cde.ttl": "https://raw.githubusercontent.com/ReproNim/fsl_seg_to_nidm/54f91ec7c5c10837d1970bcbd2e39add6a5a3530/fsl_seg_to_nidm/mapping_data/fsl_cde.ttl",
    "cde_tools/fs_cde.ttl": SIMPLE2_RAW + "cde/fs_cde.ttl",
}
TOOLS = {"http://stnava.github.io/ANTs/": "ANTs", "http://purl.org/nidash/fsl#": "FSL", "https://surfer.nmr.mgh.harvard.edu/": "FreeSurfer"}
CONVERTERS = {"ANTs": "ReproNim/ants_seg_to_nidm", "FSL": "ReproNim/fsl_seg_to_nidm", "FreeSurfer": "ReproNim/segstats_jsonld"}
E = Namespace("urn:repronim:abide:")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
CRYPTO = Namespace("http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions#")
UBERON_NAMES = {
    "UBERON_0000956": "cerebral cortex grey matter", "UBERON_0002437": "cerebral white matter", "UBERON_0001359": "CSF",
    "UBERON_0001873": "caudate", "UBERON_0001874": "putamen", "UBERON_0001876": "amygdala", "UBERON_0001882": "accumbens",
    "UBERON_0001897": "thalamus", "UBERON_0001954": "hippocampus", "UBERON_0006514": "pallidum",
}

Q_IDS = """PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX ilx: <http://uri.interlex.org/>
PREFIX ncit: <http://ncitt.ncit.nih.gov/>
SELECT ?g ?ID (SAMPLE(?age) AS ?Age) (SAMPLE(?sex) AS ?Sex) (SAMPLE(?dx) AS ?DX) (SAMPLE(?fiq) AS ?FIQ) WHERE {
  GRAPH ?g {
    ?agent ndar:src_subject_id ?ID .
    OPTIONAL {
      ?act prov:qualifiedAssociation ?as . ?as prov:agent ?agent . ?ent prov:wasGeneratedBy ?act .
      OPTIONAL { ?ent ?am ?age . ?am a nidm:PersonalDataElement ; nidm:isAbout ilx:ilx_0100400 }
      OPTIONAL { ?ent ?sm ?sex . ?sm a nidm:PersonalDataElement ; nidm:isAbout <http://uri.interlex.org/base/ilx_0101292> }
      OPTIONAL { ?ent ?dm ?dx . ?dm a nidm:PersonalDataElement ; nidm:isAbout ncit:Diagnosis }
      OPTIONAL { ?ent ?fm ?fiq . ?fm a nidm:PersonalDataElement ; nidm:isAbout <http://uri.interlex.org/base/ilx_0739365> }
    }
  }
} GROUP BY ?g ?ID"""

Q8_TEMPLATE = """PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <urn:repronim:abide:>
SELECT ?fileId ?srcId ?tool ?converter ?label ?region ?laterality ?volume ?namedGraph WHERE {
  GRAPH <urn:repronim:abide:graph/link> {
    VALUES ?p { <urn:repronim:abide:participant/%s> }
    ?link ex:localParticipant ?p ; ex:externalId ?srcId .
    BIND (STRAFTER(STR(?p), "participant/") AS ?fileId)
  }
  GRAPH ?namedGraph {
    ?act prov:qualifiedAssociation ?a1 , ?a2 .
    ?a1 prov:agent ?sw . ?sw nidm:NIDM_0000164 ?tool .
    ?a2 prov:agent ?subj . ?subj ndar:src_subject_id ?srcId .
    ?ent prov:wasGeneratedBy ?act ; ?measure ?volume .
  }
  ?measure rdfs:label ?label ; nidm:isAbout ?region ;
           nidm:measureOf <http://uri.interlex.org/base/ilx_0112559> ; nidm:datumType <http://uri.interlex.org/base/ilx_0738276> .
  OPTIONAL { ?measure nidm:hasLaterality ?laterality }
  OPTIONAL { GRAPH <urn:repronim:abide:graph/link> { ?toolRes ex:nidmToolNamespace ?tool ; ex:converterRepo ?converter } }
} ORDER BY ?region ?laterality ?tool"""


def val(term):
    """Plain Python value of an Oxigraph term (None stays None)."""
    return None if term is None else term.value


def load_store() -> tuple[ox.Store, list[dict]]:
    """Load every simple2 ABIDE file and the CDE files into named graphs."""
    store = ox.Store()
    manifest = []
    files = sorted(glob.glob(str(S2 / "datasets.datalad.org/abide/**/nidm.ttl"), recursive=True))
    for f in files:
        rel = f.split("repronim_simple2/")[1]
        g = f"urn:repronim:simple2:{rel}"
        store.bulk_load(path=f, format=ox.RdfFormat.TURTLE, to_graph=ox.NamedNode(g))
        manifest.append({"named_graph": g, "source": SIMPLE2_RAW + rel, "sha256": sha256_file(S2 / rel), "kind": "site NIDM"})
    for rel, url in CDE_SOURCES.items():
        g = f"urn:repronim:simple2:{rel}"
        store.bulk_load(path=str(S2 / rel), format=ox.RdfFormat.TURTLE, to_graph=ox.NamedNode(g))
        manifest.append({"named_graph": g, "source": url, "sha256": sha256_file(S2 / rel), "kind": "tool CDE"})
    return store, manifest


def run_verbatim(store: ox.Store) -> tuple[pd.DataFrame, dict]:
    """Their simple2_query.sparql, unmodified, over the union of named graphs; compare with their shipped CSV."""
    q = (S2 / "queries/simple2_query.sparql").read_text()
    t0 = time.time()
    cols = ["study", "ID", "Age", "dx", "Gender", "FIQ", "PIQ", "VIQ", "tool", "softwareLabel", "federatedLabel", "laterality", "volume"]
    rows = [{c: val(r[c]) for c in cols} for r in store.query(q, use_default_graph_as_union=True)]
    secs = time.time() - t0
    df = pd.DataFrame(rows, columns=cols)
    df["tool_name"] = df.tool.map(TOOLS)
    df["volume"] = df.volume.astype(float)
    df.to_csv(RESULTS / "simple2_query_output_abide.csv", index=False)
    shipped = pd.read_csv(S2 / "queries/simple2_query_output.csv", dtype=str)
    shipped["ID"] = shipped.ID.astype(int).astype(str)
    shipped_ids = set(shipped.ID)
    ours_ids = set(df.ID.astype(int).astype(str))
    key = ["ID", "softwareLabel"]
    mine = df.assign(ID=df.ID.astype(int).astype(str))
    mine = mine[mine.ID.isin(shipped_ids)].groupby(key).volume.apply(lambda v: tuple(sorted(v.astype(float))))
    theirs = shipped[shipped.ID.isin(ours_ids)].groupby(key).volume.apply(lambda v: tuple(sorted(v.astype(float))))
    common = mine.index.intersection(theirs.index)
    equal = sum(len(mine[k]) == len(theirs[k]) and np.allclose(mine[k], theirs[k], rtol=1e-6) for k in common)
    only_ours = sorted(set(mine.index.get_level_values(1)) - set(theirs.index.get_level_values(1)))
    only_theirs = sorted(set(theirs.index.get_level_values(1)) - set(mine.index.get_level_values(1)))
    return df, {
        "query": "data/repronim_simple2/queries/simple2_query.sparql (unmodified)",
        "engine": f"pyoxigraph {ox.__version__}",
        "seconds": round(secs, 1),
        "rows": len(df),
        "participants": int(df.ID.nunique()),
        "rows_by_tool": df.tool_name.value_counts().to_dict(),
        "shipped_output_rows_total": len(shipped),
        "shipped_output_ids_total": len(shipped_ids),
        "shipped_ids_also_in_ours": len(shipped_ids & ours_ids),
        "participant_label_keys_in_both": int(len(common)),
        "keys_with_equal_values_rtol_1e-6": int(equal),
        "labels_only_in_our_run": only_ours,
        "labels_only_in_shipped_output": only_theirs,
        "label_drift_note": "shipped CSV predates a CDE relabel; same measures, different rdfs:label",
    }


def identity_join(store: ox.Store) -> tuple[pd.DataFrame, dict]:
    """src_subject_id -> SUB_ID join with field-by-field conflict checks."""
    (QUERIES / "simple2_identity.rq").write_text(Q_IDS)
    ids = pd.DataFrame([{k: val(r[k]) for k in ("g", "ID", "Age", "Sex", "DX", "FIQ")} for r in store.query(Q_IDS)])
    dup = ids.groupby("ID").g.nunique()
    ids["SUB_ID"] = ids.ID.astype(int)
    ph = load_pheno()
    ph = ph[["SUB_ID", "FILE_ID", "SITE_ID", "AGE_AT_SCAN", "SEX", "DX_GROUP", "FIQ"]]
    m = ids.merge(ph, on="SUB_ID", how="outer", indicator=True)
    both = m[m._merge == "both"].copy()

    def num(s):
        return pd.to_numeric(s, errors="coerce")

    sex_theirs = both.Sex.map(lambda x: {"1": 1, "2": 2, "Male": 1, "Female": 2, "male": 1, "female": 2}.get(str(x), np.nan))
    both["age_conflict"] = (num(both.Age) - both.AGE_AT_SCAN).abs() > 0.01
    both["sex_conflict"] = sex_theirs.notna() & (sex_theirs != both.SEX)
    both["dx_conflict"] = num(both.DX).notna() & (num(both.DX) != both.DX_GROUP)
    fiq_ours = both.FIQ_y.where(both.FIQ_y > 0)
    both["fiq_conflict"] = num(both.FIQ_x).notna() & fiq_ours.notna() & ((num(both.FIQ_x) - fiq_ours).abs() > 0.5)
    both["missing_fields_theirs"] = both[["Age", "Sex", "DX"]].isna().sum(axis=1)
    b = base_table()
    coh = json.loads((RESULTS / "cohorts.json").read_text())
    conflicts = both[both[["age_conflict", "sex_conflict", "dx_conflict", "fiq_conflict"]].any(axis=1)]
    out = {
        "query": "queries/simple2_identity.rq",
        "rule": "integer(ndar:src_subject_id) == SUB_ID in Phenotypic_V1_0b_preprocessed1.csv; reviewed link, not owl:sameAs",
        "simple2_ids": int(ids.ID.nunique()),
        "simple2_ids_in_more_than_one_site_graph": int((dup > 1).sum()),
        "phenotype_rows": len(ph),
        "matched": int(len(both)),
        "only_in_simple2": int((m._merge == "left_only").sum()),
        "only_in_phenotype": int((m._merge == "right_only").sum()),
        "matched_with_preprocessed_FILE_ID": int((both.FILE_ID != "no_filename").sum()),
        "matched_in_cohort_B_v1": int(both.FILE_ID.isin(coh["B_v1"]["members"]).sum()),
        "matched_in_cohort_A_v1": int(both.FILE_ID.isin(coh["A_v1"]["members"]).sum()),
        "conflicts": {k: int(both[f"{k}_conflict"].sum()) for k in ("age", "sex", "dx", "fiq")},
        "conflict_examples": conflicts.head(10)[["ID", "FILE_ID", "Age", "AGE_AT_SCAN", "Sex", "SEX", "DX", "DX_GROUP", "FIQ_x", "FIQ_y"]].astype(str).to_dict(orient="records"),
        "n_participants_with_any_conflict": int(len(conflicts)),
        "fields_missing_in_simple2": int((both.missing_fields_theirs > 0).sum()),
    }
    del b
    return both, out


def agreement(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Pairwise tool agreement for regions measured by all three tools."""
    df = df.copy()
    df["region"] = df.federatedLabel.str.rsplit("/", n=1).str[-1]
    df["side"] = df.laterality.fillna("").str.rsplit("/", n=1).str[-1].replace("", "both")
    labels_per = df.groupby(["region", "side", "tool_name"]).softwareLabel.nunique()
    ambiguous = labels_per[labels_per > 1].reset_index()
    single = labels_per[labels_per == 1].reset_index()
    tools_per = single.groupby(["region", "side"]).tool_name.nunique()
    three = tools_per[tools_per == 3].index
    wide = (
        df.set_index(["region", "side"]).loc[list(three)].reset_index()
        .pivot_table(index=["ID", "region", "side"], columns="tool_name", values="volume", aggfunc="first")
        .reset_index()
    )
    rows = []
    for (reg, side), sub in wide.groupby(["region", "side"]):
        for t1, t2 in itertools.combinations(["ANTs", "FSL", "FreeSurfer"], 2):
            s = sub[[t1, t2]].dropna()
            x, y = s[t1].to_numpy(), s[t2].to_numpy()
            mean = (x + y) / 2
            rows.append({
                "region": UBERON_NAMES.get(reg, reg), "uberon": reg, "side": side, "pair": f"{t1} vs {t2}", "n": len(s),
                "pearson_r": float(np.corrcoef(x, y)[0, 1]),
                "median_ratio": float(np.median(x / y)),
                "mean_abs_pct_diff": float(np.mean(np.abs(x - y) / mean) * 100),
            })
    agree = pd.DataFrame(rows)
    agree.to_csv(RESULTS / "simple2_tool_agreement.csv", index=False)
    summary = {
        "regions_with_all_three_tools": int(len(three)),
        "region_tool_pairs_ambiguous": ambiguous.assign(n_labels=ambiguous.softwareLabel).drop(columns="softwareLabel").to_dict(orient="records"),
        "pairwise": rows,
        "median_r_by_pair": agree.groupby("pair").pearson_r.median().to_dict(),
        "median_abs_pct_diff_by_pair": agree.groupby("pair").mean_abs_pct_diff.median().to_dict(),
    }
    return wide, summary


def figure(agree: pd.DataFrame, wide: pd.DataFrame) -> None:
    """Heatmap of pairwise r by region plus a left-hippocampus scatter."""
    piv = agree.assign(lab=agree.region + " " + agree.side.str[0].replace("b", "")).pivot_table(index="lab", columns="pair", values="pearson_r")
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13, 6), gridspec_kw={"width_ratios": [1.1, 1]})
    im = ax.imshow(piv.to_numpy(), cmap="viridis", vmin=0, vmax=1, aspect="auto")
    ax.set_yticks(range(len(piv)), piv.index, fontsize=8)
    ax.set_xticks(range(len(piv.columns)), piv.columns, rotation=20, fontsize=9)
    for i in range(piv.shape[0]):
        for j in range(piv.shape[1]):
            ax.text(j, i, f"{piv.iat[i, j]:.2f}", ha="center", va="center", fontsize=7, color="w" if piv.iat[i, j] < 0.6 else "k")
    fig.colorbar(im, ax=ax, label="Pearson r across participants")
    ax.set_title("Same region, different software (ReproNim simple2 NIDM)", fontsize=10)
    h = wide[(wide.region == "UBERON_0001954") & (wide.side == "Left")]
    for t, c in (("FSL", "#DD8452"), ("ANTs", "#4C72B0")):
        ax2.scatter(h.FreeSurfer, h[t], s=5, alpha=0.5, color=c, label=f"{t} vs FreeSurfer")
    lim = [np.nanmin(h[["FreeSurfer", "FSL", "ANTs"]].to_numpy()), np.nanmax(h[["FreeSurfer", "FSL", "ANTs"]].to_numpy())]
    ax2.plot(lim, lim, color="#8C8C8C", lw=0.8)
    ax2.set_xlabel("FreeSurfer left hippocampus (mm³)")
    ax2.set_ylabel("other tool (mm³)")
    ax2.legend(frameon=False)
    ax2.set_title("Left hippocampus: identity line in grey", fontsize=10)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(FIGURES / f"tool_agreement.{ext}", dpi=170)
    plt.close(fig)


def link_graph(manifest: list[dict], joined: pd.DataFrame, agree_rows: list[dict]) -> Graph:
    """Our side of the join: named-graph manifest, identity links, conflicts, agreement results."""
    g = Graph()
    for k, v in (("ex", E), ("prov", PROV), ("dct", DCT)):
        g.bind(k, v)
    org = E["org/ReproNim"]
    g.add((org, RDF.type, PROV.Organization))
    g.add((org, RDFS.label, Literal("ReproNim")))
    conv = E["activity/simple2_conversion"]
    g.add((conv, RDF.type, PROV.Activity))
    g.add((conv, RDFS.label, Literal("ReproNim simple2: bidsmri2nidm + csv2nidm + ants_seg_to_nidm / fsl_seg_to_nidm / segstats_jsonld")))
    g.add((conv, E.executionRecord, Literal("described in the simple2_NIDM_examples README; not observed or rerun here")))
    g.add((conv, PROV.wasAssociatedWith, org))
    for tool, repo in CONVERTERS.items():
        r = E[f"resource/github/{repo}"]
        g.add((conv, PROV.used, r))
        ns = [k for k, v in TOOLS.items() if v == tool][0]
        g.add((r, E.nidmToolNamespace, URIRef(ns)))
        g.add((r, E.converterRepo, Literal(repo)))
    for m in manifest:
        ng = URIRef(m["named_graph"])
        g.add((ng, RDF.type, PROV.Bundle))
        g.add((ng, RDF.type, E.ExternalNamedGraph))
        g.add((ng, PROV.atLocation, URIRef(m["source"])))
        g.add((ng, CRYPTO.sha256, Literal(m["sha256"])))
        g.add((ng, E.kind, Literal(m["kind"])))
        g.add((ng, PROV.wasAttributedTo, org))
        g.add((ng, E.loadedUnmodified, Literal(True)))
        if m["kind"] == "site NIDM":
            g.add((ng, PROV.wasGeneratedBy, conv))
    act = E["activity/identity_join_simple2"]
    g.add((act, RDF.type, PROV.Activity))
    g.add((act, PROV.wasAssociatedWith, E["software/repronim_simple2.py"]))
    g.add((E["software/repronim_simple2.py"], RDF.type, PROV.SoftwareAgent))
    g.add((act, E.rule, Literal("integer(ndar:src_subject_id) == SUB_ID")))
    for _, r in joined.iterrows():
        fid = r.FILE_ID if r.FILE_ID != "no_filename" else f"SUB_{r.SUB_ID}"
        link = E[f"identity/simple2/{r.ID}"]
        g.add((link, RDF.type, E.IdentityLink))
        g.add((link, PROV.wasGeneratedBy, act))
        g.add((link, E.localParticipant, E[f"participant/{fid}"]))
        g.add((link, E.externalId, Literal(r.ID)))
        g.add((link, E.externalIdProperty, URIRef("https://ndar.nih.gov/api/datadictionary/v2/dataelement/src_subject_id")))
        g.add((link, E.externalGraph, URIRef(r.g)))
        conflicts = [k for k in ("age", "sex", "dx", "fiq") if r[f"{k}_conflict"]]
        g.add((link, E.status, Literal("conflict" if conflicts else "matched")))
        for k in conflicts:
            g.add((link, E.conflictField, Literal(k)))
    for i, a in enumerate(agree_rows):
        n = E[f"tool_agreement/{i}"]
        g.add((n, RDF.type, E.ToolAgreement))
        g.add((n, PROV.wasGeneratedBy, act))
        g.add((n, E.region, URIRef(f"http://purl.obolibrary.org/obo/{a['uberon']}")))
        g.add((n, RDFS.label, Literal(f"{a['region']} {a['side']}: {a['pair']}")))
        g.add((n, E.n, Literal(a["n"], datatype=XSD.integer)))
        g.add((n, E.pearson_r, Literal(a["pearson_r"], datatype=XSD.double)))
        g.add((n, E.median_ratio, Literal(a["median_ratio"], datatype=XSD.double)))
    g.serialize(GRAPH / "repronim_simple2_link.ttl", format="turtle")
    return g


def q8(store: ox.Store, link: Graph, fid: str) -> dict:
    """Per-tool volumes for one participant through the identity link."""
    store.load(link.serialize(format="nt").encode(), format=ox.RdfFormat.N_TRIPLES, to_graph=ox.NamedNode("urn:repronim:abide:graph/link"))
    q = Q8_TEMPLATE % fid
    (QUERIES / "Q8.rq").write_text(q)
    rows = [{k: val(r[k]) for k in ("fileId", "srcId", "tool", "converter", "label", "region", "laterality", "volume", "namedGraph")} for r in store.query(q, use_default_graph_as_union=True)]
    df = pd.DataFrame(rows)
    if df.empty:
        return {"participant": fid, "rows": 0}
    df["tool_name"] = df.tool.map(TOOLS)
    df["volume"] = df.volume.astype(float)
    df["side"] = df.laterality.fillna("").str.rsplit("/", n=1).str[-1].replace("", "both")
    df["region_id"] = df.region.str.rsplit("/", n=1).str[-1]
    per = df[df.region_id.isin(UBERON_NAMES)].groupby(["region_id", "side", "tool_name"]).agg(volume=("volume", "first"), label=("label", "first"), converter=("converter", "first")).reset_index()
    out = []
    for (reg, side), s in per.groupby(["region_id", "side"]):
        vals = dict(zip(s.tool_name, s.volume))
        if len(vals) == 3:
            out.append({"region": UBERON_NAMES[reg], "side": side, "volumes_mm3": vals, "max_over_min": max(vals.values()) / min(vals.values()),
                        "producers": dict(zip(s.tool_name, s.converter))})
    return {"participant": fid, "src_subject_id": rows[0]["srcId"], "rows": len(rows), "named_graph": rows[0]["namedGraph"], "three_tool_regions": out}


def idps(df: pd.DataFrame, joined: pd.DataFrame) -> None:
    """Per FILE_ID volumes for the UMAP join: grey matter, white matter, left/right hippocampus by tool."""
    d = df.copy()
    d["region"] = d.federatedLabel.str.rsplit("/", n=1).str[-1]
    d["side"] = d.laterality.fillna("").str.rsplit("/", n=1).str[-1].replace("", "both")
    keep = {("UBERON_0000956", "both"): "gm", ("UBERON_0002437", "both"): "wm", ("UBERON_0001954", "Left"): "hippo_L", ("UBERON_0001954", "Right"): "hippo_R"}
    d = d[[(r, s) in keep for r, s in zip(d.region, d.side)]]
    d["col"] = [f"{keep[(r, s)]}_{t}" for r, s, t in zip(d.region, d.side, d.tool_name)]
    wide = d.pivot_table(index="ID", columns="col", values="volume", aggfunc="first").reset_index()
    wide = wide.merge(joined[["ID", "FILE_ID"]], on="ID")
    wide.to_csv(RESULTS / "simple2_idps.csv", index=False)


def main() -> None:
    """Run every step."""
    t0 = time.time()
    store, manifest = load_store()
    df, verbatim = run_verbatim(store)
    joined, ident = identity_join(store)
    wide, agree = agreement(df)
    figure(pd.DataFrame(agree["pairwise"]), wide)
    link = link_graph(manifest, joined, agree["pairwise"])
    idps(df, joined)
    coh = json.loads((RESULTS / "cohorts.json").read_text())
    three = set(df.groupby("ID").tool_name.nunique().loc[lambda x: x == 3].index)
    pid = sorted(set(coh["A_v1"]["members"]) & set(coh["B_v1"]["members"]) & set(joined[joined.ID.isin(three)].FILE_ID))[0]
    q8res = q8(store, link, pid)
    out = {"simple2_commit": SIMPLE2_SHA, "named_graphs": manifest, "n_named_graphs": len(manifest), "store_quads": len(store),
           "verbatim_query": verbatim, "identity_join": ident, "tool_agreement": agree, "Q8": q8res, "link_graph_triples": len(link),
           "seconds": round(time.time() - t0, 1)}
    write_json("simple2.json", out)
    print(json.dumps({k: v for k, v in out.items() if k not in ("named_graphs", "tool_agreement")}, indent=1, default=str)[:4000])
    print(json.dumps({k: agree[k] for k in ("regions_with_all_three_tools", "median_r_by_pair", "median_abs_pct_diff_by_pair")}, indent=1))


if __name__ == "__main__":
    main()
