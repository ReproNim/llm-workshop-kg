# Charting instructions — ABIDE I/II review (phase 2)

You chart one batch (`batches/batch_N.json`). Each entry gives `source_id` (S-001…), `pmid`
(the corpus id, `local_<sha8>`), `doi`, `title`, and `corpus_index` into `corpus.json["items"]`, whose
entry holds the full text (`full_text`) and its provenance. Read the **whole** full text —
methods, results, tables and supplementary statements included — not the abstract.

Protocol: `protocol.json` (research questions RQ1–RQ6, checklist CL1–CL8, appraisal domains).
Schema: `export_review.py --print-template` (skill: `~/software/sensein/agent_skills/skills/synthscholar/scripts/`,
run with the uv env at `${SYNTHSCHOLAR_ENV}`, `uv run python …`).
Write `batches/batch_N_records.json`: a list with **one object per article in the batch**, keys below.
Do not edit `corpus.json`, `protocol.json` or other batches. Phase 3 merges all batches into
`review.json` and runs `export_review.py --check`.

## Rules that apply everywhere

- Quote verbatim. Every supporting quote must be a substring of that article's `full_text`
  (whitespace-normalised); phase 3 checks this mechanically and drops anything that fails.
- Only the paper's **own** evidence. A number the paper cites from another study is not its finding.
- Never fill a field by inference. Use `""` when the paper does not report it.
- No invented numbers: N, accuracies, AUCs, effect sizes and p-values must appear in the text.

## Per-article object

```json
{
  "source_id": "S-017",
  "pmid": "local_1a2b3c4d",
  "doi": "10.xxxx/…",
  "screening": {                       // ScreeningLogEntry, stage full_text
    "decision": "include" | "exclude",
    "reason": "specific reason (cite the criterion number, e.g. 'Exclusion 3: structural MRI only')",
    "stage": "full_text",
    "assessed_on": "full_text",        // or "abstract_only" if full_text is empty/garbled; reason then starts "Abstract only — "
    "full_text_source": "<copy corpus entry full_text_source>"
  },
  // ---- the remaining keys only when decision == include ----
  "evidence_spans": [                  // EvidenceSpan, ≤ 8, the paper's main findings
    {"text": "<verbatim quote>", "section": "results|methods|discussion|abstract|table",
     "claim": "<one-sentence claim the quote supports>", "relevance_score": 0.0-1.0}
  ],
  "risk_of_bias": {                    // Article.risk_of_bias
    "assessments": [{"domain": "...", "judgment": "Low|High|Unclear", "support": "<reason, quote where possible>"}],
    "overall": "Low|High|Unclear", "summary": "..."
  },
  "charting": { ... DataChartingRubric ... },
  "critical_appraisal": { ... CriticalAppraisalRubric ... },
  "narrative_row": { ... PRISMANarrativeRow ... },
  "kg_link": { ... knowledge-graph link record ... }
}
```

### Screening

Apply protocol inclusion 1–4 and exclusion 1–6 to the full text. Typical exclusions here:
ABIDE only cited (exclusion 2); structural/DTI/phenotype-only use (3); registration/motion
methods benchmark without an autism-vs-control analysis (4). A paper using ABIDE data as one
of several datasets is **included** if it reports an ABIDE resting-state analysis.

### Risk of bias (`risk_of_bias`)

- Predictive papers (RQ3 = predictive): PROBAST domains, exactly these names —
  `Participants`, `Predictors`, `Outcome`, `Analysis`. Analysis is High when feature selection,
  scaling or harmonisation used test data, when only accuracy on a single random split is
  reported without uncertainty, or when site is ignored with pooled CV.
- Associational papers: `rob_tool` is "JBI Critical Appraisal" — use the JBI analytical
  cross-sectional items as domains: `Inclusion criteria defined`, `Subjects and setting described`,
  `Exposure measured validly (rs-fMRI pipeline)`, `Condition measured (diagnosis source)`,
  `Confounders identified (age, sex, site, motion)`, `Confounders handled`,
  `Outcomes measured validly (connectivity metric)`, `Appropriate statistical analysis (multiple comparisons)`.
- Data descriptors (Di Martino 2014/2017): judge the same JBI items on what they report.

### Charting (`charting`, a DataChartingRubric)

Fill sections A–G where reported (`""` otherwise). Mapping for this corpus:
`disorder_cohort` = "Autism spectrum disorder (ABIDE I)" / "(ABIDE II)" / "(ABIDE I+II)";
`study_design` = one of `Group-difference (associational)`, `Diagnostic prediction`,
`Both`, `Data descriptor` (this is the `grouping_dimension`);
`n_disordered` / `n_controls` = analysed ABIDE N (not the full release);
`data_types` = "resting-state fMRI" (+ others used);
`feature_extraction_tools` = pipeline (CPAC/DPARSF/NIAK/CCS/fMRIPrep/custom + version);
`specific_features` = connectivity measure + atlas;
`model_category` / `specific_algorithms` / `validation_methodology` / `performance_metrics` /
`key_performance_results` for predictive papers;
`features_associated_disorder` / `feature_change_direction` for associational papers;
`dataset_openly_available` = whether code/participant list is released (and where).

`custom_fields` — **one key per research question id and per checklist id**, exact keys:
`RQ1` … `RQ6`, and the checklist questions keyed by their full text as written in
`protocol.charting_questions` (e.g. `"CL1 Cohort definition reported (inclusion/exclusion rules and resulting N by diagnosis)?"`).
Each value: a concise answer followed by ` | quote: "<verbatim supporting quote>"`. For CL items
answer `Yes`, `No` or `Partly` first. RQ3 answer must start with `associational`,
`predictive`, `both` or `descriptor`. RQ6 answer must start with `yes — participant list`,
`yes — exact rules`, `partly` or `no`.

### Critical appraisal (`critical_appraisal`, CriticalAppraisalRubric)

Four domains, named exactly as `protocol.appraisal_domains`, keys
`domain_1_participant_quality` … `domain_4_bias_transparency`. Items:
domain 1 ← CL1, CL2 (+ PROBAST D1 signalling questions for predictive papers);
domain 2 ← CL3, CL4; domain 3 ← diagnosis source and label definition;
domain 4 ← CL5, CL6, CL7. `rating` ∈ `Yes|No|Partial|Unclear|N/A`; `overall_concern` ∈ `Low|Some|High`.

### Narrative row (`narrative_row`)

`study_design_sample_dataset` (design, ABIDE release, N by diagnosis, sites), `methods`,
`outcomes`, `key_limitations`, `relevance_notes` (what this paper contributes to the
dataset–publication link), `review_specific_questions` = "".

### Knowledge-graph link record (`kg_link`)

```json
{
  "doi": "10.xxxx/…",
  "dataset": "ABIDE I" | "ABIDE II" | "ABIDE I+II",
  "relation": "uses-data" | "describes-release" | "mentions",
  "cohort_description": "<selection rules as stated>",
  "n_by_dx": {"ASD": 0, "TD": 0, "total": 0},          // null for any value not reported
  "sites": "<number or list as stated, or ''>",
  "pipeline": "<pipeline + strategy + version>",
  "atlas": "<parcellation>",
  "claim_type": "associational" | "predictive" | "both" | "descriptor",
  "finding": "<main finding, one sentence, with numbers as reported>",
  "reconstructible": "yes — participant list" | "yes — exact rules" | "partly" | "no",
  "evidence_quotes": ["<verbatim>", "..."]
}
```

Excluded articles carry only `source_id`, `pmid`, `doi`, `screening` and, if ABIDE is named,
a `kg_link` with `relation: "mentions"` and empty analysis fields.
