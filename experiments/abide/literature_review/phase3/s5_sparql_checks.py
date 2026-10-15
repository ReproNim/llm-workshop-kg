"""SPARQL checks on literature_kg.ttl against results_synthesis.json."""
import json
from rdflib import Graph
from common import ROOT

g = Graph(); g.parse(ROOT / "literature_kg.ttl")
syn = json.load(open(ROOT / "results_synthesis.json"))
P = """PREFIX ex: <urn:repronim:abide:> PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"""


def q(s):
    return list(g.query(P + s))


checks = []
inc = q('SELECT (COUNT(DISTINCT ?p) AS ?n) WHERE { ?p ex:reviewDecision "included" }')[0][0].toPython()
checks.append(("included publications", inc, syn["screening"]["included"]))
exc = q('SELECT (COUNT(DISTINCT ?p) AS ?n) WHERE { ?p ex:reviewDecision "excluded" }')[0][0].toPython()
checks.append(("excluded publications", exc, syn["screening"]["excluded"]))
rel = {str(r[0]): r[1].toPython() for r in q('SELECT ?r (COUNT(DISTINCT ?p) AS ?n) WHERE { ?p ex:reviewDecision "included" . ?l ex:publication ?p ; ex:abideReleaseNamed ?r } GROUP BY ?r')}
checks.append(("release distribution (included)", rel, syn["release"]))
abide1 = q('SELECT (COUNT(DISTINCT ?p) AS ?n) WHERE { ?l ex:publication ?p ; ex:dataset <urn:repronim:abide:dataset/abide_i> ; ex:status ?s . ?p ex:reviewDecision "included" }')[0][0].toPython()
checks.append(("included linked to dataset/abide_i", abide1, syn["release"].get("ABIDE I", 0) + syn["release"].get("ABIDE I+II", 0)))
ct = {str(r[0]): r[1].toPython() for r in q('SELECT ?c (COUNT(?p) AS ?n) WHERE { ?p ex:claimType ?c } GROUP BY ?c')}
checks.append(("claim types", ct, syn["claim_type"]))
lso = q('SELECT (COUNT(DISTINCT ?p) AS ?n) WHERE { ?p a ex:Publication ; ex:evaluationScheme "leave-site-out" }')[0][0].toPython()
checks.append(("papers with leave-site-out evaluation", lso, syn["evaluation"]["papers_per_scheme"]["leave-site-out"]))
leak = q('SELECT (COUNT(DISTINCT ?p) AS ?n) WHERE { ?p ex:leakageFlag ?f }')[0][0].toPython()
checks.append(("leakage-flagged", leak, len(syn["evaluation"]["leakage_flagged"])))
rec = {str(r[0]): r[1].toPython() for r in q('SELECT ?r (COUNT(?c) AS ?n) WHERE { ?c a ex:AnalysedCohort ; ex:reconstructible ?r } GROUP BY ?r')}
checks.append(("reconstructible", rec, syn["reconstructibility_RQ6"]["detail"]))
sc = {str(r[0]): r[1].toPython() for r in q('SELECT ?l (COUNT(DISTINCT ?c) AS ?n) WHERE { ?c ex:matchesSharedCohort ?s . ?s rdfs:label ?l } GROUP BY ?l')}
checks.append(("shared cohort membership", sorted(sc.values(), reverse=True), sorted([x["n_papers"] for x in syn["shared_cohorts"]["groups"]], reverse=True)))
n871 = [str(r[0]) for r in q('SELECT ?id WHERE { ?c ex:matchesSharedCohort ?s . ?s ex:nTotal 871 . ?l ex:cohort ?c ; ex:publication ?p . ?p ex:reviewSourceId ?id } ORDER BY ?id')]
med = q('SELECT (COUNT(?x) AS ?n) WHERE { ?p ex:reportsPerformance ?x . ?x ex:evaluationScheme "pooled k-fold CV" }')[0][0].toPython()
checks.append(("pooled-CV accuracy rows", med, syn["evaluation"]["accuracy_by_scheme"]["pooled k-fold CV"]["n_papers_with_accuracy"]))
unver = q('SELECT (COUNT(?q) AS ?n) WHERE { ?q a ex:EvidenceQuote . FILTER NOT EXISTS { ?q ex:sourceQuoteVerified true } }')[0][0].toPython()
checks.append(("unverified quotes", unver, 0))
prov_ok = q('SELECT (COUNT(?q) AS ?n) WHERE { ?q a ex:EvidenceQuote ; prov:wasGeneratedBy ?a . ?a prov:qualifiedAssociation/prov:hadPlan ?plan . ?plan prov:wasDerivedFrom/prov:wasGeneratedBy ?session }')[0][0].toPython()
nq = q('SELECT (COUNT(?q) AS ?n) WHERE { ?q a ex:EvidenceQuote }')[0][0].toPython()
checks.append(("quotes traceable to the intake session (quote -> charting activity -> plan -> protocol -> intake)", prov_ok, nq))
xm = q('SELECT (COUNT(DISTINCT ?p) AS ?n) WHERE { ?p skos:exactMatch ?o }')[0][0].toPython()
ok = True
for name, got, exp in checks:
    flag = "OK " if got == exp else "MISMATCH"
    ok &= got == exp
    print(f"{flag} {name}: kg={got} synthesis={exp}")
print("871 cohort members:", n871)
print("publications cross-linked to ../graph nodes (skos:exactMatch):", xm)
print("triples:", len(g))
raise SystemExit(0 if ok else 1)
