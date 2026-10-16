# Talk plan — 25 min, neuroimaging audience, interactive

Audience: neuroimagers, not AI specialists. Aim: clear, no overclaiming about what the AI knows,
leave with practices usable this week. Background experiments (CNP/ds000030 and ABIDE I packages)
are evidence for the slides, not the subject of the talk; details live in backup and the zips.

## Learning objectives (slide 2) — revised: focus on connecting graphs (audience has heard much about skills)

Title: **Connecting neuroimaging knowledge graphs across data, publications and labs** (no AI in the title — speaker choice; "checkable" judged unclear)

By the end of this talk, you should be able to:

1. **Represent a neuroimaging result as a knowledge graph**, linking the research question, the claim
   and its scope, the participants and derived measures it relies on, and the source data.
2. **Connect information across knowledge graphs**, joining your data with public datasets,
   publications, tools and collaborators' work through shared identifiers and vocabularies, and
   deciding what can leave your lab.

Consequences for the route: skills become a supporting element (how agent work is checked), not an
objective. New main slide on join keys across graphs (participant IDs / ndar:src_subject_id, NIDM concept
IRIs via nidm:isAbout, DOIs, RRIDs / repository URLs, ORCIDs) with measured match rates. Practices:
"Use shared identifiers and terms" replaces "Give agents tests".

## Main route (16 slides, ~23 min + discussion)

| # | Slide | Time | Interactive | Evidence source |
|---|-------|------|-------------|-----------------|
| 1 | Title | 0:30 | | |
| 2 | Two learning objectives | 0:45 | | |
| 3 | "How many subjects are in ds000030?" 290 / 272 / 261 / 259 / 255 / 94 | 2:00 | **Poll** (hands / show of fingers) | CNP package |
| 4 | What the assistant does and does not know (reads what you give it; cannot see your cohort; can quote correctly and still be wrong) — graph = memory you control, skill = written procedure, harness = checks that run | 1:30 | | |
| 4b | What a neuroimaging knowledge graph can hold — comprehensive typology grid (below); tiles executed in our packages highlighted | 1:30 | **"Which of these does your lab already write down?"** | |
| 5 | One measurement with its source (sub-10159 Barratt: person → acquisition → row → value) | 1:15 | | CNP graph |
| 6 | Recompute one derivative: 272/272 Barratt scores match | 1:00 | | CNP |
| 7 | A claim needs its evaluation and cohort (Kim 2023 70.2% chain, missing manifest) | 1:30 | | CNP |
| 8 | Spot the unsupported claim: valid quote → "70.2% proves a causal mechanism" | 1:30 | **Spot the error** | CNP skill pilot |
| 9 | Two collaborators, one dataset, two questions (ABIDE I: A = group difference, B = leave-site-out prediction) | 1:30 | | ABIDE package |
| 10 | What each found (A effect summary; B AUC vs demographic baseline per site) | 1:30 | | ABIDE |
| 11 | A tightens motion QC — predict how many of B's test participants are affected; then graph traversal + actual recompute | 2:00 | **Predict, then reveal** | ABIDE |
| 12 | Phenotype UMAP joined to image-derived measures; site structure first | 1:15 | | ABIDE |
| 13 | Validate the skill ≠ validate the output (fault-injection results) | 1:30 | | CNP |
| 14 | Graph vs search (vs Brain Researcher, if run) — n=1, honest | 1:30 | | comparison |
| 15 | Five things to do this week | 2:00 | | |
| 16 | Close: "Which link would your lab require before accepting an agent's next action?" + links to packages | 1:00 | **Discussion** | |

## Five things to do this week (slide 15 draft)

1. Pin the data you analyse (DataLad / commit + hashes) and record it next to every result.
2. Save the participant manifest for every analysis, including the exclusions and the rule that made them.
3. For each claim, write its scope: population, measure, contrast, evaluation (association ≠ prediction).
4. Recompute one derived value from source before trusting a derivative table.
5. When you hand a step to an agent: write the procedure as a skill, give it acceptance tests, and let checks — not the agent — decide what is accepted.

## Backup

Current deck slides 3–45 (NIDM mapping table, scan metadata, events, registration, StructSense
details, AbstractAtlas, sensein/K-Dense skills and PRs, Brain Researcher benchmark, workshop links).

## Kinds of neuroimaging knowledge in a graph (slide 4b; full table in backup)

| Group | Kind | Standards / examples |
|---|---|---|
| What was studied | Datasets and versions | BIDS, DataLad, OpenNeuro/DANDI/NDA accessions, DCAT |
| | Participants, phenotypes, assessments | NIDM-Experiment, ReproSchema, NIH CDEs, NDA data dictionary |
| | Acquisitions and protocols | BIDS sidecars, ReproIn, scanner/sequence parameters, ReproStim |
| | Tasks and cognitive constructs | Cognitive Atlas, CogPO, task events |
| How it was done | Methods, software, pipelines, versions | CodeMeta/schema.org, containers (ReproNim/containers, Neurodocker), Boutiques |
| | Procedures: how to apply a method | Registration routes, compatible spaces, QC criteria, failure modes — skills with acceptance checks |
| | Atlases, templates, coordinate spaces, transforms | TemplateFlow (MNI152NLin2009cAsym, fsaverage), Julich/Allen, transform chains |
| | Computational runs and provenance | W3C PROV, NIDM, DataLad run records, ReproMan, BABS |
| | Compute environments | Container images, HPC profiles, seeds (reproseed) |
| What was found | Derivatives and image-derived phenotypes | BIDS-Derivatives, NIDM (FreeSurfer/ANTs/FSL → NIDM), MRIQC → NIDM |
| | Statistical results and maps | NIDM-Results, NeuroVault, effect sizes with cohort |
| | Questions and hypotheses | Preregistrations, research-question nodes |
| | Claims and findings, with scope | Population, measure, contrast, evaluation; ECO evidence codes; nanopublications |
| Who and in what context | Publications and preprints | DOI, PMID, sections and quotes as evidence locators |
| | People, organisations, roles | ORCID, ROR, CRediT, PROV qualified roles |
| | Projects and funding | NIH RePORTER grant IDs |
| | Reviews, assessments, disagreements | Attributed assessments; who asserted what, on what evidence |
| | Resources and their activity | Dated activity snapshots (commits, issues, citing papers) with age |
| | Ontologies and vocabularies | UBERON, InterLex/NeuroNames, NCIT, EDAM, ECO, SIO, nidm-terms |
| | Governance: consent, data use, licences | DUO, data use agreements, CC0/CC-BY |

## Types of knowledge, and where each lives (slide 6b — practical)

Message: write each kind of knowledge where it can be checked. Graph = records you query;
skill = procedure you follow; harness check = test that runs; human review = judgement you record.

| Kind | Neuroimaging example | Where it lives |
|---|---|---|
| Observations / facts | TR = 2 s for this scan; mean FD = 0.18 mm | Graph, with source |
| Definitions and conventions | SSRT computed by quantile method; RAS+; MNI152NLin2009cAsym | Graph + ontology terms |
| Theories and hypotheses | Dysconnectivity hypothesis of autism | Graph, as question/hypothesis with status |
| Findings / claims | Under-connectivity in ASD, in this cohort, this measure | Graph, scoped, with evidence |
| Methods | What tangent-space connectivity estimates | Graph + docs |
| Know-how (procedures) | How to register BOLD → T1 → template and check it | Skill |
| Best practices / guidelines | COBIDAS; preprocessing inside CV folds | Skill, citing the guideline |
| Heuristics / rules of thumb | Exclude mean FD > 0.2 mm | Skill parameter, with its derivation and limits |
| Failure modes / pitfalls | Left–right flips; leakage across folds; site confounds; double dipping | Harness check / test |
| Acceptance criteria | Recomputed score matches; derivative has a source edge | Harness check (SHACL, tests) |
| Tacit judgement | Visual QC of a registration | Human review, recorded as an attributed assessment |
| Local / lab knowledge | Scanner B's phase-encoding quirk; lab naming conventions | Graph + skill, scoped to site |
| Disagreement and uncertainty | Two reviewers disagree on QC | Graph, as separate attributed assessments |
| Currency (how fresh) | Tool last released 3 weeks ago | Graph, dated snapshot with age |

## Local and global knowledge, and transitions between them (main slide after "Types of knowledge")

Scope levels: individual analyst → lab → institution / site → consortium → global (community registries,
ontologies, literature-derived KGs such as BR-KG, AbstractAtlas).

| Local (lab / site) | Global (community) |
|---|---|
| Scanner B phase-encoding quirk; site motion profile | BIDS spec, scanner-independent conventions |
| Lab QC threshold and its derivation (FD < 0.2 mm on our data) | Published guideline / consensus (COBIDAS, OHBM best practices) |
| Exact cohort manifests, exclusions, per-participant derivatives | Dataset record, version, licence (OpenNeuro, DANDI, ABIDE) |
| Lab skills and runbooks (how we register, how we QC) | Shared skill repos (ReproNim/skills, sensein/agent_skills) |
| Local variable names, site-specific instruments | nidm-terms / InterLex concepts, ReproSchema library |
| Unpublished findings, reviews, disagreements | Publications, scoped claims in literature KGs |
| Data whose consent covers only the study or named uses; DUAs | DUO codes; only de-identified summaries the consent permits |

Transitions (each recorded as a PROV activity with an agent and a review assessment):
- **Promotion (local → global)** — gates: generality evidence (tested beyond one site/sample), review, de-identification and a check that consent covers broad sharing (DUO), licence, persistent identifier and version, provenance retained.
  Examples here: ABIDE claims and cohort definitions absent from BR-KG; FD-threshold sweep as evidence for a guideline; local ABIDE variable mappings → nidm-terms; a lab registration skill → shared skill repo.
- **Adoption (global → local)** — pin the version, record local parameters and deviations, re-validate on local data (a global template still needs per-participant QC).
- **Deprecation / revision** — global knowledge ages (activity snapshots) or is contradicted; local copies must be flagged when the global source changes.
- **Never promoted** — identifiable participant data, restricted fields, tacit judgements without recorded evidence.

### ReproNim terms: ReproPond and ReproLake (supersedes "local/global" wording on the slide)

Source: repronim.org tutorial "Sharing and Searching Metadata Using a ReproPond and the ReproLake"
(content/resources/tutorials/pond-lake.md). ReproPond = local FAIR metadata store (NIDM .ttl served by a
Neurobagel node; ponds can be federated across sites). ReproLake = semantically aligned store of
publicly available datasets (OpenNeuro and others) maintained by ReproNim. Neurobagel Query searches
across ponds and the lake (participant-level and dataset-level results).

What stays in the pond (cannot leave for sensitivity reasons):
- Data whose consent does not cover broad sharing (consent scoped to the study or to named uses; DUO restrictions; NDA/ABCD-style DUAs). Data with no research consent does not belong in a pond at all.
- Direct identifiers: names, MRNs, addresses, contact details, full dates (birth, scan), free text
- Identifiable images: undefaced structural scans
- Quasi-identifier combinations: rare diagnosis + site + exact age; small cells
- Restricted fields defined by the study's agreements
- Linking keys between pseudonymous IDs and people

What can flow pond → lake (after the gates): dataset-level metadata, data dictionaries and term mappings,
aggregate counts above a minimum cell size, de-identified/consented participant-level records,
derived measures where consent allows, skills/procedures, provenance with pseudonymous IDs,
scoped claims. Federated query lets the question travel to the pond and only permitted answers return.

In our examples: ds000030 and ABIDE I are public, de-identified releases (lake-eligible); analysts'
reviews, local QC rules and the illustrative collaboration records start in a pond.

## How each slide was made: AI-involvement badges (teaching lecture)

Every slide carries a small badge (bottom-left, consistent) with two parts: how it was produced, and how it was checked.
Full key on one backup slide; one MAIN slide near the end ("How this lecture was produced", ~1:00).

Production (one or more):
- **H** — written or decided by the speaker
- **L** — drafted by an LLM from the speaker's instructions, then edited by the speaker
- **A** — computed by an agent writing and running code (Python, SPARQL, Slurm on ORCD)
- **R** — retrieved by an agent from cited sources (papers, repos, web); quotes checked against source
- **M** — answered by an external agent system through MCP (Brain Researcher)
- **P** — produced in an earlier session by a different agentic system (ds000030 package, v3 deck), reused

Checking (one):
- **re-run** — recomputed independently (e.g., clean rebuild on ORCD matched)
- **validated** — passed automated checks (SHACL, schema, tests, render QA)
- **reviewed** — read and corrected by the speaker
- **unverified** — not independently checked; stated as such

"How this lecture was produced" slide: speaker instructions → orchestrating agent → sub-agents (deck builder,
experiment builder) + a second session using Brain Researcher (MCP) → tools (Python, Oxigraph, pyshacl, PowerPoint
render, ORCD Slurm) → automated checks → speaker review. Human corrections made during production (examples):
consent wording ("consent not covering broad sharing", not "no consent"); query performance (rdflib → Oxigraph +
query optimisation); AbstractAtlas links dropped and restored; LLM-style footers and titles removed; ReproNim
terms (ReproPond/ReproLake) substituted; local vs global knowledge added; NIDM model updated to PyNIDM LinkML.
Agent-side issues caught by checks: failed ORCD FDR job (invalid p-values); a stalled 27-min rdflib query;
two agents reconstructing the same cohorts differently.

The slide-provenance records are also emitted as PROV (talk_provenance.ttl): each slide an entity,
wasGeneratedBy activities with the agent types above, wasDerivedFrom the results/figures it shows.

## Route v5 — didactic, organised by the two learning objectives (supersedes earlier routes)

Audience: neuroimagers. Assume they know BIDS, fMRIPrep/C-PAC, FreeSurfer, phenotype tables, motion QC,
cross-validation. Do NOT assume RDF, triples, SPARQL, PROV, ontologies, or how LLM agents work. Define each
term in plain words at first use, with a neuroimaging example. Every main slide carries a small tag
"Objective 1" or "Objective 2" (or "Doing it with an assistant") so the audience sees where they are.

Opening (2:00)
1. Title (with badge legend)                                      0:20
2. Learning objectives                                            0:40
3. NEW "A knowledge graph in three statements" — triples primer:   1:00
   sub-10159 —has value→ bis_parcel1 = 2; that value —was derived from→ barratt.tsv row 2;
   sub-10159 —participated in→ ds000030 (commit 4070b6e). Subject / relation / object; a graph is
   statements that share nodes; a query is a statement pattern with blanks ("?participant has FIQ ?x").
   Plain-word glossary strip: triple, identifier, vocabulary (NIDM/PROV), query (SPARQL).

Part 1 — Objective 1: represent a result as a knowledge graph (~8:00)
4. Components of a dataset and a publication (JB)                 1:00
5. Entities in a neuroimaging knowledge graph (taxonomy ring)     0:45
6. Knowledge graph around a single participant (ABIDE)            1:00
7. Linking a claim to its evaluation and cohort (Kim chain)       1:15
8. Exercise (replaces the ds000030 poll): "Write the chain for your own last result" —
   pairs, 60 s: question → claim (with scope) → cohort → derived measure → source data;
   prompt card with the five boxes to fill. Then 1–2 volunteers.        1:30
9. Exercise: evaluating claims against a source (A/B/C)          1:00
10. Quotation checks and scientific entailment (reveal)           0:45
(types of knowledge → backup or merged into 5's notes; recompute 272/272 → backup; poll + scope pair → backup)

Part 2 — Objective 2: connect information across graphs (~8:00)
11. Joining graphs through shared identifiers (simple2, AbstractAtlas, OpenAlex, BR-KG, review)  1:15
12. Participant coverage by data element (the flipped view)       0:45
13. ABIDE I: two analyses, two research questions                 0:45
14. ABIDE I: group differences and site-held-out prediction       1:00
15. Exercise: consequences of a stricter motion threshold         0:30
16. Dependency tracing after a QC revision (reveal)               0:45
17. Linking datasets, publications and abstracts + Evaluation schemes in 74 ABIDE studies (keep both, tight)  1:30
18. ReproPond and ReproLake: what can leave your lab               1:00

Part 3 — Doing it with an assistant (~4:30)
19. Capabilities and limits of LLM assistants                     0:30
20. NEW Live demo (1/2): build a graph in Claude Code — exact install + prompt 1–2, expected output   1:30
21. NEW Live demo (2/2): query and use it — prompts 3–4 (cohort join, trace, QC impact), expected output   1:30
22. How this lecture was produced (checks + speaker corrections)  0:45
(Checking agent outputs → merge its 4 fault tiles into 22 or backup; BR comparison → backup)

Close (1:30)
23. Practices to adopt now (grouped under Objective 1 / Objective 2)   1:00
24. Discussion                                                     0:30
Target total ≈ 24:00. Demo slides double as a printed fallback if live demo fails (show the recorded transcript).

## Plain-language glossary (use at first mention on slides; full list on a backup slide)

Rule: every dataset, instrument, variable, pipeline, method and standard named on a main slide is explained in
plain words on that slide (short gloss in smaller text) or the term is replaced by its plain description.

Datasets and participants
- ds000030 — UCLA Consortium for Neuropsychiatric Phenomics (CNP) dataset on OpenNeuro: adults with schizophrenia,
  bipolar disorder, ADHD and healthy controls; MRI, task fMRI and questionnaires.
- sub-10159 — one participant's anonymised ID in ds000030.
- ABIDE I — Autism Brain Imaging Data Exchange: resting-state fMRI and phenotypes from 17 international sites
  (1,112 participants); "ABIDE Preprocessed" = the same data processed by the Preprocessed Connectomes Project.
- ASD / TD — autistic participants / typically developing (non-autistic) comparison participants.
- UCLA, COBRE — two separate patient/control cohorts used by Kim et al. 2023.
Instruments and variables (verified against the ds000030 data dictionary)
- Barratt Impulsiveness Scale (BIS) — 30-item self-report questionnaire of impulsivity; each item scored
  1 = rarely, 2 = occasionally, 3 = often, 4 = almost always.
- bis_parcel1 ("acts impulsively") — mean of item 17 "I act 'on impulse'" and item 19 "I act on the spur of the
  moment"; sub-10159 scored 2 and 2 → 2.0 ("occasionally").
- Stop-signal task; SSRT — stop-signal reaction time: how long a person needs to cancel a started response
  (quantile RT minus mean stop-signal delay).
- FIQ — full-scale IQ. SRS — Social Responsiveness Scale (caregiver/self rating of social behaviour).
  ADOS — Autism Diagnostic Observation Schedule (clinician-administered).
- Mean FD — mean framewise displacement: average head movement between fMRI volumes, in mm.
Pipelines, atlases, methods
- C-PAC — Configurable Pipeline for the Analysis of Connectomes (the preprocessing used for ABIDE Preprocessed).
- CC200 — a 200-region functional brain parcellation (Craddock 2012); connectivity = correlation between regions'
  average time series.
- Tangent-space connectivity — a way of comparing connectivity matrices that accounts for their geometry.
- fMRIPrep; FreeSurfer BBR (boundary-based registration of fMRI to anatomy); ANTs SyN (non-linear registration to a
  template); MNI152NLin2009cAsym (a standard adult brain template).
- CPM — connectome-based predictive modelling; linear SVM — a standard linear classifier.
- LOOCV — leave-one-subject-out cross-validation; leave-site-out — train on all sites but one, test on the
  held-out site; pooled k-fold — sites mixed across training and test folds.
- AUC — area under the ROC curve: 0.5 = chance, 1 = perfect separation. FDR — false discovery rate correction.
- Cohen's d — standardised effect size (difference in means / SD).
- UMAP — a method that places participants on a 2-D map so similar profiles sit close; trustworthiness — how well
  local neighbours are preserved (1 = perfectly).
Standards and vocabularies
- Knowledge graph — a set of statements (subject → relation → object) that share identifiers.
- RDF/Turtle — the file format for such statements. SPARQL — the query language ("find statements matching this
  pattern"). Oxigraph — a database that answers SPARQL queries.
- NIDM — Neuroimaging Data Model: vocabulary for participants, acquisitions, measurements and derivatives.
  PROV — W3C provenance standard: which activity produced what, from what, by whom.
- SHACL — machine-checkable rules a graph must satisfy (e.g. "every derived value names its source").
- UBERON — anatomy vocabulary (e.g. UBERON:0000956 = cerebral cortex grey matter). InterLex / nidm-terms —
  shared definitions of neuroimaging variables. ECO — Evidence & Conclusion Ontology (types of evidence for a claim).
- DUO — Data Use Ontology (machine-readable consent/data-use conditions). ORCID / DOI / RRID — persistent IDs for
  people / papers / tools.
- PROBAST — Prediction model Risk Of Bias ASsessment Tool. ComBat — statistical harmonisation of site effects.
- ReproPond / ReproLake — ReproNim terms: a lab's local metadata store / a shared store of public datasets.
  Neurobagel — tool that sends a query to each pond and returns only permitted results.
- AbstractAtlas — searchable map of OHBM 2026 abstracts and their extracted claims. OpenAlex — open catalogue of
  scholarly works. SynthScholar — systematic-review tool (PRISMA). StructSense — claim/entity extraction tool.
  Brain Researcher — an external AI research assistant reached through MCP (a standard plug-in interface for tools).

## Every slide relates to the knowledge graph (speaker direction, 2026-10-15)

Each main slide carries a small "In the graph" strip: what the slide reads from the graph (named graph(s),
node/edge types, query file) and what produced any figure (script path). If a slide does not relate to the graph,
reframe or cut it. Example — Participant coverage by data element: "8 SPARQL queries (queries/Q14.rq) over
graph/core + view/volumes + ReproNim simple2 graphs → counts by site and diagnosis → figure by
code/element_coverage.py". The data are in the graph; the figure is a script output.

Reframes: Capabilities and limits → "What an assistant can read from a graph, and what it cannot";
How this lecture was produced → "The lecture's own provenance graph" (talk_provenance.ttl) with one query;
ReproPond/ReproLake → scope and consent as attributes on graph records.

## Harmonising graphs built by different people (new main slide, Objective 2)

1. Shared identifiers — dataset IRI + version, participant ID, DOI, ORCID, RRID.
   Example: ReproNim simple2 ↔ ours via ndar:src_subject_id = SUB_ID, 1,112/1,112.
2. Shared vocabularies — nidm:isAbout concepts (InterLex/nidm-terms), UBERON regions, Cognitive Atlas tasks.
3. Shared schema and validation — PyNIDM LinkML schema → SHACL; the same checks for every contributor.
4. Reviewed mapping links where vocabularies differ — skos:exactMatch / closeMatch, attributed to a reviewer;
   never a silent owl:sameAs.
5. One named graph per contributor, with PROV — conflicts stay visible instead of being overwritten.
   Examples: "CSF" under one UBERON term is total CSF in FSL but ventricles in ANTs/FreeSurfer (~200×);
   two agents reconstructed the ABIDE cohorts differently (871-based vs 767).
6. Federation instead of copying — Neurobagel sends the query to each pond.
