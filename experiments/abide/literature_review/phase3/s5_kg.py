"""Step 5: literature_kg.ttl — publication -> ABIDE dataset links with cohort, method, claim and evidence nodes.

Dataset IRIs reuse ../graph/publications.ttl (urn:repronim:abide:dataset/abide_i, abide_ii); ../graph is read only
to find existing publication nodes with the same DOI (linked by skos:exactMatch). The link class and properties
follow ../graph (ex:DatasetPublicationLink, ex:dataset, ex:publication, ex:status, ex:evidenceQuote).
"""
import json
import re
from pathlib import Path
from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import DCTERMS, PROV, RDF, RDFS, SKOS, XSD
from common import ROOT, norm

EX = Namespace("urn:repronim:abide:")
LR = Namespace("urn:repronim:abide:litreview/")
INTAKE = Namespace("urn:repronim-talk:abide-review:")
SLR = Namespace("https://w3id.org/slr-ontology/")
DS = {"ABIDE I": [EX["dataset/abide_i"]], "ABIDE II": [EX["dataset/abide_ii"]],
      "ABIDE I+II": [EX["dataset/abide_i"], EX["dataset/abide_ii"]]}
REVIEW_IRI = URIRef("urn:synthscholar:review:review_local_20261015_abide_rsfmri")
K2 = "CL2 Motion/QC rule reported (metric and threshold, e.g. mean FD cut-off; rater QC)?"


def doi_iri(doi):
    return URIRef("https://doi.org/" + doi)


def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")


def graph_pub_nodes():
    """DOI -> existing publication nodes in ../graph (read only)."""
    out = {}
    gdir = ROOT.parent / "graph"
    for f in ("papers.ttl", "publications.ttl"):
        gg = Graph()
        gg.parse(gdir / f)
        for s, o in gg.subject_objects(DCTERMS.identifier):
            if (s, RDF.type, EX.Publication) in gg and str(o).lower().startswith("https://doi.org/"):
                out.setdefault(str(o)[16:].lower(), set()).add(str(s))
    return out


def locate(quote, text):
    """Character offset of the quote in the raw full text when it occurs verbatim, else None."""
    i = text.find(quote)
    return i if i >= 0 else None


def main():
    recs = json.load(open(ROOT / "phase3" / "records_verified.json"))
    corpus = {e["pmid"]: e for e in json.load(open(ROOT / "corpus.json"))["items"]}
    syn = json.load(open(ROOT / "results_synthesis.json"))
    ev = syn["evaluation"]
    per = syn["per_paper_categories"]
    integ = set(json.load(open(ROOT / "phase3" / "integrity.json"))["mismatched"])
    gnodes = graph_pub_nodes()
    g = Graph()
    for p, ns in [("ex", EX), ("lr", LR), ("prov", PROV), ("dct", DCTERMS), ("skos", SKOS), ("slr", SLR),
                  ("intake", INTAKE), ("rdfs", RDFS), ("xsd", XSD)]:
        g.bind(p, ns)
    g.parse(ROOT / "intake_provenance.ttl")  # user's protocol decisions (slr:UserInput) — the plan's provenance

    # ---- plan, agents, activities ----
    plan = LR["plan/protocol"]
    g.add((plan, RDF.type, PROV.Plan)); g.add((plan, RDF.type, PROV.Entity))
    g.add((plan, RDFS.label, Literal("Review protocol (protocol.json): RQ1-RQ6, CL1-CL8, PROBAST/JBI appraisal")))
    g.add((plan, PROV.atLocation, URIRef("file:protocol.json")))
    g.add((plan, PROV.wasGeneratedBy, INTAKE["intake-session"]))
    for ui in ("ui-scope", "ui-corpus", "ui-execution", "ui-appraisal"):
        g.add((plan, PROV.wasInfluencedBy, INTAKE[ui]))
    instr = LR["plan/charting_instructions"]
    g.add((instr, RDF.type, PROV.Plan)); g.add((instr, PROV.atLocation, URIRef("file:charting_instructions.md")))
    g.add((instr, PROV.wasDerivedFrom, plan))
    corpus_ent = LR["corpus"]
    g.add((corpus_ent, RDF.type, PROV.Entity)); g.add((corpus_ent, PROV.atLocation, URIRef("file:corpus.json")))
    g.add((corpus_ent, RDFS.label, Literal("99 open-access full texts (PyMuPDF)")))

    merge = LR["activity/phase3-merge"]
    merge_agent = LR["agent/phase3-merge"]
    g.add((merge_agent, RDF.type, PROV.SoftwareAgent))
    g.add((merge_agent, RDFS.label, Literal("Phase 3 merge agent (Claude Code sub-agent)")))
    g.add((merge_agent, EX.model, Literal("claude-opus-5-5")))
    g.add((merge, RDF.type, PROV.Activity))
    g.add((merge, RDFS.label, Literal("Integrity check, quote re-verification, merge, synthesis and KG build (phase3/*.py)")))
    g.add((merge, PROV.wasAssociatedWith, merge_agent))
    qa = BNode(); g.add((merge, PROV.qualifiedAssociation, qa)); g.add((qa, RDF.type, PROV.Association))
    g.add((qa, PROV.agent, merge_agent)); g.add((qa, PROV.hadPlan, plan))
    g.add((merge, PROV.used, corpus_ent))
    g.add((LR["synthesis"], RDF.type, PROV.Entity)); g.add((LR["synthesis"], PROV.atLocation, URIRef("file:results_synthesis.json")))
    g.add((LR["synthesis"], PROV.wasGeneratedBy, merge))
    g.add((REVIEW_IRI, PROV.wasInfluencedBy, merge))
    batch_act = {}
    for b in range(1, 9):
        act, ag = LR[f"activity/charting-batch-{b}"], LR[f"agent/charting-batch-{b}"]
        out_ent = LR[f"batch/{b}"]
        g.add((ag, RDF.type, PROV.SoftwareAgent)); g.add((ag, RDFS.label, Literal(f"Charting agent, batch {b}")))
        g.add((ag, EX.model, Literal("Claude Sonnet"))); g.add((ag, EX.batchId, Literal(b)))
        g.add((act, RDF.type, PROV.Activity)); g.add((act, PROV.wasAssociatedWith, ag))
        g.add((act, RDFS.label, Literal(f"Full-text screening, charting and appraisal, batch {b}")))
        qa = BNode(); g.add((act, PROV.qualifiedAssociation, qa)); g.add((qa, RDF.type, PROV.Association))
        g.add((qa, PROV.agent, ag)); g.add((qa, PROV.hadPlan, instr))
        g.add((act, PROV.used, corpus_ent))
        g.add((out_ent, RDF.type, PROV.Entity)); g.add((out_ent, PROV.wasGeneratedBy, act))
        g.add((out_ent, PROV.atLocation, URIRef(f"file:batches/charting_{b}_records.json")))
        g.add((merge, PROV.used, out_ent))
        batch_act[b] = act

    # ---- shared cohorts ----
    shared_of = {}
    for grp in syn["shared_cohorts"]["groups"]:
        sc = LR["sharedcohort/" + grp["cohort_id"]]
        g.add((sc, RDF.type, EX.SharedCohortDefinition)); g.add((sc, RDF.type, PROV.Entity))
        g.add((sc, RDFS.label, Literal(f"{grp['release']} N={grp['n_total']}" + (f" ({grp['n_asd']} ASD / {grp['n_td']} TD)" if grp["n_asd"] else ""))))
        g.add((sc, EX.release, Literal(grp["release"])))
        for d in DS[grp["release"]]:
            g.add((sc, PROV.wasDerivedFrom, d))
        g.add((sc, EX.nTotal, Literal(grp["n_total"])))
        if grp["n_asd"]:
            g.add((sc, EX.nASD, Literal(grp["n_asd"]))); g.add((sc, EX.nTD, Literal(grp["n_td"])))
        for p, n in grp["pipelines"].items():
            g.add((sc, EX.pipelineUsed, Literal(f"{p} ({n})")))
        g.add((sc, EX.groupingRule, Literal(syn["shared_cohorts"]["rule"])))
        g.add((sc, EX.samePipelineAcrossMembers, Literal(grp["same_pipeline"])))
        g.add((sc, PROV.wasGeneratedBy, merge))
        for m in grp["members"]:
            g.add((sc, EX.usedBy, doi_iri(m["doi"])))
            shared_of[m["source_id"]] = sc

    acc_by = {}
    for a in ev["accuracy_rows"]:
        acc_by.setdefault(a["source_id"], []).append(a)
    n_quotes = 0
    for r in recs:
        sid, e = r["source_id"], corpus[r["pmid"]]
        inc = r["screening"]["decision"] == "include"
        kg = r.get("kg_link") or {}
        pub = doi_iri(r["doi"])
        act = batch_act[r["_batch"]]
        g.add((pub, RDF.type, EX.Publication)); g.add((pub, RDF.type, PROV.Entity))
        g.add((pub, DCTERMS.title, Literal(e["title"]))); g.add((pub, DCTERMS.identifier, pub))
        if e.get("year"):
            g.add((pub, EX.year, Literal(int(e["year"]))))
        g.add((pub, EX.reviewSourceId, Literal(sid))); g.add((pub, EX.corpusId, Literal(r["pmid"])))
        g.add((pub, EX.reviewDecision, Literal("included" if inc else "excluded")))
        g.add((pub, EX.screeningReason, Literal(r["screening"]["reason"] if sid not in integ else
                                               "Abstract only — full text mismatched; " + r["screening"]["reason"].split("Abstract only —", 1)[-1].strip())))
        g.add((pub, EX.assessedOn, Literal("abstract_only" if sid in integ else r["screening"]["assessed_on"])))
        for node in sorted(gnodes.get(r["doi"].lower(), [])):
            g.add((pub, SKOS.exactMatch, URIRef(node)))
        if not kg:
            continue
        rel = kg.get("relation", "")
        status = {"uses-data": "uses-data (charted)", "describes-release": "describes-release (charted)"}.get(rel, "mentions")
        link = LR["datalink/" + sid]
        g.add((link, RDF.type, EX.DatasetPublicationLink)); g.add((link, RDF.type, PROV.Entity))
        g.add((link, EX.publication, pub)); g.add((link, EX.status, Literal(status)))
        g.add((link, EX.abideReleaseNamed, Literal(kg.get("dataset", ""))))
        for d in DS.get(kg.get("dataset", ""), []):
            g.add((link, EX.dataset, d))
        g.add((link, EX.method, Literal("full-text charting by AI agent (charting_instructions.md); quotes re-verified by phase3/s2_quotes.py")))
        g.add((link, PROV.wasGeneratedBy, act))
        # evidence quotes: evidence spans + kg_link quotes (deduplicated)
        quotes, seen = [], set()
        for s in r.get("evidence_spans", []) or []:
            quotes.append((s["text"], s.get("section", ""), s.get("claim", "")))
        for q in kg.get("evidence_quotes", []) or []:
            quotes.append((q, "", "kg_link evidence"))
        k = 0
        basis_text = e.get("abstract", "") if sid in integ else (e.get("full_text") or "")
        for text, sec, claim in quotes:
            key = norm(text)
            if not key or key in seen:
                continue
            seen.add(key); k += 1
            qn = LR[f"quote/{sid}/{k}"]
            g.add((qn, RDF.type, PROV.Entity)); g.add((qn, RDF.type, EX.EvidenceQuote))
            g.add((qn, PROV.value, Literal(text)))
            g.add((qn, PROV.wasQuotedFrom, pub))
            g.add((qn, EX.sourceQuoteVerified, Literal(True)))
            g.add((qn, EX.verifiedBy, merge))
            if claim:
                g.add((qn, EX.supportsClaim, Literal(claim)))
            loc = locate(text, basis_text)
            locator = (f"corpus {r['pmid']} " + ("abstract" if sid in integ else f"full_text sha256:{e['content_sha256']}")
                       + (f" section:{sec}" if sec else "") + (f" char:{loc}" if loc is not None else " (whitespace/ligature-normalised match)"))
            g.add((qn, EX.sourceLocator, Literal(locator)))
            g.add((qn, PROV.wasGeneratedBy, act))
            g.add((link, EX.hasEvidence, qn))
            if k == 1:
                g.add((link, EX.evidenceQuote, Literal(text)))
            n_quotes += 1
        if not inc:
            continue
        # cohort
        coh = LR["cohort/" + sid]
        n = kg.get("n_by_dx") or {}
        g.add((coh, RDF.type, EX.AnalysedCohort)); g.add((coh, RDF.type, PROV.Entity))
        g.add((coh, RDFS.label, Literal(f"{sid} analysed cohort")))
        g.add((link, EX.cohort, coh))
        for d in DS.get(kg.get("dataset", ""), []):
            g.add((coh, PROV.wasDerivedFrom, d))
        g.add((coh, EX.release, Literal(kg.get("dataset", ""))))
        for key, prop in (("ASD", EX.nASD), ("TD", EX.nTD), ("total", EX.nTotal)):
            g.add((coh, prop, Literal(n[key]) if n.get(key) is not None else Literal("not reported")))
        g.add((coh, EX.sites, Literal(str(kg.get("sites") or "not reported"))))
        g.add((coh, EX.selectionRule, Literal(kg.get("cohort_description") or "not reported")))
        g.add((coh, EX.qcRule, Literal(r["charting"]["custom_fields"].get(K2, "").split(" | quote")[0] or "not reported")))
        g.add((coh, EX.reconstructible, Literal(kg.get("reconstructible", ""))))
        g.add((coh, PROV.wasGeneratedBy, act))
        if sid in shared_of:
            g.add((coh, EX.matchesSharedCohort, shared_of[sid]))
        # methods / claim
        g.add((pub, EX.pipelineStated, Literal(kg.get("pipeline") or "not reported")))
        g.add((pub, EX.atlasStated, Literal(kg.get("atlas") or "not reported")))
        if sid in per:
            for p in per[sid]["pipeline"]:
                g.add((pub, EX.pipeline, Literal(p)))
            for a in per[sid]["atlas"]:
                g.add((pub, EX.atlas, Literal(a)))
            for s in per[sid]["site_handling"]:
                g.add((pub, EX.siteHandling, Literal(s)))
        g.add((pub, EX.claimType, Literal(kg.get("claim_type", ""))))
        g.add((pub, EX.finding, Literal(kg.get("finding", ""))))
        rob = r.get("risk_of_bias") or {}
        tool = "PROBAST" if kg.get("claim_type") in ("predictive", "both") and any(
            a["domain"] == "Analysis" for a in rob.get("assessments", [])) else "JBI analytical cross-sectional"
        g.add((pub, EX.appraisalTool, Literal(tool)))
        g.add((pub, EX.riskOfBiasOverall, Literal(rob.get("overall", ""))))
        if tool == "PROBAST":
            g.add((pub, EX.probastOverall, Literal(rob.get("overall", ""))))
            for a in rob["assessments"]:
                if a["domain"] == "Analysis":
                    g.add((pub, EX.probastAnalysis, Literal(a["judgment"])))
        for sch in ev["schemes_per_paper"].get(sid, []):
            g.add((pub, EX.evaluationScheme, Literal(sch)))
        if sid in ev["leakage_flagged"]:
            g.add((pub, EX.leakageFlag, Literal(ev["leakage_flagged"][sid])))
        for a in acc_by.get(sid, []):
            pn = LR[f"performance/{sid}/{slug(a['scheme'])}"]
            g.add((pn, RDF.type, EX.ReportedPerformance)); g.add((pn, RDF.type, PROV.Entity))
            g.add((pn, EX.evaluationScheme, Literal(a["scheme"])))
            g.add((pn, EX.accuracyPct, Literal(a["accuracy_pct"], datatype=XSD.decimal)))
            g.add((pn, EX.basis, Literal(a["basis"]))); g.add((pn, EX.chartedSnippet, Literal(a["charted_snippet"])))
            g.add((pn, PROV.wasGeneratedBy, merge)); g.add((pn, PROV.wasDerivedFrom, LR[f"batch/{r['_batch']}"]))
            g.add((pub, EX.reportsPerformance, pn))
    g.add((LR["kg"], RDF.type, PROV.Entity)); g.add((LR["kg"], PROV.wasGeneratedBy, merge))
    g.add((LR["kg"], RDFS.comment, Literal("Categorical literals (pipeline, atlas, siteHandling, evaluationScheme, leakageFlag) "
                                           "were derived by the merge agent from charted values (phase3/s4_synthesis.py); charted "
                                           "values (cohort, finding, quotes) were generated by the charting batch activity.")))
    out = ROOT / "literature_kg.ttl"
    g.serialize(out, format="turtle")
    g2 = Graph(); g2.parse(out)
    print(len(g2), "triples;", n_quotes, "evidence quotes")


if __name__ == "__main__":
    main()
