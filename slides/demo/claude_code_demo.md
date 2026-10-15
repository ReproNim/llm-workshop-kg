# Live demo in a Claude Code terminal (about 10 minutes)

This walks through building and questioning a knowledge graph for one site of **ABIDE I** (Autism
Brain Imaging Data Exchange: resting-state fMRI and phenotypes from 17 international sites) by
talking to Claude Code with the `neuroimaging-kg` skill installed. Everything runs on your laptop from
pinned public files. The prompts and expected outputs below were tested headlessly; the transcript is
in `claude_code_demo_transcript.md`.

Terms used: a **knowledge graph** is a set of statements (subject → relation → object) that share
identifiers. **NIDM** (Neuroimaging Data Model) is a shared vocabulary for participants, measurements
and derivatives; **PROV** records which step produced what, from what, by whom. **SPARQL** is the
query language for graphs; **Oxigraph** is a database that answers it. **FIQ** is full-scale IQ;
**mean FD** (mean framewise displacement) is average head movement between fMRI volumes, in mm.

## 0. Set up (once, ~2 minutes)

Requires `git`, `uv` and Claude Code (`claude`) on your PATH.

```bash
git clone https://github.com/sensein/agent_skills.git
cd agent_skills && git checkout neuroimaging-kg && cd ..
mkdir abide-kg-demo && cd abide-kg-demo
# project scope: installs into ./.claude/skills only, nothing in your home directory changes
python ../agent_skills/scripts/install_skills.py --agent claude --scope project --skills neuroimaging-kg
claude
```

## 1–4. Prompts to type

Type each prompt in the same Claude Code session, in order. Durations are from the headless test
(Claude Sonnet, Apple-silicon laptop, inputs not yet cached); expect similar times live.

### Prompt 1 — build the graph (~35 s; ~1 min more on the very first run while PyNIDM and LinkML download)

```text
Use the neuroimaging-kg skill to build a knowledge graph for ABIDE I site Caltech — the phenotype table plus ReproNim's NIDM file with brain volumes — validate it, and load it into Oxigraph. Tell me in plain words what is in the graph.
```

Expect: 38 Caltech participants (19 autistic, 19 control) converted to NIDM, each variable tied to a
shared concept (e.g. FIQ → "full intelligence quotient"); all 38 linked one-to-one to ReproNim's file
with age, sex and diagnosis agreeing; a head-motion cohort (everyone at Caltech has mean FD below 0.2
mm) recorded with its rule and input fingerprint; one published claim (Abraham et al. 2017, 67%
accuracy on 871 ABIDE participants) with a verbatim quote; checks pass, and a deliberately deleted
"derived from" link is caught. *Point to make:* the graph says how each number was produced.
*Known slip in testing:* the agent said volumes came from three tools; Caltech's file has FreeSurfer
and FSL only (no ANTs) — a good moment to ask "how would we check that?" (prompt 3 does).

### Prompt 2 — a cross-graph question (~15 s)

```text
How many Caltech participants have both a full-scale IQ (FIQ) score and a FreeSurfer hippocampal volume, by diagnostic group? Show the SPARQL query you used and explain it briefly.
```

Expect: **18 autistic, 19 control** (one autistic participant has no FIQ recorded), with the query.
*Point to make:* FIQ comes from our table, the volume from ReproNim's file; they meet only through
the shared participant ID, and "hippocampal volume" must be picked by its unit (mm³) because the same
anatomy term also labels voxel counts.

### Prompt 3 — provenance (~2.5 min)

```text
Trace participant 51456's left-hippocampus volume from FreeSurfer back to the scan and the software it came from. Say which links are recorded in the graph and which are only inferred.
```

Expect: participant → FreeSurfer run → stats entity holding `fs_003343 = 4513.9` (left hippocampus,
mm³, defined in the FreeSurfer term file); the T1-weighted scan (Siemens 3 T MPRAGE, TR 1.59 s, with an
S3 location and SHA-512 checksum) is recorded separately. **Not recorded:** an edge saying FreeSurfer
ran on that scan — it is only implied by the subject ID appearing in the command line — and the
FreeSurfer version (6.0.0) appears only in a path string. *Point to make:* a graph shows where
provenance is missing, not only where it exists.

### Prompt 4 — what changes if a rule changes (~1 min)

```text
If we tightened the head-motion rule to mean framewise displacement below 0.15 mm, which participants would be excluded, and which results in our graph depend on them?
```

Expect: **51456** (mean FD 0.186 mm) and **51469** (0.156 mm), both autistic → cohort 17 autistic /
19 control. Results that depend on the cohort update (cohort counts, the recorded rule); the agent also
notices that two queries ignore cohort membership (the FIQ+volume count and the per-tool example,
which happens to use 51456). *Point to make:* dependency tracing turns "re-run everything" into a
list of what to re-check — and exposes questions that were never tied to the cohort.

## After the demo

Everything is in the demo directory: `graph/` holds the Turtle files and reports, `data/` the pinned
inputs. A tested transcript of these four prompts is in `claude_code_demo_transcript.md`; the
non-interactive version of the same build is `abide_one_site/run_demo.sh`.

Headless re-test: `bash test_claude_code_demo.sh <empty dir outside ~/.claude> [model]`. (Claude Code
refuses headless writes under `~/.claude`, so pick a directory elsewhere.)
