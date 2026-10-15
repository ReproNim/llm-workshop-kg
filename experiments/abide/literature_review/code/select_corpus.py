"""Pre-screen OpenAlex records on metadata and rank open-access candidates for the ABIDE review corpus."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MUST = {"10.1038/mp.2013.78", "10.1038/sdata.2017.10", "10.1016/j.neuroimage.2016.10.045"}
EXCLUDED_TYPES = {"review", "editorial", "erratum", "paratext", "letter", "dissertation", "book", "retraction", "other"}
REVIEW_TITLE = re.compile(r"\b(systematic review|meta-analys|a review|review of|survey|overview)\b", re.I)
PRED = re.compile(r"classif|predict|machine learning|deep learning|neural network|support vector|\bsvm\b|accuracy|\bauc\b|graph convolution|transformer", re.I)
ASSOC = re.compile(r"(hypo|hyper|under|over)[- ]?connectiv|altered|atypical|reduced|increased|decreased|differ(ence|ed)|group difference|aberrant|disrupted", re.I)
QUOTA = {"abide2": 25, "pred": 40, "assoc": 30}
TARGET = 100
CANDIDATES = 200


def abstract(r):
    inv = r.get("abstract_inverted_index") or {}
    pos = {i: w for w, idx in inv.items() for i in idx}
    return " ".join(pos[i] for i in sorted(pos))


def doi(r):
    return (r.get("doi") or "").replace("https://doi.org/", "").lower()


def main():
    recs = json.load(open(ROOT / "search" / "openalex_records.json"))
    flow = {"after_dedup": len(recs)}
    rows, excl = [], {}
    for r in recs:
        d = doi(r)
        a = abstract(r)
        t = r.get("display_name") or r.get("title") or ""
        reason = None
        if not (r.get("open_access") or {}).get("is_oa"):
            reason = "not open access"
        elif r.get("type") in EXCLUDED_TYPES:
            reason = f"publication type: {r.get('type')}"
        elif REVIEW_TITLE.search(t) and d not in MUST:
            reason = "review/survey (title)"
        elif not d:
            reason = "no DOI"
        if reason and d not in MUST:
            excl[reason] = excl.get(reason, 0) + 1
            continue
        text = f"{t} {a}"
        rows.append({
            "openalex_id": r["id"], "doi": d, "title": t, "year": r.get("publication_year"),
            "cited_by_count": r.get("cited_by_count", 0), "type": r.get("type"),
            "seeds": r.get("_seed_releases", []),
            "abide2_seeded": "ABIDE II" in r.get("_seed_releases", []) or bool(re.search(r"ABIDE[- ]?II\b|ABIDE[- ]?2\b", text)),
            "heuristic_predictive": bool(PRED.search(text)),
            "heuristic_associational": bool(ASSOC.search(text)) and not PRED.search(text),
            "must_include": d in MUST,
            "oa_url": (r.get("open_access") or {}).get("oa_url"),
            "journal": ((r.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
            "authors": "; ".join(a_["author"]["display_name"] for a_ in r.get("authorships", [])),
            "abstract": a,
        })
    flow["excluded_metadata"] = excl
    flow["eligible_oa_primary"] = len(rows)
    rows.sort(key=lambda x: -x["cited_by_count"])
    chosen, seen = [], set()

    def take(pred, n):
        for x in rows:
            if len([c for c in chosen if pred(c)]) >= n:
                return
            if x["doi"] not in seen and pred(x):
                chosen.append(x); seen.add(x["doi"])

    take(lambda x: x["must_include"], 99)
    take(lambda x: x["abide2_seeded"], QUOTA["abide2"])
    take(lambda x: x["heuristic_predictive"], QUOTA["pred"])
    take(lambda x: x["heuristic_associational"], QUOTA["assoc"])
    for x in rows:
        if len(chosen) >= CANDIDATES:
            break
        if x["doi"] not in seen:
            chosen.append(x); seen.add(x["doi"])
    for i, x in enumerate(chosen):
        x["rank"] = i + 1
    json.dump(chosen, open(ROOT / "search" / "candidates.json", "w"), indent=1)
    (ROOT / "search" / "candidate_dois.txt").write_text("\n".join(x["doi"] for x in chosen) + "\n")
    flow["candidates_ranked"] = len(chosen)
    flow["candidate_mix"] = {k: sum(1 for x in chosen if x[f]) for k, f in
                             (("abide2", "abide2_seeded"), ("pred", "heuristic_predictive"), ("assoc", "heuristic_associational"))}
    json.dump(flow, open(ROOT / "search" / "prescreen_flow.json", "w"), indent=2)
    print(json.dumps(flow, indent=2))


if __name__ == "__main__":
    main()
