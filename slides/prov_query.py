# /// script
# requires-python = ">=3.11"
# dependencies = ["pyoxigraph>=0.4"]
# ///
"""Count slides by checking status in talk_provenance.ttl with pyoxigraph; writes provenance_query.json."""
import json
from pathlib import Path
import pyoxigraph as ox

HERE = Path(__file__).parent
QUERY = """PREFIX talk: <https://repronim.org/talks/kg-skills-2026#>
SELECT ?status (COUNT(?slide) AS ?n) WHERE {
  ?a talk:assesses ?slide ; talk:checkingLabel ?status .
} GROUP BY ?status ORDER BY DESC(?n)"""
store = ox.Store()
store.load(path=str(HERE / "talk_provenance.ttl"), format=ox.RdfFormat.TURTLE)
rows = [{"status": r["status"].value, "n": int(r["n"].value)} for r in store.query(QUERY)]
(HERE / "provenance_query.json").write_text(json.dumps({"query": QUERY, "rows": rows, "triples": len(store)}, indent=1))
print(rows, len(store))
