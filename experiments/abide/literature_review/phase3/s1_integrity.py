"""Step 1: check each corpus full_text corresponds to its title/DOI."""
import json
import re
from common import ROOT, load_corpus, load_records, norm

STOP = set("a an the of in and or for with to on by from using via at as is are its into based between among across".split())


def tokens(s):
    return [t for t in re.findall(r"[a-z0-9]+", norm(s)) if t not in STOP and len(t) > 2]


def main():
    corpus = load_corpus()
    sid = {r["pmid"]: r["source_id"] for r in load_records()}
    rows = []
    for e in corpus:
        ft = e.get("full_text") or ""
        head = norm(ft[:5000])
        head_tok = set(re.findall(r"[a-z0-9]+", head))
        tt = tokens(e.get("title", ""))
        overlap = sum(1 for t in tt if t in head_tok) / max(1, len(tt))
        doi = (e.get("doi") or "").lower()
        doi_in = doi and doi in norm(ft[:20000]).replace(" ", "")
        doi_any = doi and doi in norm(ft).replace(" ", "")
        title_contig = norm(e.get("title", ""))[:60] in head
        ok = title_contig or overlap >= 0.6 or doi_in
        rows.append({"source_id": sid.get(e["pmid"]), "pmid": e["pmid"], "doi": e.get("doi"), "title": e.get("title"),
                     "title_token_overlap_head5k": round(overlap, 2), "title_prefix_in_head": bool(title_contig),
                     "doi_in_first20k": bool(doi_in), "doi_anywhere": bool(doi_any), "chars": len(ft),
                     "head_preview": re.sub(r"\s+", " ", ft[:200]), "plausible": bool(ok)})
    rows.sort(key=lambda r: r["source_id"])
    bad = [r for r in rows if not r["plausible"]]
    weak = [r for r in rows if r["plausible"] and r["title_token_overlap_head5k"] < 0.8 and not r["doi_in_first20k"]]
    json.dump({"n": len(rows), "mismatched": [r["source_id"] for r in bad],
               "weak_but_plausible": [r["source_id"] for r in weak], "items": rows},
              open(ROOT / "phase3" / "integrity.json", "w"), indent=1, ensure_ascii=False)
    print("mismatched:", [(r["source_id"], r["doi"], r["title_token_overlap_head5k"], r["head_preview"][:120]) for r in bad])
    print("weak:", [(r["source_id"], r["title_token_overlap_head5k"], r["title"][:60], r["head_preview"][:100]) for r in weak])


if __name__ == "__main__":
    main()
