"""Collect the OpenAlex search for the ABIDE review and record PRISMA identification counts."""
import json, sys, time, datetime, urllib.parse, urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "search"
MAILTO = "satra@mit.edu"
SEEDS = {"ABIDE I": "W2167868121", "ABIDE II": "W2590651237",
         "Abraham 2017 (graph seed)": "W2522924024"}
EXTRA_DOIS = ["10.1038/mp.2013.78", "10.1038/sdata.2017.10"]
SELECT = ("id,doi,title,display_name,publication_year,publication_date,type,cited_by_count,"
          "open_access,best_oa_location,primary_location,authorships,abstract_inverted_index,ids")


def get(url):
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(url)


def run(filter_str):
    base = "https://api.openalex.org/works"
    page, rows, count = 1, [], None
    while True:
        q = {"filter": filter_str, "per-page": "200", "page": str(page), "select": SELECT, "mailto": MAILTO}
        d = get(base + "?" + urllib.parse.urlencode(q))
        count = d["meta"]["count"]
        rows += d["results"]
        if not d["results"] or len(rows) >= count:
            break
        page += 1
    return count, rows


def main():
    OUT.mkdir(exist_ok=True)
    date = datetime.date.today().isoformat()
    searches, records = [], {}
    for release, wid in SEEDS.items():
        for label, extra in (("all", ""),):
            f = f"cites:{wid},title_and_abstract.search:ABIDE{extra}"
            n, rows = run(f)
            searches.append({"release_seed": release, "seed_work": wid, "subset": label,
                             "query": f"https://api.openalex.org/works?filter={f}",
                             "date_searched": date, "records_identified": n, "records_downloaded": len(rows)})
            if label == "all":
                for r in rows:
                    rec = records.setdefault(r["id"], r)
                    rec.setdefault("_seed_releases", set()).add(release)
    for doi in EXTRA_DOIS:
        r = get(f"https://api.openalex.org/works/https://doi.org/{doi}?" + urllib.parse.urlencode({"select": SELECT, "mailto": MAILTO}))
        rec = records.setdefault(r["id"], r)
        rec.setdefault("_seed_releases", set()).add("release descriptor (other source)")
    for r in records.values():
        r["_seed_releases"] = sorted(r["_seed_releases"])
    total = sum(s["records_identified"] for s in searches if s["subset"] == "all")
    dedup = len(records)
    oa = [r for r in records.values() if (r.get("open_access") or {}).get("is_oa")]
    summary = {"date_searched": date, "searches": searches, "total_identified": total,
               "other_sources": EXTRA_DOIS,
               "after_dedup": dedup, "duplicates_removed": total - dedup, "open_access": len(oa)}
    json.dump(sorted(records.values(), key=lambda r: -r["cited_by_count"]),
              open(OUT / "openalex_records.json", "w"))
    json.dump(summary, open(OUT / "search_summary.json", "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    sys.exit(main())
