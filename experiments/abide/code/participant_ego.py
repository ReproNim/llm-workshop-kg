"""Participant-centred view: everything the graph knows about one participant, by query, with sources.

The participant is present in every layer: phenotype, CC200 time series, cohorts A and B, ReproNim simple2
NIDM with ANTs, FSL and FreeSurfer volumes, and the PyNIDM phenotype graph. Source triples within two hops
are CONSTRUCTed into results/participant_ego.ttl; a grouped summary (<= 40 nodes, repeated data elements
collapsed) goes to results/participant_ego.json and figures/participant_ego.{png,svg}.

Usage: uv run python code/participant_ego.py [FILE_ID]
"""

import json
import sys
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from rdflib import Graph

from common import FIGURES, QUERIES, RESULTS, write_json
from store import open_store

G = "urn:repronim:abide:graph/"
PID = sys.argv[1] if len(sys.argv) > 1 else "MaxMun_c_0051332"
P = f"<urn:repronim:abide:participant/{PID}>"
PX = """PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
"""
CONSTRUCT = PX + f"""CONSTRUCT {{ ?s ?p ?o }} WHERE {{ GRAPH <{G}core> {{
  {{ BIND({P} AS ?s) ?s ?p ?o }}
  UNION {{ ?s ex:participant {P} ; ?p ?o }}
  UNION {{ ?s prov:hadMember {P} ; ?p ?o FILTER (?p != prov:hadMember) }}
  UNION {{ ?a prov:qualifiedAssociation ?as . ?as prov:agent {P} . BIND(?a AS ?s) ?s ?p ?o FILTER (?p != prov:used) }}
  UNION {{ ?c ex:participant {P} . ?s ex:testedOn ?c ; ?p ?o FILTER (?p NOT IN (ex:testedOn, ex:trainedOn)) }}
}} }}"""
Q = {
    "phenotype": PX + f"""SELECT ?var ?label ?value ?about ?row WHERE {{ GRAPH <{G}core> {{
        ?rec ex:participant {P} ; a nidm:AcquisitionObject ; ex:sourceRow ?row ; ?var ?value .
        ?var a nidm:DataElement ; rdfs:label ?label . OPTIONAL {{ ?var nidm:isAbout ?about }} }} }}""",
    "missing": PX + f"""SELECT (COUNT(?v) AS ?n) WHERE {{ GRAPH <{G}core> {{ ?rec ex:participant {P} ; ex:missingVariable ?v }} }}""",
    "scans": PX + f"""SELECT ?img ?kind ?url WHERE {{ GRAPH <{G}core> {{ ?img ex:participant {P} ; a nidm:AcquisitionObject ; prov:atLocation ?url ;
        nidm:hadImageUsageType ?kind }} }}""",
    "derived": PX + f"""SELECT ?ent ?type ?act ?agentLabel ?sha WHERE {{ GRAPH <{G}core> {{ ?ent ex:participant {P} ; a nidm:DerivativeObject ;
        prov:wasGeneratedBy ?act . ?act prov:wasAssociatedWith ?ag . ?ag a prov:SoftwareAgent ; rdfs:label ?agentLabel .
        OPTIONAL {{ ?ent <http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions#sha256> ?sha }}
        BIND(STRBEFORE(STRAFTER(STR(?ent), "abide:"), "/") AS ?type) }} }}""",
    "cohorts": PX + f"""SELECT ?cohort WHERE {{ GRAPH <{G}core> {{ ?cohort prov:hadMember {P} }} }}""",
    "folds": PX + f"""SELECT ?fold ?site ?role WHERE {{ GRAPH <{G}core> {{ ?c ex:participant {P} ; a nidm:DerivativeObject .
        {{ ?fold ex:testedOn ?c BIND("held out (test)" AS ?role) }} UNION {{ ?fold ex:trainedOn ?c BIND("training" AS ?role) }}
        ?fold ex:heldOutSite ?site }} }}""",
    "results": PX + f"""SELECT DISTINCT ?result ?label WHERE {{ GRAPH <{G}core> {{ ?c ex:participant {P} ; a nidm:DerivativeObject .
        {{ ?an prov:used ?c . ?result prov:wasGeneratedBy ?an }} UNION {{ ?f ex:testedOn ?c . ?result prov:wasGeneratedBy ?f }}
        OPTIONAL {{ ?result rdfs:label ?label }} }} }}""",
    "paper": PX + f"""SELECT ?paper ?title ?cohortNode WHERE {{ GRAPH <{G}core> {{ ?cohortNode prov:hadMember {P} .
        ?reported ex:reconstructedAs ?cohortNode ; ex:statedIn ?paper . ?paper rdfs:label ?title }} }}""",
    "volumes": PX + f"""SELECT ?tool (COUNT(?o) AS ?n) (SAMPLE(?g) AS ?graph) WHERE {{ GRAPH <{G}view/volumes> {{ ?o ex:participant {P} ; ex:tool ?tool ; ex:sourceGraph ?g }} }} GROUP BY ?tool""",
    "hippocampus": PX + f"""SELECT ?tool ?v WHERE {{ GRAPH <{G}view/volumes> {{ ?o ex:participant {P} ; ex:tool ?tool ; ex:region <http://purl.obolibrary.org/obo/UBERON_0001954> ;
        ex:side ?side ; ex:volume ?v . FILTER (STRENDS(STR(?side), "Left")) }} }}""",
    "external_ids": PX + f"""SELECT ?g ?person WHERE {{ GRAPH <{G}core> {{ {P} ndar:src_subject_id ?id }} GRAPH ?g {{ ?person ndar:src_subject_id ?id }}
        FILTER (?g != <{G}core> && ?g != <{G}core_v1>) }}""",
    "scope": PX + f"""SELECT ?scope ?level ?consent ?egress ?lake ?policy WHERE {{ GRAPH <{G}scope> {{ ex:participantRecords ex:knowledgeScope ?scope ;
        ex:pondLevel ?level ; ex:hasSensitivityProfile ?p ; ex:lakeCopy ?lake ; ex:promotionPolicy ?policy . ?p ex:consentScope ?consent ; ex:egressPermitted ?egress }} }}""",
}
LAYER_COLOURS = {"participant": "#222222", "phenotype": "#4C72B0", "scan": "#8172B2", "derived": "#55A868", "idp": "#C44E52",
                 "cohort": "#DD8452", "analysis": "#937860", "paper": "#DA8BC3", "scope": "#8C8C8C", "external": "#64B5CD"}


def short(x: str) -> str:
    """Compact IRI."""
    return x.replace("urn:repronim:abide:", "ex:").replace("urn:repronim:simple2:datasets.datalad.org/abide/RawDataBIDS/", "simple2:")


def main() -> None:
    """Query, assemble, plot."""
    st = open_store()
    t0 = time.time()
    (QUERIES / "Q13_construct.rq").write_text(CONSTRUCT)
    triples = list(st.query(CONSTRUCT))
    ego = Graph()
    for t in triples:
        ego.parse(data=f"{t.subject} {t.predicate} {t.object} .", format="nt")
    ego.serialize(RESULTS / "participant_ego.ttl", format="turtle")
    rows = {}
    for k, q in Q.items():
        (QUERIES / f"Q13_{k}.rq").write_text(q)
        r = st.query(q)
        vs = [v.value for v in r.variables]
        rows[k] = [{v: s[i].value for i, v in enumerate(vs) if s[i] is not None} for s in r]
    secs = round(time.time() - t0, 3)
    a_v2_reason = json.loads((RESULTS / "revision_flags.json").read_text())["cohort_A_sites_falling_below_minimum"]

    gr = nx.DiGraph()

    def node(n, layer, label):
        gr.add_node(n, layer=layer, label=label)

    def edge(a, b, label):
        gr.add_edge(a, b, label=label)

    sub = next((r["value"] for r in rows["phenotype"] if r["var"].endswith("/SUB_ID")), "?")
    node("P", "participant", f"{PID}\nndar:src_subject_id {sub}")
    groups = {"demographics": ["AGE_AT_SCAN", "SEX", "DX_GROUP", "SITE_ID", "HANDEDNESS_CATEGORY", "EYE_STATUS_AT_SCAN"], "IQ": ["FIQ", "VIQ", "PIQ"],
              "motion & rater QC": ["func_mean_fd", "func_perc_fd", "qc_rater_1", "qc_func_rater_2", "qc_func_rater_3", "qc_anat_rater_2", "qc_anat_rater_3"]}
    ph = {r["var"].rsplit("/", 1)[-1]: r for r in rows["phenotype"]}
    shown = set()
    for gname, vars_ in groups.items():
        vals = [f"{v}={float(ph[v]['value']):.3g}" if ph[v]["value"].replace('.', '', 1).replace('-', '', 1).isdigit() else f"{v}={ph[v]['value']}" for v in vars_ if v in ph]
        shown |= set(vars_)
        node(f"ph:{gname}", "phenotype", f"{gname}\n" + "\n".join(vals[:4]) + ("\n..." if len(vals) > 4 else ""))
        edge("P", f"ph:{gname}", "phenotype record (source row " + str(next(iter(ph.values()))["row"]) + ")")
    other = len([v for v in ph if v not in shown])
    node("ph:other", "phenotype", f"{other} other phenotype values\n{rows['missing'][0]['n']} recorded as missing")
    edge("P", "ph:other", "phenotype record")
    for s in rows["scans"]:
        kind = s["kind"].rsplit("#", 1)[-1]
        node(f"scan:{kind}", "scan", f"raw {('T1w' if kind == 'Anatomical' else 'rest BOLD')}\n(S3 pointer, not downloaded)")
        edge("P", f"scan:{kind}", "subject of acquisition")
    for d in rows["derived"]:
        t = d["type"]
        lab = {"timeseries": "CC200 time series", "connectivity": "connectivity\n(19,900 Fisher-z edges)", "idp": "ANTs ROI thickness"}.get(t, t)
        node(f"der:{t}", "derived", f"{lab}\nsha256 {d.get('sha', '')[:10]}")
        edge(f"der:{t}", "P", "ex:participant")
        node(f"sw:{d['agentLabel']}", "derived", d["agentLabel"].replace(" (", "\n("))
        edge(f"sw:{d['agentLabel']}", f"der:{t}", "generated")
    if "scan:Functional" in gr and "der:timeseries" in gr:
        edge("scan:Functional", "der:timeseries", "wasDerivedFrom")
    if "der:timeseries" in gr and "der:connectivity" in gr:
        edge("der:timeseries", "der:connectivity", "wasDerivedFrom")
    hip = {r["tool"]: float(r["v"]) for r in rows["hippocampus"]}
    tn = {"http://stnava.github.io/ANTs/": "ANTs", "http://purl.org/nidash/fsl#": "FSL", "https://surfer.nmr.mgh.harvard.edu/": "FreeSurfer"}
    for r in rows["volumes"]:
        name = tn.get(r["tool"], r["tool"])
        node(f"vol:{name}", "idp", f"{name} volumes ({r['n']})\nL hippocampus {hip.get(r['tool'], float('nan')):,.0f} mm³")
        edge(f"vol:{name}", "P", "via shared ndar:src_subject_id")
    for r in rows["external_ids"]:
        g = short(r["g"])
        lab = "PyNIDM csv2nidm person" if "pynidm" in g else ("ReproNim simple2 person\n" + g.split("/")[0] if "simple2" in g else g)
        node(f"ext:{g}", "external", lab)
        edge("P", f"ext:{g}", "same src_subject_id")
    for r in rows["cohorts"]:
        c = r["cohort"].rsplit("/", 1)[-1]
        node(f"coh:{c}", "cohort", f"cohort {c}")
        edge(f"coh:{c}", "P", "hadMember")
    if not any(r["cohort"].endswith("A_v2") for r in rows["cohorts"]):
        node("coh:A_v2", "cohort", f"cohort A_v2: NOT a member\n(site {', '.join(a_v2_reason)} < 10 per group)")
        edge("coh:A_v2", "P", "excluded by site rule")
    test = [r for r in rows["folds"] if r["role"].startswith("held")]
    train = [r for r in rows["folds"] if r["role"] == "training"]
    for r in test:
        v = r["fold"].split("/")[-2]
        node(f"fold:{v}", "analysis", f"B {v} fold: held-out site {r['site']}")
        edge("P", f"fold:{v}", "test participant")
    for v in sorted({r["fold"].split("/")[-2] for r in train}):
        n = sum(1 for r in train if r["fold"].split("/")[-2] == v)
        node(f"train:{v}", "analysis", f"B {v}: training in {n} other folds")
        edge("P", f"train:{v}", "training participant")
    res = [r for r in rows["results"]]
    node("results", "analysis", f"{len(res)} results used this\nparticipant (A edgewise GLM,\nB per-fold metrics)")
    edge("P", "results", "input to")
    for r in rows["paper"]:
        node("paper", "paper", "Abraham et al. 2017\n(reconstructed cohort, N=873\nvs 871 reported)")
        edge("coh:abraham2017_reconstructed", "paper", "reconstructs reported cohort")
    for r in rows["scope"]:
        node("scope", "scope", f"pond:{r['level']} copy\nconsent {r['consent']}, egress {r['egress']}\nlake copy: ABIDE Preprocessed")
        edge("P", "scope", "record family scope")
    write_json("participant_ego.json", {"participant": PID, "query_seconds": secs, "construct_triples": len(ego), "rows": rows,
                                        "figure_nodes": gr.number_of_nodes(), "figure_edges": gr.number_of_edges(),
                                        "nodes": [{"id": n, **d} for n, d in gr.nodes(data=True)], "edges": [{"from": a, "to": b, **d} for a, b, d in gr.edges(data=True)]})

    layers = ["phenotype", "scan", "derived", "idp", "external", "cohort", "analysis", "paper", "scope"]
    pos = {"P": np.array([0.0, 0.0])}
    outer = [n for n in gr if n.startswith("sw:") or n == "paper"]
    ring = [n for n in gr if n != "P" and n not in outer]
    ring.sort(key=lambda n: (layers.index(gr.nodes[n]["layer"]), n))
    for i, n in enumerate(ring):
        ang = np.pi / 2 - 2 * np.pi * i / len(ring)
        r = (1.0, 1.38, 1.76)[i % 3] if not (i == len(ring) - 1 and i % 3 == 0) else 1.38
        pos[n] = np.array([1.5 * r * np.cos(ang), 1.0 * r * np.sin(ang)])
    for n in outer:
        nb = [m for m in list(gr.successors(n)) + list(gr.predecessors(n)) if m in pos]
        base = np.mean([pos[m] for m in nb], axis=0) if nb else np.array([1.0, 0.0])
        pos[n] = base / max(np.linalg.norm(base / np.array([1.5, 1.0])), 1e-6) * 2.15
    taken = [pos[n] for n in ring]
    for n in outer:
        while any(np.linalg.norm(pos[n] - t) < 0.28 for t in taken):
            pos[n] = pos[n] + np.array([0.0, 0.3 if pos[n][1] >= 0 else -0.3])
        taken.append(pos[n])
    fig, ax = plt.subplots(figsize=(20, 14))
    nx.draw_networkx_edges(gr, pos, ax=ax, edge_color="#AAAAAA", arrows=True, arrowsize=8, width=0.8, connectionstyle="arc3,rad=0.05")
    nx.draw_networkx_edge_labels(gr, pos, ax=ax, edge_labels={(a, b): d["label"] for a, b, d in gr.edges(data=True)}, font_size=6.5,
                                 font_color="#555555", bbox={"boxstyle": "round,pad=0.1", "fc": "white", "ec": "none", "alpha": 0.8})
    for n, d in gr.nodes(data=True):
        x, y = pos[n]
        ax.text(x, y, d["label"], ha="center", va="center", fontsize=8 if n != "P" else 10, color="white" if d["layer"] in ("participant", "analysis") else "black",
                bbox={"boxstyle": "round,pad=0.35", "fc": LAYER_COLOURS[d["layer"]], "ec": "black", "lw": 0.5, "alpha": 0.95 if n != "P" else 1})
    for lay in layers:
        ax.scatter([], [], s=120, color=LAYER_COLOURS[lay], label=lay)
    ax.legend(frameon=False, loc="lower left", fontsize=9, ncol=3)
    ax.set_xlim(-3.6, 3.6)
    ax.set_ylim(-2.35, 2.35)
    ax.axis("off")
    ax.set_title(f"Everything the graph knows about {PID} ({gr.number_of_nodes()} grouped nodes from {len(ego):,} source triples)", fontsize=12)
    for ext in ("png", "svg"):
        fig.savefig(FIGURES / f"participant_ego.{ext}", dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(PID, gr.number_of_nodes(), "nodes", len(ego), "triples", secs, "s")


if __name__ == "__main__":
    main()
