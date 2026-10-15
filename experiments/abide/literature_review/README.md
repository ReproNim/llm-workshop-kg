# ABIDE I/II literature review (SynthScholar skill, phase 1: protocol + corpus)

Skill: `sensein/agent_skills` skills/synthscholar v0.3.0 at dde5425 (Mode 1 intake + Mode 3 BYO
corpus, path B agent-authored). Exporters need the SynthScholar development checkout:
`sensein/synthscholar` branch `improve_verification` at da23314 (branch `main` at f2f41a6 lacks
`synthscholar.text_windows` / `synthscholar.ezproxy`, which the skill's scripts require). Local env:
uv project with `synthscholar[fulltext]` editable from that checkout, Python 3.12.

## Decisions (review owner, recorded in `intake_provenance.ttl` as slr:UserInput)

Scope ABIDE I and II · ~100 open-access papers · agent-authored stages serialised through the
skill's exporters (no OpenRouter key) · PROBAST for prediction papers, JBI cross-sectional items +
reporting checklist CL1–CL8 for group-difference papers. Everything else in `protocol.json` was
drafted by the agent; `validate_protocol.py` passes (warnings only: no registration number, no funding).

## PRISMA flow so far (`search_provenance.json`)

| Step | Count |
|---|---|
| Identified: OpenAlex, citing Di Martino 2014 + "ABIDE" in title/abstract | 598 |
| Identified: OpenAlex, citing Di Martino 2017 + "ABIDE" | 174 |
| Identified: OpenAlex, citing Abraham 2017 + "ABIDE" | 220 |
| Identified: other sources (the two release descriptors by DOI) | 2 |
| Total identified | 994 |
| Duplicates removed | 268 |
| Records screened on metadata | 726 |
| Excluded on metadata (310 not open access; 4 non-primary type/review title) | 314 |
| Open-access primary records eligible for retrieval | 412 |
| Reports sought (top 200 by citations, with quotas — `search/selection_rule.md`) | 200 |
| Reports not retrieved | 101 |
| Reports retrieved = corpus assessed for eligibility (phase 2) | 99 |

The metadata screen is not a title/abstract reading; screening on full text happens in phase 2.
Open-access records outside the top 200 were not sought (corpus-size decision).

Not retrieved (101), with reasons (`search_provenance.json` → `not_retrieved_reasons`):
47 had no open-access PDF location known to Unpaywall/OpenAlex/Semantic Scholar; 23 had a publisher
OA URL that returned an HTML bot-check page instead of a PDF; 49 of the misses have a PMCID, but
the PMC routes were blocked on 2026-10-15 (Europe PMC `?pdf=render` HTTP 403, Europe PMC
`fullTextXML` HTTP 500, NCBI PMC OA service 404); the 40-paper extension batch was not re-checked by
the second pass. **Di Martino 2014 (ABIDE I descriptor, a must-include) was not retrieved**: its OA
copies are a repository landing page whose file link returned a bot-check page, and PMC4162310.

## Corpus (`corpus.json`, 99 entries; `build_corpus.py --check` passes)

- Extraction: PyMuPDF (`--no-docling`). Docling was measured on one PDF: 47 s and 2.9 GB peak RSS
  (21,087 chars), i.e. ~80 min serial for 99 papers; PyMuPDF was used for this phase. Re-run
  with Docling for any paper where tables matter at charting.
- Retrieval routes: unpaywall_pdf 96, openalex_pdf 3. All entries have DOI, title, authors, year,
  abstract (from the OpenAlex manifest) and full text (10,930–162,027 chars, median 63,246).
- Mix (selection heuristics, not charted values): 26 seeded by/naming ABIDE II, 65 prediction
  vocabulary, 23 group-difference vocabulary (quota target 30 not met after retrieval losses).
  Must-includes present: Di Martino 2017, Abraham 2017.
- 98/99 full texts contain "ABIDE"; 10.1016/j.biopsych.2017.09.029 (cerebellar volume) names the
  dataset only in long form — a likely exclusion at full-text screening (structural only).
- PDFs: `pdfs/` (282 MB, gitignored); hashes in `pdf_sha256.json`, routes in `corpus_manifest.json`.

## Phase 2 (prepared, not run)

`batches/batch_1..4.json` (24/24/25/26 articles, ~1.52 M characters each; `source_ids.json` maps
pmid → S-nnn in citation-rank order) and `charting_instructions.md` (fields per article, RQ1–RQ6 and
CL1–CL8 custom_fields with verbatim quotes, PROBAST/JBI domains, knowledge-graph `kg_link` records).

## Rebuild

```bash
python3 code/search_openalex.py          # identification (OpenAlex; counts drift over time)
python3 code/select_corpus.py            # metadata screen + ranking → search/candidates.json
SYNTHSCHOLAR_EMAIL=… uv run python <skill>/scripts/fetch_ezproxy.py --doi-file search/candidate_dois.txt --pdf-dir pdfs_part0 --oa-only
uv run python code/fetch_fallback.py search/missing_dois.txt pdfs_fallback
uv run python code/assemble_corpus.py    # → pdfs/, corpus_manifest.json, pdf_sha256.json
uv run python <skill>/scripts/build_corpus.py --dir pdfs --manifest corpus_manifest.json --source openalex --no-docling --out corpus.json
uv run python code/make_batches.py
python3 code/write_search_provenance.py
```
