"""Step 3: assemble phase3/review_draft.json (PRISMAReviewResult) from verified records + corpus + synthesis.

Search provenance (queries, iterations, identification counts) is applied afterwards by the skill's
update_provenance.py from phase3/search_provenance_phase3.json, which is search_provenance.json plus a
search_notes line carrying the not-retrieved reasons (the flow model has no slot for them).
"""
import collections
import json
from datetime import datetime, timezone
from common import ROOT

NOW = datetime.now(timezone.utc).isoformat()
PROTOCOL = json.load(open(ROOT / "protocol.json"))
CORPUS = {e["pmid"]: e for e in json.load(open(ROOT / "corpus.json"))["items"]}
RECS = json.load(open(ROOT / "phase3" / "records_verified.json"))
SYN = json.load(open(ROOT / "results_synthesis.json"))
INTEG = json.load(open(ROOT / "phase3" / "integrity.json"))
QV = json.load(open(ROOT / "phase3" / "quote_verification.json"))
SP = json.load(open(ROOT / "search_provenance.json"))
TEMPLATE_PROTOCOL = json.load(open(ROOT / "phase3" / "template.json"))["protocol"]
SYN_MD = open(ROOT / "synthesis.md").read()
REVIEW_ID = "review_local_20261015_abide_rsfmri"
DOMAIN_KEYS = ["domain_1_participant_quality", "domain_2_data_collection_quality",
               "domain_3_feature_model_quality", "domain_4_bias_transparency"]
MISMATCH = set(INTEG["mismatched"])


def article(e, rec=None):
    a = {k: v for k, v in e.items() if not k.startswith("_")}
    for k in ("keywords", "mesh_terms"):
        v = a.get(k)
        if isinstance(v, str):
            try:
                a[k] = json.loads(v)
            except json.JSONDecodeError:
                a[k] = [v] if v else []
    a.setdefault("pmc_id", "")
    a["hop_level"], a["parent_id"] = 0, ""
    if rec is not None:
        a["inclusion_status"] = "included"
        a["risk_of_bias"] = rob(rec)
        a["critical_appraisal"] = appraisal(rec)
    return a


def rob(rec):
    r = rec["risk_of_bias"]
    out = []
    for x in r.get("assessments", []):
        j = x["judgment"]
        sup = x.get("support", "")
        if j not in ("Low", "High", "Unclear", "Some concerns"):
            sup = f"[charted judgment: {j}] " + sup
            j = "Unclear"
        out.append({"domain": x["domain"], "judgment": j, "support": sup})
    return {"assessments": out, "overall": r.get("overall") or "Unclear", "summary": r.get("summary", "")}


def appraisal(rec):
    """Normalise the batch agents' four appraisal shapes onto CriticalAppraisalRubric."""
    ca = rec["critical_appraisal"]
    by_pos = {}
    for k, v in ca.items():
        if k.startswith("domain_") and isinstance(v, dict):
            by_pos[int(k.split("_")[1])] = v
    out = {"source_id": rec["source_id"]}
    for i, key in enumerate(DOMAIN_KEYS, start=1):
        d = by_pos.get(i) or {}
        name = PROTOCOL["appraisal_domains"][i - 1]
        if "items" in d:
            items = [{"item_text": it.get("item_text") or it.get("item", ""), "rating": it.get("rating", ""),
                      "notes": it.get("notes") or it.get("support", "")} for it in d["items"]]
        elif d:
            items = [{"item_text": "Domain rating", "rating": d.get("rating", ""),
                      "notes": d.get("notes") or d.get("support", "")}]
        else:
            items = []
        out[key] = {"domain_name": name, "items": items, "overall_concern": d.get("overall_concern", "")}
    return out


def structured(ca):
    doms = []
    for key in DOMAIN_KEYS:
        d = ca[key]
        if d["overall_concern"] in ("Low", "Some", "High"):
            doms.append({"domain_name": d["domain_name"],
                         "item_ratings": [{"item_text": it["item_text"], "rating": it["rating"]} for it in d["items"]],
                         "domain_concern": d["overall_concern"]})
    return {"source_id": ca["source_id"], "domains": doms}


def charting(rec, e):
    c = dict(rec["charting"])
    meta = {"source_id": rec["source_id"], "title": e.get("title", ""), "authors": e.get("authors", ""),
            "year": e.get("year", ""), "journal_conference": e.get("journal", ""), "doi": e.get("doi", ""),
            "database_retrieved": "openalex"}
    for k, v in meta.items():
        if not c.get(k):
            c[k] = v
    return c


def screening_entry(rec, e):
    s = rec["screening"]
    reason = s["reason"]
    if rec["source_id"] in MISMATCH:
        body = reason.split("Abstract only —", 1)[-1].strip()
        reason = ("Abstract only — full text mismatched (the PDF retrieved for this DOI is an unrelated HAL preprint, "
                  "hal-01684048, on motion/form perception); decided on the corpus abstract. " + body)
        assessed = "abstract_only"
    else:
        assessed = s["assessed_on"]
    return {"pmid": rec["pmid"], "title": e.get("title", ""), "decision": s["decision"], "reason": reason,
            "stage": "full_text", "assessed_on": assessed, "full_text_source": e.get("full_text_source", "")}


def group_analysis(inc):
    per = SYN["per_paper_categories"]
    leak = SYN["evaluation"]["leakage_flagged"]
    groups = collections.defaultdict(list)
    for r in inc:
        groups[r["charting"]["study_design"]].append(r)
    entries = []
    for label, rs in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        ids = [r["pmid"] for r in rs]
        rel = collections.Counter(r["kg_link"]["dataset"] for r in rs)
        ns = sorted(r["kg_link"]["n_by_dx"]["total"] for r in rs if r["kg_link"]["n_by_dx"].get("total"))
        pip = collections.Counter(p for r in rs for p in per.get(r["source_id"], {}).get("pipeline", []))
        atl = collections.Counter(a for r in rs for a in per.get(r["source_id"], {}).get("atlas", []))
        site = collections.Counter(s for r in rs for s in per.get(r["source_id"], {}).get("site_handling", []))
        cl5 = collections.Counter(r["charting"]["custom_fields"].get(
            "CL5 Leakage control reported (feature selection/scaling/harmonisation confined to training folds)?", "").split(" ")[0].strip(" —-|")
            for r in rs)
        rq6 = collections.Counter(r["kg_link"]["reconstructible"].split(" ")[0] for r in rs)
        nl = sum(1 for r in rs if r["source_id"] in leak)
        fmt = lambda c: ", ".join(f"{k} {v}" for k, v in c.most_common())
        med = ns[len(ns) // 2] if ns else None
        answers = [
            {"question": PROTOCOL["default_group_questions"][0],
             "answer": f"Releases: {fmt(rel)}. Analysed total N median {med} (range {ns[0] if ns else '—'}–{ns[-1] if ns else '—'}; {len(rs) - len(ns)} not reported).",
             "supporting_pmids": ids[:5], "caveats": "Charted analysed N, not release size."},
            {"question": PROTOCOL["default_group_questions"][1],
             "answer": f"Pipelines: {fmt(pip) or 'n/a'}. Atlases (top 5): {', '.join(f'{k} {v}' for k, v in atl.most_common(5)) or 'n/a'}.",
             "supporting_pmids": ids[:5], "caveats": "Multi-label: a paper can use several."},
            {"question": PROTOCOL["default_group_questions"][2],
             "answer": f"Site handling: {fmt(site) or 'n/a'}. Leakage control reported (CL5): {fmt(cl5)}. Leakage-flagged (PROBAST Analysis High, specific pattern): {nl}.",
             "supporting_pmids": ids[:5], "caveats": ""},
            {"question": PROTOCOL["default_group_questions"][3],
             "answer": f"Cohort reconstructible (RQ6): {fmt(rq6)}.", "supporting_pmids": ids[:5], "caveats": ""},
        ]
        entries.append({"label": label, "n_studies": len(rs), "summary": {
            "label": label, "n_studies": len(rs),
            "aggregate_finding": f"{len(rs)} studies; releases {fmt(rel)}; median analysed N {med}.",
            "representative_pmids": ids[:5], "caveats": ""}, "answers": answers})
    return {"dimension": "study_design", "topic": PROTOCOL["title"], "n_articles_synthesized": len(inc),
            "n_groups": len(entries), "unlabeled_count": 0, "groups": entries,
            "overall_caveats": "Computed from charted values by phase3/s3_assemble.py; see results_synthesis.json."}


def main():
    inc = [r for r in RECS if r["screening"]["decision"] == "include"]
    exc = [r for r in RECS if r["screening"]["decision"] == "exclude"]
    proto = dict(TEMPLATE_PROTOCOL)
    proto.update(PROTOCOL)
    proto.update({"review_id": REVIEW_ID, "pg_dsn": "", "share_to_cache": False, "force_refresh": False,
                  "amendments": ""})
    screening_log = [screening_entry(r, CORPUS[r["pmid"]]) for r in RECS]
    ev, scr = SYN["evaluation"], SYN["screening"]
    ft_sources = collections.Counter(CORPUS[r["pmid"]]["full_text_source"] for r in RECS)
    flow = {
        "db_pubmed": 0, "db_biorxiv": 0, "db_medrxiv": 0, "db_related": 0, "db_hops": 0, "db_other_sources": {},
        "total_identified": SP["total_identified"], "duplicates_removed": SP["duplicates_removed"],
        "after_dedup": SP["total_identified"] - SP["duplicates_removed"],
        "screened_title_abstract": SP["records_screened"], "excluded_title_abstract": SP["records_excluded_title_abstract"],
        "sought_fulltext": SP["reports_sought"], "not_retrieved": SP["reports_not_retrieved"],
        "assessed_eligibility": len(RECS), "excluded_eligibility": len(exc),
        "excluded_reasons": scr["excluded_reasons"], "included_synthesis": len(inc),
        "full_text_retrieved": len(RECS), "full_text_sources": dict(ft_sources),
        "assessed_on_full_text": scr["assessed_on"].get("full_text", 0),
        "assessed_on_abstract_only": scr["assessed_on"].get("abstract_only", 0),
        "excluded_reasons_title_abstract": {"Not open access (metadata screen)": 310,
                                            "Non-primary publication type or review title (metadata screen)": 4},
        "excluded_reasons_full_text": scr["excluded_reasons"],
        "included_with_full_text": sum(1 for r in inc if r["source_id"] not in MISMATCH),
        "included_abstract_only": sum(1 for r in inc if r["source_id"] in MISMATCH),
    }
    articles = [article(CORPUS[r["pmid"]], r) for r in inc]
    spans = []
    for r in inc:
        e = CORPUS[r["pmid"]]
        for s in r.get("evidence_spans", []):
            spans.append({"text": s["text"], "paper_pmid": r["pmid"], "paper_title": e["title"],
                          "section": s.get("section", ""), "relevance_score": float(s.get("relevance_score") or 0),
                          "claim": s.get("claim", ""), "doi": e.get("doi", ""), "grounding_score": 1.0, "grounded": True})
    cas = [a["critical_appraisal"] for a in articles]
    pred_n = ev["n_predictive_or_both"]
    overall = ev["probast_overall"]
    acc = ev["accuracy_by_scheme"]
    jbi = collections.Counter(r["risk_of_bias"]["overall"] for r in inc if r["kg_link"]["claim_type"] in ("associational", "descriptor"))
    bias = (f"Predictive papers (n={pred_n}) were appraised with PROBAST domains (Participants, Predictors, Outcome, Analysis); "
            f"overall: {', '.join(f'{k} {v}' for k, v in overall.items())}. The Analysis domain drove most High ratings "
            f"({ev['probast_analysis_judgment'].get('High', 0)} High): single train/test splits without uncertainty, cross-validation "
            f"pooling sites, and in {len(ev['leakage_flagged'])} papers leakage — feature selection, harmonisation or tuning on data "
            f"outside the training folds ({', '.join(sorted(ev['leakage_flagged']))}). Group-difference papers and the data descriptor "
            f"(n={sum(jbi.values())}) were appraised with JBI analytical cross-sectional items; overall: "
            f"{', '.join(f'{k} {v}' for k, v in jbi.items())}. The commonest weaknesses were unreported motion/QC thresholds (CL2), "
            f"no site handling ({SYN['site_handling']['counts_multi_label']['none reported']} of {SYN['site_handling']['n_papers']} analysis papers), "
            f"and cohorts that cannot be rebuilt from released files (RQ6 no: {SYN['reconstructibility_RQ6']['summary']['no']}).")
    limitations = (
        "Corpus: 200 of 412 open-access primary records were sought (top by citation count, with quotas) and 99 retrieved; 101 were "
        "not retrieved (47 no OA PDF location known; 23 publisher OA URL served a bot-check page; 49 of the misses had a PMCID but PMC "
        "routes were blocked on 2026-10-15), including the ABIDE I descriptor (Di Martino 2014). Paywalled work is absent by design. "
        "Full texts were extracted with PyMuPDF; tables may be garbled. One retrieved PDF (S-040, 10.1016/j.biopsych.2017.09.029) is "
        "a different paper, so that record was assessed on its abstract. Screening, charting and appraisal were done by AI charting "
        "agents (Claude Sonnet, 8 batches), single-charted, without human double extraction; every quote was mechanically re-verified "
        f"against the full text ({QV['stats']['checked']} checked, {QV['stats']['dropped']} dropped, all empty strings), but the "
        "judgments themselves were not independently re-rated. Evaluation-scheme, headline-accuracy and site-handling categories were "
        "assigned by the merge agent from charted text, each tied to a verbatim charted snippet. Accuracies are not comparable across "
        "papers (different subsets, pipelines, models, metrics), so the scheme-wise distributions are descriptive. Shared cohorts are "
        "inferred from identical stated N and release, not from participant lists.")
    import re
    synth_body = re.sub(r"(?m)^(#{2,3}) ", lambda m: "#" * (len(m.group(1)) + 2) + " ", SYN_MD.split("\n", 2)[2])
    grade = {"Diagnostic classification of autism vs typical development from ABIDE rs-fMRI": {
        "outcome": "Diagnostic classification of autism vs typical development from ABIDE rs-fMRI",
        "domains": {
            "Risk of bias": {"rating": "Serious", "explanation": f"PROBAST overall High in {overall.get('High', 0)}/{pred_n}; {len(ev['leakage_flagged'])} leakage-flagged."},
            "Inconsistency": {"rating": "Serious", "explanation": f"Headline accuracies span {acc['pooled k-fold CV']['min']}–{acc['pooled k-fold CV']['max']}% under pooled CV alone."},
            "Indirectness": {"rating": "Serious", "explanation": f"{ev['papers_per_scheme']['pooled k-fold CV']} of {pred_n} papers mix sites across folds; only {ev['papers_per_scheme']['leave-site-out']} hold out whole sites, the setting closest to use on new scanners."},
            "Imprecision": {"rating": "Serious", "explanation": "Most papers report point estimates; few give intervals."},
            "Publication bias": {"rating": "Undetected", "explanation": "Not assessable from this corpus (open-access, citation-ranked)."},
        },
        "overall_certainty": "Very Low",
        "summary": "Very low certainty that the reported accuracies would hold on data from unseen sites."}}
    review = {
        "research_question": PROTOCOL["objective"],
        "protocol": proto,
        "search_queries": [], "search_iterations": [],
        "flow": flow,
        "included_articles": articles,
        "screening_log": screening_log,
        "evidence_spans": spans,
        "synthesis_text": synth_body,
        "bias_assessment": bias,
        "limitations": limitations,
        "grade_assessments": grade,
        "timestamp": NOW, "prisma_review": None, "cache_hit": False, "cache_similarity_score": 0.0,
        "cache_matched_criteria": {},
        "data_charting_rubrics": [charting(r, CORPUS[r["pmid"]]) for r in inc],
        "narrative_rows": [dict(r["narrative_row"], source_id=r["source_id"]) for r in inc],
        "critical_appraisals": cas,
        "grounding_validation": None,
        "structured_abstract": (
            f"Background: ABIDE I and II are the most reused open autism rs-fMRI releases. Objective: {PROTOCOL['objective'][:300]}… "
            f"Methods: OpenAlex citation searches (994 records, 268 duplicates); metadata screen; 200 open-access reports sought, 99 "
            f"retrieved and assessed on full text (1 on abstract); AI-agent charting of RQ1–RQ6 and CL1–CL8 with quotes re-verified; "
            f"PROBAST / JBI appraisal. Results: {len(inc)} included ({SYN['release'].get('ABIDE I', 0)} ABIDE I, "
            f"{SYN['release'].get('ABIDE I+II', 0)} I+II, {SYN['release'].get('ABIDE II', 0)} II); {pred_n} predictive. "
            f"{ev['papers_per_scheme']['pooled k-fold CV']} used site-pooled k-fold CV and {ev['papers_per_scheme']['leave-site-out']} leave-site-out; "
            f"median headline accuracy {acc['pooled k-fold CV']['median']}% vs {acc['leave-site-out']['median']}%. "
            f"{len(ev['leakage_flagged'])} were leakage-flagged. Cohorts were exactly reconstructible in "
            f"{SYN['reconstructibility_RQ6']['summary']['yes']} papers. Conclusion: reported ABIDE accuracies mostly come from "
            "site-mixed evaluation on cohorts that cannot be rebuilt; holding sites out and publishing participant lists are the gaps."),
        "introduction_text": (
            "ABIDE I (2014) and ABIDE II (2017) aggregate resting-state fMRI from autistic and typically developing participants across "
            "many sites, and the Preprocessed Connectomes Project released derivatives from several pipelines. This review asks how "
            "papers subset, process and evaluate these data, and whether the analysed cohort can be traced back to the release — the "
            "link a knowledge graph of dataset use needs."),
        "conclusions_text": (
            "Most ABIDE rs-fMRI papers in this corpus make predictive claims evaluated with cross-validation that mixes sites; a "
            "minority hold sites out, and those report lower accuracies. A few subsets recur (notably ABIDE I N=871 from the "
            "Preprocessed Connectomes Project), but participant lists are rarely published, so most cohorts can be rebuilt only "
            "partly. Reporting the participant list, the QC rule and a leave-site-out result would make these claims checkable."),
        "quality_checklist": {},
        "structured_appraisal_results": [structured(c) for c in cas],
        "per_group_analysis": group_analysis(inc),
        "run_configuration": {
            "started_at": NOW, "review_id": REVIEW_ID,
            "model_name": "Charting: Claude Sonnet sub-agents (8 batches). Merge/verification/synthesis: Claude Opus 5.5 (claude-opus-5-5).",
            "protocol_snapshot": PROTOCOL,
            "pipeline_kwargs": {
                "execution_path": "B — agent-authored (no OpenRouter key), serialised with the skill's exporters",
                "skill": "sensein/agent_skills skills/synthscholar v0.3.0 @ dde5425",
                "synthscholar": "sensein/synthscholar improve_verification @ da23314",
                "corpus_provenance": "open-access PDFs fetched by DOI (Unpaywall/OpenAlex), PyMuPDF text (--no-docling)",
                "full_text_integrity": {"mismatched": INTEG["mismatched"], "rule": "title prefix or >=60% title tokens in first 5k chars, or DOI in first 20k chars"},
                "quote_verification": QV["stats"],
                "not_retrieved_reasons": SP["not_retrieved_reasons"],
                "intake_provenance": "intake_provenance.ttl (slr:PreWorkflowSession + 4 slr:UserInput)",
                "phase3_scripts": "phase3/s1_integrity.py, s2_quotes.py, s4_synthesis.py, s3_assemble.py",
            },
            "env_vars_present": {"OPENROUTER_API_KEY": False},
            "cli_invocation": "python phase3/s3_assemble.py && update_provenance.py && export_review.py review.json --formats md ttl json",
            "package_version": "synthscholar 0.0.11 (da23314)"},
        "plan_iterations": [],
        "agent_invocations": [
            {"agent_name": f"charting-agent-batch-{b}", "step_name": "screening+charting+appraisal (full text)",
             "iteration_mode": "zero_shot", "model_name": "Claude Sonnet", "batch_index": b,
             "tool_call_summary": f"batches/charting_{b}_records.json ({sum(1 for r in RECS if r['_batch'] == b)} articles)",
             "output_type": "charting records", "succeeded": True}
            for b in range(1, 9)] + [
            {"agent_name": "phase3-merge-agent", "step_name": "integrity check, quote re-verification, merge, synthesis",
             "iteration_mode": "validated_against_source", "model_name": "claude-opus-5-5", "started_at": NOW,
             "tool_call_summary": f"{QV['stats']['checked']} quotes checked, {QV['stats']['dropped']} dropped",
             "output_type": "PRISMAReviewResult", "succeeded": True}],
    }
    json.dump(review, open(ROOT / "phase3" / "review_draft.json", "w"), indent=1, ensure_ascii=False)
    sp = dict(SP)
    nr = SP["not_retrieved_reasons"]
    sp["search_notes"] = (SP["search_notes"] + f" Not retrieved ({SP['reports_not_retrieved']}): "
                          f"{nr['no_open_access_pdf_location_known']} no open-access PDF location known; "
                          f"{nr['publisher_oa_url_returned_non_pdf_bot_check']} publisher OA URL returned a bot-check page instead of a PDF; "
                          f"{nr['had_pmcid_but_pmc_routes_blocked']} of the misses had a PMCID but PMC routes were blocked ({nr['pmc_routes_blocked_detail']}); "
                          f"{nr['extension_batch_not_rechecked']} extension-batch misses not re-checked. Must-include not retrieved: "
                          + "; ".join(f"{k}: {v}" for k, v in nr["must_include_not_retrieved"].items()))
    json.dump(sp, open(ROOT / "phase3" / "search_provenance_phase3.json", "w"), indent=1, ensure_ascii=False)
    print("wrote review_draft.json:", len(articles), "included,", len(screening_log), "screening,", len(spans), "spans")


if __name__ == "__main__":
    main()
