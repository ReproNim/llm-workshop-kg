# Demo: a knowledge graph for one ABIDE I site

This demo builds, checks and queries a small knowledge graph for one site of **ABIDE I** (Autism Brain
Imaging Data Exchange: resting-state fMRI and phenotypes from 17 international sites, 1,112
participants; "ABIDE Preprocessed" is the same data processed by the Preprocessed Connectomes
Project). It uses only pinned public files and finishes in about 15 seconds after the first download
(the first run also downloads PyNIDM and LinkML, about a minute).

```bash
mkdir abide-demo && cd abide-demo
bash /path/to/agent_skills/skills/neuroimaging-kg/examples/abide_one_site/run_demo.sh Caltech
# also pinned: SBL, OHSU, Stanford
```

Requires `uv` (and `uvx`) and Python ≥ 3.11. Nothing is installed globally.

## What each step does, in plain words

| Step | What happens | Why it matters |
|---|---|---|
| 1 | Download the ABIDE phenotype table, ReproNim's term map and its NIDM file for the site, the three tools' measure definitions, and PyNIDM's schema; refuse any file whose SHA-256 (a fingerprint of its bytes) differs from the pin | the graph is built from exactly the files named, every time |
| 2 | Keep the site's rows and the 75 columns that have shared definitions | scope the work to what can be linked |
| 3 | Convert the rows to **NIDM** (Neuroimaging Data Model: a shared vocabulary for participants, measurements and derivatives) with PyNIDM `csv2nidm` | variables become shared concepts, e.g. FIQ → "full intelligence quotient" in InterLex (a registry of neuroscience terms) |
| 4 | Link our participants to ReproNim's NIDM participants by ID, and compare age, sex and diagnosis between the two | a shared ID is evidence, not proof; disagreements are listed for review |
| 5 | Define a head-motion cohort: **mean FD** (mean framewise displacement: average head movement between fMRI volumes, in mm) below 0.2 mm | an analysis decision, recorded with its rule, input file (by fingerprint), software version and who made it |
| 6 | Record the dataset's consent scope (ABIDE I is a public, de-identified release: broad sharing) and one published claim with its scope and a verbatim quote | claims stay tied to the population and evaluation they were made on |
| 7 | Check the graph with **SHACL** (machine-checkable rules, e.g. "every derived result names its inputs"), then delete those links on purpose and confirm the check fails; check PyNIDM's output against PyNIDM's own schema | shows the checks can catch a real omission |
| 8 | Compute the expected answers straight from the source files | the graph is tested against the data, not against itself |
| 10 | Compare our graph with ReproNim's as two separate contributors: which participants, datasets and papers both have; which variables share a concept and which only *look* alike (proposed mappings for review); which values disagree | how graphs from different people are harmonised without overwriting either |
| 9 | Load every layer into **Oxigraph** (a database that answers **SPARQL**, the query language for graphs) as separate named graphs and answer six questions | each question is a `.rq` file in `queries/` |

## The questions and what the Caltech answers mean

| Question | Caltech answer | In plain words |
|---|---|---|
| Q1 participants in our table, and linked to ReproNim's NIDM | 38 and 38 | every Caltech participant was found in ReproNim's file; age, sex and diagnosis agree for all 38 |
| Q2 participants with mean FD < 0.2 mm, by group (1 = autism, 2 = control) | 19 and 19 | every Caltech participant moved less than 0.2 mm on average (largest mean FD 0.186 mm) |
| Q3 participants with both FIQ (full-scale IQ) and a FreeSurfer hippocampal volume, by group | 18 and 19 | one autistic participant has no FIQ recorded |
| Q4 what produced the cohort | step, software and version, parameter 0.2, input file and its fingerprint | the cohort can be re-derived and checked |
| Q5 published claims that use ABIDE I | Abraham et al. 2017: predictive, 871 participants, accuracy 0.67, with the quote | the claim carries its population and evaluation |
| Q6 left-hippocampus volume for one participant, by tool | FSL 3,766 mm³; FreeSurfer 4,513.9 mm³ | same person, same structure, ~20% apart: different tools measure differently (no ANTs output exists for Caltech) |

Step 10 on Caltech: all 38 participants match; 12 concepts are shared; 28 variables (e.g. the ADOS and
SRS subscores) have no shared concept in one of the files but the same source variable in both, so they
are listed as proposed matches for a person to review; 282 participant-by-concept values were compared
and none disagree (both graphs come from the same ABIDE table). Results: `graph/compare.md`,
`graph/mapping_review.ttl` (proposals only), `graph/contributors.ttl` (who contributed which graph).

Q1–Q5 are compared with gold answers and print `PASS`; Q6 is descriptive. The full output of a run is
in `demo_output.txt`.

## Files written

`graph/phenotype.ttl` (NIDM from csv2nidm), `graph/identity_links.ttl`, `graph/cohort.ttl`,
`graph/dataset_claims.ttl`, `graph/provenance.ttl`, `graph/join_report.json`,
`graph/validation_*.json`, `graph/gold.json`, `graph/answers.json`, `graph/compare.{json,md}`,
`graph/mapping_review.ttl`, `graph/contributors.ttl`.
