"""SHACL validation of the final graph plus targeted mutation tests.

Mutations (each must be rejected by the named shape):
  1. remove prov:wasDerivedFrom from one connectivity DerivativeObject
  2. remove prov:wasAttributedTo from one review
  3. change a claim's claimType to an unknown value ("causal")
  4. mark a paper evidence span as not verbatim
  5. add a fold that lists no test participants
  6. remove prov:generatedAtTime from one activity snapshot
  7. promote the ILLUSTRATIVE study-only record (egress gate must reject it)
  8. drop one gate from a promotion candidate

Usage: uv run python code/validate.py
"""

import json
import time

from pyshacl import validate
from rdflib import RDF, Graph, Literal, Namespace

from common import GRAPH, RESULTS, ROOT, write_json

E = Namespace("urn:repronim:abide:")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")


def check(g: Graph, shapes: Graph, focus) -> tuple[bool, str]:
    """Validate only the focus node(s)."""
    ok, _, text = validate(g, shacl_graph=shapes, inference="none", focus_nodes=focus, allow_warnings=False)
    return ok, text


def main() -> None:
    """Validate, mutate, re-validate, and record."""
    t0 = time.time()
    shapes = Graph().parse(ROOT / "code/shapes.ttl")
    g = Graph().parse(GRAPH / "abide_kg.ttl")
    for extra in ("embedding_provenance.ttl", "resources.ttl", "resource_activity.ttl", "scope.ttl"):
        g += Graph().parse(GRAPH / extra)
    ok, report, text = validate(g, shacl_graph=shapes, inference="none")
    (RESULTS / "shacl_report.txt").write_text(text)
    conn = next(g.subjects(RDF.type, E.Fold))
    some_conn = next(iter(g.objects(conn, E.testedOn)))
    review = E["review/B_reviews_A_v1"]
    claim = E["claim/A_v1"]
    span = E["paper/abraham2017/AB_C1/evidence"]
    mutations = []

    def mutate(name, focus, apply, undo):
        apply()
        passed, txt = check(g, shapes, [focus])
        undo()
        msgs = [ln.strip() for ln in txt.splitlines() if ln.strip().startswith("Message:")]
        mutations.append({"mutation": name, "focus": str(focus), "rejected": not passed, "messages": msgs[:3]})

    src = list(g.objects(some_conn, PROV.wasDerivedFrom))
    mutate("connectivity derivative without source", some_conn,
           lambda: g.remove((some_conn, PROV.wasDerivedFrom, None)),
           lambda: [g.add((some_conn, PROV.wasDerivedFrom, s)) for s in src])
    who = list(g.objects(review, PROV.wasAttributedTo))
    mutate("review without reviewer", review,
           lambda: g.remove((review, PROV.wasAttributedTo, None)),
           lambda: [g.add((review, PROV.wasAttributedTo, w)) for w in who])
    ctype = list(g.objects(claim, E.claimType))
    mutate("claim typed as causal", claim,
           lambda: (g.remove((claim, E.claimType, None)), g.add((claim, E.claimType, Literal("causal")))),
           lambda: (g.remove((claim, E.claimType, None)), [g.add((claim, E.claimType, c)) for c in ctype]))
    mutate("evidence span not verbatim", span,
           lambda: (g.remove((span, E.verbatimMatch, None)), g.add((span, E.verbatimMatch, Literal(False)))),
           lambda: (g.remove((span, E.verbatimMatch, None)), g.add((span, E.verbatimMatch, Literal(True)))))
    bad_fold = E["fold/mutation_test"]
    mutate("fold with no test participants", bad_fold,
           lambda: (g.add((bad_fold, RDF.type, E.Fold)), g.add((bad_fold, E.trainedOn, some_conn)), g.add((bad_fold, DCT.isPartOf, E["analysis/B_v1"]))),
           lambda: g.remove((bad_fold, None, None)))
    snap = next(g.subjects(RDF.type, E.ResourceActivitySnapshot))
    ts = list(g.objects(snap, PROV.generatedAtTime))
    mutate("activity snapshot without timestamp", snap,
           lambda: g.remove((snap, PROV.generatedAtTime, None)),
           lambda: [g.add((snap, PROV.generatedAtTime, t)) for t in ts])
    prom = E["promotion/illustrative_study_only"]
    mutate("promote a study-only record to the lake", prom,
           lambda: (g.add((prom, RDF.type, E.PromotionCandidate)), g.add((prom, PROV.used, E["illustrative/study_only_record"])),
                    g.add((prom, E.promotionStatus, Literal("promoted"))),
                    [(g.add((prom, E.gate, E[f"promotion/illustrative_study_only/gate/{k}"])), g.add((E[f"promotion/illustrative_study_only/gate/{k}"], E.gateType, Literal(k))),
                      g.add((E[f"promotion/illustrative_study_only/gate/{k}"], E.status, Literal("pass"))))
                     for k in ("generality", "review", "consent_and_deidentification", "licence", "persistent_identifier_and_version", "provenance_retained")]),
           lambda: [g.remove((x, None, None)) for x in [prom] + [E[f"promotion/illustrative_study_only/gate/{k}"] for k in
                    ("generality", "review", "consent_and_deidentification", "licence", "persistent_identifier_and_version", "provenance_retained")]])
    cand = E["promotion/motion_rule_v2"]
    gate = E["promotion/motion_rule_v2/gate/licence"]
    mutate("promotion candidate missing a gate", cand,
           lambda: g.remove((cand, E.gate, gate)),
           lambda: g.add((cand, E.gate, gate)))
    out = {
        "graph": "graph/abide_kg.ttl + embedding_provenance.ttl + resources.ttl + resource_activity.ttl + scope.ttl",
        "triples": len(g),
        "n_shapes": len(set(shapes.subjects(RDF.type, Namespace("http://www.w3.org/ns/shacl#").NodeShape))),
        "conforms": ok,
        "mutations": mutations,
        "all_mutations_rejected": all(m["rejected"] for m in mutations),
        "scope": "local profile for this experiment; not NIDM certification and not a check of scientific correctness",
        "seconds": round(time.time() - t0, 1),
    }
    write_json("shacl_summary.json", out)
    print(json.dumps({k: v for k, v in out.items() if k != "mutations"}, indent=1), [(m["mutation"], m["rejected"]) for m in mutations])


if __name__ == "__main__":
    main()
