"""OPTIONAL, NOT RUN BY rebuild.sh. Holds OPT, the optimized query texts that revision.py, umap_phenotype.py and
competency.py run on Oxigraph. Running it as a script compares engines (abandoned; results not shipped).

Original vs optimized SPARQL, on rdflib (in-memory) and Oxigraph (on-disk store).

Every (query, version, engine) runs in its own subprocess with a timeout, so peak RSS is per run.
Load time and query time are reported separately. Each result set is hashed (sorted rows of lexical
values) so original and optimized versions can be shown to return identical rows.

Writes queries/original/*.rq, queries/optimized/*.rq and results/query_timings.json.

Usage: uv run python code/query_bench.py [--rdflib-timeout 300] [--only name1,name2]
"""

import hashlib
import json
import resource
import subprocess
import sys
import time

from common import DATA, GRAPH, QUERIES, RESULTS, ROOT

STORE = DATA / "derived/oxigraph_store"
VIEWS = DATA / "derived/views"
G = "urn:repronim:abide:graph/"
S2 = DATA / "repronim_simple2"
SITE1 = "datasets.datalad.org/abide/RawDataBIDS/CMU_a/nidm.ttl"
CDES = ["cde_tools/ants_cde.ttl", "cde_tools/fs_cde.ttl", "cde_tools/fsl_cde.ttl"]
PX = """PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
"""
CORE = f"<{G}core>"
CORE1 = f"<{G}core_v1>"
PM = f"<{G}view/phenotype_matrix>"
TC = f"<{G}view/type_closure>"


def originals() -> dict[str, str]:
    """Original query texts as first written (default/union graph, no views)."""
    import queries_original as qo

    q = {k: v for k, v in qo.Q.items() if k in ("Q1", "Q2", "Q4", "Q5", "Q6", "Q7")}
    q["Q3"] = qo.Q["Q3"] % "Leuven_1_0050682"
    q["revision_participants"] = qo.Q_PARTICIPANTS
    q["revision_folds"] = qo.Q_FOLDS
    q["revision_downstream"] = qo.Q_DOWNSTREAM
    q["phenotype_matrix"] = qo.PHENOTYPE_MATRIX
    q["simple2_query"] = (S2 / "queries/simple2_query.sparql").read_text()
    return q


OPT = {
    "Q1": PX + f"""SELECT ?cohort ?dx (COUNT(DISTINCT ?p) AS ?n) WHERE {{
  VALUES ?cohort {{ <urn:repronim:abide:cohort/B_v1> <urn:repronim:abide:cohort/B_v2> <urn:repronim:abide:cohort/abraham2017_reconstructed> }}
  GRAPH {CORE} {{ ?cohort prov:hadMember ?p }}
  GRAPH {PM} {{ ?p <urn:repronim:abide:variable/DX_GROUP> ?dx }}
}} GROUP BY ?cohort ?dx ORDER BY ?cohort ?dx""",
    "Q2": PX + f"""SELECT (COUNT(DISTINCT ?both) AS ?overlap) (COUNT(DISTINCT ?dropped) AS ?bTestExcludedByV2) WHERE {{ GRAPH {CORE} {{
  {{ <urn:repronim:abide:cohort/A_v1> prov:hadMember ?both . <urn:repronim:abide:cohort/B_v1> prov:hadMember ?both . }}
  UNION
  {{ <urn:repronim:abide:cohort/B_v1> prov:hadMember ?dropped .
     FILTER NOT EXISTS {{ <urn:repronim:abide:cohort/B_v2> prov:hadMember ?dropped }}
     FILTER EXISTS {{ ?fold dct:isPartOf <urn:repronim:abide:analysis/B_v1> ; ex:testedOn ?c . ?c ex:participant ?dropped }} }}
}} }}""",
    "Q3": PX + f"""SELECT ?conn ?method ?ts ?tsUrl ?tsSha ?pre ?software ?raw ?rawUrl ?cfg ?strategy ?nuisance ?gsr ?bandpass WHERE {{ GRAPH {CORE} {{
  VALUES ?p {{ <urn:repronim:abide:participant/Leuven_1_0050682> }}
  ?conn ex:participant ?p ; a nidm:DerivativeObject ; prov:wasDerivedFrom ?ts ; prov:wasGeneratedBy ?ca .
  ?ca ex:method ?method .
  ?ts prov:atLocation ?tsUrl ; <http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions#sha256> ?tsSha ; prov:wasGeneratedBy ?pre .
  ?pre prov:wasAssociatedWith ?swa ; prov:used ?raw , ?cfg . ?swa rdfs:label ?software .
  ?raw a nidm:AcquisitionObject ; prov:atLocation ?rawUrl .
  ?cfg ex:strategy ?strategy ; ex:nuisance ?nuisance ; ex:globalSignalRegression ?gsr ; ex:bandpassHz ?bandpass .
}} }}""",
    "Q4": PX + f"""SELECT ?paper ?question ?claim ?claimType ?scope ?quote ?locator ?cohortQuote WHERE {{ GRAPH {CORE} {{
  ?claim a ex:Claim ; ex:statedIn ?paper ; ex:claimType ?claimType ; ex:scope ?scope ; ex:addresses ?q ; ex:hasEvidence ?ev .
  ?ev ex:quote ?quote ; ex:locator ?locator .
  ?q ex:hasEvidence ?qe . ?qe ex:quote ?question .
  OPTIONAL {{ ?claim ex:dependsOn ?coh . ?coh a ex:ReportedCohort ; ex:hasEvidence ?ce . ?ce ex:quote ?cohortQuote . }}
}} }} ORDER BY ?paper ?claim""",
    "Q5": PX + f"""SELECT ?kind (COUNT(DISTINCT ?e) AS ?nFlagged) WHERE {{ GRAPH {CORE} {{
  VALUES ?kind {{ ex:Result ex:Claim ex:EvidenceAssessment }}
  ?act a prov:Activity . ?e ex:flaggedForReassessmentBy ?act ; a ?kind .
}} }} GROUP BY ?kind""",
    "Q6": PX + f"""SELECT ?review ?verdict ?d ?nInd ?nSites ?nConsistent ?caveat WHERE {{ GRAPH {CORE} {{
  VALUES ?review {{ <urn:repronim:abide:review/B_reviews_A_v1> <urn:repronim:abide:review/B_reviews_A_v2> }}
  ?review ex:verdict ?verdict ; ex:pooled_d_fixed_effect ?d ; ex:n_independent_participants ?nInd ;
          ex:n_sites_usable ?nSites ; ex:n_sites_direction_consistent ?nConsistent ; ex:caveat ?caveat .
}} }}""",
    "Q7": PX + f"""SELECT ?review ?reviewer ?role ?target ?evidence ?verdict WHERE {{ GRAPH {CORE} {{
  ?review a ex:EvidenceAssessment ; prov:wasGeneratedBy ?act ; prov:wasAttributedTo ?r ; ex:target ?target ; ex:verdict ?verdict ;
          prov:wasDerivedFrom ?evidence .
  ?act prov:qualifiedAssociation ?as . ?as prov:agent ?r ; prov:hadRole ?role .
  ?r rdfs:label ?reviewer .
}} }} ORDER BY ?review ?evidence""",
    "revision_participants": PX + f"""SELECT ?cohort ?participant ?fd WHERE {{ GRAPH {CORE1} {{
  ?new prov:wasRevisionOf ?old ; ex:threshold ?thr ; ex:variable ?var .
  ?sel prov:used ?old . ?cohort prov:wasGeneratedBy ?sel ; prov:hadMember ?participant .
  ?rec ex:participant ?participant ; ?var ?fd .
  FILTER (?fd >= ?thr)
}} }}""",
    "revision_folds": PX + f"""SELECT ?fold ?site (SUM(?isTest) AS ?nTest) (SUM(?isTrain) AS ?nTrain) WHERE {{ GRAPH {CORE1} {{
  {{ SELECT DISTINCT ?p WHERE {{ ?new prov:wasRevisionOf ?old ; ex:threshold ?thr ; ex:variable ?var .
       ?sel prov:used ?old . ?cohort prov:wasGeneratedBy ?sel ; prov:hadMember ?p . ?rec ex:participant ?p ; ?var ?fd . FILTER (?fd >= ?thr) }} }}
  ?conn ex:participant ?p ; a nidm:DerivativeObject .
  {{ ?fold ex:testedOn ?conn . BIND(1 AS ?isTest) BIND(0 AS ?isTrain) }} UNION {{ ?fold ex:trainedOn ?conn . BIND(0 AS ?isTest) BIND(1 AS ?isTrain) }}
  ?fold ex:heldOutSite ?site .
}} }} GROUP BY ?fold ?site ORDER BY ?site""",
    "revision_downstream": PX + f"""SELECT DISTINCT ?entity ?kind WHERE {{ GRAPH {CORE1} {{
  ?new prov:wasRevisionOf ?old . ?sel prov:used ?old . ?cohort prov:wasGeneratedBy ?sel .
  ?analysis prov:used ?cohort .
  {{ ?entity prov:wasGeneratedBy ?analysis . BIND("result" AS ?kind) }}
  UNION {{ ?fold dct:isPartOf ?analysis . ?entity prov:wasGeneratedBy ?fold . BIND("fold_result" AS ?kind) }}
  UNION {{ ?fold dct:isPartOf ?analysis . ?r prov:wasGeneratedBy ?fold . ?entity prov:wasDerivedFrom ?r . BIND("pooled_result" AS ?kind) }}
  UNION {{ {{ ?r prov:wasGeneratedBy ?analysis }} UNION {{ ?fold dct:isPartOf ?analysis . ?fr prov:wasGeneratedBy ?fold . ?r prov:wasDerivedFrom ?fr }}
          VALUES ?t {{ ex:Claim ex:EvidenceAssessment }} ?entity a ?t ; prov:wasDerivedFrom+ ?r . BIND("claim_or_review" AS ?kind) }}
  UNION {{ ?entity prov:wasDerivedFrom ?cohort . BIND("result" AS ?kind) }}
}} }}""",
    "phenotype_matrix": PX + f"""SELECT ?fid ?site ?dx ?sex ?var ?value ?thick ?conn WHERE {{
  GRAPH {CORE} {{ <urn:repronim:abide:cohort/B_v1> prov:hadMember ?p . ?p rdfs:label ?fid . }}
  GRAPH {PM} {{ ?p ex:site ?site ; <urn:repronim:abide:variable/DX_GROUP> ?dx ; <urn:repronim:abide:variable/SEX> ?sex .
    OPTIONAL {{ VALUES ?var {{ <urn:repronim:abide:variable/AGE_AT_SCAN> <urn:repronim:abide:variable/FIQ> <urn:repronim:abide:variable/VIQ>
                               <urn:repronim:abide:variable/PIQ> <urn:repronim:abide:variable/SRS_RAW_TOTAL> }} ?p ?var ?value }} }}
  OPTIONAL {{ GRAPH {CORE} {{ ?idp ex:participant ?p ; ex:meanCorticalThickness ?thick }} }}
  OPTIONAL {{ GRAPH {CORE} {{ ?c ex:participant ?p ; ex:meanFisherZ ?conn }} }}
}}""",
}

OPT["simple2_query"] = """prefix prov: <http://www.w3.org/ns/prov#>
prefix ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
prefix nidm: <http://purl.org/nidash/nidm#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix ilx: <http://uri.interlex.org/>
prefix ncit: <http://ncitt.ncit.nih.gov/>
# Same result set as ReproNim simple2_query.sparql. Changes: the six demographic data elements are bound
# first through one VALUES block instead of six disconnected groups; the a/rdfs:subClassOf path is read
# from the materialized type_closure view; tool and subject are reached from the activity node.
select distinct ?study ?ID ?Age ?dx ?Gender ?FIQ ?PIQ ?VIQ ?tool ?softwareLabel ?federatedLabel ?laterality ?volume
where {
  VALUES (?ageC ?sexC ?dxC ?fiqC ?piqC ?viqC) { (ilx:ilx_0100400 <http://uri.interlex.org/base/ilx_0101292> ncit:Diagnosis
      <http://uri.interlex.org/base/ilx_0739365> <http://uri.interlex.org/base/ilx_0739363> <http://uri.interlex.org/base/ilx_0739359>) }
  ?age_measure a nidm:PersonalDataElement ; nidm:isAbout ?ageC .
  ?sex_measure a nidm:PersonalDataElement ; nidm:isAbout ?sexC .
  ?DX_measure a nidm:PersonalDataElement ; nidm:isAbout ?dxC .
  ?FIQ_measure a nidm:PersonalDataElement ; nidm:isAbout ?fiqC .
  ?PIQ_measure a nidm:PersonalDataElement ; nidm:isAbout ?piqC .
  ?VIQ_measure a nidm:PersonalDataElement ; nidm:isAbout ?viqC .
  ?as_entity ?age_measure ?Age ; ?sex_measure ?GenderCoded ; ?FIQ_measure ?FIQ ; ?PIQ_measure ?PIQ ; ?VIQ_measure ?VIQ ; ?DX_measure ?dx ;
             prov:wasGeneratedBy ?as_activity .
  ?as_activity prov:qualifiedAssociation ?asA . ?asA prov:agent ?asAgent . ?asAgent ndar:src_subject_id ?ID .
  ?subj ndar:src_subject_id ?ID .
  ?a2 prov:agent ?subj . ?tool_act prov:qualifiedAssociation ?a2 , ?a1 ; a prov:Activity .
  ?a1 prov:agent ?sw . ?sw nidm:NIDM_0000164 ?tool .
  ?tool_entity prov:wasGeneratedBy ?tool_act ; a prov:Entity ; ?measure ?volume .
  GRAPH <urn:repronim:abide:graph/view/type_closure> { ?measure a nidm:DataElement }
  ?measure rdfs:label ?softwareLabel ; nidm:measureOf <http://uri.interlex.org/base/ilx_0112559> ; nidm:datumType <http://uri.interlex.org/base/ilx_0738276> .
  OPTIONAL { ?measure nidm:isAbout ?federatedLabel }
  OPTIONAL { ?measure nidm:hasLaterality ?laterality }
  bind(IF((?GenderCoded = "1" || ?GenderCoded = "Male"^^xsd:string), "Male"^^xsd:string, "Female"^^xsd:string) as ?Gender) .
} order by ?study"""

# Which graphs each query needs, for rdflib loading and Oxigraph scoping.
SCOPE = {k: "core" for k in OPT}
SCOPE.update({"revision_participants": "core_v1", "revision_folds": "core_v1", "revision_downstream": "core_v1", "simple2_query": "simple2"})


def row_hash(rows: list[tuple]) -> str:
    """Order-independent hash of a result set."""
    return hashlib.sha256("\n".join(sorted("\t".join(r) for r in rows)).encode()).hexdigest()


def peak_rss_mb() -> float:
    """Peak RSS of this process in MB (macOS reports bytes, Linux kilobytes)."""
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return round(r / 1e6 if sys.platform == "darwin" else r / 1e3, 1)


def run_one(spec: dict) -> dict:
    """Execute one query in this process and report timings."""
    t0 = time.time()
    q = (QUERIES / spec["version"] / f"{spec['name']}.rq").read_text()
    scope, subset = SCOPE[spec["name"]], spec.get("subset")
    if spec["engine"] == "rdflib":
        from rdflib import Dataset, URIRef

        ds = Dataset(default_union=True)
        if scope == "simple2":
            for rel in [SITE1] + CDES:
                ds.graph(URIRef("urn:repronim:simple2:" + rel)).parse(S2 / rel)
            if spec["version"] == "optimized":
                ds.graph(URIRef(G + "view/type_closure")).parse(VIEWS / "type_closure.nt")
        else:
            ds.graph(URIRef(G + scope)).parse(GRAPH / ("abide_kg_v1.ttl" if scope == "core_v1" else "abide_kg.ttl"))
            if spec["version"] == "optimized" and scope == "core":
                ds.graph(URIRef(G + "view/phenotype_matrix")).parse(VIEWS / "phenotype_matrix.nt")
        t1 = time.time()
        rows = [tuple("" if v is None else str(v) for v in r) for r in ds.query(q)]
    else:
        import pyoxigraph as ox

        st = ox.Store.read_only(str(STORE))
        t1 = time.time()
        kw = {}
        if scope == "simple2":
            graphs = [ox.NamedNode("urn:repronim:simple2:" + r) for r in ([SITE1] + CDES)] if subset == "1site" else [g for g in st.named_graphs() if g.value.startswith("urn:repronim:simple2:")]
            if spec["version"] == "original":
                kw = {"default_graph": graphs}
            else:
                kw = {"default_graph": graphs, "named_graphs": [ox.NamedNode(G + "view/type_closure")]}
        elif spec["version"] == "original":
            kw = {"default_graph": [ox.NamedNode(G + scope)]}
        res = st.query(q, **kw)
        rows = [tuple("" if s[i] is None else s[i].value for i in range(len(res.variables))) for s in res]
    t2 = time.time()
    return {"load_s": round(t1 - t0, 2), "query_s": round(t2 - t1, 3), "rows": len(rows), "result_sha256": row_hash(rows), "peak_rss_mb": peak_rss_mb()}


def main() -> None:
    """Write the query files and benchmark every combination."""
    if "--summarize" in sys.argv:
        d = json.loads((RESULTS / "query_timings.json").read_text())
        write(d["runs"], d["rdflib_timeout_s"])
        return
    if "--one" in sys.argv:
        print(json.dumps(run_one(json.loads(sys.argv[sys.argv.index("--one") + 1]))))
        return
    timeout = int(sys.argv[sys.argv.index("--rdflib-timeout") + 1]) if "--rdflib-timeout" in sys.argv else 300
    only = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
    orig = originals()
    for v, qs in (("original", orig), ("optimized", OPT)):
        (QUERIES / v).mkdir(parents=True, exist_ok=True)
        for k, q in qs.items():
            (QUERIES / v / f"{k}.rq").write_text(q)
    runs = []
    for name in OPT:
        if only and name not in only:
            continue
        combos = [("rdflib", None), ("oxigraph", None)]
        if name == "simple2_query":
            combos = [("rdflib", "1site"), ("oxigraph", "1site"), ("oxigraph", "all24")]
        for engine, subset in combos:
            for version in ("original", "optimized"):
                spec = {"name": name, "version": version, "engine": engine, "subset": subset}
                t0 = time.time()
                try:
                    out = subprocess.run([sys.executable, __file__, "--one", json.dumps(spec)], capture_output=True, text=True,
                                         timeout=timeout if engine == "rdflib" else 1800)
                    rec = json.loads(out.stdout.strip().splitlines()[-1]) if out.returncode == 0 else {"error": out.stderr[-400:]}
                except subprocess.TimeoutExpired:
                    rec = {"timeout_s": timeout if engine == "rdflib" else 1800}
                rec["wall_s"] = round(time.time() - t0, 2)
                runs.append({**spec, **rec})
                print(name, engine, subset or "", version, {k: rec.get(k) for k in ("query_s", "rows", "peak_rss_mb", "timeout_s", "error")}, flush=True)
    if only and (RESULTS / "query_timings.json").exists():
        old = json.loads((RESULTS / "query_timings.json").read_text())["runs"]
        runs = [r for r in old if r["name"] not in only] + runs
    write(runs, timeout)


NOTES = {
    "phenotype_matrix": "The original as first written (queries/original/phenotype_matrix.as_first_written.rq) used rdfs:label without "
                        "declaring PREFIX rdfs. rdflib accepts that (built-in prefix); Oxigraph rejects it as a parse error. The only change "
                        "in queries/original/phenotype_matrix.rq is the added PREFIX line.",
    "revision_folds": "The original double-counts participants who are in both cohorts; the optimized query is the correct one, so the "
                      "two versions' hashes differ on purpose.",
    "cross_engine_hashes": "Where rdflib and Oxigraph hashes differ with equal row counts, the rows differ only in how numeric literals "
                           "are printed (rdflib normalizes 1 to 1.0, Oxigraph keeps the stored form; checked for Q1 and phenotype_matrix); within one engine, original and optimized agree except "
                           "revision_folds.",
    "timings": "Laptop timings depend on load; the machine was on battery, and an idle sleep during an earlier run inflated one "
               "record, so the affected queries were rerun under caffeinate. "
               "rdflib arms are capped at --rdflib-timeout, Oxigraph arms at 1800 s, each in its own subprocess. The first local run's all24 "
               "simple2 arms failed because the store was rebuilt under them; in the rerun the original hit the 1800 s cap and the optimized "
               "arm was stopped by hand at ~25 min. All other records are from runs with the store intact.",
}


def cell(r: dict | None, timeout: int) -> str:
    """Display string for one run."""
    if r is None:
        return "not run"
    if "killed" in r.get("note", ""):
        return f"killed by hand at {r['wall_s']:.0f} s (cap 1800 s), no result"
    if "timeout_s" in r:
        return f">{r['timeout_s']} s (timeout)"
    if "error" in r:
        return "error: " + (r["error"].strip().splitlines() or ["(no stderr; process killed)"])[-1][:120]
    return f"{r['wall_s']} s, {r['peak_rss_mb']} MB, {r['rows']} rows, {r['result_sha256'][:8]}"


def write(runs: list, timeout: int) -> None:
    """Write results/query_timings.json: runs, a display table, cross-version agreement and notes."""
    by = {}
    for r in runs:
        by.setdefault((r["name"], r["subset"]), []).append(r)
    agree, table = {}, []
    for (name, subset), rs in by.items():
        key = f"{name}{'@' + subset if subset else ''}"
        hashes = {r["result_sha256"] for r in rs if "result_sha256" in r}
        same_engine = {e: len({r["result_sha256"] for r in rs if r["engine"] == e and "result_sha256" in r}) == 1
                       and sum(1 for r in rs if r["engine"] == e and "result_sha256" in r) == 2 for e in ("rdflib", "oxigraph")}
        agree[key] = {"identical_across_versions_and_engines": len(hashes) == 1, "n_distinct_hashes": len(hashes),
                      "original_equals_optimized": same_engine}
        get = {(r["engine"], r["version"]): r for r in rs}
        table.append({"query": key, **{f"{e}_{v}": cell(get.get((e, v)), timeout) for e in ("rdflib", "oxigraph") for v in ("original", "optimized")}})
    (RESULTS / "query_timings.json").write_text(json.dumps({"platform": sys.platform, "rdflib_timeout_s": timeout,
                                                            "cell_format": "wall s (subprocess incl. load), peak RSS MB, rows, result sha256[:8]",
                                                            "table": table, "agreement": agree, "notes": NOTES, "runs": runs}, indent=1))

if __name__ == "__main__":
    main()
