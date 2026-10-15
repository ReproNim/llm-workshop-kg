"""Build the publication layer: questions, scoped claims, cohorts and methods with verbatim evidence.

Every quote is checked as an exact substring of the whitespace-normalised source text; a quote
that fails is written as an explicit gap instead of a claim. Source texts are downloaded by
code/download.py into data/papers/ and hashed.

Usage: uv run python code/papers.py
"""

import json
import re
import unicodedata
import xml.etree.ElementTree as ET

from pypdf import PdfReader
from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace, URIRef

from common import DATA, GRAPH, sha256_file, write_json

E = Namespace("urn:repronim:abide:")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")

PAPERS = {
    "dimartino2014": {
        "title": "The autism brain imaging data exchange: towards a large-scale evaluation of the intrinsic brain architecture in autism",
        "doi": "https://doi.org/10.1038/mp.2013.78",
        "text_url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4162310/fullTextXML",
        "file": "papers/dimartino2014_PMC4162310.xml",
        "version_note": "PMC author manuscript PMC4162310",
    },
    "abraham2017": {
        "title": "Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example",
        "doi": "https://doi.org/10.1016/j.neuroimage.2016.10.045",
        "text_url": "https://arxiv.org/pdf/1611.06066v1",
        "file": "papers/abraham2017_arxiv1611.06066v1.pdf",
        "version_note": "arXiv v1 preprint (18 Nov 2016); published NeuroImage text not compared",
    },
}

RECORDS = [
    # (id, paper, kind, claim_type, locator, quote, scope)
    ("DM_Q", "dimartino2014", "ResearchQuestion", None, "Methods, Analytic Strategy",
     "To understand the relative contributions of hypo and hyperconnectivity in ASD, we carried out whole-brain iFC analyses", None),
    ("DM_C1", "dimartino2014", "Claim", "associational", "Abstract",
     "both were detected, though hypoconnectivity dominated, particularly for cortico-cortical and interhemispheric functional connectivity",
     "Group difference (ASD vs TC) in 763 males, 17 sites; covariates age, FIQ, site, mean FD; FDR q<0.05"),
    ("DM_cohort", "dimartino2014", "ReportedCohort", None, "Methods, Participants",
     "This yielded data for 763 individuals (ASD=360, TC=403) from 17 sites", None),
    ("DM_motion", "dimartino2014", "InclusionCriterion", None, "Methods, Participants",
     "less than two SD above the sample mean (0.23±0.27mm", None),
    ("DM_fiq", "dimartino2014", "InclusionCriterion", None, "Methods, Participants",
     "individuals with FIQ within two SD of the overall ABIDE sample mean (108±15)", None),
    ("DM_preproc", "dimartino2014", "Method", None, "Methods, Image Preprocessing",
     "R-fMRI scans were preprocessed with an alpha version of the Configurable Pipeline for the Analysis of Connectomes", None),
    ("DM_nuisance", "dimartino2014", "Method", None, "Methods, Image Preprocessing",
     "nuisance signal regression (including 6 motion parameters, 5 CompCorr signals", None),
    ("DM_glm", "dimartino2014", "Method", None, "Methods, Group-level Analyses",
     "(covariates: age, FIQ, site, and mean FD)", None),
    ("DM_fdr", "dimartino2014", "Method", None, "Methods, Group-level Analyses",
     "we corrected for multiple comparisons using false discovery rate (FDR; q<0.05)", None),
    ("AB_Q", "abraham2017", "ResearchQuestion", None, "Abstract",
     "we demonstrate the feasibility of inter-site classification of neuropsychiatric status", None),
    ("AB_C1", "abraham2017", "Claim", "predictive", "Abstract",
     "Good choices of methods for the various steps of the pipeline lead to 67% prediction accuracy on the full ABIDE data",
     "Out-of-sample diagnosis prediction, N=871 after visual QC, inter- and intra-site CV"),
    ("AB_C2", "abraham2017", "Claim", "predictive", "Abstract",
     "the definition of functional brain areas is of paramount importance for biomarker discovery",
     "Comparison of atlas choices within the prediction pipeline"),
    ("AB_C3", "abraham2017", "Claim", "predictive", "Abstract",
     "prediction accuracy improves as we include more subjects",
     "Learning curves over training-set size"),
    ("AB_cohort", "abraham2017", "ReportedCohort", None, "Section 2.1",
     "This yielded 871 subjects out of the initial 1112.", None),
    ("AB_qc", "abraham2017", "InclusionCriterion", None, "Section 2.1",
     "Data were selected based on the results of quality visual inspection by three human experts", None),
    ("AB_cv", "abraham2017", "Method", None, "Introduction",
     "we left out entire sites to measure performance in the presence of uncontrolled variability", None),
    ("AB_motion", "abraham2017", "Method", None, "Section 2.1",
     "Head motion was modeled using 24 regressors derived from the parameters estimated during motion realignment", None),
    ("AB_tangent", "abraham2017", "Method", None, "Section 3.3",
     "Among all matrix types, tangent embedding is the best on all ABIDE subsets.", None),
]

REPORTED_COHORTS = {
    "DM_cohort": {"reported_n": 763, "ASD": 360, "TD": 403, "sites": 17, "membership": "participant list not machine-readable in the article; Supplementary Table 1 gives per-site counts"},
    "AB_cohort": {"reported_n": 871, "sites_text": "17 different sites", "membership": "participant list not published in the article; reconstructed here from ABIDE Preprocessed rater columns"},
}


def normalise(text: str) -> str:
    """Apply NFKC (expands ligatures), join hyphenated line breaks and collapse whitespace."""
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"-\n(?=[a-z])", "", text)
    return re.sub(r"\s+", " ", text)


def source_text(key: str) -> str:
    """Whitespace-normalised full text of one paper."""
    path = DATA / PAPERS[key]["file"]
    if path.suffix == ".xml":
        root = ET.parse(path).getroot()
        parts = ["".join(root.find(".//abstract").itertext()), "".join(root.find(".//body").itertext())]
        return normalise(" ".join(parts))
    return normalise("\n".join(p.extract_text() for p in PdfReader(path).pages))


def main() -> None:
    """Verify quotes and write graph/papers.ttl plus results/paper_extraction.json."""
    g = Graph()
    for k, v in (("ex", E), ("prov", PROV), ("dct", DCT)):
        g.bind(k, v)
    texts = {k: source_text(k) for k in PAPERS}
    for key, meta in PAPERS.items():
        p = E[f"paper/{key}"]
        g.add((p, RDF.type, E.Publication))
        g.add((p, RDF.type, PROV.Entity))
        g.add((p, RDFS.label, Literal(meta["title"])))
        g.add((p, DCT.identifier, URIRef(meta["doi"])))
        g.add((p, PROV.atLocation, URIRef(meta["text_url"])))
        g.add((p, E.textSha256, Literal(sha256_file(DATA / meta["file"]))))
        g.add((p, E.versionNote, Literal(meta["version_note"])))
    report = []
    for rid, key, kind, ctype, loc, quote, scope in RECORDS:
        found = quote in texts[key]
        node = E[f"paper/{key}/{rid}"]
        ev = E[f"paper/{key}/{rid}/evidence"]
        g.add((node, RDF.type, E[kind] if found else E.Gap))
        g.add((node, RDFS.label, Literal(rid)))
        g.add((node, E.statedIn, E[f"paper/{key}"]))
        g.add((node, E.hasEvidence, ev))
        g.add((ev, RDF.type, E.EvidenceSpan))
        g.add((ev, PROV.wasQuotedFrom, E[f"paper/{key}"]))
        g.add((ev, E.quote, Literal(quote)))
        g.add((ev, E.locator, Literal(loc)))
        g.add((ev, E.verbatimMatch, Literal(found)))
        if found:
            g.add((ev, E.charOffset, Literal(texts[key].index(quote), datatype=XSD.integer)))
        if ctype:
            g.add((node, E.claimType, Literal(ctype)))
            g.add((node, E.scope, Literal(scope)))
            g.add((node, E.addresses, E[f"paper/{key}/{rid.split('_')[0]}_Q"]))
            g.add((node, E.evidenceStatus, Literal("paper-reported; not replicated here")))
        if rid in REPORTED_COHORTS:
            for k2, v2 in REPORTED_COHORTS[rid].items():
                g.add((node, E[k2], Literal(v2)))
        if kind in ("Method", "InclusionCriterion", "ReportedCohort"):
            claims = [r[0] for r in RECORDS if r[1] == key and r[2] == "Claim"]
            for c in claims:
                g.add((E[f"paper/{key}/{c}"], E.dependsOn, node))
        report.append({"id": rid, "paper": key, "kind": kind, "claim_type": ctype, "locator": loc, "quote": quote, "verbatim_match": found})
    g.add((E["paper/abraham2017/AB_cohort"], E.reconstructedAs, E["cohort/abraham2017_reconstructed"]))
    g.serialize(GRAPH / "papers.ttl", format="turtle")
    write_json("paper_extraction.json", {"records": report, "n_verbatim": sum(r["verbatim_match"] for r in report), "n": len(report),
                                         "sources": {k: {**v, "sha256": sha256_file(DATA / v["file"])} for k, v in PAPERS.items()}})
    print(json.dumps([(r["id"], r["verbatim_match"]) for r in report]))


if __name__ == "__main__":
    main()
