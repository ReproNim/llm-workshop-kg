"""Compare rebuilt CNP package results against the originally shipped results."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NEW = ROOT / "experiment" / "results"
OLD = ROOT / "experiment" / "results_original"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load(base, name):
    p = base / name
    return json.loads(p.read_text()) if p.exists() else None


def get(d, path):
    for k in path:
        if d is None:
            return None
        d = d[k] if isinstance(k, int) and isinstance(d, list) and k < len(d) else (d.get(k) if isinstance(d, dict) else None)
    return d


def tree_counts():
    tree = json.loads((ROOT / "research" / "tree.txt").read_text())["tree"]
    paths = [x["path"] for x in tree]
    t1 = {p.split("/")[0] for p in paths if re.match(r"sub-[^/]+/anat/sub-[^_]+_T1w\.nii\.gz$", p)}
    rest = {p.split("/")[0] for p in paths if re.match(r"sub-[^/]+/func/sub-[^_]+_task-rest_bold\.nii\.gz$", p)}
    return {"t1w": len(t1), "rest": len(rest), "t1w_and_rest": len(t1 & rest)}


def emb_val(d, seed, nn, key):
    for r in (d or {}).get("umap", []):
        if r.get("seed") == seed and r.get("nNeighbors") == nn:
            return r.get(key)
    return None


def pca_tw(d):
    if not d:
        return None
    for k in ("pca", "pca_trustworthiness_k15", "pca_trustworthiness"):
        v = d.get(k)
        if isinstance(v, dict):
            v = v.get("trustworthiness_k15")
        if isinstance(v, (int, float)):
            return v
    return None


def deriv(d):
    if not d:
        return None
    return {"n": len(d), "matches": sum(bool(x.get("matches")) for x in d)}


CHECKS = [
    # name, slide value, file, extractor, tolerance
    ("participants (SPARQL count)", 272, "competency_queries.json",
     lambda d: int(get(d, ["queries", "participants", "rows", 0, "n"])) if get(d, ["queries", "participants", "rows", 0, "n"]) else None, 0),
    ("phenotype tables", 52, "coverage.json", lambda d: get(d, ["tables"]), 0),
    ("table columns", 1983, "coverage.json", lambda d: get(d, ["table_variables"]), 0),
    ("observed cells", 411584, "coverage.json", lambda d: get(d, ["observed_cells"]), 0),
    ("missing cells", 127792, "coverage.json", lambda d: get(d, ["missing_cells"]), 0),
    ("image inventory pointers", 2531, "coverage.json", lambda d: get(d, ["image_inventory"]), 0),
    ("NIDM triples", 834327, "coverage.json", lambda d: get(d, ["triples"]), 0),
    ("combined graph triples", 1113959, "combined_summary.json", lambda d: get(d, ["triples"]), 0),
    ("Barratt parcel1 matches (n)", 272, "derivative_validation.json", lambda d: (deriv(d) or {}).get("matches"), 0),
    ("Barratt parcel1 checked (n)", 272, "derivative_validation.json", lambda d: (deriv(d) or {}).get("n"), 0),
    ("embedding participants", 272, "embedding_assessment.json", lambda d: get(d, ["n_participants"]), 0),
    ("embedding features", 10, "embedding_assessment.json", lambda d: get(d, ["n_features"]), 0),
    ("imputed cells", 3, "embedding_assessment.json", lambda d: get(d, ["imputed_cells"]), 0),
    ("UMAP trustworthiness seed42 k15", 0.874, "embedding_assessment.json", lambda d: emb_val(d, 42, 15, "trustworthiness_k15"), 0.0015),
    ("PCA trustworthiness k15", 0.805, "embedding_assessment.json", pca_tw, 0.0015),
    ("UMAP trustworthiness seed43", 0.868, "embedding_assessment.json", lambda d: emb_val(d, 43, 15, "trustworthiness_k15"), 0.0015),
    ("UMAP trustworthiness seed44", 0.879, "embedding_assessment.json", lambda d: emb_val(d, 44, 15, "trustworthiness_k15"), 0.0015),
    ("UMAP trustworthiness 30 neighbours", 0.867, "embedding_assessment.json", lambda d: emb_val(d, 42, 30, "trustworthiness_k15"), 0.0015),
    ("15-NN overlap seed43 vs 42 (~74%)", 0.74, "embedding_assessment.json", lambda d: emb_val(d, 43, 15, "mean_neighbor_overlap_with_seed42"), 0.01),
    ("15-NN overlap seed44 vs 42 (~74%)", 0.74, "embedding_assessment.json", lambda d: emb_val(d, 44, 15, "mean_neighbor_overlap_with_seed42"), 0.01),
    ("SHACL conforms", True, "shacl_summary.json", lambda d: get(d, ["conforms"]), None),
    ("SHACL mutation (missing source) rejected", True, "shacl_summary.json", lambda d: get(d, ["mutation_missing_source_rejected"]), None),
    ("JSON Schema valid", True, "skill/schema_validation.json", lambda d: get(d, ["valid"]), None),
    ("JSON Schema wrong numeric type rejected", True, "skill/schema_validation.json", lambda d: get(d, ["wrong_numeric_type_rejected"]), None),
    ("collaboration SHACL conforms", True, "collaboration_query.json", lambda d: get(d, ["conforms"]), None),
    ("collaboration missing reviewer rejected", True, "collaboration_query.json", lambda d: get(d, ["missing_reviewer_rejected"]), None),
]


def judge(slide, val, tol):
    if val is None:
        return "could-not-run"
    if tol is None or isinstance(slide, bool):
        return "matched" if val == slide else "differed"
    return "matched" if abs(float(val) - float(slide)) <= tol else "differed"


def main():
    rows = []
    for name, slide, f, ext, tol in CHECKS:
        try:
            new = ext(load(NEW, f))
        except Exception as e:  # noqa: BLE001
            new = None
            err = repr(e)
        else:
            err = None
        try:
            old = ext(load(OLD, f))
        except Exception:  # noqa: BLE001
            old = None
        status = judge(slide, new, tol)
        delta = None
        if status == "differed" and isinstance(new, (int, float)) and not isinstance(new, bool):
            delta = float(new) - float(slide)
        rows.append({"check": name, "slide_value": slide, "original": old, "rebuilt": new,
                     "status": status, "delta_vs_slide": delta, "file": f, "error": err})

    tc = tree_counts()
    for name, key, slide in [("T1w entries", "t1w", 265), ("resting BOLD entries", "rest", 268),
                             ("T1w + rest candidates", "t1w_and_rest", 261)]:
        rows.append({"check": name + " (recomputed from pinned Git tree)", "slide_value": slide, "original": slide,
                     "rebuilt": tc[key], "status": "matched" if tc[key] == slide else "differed",
                     "delta_vs_slide": tc[key] - slide, "file": "research/tree.txt", "error": None})

    files = []
    for p in sorted(OLD.rglob("*")):
        if p.is_file():
            rel = p.relative_to(OLD)
            q = NEW / rel
            files.append({"file": str(rel), "original_sha256": sha(p),
                          "rebuilt_sha256": sha(q) if q.exists() else None,
                          "identical": q.exists() and sha(q) == sha(p)})

    summary = {s: sum(r["status"] == s for r in rows) for s in ("matched", "differed", "could-not-run")}
    out = {"summary": summary, "checks": rows,
           "files": {"identical": sum(f["identical"] for f in files), "total": len(files), "detail": files},
           "not_rerun": ["skill_pilot.py extraction (frozen host-model artifacts; needs original web snapshots)",
                         "claims_and_questions.ttl (frozen input)", "make_report.py (HTML report)"]}
    (ROOT / "rebuild_comparison.json").write_text(json.dumps(out, indent=2, default=str))

    md = ["# CNP package rebuild vs original", "",
          f"Checks: {summary['matched']} matched, {summary['differed']} differed, {summary['could-not-run']} could not run.",
          f"Byte-identical result files: {out['files']['identical']} / {out['files']['total']}.", "",
          "| Check | Slide | Original | Rebuilt | Status |", "|---|---|---|---|---|"]
    for r in rows:
        md.append(f"| {r['check']} | {r['slide_value']} | {r['original']} | {r['rebuilt']} | {r['status']} |")
    md += ["", "Not re-run: " + "; ".join(out["not_rerun"]), "",
           "Files that differ byte-wise:", ""]
    md += [f"- {f['file']}" for f in files if not f["identical"]]
    (ROOT / "rebuild_comparison.md").write_text("\n".join(md) + "\n")
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
