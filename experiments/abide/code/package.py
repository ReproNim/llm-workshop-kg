"""Assemble ../ABIDE_Collaboration_Knowledge_Graph.zip with SHA256SUMS and a manifest.

Bulk inputs (time series, thickness files, paper texts, ReproNim files) and derived caches (Oxigraph store,
view dumps, npz) are left out; rebuild.sh fetches and regenerates them.

Usage: uv run python code/package.py
"""

import json
import zipfile

from common import ROOT, sha256_file

TOP = "ABIDE_Collaboration_Experiment"
INCLUDE_DIRS = ["literature_review", "code", "graph", "queries", "results", "figures", "comparison", "orcd", "scheduling", "data/Resources", "data/vocab"]
INCLUDE_FILES = ["data/openalex_abide.json", "README.txt", "STATUS.md", "report.html", "rebuild.sh", "pyproject.toml", "uv.lock", ".python-version",
                 "data/Phenotypic_V1_0b_preprocessed1.csv", "data/expected_sha256.json", "data/download_manifest.json", "data/resources_pinned.json"]
EXCLUDE_PARTS = ("__pycache__", ".DS_Store", "pdfs", "archive")


def files() -> list:
    """Every file to ship, relative to ROOT."""
    out = [ROOT / f for f in INCLUDE_FILES]
    for d in INCLUDE_DIRS:
        out += [p for p in (ROOT / d).rglob("*") if p.is_file()]
    def skip(p) -> bool:
        rel = p.relative_to(ROOT).parts
        return (any(x in rel for x in EXCLUDE_PARTS) or rel[:2] == ("queries", "original") or any(x.startswith("pdfs") for x in rel)
                or (rel[0] == "literature_review" and p.suffix.lower() == ".pdf"))
    return sorted({p for p in out if not skip(p)})


def main() -> None:
    """Write SHA256SUMS.json, MANIFEST.json and the zip."""
    fs = files()
    sums = {str(p.relative_to(ROOT)): sha256_file(p) for p in fs}
    (ROOT / "SHA256SUMS.json").write_text(json.dumps(sums, indent=1, sort_keys=True))
    (ROOT / "SHA256SUMS").write_text("".join(f"{h}  {f}\n" for f, h in sorted(sums.items())))
    manifest = {"files": len(sums) + 3, "checksums": "SHA256SUMS (shasum -a 256 -c SHA256SUMS) and SHA256SUMS.json", "bytes": sum(p.stat().st_size for p in fs),
                "not_included": ["data/Outputs (CC200 time series, ANTs thickness): fetched by code/download.py",
                                 "data/papers: fetched; not redistributed", "data/repronim_simple2: fetched at pinned commits",
                                 "literature_review/pdfs*/ and any literature_review PDF: paper PDFs not redistributed (hashes in literature_review/pdf_sha256.json)",
                                 "data/abstractatlas: fetched by content hash",
                                 "data/derived: regenerated (connectivity cache, Oxigraph store, view dumps, PyNIDM output)"]}
    (ROOT / "MANIFEST.json").write_text(json.dumps(manifest, indent=1))
    dest = ROOT.parent / "ABIDE_Collaboration_Knowledge_Graph.zip"
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in fs + [ROOT / "SHA256SUMS", ROOT / "SHA256SUMS.json", ROOT / "MANIFEST.json"]:
            z.write(p, f"{TOP}/{p.relative_to(ROOT)}")
    print(dest, round(dest.stat().st_size / 1e6, 1), "MB,", manifest["files"], "files")


if __name__ == "__main__":
    main()
