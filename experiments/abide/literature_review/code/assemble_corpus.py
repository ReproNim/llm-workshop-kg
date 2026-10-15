"""Choose the ~100-paper corpus from retrieved PDFs (rank order, quotas) and write the build_corpus manifest."""
import json, shutil, hashlib, fitz
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = 100
QUOTA = {"abide2_seeded": 25, "heuristic_predictive": 40, "heuristic_associational": 30}
MIN_TEXT = 5000


def main():
    cands = json.load(open(ROOT / "search" / "candidates.json"))
    routes = {}
    for m in sorted(ROOT.glob("pdfs_*/retrieval_manifest.json")) + sorted(ROOT.glob("pdfs_part*/retrieval_manifest.json")):
        for name, v in json.load(open(m)).items():
            routes.setdefault(v["doi"].lower(), (m.parent / name, v["full_text_source"]))
    retrieved, textless = [], []
    for c in cands:
        hit = routes.get(c["doi"])
        if not hit:
            continue
        path, route = hit
        try:
            n = sum(len(p.get_text()) for p in fitz.open(path))
        except Exception:
            n = 0
        if n < MIN_TEXT:
            textless.append(c["doi"]); continue
        retrieved.append((c, path, route))
    chosen, seen = [], set()

    def take(pred, n):
        for c, p, r in retrieved:
            if sum(1 for x in chosen if pred(x[0])) >= n:
                return
            if c["doi"] not in seen and pred(c):
                chosen.append((c, p, r)); seen.add(c["doi"])

    take(lambda c: c["must_include"], 99)
    for k, n in QUOTA.items():
        take(lambda c, k=k: c[k], n)
    for c, p, r in retrieved:
        if len(chosen) >= TARGET:
            break
        if c["doi"] not in seen:
            chosen.append((c, p, r)); seen.add(c["doi"])
    chosen.sort(key=lambda x: x[0]["rank"])
    final = ROOT / "pdfs"
    for f in final.glob("*.pdf"):
        f.unlink()
    manifest, hashes = [], {}
    for c, p, r in chosen:
        name = c["doi"].replace("/", "_") + ".pdf"
        shutil.copy2(p, final / name)
        hashes[name] = hashlib.sha256((final / name).read_bytes()).hexdigest()
        manifest.append({"file": name, "doi": c["doi"], "title": c["title"], "authors": c["authors"],
                         "journal": c["journal"], "year": str(c["year"] or ""), "abstract": c["abstract"],
                         "source": "openalex", "full_text_source": r})
    json.dump(manifest, open(ROOT / "corpus_manifest.json", "w"), indent=1)
    json.dump(hashes, open(ROOT / "pdf_sha256.json", "w"), indent=1)
    stats = {"candidates": len(cands), "retrieved_pdf": len(routes), "retrieved_ranked": len(retrieved) + len(textless),
             "too_little_text": textless, "corpus": len(chosen),
             "mix": {k: sum(1 for c, _, _ in chosen if c[k]) for k in QUOTA},
             "must_include_present": [c["doi"] for c, _, _ in chosen if c["must_include"]],
             "routes": {}}
    for _, _, r in chosen:
        stats["routes"][r] = stats["routes"].get(r, 0) + 1
    json.dump(stats, open(ROOT / "search" / "assembly_stats.json", "w"), indent=2)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
