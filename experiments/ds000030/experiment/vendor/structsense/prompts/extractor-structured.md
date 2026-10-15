# Extractor prompt — schema-driven structured extraction

Use this prompt template when the user has a target JSON schema and wants a document mapped into it (e.g. PDF → ReproSchema, paper → Croissant dataset card, form → custom schema).

## System

```
You extract structured metadata from a source document and emit a JSON
document that MUST validate against the JSON Schema below.

OUTPUT
- Strict JSON. No prose. No markdown fences. No comments.
- The JSON MUST validate against the provided JSON Schema.
- For every required field that is not present in the source, set its value
  to null. Do NOT invent values.
- Preserve original strings; never reword without need.

JSON SCHEMA (the contract):
{json_schema}

FIELD HINTS
{field_hints}

RULES
1. Output exactly one top-level JSON object matching the root schema.
2. Enum fields MUST use one of the listed enum values verbatim.
3. Date fields use ISO 8601: "YYYY-MM-DD" or "YYYY-MM-DDTHH:MM:SSZ".
4. URLs must appear literally in the source or be null.
5. If a list field has no items in the source, return [] (not null).
6. If a string field is not present in the source, return null.
7. Preserve the original phrasing as <field>_raw alongside any normalized
   value where the schema allows it.

If you cannot comply, output {"error": "<one-line reason>"}.
```

## User

```
SOURCE DOCUMENT:
<<<
{input_text}
>>>

ADDITIONAL CONTEXT (optional metadata, hints, page references):
{metadata_json}
```

## How to fill the placeholders

- `{json_schema}`: paste the entire JSON Schema document. Yes, the whole thing. Models do better with the explicit contract than with a paraphrase.
- `{field_hints}`: a short per-field note where it helps. Example:
  ```
  - activity.id: short identifier built from title initials, ignoring stopwords ("and", "the").
                 e.g. "Mood and Feelings Questionnaire" → "MFQ".
  - items[].inputType: one of [radio | text | number | slider].
  - items[].responseOptions[].value: integer score; lowest first.
  ```

## Repair prompt (used after schema-validation failure)

```
The JSON below is INVALID for the schema. Fix it. Output ONLY the
corrected JSON — no prose, no markdown fences.

SCHEMA:
{json_schema}

ERROR:
{validator_error}  (path: {validator_path})

INVALID JSON:
{invalid_json}
```

Cap repair attempts at 2. If still invalid, return the closest-valid output plus `errors[]` populated with the validator errors.

## Common failure modes

| Symptom | Fix |
|---|---|
| Model omits required fields | Add: "Every required field is mandatory. Use null only if explicitly allowed." |
| Numeric fields emitted as strings (`"3"`) | Add explicit type hint in `{field_hints}`. Validate types. |
| Enum mis-spelt (e.g. `"Radio"` not `"radio"`) | Hard-reject in parser; reprompt with the enum list. |
| Hallucinated URLs / citations | Add: "Do NOT include URLs that don't appear literally in the source." |
| List flattened to a comma-separated string | Add: "List fields are JSON arrays, never comma-separated strings." |

