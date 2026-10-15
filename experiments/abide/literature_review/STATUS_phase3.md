# Phase 3 status (merge, verification, export, synthesis, KG, figures)

Scripts: `phase3/` (run from that dir; exporters via `uv run --project <ssenv> python …`).

## Step 1 — corpus integrity: DONE
`phase3/s1_integrity.py` → `phase3/integrity.json`. Test per item: title prefix in first 5k chars, or
≥60 % title-token overlap in first 5k chars, or DOI string in first 20k chars.
- 98/99 plausible (all others: title-token overlap 1.0).
- **1 mismatch: S-040** `10.1016/j.biopsych.2017.09.029` (Cerebellar volume in autism) — corpus full_text is
  a HAL preprint (hal-01684048) on motion/form perception; title-token overlap 0.23, DOI absent.
  Charting agent already assessed it `abstract_only` (exclude, Exclusion 3); reason will be re-prefixed
  "Abstract only — full text mismatched" at merge.

## Step 2 — quote re-verification: DONE
`phase3/s2_quotes.py` → `phase3/records_verified.json` (batch records with failures removed) and
`phase3/quote_verification.json` (stats + every dropped quote). Normalisation (`phase3/common.py::norm`),
applied identically to quote and full text: ligatures ﬁ ﬂ ﬀ ﬃ ﬄ, curly quotes, dash variants, soft
hyphen and zero-width chars removed, NFKC, whitespace collapsed, case-folded; then fallbacks for
spacing-only differences and line-wrap hyphenation (`iden- tified` / `multi-\nsite`).
- 1,743 quotes checked (577 evidence spans, 77 quoted segments inside RoB `support`, 874 custom_field
  quotes, 215 kg_link quotes). 1,735 pass: 1,520 exact after normalisation, 214 via hyphenation, 1 via spacing.
- **8 dropped — all empty quote strings** (S-014 evidence_spans 4/6/8; S-041 spans 4/5; kg_link quotes
  S-013, S-029, S-041). No non-empty quote failed. Note S-014 span 6 claimed "F-score feature selection
  was computed using all features" with no quote — the claim is dropped with it.
- 49 custom_field answers carried `| quote: ""` (no quote); the empty marker was removed, the answer kept.
- S-040 (mismatched) carries only a kg_link with no quotes; its quotes would be checked against the abstract.
- 15 included articles have >8 evidence spans (protocol `evidence_spans_per_article`=8); all verified spans kept.

## Step 4 — synthesis: DONE (run before step 3, whose review.json uses it)
`phase3/s4_synthesis.py` → `results_synthesis.json`, `synthesis.md`. Categorical rules over charted fields;
evaluation schemes (`EVAL`), headline accuracies (`ACC`) and site handling (`SITE`) are per-paper tables whose
snippet must occur verbatim in that paper's charted text (script asserts). Key numbers: 74 included / 25
excluded (21 Excl. 3 structural/phenotype-only, 4 Excl. 4 benchmark-only); release I 54, I+II 16, II 4; claim
predictive 46, both 7, associational 20, descriptor 1; 53 predictive: pooled k-fold 26, LOSO 6, LOOCV 5,
single split 9, external 4, within-site 12; accuracy medians pooled 73.3% (n=23), LSO 66.8% (n=5);
8 leakage-flagged; RQ6 yes 17 (participant list 4) / partly 42 / no 15; 6 shared-cohort groups (largest
ABIDE I N=871, 9 papers incl. S-002 Abraham, S-019 Parisot, S-024 Ktena).

## Step 3 — review.json + exports: DONE
`phase3/s3_assemble.py` → `phase3/review_draft.json`; `update_provenance.py --provenance phase3/search_provenance_phase3.json
--replace-queries` (search_provenance.json + a search_notes line with the not-retrieved reasons, since the flow
model has no slot) → `review.json`; `export_review.py review.json --check` → **✓ Exportable, 1 warning**
(registration_number unset). Exported `out/review.md`, `out/review.ttl` (21,087 triples, rdflib), `out/review.json`.
Rebuild all of phase 3 with `phase3/run_export.sh`.
- Flow: 994 identified (OpenAlex 992 + other 2) → 268 dup → 726 screened (metadata) → 314 excluded (310 not OA, 4
  non-primary) → 200 sought → 101 not retrieved → 99 retrieved/assessed (98 full text, 1 abstract-only: S-040)
  → 25 excluded (21 Excl. 3, 4 Excl. 4) → 74 included (all full text).
- RQ1–RQ6 + CL1–CL8 in custom_fields; exporters emit Appendix B / slr:ResearchQuestion (14 questions, 1,036 answers).
- Normalisations: 4 differently shaped critical_appraisal objects mapped onto the 4 protocol domains; 2 RoB
  judgments charted "N/A" stored as Unclear with "[charted judgment: N/A]" prefix (enum has no N/A); 28 charting
  rubrics lacking bibliographic fields filled from corpus metadata.
- Agent provenance: run_configuration + agent_invocations (8 charting batches, Claude Sonnet; merge agent).
  Intake provenance stays in intake_provenance.ttl (exporters have no slot) and is merged into literature_kg.ttl.
- Known exporter boilerplate: review.md §2.4 says "AI-assisted batch screening with human verification" — there
  was no human verification of individual decisions in this run.

## Step 5 — knowledge graph: DONE
`phase3/s5_kg.py` → `literature_kg.ttl` (**10,779 triples**, parses with rdflib). Reuses `../graph` dataset IRIs
`urn:repronim:abide:dataset/abide_i` / `abide_ii` and its `ex:DatasetPublicationLink` pattern (ex:dataset,
ex:publication, ex:status, ex:evidenceQuote); `../graph` read only. Per article: DOI publication node
(skos:exactMatch to 37 existing ../graph publication nodes), link with status `uses-data (charted)` /
`describes-release (charted)` / `mentions`, `ex:AnalysedCohort` (N by DX, sites, release, selection rule, QC rule,
reconstructible), pipeline/atlas (stated + category), claim type, finding, evaluation scheme(s),
PROBAST/JBI overall, leakage flag, `ex:ReportedPerformance` nodes, 610 `ex:EvidenceQuote` prov:Entities
(prov:wasQuotedFrom DOI, sourceLocator = corpus id + full-text sha256 + section + char offset), 6
`ex:SharedCohortDefinition` nodes. Provenance: charted entities prov:wasGeneratedBy `charting-batch-N`
(SoftwareAgent, model Claude Sonnet, batch id) whose association hadPlan charting_instructions → protocol plan →
intake session (intake_provenance.ttl merged in, 4 slr:UserInput); derived categories/shared cohorts/performance
by `phase3-merge` (claude-opus-5-5). `phase3/s5_sparql_checks.py` → `phase3/s5_sparql_checks.txt`: 12/12 checks
match results_synthesis.json.

## Step 6 — figures: DONE
`phase3/s6_figures.py` (matplotlib via `uv run --with matplotlib`, the pinned env is untouched) →
`figures/prisma_flow.{png,svg}` and `figures/accuracy_by_evaluation.{png,svg}`, 1920×1080, text 14–26 pt,
blue/orange/gray from a colour-blind-checked palette; leakage-flagged = hollow orange ring (shape + colour),
leave-site-out column shaded and blue. Accuracy-figure title states only what the data show: "Reported ABIDE
accuracy is lower when whole sites are held out" (median 73% pooled, n=23 vs 67% LSO, n=5; S-030 and S-072
labelled with their pooled values; footer: descriptive, not a controlled comparison).

## Step 7 — report: DONE (returned to caller). Whole phase rebuilds with `phase3/run_export.sh`.

## Open items
- review.md §2.4 carries exporter boilerplate "AI-assisted batch screening with human verification"; no human
  verification of individual decisions happened. Fix needs an exporter change or a post-edit.
- No human double-charting; categorical tables (EVAL/ACC/SITE in s4_synthesis.py) are merge-agent assignments tied
  to charted snippets — worth a human spot-check before the talk, especially headline-accuracy choices.
- S-040: the real cerebellar-volume paper's PDF was never obtained; Di Martino 2014 (ABIDE I descriptor) not retrieved.
- Within-site accuracies for S-020/S-036/S-058/S-059 are best single site (no average reported).
- registration_number unset (only --check warning). Intake provenance is in literature_kg.ttl, not in review.ttl.
