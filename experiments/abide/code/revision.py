"""Propagate the motion-rule revision through the graph, then measure what actually changed.

  flag     Run SPARQL (Oxigraph, in memory) over graph/abide_kg_v1.ttl, before any recomputation, to find participants,
           cohorts, folds, results, claims and reviews that depend on the revised rule.
           Writes results/revision_flags.json and queries/revision_*.rq.
  compare  Compare v1 and recomputed v2 results for every flagged result.
           Writes results/revision_impact.json.

Usage: uv run python code/revision.py flag|compare
"""

import json
import sys

import time

import pyoxigraph as ox

from common import GRAPH, QUERIES, RESULTS, write_json

PREFIX = """PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dct: <http://purl.org/dc/terms/>
"""

Q_SITE_ELIGIBILITY = PREFIX + """
SELECT ?site ?dx (COUNT(DISTINCT ?p) AS ?remaining) WHERE {
  ?new prov:wasRevisionOf ?old ; ex:threshold ?thr ; ex:variable ?var .
  ?sel prov:used ?old , <urn:repronim:abide:rule/site_min> .
  ?cohort prov:wasGeneratedBy ?sel ; prov:hadMember ?p .
  ?p ex:site ?site .
  ?rec ex:participant ?p ; ?var ?fd ; <urn:repronim:abide:variable/DX_GROUP> ?dx .
  FILTER (?fd < ?thr)
} GROUP BY ?site ?dx ORDER BY ?site ?dx"""


def flag() -> None:
    """Run the traversal queries on the v1 graph (Oxigraph, in memory)."""
    import queries_original as qo
    from query_bench import OPT

    st = ox.Store()
    st.bulk_load(path=str(GRAPH / "abide_kg_v1.ttl"), format=ox.RdfFormat.TURTLE, to_graph=ox.NamedNode("urn:repronim:abide:graph/core_v1"))
    site_q = Q_SITE_ELIGIBILITY.replace("WHERE {", "WHERE { GRAPH <urn:repronim:abide:graph/core_v1> {", 1).replace("} GROUP BY", "} } GROUP BY")
    qs = {"participants": OPT["revision_participants"], "folds": OPT["revision_folds"], "downstream": qo.Q_DOWNSTREAM.replace("WHERE {", "WHERE { GRAPH <urn:repronim:abide:graph/core_v1> {", 1).rstrip().rstrip("}") + "} }", "site_eligibility": site_q}
    res, secs = {}, {}
    for name, q in qs.items():
        (QUERIES / f"revision_{name}.rq").write_text(q)
        t0 = time.time()
        r = st.query(q)
        vs = [v.value for v in r.variables]
        res[name] = [{v: (s_[i].value if s_[i] is not None else None) for i, v in enumerate(vs)} for s_ in r]
        secs[name] = round(time.time() - t0, 4)
    parts = [(r["cohort"], r["participant"], float(r["fd"])) for r in res["participants"]]
    by_cohort = {}
    for c, p, _ in parts:
        by_cohort.setdefault(c.rsplit("/", 1)[-1], set()).add(p)
    folds = [{"fold": r["fold"], "site": r["site"], "affected_in_test": int(r["nTest"]), "affected_in_train": int(r["nTrain"])} for r in res["folds"]]
    down = sorted({(r["entity"], r["kind"]) for r in res["downstream"]})
    elig = {}
    for r in res["site_eligibility"]:
        elig.setdefault(r["site"], {})["ASD" if float(r["dx"]) == 1 else "TD"] = int(r["remaining"])
    dropped_sites = sorted(s for s, c in elig.items() if c.get("ASD", 0) < 10 or c.get("TD", 0) < 10)
    kinds = {}
    for e, k in down:
        kinds[k] = kinds.get(k, 0) + 1
    out = {
        "graph": "graph/abide_kg_v1.ttl (before recomputation)",
        "affected_participants_by_cohort": {k: len(v) for k, v in by_cohort.items()},
        "affected_participants": {k: sorted(v) for k, v in by_cohort.items()},
        "folds": folds,
        "n_folds_with_affected_test": sum(f["affected_in_test"] > 0 for f in folds),
        "n_folds_with_affected_train": sum(f["affected_in_train"] > 0 for f in folds),
        "n_folds_total": len(folds),
        "cohort_A_site_counts_under_v2": elig,
        "cohort_A_sites_falling_below_minimum": dropped_sites,
        "flagged_by_kind": kinds,
        "flagged_entities": [e for e, _ in down],
        "queries": [f"queries/revision_{n}.rq" for n in ("participants", "folds", "downstream", "site_eligibility")],
        "engine": f"pyoxigraph {ox.__version__} (in memory)",
        "query_seconds": secs,
    }
    write_json("revision_flags.json", out)
    print(json.dumps({k: v for k, v in out.items() if k not in ("affected_participants", "flagged_entities", "folds")}, indent=1))


def load(name: str) -> dict:
    """Load a results JSON."""
    return json.loads((RESULTS / name).read_text())


def outside(x: float, ci: list[float]) -> bool:
    """True if x lies outside a closed interval."""
    return x < ci[0] or x > ci[1]


def compare() -> None:
    """Compare v1 and v2 results for each flagged result family."""
    flags = load("revision_flags.json")
    a1, a2 = load("analyst_a_v1.json"), load("analyst_a_v2.json")
    b1, b2 = load("analyst_b_v1.json"), load("analyst_b_v2.json")
    r1, r2 = load("reviews_v1.json"), load("reviews_v2.json")
    base = "urn:repronim:abide:"
    changes = {
        "A_result": {
            "v1": base + "result/A_v1", "v2": base + "result/A_v2",
            "summary": f"n {a1['n']}->{a2['n']}; sites {len(a1['sites'])}->{len(a2['sites'])}; FDR edges {a1['n_fdr_significant']}->{a2['n_fdr_significant']}; hypo fraction {a1['hypo_fraction']:.3f}->{a2['hypo_fraction']:.3f}",
            "material": outside(a2["hypo_fraction"], a1["hypo_fraction_bootstrap_95ci"]),
        },
    }
    for m in ("demographic", "demographic_fd", "correlation", "tangent"):
        p1, p2 = b1["pooled"][m], b2["pooled"][m]
        changes[f"B_pooled_{m}"] = {
            "v1": base + f"result/B_v1/pooled/{m}", "v2": base + f"result/B_v2/pooled/{m}",
            "summary": f"AUC {p1['auc']:.3f} [{p1['auc_95ci'][0]:.3f},{p1['auc_95ci'][1]:.3f}] -> {p2['auc']:.3f}; accuracy {p1['accuracy']:.3f}->{p2['accuracy']:.3f}",
            "material": outside(p2["auc"], p1["auc_95ci"]),
        }
    folds1 = {f["held_out_site"]: f for f in b1["folds"]}
    site_rows = []
    for f2 in b2["folds"]:
        f1 = folds1[f2["held_out_site"]]
        site_rows.append({
            "site": f2["held_out_site"], "n_test_v1": f1["n_test"], "n_test_v2": f2["n_test"],
            "tangent_acc_v1": f1["tangent"]["accuracy"], "tangent_acc_v2": f2["tangent"]["accuracy"],
            "delta": f2["tangent"]["accuracy"] - f1["tangent"]["accuracy"],
            "v2_outside_v1_wilson_ci": outside(f2["tangent"]["accuracy"], f1["tangent"]["accuracy_95ci"]),
        })
    for key, label in (("A_reviews_B", "review_A_of_B"), ("B_reviews_A", "review_B_of_A")):
        changes[label] = {
            "v1": base + f"review/{key}_v1", "v2": base + f"review/{key}_v2",
            "summary": f"verdict '{r1[key]['verdict']}' -> '{r2[key]['verdict']}'",
            "material": r1[key]["verdict"] != r2[key]["verdict"],
        }
    for who in ("A", "B"):
        c1 = f"{base}claim/{who}_v1"
        changes[f"claim_{who}"] = {
            "v1": c1, "v2": f"{base}claim/{who}_v2",
            "summary": "claim text regenerated from v2 result",
            "material": changes["A_result"]["material"] if who == "A" else changes["B_pooled_tangent"]["material"],
        }
    out = {
        "n_flagged_entities": len(flags["flagged_entities"]),
        "flagged_by_kind": flags["flagged_by_kind"],
        "n_result_families_compared": len(changes),
        "n_material_changes": sum(c["material"] for c in changes.values()),
        "materiality_rule": "material if the v2 point estimate falls outside the v1 95% interval (bootstrap for pooled AUC and A's hypo fraction), or a review verdict string changes",
        "changes": changes,
        "per_site_tangent_accuracy": site_rows,
        "n_sites_outside_v1_ci": sum(r["v2_outside_v1_wilson_ci"] for r in site_rows),
        "dropped_folds": sorted(set(folds1) - {f["held_out_site"] for f in b2["folds"]}),
    }
    write_json("revision_impact.json", out)
    print(json.dumps({k: v for k, v in out.items() if k != "per_site_tangent_accuracy"}, indent=1))


if __name__ == "__main__":
    {"flag": flag, "compare": compare}[sys.argv[1]]()
