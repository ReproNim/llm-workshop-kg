"""Assign stable source ids and split the corpus into four reading-balanced charting batches."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
N_BATCHES = 4


def main():
    corpus = json.load(open(ROOT / "corpus.json"))["items"]
    cands = {c["doi"]: c for c in json.load(open(ROOT / "search" / "candidates.json"))}
    items = []
    for i, e in enumerate(corpus):
        c = cands.get((e.get("doi") or "").lower(), {})
        items.append({"corpus_index": i, "pmid": e["pmid"], "doi": e.get("doi", ""), "title": e.get("title", ""),
                      "year": e.get("year", ""), "chars": len(e.get("full_text") or ""),
                      "rank": c.get("rank", 9999), "heuristic_predictive": c.get("heuristic_predictive"),
                      "abide2_seeded": c.get("abide2_seeded"), "full_text_source": e.get("full_text_source")})
    items.sort(key=lambda x: x["rank"])
    for k, x in enumerate(items, 1):
        x["source_id"] = f"S-{k:03d}"
    batches = [[] for _ in range(N_BATCHES)]
    load = [0] * N_BATCHES
    for x in sorted(items, key=lambda x: -x["chars"]):
        b = min(range(N_BATCHES), key=lambda i: (load[i], len(batches[i])))
        batches[b].append(x); load[b] += x["chars"]
    (ROOT / "batches").mkdir(exist_ok=True)
    for i, b in enumerate(batches, 1):
        b.sort(key=lambda x: x["source_id"])
        json.dump(b, open(ROOT / "batches" / f"batch_{i}.json", "w"), indent=1)
    json.dump({x["pmid"]: x["source_id"] for x in items}, open(ROOT / "batches" / "source_ids.json", "w"), indent=1)
    print(json.dumps([{"batch": i + 1, "n": len(b), "chars": load[i],
                       "predictive_heuristic": sum(1 for x in b if x["heuristic_predictive"]),
                       "abide2": sum(1 for x in b if x["abide2_seeded"])} for i, b in enumerate(batches)], indent=1))


if __name__ == "__main__":
    main()
