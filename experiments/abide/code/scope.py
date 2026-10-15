"""Knowledge scope (ReproPond / consortium federation / ReproLake), egress profiles and transitions.

Scope values: pond (with level analyst | lab | site), consortium-federation, lake.
Sensitivity profile per record family: consentScope (broad-sharing | study-only | named-uses), DUO codes
when known, containsDirectIdentifiers, containsQuasiIdentifiers (+ minimum cell size met), defaced,
restrictedByAgreement, accessLevel; egressPermitted derived with its reason.
Transitions as PROV activities:
  ex:PromotionCandidate (pond -> lake/consortium) with six gate assessments, each pass | fail | unknown
  ex:Adoption (lake -> pond) with pinned version, local parameters, local re-validation
  ex:Revision / deprecation flags linked to activity snapshots or contradicting assessments
Also computes the motion-rule generality evidence (site-wise exclusion sweep) in results/fd_sweep.json.

Usage: uv run python code/scope.py
"""

import json

import numpy as np
from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace, URIRef

from common import MOTION_RULES, RESULTS, GRAPH, base_table, write_json

E = Namespace("urn:repronim:abide:")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
OBO = Namespace("http://purl.obolibrary.org/obo/")
GATES = ["generality", "review", "consent_and_deidentification", "licence", "persistent_identifier_and_version", "provenance_retained"]
ABIDE_STATEMENT = ("In accordance with HIPAA guidelines and 1000 Functional Connectomes Project / INDI protocols, all datasets have been anonymized, "
                   "with no protected health information included.")
ABIDE_PAGE = "https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html"
BRKG_NOTE = ("BR-KG (Brain Researcher knowledge graph) queried by a parallel session on 2026-10-15: one aggregate ABIDE node "
             "(2,226 subjects, ABIDE I+II); neither DOI 10.1038/mp.2013.78 nor 10.1016/j.neuroimage.2016.10.045 present. Relayed, not re-run here.")


def fd_sweep() -> dict:
    """Site-wise exclusion fraction at several mean-FD thresholds, on the rater-QC + full-coverage base."""
    d = base_table()
    base = d[d.rater_qc_pass & d.full_roi_coverage]
    out = {"base_n": len(base), "thresholds_mm": [0.1, 0.15, 0.2, 0.25, 0.3], "by_threshold": {}}
    for t in out["thresholds_mm"]:
        frac = base.groupby("SITE_ID").func_mean_fd.apply(lambda x: float((x >= t).mean()))
        out["by_threshold"][str(t)] = {
            "overall_excluded_fraction": float((base.func_mean_fd >= t).mean()),
            "site_min": float(frac.min()), "site_max": float(frac.max()), "site_median": float(frac.median()),
            "site_max_name": frac.idxmax(), "n_sites_over_50pct_excluded": int((frac > 0.5).sum()), "n_sites": int(frac.size),
            "dx_excluded_fraction": base.assign(x=base.func_mean_fd >= t).groupby("dx").x.mean().round(4).to_dict(),
        }
    return out


class S:
    """Graph helper."""

    def __init__(self) -> None:
        """New graph with prefixes."""
        self.g = Graph()
        for k, v in (("ex", E), ("prov", PROV), ("dct", DCT), ("obo", OBO)):
            self.g.bind(k, v)

    def add(self, s, p, o) -> None:
        """Add a triple with literal conversion."""
        if not isinstance(o, (URIRef, Literal)):
            o = Literal(o, datatype=XSD.boolean) if isinstance(o, bool) else Literal(o)
        self.g.add((s, p, o))

    def scope(self, item, scope: str, level: str | None = None, access: str = "public") -> None:
        """Attach a knowledge scope."""
        self.add(item, E.knowledgeScope, E[f"scope/{scope}"])
        if level:
            self.add(item, E.pondLevel, level)
        self.add(item, E.accessLevel, access)

    def profile(self, key: str, **kw) -> URIRef:
        """A sensitivity profile with a derived egress decision."""
        p = E[f"sensitivity/{key}"]
        self.add(p, RDF.type, E.SensitivityProfile)
        for k, v in kw.items():
            if v is None:
                continue
            if k == "duo":
                for code in v:
                    self.add(p, E.duoCode, OBO[code])
            elif k == "source":
                self.add(p, DCT.source, URIRef(v))
            else:
                self.add(p, E[k], v)
        reasons = []
        if kw.get("consentScope") != "broad-sharing":
            reasons.append(f"consent scope is {kw.get('consentScope')}, not broad-sharing")
        if kw.get("containsDirectIdentifiers"):
            reasons.append("contains direct identifiers")
        if kw.get("defaced") is False:
            reasons.append("structural images not defaced")
        if kw.get("restrictedByAgreement"):
            reasons.append("restricted by agreement")
        if kw.get("containsQuasiIdentifiers") and not kw.get("minCellSizeMet") and not kw.get("alreadyPublicRelease"):
            reasons.append("quasi-identifiers without aggregation to minimum cell size")
        unknown = [k for k in ("consentScope", "containsDirectIdentifiers") if kw.get(k) is None]
        status = "unknown" if unknown else ("permitted" if not reasons else "not permitted")
        self.add(p, E.egressPermitted, status)
        self.add(p, E.egressReason, "; ".join(reasons) if reasons else ("no blocking attribute" if status == "permitted" else f"unknown: {', '.join(unknown)}"))
        return p

    def promotion(self, key: str, item, target: str, registry: str, gates: dict, status: str = "candidate", note: str = "") -> URIRef:
        """A promotion candidate activity with one assessment per gate."""
        a = E[f"promotion/{key}"]
        self.add(a, RDF.type, E.PromotionCandidate)
        self.add(a, RDF.type, PROV.Activity)
        self.add(a, PROV.used, item)
        self.add(a, E.targetScope, E[f"scope/{target}"])
        self.add(a, E.targetRegistry, registry)
        self.add(a, E.promotionStatus, status)
        if note:
            self.add(a, RDFS.comment, note)
        for gname in GATES:
            st, ev = gates.get(gname, ("unknown", "not assessed"))
            gnode = E[f"promotion/{key}/gate/{gname}"]
            self.add(gnode, RDF.type, E.GateAssessment)
            self.add(gnode, RDF.type, PROV.Entity)
            self.add(gnode, E.gateType, gname)
            self.add(gnode, E.status, st)
            self.add(gnode, E.evidence, ev)
            self.add(gnode, PROV.wasGeneratedBy, a)
            self.add(a, E.gate, gnode)
        return a

    def adoption(self, key: str, global_item, version: str, local_params: str, revalidation: str, deviation: str = "") -> None:
        """A global -> local adoption activity."""
        a = E[f"adoption/{key}"]
        self.add(a, RDF.type, E.Adoption)
        self.add(a, RDF.type, PROV.Activity)
        self.add(a, PROV.used, global_item)
        self.add(a, E.pinnedVersion, version)
        self.add(a, E.localParameters, local_params)
        self.add(a, E.localRevalidation, revalidation)
        if deviation:
            self.add(a, E.localDeviation, deviation)


def main() -> None:
    """Write graph/scope.ttl and results/scope.json."""
    sweep = fd_sweep()
    write_json("fd_sweep.json", sweep)
    linkml = json.loads((RESULTS / "linkml_validation.json").read_text())
    simple2 = json.loads((RESULTS / "simple2.json").read_text())
    cohorts = json.loads((RESULTS / "cohorts.json").read_text())
    s = S()
    for sc, label in (("pond", "ReproPond: local FAIR metadata store (lab, site or analyst level)"), ("consortium-federation", "Federated ponds queried together (e.g. via Neurobagel)"),
                      ("lake", "ReproLake: semantically aligned store of public datasets")):
        s.add(E[f"scope/{sc}"], RDF.type, E.KnowledgeScope)
        s.add(E[f"scope/{sc}"], RDFS.label, label)
    s.add(E["scope/lake"], RDFS.seeAlso, URIRef("https://www.repronim.org/resources/tools/reprolake/"))
    s.add(E["scope/pond"], RDFS.seeAlso, URIRef("https://repronim.org/resources/tutorials/pond-lake/"))

    public = s.profile("abide_public_release", consentScope="broad-sharing", containsDirectIdentifiers=False, containsQuasiIdentifiers=True,
                       alreadyPublicRelease=True, defaced="unknown (not stated on the ABIDE page; image content not in this graph)",
                       restrictedByAgreement=False, licence="CC BY-NC-SA (ABIDE I page)", statement=ABIDE_STATEMENT, source=ABIDE_PAGE)
    pond_only = s.profile("analyst_pond_records", consentScope="broad-sharing", containsDirectIdentifiers=False, containsQuasiIdentifiers=False,
                          restrictedByAgreement=False, note="derived from public data; kept in the pond because unreviewed, not because sensitive")
    study_only = s.profile("illustrative_study_only", consentScope="study-only", containsDirectIdentifiers=False, containsQuasiIdentifiers=True,
                           restrictedByAgreement=True, illustrative=True, note="ILLUSTRATIVE flag only, used for the SHACL egress mutation test; no real record has this profile")

    # Participant-level records: public de-identified release; our copies stay in the pond, the lake holds the release.
    s.add(E.participantRecords, RDF.type, E.RecordFamily)
    s.add(E.participantRecords, RDFS.label, "ABIDE participant-level phenotype records, scan pointers, time series and IDPs (1,112 participants)")
    s.scope(E.participantRecords, "pond", "lab")
    s.add(E.participantRecords, E.hasSensitivityProfile, public)
    s.add(E.participantRecords, E.lakeCopy, URIRef("http://preprocessed-connectomes-project.org/abide/"))
    s.add(E.participantRecords, E.promotionPolicy, "never-promote: the lake already holds the authoritative public release; link to it instead of copying")
    s.add(E.participantRecords, E.memberPattern, "urn:repronim:abide:record/*, participant/*, timeseries/*, connectivity/*, idp/*")

    # Cohorts and rules (analyst/lab pond).
    for c in ("A_v1", "A_v2", "B_v1", "B_v2"):
        s.scope(E[f"cohort/{c}"], "pond", "analyst")
        s.add(E[f"cohort/{c}"], E.hasSensitivityProfile, pond_only)
    s.scope(E["cohort/abraham2017_reconstructed"], "pond", "lab")
    for r in ("motion_v1", "motion_v2", "rater_qc", "coverage", "fiq_range", "site_min"):
        s.scope(E[f"rule/{r}"], "pond", "lab")
    for k in ("claim/A_v1", "claim/B_v1", "claim/A_v2", "claim/B_v2", "review/A_reviews_B_v1", "review/B_reviews_A_v1"):
        s.scope(E[k], "pond", "analyst")
        s.add(E[k], E.hasSensitivityProfile, pond_only)
    for k in ("paper/dimartino2014/DM_C1", "paper/abraham2017/AB_C1", "paper/abraham2017/AB_C2", "paper/abraham2017/AB_C3"):
        s.scope(E[k], "lake")

    # (a) paper claims and cohort definition -> literature knowledge graph
    for key, item in (("DM_C1", "paper/dimartino2014/DM_C1"), ("AB_C1", "paper/abraham2017/AB_C1"), ("AB_C2", "paper/abraham2017/AB_C2")):
        s.promotion(f"claim_{key}", E[item], "lake", "literature KG (e.g. BR-KG, AbstractAtlas)", {
            "generality": ("pass", "published, peer-reviewed claim with stated cohort scope"),
            "review": ("pass", "journal peer review; extraction checked verbatim against source text (paper_extraction.json)"),
            "consent_and_deidentification": ("pass", "claim-level statement; no participant data"),
            "licence": ("unknown", "article licence not recorded; quote length kept short"),
            "persistent_identifier_and_version": ("pass", "DOI recorded; Abraham quotes from arXiv v1, journal text not compared" if key.startswith("AB") else "DOI recorded; Europe PMC PMC4162310"),
            "provenance_retained": ("pass", "quote, locator, character offset and source hash recorded"),
        }, note=BRKG_NOTE)
    s.promotion("cohort_abraham_reconstruction", E["cohort/abraham2017_reconstructed"], "lake", "literature KG / ABIDE dataset record", {
        "generality": ("fail", f"rater-QC rule reconstructs {cohorts['abraham2017_reconstructed']['n']} participants vs 871 reported; membership unverified"),
        "review": ("unknown", "no external review"),
        "consent_and_deidentification": ("pass", "cohort definition and pseudonymous FILE_IDs from a public de-identified release"),
        "licence": ("pass", "ABIDE CC BY-NC-SA; definition is our text"),
        "persistent_identifier_and_version": ("fail", "no persistent identifier minted for the cohort definition"),
        "provenance_retained": ("pass", "rule text and membership in graph"),
    }, status="blocked", note=BRKG_NOTE)

    # (b) analyst A's motion rule, with the site-wise sweep as generality evidence
    t = sweep["by_threshold"]
    s.promotion("motion_rule_v2", E["rule/motion_v2"], "consortium-federation", "consortium QC guideline", {
        "generality": ("fail", f"FD<0.15 excludes {t['0.15']['site_min']:.0%}-{t['0.15']['site_max']:.0%} per site (max {t['0.15']['site_max_name']}); "
                               f"{t['0.15']['n_sites_over_50pct_excluded']} of {t['0.15']['n_sites']} sites lose over half; excludes {t['0.15']['dx_excluded_fraction']['ASD']:.1%} of ASD vs "
                               f"{t['0.15']['dx_excluded_fraction']['TD']:.1%} of TD, so the rule is site- and diagnosis-dependent (fd_sweep.json)"),
        "review": ("pass", "reviewed through revision_impact.json: 0 of 9 result families changed materially"),
        "consent_and_deidentification": ("pass", "a rule, no participant data"),
        "licence": ("unknown", "no licence chosen for local rules"),
        "persistent_identifier_and_version": ("fail", "versioned in this graph only (motion_v1 -> motion_v2)"),
        "provenance_retained": ("pass", "revision activity attributed to Analyst A"),
    })

    # (c) local variable mappings -> nidm-terms
    s.promotion("variable_cc200_mean_fisher_z", E["variable/cc200_mean_fisher_z"], "lake", "NIDM-Terms / InterLex", {
        "generality": ("unknown", "used in one dataset"),
        "review": ("unknown", "no term review"),
        "consent_and_deidentification": ("pass", "term definition only"),
        "licence": ("unknown", ""),
        "persistent_identifier_and_version": ("fail", "local urn only; no InterLex/NIDM-Terms identifier; no isAbout concept found"),
        "provenance_retained": ("pass", "DataElement records derivation and attributed software"),
    })
    s.promotion("variable_qc_raters", E["variable/qc_func_rater_2"], "lake", "NIDM-Terms / InterLex", {
        "generality": ("pass", "same three-rater QC columns released for all 1,112 ABIDE participants"),
        "review": ("unknown", ""),
        "consent_and_deidentification": ("pass", "term definition only"),
        "licence": ("unknown", ""),
        "persistent_identifier_and_version": ("fail", "not in ReproNim's ABIDE term map (abide_phenotypic_v1_0b_vars_to_terms_v5.json); no isAbout"),
        "provenance_retained": ("pass", "DataElement derived from the phenotype CSV with source row"),
    })

    # (d) adoptions with pinned versions and local re-validation
    s.adoption("nidm_linkml_schema", E["resource/pynidm"], f"PyNIDM v4.5.5 ({linkml['pynidm_commit']}), schema 0.1.0",
               "open and closed SHACL generated with linkml gen-shacl 1.12.1",
               f"core graph: {linkml['targets']['abide_core']['open']['n_results']} open-shape results; PyNIDM's own csv2nidm output: "
               f"{linkml['targets']['pynidm_csv2nidm_phenotype']['open']['n_results']}; simple2 Caltech: {linkml['targets']['repronim_simple2_Caltech']['open']['n_results']}",
               deviation=f"{linkml['extension']['n_classes']} classes and {linkml['extension']['n_properties']} properties declared in graph/abide_extension.ttl")
    s.adoption("simple2_nidm", E["resource/simple2_nidm_examples"], f"commit {simple2['simple2_commit']}", "loaded unmodified as 27 named graphs",
               f"identity join {simple2['identity_join']['matched']}/{simple2['identity_join']['phenotype_rows']} with 0 field conflicts; shipped query output reproduced "
               f"{simple2['verbatim_query']['keys_with_equal_values_rtol_1e-6']}/{simple2['verbatim_query']['participant_label_keys_in_both']}")
    s.add(E["resource/mni152_fsl"], RDF.type, E.Template)
    s.add(E["resource/mni152_fsl"], RDFS.label, "MNI152_T1 2 mm template as shipped with FSL 5.0")
    s.scope(E["resource/mni152_fsl"], "lake")
    s.adoption("mni152_fsl_template", E["resource/mni152_fsl"], "FSL 5.0 MNI152_T1_2mm (C-PAC pipeline_config.yml)",
               "anatomical registration at 2 mm, functional at 3 mm, ANTs", "not re-validated here: preprocessing taken as released",
               deviation="not MNI152NLin2009cAsym (the fMRIPrep default used in the CNP example)")

    # Revision / deprecation driven by evidence
    rv = E["revision/ants_cde_relabel"]
    s.add(rv, RDF.type, E.Revision)
    s.add(rv, RDF.type, PROV.Activity)
    s.add(rv, PROV.used, E["resource/ants_seg_to_nidm"])
    s.add(rv, RDFS.comment, f"ANTs CDE labels changed ({', '.join(simple2['verbatim_query']['labels_only_in_shipped_output'])} -> "
                            f"{', '.join(simple2['verbatim_query']['labels_only_in_our_run'])}); the shipped simple2_query_output.csv is a stale local copy")
    s.add(rv, E.flags, URIRef(f"https://github.com/ReproNim/simple2_NIDM_examples/blob/{simple2['simple2_commit']}/queries/simple2_query_output.csv"))
    dep = E["revision/bids_ld_dormant"]
    s.add(dep, RDF.type, E.DeprecationFlag)
    s.add(dep, RDF.type, PROV.Activity)
    s.add(dep, PROV.used, E["resource/bids-ld"])
    s.add(dep, RDFS.comment, "latest activity snapshot: no pushes since 2019; do not adopt without checking for a successor")

    # Skills: ReproNim/skills is empty -> promotion target for lab procedures
    s.add(E["skill/abide_graph_build"], RDF.type, E.Procedure)
    s.add(E["skill/abide_graph_build"], RDFS.label, "This experiment's rebuild.sh as a reusable procedure")
    s.scope(E["skill/abide_graph_build"], "pond", "lab")
    s.promotion("skill_graph_build", E["skill/abide_graph_build"], "lake", "ReproNim/skills (0 skills at pinned commit)", {
        "generality": ("fail", "tested on ABIDE only"),
        "review": ("unknown", ""),
        "consent_and_deidentification": ("pass", "procedure only"),
        "licence": ("unknown", ""),
        "persistent_identifier_and_version": ("fail", "not yet in a versioned repository"),
        "provenance_retained": ("pass", "rebuild.sh + uv.lock + hashes"),
    })

    # Illustrative record for the egress mutation test (kept out of all counts)
    ill = E["illustrative/study_only_record"]
    s.add(ill, RDF.type, E.IllustrativeRecord)
    s.add(ill, RDFS.label, "ILLUSTRATIVE study-only record (not real data)")
    s.add(ill, E.hasSensitivityProfile, study_only)
    s.scope(ill, "pond", "site", access="restricted")

    for r in Graph().parse(GRAPH / "resources.ttl").subjects(RDF.type, E.Resource):
        s.scope(r, "lake")
    s.g.serialize(GRAPH / "scope.ttl", format="turtle")
    g = s.g
    by_scope = {}
    for item, sc in g.subject_objects(E.knowledgeScope):
        key = str(sc).rsplit("/", 1)[-1] + (f":{g.value(item, E.pondLevel)}" if g.value(item, E.pondLevel) else "")
        by_scope[key] = by_scope.get(key, 0) + 1
    cands = []
    for a in g.subjects(RDF.type, E.PromotionCandidate):
        gates = {str(g.value(x, E.gateType)): str(g.value(x, E.status)) for x in g.objects(a, E.gate)}
        cands.append({"candidate": str(a).rsplit("/", 1)[-1], "item": str(g.value(a, PROV.used)).replace("urn:repronim:abide:", "ex:"),
                      "target": str(g.value(a, E.targetRegistry)), "status": str(g.value(a, E.promotionStatus)), "gates": gates,
                      "unmet": [k for k, v in gates.items() if v != "pass"]})
    write_json("scope.json", {"by_scope": by_scope, "promotion_candidates": sorted(cands, key=lambda x: x["candidate"]),
                              "n_adoptions": len(set(g.subjects(RDF.type, E.Adoption))), "n_revisions": len(set(g.subjects(RDF.type, E.Revision))) + len(set(g.subjects(RDF.type, E.DeprecationFlag))),
                              "fd_sweep_0.15": t["0.15"], "triples": len(g)})
    print(json.dumps(by_scope), len(cands), "candidates")


if __name__ == "__main__":
    main()
