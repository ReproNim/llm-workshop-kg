# Source of the demo files

## Live demo (`neuroimaging-kg` skill)

Copied unchanged from sensein/agent_skills:

- Pull request: https://github.com/sensein/agent_skills/pull/49 (branch `neuroimaging-kg`)
- Commit: `4f7409a` ("compare and harmonise contributors' graphs"; adds `scripts/compare_graphs.py`).
  `claude_code_demo.md` and `claude_code_demo_transcript.md` are unchanged from the earlier copy at `2bf966c`.
- Files:
  - `skills/neuroimaging-kg/examples/claude_code_demo.md` — steps and prompts
  - `skills/neuroimaging-kg/examples/claude_code_demo_transcript.md` — headless test run (Claude Sonnet, 2026-10-15)
  - `skills/neuroimaging-kg/examples/abide_one_site/demo_output.txt` → `abide_one_site_demo_output.txt` — end-to-end
    run on ABIDE I Caltech, including step 10, the `compare_graphs.py` comparison with ReproNim's simple2 graph
  - `skills/neuroimaging-kg/examples/abide_one_site/README.md` → `abide_one_site_README.md`

## "Asking Claude about the literature graph"

`literature_query_answer.md` is the answer from a headless Claude Code run (2026-10-15) in a fresh folder
that contained only the review's graph, `literature_kg.ttl`. That file is byte-identical to
`experiments/abide/literature_review/literature_kg.ttl` (sha256 1e54c8b0c7c51465…). The run wrote
nothing to stderr. The answer file here is identical to the one the run produced
(sha256 b752e507b7f19f5b…).

The slide's run time ("88 s") is not recorded in any file of that run: the folder shows only an
empty `err.txt` created at 18:44 and `answer.md` written at 18:46. It is the coordinating agent's
timing and is not machine-checked.

## Checks

`scripts/check_slide_values.py` checks that every quoted demo output and every harmonisation and
literature-query number on these slides appears verbatim in the file it came from and on the slide.
