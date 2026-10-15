ABIDE I COLLABORATION KNOWLEDGE GRAPH EXPERIMENT

Start with report.html. Every number in it comes from results/*.json, and
results/key_numbers.json holds the headline numbers in one flat file so two
runs can be diffed (code/key_numbers.py --compare).

WHAT THIS IS
Two HYPOTHETICAL analysts share one public dataset (ABIDE I Preprocessed,
C-PAC "filt_noglobal" strategy, CC200 atlas) and ask different questions:
  Analyst A: do ASD and TD males differ in functional connectivity?
             (modelled on Di Martino et al. 2014, Mol Psychiatry)
  Analyst B: can connectivity predict diagnosis at unseen sites better than
             age, sex and head motion? (modelled on Abraham et al. 2017)
They review each other's results. Then A tightens a shared head-motion rule
(mean framewise displacement < 0.2 mm -> < 0.15 mm). The graph is queried to
find everything that depends on the change BEFORE anything is recomputed;
then everything is recomputed and the real change is measured. The analysts,
reviews and revision are a simulation. No real person's work is represented.
Neither paper is replicated.

Around that core the graph joins: ReproNim's own NIDM files for ABIDE
(phenotype plus ANTs, FSL and FreeSurfer brain volumes), a PyNIDM-generated
phenotype graph, a catalog of 58 resources with dated activity snapshots, and
a ReproPond / ReproLake scope layer that says what may leave the lab.

WHAT RAN
- Inputs: phenotype table, 1,035 CC200 time series, 1,035 ANTs ROI-thickness
  files, the C-PAC config, two paper texts, 24 ReproNim simple2 site graphs,
  3 tool CDE files and ReproNim's ABIDE term map: 2,108 files, all checked
  against data/expected_sha256.json.
- NIDM/PROV graph (graph/abide_kg.ttl) conformed to PyNIDM v4.5.5's LinkML
  schema: participants carry ndar:src_subject_id; phenotype variables are
  nidm:PersonalDataElements with nidm:isAbout concepts taken from ReproNim's
  term map (the same IRIs ReproNim's files use); scans carry modality,
  contrast, usage and nfo:filename; derivatives carry a tool association
  (role nidm:NIDM_0000164) and a subject association; hashes use crypto:sha256.
  Selection rules, cohorts (with members), analyses, folds (with train/test
  participants), results, claims and reviews are nodes too.
- PyNIDM csv2nidm v4.5.5 run non-interactively, exactly as ReproNim's simple2
  script does, on the 75 mapped phenotype columns (code/pynidm_phenotype.py).
- Paper layer: questions, claims typed associational or predictive, reported
  cohorts and methods; 18 quotes checked verbatim against the source text.
- Analyst A (edgewise OLS, FDR), Analyst B (leave-one-site-out, four feature
  sets), cross-reviews, the revision traversal and recomputation, a phenotype
  UMAP joined to image-derived measures.
- ReproNim simple2 join (code/repronim_simple2.py): their files loaded
  unmodified as named graphs; their simple2_query.sparql run unmodified; an
  identity join through the shared ndar:src_subject_id literal; the same
  anatomical region compared across ANTs, FSL and FreeSurfer.
- Validation: our local SHACL profile (17 shapes, 8 mutation tests) and SHACL
  generated from the LinkML schema with `linkml gen-shacl`, applied to our
  graph, to PyNIDM's own output and to one ReproNim file.
- Resource catalog (code/resources_catalog.py): schema.org/CodeMeta records
  with plain-language descriptions sourced from each README at a pinned
  commit, workflow-step facets, EDAM terms resolved from the EDAM release
  file, graph classes consumed/produced, and whether each was executed here,
  used as a data source, or is a pointer only. ReproNim/skills was inspected:
  at commit faef6c04 it contains no skills yet.
- Activity snapshots (code/refresh_activity.py): appended, never
  overwritten; each has prov:generatedAtTime and the refresh activity that
  made it. Four refreshes (one partial) are in graph/resource_activity.ttl. "Latest" is
  resolved by query. Commit counts are taken on the default branch.
- Resource search (code/find_resources.py): SPARQL facet filters plus BM25
  over descriptions, ranked with a freshness factor; every activity number is
  printed with its as-of time and age (results/find_resources_examples.txt).
- Scope layer (code/scope.py, graph/scope.ttl), using ReproNim's terms:
  ReproPond (local store, at analyst, lab or site level), consortium
  federation, ReproLake (public, semantically aligned). Each record family has
  a sensitivity profile: consentScope (broad-sharing | study-only |
  named-uses, plus DUO codes when known), direct and quasi-identifiers,
  defacing, agreements, access level, and a derived egress decision with its
  reason. Data without research consent does not belong in a pond at all and
  is not modelled. Promotions (pond -> lake) record six gates; adoptions
  (lake -> pond) record the pinned version, local parameters and local
  re-validation; revisions and deprecations link to the evidence.
- Query engines: an on-disk Oxigraph store (code/store.py) with one named
  graph per source and four materialized views, each recorded as a PROV
  activity with input hashes so it is rebuilt when an input changes. Every
  competency query (Q1-Q15) runs there. rdflib is used only to build the
  smaller graphs and for SHACL validation.

THINGS WORTH SAYING OUT LOUD
- Rater QC reconstructs 873 participants; Abraham et al. report 871.
- A's "hypoconnectivity" signature correlates about 0.98 with whole-brain
  mean connectivity (no global signal regression), and does not separate the
  groups in participants A never used (B's review).
- The revision flags every one of B's folds, but 0 of 9 result families
  change materially. Flagging says what to recheck; recomputing says what
  changed. The tightened rule also removes 23% of ASD vs 14% of TD
  participants, and up to 88% of one site: it is site- and
  diagnosis-dependent, so it fails the generality gate for promotion.
- ReproNim's shipped query output is reproduced exactly except for three
  ANTs measures whose labels changed after the CSV was written.
- The same UBERON term ("CSF") means total CSF in FSL and the ventricular
  label in FreeSurfer and ANTs. Cortical grey-matter volume correlates with
  age at -0.25 (FreeSurfer), -0.11 (FSL) and +0.09 (ANTs) in the same people.
- The schema written for LLM query generation (PyNIDM's LinkML file) is
  violated by PyNIDM's own output and by ReproNim's files as well as by
  ours (one violation, the association-agent class, is shared by ReproNim's
  files and ours). Those are schema gaps, recorded in
  results/linkml_validation.json.
- Oxigraph runs ReproNim's simple2 query unmodified on all 24 sites in about
  2 minutes (in-memory store, union default graph; results/simple2.json).
- Rewriting the revision-fold query exposed a double count in the first
  version (participants in both cohorts counted twice per fold); the
  version shipped is the corrected one.

PUBLICATION LINKS: ABSTRACTATLAS AND OPENALEX (code/publications.py)
- Which recent work uses ABIDE? Two sources, both pinned so the answer can
  be re-derived (facts: results/publications.json; Q15).
- AbstractAtlas: the OHBM 2026 bundle
  (https://aadata.cirrusscience.org/dd1a1a8d88f7f505128733bf789c6a3fa4f48ed62e546bebfab2453587b0149f/ohbm2026.parquet,
  addressed by its content hash; AbstractAtlas repo commit 181652e2) holds
  3,240 abstracts. 35 mention ABIDE; 17 state that they used ABIDE data, 18
  only mention it. Those 35 abstracts carry 541 AbstractAtlas claims (each
  with its source quote). Of the 17 "stated use" links, read by hand: 15 are
  correct; posters 1217 (a regex hit on a long methods sentence about
  matched controls) and 639 (a reference title) are not ABIDE data use.
  The link is a regex over title and sections, so it says "states use",
  not "used".
- OpenAlex: 598 works cite Di Martino 2014 and name ABIDE in their title or
  abstract (220 for Abraham 2017). These are "candidate" links, not checked
  by hand; the 50 most-cited per paper are stored as nodes.
- Each pull is a dated snapshot (graph/publication_links_activity.ttl), so
  the graph answers "how current is this list" from its own timestamps.

REPRONIM RESOURCES, ACTIVITY SNAPSHOTS AND find_resources
- graph/resources.ttl: 58 ReproNim and related resources (tools, BIDS apps,
  specifications, vocabularies, training material, datasets) described with
  schema.org/CodeMeta terms, a plain-language description taken from each
  README at a pinned commit, the workflow step it serves, EDAM terms, the
  graph classes it consumes or produces, and how it was used here: 6
  executed (nilearn, scikit-learn, umap-learn, rdflib, pySHACL, pyoxigraph),
  8 used as data sources (e.g. segstats_jsonld, ants_seg_to_nidm and
  fsl_seg_to_nidm outputs in ReproNim's simple2 files), 44 pointers only.
- Activity (commits in 90/365 days, contributors, last default-branch
  commit, release, OpenAlex mentions) is stored as dated snapshots, each
  with prov:generatedAtTime and the refresh activity that produced it
  (graph/resource_activity.ttl: 168 snapshots from four refreshes, one partial). Snapshots are appended,
  never overwritten; "latest" is chosen by query.
- code/find_resources.py answers "which tool should I use for X": SPARQL
  facet filters plus BM25 over the descriptions, ranked with a freshness
  factor. Every activity figure is printed with its as-of time and age
  (results/find_resources_examples.txt). Q10 example: for exporting
  FreeSurfer stats to NIDM the most active candidate is the FreeSurfer NIDM
  BIDS App (13 default-branch commits in 90 days); segstats_jsonld, the
  converter that made ReproNim's ABIDE files, had none in 90 days.

POND / LAKE SCOPE AND THE consentScope EGRESS GATE (code/scope.py)
- Every record family has a scope: ReproPond (local; analyst, lab or site
  level), consortium federation, or ReproLake (public, semantically
  aligned). Counts: 10 pond:analyst, 9 pond:lab, 1 pond:site, 63 lake.
- A sensitivity profile records consentScope (broad-sharing | study-only |
  named-uses, plus DUO codes when known), direct and quasi-identifiers,
  defacing, agreements and access level. Egress is derived from it, with
  the reason: anything whose consent is scoped to the study or to named
  uses, or restricted by agreement, or carrying quasi-identifiers without
  minimum cell sizes, stays in the pond (Q12). All records in a pond carry
  research consent; the gate is about the scope of that consent.
- The one site-level record is ILLUSTRATIVE (not real data): a study-only
  record that the gate keeps in the pond. ABIDE's own participant records
  are already public; they are linked to the lake copy, never re-promoted.
- Promotions (pond -> lake) record six gates (generality, review, consent
  and de-identification, licence, persistent identifier and version,
  provenance). 8 candidates; none passes all six (Q11). The tightened
  motion rule fails generality: it removes 23% of ASD vs 14% of TD
  participants and up to 88% of one site.

NIDM CONFORMANCE (code/validate_linkml.py, results/linkml_validation.json)
- The graph uses the terms of PyNIDM v4.5.5's LinkML schema
  (nidm_schema.yaml, commit 74793553): ndar:src_subject_id on participants,
  nidm:PersonalDataElement + nidm:isAbout for phenotype variables (ReproNim's
  own concept IRIs), modality/contrast/usage on scans, tool association role
  nidm:NIDM_0000164 on derivatives, crypto:sha256 hashes.
- What the schema has no place for is declared as an extension
  (graph/abide_extension.ttl): 13 classes (Claim, Cohort,
  EvidenceAssessment, EvidenceSpan, Fold, InclusionCriterion,
  MeasuredChange, Method, Publication, ReportedCohort, ResearchQuestion,
  Result, SelectionRule) and 191 properties.
- SHACL generated from the LinkML schema was applied to our graph, to
  PyNIDM's own csv2nidm output and to one ReproNim simple2 file. None of
  the three conforms even in "open" mode (extension terms allowed). Ours:
  activities with more than one association or input (the schema allows
  one) and association agents outside the schema's agent class. PyNIDM's
  own output: data-element "choices" and start/end-time datatypes.
  ReproNim's Caltech file: the same association-agent class as ours, and
  an acquisition-object datatype. These are schema gaps, recorded per
  shape and path, not patched in the data. "Closed" mode (no extension
  terms allowed) is also reported, to show how much the extension carries.

PARTICIPANT VIEW AND DATA-ELEMENT COVERAGE
- Q13 (code/participant_ego.py, figures/participant_ego.svg): everything
  the graph holds about MaxMun_c_0051332 - 239 source triples within two
  hops, drawn as 30 nodes: phenotype, motion and rater QC, raw-scan
  pointers, derived files with hashes, ANTs/FSL/FreeSurfer volumes, the
  PyNIDM and ReproNim records of the same person, cohort memberships (and
  why A_v2 excludes this person), folds, results, and scope.
- Q14 (code/element_coverage.py, figures/element_coverage.png): how many
  participants have each data element, by diagnosis and site, and which
  element limits each analysis (e.g. UMAP + SRS: 330 participants, limited
  by SRS, which is missing at 15 sites; ADOS + connectivity: 347).

QUERIES (queries/, queries/optimized/)
- All queries run on Oxigraph (pyoxigraph) over the on-disk store, written
  for it: scoped to named graphs, with four materialized views
  (queries/views/) for the type closure, volume measures, volumes and the
  phenotype matrix. Each competency answer takes under 0.5 s
  (results/competency_answers.json).
- An earlier plan to time rdflib against Oxigraph was dropped; no engine
  comparison is part of this package.

ORCD VS LOCAL (results/orcd_vs_local.json)
- ORCD job 25939932 (graph steps) was submitted, but
  its outputs could not be fetched: two SSH logins were refused on
  2026-10-15 and no further attempt was made. The comparison is therefore
  NOT done; the file says how to complete it with
  code/key_numbers.py --compare.

CLEAN-ROOM CHECK (results/clean_room_verify.json)
- This zip was unzipped into an empty directory, every input was
  downloaded fresh (2,108/2,108 hashes match) and the pipeline rerun:
  every key number that is not a run time agrees within 1%, and all 15
  gold answers are identical (Q10 differs only in its "answered at"
  time).
- The check caught a real reproducibility bug: the AbstractAtlas bundle
  host refuses Python's default user agent (HTTP 403), so publications.py
  now sends its own. It also caught a stale file (abide_extension.ttl had
  12 classes; current code gives 13), regenerated before packaging.

WHAT DID NOT RUN
- No raw MRI was downloaded or reprocessed. Preprocessing and the ReproNim
  volumes are taken as released.
- No replication of either paper.
- Abraham 2017 quotes come from arXiv v1, not the journal text.
- PyNIDM `queryai` was not run (it needs an LLM API key); recorded as a
  pointer. Its schema file is the one validated here.
- Neurobagel, the ReproNim BIDS apps, ReproSchema, Neurodocker and the other
  pointer resources were not run.
- The BR-KG fact used in a promotion gate (one aggregate ABIDE node, neither
  paper DOI present) was relayed from a parallel session, not re-queried.
- Neither local SHACL profile nor LinkML SHACL checks scientific correctness.

REBUILD (needs uv; network access to s3.amazonaws.com, raw.githubusercontent.com,
ebi.ac.uk and arxiv.org)
  bash rebuild.sh                  # everything, about 45-60 min on a laptop
  STEPS=graph bash rebuild.sh      # graph, query and report steps only
On ORCD: orcd/run_graph.sbatch (graph steps; RUN_FULL=1 for everything).
Compare a rebuild with this package:
  uv run python code/key_numbers.py --compare <other>/results/key_numbers.json --rtol 0.01
Activity snapshots are not part of the rebuild (they depend on the date):
  uv run python code/refresh_activity.py      # appends one snapshot per resource
Scheduling templates (not installed): scheduling/.

EXPECTED NONDETERMINISM
- Seeds are fixed (42; UMAP also 1 and 2); UMAP runs single-threaded.
- Floating point differs in late digits across CPUs and BLAS builds, which
  can move UMAP coordinates and, rarely, flip a borderline FDR edge or a
  prediction at 0.5. Counts should match exactly; continuous values within ~1%.
- csv2nidm mints random UUIDs, so its output hash changes every run; its
  structure and counts do not.
- Run times (pynidm, simple2, competency) depend on the machine and its load.
- Europe PMC or arXiv may re-render a paper; download.py warns and
  papers.py re-checks every quote.

LAYOUT
code/        scripts, SHACL shapes, frozen original queries
data/        phenotype CSV, resources, vocabularies (EDAM, NIDM LinkML schema
             and generated shapes), pinned resource metadata, expected hashes
             (time series, thickness files, papers and ReproNim files are
             fetched by the rebuild)
graph/       abide_kg.ttl (final), abide_kg_v1.ttl (before revision),
             papers.ttl, repronim_simple2_link.ttl, resources.ttl,
             resource_activity.ttl, scope.ttl, abide_extension.ttl,
             embedding_provenance.ttl
queries/     Q1-Q15, revision traversal, optimized/ (texts run on Oxigraph),
             views/ (SPARQL Update for materialized views)
results/     numeric outputs, key_numbers.json, validation reports
figures/     PNG + PDF
comparison/  questions.json (no answers) and gold_answers.json
orcd/, scheduling/  cluster job and refresh templates

SOURCES AND LICENCES
ABIDE Preprocessed: http://preprocessed-connectomes-project.org/abide/
  ABIDE I is shared under CC BY-NC-SA; "In accordance with HIPAA guidelines
  and 1000 Functional Connectomes Project / INDI protocols, all datasets have
  been anonymized, with no protected health information included."
  (https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html)
ReproNim simple2_NIDM_examples, commit e0dff17629bd5031e246c05ff4bed174597552a2
PyNIDM v4.5.5, commit 74793553f2ef0884602c4383fe8dbe8c74e3dcb8 (Apache-2.0 schema)
EDAM ontology TSV (CC BY-SA 4.0), retrieved 2026-10-15
Di Martino A et al. 2014. Mol Psychiatry 19:659-667. doi:10.1038/mp.2013.78
Abraham A et al. 2017. NeuroImage 147:736-745. doi:10.1016/j.neuroimage.2016.10.045
Paper texts are not redistributed in this package.
