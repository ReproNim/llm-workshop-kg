"""Write search_provenance.json (PRISMA identification and retrieval counts) from the recorded search artifacts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def not_retrieved_reasons(asm):
    fb = json.load(open(ROOT / "search" / "fetch_fallback_log.json"))
    pmc = json.load(open(ROOT / "search" / "missing_pmcids.json"))
    fb_miss = [x for x in fb if x["status"] == "MISS"]
    return {
        "sought": asm["candidates"],
        "retrieved": asm["retrieved_ranked"],
        "first_pass_misses_rechecked": len(fb),
        "recovered_by_second_pass": len(fb) - len(fb_miss),
        "no_open_access_pdf_location_known": sum(1 for x in fb_miss if not x.get("tried")),
        "publisher_oa_url_returned_non_pdf_bot_check": sum(1 for x in fb_miss if x.get("tried")),
        "had_pmcid_but_pmc_routes_blocked": len(pmc),
        "pmc_routes_blocked_detail": "Europe PMC ?pdf=render returned HTTP 403 (bot check); Europe PMC fullTextXML returned 500; NCBI PMC OA service returned 404 (2026-10-15)",
        "extension_batch_not_rechecked": asm["candidates"] - 160,
        "must_include_not_retrieved": {"10.1038/mp.2013.78": "Di Martino 2014 (ABIDE I descriptor): OA locations are a repository landing page (pure.knaw.nl) whose file link returned an HTML bot-check page, and PMC4162310 (PMC routes blocked); no PDF obtained"},
    }


def main():
    s = json.load(open(ROOT / "search" / "search_summary.json"))
    pre = json.load(open(ROOT / "search" / "prescreen_flow.json"))
    asm = json.load(open(ROOT / "search" / "assembly_stats.json"))
    excluded_ta = sum(pre["excluded_metadata"].values())
    prov = {
        "searches": [{
            "database": "OpenAlex",
            "query": x["query"],
            "date_searched": x["date_searched"],
            "records_identified": x["records_identified"],
            "filters": "title_and_abstract.search:ABIDE; citing the named descriptor/seed work",
            "notes": f"seed {x['release_seed']} ({x['seed_work']})",
        } for x in s["searches"]] + [{
            "database": "Other sources",
            "query": "release descriptors added by DOI: " + ", ".join(s["other_sources"]),
            "date_searched": s["date_searched"], "records_identified": len(s["other_sources"]),
            "filters": "", "notes": "Di Martino 2014 (ABIDE I) and Di Martino 2017 (ABIDE II) data descriptors"}],
        "duplicates_removed": s["total_identified"] + len(s["other_sources"]) - s["after_dedup"],
        "total_identified": s["total_identified"] + len(s["other_sources"]),
        "records_screened": s["after_dedup"],
        "records_excluded_title_abstract": excluded_ta,
        "reports_sought": asm["candidates"],
        "reports_not_retrieved": asm["candidates"] - asm["retrieved_ranked"],
        "date_range_start": "2012-01-01",
        "date_range_end": "2026-10-15",
        "grey_literature": "none",
        "not_retrieved_reasons": not_retrieved_reasons(asm),
        "search_notes": (
            "Metadata screen (not a title/abstract reading): records excluded = not open access "
            f"({pre['excluded_metadata'].get('not open access', 0)}) plus non-primary publication types / "
            "review titles. Of the remaining open-access primary records, the top "
            f"{asm['candidates']} by citation count (with quotas, search/selection_rule.md) were sought in full text; "
            f"{asm['retrieved_ranked']} retrieved; {asm['corpus']} form the corpus assessed for eligibility. "
            "Open-access primary records not in the top-ranked set were not sought (corpus-size decision by the review owner)."),
    }
    json.dump(prov, open(ROOT / "search_provenance.json", "w"), indent=2)
    print(json.dumps({k: v for k, v in prov.items() if k != "searches"}, indent=2))


if __name__ == "__main__":
    main()
