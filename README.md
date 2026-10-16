# Connecting neuroimaging knowledge graphs across data, publications and labs

Materials for a 25-minute talk at the ReproNim LLM symposium (Satrajit Ghosh), built as a
reproducible, provenance-tracked presentation: every number on a slide is read from a result
file in this repository, every build step is recorded with `datalad run`, and every slide
carries a badge saying how it was produced and how it was checked.

## Learning objectives

By the end of the talk you should be able to:

1. **Represent a neuroimaging result as a knowledge graph**, linking the research question, the
   claim and its scope, the participants and derived measures it relies on, and the source data.
2. **Connect information across knowledge graphs**, joining your data with public datasets,
   publications, tools and collaborators' work through shared identifiers and vocabularies, and
   deciding what can leave your lab.

## What is here

| Path | Contents |
|---|---|
| `slides/` | Deck sources (`build_deck.js`, `values.js`, `values_map.json`, `apply_theme.js`), slide-size figures (`figs_slide/`), the built `.pptx` (PDF: see below), the talk plan, and `talk_provenance.ttl` (W3C PROV record of every slide) |
| `experiments/abide/` | ABIDE I worked example: two simulated analysts (group difference, leave-site-out prediction), a QC revision traced through the graph, NIDM/PROV graph conformed to the PyNIDM v4.5.5 LinkML schema, joins to ReproNim simple2 NIDM, AbstractAtlas and OpenAlex, a SynthScholar literature review of 74 ABIDE studies, competency questions with gold answers, and a Brain Researcher (MCP) comparison. See its `README.txt` |
| `experiments/ds000030/` | ds000030 (UCLA CNP) worked example produced in an earlier agentic session, plus `codex_verification/`: an independent claim check (39 confirmed, 0 contradicted) and an ORCD rebuild comparison |
| `scripts/` | `build_all.sh` (all steps under `datalad run`), `check_slide_values.py`, `check_pdf_text.py`, `parse_all_ttl.py`, `refresh_checksums.py`, `strip_fulltext.py`, `sync_from_workspace.sh` + `port_build_deck.py` (bring in a workspace deck), `export_pdf.sh` |
| `provenance/` | Outputs of the recorded check steps |

The two packaged experiments are also attached to the
[v0.1 release](https://github.com/ReproNim/llm-workshop-kg/releases/tag/v0.1) as zip files. Compared with
the packages as first built, article full text was removed from the literature review
(`scripts/strip_fulltext.py`), local absolute paths were replaced with relative ones, and
`experiments/abide/SHA256SUMS` was refreshed for the changed files.

## Rebuild

Requirements: [uv](https://docs.astral.sh/uv/), Node.js 22, and for recorded runs
[DataLad](https://www.datalad.org/) with git-annex (`uv tool install datalad`; `brew install git-annex`).

```bash
git clone https://github.com/ReproNim/llm-workshop-kg && cd llm-workshop-kg
scripts/build_all.sh            # figures, deck, PDF, value check, graph checks — each a datalad run
scripts/build_all.sh deck       # or one step: figures | deck | pdf | values | graphs
datalad rerun <commit>          # replay any recorded step
```

Without DataLad, the same commands run directly:

```bash
uv run slides/figs_slide/make_slide_figs.py
(cd slides && npm ci && node build_deck.js)
uv run scripts/check_slide_values.py
uv run scripts/parse_all_ttl.py
(cd experiments/abide && uv run --frozen python code/validate.py)
```

The full ABIDE analysis (downloads about 2 GB of public time series, about an hour on a laptop)
is `experiments/abide/rebuild.sh`; a clean-room run from a fresh download reproduced 215 of 218
key numbers (the other three are run times) and all 15 gold answers
(`experiments/abide/results/clean_room_verify.json`).

The PDF export is a host step (`scripts/build_all.sh pdf`, then `scripts/build_all.sh pdftext`, where `scripts/check_pdf_text.py` confirms the PDF carries the deck's text slide by slide). For v0.2 no PDF matching the final deck could be exported (PowerPoint automation failed with error -9074), so the release carries the `.pptx` and the PDF will be added once exported: it uses LibreOffice where installed, otherwise Microsoft PowerPoint
on macOS through `scripts/export_pdf.applescript`.

## How provenance is recorded

- **Numbers.** `slides/values_map.json` lists every experiment number shown on a slide with its
  source file and JSON path; `build_deck.js` reads them through `values.js`, and
  `scripts/check_slide_values.py` recomputes each one and fails if the slide disagrees.
- **Build steps.** `datalad run` records the command, inputs, outputs and resulting commit for
  each step (`git log` shows them as `[DATALAD RUNCMD]` commits).
- **Slides.** `slides/talk_provenance.ttl` describes each slide as a `prov:Entity`, how it was
  produced, the files it was derived from, and who or what checked it, with links to the
  evidence (rebuild comparisons, claim verification).
- **Graphs.** Each experiment ships SHACL shapes with mutation tests (removing a derivation
  edge must make validation fail); CI runs them on every push.

### AI-involvement badges

Each slide's bottom-left badge combines production letters and a checking status.

| Letter | Production |
|---|---|
| H | written or decided by the speaker |
| L | drafted by an LLM from the speaker's instructions, then edited by the speaker |
| A | computed by an agent writing and running code (Python, SPARQL, Slurm on ORCD) |
| R | retrieved by an agent from cited sources; quotes checked against the source |
| M | answered by an external agent system through MCP (Brain Researcher) |
| P | produced in an earlier session by a different agentic system, reused |

| Status | Meaning |
|---|---|
| re-run | recomputed independently (for example a clean rebuild matched) |
| validated | passed automated checks (SHACL, schema, tests, render checks) |
| reviewed | read and corrected by the speaker |
| unverified | not independently checked; stated as such |

## Verification status (v0.1)

- ds000030 package rebuilt on MIT ORCD: all 24 deterministic checks matched; UMAP values differed
  by at most 0.011 with the same seeds (`experiments/ds000030/codex_verification/orcd_rebuild/`).
- ds000030 retrieved claims: 39 confirmed against primary sources, 0 contradicted, 1 not found verbatim.
- ABIDE clean-room rebuild: 2,108/2,108 input hashes, 215/218 key numbers, 15/15 gold answers.
- Literature review: 1,735 of 1,743 quotes verified against source text (the 8 dropped were
  empty); charting was done by AI agents and individual decisions were not checked by a human.
- ABIDE run on ORCD (Slurm job 25939932) compared with the local run: `experiments/abide/results/orcd_vs_local.json`.

## Related

- Skill for building such a graph: `neuroimaging-kg` in sensein/agent_skills,
  [pull request #49](https://github.com/sensein/agent_skills/pull/49) (branch `neuroimaging-kg`).
  The live-demo slides use its tested Claude Code demo: steps in `slides/demo/claude_code_demo.md`,
  the headless test run in `slides/demo/claude_code_demo_transcript.md` (copied from commit 2bf966c;
  see `slides/demo/SOURCE.md`). `scripts/check_slide_values.py` checks every quoted demo output
  against that transcript.
- [AbstractAtlas](https://abstractatlas.brainkb.org) — OHBM 2026 abstracts and their extracted claims.
- ReproNim: [ReproPond and ReproLake](https://www.repronim.org/resources/tutorials/pond-lake/),
  [simple2_NIDM_examples](https://github.com/ReproNim/simple2_NIDM_examples), [PyNIDM](https://github.com/INCF-NIDASH/PyNIDM).

## Licences

Code: Apache-2.0 (`LICENSE`). Slides and text: CC BY 4.0 (`LICENSE-content`). Data-derived files
keep their source terms — ds000030 is CC0; ABIDE-derived participant-level files are
CC BY-NC-SA for non-commercial research — see `DATA_LICENSES.md`. Article full text is not
redistributed.
