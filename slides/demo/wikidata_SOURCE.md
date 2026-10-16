# Wikipedia / Wikidata example (retrieved 2026-10-16)

- Wikidata item Q48360 "hippocampus" — https://www.wikidata.org/wiki/Q48360 (lastrevid 2516828778, modified 2026-07-13).
  Summary of statements and identifiers: `wikidata_Q48360_summary.json` (62 sitelinks; enwiki "Hippocampus").
- English Wikipedia "Hippocampus" — https://en.wikipedia.org/wiki/Hippocampus (revision 1374836959). Short quote used:
  "a major component of the brain of humans and many other vertebrates".
- Query (https://query.wikidata.org/sparql), result in `wikidata_temporal_lobe_parts.json`:

```sparql
SELECT ?r ?rLabel ?nn WHERE {
  ?r wdt:P361 wd:Q744385 .            # part of: temporal lobe
  OPTIONAL { ?r wdt:P4394 ?nn }       # NeuroNames ID
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
} ORDER BY ?rLabel
```
5 rows: archicortex (NeuroNames 170), auditory cortex (1354), entorhinal cortex (168), hippocampus (3157), Q2205433 (no English label).
