# Pipeline pattern

The whole skill rests on a four-stage agent pattern. Each stage is a single LLM call (or a parallel set of LLM calls if the input was chunked). Stages pass JSON between them — never freeform text.

```
extractor → alignment → judge → humanfeedback (optional)
```

## Stage contract

Each stage has a strict input/output contract. **Treat it as a function signature.**

| Stage | Input | Output |
|---|---|---|
| **Extractor** | `{ "text": <raw text>, "metadata": {paper_title?, doi?, paper_location?} }` | Items keyed by task: `entities[]`, `key_terms[]`, `resources[]`, or your custom schema. Each item has `start`, `end`, `sentence` (source-span fields), plus task-specific fields. |
| **Alignment** | Extractor output (verbatim) | Same structure, with `ontology_id`, `ontology_label`, `ontology`, `concept_mapping_provenance` added to each item. **No fields removed.** |
| **Judge** | Alignment output (verbatim) | Same structure, with `judge_score` (float 0–1) and `remarks` (string) added to each item. **No fields removed.** |
| **Human feedback** | Judge output + `{modification_context, user_feedback_text}` | Same structure, revised per the human's input. |

## Why four stages and not one mega-prompt

Separation lets you:

- **Use different models per stage.** Extraction often needs a strong instruction-following model; judging can use a smaller, faster one. Alignment can use a tool-using model or skip the LLM entirely.
- **Cache and resume.** Each stage's output is saved as JSON. If the judge fails, re-run only the judge.
- **Swap implementations.** Replace LLM alignment with a direct call to a concept-mapping service. Replace LLM judging with rule-based scoring.
- **Parallelize.** Chunked inputs run extractor in parallel; downstream stages can run per-chunk too.

## Chain the stages

In pseudocode:

```python
def pipeline(text, schemas, models, mapping_backend):
    extraction = call_llm(
        model=models["extractor"],
        system=PROMPT_EXTRACTOR,
        user={"text": text},
        response_schema=schemas["extractor"],
    )

    if mapping_backend == "tool":
        alignment = call_mapping_tool_batch(extraction)   # direct, no LLM
        for item in flatten(alignment):
            item["concept_mapping_provenance"] = "tool"
    else:
        alignment = call_llm(
            model=models["alignment"],
            system=PROMPT_ALIGNMENT,
            user={"extracted": extraction},
            tools=[concept_mapping_tool_schema],
            response_schema=schemas["alignment"],
        )

    judgment = call_llm(
        model=models["judge"],
        system=PROMPT_JUDGE,
        user={"aligned": alignment},
        response_schema=schemas["judge"],
    )

    if human_feedback_enabled:
        user_feedback = ask_human(judgment)
        if user_feedback:
            judgment = call_llm(
                model=models["humanfeedback"],
                system=PROMPT_HUMANFEEDBACK,
                user={"judged": judgment, "feedback": user_feedback},
            )

    return judgment
```

## Skip a stage

Sometimes you don't need every stage. Common variants:

| Situation | Drop |
|---|---|
| You trust alignment and don't need scoring | judge |
| You only want raw entities, no ontology mapping | alignment, judge |
| You have no humans in the loop | humanfeedback |
| You want only extraction with ontology hints | judge, humanfeedback |

When you skip a stage, the previous stage's output is the final output (or the input to the next non-skipped stage). Mark the skipped stage's fields with a sentinel:

- Skipped alignment → set `concept_mapping_provenance: "skipped"` on each item.
- Skipped judge → set `judge_score: 1.0`, `remarks: "auto-approved"`, `judge_method: "auto_approved"`.

## Bypass LLM for alignment when you have a tool

Alignment is the most expensive stage when run via an LLM agent loop (because the model calls the tool one item at a time, then narrates). If you have a concept-mapping tool with a batch endpoint, **call it directly** with the full list of extracted terms, skip the LLM entirely, and merge the tool's response into the extraction.

```python
terms = [item["entity"] for item in extraction["entities"]]
mappings = mapping_tool.batch(terms, max_results=1)  # one POST
for item, mapping in zip(extraction["entities"], mappings):
    item.update({
        "ontology_id": mapping["id"],
        "ontology_label": mapping["label"],
        "ontology": mapping["ontology"],
        "concept_mapping_provenance": "tool",
    })
```

This turns hours of LLM time into seconds. Output records `alignment_method: "direct_tool_call"`.

## Run stages in parallel (chunked input)

For long inputs, after chunking:

1. **Extraction** — run the extractor per chunk in parallel (`asyncio.gather`, thread pool, etc).
2. **Merge** — concatenate items across chunks. Deduplicate by `(entity_text, start, end, paper_location)` or your stable key.
3. **Alignment / judge / humanfeedback** — run in parallel batches (e.g. 100 items per batch).
4. **Re-merge** — collect batch outputs back into a single result.

See `chunking-strategy.md` for the math.

## Persistence: save each stage's output

Write stage outputs as numbered files so you can resume after a crash:

```
00_extractor.json
01_alignment.json
02_judge.json
03_humanfeedback.json
```

To restart from a later stage, load the saved file as the input and skip earlier stages. The user shouldn't have to re-run a 40-minute extraction because the judge timed out.

## Stage budgets (safety rails)

Without limits, an LLM agent can loop indefinitely on tool calls or bad parses. Set hard caps per stage:

| Limit | Default | Why |
|---|---|---|
| Max reasoning iterations | 5–20 | Stops infinite ReAct loops. |
| Max wall-clock per item | 30–60 s | Stops hanging requests. |
| Max retries on parse error | 1–3 | Retries help; infinite retries hide bugs. |

If a stage exhausts its budget, emit the partial result with `errors: [...]` populated and continue to the next stage. Never silently drop items.

## Provenance map (what every item should carry by the end)

After a full run, every item should look like:

```jsonc
{
  // from extractor
  "entity": "hippocampus",
  "label": "BrainRegion",
  "sentence": "We recorded from CA1 pyramidal cells in the hippocampus.",
  "start": 32,
  "end": 43,
  "paper_location": "page 3, paragraph 2",
  "paper_title": "...",
  "doi": "10.1234/...",

  // from alignment
  "ontology_id": "http://purl.obolibrary.org/obo/UBERON_0002421",
  "ontology_label": "hippocampal formation",
  "ontology": "UBERON",
  "concept_mapping_provenance": "tool",   // or "llm_knowledge" or "skipped"
  "alignment_method": "direct_tool_call",  // or "llm_agent" or "skipped"

  // from judge
  "judge_score": 0.92,
  "remarks": "Confident match; consistent with surrounding context.",
  "judge_method": "llm"                    // or "auto_approved"
}
```

This is the contract every downstream consumer should be able to rely on.

