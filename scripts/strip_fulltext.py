# /// script
# requires-python = ">=3.11"
# dependencies = ["rdflib>=7"]
# ///
"""Remove article full text from the literature-review files before publication.

Full text is kept only as its SHA-256 (``content_sha256``) so a re-fetched copy can be
verified. Run from the repository root:

    uv run scripts/strip_fulltext.py experiments/abide/literature_review
"""

import json
import sys
from pathlib import Path

import rdflib

TEXT_KEYS = ("full_text", "_head_text")
NOTE = "omitted from the public repository (publisher licences vary); re-fetch with literature_review/code and verify content_sha256"
SLR_CONTENT = rdflib.URIRef("https://w3id.org/slr-ontology/content_text")


def strip_json(obj):
    """Return the number of characters removed from ``obj`` in place."""
    removed = 0
    if isinstance(obj, dict):
        for key in TEXT_KEYS:
            if isinstance(obj.get(key), str) and obj[key]:
                removed += len(obj[key])
                obj[key] = None
                obj["full_text_note"] = NOTE
        for value in obj.values():
            removed += strip_json(value)
    elif isinstance(obj, list):
        for value in obj:
            removed += strip_json(value)
    return removed


def strip_ttl(path):
    """Drop slr:content_text triples; return the number of triples removed."""
    graph = rdflib.Graph().parse(path)
    triples = list(graph.triples((None, SLR_CONTENT, None)))
    for triple in triples:
        graph.remove(triple)
    if triples:
        graph.serialize(path, format="turtle")
    return len(triples)


def main(root):
    root = Path(root)
    for path in sorted(root.rglob("*.json")):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        removed = strip_json(data)
        if removed:
            path.write_text(json.dumps(data, indent=1, ensure_ascii=False))
            print(f"{path}: removed {removed} characters of full text")
    for path in sorted(root.rglob("*.ttl")):
        removed = strip_ttl(path)
        if removed:
            print(f"{path}: removed {removed} content_text triples")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "experiments/abide/literature_review")
