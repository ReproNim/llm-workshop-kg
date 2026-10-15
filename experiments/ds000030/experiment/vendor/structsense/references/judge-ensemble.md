# Judge ensemble — weak learners + one combiner

Replaces the single-judge stage with a **panel of narrow judges** and a
**combiner**. The principle is the weak-learner one: each judge evaluates ONE
dimension it can be nearly perfect at, judges never see each other's output
(decorrelated errors), and a final stage aggregates verdicts and applies
fixes. A monolithic "score this item 0–1" judge mixes orthogonal failure
modes and hides which one fired; the panel makes every rejection attributable
and every fix traceable to a specific reviewer.

```
                   judge_prepare.py (no LLM)
 aligned result ──► ├─ grounding_script review   (deterministic: does the surface exist?)
 (+ kg_plan.json)   └─ one packet per judge      (only the fields that judge needs)
                              │
          ┌─ judge: grounding ─┤  (only items the script could not pass)
          ├─ judge: labeling  ─┤
          ├─ judge: mapping   ─┤  run INDEPENDENTLY — one judge at a time
          ├─ judge: kg-keys   ─┤  (kg_plan only)
          └─ judge: claims    ─┘  (kg_plan only)
                              │  reviews/<judge>-NNN.json
                              ▼
                   judge_combine.py (no LLM) ──► needs_review? ──► judge-combiner.md ──► --apply-fixes
                   gates, demotions, mechanical fixes, scores        (chooses among judges' suggestions)
                              │
                              ▼
                   json_to_ttl.py: every review becomes a ner:ReviewDecision in the TTL
```

## The panel (default; configure in judges_config.json)

| judge | dimension — the ONLY thing it may fail an item for | critical | typical fix |
|---|---|---|---|
| **grounding_script** | deterministic (`judge_prepare.py`): `pass` when every mention's offsets select its surface; `fail` when the surface occurs nowhere in the source; `flag` otherwise. No model. | yes | none — a fail is a drop |
| **grounding** | the items the script flagged: is the entity really in the text as claimed (not only inside a longer word, not only in a figure reference)? | yes | none — a grounding fail is a drop |
| **labeling** | entity-type label is right for the referent (`CellType` vs `Protein` vs `Chemical`…) | no | `suggestion.label` |
| **mapping** | the ontology mapping *means the same thing*: entity ↔ `ontology_label` semantic identity, and (KG mode) the skos tier honestly states the strength. This is the check `--check-ols` cannot do — existence ≠ meaning. | no | `suggestion.tier`, or fail → demote to unmapped |
| **kg-keys** (kg_plan only) | `normalized_key` follows references/key-normalization.md: guardrails (no `model`, `imaging`, bare `neuron`), coreferent groups share a key, distinct referents don't | no | `suggestion.normalized_key` |
| **claims** (extraction + kg_plan) | relations and causal entries are stated by THIS paper (no world-knowledge edges); `hypothetical` is `false` only for interventional evidence; chain order matches the paper's argument | yes | `suggestion.hypothetical`, or fail → drop the edge/relation |

Weak-learner properties to preserve when extending the panel:

1. **One dimension per judge.** If a prompt needs the word "also", split it.
   Anything a script can decide is a script judge (`grounding_script`), not a
   prompt.
2. **Independence.** Judges never read another judge's review. In framework
   mode that's parallel calls (different models encouraged — diversity
   decorrelates further; each judge can be a small cheap model). In
   host-model mode, emulate it: run each judge prompt as a **separate pass
   over the items**, completing one judge's full review before starting the
   next, never as one mega-pass — and be honest in the output that
   independence is procedural, not process-level (`"mode": "host_sequential"`
   in each review file).
3. **Judges never fix.** Verdict + confidence + one-line reason +
   machine-usable `suggestion` at most. Fixing is the combiner's monopoly;
   a judge that rewrites items is a second extractor, and its errors stop
   being weak.

## Running it

```bash
# 1. packets + the deterministic grounding review (no LLM)
python -m scripts.judge_prepare work/<stem>_final.json --source work/<stem>.txt \
    [--kg-plan work/kg_plan.json] --out-dir work/judge

# 2. each judge, one at a time: read judge/packets/<judge>/part-NNN.json, follow
#    its `prompt`, write its `review_file` (judge/reviews/<judge>-NNN.json)

# 3. aggregate (no LLM) — writes back into the result and the kg_plan
python -m scripts.judge_combine work/<stem>_final.json --reviews work/judge/reviews/*.json \
    [--kg-plan work/kg_plan.json]

# 4. only if it printed needs_review > 0: prompts/judge-combiner.md, then
python -m scripts.judge_combine work/<stem>_final.json --apply-fixes work/judge/combiner.json
```

In framework mode `pipeline.py --judge <model>` does all four steps itself, with
`--judge-models mapping=<model>,claims=<model>` to give panel members different
models (diversity decorrelates further) and `--combiner <model>` for step 4.

## Review format (one file per judge part; schemas/judge-review.schema.json)

```json
{
  "judge": "mapping",
  "model": "llm:<model-id>",
  "mode": "host_sequential",
  "items": [
    {"id": "prefrontal cortex|BrainRegion", "verdict": "pass", "confidence": 0.95, "reason": "UBERON:0000451 label identical"},
    {"id": "IT cortex|BrainRegion", "verdict": "flag", "confidence": 0.7,
     "reason": "UBERON term is inferior temporal GYRUS — near, not identical",
     "suggestion": {"tier": "closeMatch"}}
  ]
}
```

`id` is `"<entity>|<label>"` exactly as in the grouped output (`"<term>|KeyTerm"`
for an unlabeled key term) — the same join key kg_plan.json and json_to_ttl use.
Claim reviews use the causal-relation or chain `id` (`rel-1`, `chain-1`) or
`"<src_key>--<predicate>--<tgt_key>"` for RO edges (`<src>--broader--<tgt>` for
skos:broader). Verdicts: `pass`, `flag` (usable but imperfect), `fail`.
Confidence is the judge's own 0–1. A judge's review may be split into parts; the
combiner merges them and rejects an id reviewed twice by one judge.

## Aggregation semantics (`scripts/judge_combine.py`, deterministic)

Per item, in order:

1. **Critical gate**: any `fail` from a critical judge (grounding_script,
   grounding, claims) → the item is dropped (or the claim/edge/chain pruned).
   No vote can save it — hallucinations don't get averaged away.
2. **Mapping fail** → demote to unmapped (ontology fields nulled,
   `concept_mapping_provenance: "unmapped"`, `alignment_method: "judge_demoted"`)
   — the item survives, the IRI doesn't. Rule 15: an IRI needs positive
   verification at every stage.
3. **Mapping tier**: mapping `pass` → `mapping_tier: "exactMatch"`; `flag` with a
   tier suggestion → that tier. Unjudged mappings are written as closeMatch.
4. **Mechanical suggestions** (label, normalized_key, hypothetical/negated) with
   no dissenting non-critical fail → applied by the script, logged in
   `fixes_applied`.
5. **Unresolved** (a fail with no usable suggestion, or a suggestion contested
   by another judge's fail) → `needs_review`, for the combiner.
6. **Score**: `judge_score = Σ w_j · conf_j · s(v_j) / Σ w_j` over the judges
   that reviewed the item, `s(pass)=1, flag=0.5, fail=0`, weights from
   `judges_config.json`.

All of it is applied to the **raw mentions** (`entities[]` / `key_terms[]`), the
authoritative record; the grouped views and `stats` are rebuilt from them, so a
later `normalize_result` run cannot resurrect a dropped item. Each mention gets
`judge_score`, `judge_method: "ensemble"` and a one-line `remarks`; the full
reviews live once, in the top-level `judge_ensemble` block (reviews by id,
models, the report), and become `ner:ReviewDecision` nodes attributed to each
judge in the TTL.

## The combiner (prompts/judge-combiner.md)

Runs once, on the strongest model in the stack, and is deliberately boring:
it may ONLY act on `needs_review` entries and unresolved suggestions. It may
not add entities, mappings, relations, or keys that no judge proposed; where
judges genuinely conflict and the text doesn't settle it, it escalates to the
human-feedback stage rather than deciding. Output: a `fixes_applied` log where
every fix cites the judge review that licensed it; `--apply-fixes` rejects any
fix whose value no judge suggested, and records escalations under
`judge_ensemble.combiner.escalated` for prompts/humanfeedback.md.

## In the TTL

Nothing the ensemble does is lost in the representation (references/ttl-representation.md
→ *Judging as provenance*): one `ner:AutomaticValidationActivity` per judge with its
model version, mode and prompt hash; one `ner:ReviewDecision` per verdict; the
combine step and the combiner as their own activities; a `ner:ChangeRecord` for every
relabel, tier change, key rename, demotion and drop — a dropped hallucination survives
only as its change record, with the surface, offsets and the review that removed it.
`judge_combine.py` records what this needs (`judge_ensemble.judges[*].prompt_sha256`,
`mode`, `model`, `combined_at`; `report.demoted[*].from`; the reviews of dropped
items); pass `--combiner-model` to `--apply-fixes` so the combiner step names its model.

## Why this beats one judge — the honest version

- attribution: "dropped by grounding, conf 0.98" is actionable; "score 0.4"
  is not;
- decorrelation: five narrow prompts (ideally five models) don't share one
  model's blind spots; the ensemble catches what any single judge misses;
- asymmetric costs are encoded structurally: hallucination is a gate, not a
  weight, because one poisoned IRI or fabricated edge costs more than ten
  false rejections;
- cost: weak judges run fine on small cheap models (framework mode) — the
  expensive model is spent once, in the combiner.

Limitation to state plainly: in host-model mode all judges share one model's
priors, so the ensemble decorrelates prompts, not models. It still buys
attribution and the critical-gate semantics; full decorrelation needs
framework mode with distinct `--judge` models per panel member.

