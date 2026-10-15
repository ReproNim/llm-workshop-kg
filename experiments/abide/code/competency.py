"""Answer the shared competency questions Q1-Q12 by SPARQL over the Oxigraph store.

Q1-Q7 use the optimized query texts held in code/query_bench.py (OPT). Q8-Q12 query the simple2 volume view, the resource catalog and activity
snapshots, and the scope/promotion graph. Every query is timed.

Writes queries/Q*.rq, results/competency_answers.json and comparison/gold_answers.json.

Usage: uv run python code/competency.py
"""

import datetime as dt
import json
import time

from common import QUERIES, ROOT, write_json

P = """PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX schema: <http://schema.org/>
"""
G = "urn:repronim:abide:graph/"
Q8_PID = "MaxMun_c_0051332"
THREE_TOOL_REGIONS = ["UBERON_0000956", "UBERON_0002437", "UBERON_0001359", "UBERON_0001873", "UBERON_0001874", "UBERON_0001876",
                      "UBERON_0001882", "UBERON_0001897", "UBERON_0001954", "UBERON_0006514"]
REGION_NAMES = {"0000956": "cortical GM", "0002437": "cerebral WM", "0001359": "CSF", "0001873": "caudate", "0001874": "putamen",
                "0001876": "amygdala", "0001882": "accumbens", "0001897": "thalamus", "0001954": "hippocampus", "0006514": "pallidum"}
TOOL_NAME = {"http://stnava.github.io/ANTs/": "ANTs", "http://purl.org/nidash/fsl#": "FSL", "https://surfer.nmr.mgh.harvard.edu/": "FreeSurfer"}
CLASS_IRIS = {"nidm:": "http://purl.org/nidash/nidm#", "ex:": "urn:repronim:abide:", "prov:": "http://www.w3.org/ns/prov#"}

Q = {}
Q["Q8"] = P + f"""SELECT ?tool ?converter ?label ?region ?side ?volume ?sourceGraph WHERE {{
  VALUES ?region {{ {' '.join(f'<http://purl.obolibrary.org/obo/{r}>' for r in THREE_TOOL_REGIONS)} }}
  GRAPH <{G}view/volumes> {{ ?o ex:participant <urn:repronim:abide:participant/{Q8_PID}> ; ex:region ?region ; ex:tool ?tool ;
                                ex:measure ?m ; ex:side ?side ; ex:volume ?volume ; ex:sourceGraph ?sourceGraph . }}
  GRAPH <{G}view/volume_measures> {{ ?m rdfs:label ?label }}
  OPTIONAL {{ GRAPH <{G}link> {{ ?res ex:nidmToolNamespace ?tool ; ex:converterRepo ?converter }} }}
}} ORDER BY ?region ?side ?tool"""
Q["Q9"] = P + f"""SELECT ?cls ?direction ?name ?usage WHERE {{ GRAPH <{G}resources> {{
  {{ ?r ex:produces ?cls . BIND("produces" AS ?direction) }} UNION {{ ?r ex:consumes ?cls . BIND("consumes" AS ?direction) }}
  ?r schema:name ?name ; ex:usageInExperiment ?usage .
}} }} ORDER BY ?cls ?direction ?name"""
Q["Q9b"] = P + f"""SELECT ?usage ?name WHERE {{ GRAPH <{G}resources> {{ ?r schema:name ?name ; ex:usageInExperiment ?usage .
  FILTER (?usage IN ("executed", "data_source")) }} }} ORDER BY ?usage ?name"""
Q["Q11"] = P + f"""SELECT ?candidate ?item ?registry ?status ?gateType ?gateStatus ?evidence WHERE {{ GRAPH <{G}scope> {{
  ?candidate a ex:PromotionCandidate ; prov:used ?item ; ex:targetRegistry ?registry ; ex:promotionStatus ?status ; ex:gate ?g .
  ?g ex:gateType ?gateType ; ex:status ?gateStatus ; ex:evidence ?evidence .
  FILTER (?gateStatus != "pass")
}} }} ORDER BY ?candidate ?gateType"""
Q["Q15"] = P + f"""SELECT ?pub ?status ?title (GROUP_CONCAT(DISTINCT STR(?dataset); separator=" ") AS ?datasets) (COUNT(DISTINCT ?c) AS ?nClaims)
WHERE {{ GRAPH <{G}publications> {{
  VALUES ?dataset {{ <urn:repronim:abide:dataset/abide> <urn:repronim:abide:dataset/abide_i> <urn:repronim:abide:dataset/abide_ii> }}
  ?link a ex:DatasetPublicationLink ; ex:dataset ?dataset ; ex:status ?status ; ex:publication ?pub .
  OPTIONAL {{ ?pub dct:title ?title }}
  OPTIONAL {{ ?c ex:statedIn ?pub ; a ex:AbstractClaim }}
}} }} GROUP BY ?pub ?status ?title ORDER BY ?status DESC(?nClaims) ?pub"""
Q["Q15b"] = P + f"""SELECT ?snap ?t ?abstracts ?stated ?oaDM ?oaAB WHERE {{ GRAPH <{G}publication_links_activity> {{
  {{ SELECT (MAX(?t0) AS ?t) WHERE {{ ?s0 a ex:PublicationLinkSnapshot ; prov:generatedAtTime ?t0 }} }}
  ?snap a ex:PublicationLinkSnapshot ; prov:generatedAtTime ?t ; ex:abstractsLinked ?abstracts ; ex:abstractsUsesDataStated ?stated .
  ?snap ex:openalexCiting_dimartino2014_mentioningABIDE ?oaDM ; ex:openalexCiting_abraham2017_mentioningABIDE ?oaAB .
}} }}"""
Q["Q12"] = P + f"""SELECT ?item ?label ?level ?access ?egress ?reason ?policy WHERE {{ GRAPH <{G}scope> {{
  ?item ex:knowledgeScope <urn:repronim:abide:scope/pond> ; ex:accessLevel ?access .
  OPTIONAL {{ ?item ex:pondLevel ?level }}
  OPTIONAL {{ ?item rdfs:label ?label }}
  OPTIONAL {{ ?item ex:hasSensitivityProfile ?p . ?p ex:egressPermitted ?egress ; ex:egressReason ?reason }}
  OPTIONAL {{ ?item ex:promotionPolicy ?policy }}
}} }} ORDER BY ?level ?item"""


SOURCES = {
    "Q8": ["results/competency_answers.json", "results/simple2.json", "results/simple2_tool_agreement.csv"],
    "Q9": ["results/competency_answers.json", "results/resources_catalog.json"],
    "Q10": ["results/competency_answers.json", "graph/resource_activity.ttl", "results/find_resources_examples.txt"],
    "Q11": ["results/competency_answers.json", "results/scope.json"],
    "Q12": ["results/competency_answers.json", "results/scope.json"],
    "Q13": ["results/participant_ego.json", "results/participant_ego.ttl"],
    "Q14": ["results/element_coverage.json"],
    "Q15": ["results/competency_answers.json", "results/publications.json"],
}


def short(x) -> str:
    """Compact string form of a term value."""
    return str(x).replace("urn:repronim:abide:", "ex:")


def run(st, name: str, q: str) -> tuple[list[dict], float]:
    """Execute one query; return rows as dicts and seconds."""
    (QUERIES / f"{name}.rq").write_text(q)
    if name[1:].rstrip("b").isdigit() and int(name[1:].rstrip("b")) >= 8:
        (QUERIES / "optimized" / f"{name}.rq").write_text(q)
    t0 = time.time()
    res = st.query(q)
    vars_ = [v.value for v in res.variables]
    rows = [{v: short(s[i].value) for i, v in enumerate(vars_) if s[i] is not None} for s in res]
    return rows, round(time.time() - t0, 4)


def main() -> None:
    """Run every question and assemble gold answers."""
    from find_resources import search, store as resource_store
    from query_bench import OPT
    from store import open_store

    st = open_store()
    for k in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"):
        Q[k] = OPT[k]
    Q["Q5b"] = P + f"""SELECT ?change ?summary ?material WHERE {{ GRAPH <{G}core> {{
  ?change a ex:MeasuredChange ; ex:summary ?summary ; ex:materialChange ?material . }} }} ORDER BY ?change"""
    rows, secs = {}, {}
    for k in sorted(Q, key=lambda x: (len(x), x)):
        rows[k], secs[k] = run(st, k, Q[k])
    t0 = time.time()
    q10 = search(resource_store(), "export FreeSurfer stats to NIDM", step="idp_extraction_to_nidm", top=5)
    secs["Q10"] = round(time.time() - t0, 4)
    (QUERIES / "Q10.txt").write_text('find_resources.search("export FreeSurfer stats to NIDM", step="idp_extraction_to_nidm", top=5)\n')
    rows["Q10"] = q10

    q1 = {}
    for r in rows["Q1"]:
        q1.setdefault(r["cohort"], {})["ASD" if float(r["dx"]) == 1 else "TD"] = int(r["n"])
    q2, q3 = rows["Q2"][0], rows["Q3"][0]
    q6 = {r["review"]: r for r in rows["Q6"]}
    flagged = {r["kind"].replace("ex:", ""): int(r["nFlagged"]) for r in rows["Q5"]}
    material = [r for r in rows["Q5b"] if r["material"] == "true"]

    per_region = {}
    for r in rows["Q8"]:
        key = (r["region"].rsplit("_", 1)[-1], r["side"].rsplit("/", 1)[-1])
        per_region.setdefault(key, {})[TOOL_NAME[r["tool"]]] = (float(r["volume"]), r["label"], r.get("converter", "?"))
    q8_parts = []
    for (reg, side), tv in sorted(per_region.items()):
        if len(tv) == 3:
            vals = {t: v[0] for t, v in tv.items()}
            q8_parts.append(f"{REGION_NAMES.get(reg, reg)} {side}: " + ", ".join(f"{k} {v:,.0f}" for k, v in sorted(vals.items()))
                            + f" mm3 (max/min {max(vals.values()) / min(vals.values()):.2f})")
    ratios = [max(v[0] for v in tv.values()) / min(v[0] for v in tv.values()) for (reg, side), tv in per_region.items() if len(tv) == 3 and reg != "0001359"]
    producers = sorted({f"{t} via {v[2]}" for tv in per_region.values() for t, v in tv.items()})

    q9 = {}
    for r in rows["Q9"]:
        q9.setdefault(r["cls"], {"produces": [], "consumes": []})[r["direction"]].append(f"{r['name']} [{r['usage']}]")
    present = {}
    for cls in q9:
        for pre, iri in CLASS_IRIS.items():
            if cls.startswith(pre):
                c = st.query(f"SELECT (COUNT(DISTINCT ?s) AS ?n) WHERE {{ GRAPH ?g {{ ?s a <{iri}{cls[len(pre):]}> }} }}")
                present[cls] = int(next(iter(c))[0].value)
    if present.get("ex:BrainVolume") == 0:
        c = st.query(f"PREFIX ex: <urn:repronim:abide:> SELECT (COUNT(?o) AS ?n) WHERE {{ GRAPH <{G}view/volumes> {{ ?o a ex:VolumeObservation }} }}")
        present["ex:BrainVolume"] = f"0 typed; {int(next(iter(c))[0].value):,} volume observations in view/volumes"
    used_here = {}
    for r in rows["Q9b"]:
        used_here.setdefault(r["usage"], []).append(r["name"])

    now = dt.datetime.now(dt.timezone.utc)
    active = [r for r in q10 if (r["commits_90d"] or 0) > 0]
    q11 = {}
    for r in rows["Q11"]:
        q11.setdefault((r["candidate"].rsplit("/", 1)[-1], r["status"], r["registry"]), []).append(f"{r['gateType']}={r['gateStatus']}")
    ego = json.loads((ROOT / "results/participant_ego.json").read_text())
    cov = json.loads((ROOT / "results/element_coverage.json").read_text())
    q15 = rows["Q15"]
    snap = rows["Q15b"][0] if rows["Q15b"] else {}
    abide_abs = [r for r in q15 if r["pub"].startswith("ex:abstract/")]
    stated_abs = [r for r in abide_abs if r["status"] == "uses-data (stated)"]
    pubs_json = json.loads((ROOT / "results/publications.json").read_text())
    stay = [r for r in rows["Q12"] if r.get("policy") or r.get("egress") not in (None, "permitted") or r["access"] == "restricted"]

    gold = {
        "Q1": f"Analyst B's QC (three-rater visual QC + full CC200 coverage + mean FD < 0.2 mm): {sum(q1['ex:cohort/B_v1'].values())} participants "
              f"({q1['ex:cohort/B_v1']['ASD']} ASD, {q1['ex:cohort/B_v1']['TD']} TD). After the FD < 0.15 revision: {sum(q1['ex:cohort/B_v2'].values())} "
              f"({q1['ex:cohort/B_v2']['ASD']} ASD, {q1['ex:cohort/B_v2']['TD']} TD). Rater QC alone (Abraham 2017 reconstruction): "
              f"{sum(q1['ex:cohort/abraham2017_reconstructed'].values())} vs 871 reported.",
        "Q2": f"{q2['overlap']} participants are in both cohorts (A is a strict subset of B). {q2['bTestExcludedByV2']} of B's test participants are excluded by the tightened rule.",
        "Q3": f"Leuven_1_0050682: connectivity {q3['conn']} <- {q3['method']} <- time series {q3['tsUrl']} (sha256 {q3['tsSha'][:12]}...) <- {q3['software']} "
              f"[{q3['strategy']}; {q3['nuisance']}; GSR={q3['gsr']}; band-pass {q3['bandpass']} Hz] <- raw scan {q3['rawUrl']}.",
        "Q4": "; ".join(f"{r['paper'].split('/')[-1]}: question \"{r['question']}\"; claim \"{r['quote']}\" is {r['claimType']} ({r['scope']})" for r in rows["Q4"]),
        "Q5": f"Flagged for reassessment by graph traversal: {flagged}. After recomputation {len(material)} of {len(rows['Q5b'])} result families changed materially"
              + (": " + "; ".join(f"{r['change'].split('/')[-1]}: {r['summary']}" for r in material) if material else "") + ".",
        "Q6": " | ".join(f"{k.split('/')[-1]}: {v['verdict']} (pooled d={float(v['d']):.3f}, {v['nConsistent']}/{v['nSites']} sites same direction, "
                         f"{v['nInd']} independent participants)" for k, v in sorted(q6.items())),
        "Q7": "; ".join(sorted({f"{r['review'].split('/')[-1]} by {r['reviewer']} as {r['role'].replace('ex:', '')} on {r['target'].split('/')[-1]}: {r['verdict']}" for r in rows["Q7"]})),
        "Q8": f"{Q8_PID} (ndar:src_subject_id 51332, ReproNim simple2 MaxMun_c graph). Producers: {'; '.join(producers)}. " + "; ".join(q8_parts)
              + f". Across tools, max/min ratios for tissue and subcortical structures range {min(ratios):.2f}-{max(ratios):.2f} (closest: thalamus, "
                "caudate, hippocampus; furthest: amygdala, accumbens, pallidum); CSF differs by two orders of magnitude because FSL reports total CSF "
                "while FreeSurfer and ANTs report the ventricular CSF label under the same UBERON term.",
        "Q9": "; ".join(f"{cls} (instances in the store: {present.get(cls, 'n/a')}) <- produced by {', '.join(v['produces']) or 'none'}"
                        + (f"; consumed by {', '.join(v['consumes'])}" if v["consumes"] else "") for cls, v in sorted(q9.items()))
               + f". Executed here: {', '.join(used_here.get('executed', []))}. Used as data sources: {', '.join(used_here.get('data_source', []))}. "
               "Every other listed resource is a pointer only (not run).",
        "Q10": ("; ".join(f"{r['name']}: {r['commits_90d']} default-branch commits in 90 d, last commit {r['last_commit'] or r['last_push']} "
                          f"(as of {r['as_of']}; snapshot {r['snapshot_age_hours']} h old when answered)" for r in active)
                or "none with default-branch commits in the last 90 days")
               + ". Not active in the last 90 days: " + "; ".join(f"{r['name']} (as of {r['as_of']})" for r in q10 if r not in active) + ".",
        "Q11": "; ".join(f"{c} [{st_}] -> {reg}: unmet {', '.join(g)}" for (c, st_, reg), g in sorted(q11.items())),
        "Q13": f"{ego['participant']}: {ego['construct_triples']} source triples within two hops (results/participant_ego.ttl), grouped into {ego['figure_nodes']} nodes: "
               + "; ".join(n["label"].replace("\n", " ") for n in ego["nodes"] if n["id"] != "P"),
        "Q14": "; ".join(f"{k}: {v['n']} ({v['by_dx'].get('ASD', 0)} ASD, {v['by_dx'].get('TD', 0)} TD; missing at {len(v['sites_with_none'])} sites)" for k, v in cov["elements"].items())
               + ". Limits: " + "; ".join(f"{k} -> {v['n']} participants, limited by {v['limiting_element']}" for k, v in cov["analysis_requirements"].items()) + ".",
        "Q15": f"As of {snap.get('t', '?')} (latest publication-link snapshot; AbstractAtlas OHBM 2026 bundle pinned by hash, repo commit 181652e2): "
               f"{len(abide_abs)} abstracts mention ABIDE ({len(stated_abs)} state they used ABIDE data, {len(abide_abs) - len(stated_abs)} mention it only; "
               f"regex, hand check 15/17 stated uses correct, posters 1217 and 639 are false positives); those abstracts carry "
               f"{sum(int(r.get('nClaims', 0)) for r in abide_abs)} AbstractAtlas claims ({sum(int(r.get('nClaims', 0)) for r in stated_abs)} in the stated-use abstracts). "
               f"OpenAlex (pulled {pubs_json.get('openalex_pulled_at', '?')}): {snap.get('oaDM', '?')} works cite Di Martino 2014 and {snap.get('oaAB', '?')} cite Abraham 2017 "
               "while naming ABIDE in title/abstract (status candidate; top 50 per paper stored as nodes). "
               "Largest stated-use abstracts: " + "; ".join(f"poster {r['pub'].rsplit('/', 1)[-1]} {r.get('title', '')[:60]} ({r.get('nClaims', 0)} claims"
                                                  + ("; false positive by hand check)" if r['pub'].rsplit('/', 1)[-1] in ("1217", "639") else ")") for r in stated_abs[:5]) + ".",
        "Q12": "; ".join(f"{r.get('label', r['item'])} (pond:{r.get('level', '')}, {r['access']}): "
                         + (r.get("policy") or f"egress {r.get('egress', 'n/a')}: {r.get('reason', '')}") for r in stay)
               + ". Other pond items (analyst cohorts, claims, reviews, local rules) are egress-permitted but stay until a promotion passes its gates.",
    }
    write_json("competency_answers.json", {"engine": "pyoxigraph (on-disk store)", "query_seconds": secs, "rows": rows, "gold": gold,
                                          "answered_at": now.isoformat(timespec="seconds")})
    questions = json.loads((ROOT / "comparison/questions.json").read_text())
    (ROOT / "comparison/gold_answers.json").write_text(json.dumps({
        "answered_at": now.isoformat(timespec="seconds"),
        "answers": [{"id": q["id"], "question": q["text"], "gold": gold[q["id"]],
                     "queries": ([f"queries/{k}.rq" for k in Q if k in (q["id"], q["id"] + "b")] or {"Q10": ["queries/Q10.txt"], "Q13": ["queries/Q13_construct.rq"], "Q14": ["queries/Q14.rq"]}.get(q["id"], [])),
                     "result_files": SOURCES.get(q["id"], ["results/competency_answers.json"]),
                     "seconds": secs.get(q["id"])} for q in questions["questions"]],
    }, indent=1))
    for f in sorted(QUERIES.glob("Q13_*.rq")) + [QUERIES / "Q14.rq", QUERIES / "Q10.txt"]:
        if f.exists():
            (QUERIES / "optimized" / f.name).write_text(f.read_text())
    print(json.dumps(secs))
    for k, v in gold.items():
        print(k, v[:300])


if __name__ == "__main__":
    main()
