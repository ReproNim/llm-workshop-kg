# /// script
# requires-python = ">=3.11"
# dependencies = ["rdflib>=7"]
# ///
"""Parse every Turtle file in the repository and report its triple count.

    uv run scripts/parse_all_ttl.py [output.json]
"""

import json
import sys
from pathlib import Path

import rdflib

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "node_modules", ".venv"}

counts, failures = {}, {}
for path in sorted(ROOT.rglob("*.ttl")):
    if SKIP & set(path.parts):
        continue
    rel = str(path.relative_to(ROOT))
    try:
        counts[rel] = len(rdflib.Graph().parse(path, format="turtle"))
    except Exception as exc:  # report every failure, not just the first
        failures[rel] = str(exc)[:300]
report = {"files": len(counts) + len(failures), "triples": sum(counts.values()), "counts": counts, "failures": failures}
out = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if out:
    out.write_text(json.dumps(report, indent=1))
print(f"{report['files']} Turtle files, {report['triples']:,} triples, {len(failures)} failures")
sys.exit(1 if failures else 0)
