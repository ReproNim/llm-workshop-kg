# Structured (schema-driven) extraction

Use this when the user has a **target JSON schema** (their own, or a known one like ReproSchema, Croissant, schema.org Dataset, JSON-LD, …) and wants a document mapped into it.

The pattern is the same — extractor → alignment → judge — but the **schema is the contract**, not the entity taxonomy.

## When to pick this over NER or resource extraction

| Signal | Use |
|---|---|
| User says "I have a JSON schema" or "convert this PDF to ReproSchema/JSON-LD/Croissant" | **structured extraction** |
| User says "extract entities" / "find all genes" | NER |
| User says "what models/datasets are in this paper" | resource extraction |
| User wants a single deeply-nested record per document | structured extraction |
| User wants many shallow items per document | NER |

## Step 1: lock the schema before anything else

The extractor cannot guess the schema. Ask the user for one of:

1. A JSON Schema (preferred).
2. A worked example output (next best).
3. A bulleted field list with types and required-ness.

If they give an example, derive a JSON Schema from it before running. Save it under `schemas/<task>.schema.json` so future runs use the same contract.

## Step 2: write the extractor prompt around the schema

In the extractor's system prompt:

1. Put the **full JSON Schema** inline.
2. State: "Output JSON that validates against this schema. Nothing else."
3. For each required field, give a one-line description and one example value.
4. For enums, list them explicitly: "`inputType` must be one of: `radio | text | number | slider`."
5. For nullable fields, say so: "If `citation` is not in the source, set it to `null`."

See `prompts/extractor-structured.md`.

## Step 3: validate before returning

After parsing the LLM's JSON, run a real JSON Schema validator (e.g. `jsonschema` in Python). If it fails:

1. Capture the validation error path (e.g. `items[3].responseOptions[1].value: missing`).
2. Send the LLM a **repair prompt** with the original JSON + the validator's error, asking it to emit ONLY the fixed JSON.
3. Re-validate. Cap at 2 repair attempts; if still failing, return partial output + `errors[]`.

## Step 4: alignment for structured extraction

Often the schema has fields that should be ontology IRIs (e.g. ReproSchema's `responseOption.valueType` ideally maps to xsd or OBO concepts). Strategy:

- Mark in the schema **which fields are mapping targets** (your task-specific decision).
- The alignment stage walks those paths in the JSON, looks up each value, and replaces it (or adds a sibling) with the mapped IRI.
- Always preserve the original string in `<field>_raw` so nothing is lost.

```jsonc
{
  "inputType": "radio",
  "inputType_raw": "radio",
  "inputType_iri": "https://schema.repronim.org/inputTypes/radio"
}
```

## Step 5: judging structured extraction

Two kinds of judging:

- **Schema-validity score** (deterministic, no LLM): 1.0 if JSON validates; 0 if not.
- **Faithfulness score** (LLM): for each top-level field, "is this value supported by the source text? Score 0–1, give one-line `remarks`." Emit a `field_judgments` object alongside the data.

```jsonc
{
  "data": { ... },
  "schema_valid": true,
  "field_judgments": {
    "prefLabel":   {"score": 1.0,  "remarks": "Exact match in title."},
    "description": {"score": 0.85, "remarks": "Slightly paraphrased."},
    "items[3].responseOptions": {"score": 1.0, "remarks": "All four options matched."}
  }
}
```

## Common schemas you'll encounter

| Schema | Use case |
|---|---|
| [ReproSchema](https://www.repronim.org/reproschema/) | Surveys/questionnaires → JSON-LD |
| [Croissant](https://github.com/mlcommons/croissant) | ML dataset cards |
| [schema.org Dataset](https://schema.org/Dataset) | Generic dataset metadata |
| [Bioschemas](https://bioschemas.org/) | Life-science profiles on schema.org |
| [DCAT](https://www.w3.org/TR/vocab-dcat/) | Open-data catalog records |

If the user names one of these, treat it as the schema and skip Step 1.

## Worked example: questionnaire PDF → ReproSchema

**Source:** a 12-page mood questionnaire PDF.

**Schema-locked fields (extractor must produce):**

```jsonc
{
  "activity": {
    "id": "MFQ-long",
    "prefLabel": "Mood and Feelings Questionnaire — Long Version",
    "description": "33-item self-report measure of depressive symptoms in children…",
    "preamble": "How have you felt in the last two weeks…",
    "citation": "Angold et al., 1987"
  },
  "items": [
    {
      "id": "Q1",
      "question": "I felt miserable or unhappy",
      "prefLabel": "miserable_unhappy",
      "inputType": "radio",
      "valueRequired": true,
      "responseOptions": [
        { "value": 0, "name": "Not true" },
        { "value": 1, "name": "Sometimes" },
        { "value": 2, "name": "True" }
      ],
      "scoring": { "type": "sum", "weights": [0, 1, 2] }
    }
    // … 32 more items
  ],
  "computedScores": [
    { "id": "total_score", "type": "sum_all", "items": ["Q1", "Q2", "..."] }
  ]
}
```

**Pipeline:**

1. **Extractor:** schema-locked prompt with the full JSON Schema inline.
2. **Alignment:** map `inputType` strings → ReproSchema IRIs; map `responseOptions.value` types → xsd types. Preserve original strings as `*_raw`.
3. **Judge:** schema validation + per-field faithfulness check.
4. **Human feedback:** display side-by-side PDF page + extracted JSON; reviewer can edit any field.

## Hard rules

- Schema first, prompt second. Don't let the model invent shape.
- Validate every run. If schema validation fails, repair-then-retry with the validator error.
- Preserve raw values. Never lose the source string — always keep it as `<field>_raw`.
- Source-supported only. The judge should penalize any field whose value isn't derivable from the source text.

