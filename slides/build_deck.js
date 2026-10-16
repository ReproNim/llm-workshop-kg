// Builds Knowledge_Graphs_Skills_Neuroimaging_v4.pptx.
//   cd deck_build && node build_deck.js
// ABIDE result slides read only from the ABIDE object below.

const fs = require("fs");
const path = require("path");
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");


const { applyTheme } = require("./apply_theme.js");
const { V, ROOT } = require("./values.js");

const OUT = path.resolve(__dirname, "Knowledge_Graphs_Skills_Neuroimaging_v4.pptx");
const CNP_UMAP = path.join(ROOT, "experiments/ds000030/experiment/results/phenotype_embedding.png");

// ---------------------------------------------------------------- ABIDE content
const PENDING = "[ABIDE: pending]";
const EXP = path.join(ROOT, "experiments/abide");
// All values below are read from ABIDE_Collaboration_Experiment results files (paths in each slide's notes).
// Slide-size redraws in deck_build/figs_slide/ replace the package figures when present.
const slideFig = (name, orig) => { const f = path.join(__dirname, "figs_slide", name); return fs.existsSync(f) ? f : orig; };
const ABIDE = {
  participant: {
    title: "Knowledge graph around a single participant",
    id: "MaxMun_c_0051332",
    figure: slideFig("participant_ego_slide.png", EXP + "/figures/participant_ego.png"),
    layers: [
      { name: "Phenotype", count: "38 values" },
      { name: "Scans and QC", count: "2 scans; head motion 0.064 mm" },
      { name: "Derived data", count: "regional time series, connectivity" },
      { name: "Brain volumes by tool", count: "ANTs 101 · FSL 18 · FreeSurfer 62" },
      { name: "Cohorts and folds", count: "4 cohorts; dropped from one" },
      { name: "Results", count: "10 results" },
      { name: "Publication", count: "Abraham 2017 cohort" },
      { name: "Consent scope", count: "broad sharing" },
    ],
    notes: "Source: results/participant_ego.json and figures/participant_ego.png (239 triples within two hops, 30 nodes; one query, 0.027 s). MaxMun_c_0051332: 38 phenotype values from source row 1003, mean FD 0.0644 mm; two raw scans held as S3 pointers; CC200 time series and 19,900-edge connectivity with hashes; brain volumes from ANTs (101), FSL (18) and FreeSurfer (62) joined from ReproNim simple2 through ndar:src_subject_id; member of the reconstructed Abraham cohort, B_v1, A_v1 and B_v2, but not A_v2, because the MAX_MUN site falls below the 10-per-group minimum under the stricter motion rule; input to 10 results; record scope broad sharing, egress permitted.",
  },
  elements: {
    title: "Participant coverage by data element",
    figure: slideFig("element_coverage_slide.png", EXP + "/figures/element_coverage.png"),
    callouts: [
      { value: V("elements.participants"), label: "participants with phenotype records" },
      { value: V("elements.analystB"), label: "meet Analyst B's inputs (time series limit it)" },
      { value: V("elements.iqVolumes"), label: "IQ scores + FreeSurfer volumes" },
      { value: V("elements.srs"), label: "with Social Responsiveness Scale (4 sites)" },
    ],
    notes: "Source: results/element_coverage.json (query Q14, 0.24 s) and figures/element_coverage.png. 1,112 participants; CC200 time series for 989; Analyst B's inputs (age, FD, CC200) for 988 at 20 sites; age + FIQ/VIQ/PIQ + FreeSurfer hippocampus for 746 at 15 sites (VIQ limits it); adding SRS leaves 330 at 4 sites. Missing elements cluster by site, not at random: SRS is missing at 15 sites, VIQ at 4.",
  },
  pubs: {
    title: "Linking datasets, publications and abstracts",
    asOf: "2026-10-15",
    publications: V("pubs.openalex"),
    abstracts: V("pubs.abstracts"),
    claims: V("pubs.claims"),
    reviewed: V("pubs.reviewed"),
    reconstructible: V("pubs.reconstructible"),
    subset: "9",
    notes: "Sources: results/publications.json and literature_review/synthesis.md. OpenAlex (pulled 2026-10-15): 598 works cite Di Martino 2014 and name ABIDE in title or abstract; 220 do so for Abraham 2017; status candidate. AbstractAtlas OHBM 2026 (commit 181652e2): 35 abstracts mention ABIDE, 17 state data use (15 of 17 correct on hand check), 18 mention it only; they carry 541 extracted claims. SynthScholar review: 994 records identified, 99 assessed, 74 included; cohorts reconstructible exactly for 17 (participant lists published for 4); 9 studies reuse the 871-participant ABIDE I subset, which our graph reconstructs as 873.",
  },
  joins: [
    { icon: "FaDatabase", name: "ReproNim simple2 NIDM", src: `ReproNim's ABIDE records, ${V("joins.sites")} sites`, key: "participant ID", result: `${V("joins.matched")} / ${V("elements.participants")} matched, none left over · ${V("joins.timeseries")} with time series · ${V("joins.inB")} in B's cohort (reviewed link, not declared identical)` },
    { icon: "FaBook", name: "AbstractAtlas", src: "OHBM 2026 abstracts", key: "dataset name in abstract text", result: `${V("pubs.abstracts")} abstracts · ${V("pubs.statedUse")} state data use · 15 / ${V("pubs.statedUse")} correct on hand check` },
    { icon: "FaGlobe", name: "OpenAlex", src: "open catalogue of papers", key: "DOI and citation", result: `${V("pubs.openalex")} works cite Di Martino 2014 and name ABIDE` },
    { icon: "FaBrain", name: "Brain Researcher KG", src: "an external AI assistant's graph", key: "dataset node", result: "one aggregate ABIDE node (2,226 subjects); neither paper present" },
    { icon: "FaSearch", name: "Literature review", src: "systematic review (SynthScholar)", key: "DOI and cohort description", result: "9 of 74 reviewed studies reuse the 871-participant ABIDE I subset, incl. Abraham 2017, Parisot 2018, Ktena 2017" },
  ],
  cohorts: { aN: V("cohort.aN"), bN: V("cohort.bN"), both: V("cohort.aN"), aOnly: "0", bOnly: V("cohort.bOnly"), aRemoved: V("cohort.aRemoved"), bRemoved: V("cohort.bRemoved") }, // results/key_numbers.json cohort.*
  results: {
    title: "ABIDE I: group differences and site-held-out prediction",
    a: { headline: `${V("a.edges")} connections differ`, lines: [`FDR-corrected (false discovery rate); ${V("a.hypo")}% weaker in ASD (95% CI ${V("a.hypoLow")}–${V("a.hypoHigh")}%)`, `${V("a.interhem")}% of the weaker connections link the two hemispheres`, `median effect size d = ${V("a.medianD")} · n = ${V("cohort.aN")}, ${V("a.sites")} sites`, `Reviewed by B: not established in held-out participants (pooled d ${V("rev.d")}, ${V("rev.dLow")} to ${V("rev.dHigh")})`], caption: "Association in this cohort" },
    b: { headline: `AUC ${V("b.auc")} (${V("b.aucLow")}–${V("b.aucHigh")})`, lines: [`AUC: 0.5 = chance, 1 = perfect · tangent-space connectivity · tested on held-out sites, n = ${V("cohort.bN")}, ${V("b.sites")} sites`, `correlation ${V("b.corr")} · demographic + head motion ${V("b.demofd")} · demographic only ${V("b.demo")}`, `accuracy ${V("b.acc")}%`, `Reviewed by A: top edges overlap A's ${V("rev.overlap")} vs ${V("rev.expected")} expected (p ≈ 4e−8)`], caption: "Prediction at held-out sites" },
    figure: null,
    notes: "Source: results/key_numbers.json. Analyst A (n = 441, 9 sites): 5,428 FDR-significant edges, 5,407 hypoconnected and 21 hyperconnected (99.6%, 95% CI 90.2–99.8%), 52% of hypoconnected edges interhemispheric, median |d| 0.30. Analyst B (n = 767, 20 leave-site-out folds): AUC tangent 0.74 (0.70–0.77), correlation 0.72 (0.69–0.76), demographic + FD 0.59 (0.54–0.62), demographic 0.48 (0.44–0.52); tangent accuracy 66.9%. Reviews: A finds 90 of B's top predictive edges among its significant edges against 54 expected (p ≈ 4e−8); B finds A's effect not established in the 326 participants outside A's cohort (pooled d −0.08, −0.31 to 0.15; 8 of 14 sites in the same direction). Abraham et al. 2017 reported 66.8% leave-site-out accuracy, against our B's 66.9%, on a different cohort definition (871 versus 767); rater QC alone gives 873 here against Abraham's reported 871 (cohort.rater_qc_pass.n). Caveat on A: its hypoconnectivity pattern correlates 0.98 with whole-brain mean connectivity (key_numbers.json: review_v1.B_of_A.signature_global_r), so much of it may reflect a global difference rather than specific edges. Figures in the package: figures/analyst_b_sites.png, figures/review_b_of_a_forest.png.",
  },
  predict: {
    title: "Exercise: consequences of a stricter motion threshold",
    change: "Analyst A tightens the head-motion rule: mean FD (average movement) < 0.2 mm → < 0.15 mm",
    questions: [
      "How many of B's test participants are now excluded?",
      "Which of B's results must be re-checked?",
      "Which will actually change?",
    ],
    notes: "The rule change is from results/key_numbers.json and README (mean framewise displacement < 0.2 mm → < 0.15 mm).",
  },
  reveal: {
    title: "Dependency tracing after a QC revision",
    stats: [
      { value: V("cohort.bRemoved"), label: `of B's ${V("cohort.bN")} participants excluded` },
      { value: `${V("reveal.foldsAffected")} / ${V("reveal.folds")}`, label: "cross-validation folds lose test participants" },
      { value: "91", label: "results, claims and reviews flagged" },
      { value: `${V("reveal.changed")} / ${V("reveal.families")}`, label: "result families changed materially" },
    ],
    notes: "Sources: results/revision_flags.json (graph traversal on the v1 graph, Oxigraph, 0.05 s in total) and results/revision_impact.json (after recomputation). 63 of B's participants fail the stricter rule; 17 of 20 leave-site-out folds have an affected test site and all 20 have affected training data. 91 distinct entities are flagged: 85 results, 2 claims and 4 reviews or assessments (comparison/gold_answers.json, Q5); revision_flags.json lists 92 entries because one review appears twice. After recomputation none of the 9 result families changed materially (rule: the v2 estimate outside the v1 95% interval, or a review verdict changing); tangent AUC 0.739 → 0.734. Analyst A loses 69 participants: 38 by the motion rule and the rest because MAX_MUN falls below the per-site minimum. The exclusion is differential: the tighter rule removes 23% of ASD and 14% of TD participants, and up to 88% at one site (key_numbers.json: scope.fd015_asd_excluded, scope.fd015_td_excluded, scope.fd015_site_max_excluded), so a QC change can shift the diagnostic balance of a cohort.",
  },
  umap: {
    title: "Phenotype embedding linked to image-derived phenotypes",
    figure: EXP + "/figures/umap_primary.png",
    points: [
      `${V("umap.n")} of B's ${V("cohort.bN")} with age, FIQ, VIQ and PIQ; ${V("umap.sites")} sites`,
      `trustworthiness ${V("umap.trust")} (PCA ${V("umap.pca")}); other seeds ${V("umap.seed1")}, ${V("umap.seed2")}`,
      "silhouette by diagnosis 0.03, by site −0.34",
    ],
    notes: "Source: results/umap.json and figures/umap_primary.png. 604 complete cases (163 dropped for missing IQ), 15 sites; trustworthiness 0.977 (PCA 0.920), other seeds 0.973 and 0.974, 15-neighbour overlap 0.87 and 0.86. Diagnosis does not separate (silhouette 0.03). Joined image-derived phenotypes correlate weakly with the embedding: FreeSurfer grey matter with UMAP 2, ρ = −0.26, which is about the same as its correlation with age (−0.25); check age and site before reading structure.",
  },
  resources: {
    title: "Resource discovery with dated activity records",
    query: "convert FreeSurfer stats to NIDM",
    results: [
      { tool: "FreeSurfer NIDM BIDS App", step: "IDP extraction to NIDM", activity: "13 commits in 90 days, release v0.1.1", asOf: "last commit 2 days before snapshot" },
      { tool: "segstats_jsonld", step: "IDP extraction to NIDM", activity: "0 commits in 90 days, used here as data source", asOf: "last commit 318 days before snapshot" },
      { tool: "MRIQC NIDM BIDS App", step: "QC to NIDM", activity: "10 commits in 90 days, release v0.1.1", asOf: "last commit 2 days before snapshot" },
    ],
    snapshot: "snapshot 2026-10-15 14:57 UTC, 0.46 h old at query time",
    figure: slideFig("resource_map_slide.png", EXP + "/figures/resource_map.png"),
    notes: "Source: results/find_resources_examples.json (first query) and figures/resource_map.png; workflow steps from graph/resources.ttl. Ranking is BM25 relevance times a freshness factor from dated activity snapshots (commits, releases, OpenAlex mentions), so every answer carries how old its evidence is. segstats_jsonld ranks second on relevance but has had no commits for 318 days.",
  },
  comparison: {
    title: "Graph, search and Brain Researcher: a small comparison",
    header: ["Question", "Our graph (gold)", "Brain Researcher (MCP tools only)"],
    rows: [
      ["Analyst B's QC cohort", "767 (348 ASD, 419 TD)", "Not answerable: one ABIDE node, 2,226 subjects"],
      ["A–B overlap; excluded by stricter QC", "441 (A within B); 63 excluded", "Not answerable: neither paper in its graph"],
      ["Trace one connectivity feature", "Time series URL + hash, C-PAC settings, raw scan", "Dataset level only: landing page, generic C-PAC node"],
      ["Results to re-check after QC change", "91 flagged by traversal; 0 of 9 changed", "Not answerable"],
      ["Does A's effect hold at held-out sites?", "Not established (pooled d −0.08)", "Not answerable: no matching nodes"],
      ["Who reviewed what, on what evidence?", "Six attributed assessments", "Not answerable"],
    ],
    notes: "Sources: comparison/gold_answers.json and comparison/brain_researcher/answers.json with transcripts Q1–Q7 (BR-only answers from its MCP tools; unscored). Brain Researcher's graph holds one aggregate ABIDE (I & II) node with 2,226 subjects and neither Di Martino 2014 nor Abraham 2017. The question about each paper's research question and claim type (Q4) is omitted from the table; BR could not answer it either. The search-only arm has not been run, so it is not shown. A second agent's reconstruction of the cohorts, built around the 871-participant subset, gave different overlaps (104 / 780 / 91) from the gold answer here; that disagreement between two agents is itself a reason to keep the cohort definition in the graph.",
  },
};

// ---------------------------------------------------------------- slide provenance (AI-involvement badges)
// production: H speaker · L LLM draft, speaker-edited · A agent computed · R agent retrieved · M external agent via MCP · P earlier agentic session
// checking: re-run · validated · reviewed · unverified
const CNP_ZIP = "experiments/ds000030";
const ABIDE_KEY = "experiments/abide/results/key_numbers.json";
const PLAN = "slides/talk_plan.md";
const prov = (production, checking, ...sources) => ({ production, checking, sources });
const DEMO_SOURCE_REL = "agent_skills: skills/neuroimaging-kg/examples/claude_code_demo.md";
const SLIDE_PROV = {
  "Connecting neuroimaging knowledge graphs across data, publications and labs": prov(["H", "L"], "reviewed", PLAN),
  "Components of a dataset and a publication": prov(["P", "R", "A"], "re-run · validated", CNP_ZIP, "experiments/abide/literature_review/results_synthesis.json"),
  "Harmonising graphs built by different people": prov(["H", "L", "A", "R"], "re-run · reviewed", PLAN, "experiments/abide/results/simple2.json", "experiments/abide/results/simple2_tool_agreement.csv", "agent_skills: skills/neuroimaging-kg/examples/abide_one_site/demo_output.txt", "agent_skills: skills/neuroimaging-kg/scripts/compare_graphs.py"),
  "Joining graphs through shared identifiers": prov(["A", "R"], "re-run · validated", "experiments/abide/results/simple2.json", "experiments/abide/results/simple2_tool_agreement.csv", "experiments/abide/results/publications.json"),
  "The two example datasets": prov(["P", "A", "R"], "re-run · validated", CNP_ZIP, ABIDE_KEY, "experiments/abide/results/element_coverage.json"),
  "A knowledge graph in four statements": prov(["H", "L", "P"], "re-run · reviewed", PLAN, CNP_ZIP),
  "Live demo: building a graph in Claude Code": prov(["A", "L"], "validated", DEMO_SOURCE_REL, "agent_skills: skills/neuroimaging-kg/examples/claude_code_demo_transcript.md"),
  "Live demo: querying and using the graph": prov(["A", "L"], "validated", DEMO_SOURCE_REL, "agent_skills: skills/neuroimaging-kg/examples/claude_code_demo_transcript.md"),
  "Glossary": prov(["H", "L", "R"], "reviewed", PLAN),
  "Learning objectives": prov(["H", "L"], "reviewed", PLAN),
  "Poll: participant count in ds000030": prov(["P", "R"], "re-run · validated", CNP_ZIP),
  "Participant counts in ds000030 by scope": prov(["P", "R"], "re-run · validated", CNP_ZIP, "https://github.com/OpenNeuroDatasets/ds000030/tree/4070b6eea231517bfeff42527a46d9d166ac4e13"),
  "Entities in a neuroimaging knowledge graph": prov(["H", "L", "R"], "reviewed", PLAN),
  "Types of knowledge and where they are recorded": prov(["H", "L", "R"], "reviewed", PLAN),
  "ReproPond and ReproLake as attributes on graph records": prov(["H", "L", "R"], "reviewed", PLAN, "https://www.repronim.org/resources/tutorials/pond-lake/"),
  "Knowledge graph around a single participant": prov(["A"], "re-run · validated", ABIDE_KEY),
  "Participant coverage by data element": prov(["A"], "re-run · validated", ABIDE_KEY),
  "Recomputing a derived score from source items": prov(["P", "R"], "re-run", CNP_ZIP),
  "Linking a claim to its evaluation and cohort": prov(["P", "R", "A"], "re-run · validated", CNP_ZIP, "https://doi.org/10.3389/fpsyt.2023.1232015", "https://osf.io/agqtn/", "slides/demo/rerun_ucla_cpm.json"),
  "Exercise: evaluating claims against a source": prov(["P", "R", "L"], "validated", CNP_ZIP, "https://doi.org/10.3389/fpsyt.2023.1232015"),
  "Quotation checks and scientific entailment": prov(["P", "R"], "validated", CNP_ZIP),
  "ABIDE I: two analyses, two research questions": prov(["A", "R"], "re-run · validated", ABIDE_KEY),
  "ABIDE I: group differences and site-held-out prediction": prov(["A", "R"], "re-run · validated", ABIDE_KEY),
  "Exercise: consequences of a stricter motion threshold": prov(["A"], "re-run · validated", ABIDE_KEY),
  "Dependency tracing after a QC revision": prov(["A"], "re-run · validated", ABIDE_KEY),
  "Phenotype embedding linked to image-derived phenotypes": prov(["A"], "re-run (UMAP-derived values differ slightly across machines)", ABIDE_KEY),
  "Linking datasets, publications and abstracts": prov(["A", "R"], "re-run · validated", ABIDE_KEY, "https://abstractatlas.brainkb.org/"),
  "Asking Claude about the literature graph": prov(["A"], "validated", "slides/demo/literature_query_answer.md", "experiments/abide/literature_review/literature_kg.ttl", "experiments/abide/literature_review/synthesis.md"),
  "Evaluation schemes in 74 ABIDE studies": prov(["A", "R"], "validated", "experiments/abide/literature_review/results_synthesis.json", "experiments/abide/literature_review/synthesis.md"),
  "Resource discovery with dated activity records": prov(["A", "R"], "re-run · validated", ABIDE_KEY),
  "Checking agent outputs against the graph": prov(["P", "R"], "re-run · validated", CNP_ZIP),
  "Graph, search and Brain Researcher: a small comparison": prov(["M", "A"], "reviewed", "experiments/abide/comparison/"),
  "The lecture's own provenance graph": prov(["H", "L"], "reviewed", PLAN, "talk_provenance.ttl"),
  "Practices to adopt now": prov(["H", "L"], "reviewed", PLAN),
  "Discussion": prov(["H", "L"], "reviewed", PLAN),
  // backup
  "Scope of the ds000030 extraction": prov(["P"], "re-run", CNP_ZIP),
  "NIDM and PROV roles for each record": prov(["P", "R"], "re-run", CNP_ZIP),
  "Requirements for joining behaviour to image-derived measures": prov(["P"], "unverified", CNP_ZIP),
  "Research questions and results of the three papers": prov(["P", "R"], "validated", CNP_ZIP),
  "StructSense extraction pilot": prov(["P"], "validated", CNP_ZIP),
  "Attribution across collaborators": prov(["P", "R"], "unverified", CNP_ZIP),
  "Design for a graph-versus-search comparison": prov(["P"], "unverified", CNP_ZIP),
  "Forms of drift and corresponding checks": prov(["P"], "unverified", CNP_ZIP),
  "Scan, events and phenotype details": prov(["P", "R"], "validated", CNP_ZIP),
  "Registration and cross-source joins": prov(["P", "R"], "validated", CNP_ZIP),
  "Skills and pull requests referenced": prov(["P", "R"], "validated", "https://github.com/sensein/agent_skills", "https://github.com/K-Dense-AI/scientific-agent-skills"),
  "Brain Researcher: reported benchmarks": prov(["P", "R"], "validated", "https://arxiv.org/abs/2608.19902"),
  "Workshop connections": prov(["P"], "unverified", "Knowledge_Graphs_Skills_and_Collaborative_Research.pptx"),
  "Sources": prov(["P", "R"], "validated", CNP_ZIP),
  "Entities in a neuroimaging knowledge graph (1 of 2)": prov(["H", "L"], "reviewed", PLAN),
  "Entities in a neuroimaging knowledge graph (2 of 2)": prov(["H", "L"], "reviewed", PLAN),
  "Types of knowledge and where they are recorded: full table": prov(["H", "L"], "reviewed", PLAN),
  "ReproPond and ReproLake: full table and transitions": prov(["H", "L", "R"], "reviewed", PLAN, "https://www.repronim.org/resources/tutorials/pond-lake/"),
  "Provenance of a single phenotype measurement": prov(["P", "R"], "re-run · validated", CNP_ZIP),
  "AbstractAtlas: building blocks": prov(["P", "R"], "validated", "https://github.com/sensein/abstractatlas"),
  "ds000030 phenotype embedding from a graph query": prov(["P"], "re-run (UMAP differed ≤ 0.011)", CNP_ZIP),
  "Key to the AI-involvement badges": prov(["H", "L"], "reviewed", PLAN),
};
const REBUILD = "experiments/ds000030/codex_verification/orcd_rebuild/rebuild_comparison.md";
const VERIFY = "experiments/ds000030/codex_verification/codex_claim_verification.md";
// evidence behind each checking word; re-run evidence is the ORCD rebuild (Slurm job 25941523)
const evidenceFor = (title, pv) => {
  const ev = [];
  const ds = pv.sources.some((x) => x === CNP_ZIP || /ds000030|fpsyt|arxiv|agent_skills|scientific-agent-skills|abstractatlas/.test(x)) || title.includes("Workshop");
  const abide = pv.sources.some((x) => x.startsWith("experiments/abide") || x === ABIDE_KEY);
  const cnp = pv.sources.includes(CNP_ZIP);
  if (pv.checking.includes("re-run")) {
    if (abide) {
      ev.push({ status: "re-run", file: "experiments/abide/results/clean_room_verify.json", activity: "talk:abide-clean-room-rebuild", agent: "talk:IndependentRebuild" });
      ev.push({ status: "re-run", file: "experiments/abide/results/orcd_vs_local.json", activity: "talk:orcd-job-25939932", agent: "talk:IndependentRebuild" });
    }
    if (cnp || !abide) ev.push({ status: "re-run", file: REBUILD, activity: "talk:orcd-job-25941523", agent: "talk:IndependentRebuild" });
  }
  if (pv.checking.includes("validated")) ev.push(ds ? { status: "validated", file: VERIFY, activity: "talk:claim-verification-2026-10-15", agent: "talk:IndependentVerifier" } : { status: "validated", file: null, activity: null, agent: "talk:AutomatedChecks" });
  if (pv.checking.includes("reviewed")) ev.push({ status: "reviewed", file: null, activity: null, agent: "talk:Speaker" });
  if (pv.checking.includes("unverified")) ev.push({ status: "unverified", file: null, activity: null, agent: null });
  return ev;
};
const PROD_DEF = [
  ["H", "Speaker", "written or decided by the speaker"],
  ["L", "LLM draft", "drafted by an LLM from the speaker's instructions, then edited by the speaker"],
  ["A", "Agent computed", "computed by an agent writing and running code (Python, SPARQL, Slurm on ORCD)"],
  ["R", "Agent retrieved", "retrieved by an agent from cited sources; quotes checked against the source"],
  ["M", "External agent (MCP)", "answered by an external agent system through MCP (Brain Researcher)"],
  ["P", "Earlier agentic session", "produced in an earlier session by a different agentic system, reused"],
];
const CHECK_DEF = [
  ["re-run", "recomputed independently (for example a clean rebuild on ORCD matched)"],
  ["validated", "passed automated checks (SHACL, schema, tests, render QA)"],
  ["reviewed", "read and corrected by the speaker"],
  ["unverified", "not independently checked; stated as such"],
];

// ---------------------------------------------------------------- live demo content
// Filled from skills/neuroimaging-kg/examples/claude_code_demo.md once that file exists and has been run; placeholders until then.
const DEMO_SOURCE = path.join(__dirname, "demo/claude_code_demo.md");
const DEMO = {
  filled: true,
  repo_branch: "github.com/sensein/agent_skills, branch neuroimaging-kg (PR #49)",
  transcript_path: "agent_skills/skills/neuroimaging-kg/examples/claude_code_demo_transcript.md",
  install: [
    "git clone https://github.com/sensein/agent_skills.git",
    "cd agent_skills && git checkout neuroimaging-kg && cd ..",
    "mkdir abide-kg-demo && cd abide-kg-demo",
    "python ../agent_skills/scripts/install_skills.py --agent claude --scope project --skills neuroimaging-kg",
    "claude",
  ],
  prompts: [
    { label: "Prompt 1", text: "Use the neuroimaging-kg skill to build a knowledge graph for ABIDE I site Caltech — the phenotype table plus ReproNim's NIDM file with brain volumes — validate it, and load it into Oxigraph. Tell me in plain words what is in the graph.",
      expected: ["“Done — the graph built, validated, and loaded cleanly, with all 5 gated questions passing.”", "“38 participants from the Caltech site of ABIDE I”"], duration: "34 s" },
    { label: "Prompt 2", text: "How many Caltech participants have both a full-scale IQ (FIQ) score and a FreeSurfer hippocampal volume, by diagnostic group? Show the SPARQL query you used and explain it briefly.",
      expected: ["“18 autism-group participants (dx_group=1) and 19 control-group participants (dx_group=2)”"], duration: "14 s" },
    { label: "Prompt 3", text: "Trace participant 51456's left-hippocampus volume from FreeSurfer back to the scan and the software it came from. Say which links are recorded in the graph and which are only inferred.",
      expected: ["“fs:fs_003343 = 4513.9”", "“T1w scan ↔ FreeSurfer activity … Not recorded.”"], duration: "162 s" },
    { label: "Prompt 4", text: "If we tightened the head-motion rule to mean framewise displacement below 0.15 mm, which participants would be excluded, and which results in our graph depend on them?",
      expected: ["“51456 | autism | 0.1862 mm”", "“51469 | autism | 0.1559 mm”", "“17 autism / 19 control”"], duration: "55 s" },
  ],
  note: "Prompts and outputs are from a headless test (Claude Sonnet, 2026-10-15) recorded in the transcript; if the live run is slow (prompt 3 took 162 s), show the transcript instead.",
};


// ---------------------------------------------------------------- dataset footnotes
const D_CNP = "ds000030 (UCLA CNP), OpenNeuro, commit 4070b6e", D_CNPs = "ds000030 (UCLA CNP, commit 4070b6e)";
const D_AB = "ABIDE I (ABIDE Preprocessed, C-PAC)", D_S2 = "ReproNim simple2 NIDM (commit e0dff17)";
const D_REV = "74 ABIDE studies (SynthScholar review, 2026-10-15)", D_REVs = "74-study review (2026-10-15)";
const D_PUB = "AbstractAtlas (OHBM 2026), OpenAlex", D_KIM = "Kim et al. 2023 (UCLA cohort from ds000030)";
const DATA = {
  "The two example datasets": ["ds000030 (OpenNeuro, commit 4070b6e)", "ABIDE I (ABIDE Preprocessed)"],
  "A knowledge graph in four statements": [D_CNP],
  "Components of a dataset and a publication": [D_CNPs, D_AB, D_REVs],
  "Knowledge graph around a single participant": [D_AB, D_S2],
  "Linking a claim to its evaluation and cohort": [D_CNPs, D_KIM],
  "Exercise: evaluating claims against a source": [D_KIM],
  "Quotation checks and scientific entailment": [D_KIM],
  "Joining graphs through shared identifiers": ["ABIDE I", "simple2 NIDM (e0dff17)", "AbstractAtlas (OHBM 2026)", "OpenAlex", "Brain Researcher KG", D_REVs],
  "Harmonising graphs built by different people": [D_AB, D_S2],
  "Participant coverage by data element": [D_AB, D_S2],
  "ABIDE I: two analyses, two research questions": [D_AB],
  "ABIDE I: group differences and site-held-out prediction": [D_AB],
  "Exercise: consequences of a stricter motion threshold": [D_AB],
  "Dependency tracing after a QC revision": [D_AB],
  "Linking datasets, publications and abstracts": [D_PUB, D_REV],
  "Asking Claude about the literature graph": [D_REV],
  "Evaluation schemes in 74 ABIDE studies": [D_REV],
  "Live demo: building a graph in Claude Code": ["ABIDE I, Caltech site (ABIDE Preprocessed; ReproNim simple2 NIDM, commit e0dff17)"],
  "Live demo: querying and using the graph": ["ABIDE I, Caltech site (ABIDE Preprocessed; ReproNim simple2 NIDM, commit e0dff17)"],
  // backup
  "Poll: participant count in ds000030": [D_CNP],
  "Participant counts in ds000030 by scope": [D_CNPs, "Gorgolewski 2017 and Kim 2023 cohorts"],
  "Recomputing a derived score from source items": [D_CNP],
  "Checking agent outputs against the graph": [D_CNP],
  "Graph, search and Brain Researcher: a small comparison": [D_AB, "Brain Researcher KG"],
  "Scope of the ds000030 extraction": [D_CNP],
  "NIDM and PROV roles for each record": [D_CNP],
  "Requirements for joining behaviour to image-derived measures": [D_CNP],
  "Research questions and results of the three papers": [D_CNPs, "Poldrack 2016, Gorgolewski 2017, Kim 2023"],
  "StructSense extraction pilot": [D_CNPs, "Gorgolewski 2017, Kim 2023"],
  "Scan, events and phenotype details": [D_CNP],
  "Registration and cross-source joins": [D_CNPs, "Gorgolewski 2017"],
  "Provenance of a single phenotype measurement": [D_CNP],
  "AbstractAtlas: building blocks": ["AbstractAtlas (OHBM 2026)"],
  "Phenotype embedding linked to image-derived phenotypes": [D_AB],
  "ds000030 phenotype embedding from a graph query": [D_CNP],
};

// ---------------------------------------------------------------- "In the graph" strips (verified against the experiment code)
const STRIP = {
  "The two example datasets": "Counts read by SPARQL: ds000030 graph (combined_graph.ttl, 1,113,959 triples); ABIDE graph/core (queries/Q14.rq)",
  "A knowledge graph in four statements": "Path query over ds000030 nidm_phenotypes.ttl: record → bis_parcel1; wasGeneratedBy → session → qualifiedAssociation/agent → participant: 272 rows",
  "Components of a dataset and a publication": "Dataset side: ds000030 graph and ABIDE graph/core · publication side: claims_and_questions.ttl, literature_kg.ttl (17 / 74 reconstructible)",
  "Entities in a neuroimaging knowledge graph": "Node and edge types; teal = types used in our ds000030 and ABIDE graphs (assigned in the plan, not computed by a query)",
  "Knowledge graph around a single participant": "13 SPARQL queries (queries/Q13_*.rq) over graph/core, scope, view/volumes → 239 triples → figure: code/participant_ego.py",
  "Linking a claim to its evaluation and cohort": "ds000030 claims_and_questions.ttl: question → claim → evaluation → cohort; evidence re-run from the authors' OSF data (osf.io/agqtn) by kim2023_rerun/rerun_ucla_cpm.py",
  "Exercise: evaluating claims against a source": "Statement A is a claim record with its evidence span (claims_and_questions.ttl); B and C were written for this exercise and are not in the graph",
  "Quotation checks and scientific entailment": "Span and schema checks ran on the extracted records (results/skill/pilot_report.json); entailment is a human judgement, not in the graph",
  "Joining graphs through shared identifiers": "queries/simple2_identity.rq over graph/link + 27 simple2 site graphs; graph/publications.ttl (Q15.rq); literature_kg.ttl; Brain Researcher via MCP, not in our store",
  "Harmonising graphs built by different people": "Store with one named graph per source plus derived views with PROV (code/store.py); SHACL shapes code/shapes.ttl; LinkML check results/linkml_validation.json",
  "Participant coverage by data element": "SPARQL (queries/Q14.rq) over graph/core + view/volumes + ReproNim simple2 graphs → counts by site and diagnosis → figure: code/element_coverage.py",
  "ABIDE I: two analyses, two research questions": "Cohorts are prov:hadMember sets in graph/core (built by code/cohorts.py); overlap by queries/Q2.rq",
  "ABIDE I: group differences and site-held-out prediction": "Result, claim and review nodes in graph/core (code/analyst_a.py, analyst_b.py, reviews.py); reviews read by queries/Q6.rq, Q7.rq",
  "Exercise: consequences of a stricter motion threshold": "The motion rule is stored on each cohort definition in graph/core (ex:threshold 0.2 for v1, 0.15 for v2)",
  "Dependency tracing after a QC revision": "4 SPARQL queries (queries/revision_*.rq) over graph/core_v1 before recomputation (code/revision.py); after rerun: results/revision_impact.json",
  "Linking datasets, publications and abstracts": "graph/publications.ttl + publication_links_activity.ttl (queries/Q15.rq, Q15b.rq; code/publications.py); review counts from literature_kg.ttl",
  "Asking Claude about the literature graph": "literature_kg.ttl — ex:reportsPerformance, ex:evaluationScheme, ex:EvidenceQuote; query written and run by Claude Code",
  "Evaluation schemes in 74 ABIDE studies": "literature_review/literature_kg.ttl (10,779 triples); phase3/s5_sparql_checks.py confirms each count → figure: phase3/s6_figures.py",
  "ReproPond and ReproLake as attributes on graph records": "graph/scope.ttl: knowledgeScope and accessLevel on 83 records; consentScope, egressPermitted on 3 profiles; 48 gate assessments (Q11.rq, Q12.rq)",
  "Live demo: building a graph in Claude Code": "Demo graph: abide-caltech/graph/*.ttl (phenotype, identity links, cohort, claims, provenance) loaded into Oxigraph, validated",
  "Live demo: querying and using the graph": "SPARQL over the demo store's named graphs (urn:g:phenotype, urn:g:repronim, urn:g:cohort), as in the tested transcript",
  "The lecture's own provenance graph": "talk_provenance.ttl, written by slides/build_deck.js; query run with pyoxigraph (slides/prov_query.py)",
  "Practices to adopt now": "Each practice adds a record: dataset version, cohort membership list, claim scope, derivation activity, shared identifiers",
};

// ---------------------------------------------------------------- kinds of knowledge
// [group, kind, tile line, full standards line, populated in worked examples]
const KINDS = [
  ["What was studied", "Datasets and versions", "BIDS, DataLad, OpenNeuro, DCAT", "BIDS, DataLad, OpenNeuro/DANDI/NDA accessions, DCAT", true, "Datasets, versions"],
  ["What was studied", "Participants, phenotypes", "NIDM-Exp, ReproSchema", "NIDM-Experiment, ReproSchema, NIH CDEs, NDA data dictionary", true, "Participants"],
  ["What was studied", "Acquisitions, protocols", "BIDS sidecars, ReproIn, ReproStim", "BIDS sidecars, ReproIn, scanner/sequence parameters, ReproStim", true, "Acquisitions"],
  ["What was studied", "Tasks and constructs", "Cognitive Atlas, CogPO, events", "Cognitive Atlas, CogPO, task events", false, "Tasks, constructs"],
  ["How it was done", "Methods and software", "CodeMeta, containers, Boutiques", "CodeMeta/schema.org, containers (ReproNim/containers, Neurodocker), Boutiques", true, "Methods, software"],
  ["How it was done", "How to apply a method", "registration routes, QC checks", "Registration routes, compatible spaces, QC criteria, failure modes — skills with acceptance checks", true, "How to apply"],
  ["How it was done", "Templates and spaces", "TemplateFlow, atlases, transforms", "TemplateFlow (MNI152NLin2009cAsym, fsaverage), Julich/Allen, transform chains", false, "Templates, spaces"],
  ["How it was done", "Run provenance", "PROV, NIDM, DataLad run, BABS", "W3C PROV, NIDM, DataLad run records, ReproMan, BABS", true, "Run provenance"],
  ["How it was done", "Compute environments", "containers, HPC profiles, seeds", "Container images, HPC profiles, seeds (reproseed)", false, "Compute envs"],
  ["What was found", "Derivatives and IDPs", "BIDS-Derivatives, FS → NIDM", "BIDS-Derivatives, NIDM (FreeSurfer/ANTs/FSL → NIDM), MRIQC → NIDM", true, "Derived measures"],
  ["What was found", "Statistical results, maps", "NIDM-Results, NeuroVault", "NIDM-Results, NeuroVault, effect sizes with cohort", false, "Statistical maps"],
  ["What was found", "Questions, hypotheses", "preregistrations, question nodes", "Preregistrations, research-question nodes", true, "Questions"],
  ["What was found", "Claims, with scope", "population, measure, ECO", "Population, measure, contrast, evaluation; ECO evidence codes; nanopublications", true, "Scoped claims"],
  ["Who and in what context", "Publications", "DOI, PMID, quotes as locators", "DOI, PMID, sections and quotes as evidence locators", true, "Publications"],
  ["Who and in what context", "People and roles", "ORCID, ROR, CRediT, PROV roles", "ORCID, ROR, CRediT, PROV qualified roles", true, "People, roles"],
  ["Who and in what context", "Projects and funding", "NIH RePORTER grant IDs", "NIH RePORTER grant IDs", false, "Projects, funding"],
  ["Who and in what context", "Reviews and disputes", "who asserted what, and why", "Attributed assessments; who asserted what, on what evidence", true, "Reviews, disputes"],
  ["Who and in what context", "Resources and activity", "dated activity, with age", "Dated activity snapshots (commits, issues, citing papers) with age", true, "Resource activity"],
  ["Who and in what context", "Ontologies", "UBERON, InterLex, ECO, SIO", "UBERON, InterLex/NeuroNames, NCIT, EDAM, ECO, SIO, nidm-terms", true, "Ontologies"],
  ["Who and in what context", "Consent, use, licences", "DUO, data use agreements, CC0", "DUO, data use agreements, CC0/CC-BY", false, "Consent, licences"],
];

// ---------------------------------------------------------------- types of knowledge
// [kind, tile example, full example, where it lives (full), home column, secondary tag]
const TYPES = [
  ["Observations, facts", "TR = 2 s; mean FD = 0.18 mm", "TR = 2 s for this scan; mean FD = 0.18 mm", "Graph, with source", "graph", ""],
  ["Definitions", "SSRT quantile method; RAS+; MNI152", "SSRT computed by quantile method; RAS+; MNI152NLin2009cAsym", "Graph + ontology terms", "graph", "+ ontology"],
  ["Theories, hypotheses", "dysconnectivity in autism, with status", "Dysconnectivity hypothesis of autism", "Graph, as question/hypothesis with status", "graph", ""],
  ["Findings, claims", "under-connectivity, this cohort, this measure", "Under-connectivity in ASD, in this cohort, this measure", "Graph, scoped, with evidence", "graph", ""],
  ["Methods", "what tangent-space connectivity estimates", "What tangent-space connectivity estimates", "Graph + docs", "graph", "+ docs"],
  ["Local knowledge", "scanner B's phase-encoding quirk", "Scanner B's phase-encoding quirk; lab naming conventions", "Graph + skill, scoped to site", "graph", "+ skill"],
  ["Disagreement", "two reviewers differ on QC", "Two reviewers disagree on QC", "Graph, as separate attributed assessments", "graph", ""],
  ["Currency", "tool released 3 weeks ago, dated", "Tool last released 3 weeks ago", "Graph, dated snapshot with age", "graph", ""],
  ["Know-how", "register BOLD → T1 → template, then check", "How to register BOLD → T1 → template and check it", "Skill", "skill", ""],
  ["Best practices", "COBIDAS; preprocess inside CV folds", "COBIDAS; preprocessing inside CV folds", "Skill, citing the guideline", "skill", ""],
  ["Heuristics", "mean FD > 0.2 mm, with derivation and limits", "Exclude mean FD > 0.2 mm", "Skill parameter, with its derivation and limits", "skill", ""],
  ["Failure modes", "L–R flips, fold leakage, site confounds", "Left–right flips; leakage across folds; site confounds; double dipping", "Harness check / test", "harness", ""],
  ["Acceptance criteria", "score recomputes; source edge present", "Recomputed score matches; derivative has a source edge", "Harness check (SHACL, tests)", "harness", ""],
  ["Tacit judgement", "visual QC of a registration, attributed", "Visual QC of a registration", "Human review, recorded as an attributed assessment", "human", ""],
];

// ---------------------------------------------------------------- old deck notes
const OLD = fs.readFileSync(path.join(__dirname, "old_deck_v3.md"), "utf8").replace(
  "Kim tests whether increased connectivity adds information beyond decreased connectivity, and whether predictive features transfer.",
  "Kim asks which direction of connectivity change is associated with schizophrenia (aim, verbatim: 'we aimed to determine the direction of the connectivity alteration associated with schizophrenia using a multivariate, data-driven approach') and tests transfer across datasets. [Corrected 2026-10-15 after checking the source, https://www.frontiersin.org/articles/10.3389/fpsyt.2023.1232015/full: earlier paraphrases ('adds information beyond decreased connectivity', then 'do decreased and increased connectivity predict diagnosis') did not match the paper's stated aim.]");
function oldNotes(n) {
  const parts = OLD.split(/<!-- Slide number: (\d+) -->/);
  for (let i = 1; i < parts.length; i += 2) {
    if (Number(parts[i]) === n) {
      const m = parts[i + 1].split("### Notes:")[1];
      return m ? m.trim() : "";
    }
  }
  return "";
}
const fromOld = (...ns) => ns.map((n) => `[v3 slide ${n}] ${oldNotes(n)}`).join("\n\n");

// ---------------------------------------------------------------- theme
const THEME = {
  name: "Repronim Graph",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1F2A30", lt1: "FFFFFF", dk2: "17303F", lt2: "F3F6F6",
    accent1: "0F7B7B", accent2: "C0562B", accent3: "5E7A88", accent4: "DCEEEC",
    accent5: "F7E4DA", accent6: "E3E9EC", hlink: "0F7B7B", folHlink: "5E7A88",
  },
};
const HEX = THEME.colors;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.author = "Satrajit Ghosh";
pres.title = "Connecting neuroimaging knowledge graphs across data, publications and labs";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;
const W = 13.333;

// ---------------------------------------------------------------- layouts
pres.defineSlideMaster({
  title: "TITLE_DARK",
  background: { color: C.text2 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.0, w: 11.5, h: 1.9, fontSize: 40, bold: true, color: C.background1, valign: "bottom", align: "left" }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 4.1, w: 11.5, h: 2.4, fontSize: 20, color: C.background2, valign: "top", align: "left" }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTENT",
  background: { color: C.background1 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.24, w: 12.1, h: 0.78, fontSize: 32, bold: true, color: C.text2, valign: "middle", align: "left" }, text: "" } },
  ],
  slideNumber: { x: 12.35, y: 6.95, w: 0.6, h: 0.35, fontSize: 11, color: C.accent3, align: "right" },
});
pres.defineSlideMaster({
  title: "BACKUP",
  background: { color: C.background1 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.3, w: 10.6, h: 0.8, fontSize: 26, bold: true, color: C.text2, valign: "middle", align: "left" }, text: "" } },
    { text: { text: "Backup", options: { x: 11.3, y: 0.42, w: 1.45, h: 0.5, fontSize: 12, color: C.accent3, align: "right", italic: true } } },
  ],
  slideNumber: { x: 12.35, y: 6.95, w: 0.6, h: 0.35, fontSize: 11, color: C.accent3, align: "right" },
});

// ---------------------------------------------------------------- helpers
let n = 0;
function card(slide, x, y, w, h, fill, text, opts = {}) {
  n += 1;
  slide.addText(text, {
    shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.08, x, y, w, h,
    fill: { color: fill }, line: opts.line ? { color: opts.line, width: opts.lineWidth || 1.5, dashType: opts.dash || "solid" } : { type: "none" },
    fontSize: opts.fontSize || 18, color: opts.color || C.text1, bold: !!opts.bold,
    align: opts.align || "left", valign: opts.valign || "middle", margin: opts.margin ?? 10,
    isTextBox: true, objectName: opts.name || `card${n}`,
    shadow: opts.shadow ? { type: "outer", color: "9AA8AF", opacity: 0.35, blur: 4, offset: 2, angle: 90 } : undefined,
  });
}
function shp(slide, kind, x, y, w, h, fill, t, opts = {}) {
  n += 1;
  const o = {
    x, y, w, h, fill: fill ? { color: fill, transparency: opts.transparency || 0 } : { type: "none" },
    line: opts.line ? { color: opts.line, width: opts.lineWidth || 1.5, dashType: opts.dash || "solid" } : { type: "none" },
    fontSize: opts.fontSize || 18, color: opts.color || C.text1, bold: !!opts.bold,
    align: opts.align || "center", valign: opts.valign || "middle", margin: opts.margin ?? 4,
    objectName: opts.name || `shape${n}`, flipH: !!opts.flipH, rotate: opts.rotate,
  };
  if (opts.angleRange) o.angleRange = opts.angleRange;
  if (opts.arcThicknessRatio) o.arcThicknessRatio = opts.arcThicknessRatio;
  if (opts.points) o.points = opts.points;
  if (kind === pres.shapes.ROUNDED_RECTANGLE) o.rectRadius = opts.rectRadius ?? 0.5;
  if (t === undefined || t === null || t === "") slide.addShape(kind, o);
  else slide.addText(t, { shape: kind, isTextBox: true, ...o });
}
function blob(slide, x, y, w, h, fill, seed = 1, opts = {}) {
  // smooth irregular closed outline (Catmull-Rom → cubic Bézier), coordinates relative to the box
  const N = 9, pts = [];
  let r = seed * 9301 + 49297;
  const rnd = () => { r = (r * 9301 + 49297) % 233280; return r / 233280; };
  for (let k = 0; k < N; k++) {
    const a = (k / N) * 2 * Math.PI, j = 0.86 + 0.14 * rnd();
    pts.push([w / 2 + (w / 2) * j * Math.cos(a), h / 2 + (h / 2) * j * Math.sin(a)]);
  }
  const P = (i) => pts[(i + N) % N];
  const path = [{ x: P(0)[0], y: P(0)[1], moveTo: true }];
  for (let i = 0; i < N; i++) {
    const p0 = P(i - 1), p1 = P(i), p2 = P(i + 1), p3 = P(i + 2);
    path.push({ x: p2[0], y: p2[1], curve: { type: "cubic", x1: p1[0] + (p2[0] - p0[0]) / 6, y1: p1[1] + (p2[1] - p0[1]) / 6, x2: p2[0] - (p3[0] - p1[0]) / 6, y2: p2[1] - (p3[1] - p1[1]) / 6 } });
  }
  path.push({ close: true });
  shp(slide, pres.shapes.CUSTOM_GEOMETRY, x, y, w, h, fill, null, { points: path, line: opts.line, lineWidth: opts.lineWidth });
}
function curve(slide, x1, y1, x2, y2, opts = {}) {
  // cubic S-curve from (x1,y1) to (x2,y2)
  n += 1;
  const x = Math.min(x1, x2), y = Math.min(y1, y2), w = Math.abs(x2 - x1) || 0.01, h = (Math.abs(y2 - y1) || 0.01) + (opts.bow || 0);
  const sx = x1 - x, sy = y1 - y, ex = x2 - x, ey = y2 - y;
  slide.addShape(pres.shapes.CUSTOM_GEOMETRY, {
    x, y, w, h, fill: { type: "none" },
    line: { color: opts.color || C.accent3, width: opts.width || 2, dashType: opts.dash || "solid", endArrowType: opts.arrow ? "triangle" : undefined, beginArrowType: opts.beginArrow ? "triangle" : undefined },
    points: opts.bow
      ? [{ x: sx, y: sy, moveTo: true }, { x: ex, y: ey, curve: { type: "cubic", x1: sx, y1: sy + opts.bow, x2: ex, y2: ey + opts.bow } }]
      : [{ x: sx, y: sy, moveTo: true }, { x: ex, y: ey, curve: { type: "cubic", x1: sx + (ex - sx) * 0.5, y1: sy, x2: sx + (ex - sx) * 0.5, y2: ey } }],
    objectName: `curve${n}`,
  });
}
function text(slide, t, x, y, w, h, opts = {}) {
  n += 1;
  slide.addText(t, { x, y, w, h, fontSize: 18, color: C.text1, valign: "top", margin: 0, isTextBox: true, objectName: `text${n}`, ...opts });
}
function arrow(slide, x1, y1, x2, y2, opts = {}) {
  n += 1;
  slide.addShape(pres.shapes.LINE, {
    x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1) || 0.001, h: Math.abs(y2 - y1) || 0.001,
    flipH: x2 < x1, flipV: y2 < y1,
    line: { color: opts.color || C.accent3, width: opts.width || 2, endArrowType: "triangle", dashType: opts.dash || "solid" },
    objectName: `arrow${n}`,
  });
}
function edgeLabel(slide, t, x, y, w = 1.6, opts = {}) {
  text(slide, t, x, y, w, 0.4, { fontSize: 16, italic: true, color: opts.color || C.accent3, align: "center", valign: "middle" });
}
function table(slide, rows, opts = {}) {
  const fs_ = opts.fontSize || 13;
  const body = rows.map((r, i) => r.map((c) => ({
    text: c,
    options: i === 0
      ? { bold: true, color: C.background1, fill: { color: C.accent1 }, fontSize: fs_ }
      : { color: C.text1, fill: { color: i % 2 ? C.background1 : C.background2 }, fontSize: fs_ },
  })));
  slide.addTable(body, {
    x: opts.x ?? 0.6, y: opts.y ?? 1.35, w: opts.w ?? 12.1, colW: opts.colW, rowH: opts.rowH,
    border: { type: "solid", pt: 0.5, color: "D5DDE0" }, margin: 4, valign: "middle",
  });
}
async function icon(Comp, color = "#FFFFFF", size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color, size }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}
const SLIDES = [];
async function fitImage(slide, file, x, y, maxW, maxH, align = "center") {
  const m = await sharp(file).metadata();
  const r = m.width / m.height;
  let w = maxW, h = maxW / r;
  if (h > maxH) { h = maxH; w = maxH * r; }
  const ox = align === "left" ? 0 : (maxW - w) / 2;
  n += 1;
  slide.addImage({ path: file, altText: path.basename(file), x: x + ox, y: y + (maxH - h) / 2, w, h, objectName: `fig${n}` });
}
function addSlide(master, section) {
  const sl = pres.addSlide({ masterName: master, sectionTitle: section });
  const rec = { slide: sl, master, section, title: null };
  const orig = sl.addText.bind(sl);
  sl.addText = (t, o) => { if (o && o.placeholder === "title" && rec.title === null) rec.title = t; return orig(t, o); };
  SLIDES.push(rec);
  return sl;
}
const isPending = (v) => typeof v === "string" && v.includes(PENDING);

// ---------------------------------------------------------------- build
async function main() {
  const MAIN = "Main talk";
  const BACK = "Backup";
  pres.addSection({ title: MAIN });

  // 1 Title
  {
    const s = addSlide("TITLE_DARK", MAIN);
    s.addText("Connecting neuroimaging knowledge graphs across data, publications and labs", { placeholder: "title" });
    s.addText([
      { text: "Worked examples on ds000030 and ABIDE I", options: { breakLine: true } },
      { text: " ", options: { breakLine: true, fontSize: 12 } },
      { text: "Satrajit Ghosh", options: { breakLine: true, bold: true, fontSize: 18 } },
      { text: "ReproNim / LLM symposium · 25 minutes + discussion", options: { fontSize: 18 } },
    ], { placeholder: "body" });
    // badge key
    const LX = 6.95, CX = 10.75;
    text(s, "How each slide was made", LX, 4.35, 5.9, 0.4, { fontSize: 15, bold: true, color: "FFFFFF", valign: "middle" });
    text(s, "Production", LX, 4.8, 3.5, 0.3, { fontSize: 12, bold: true, color: "C9D3D7", valign: "middle" });
    const prodGloss = { H: "written by the speaker", L: "drafted by an LLM, edited by the speaker", A: "computed by an agent running code", R: "retrieved by an agent from cited sources", M: "answered by an external agent via MCP (Brain Researcher)", P: "produced earlier by a different agentic system" };
    let py = 5.12;
    for (const L of ["H", "L", "A", "R", "M", "P"]) {
      const h = L === "M" ? 0.42 : 0.3;
      s.addText(L, { shape: pres.shapes.OVAL, x: LX, y: py + 0.02, w: 0.26, h: 0.26, fill: { color: "2F4A57" }, line: { type: "none" }, fontSize: 11, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: `keyChip${L}` });
      text(s, prodGloss[L], LX + 0.34, py - 0.02, 3.35, h, { fontSize: 12, color: "DCEEEC", valign: "top" });
      py += h;
    }
    text(s, "Checking", CX, 4.8, 2.2, 0.3, { fontSize: 12, bold: true, color: "C9D3D7", valign: "middle" });
    let cy = 5.12;
    [["re-run", "recomputed independently", 0.47], ["validated", "passed automated checks", 0.47], ["reviewed", "read and corrected by the speaker", 0.64], ["unverified", "not independently checked", 0.47]].forEach(([w, g, h]) => {
      text(s, [{ text: w, options: { italic: true, bold: true, color: "FFFFFF", breakLine: true } }, { text: g, options: { color: "DCEEEC" } }], CX, cy, 2.3, h, { fontSize: 12, valign: "top" });
      cy += h;
    });
    s.addNotes("0:20. " + "Every term is explained on the slide where it first appears, and a full glossary is in backup. Two worked examples run in the background: a pinned OpenNeuro dataset (ds000030) joined to three papers, and ABIDE I with two simulated collaborators. Both are packaged with code and graphs; the talk uses them as evidence, not as the topic.\n\n" + fromOld(1));
  }

  // 2 Learning objectives
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Learning objectives", { placeholder: "title" });
    text(s, "By the end of this talk, you should be able to:", 0.75, 1.3, 11.5, 0.5, { fontSize: 22, color: C.text1, valign: "middle" });
    const objs = [
      ["1", "Represent a neuroimaging result as a knowledge graph", "linking the research question, the claim and its scope, the participants and derived measures it relies on, and the source data", 0.75, 2.0, C.accent1],
      ["2", "Connect information across knowledge graphs", "joining your data with public datasets, publications, tools and collaborators' work through shared identifiers and vocabularies, and deciding what can leave your lab", 1.6, 4.55, C.text2],
    ];
    objs.forEach(([num, head, sub, x, y, col]) => {
      shp(s, pres.shapes.DONUT, x, y, 2.3, 2.3, col);
      text(s, num, x, y, 2.3, 2.3, { fontSize: 62, bold: true, color: col, align: "center", valign: "middle" });
      text(s, [
        { text: head, options: { bold: true, fontSize: 28, color: C.text2, breakLine: true } },
        { text: sub, options: { fontSize: 19, color: C.accent3 } },
      ], x + 2.5, y + 0.1, 12.85 - (x + 2.5), 2.1, { valign: "middle", paraSpaceAfter: 8 });
    });
    s.addNotes("0:40. Two objectives, both tied to the title. First, represent a neuroimaging result as a knowledge graph: the research question, the claim and its scope, the participants and derived measures it relies on, and the source data, each linked so that the result can be traced back to data and evidence by a colleague or an AI assistant. NIDM and PROV give these links standard names, but the habit of recording them matters more than the vocabulary. Second, connect information across knowledge graphs, which is the connecting in the title: join your lab's graph to public datasets, publications, tools and collaborators' work through shared identifiers (participant IDs, DOIs, ORCIDs, repository URLs) and shared vocabularies (nidm-terms, InterLex, UBERON), and decide what can leave your lab. A shared identifier makes a join possible; it does not make two measurements the same, so joined information still has to be verified before it is used. The ReproPond/ReproLake and joining-graphs slides show both sides.");
  }


  // N0 The two example datasets
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("The two example datasets", { placeholder: "title" });
    const panel = (x, fill, accent, name, full, facts, papers, used) => {
      shp(s, pres.shapes.ROUNDED_RECTANGLE, x, 1.4, 6.05, 5.55, fill, null, { rectRadius: 0.3 });
      text(s, [{ text: name, options: { bold: true, fontSize: 26, color: accent, breakLine: true } }, { text: full, options: { fontSize: 16, color: C.text1 } }], x + 0.3, 1.55, 5.5, 1.0, { valign: "top" });
      s.addText(facts.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < facts.length - 1 } })), { x: x + 0.3, y: 2.65, w: 5.5, h: 2.15, fontSize: 16, color: C.text1, valign: "top", paraSpaceAfter: 4, margin: 0, isTextBox: true, objectName: `dsFacts${x}` });
      text(s, "Papers used here", x + 0.3, 4.85, 5.5, 0.35, { fontSize: 15, bold: true, color: accent });
      s.addText(papers.map((t, i) => ({ text: t, options: { breakLine: i < papers.length - 1 } })), { x: x + 0.3, y: 5.2, w: 5.5, h: 1.0, fontSize: 15, color: C.text1, valign: "top", margin: 0, isTextBox: true, objectName: `dsPapers${x}` });
      shp(s, pres.shapes.ROUNDED_RECTANGLE, x + 0.3, 6.3, 5.45, 0.45, C.background1, used, { fontSize: 15, bold: true, color: accent, rectRadius: 0.5 });
    };
    panel(0.5, C.accent4, C.accent1, "ds000030", "UCLA Consortium for Neuropsychiatric Phenomics · OpenNeuro, commit 4070b6e, CC0",
      [`${V("ds.total")} adults: ${V("ds.control")} controls, ${V("ds.schz")} schizophrenia, ${V("ds.bipolar")} bipolar disorder, ${V("ds.adhd")} ADHD`, "structural MRI, resting and task fMRI (e.g. stop-signal)", "52 questionnaire and phenotype tables"],
      ["Poldrack et al. 2016: data descriptor", "Gorgolewski et al. 2017: preprocessed derivatives", "Kim et al. 2023: prediction across UCLA and COBRE"],
      "Used in Part 1: representing a result");
    panel(6.8, C.accent5, C.accent2, "ABIDE I", "Autism Brain Imaging Data Exchange · ABIDE Preprocessed (C-PAC), CC BY-NC-SA",
      [`${V("abide.total")} participants (${V("abide.asd")} autistic, ${V("abide.td")} typically developing) from 17 sites`, "resting-state fMRI; phenotypes incl. IQ, ADOS, SRS", `200-region time series for ${V("abide.timeseries")} participants`],
      ["Di Martino et al. 2014: group differences", "Abraham et al. 2017: site-held-out prediction", "a 74-study literature review"],
      "Used in Part 2 and the live demo (one site)");
    s.addNotes("0:45. Two public datasets carry every example. ds000030 is the UCLA Consortium for Neuropsychiatric Phenomics dataset on OpenNeuro (commit 4070b6e, CC0 licence): 272 adults, 130 healthy controls, 50 with schizophrenia, 49 with bipolar disorder and 43 with ADHD, with structural MRI, resting and task fMRI such as the stop-signal task, and 52 questionnaire and phenotype tables. We use it with three papers: the data descriptor (Poldrack et al. 2016), the preprocessed derivatives (Gorgolewski et al. 2017) and a prediction study across the UCLA and COBRE cohorts (Kim et al. 2023). It carries Part 1, representing a result. ABIDE I is the Autism Brain Imaging Data Exchange: 1,112 participants, 539 autistic and 573 typically developing, from 17 sites (20 site codes in the data), with resting-state fMRI and phenotypes including IQ, the ADOS clinician assessment and the Social Responsiveness Scale. ABIDE Preprocessed provides C-PAC-processed 200-region time series for 1,035 of them (CC BY-NC-SA licence). We use it with Di Martino et al. 2014 (group differences), Abraham et al. 2017 (prediction at held-out sites) and a review of 74 ABIDE studies; it carries Part 2, connecting graphs, and the live demo uses one site. Counts are from the ds000030 package (rebuilt and matched) and ABIDE results/key_numbers.json and element_coverage.json.");
  }

  // N1 Knowledge graph primer
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("A knowledge graph in four statements", { placeholder: "title" });
    const node = (x, y, w, h, fill, main, sub, col) => shp(s, pres.shapes.OVAL, x, y, w, h, fill, [
      { text: main, options: { bold: true, fontSize: 18, breakLine: !!sub } }, ...(sub ? [{ text: sub, options: { fontSize: 13, bold: false, color: col ? C.accent4 : C.accent3 } }] : []),
    ], { color: col || C.text2, margin: 4 });
    const lab = (t, sub, x, y, w, align = "center") => text(s, [{ text: t, options: { italic: true, fontSize: 16, color: C.accent1, breakLine: true } }, { text: sub, options: { fontSize: 12, color: C.accent3 } }], x, y, w, 0.62, { align, valign: "middle" });
    node(0.55, 2.0, 1.75, 1.15, C.accent4, "2.0", "‘acts impulsively’");
    node(4.45, 2.0, 3.1, 1.15, C.accent4, "questionnaire record", "nidm:AcquisitionObject");
    node(9.05, 1.4, 3.8, 1.15, C.accent4, "Barratt questionnaire session", "nidm:Acquisition");
    node(10.25, 3.3, 1.5, 1.2, C.text2, "sub-10159", "participant", C.background1);
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 4.6, 3.65, 2.8, 0.78, C.background2, [{ text: "barratt.tsv, row 2", options: { bold: true, fontSize: 16, breakLine: true } }, { text: "Barratt Impulsiveness Scale answers", options: { fontSize: 12, color: C.accent3 } }], { line: "C9D3D7", rectRadius: 0.2 });
    arrow(s, 4.45, 2.57, 2.3, 2.57, { color: C.accent1, width: 2.5 });
    lab("‘acts impulsively’ score", "bis_parcel1", 2.25, 1.55, 2.3);
    curve(s, 7.55, 2.3, 9.05, 1.97, { arrow: true, width: 2.5, color: C.accent1 });
    lab("was generated by", "prov:wasGeneratedBy", 7.2, 1.3, 2.0);
    arrow(s, 11.0, 2.55, 11.0, 3.3, { color: C.accent1, width: 2.5 });
    lab("with participant", "prov:qualifiedAssociation · agent, role: subject", 7.55, 2.65, 3.35, "right");
    arrow(s, 6.0, 3.15, 6.0, 3.65, { color: C.accent3, width: 1.5 });
    text(s, [{ text: "was derived from ", options: { italic: true, fontSize: 14, color: C.accent3 } }, { text: "prov:wasDerivedFrom", options: { fontSize: 12, color: C.accent3 } }], 6.1, 3.22, 3.0, 0.35, { valign: "middle" });
    text(s, "Barratt items 17 ‘I act on impulse’ and 19 ‘I act on the spur of the moment’ were each answered 2 (occasionally); their mean is the ‘acts impulsively’ score.", 0.55, 3.35, 3.85, 1.1, { fontSize: 13, color: C.accent3, valign: "top" });
    // query pattern along the same path
    text(s, "A query", 0.55, 4.7, 1.2, 0.6, { fontSize: 18, bold: true, color: C.text2, valign: "middle" });
    const blank = (x, w, t) => shp(s, pres.shapes.OVAL, x, 4.68, w, 0.64, C.background1, t, { fontSize: 16, italic: true, color: C.accent2, line: C.accent2, dash: "dash" });
    blank(1.75, 0.9, "?x"); blank(3.6, 1.55, "?record"); blank(6.45, 1.55, "?session"); blank(9.3, 1.9, "?participant");
    arrow(s, 3.6, 5.0, 2.65, 5.0, { color: C.accent1, width: 2 }); arrow(s, 5.15, 5.0, 6.45, 5.0, { color: C.accent1, width: 2 }); arrow(s, 8.0, 5.0, 9.3, 5.0, { color: C.accent1, width: 2 });
    text(s, "score", 2.6, 4.45, 1.05, 0.3, { fontSize: 13, italic: true, color: C.accent1, align: "center" });
    text(s, "generated by", 5.05, 4.45, 1.5, 0.3, { fontSize: 13, italic: true, color: C.accent1, align: "center" });
    text(s, "with participant", 7.85, 4.45, 1.6, 0.3, { fontSize: 13, italic: true, color: C.accent1, align: "center" });
    text(s, `→ ${V("ds.total")} participants and their scores`, 11.25, 4.6, 1.75, 0.8, { fontSize: 14, color: C.text1, valign: "middle" });
    const gl = [["Triple", "one statement: subject, relation, object"], ["Identifier", "a name that means one thing everywhere (sub-10159, a DOI)"], ["Vocabulary", "agreed names for relations and types (NIDM, PROV)"], ["Query", "a statement pattern with blanks (SPARQL)"]];
    gl.forEach(([k, v], i) => shp(s, pres.shapes.ROUNDED_RECTANGLE, 0.5 + i * 3.1, 5.75, 2.95, 1.15, C.background2, [
      { text: k, options: { bold: true, fontSize: 16, color: C.text2, breakLine: true } }, { text: v, options: { fontSize: 14, color: C.text1 } },
    ], { align: "left", margin: 8, line: "C9D3D7", rectRadius: 0.2 }));
    s.addNotes("1:15. A knowledge graph is a set of statements, each with three parts: a subject, a relation and an object; that unit is called a triple. This is how the ds000030 graph actually records one questionnaire score, in four statements. A questionnaire record has the 'acts impulsively' score 2.0 (the variable bis_parcel1). The record was generated by a Barratt questionnaire session (in NIDM, an acquisition). That session was carried out with participant sub-10159, who has the role of subject (in PROV, a qualified association with an agent). And the record was derived from row 2 of barratt.tsv. The participant is two steps away from the score, not attached to it directly: that is how the graph keeps the measurement, the session it came from and the person separate. An identifier is a name that means the same thing everywhere, such as a participant ID or a DOI; a vocabulary is an agreed set of names for relations and types, such as NIDM for neuroimaging records and PROV for where things came from. A query is the same path with blanks: find any record with an 'acts impulsively' score ?x, generated by some session ?session, carried out with some participant ?participant. Run on the ds000030 graph (results/nidm_phenotypes.ttl) it returns all 272 participants and their scores; for sub-10159 it returns 2.0 from barratt.tsv row 2. SPARQL is the standard language for writing such patterns.");
  }

  // 4c2 Components of a dataset and a publication
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Components of a dataset and a publication", { placeholder: "title" });
    const DS = [
      ["Participants and phenotypes", `${V("ds.total")} participants; 52 tables, 1,983 columns`],
      ["Data dictionary", "'acts impulsively' = mean of Barratt items 17 and 19"],
      ["Scan sidecars", "sub-10159 BOLD: TR 2 s, TE 0.03 s, 3 T, scanner 35343"],
      ["Task events", "stop-signal task: 96 go, 32 stop trials, 128 rest intervals"],
      ["File inventory", "2,531 file pointers"],
      ["Derivatives", "questionnaire scores; 200-region time series (C-PAC)"],
      ["Release and version", "ds000030 commit 4070b6e; ABIDE Preprocessed"],
    ];
    const PUB = [
      ["Research question", "Kim 2023: which direction of connectivity change is associated with schizophrenia?"],
      ["Cohort and exclusions", "Kim 2023: 47 patients + 47 controls; Abraham 2017: 871 of 1,112"],
      ["Preprocessing and versions", "fMRIPrep: fMRI to anatomy (FreeSurfer 6.0.0), anatomy to MNI template (ANTs 2.1.0)"],
      ["Analysis and evaluation", "linear classifier; leave-one-participant-out, leave-site-out"],
      ["Results and claims, with scope", "both directions altered; evidence 70.2% accuracy, UCLA, leave-one-out"],
      ["Data and code availability", "cohorts reconstructible for only 17 of 74 ABIDE studies"],
    ];
    text(s, "Dataset", 0.5, 1.3, 4.9, 0.4, { fontSize: 20, bold: true, color: C.text2 });
    text(s, "Publication", 8.0, 1.3, 4.85, 0.4, { fontSize: 20, bold: true, color: C.accent2, align: "right" });
    DS.forEach(([k, v], i) => {
      const x = 0.4 + 0.15 * Math.sin((i / (DS.length - 1)) * Math.PI);
      shp(s, pres.shapes.ROUNDED_RECTANGLE, x, 1.8 + i * 0.75, 4.95, 0.68, C.accent4, [
        { text: k, options: { bold: true, fontSize: 16, color: C.text2, breakLine: true } },
        { text: v, options: { fontSize: 14, color: C.text1 } },
      ], { align: "left", margin: 8, rectRadius: 0.5 });
    });
    PUB.forEach(([k, v], i) => {
      const x = 7.9 - 0.15 * Math.sin((i / (PUB.length - 1)) * Math.PI);
      shp(s, pres.shapes.ROUNDED_RECTANGLE, x, 1.8 + i * 0.875, 5.05, 0.78, C.accent5, [
        { text: k, options: { bold: true, fontSize: 16, color: C.text2, breakLine: true } },
        { text: v, options: { fontSize: 14, color: C.text1 } },
      ], { align: "left", margin: 8, rectRadius: 0.5 });
    });
    shp(s, pres.shapes.OVAL, 5.68, 2.45, 1.95, 3.9, C.text2, null);
    text(s, "Linked by", 5.68, 2.8, 1.95, 0.4, { fontSize: 16, bold: true, color: C.background1, align: "center" });
    ["participant IDs", "accession and version", "cohort definition"].forEach((t, i) =>
      shp(s, pres.shapes.ROUNDED_RECTANGLE, 5.82, 3.3 + i * 0.78, 1.67, 0.64, C.background1, t, { fontSize: 14, bold: true, color: C.text2, margin: 4 }));
    s.addNotes("1:15. Terms: ds000030 is the UCLA Consortium for Neuropsychiatric Phenomics dataset on OpenNeuro; the Barratt Impulsiveness Scale is a 30-item impulsivity questionnaire; a scan sidecar is the BIDS JSON file of acquisition parameters; C-PAC and fMRIPrep are preprocessing pipelines; BBR and ANTs SyN are registration methods to anatomy and to the MNI template. Concrete components, each with an example already in this talk. A dataset is more than its images: participant and phenotype tables (272 participants; 52 tables and 1,983 columns in ds000030), a data dictionary that defines derived scores (the 'acts impulsively' score bis_parcel1 is the mean of Barratt items 17 and 19, stored on each participant's questionnaire record), scan sidecars (sub-10159's resting BOLD: TR 2 s, TE 0.03 s, 3 T, scanner 35343), task event files (256 rows), a file inventory (2,531 pointers), derivatives (Barratt scores; CC200 time series from C-PAC) and a release version (commit 4070b6e; ABIDE Preprocessed). A publication has its own components: the research question, the cohort and its exclusions (Kim 2023, 47 + 47; Abraham 2017, 871 of ABIDE I's 1,112), preprocessing with versions (Gorgolewski 2017: FMRIPREP with FreeSurfer 6.0.0 BBR and ANTs 2.1.0 SyN to MNI152NLin2009cAsym), the analysis and evaluation scheme, scoped results (70.2% UCLA leave-one-out) and data and code availability; in our review, only 17 of 74 ABIDE studies had reconstructible cohorts. What links the two sides is participant IDs, the dataset accession and version, and the cohort definition, which is what the joining slide uses. Details are in the backup slides on the ds000030 extraction, the papers' research questions, and scan, event and phenotype details.");
  }

  // 4b What a neuroimaging graph can hold
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Entities in a neuroimaging knowledge graph", { placeholder: "title" });
    const cx = 6.67, cy = 4.15, R = 1.75;
    const groups = [...new Set(KINDS.map((k) => k[0]))];
    const arcCol = [C.text2, C.accent3, C.accent2, "8EA4AE"];
    const labCol = [C.text2, C.accent3, C.accent2, C.text1];
    const ranges = [[182, 268], [272, 358], [2, 88], [92, 178]]; // TL, TR, BR, BL
    const clusterOf = [0, 1, 2, 3]; // studied TL, how TR, found BR, context BL
    groups.forEach((g, gi) => {
      shp(s, pres.shapes.BLOCK_ARC, cx - R, cy - R, 2 * R, 2 * R, arcCol[gi], null, { angleRange: ranges[gi], arcThicknessRatio: 0.28 });
    });
    shp(s, pres.shapes.OVAL, cx - 0.95, cy - 0.95, 1.9, 1.9, C.background2, [
      { text: "participant", options: { bold: true, breakLine: true } }, { text: "·", options: { breakLine: true } }, { text: "dataset", options: { bold: true } },
    ], { fontSize: 18, color: C.text2, line: "C9D3D7" });
    const pillW = 2.12, pillH = 0.46, gx = 0.08, gy = 0.07;
    const anchor = [
      { x: 0.5, y: 1.75, cols: 2, label: [0.5, 1.3] },
      { x: 8.55, y: 1.75, cols: 2, label: [8.55, 1.3] },
      { x: 8.55, y: 5.0, cols: 2, label: [8.55, 4.55] },
      { x: 0.5, y: 4.85, cols: 2, label: [0.5, 4.4] },
    ];
    groups.forEach((g, gi) => {
      const a = anchor[gi];
      text(s, g, a.label[0], a.label[1], 4.3, 0.4, { fontSize: 18, bold: true, color: labCol[gi], valign: "middle" });
      KINDS.filter((k) => k[0] === g).forEach((k, ki) => {
        const col = ki % a.cols, row = Math.floor(ki / a.cols);
        const on = k[4];
        shp(s, pres.shapes.ROUNDED_RECTANGLE, a.x + col * (pillW + gx), a.y + row * (pillH + gy), pillW, pillH, on ? C.accent1 : C.background2, k[5], {
          fontSize: 16, bold: true, color: on ? C.background1 : C.text2, line: on ? undefined : "C9D3D7", margin: 2,
        });
      });
    });
    shp(s, pres.shapes.OVAL, 5.05, 6.38, 0.3, 0.3, C.accent1);
    text(s, "teal = in the worked examples", 5.45, 6.33, 3.0, 0.4, { fontSize: 16, color: C.accent3, valign: "middle" });
    text(s, "Which of these does your lab already write down?", 8.55, 6.25, 4.3, 0.8, { fontSize: 18, italic: true, color: C.accent2, valign: "middle" });
    s.addNotes("0:45. Twenty kinds of neuroimaging knowledge, in four groups: what was studied (datasets, participants, acquisitions, tasks), how it was done (methods, procedures, spaces, provenance, environments), what was found (derivatives, results, questions, scoped claims) and who and in what context (papers, people, funding, reviews, resource activity, vocabularies, governance). Short names are on the slide; standards and examples for each are in the backup table. Teal tiles are populated in the ds000030 and ABIDE packages; grey ones are not. 'How to apply a method' is distinct from the method itself: for registration, the graph holds the route (functional → T1 → MNI152NLin2009cAsym), compatible spaces and per-case QC checks (see the backup registration slide). Atlases and templates are best referenced by TemplateFlow identifiers. A graph is only as good as what someone wrote down: each tile is a habit before it is a technology. Ask: which of these does your lab already write down?");
  }


  // 5 Participant ego graph
  {
    const PA = ABIDE.participant;
    const s = addSlide("CONTENT", MAIN);
    s.addText(PA.title, { placeholder: "title" });
    const LCOL = [C.accent1, C.text2, C.accent3, C.accent2, "8EA4AE", "5FA8A9", "D98C6A", "2F5D6E"];
    if (PA.figure) {
      await fitImage(s, PA.figure, 0.4, 1.35, 8.9, 5.65);
    } else {
      const cx = 4.8, cy = 4.25;
      PA.layers.forEach((L, i) => {
        const a = (i / PA.layers.length) * 2 * Math.PI - Math.PI / 2;
        const x = cx + 3.4 * Math.cos(a), y = cy + 2.3 * Math.sin(a);
        curve(s, cx, cy, x, y, { color: "C9D3D7", width: 1.5 });
        shp(s, pres.shapes.OVAL, x - 0.5, y - 0.5, 1.0, 1.0, LCOL[i], null, { transparency: 20 });
      });
      shp(s, pres.shapes.OVAL, cx - 0.9, cy - 0.9, 1.8, 1.8, C.background1, [{ text: "participant", options: { fontSize: 16, breakLine: true } }, { text: PA.id, options: { fontSize: 18, bold: true } }], { color: C.text2, line: C.text2, lineWidth: 2 });
    }
    text(s, "Layers", 9.5, 1.45, 3.3, 0.45, { fontSize: 20, bold: true, color: C.text2 });
    PA.layers.forEach((L, i) => {
      const y = 2.0 + i * 0.62;
      shp(s, pres.shapes.OVAL, 9.5, y + 0.1, 0.34, 0.34, LCOL[i]);
      text(s, [{ text: L.name, options: { bold: true, color: C.text2 } }, { text: "  " + L.count, options: { color: C.accent3 } }], 9.95, y, 3.0, 0.55, { fontSize: 16, valign: "middle" });
    });
    s.addNotes("1:00. Terms: an image-derived phenotype is a measurement computed from images, such as a regional brain volume; a cross-validation fold is one train/test split. One ABIDE participant, with every layer the graph holds about them: phenotype values, acquisition and QC records, derivatives, image-derived phenotypes by tool, membership in each analyst's cohort and cross-validation folds, the results that depend on them, the publication that used the cohort, and the consent scope that governs what can be shared. This replaces the single-measurement view from ds000030, which is in backup. " + PA.notes);
  }

  // 7 Claim chain
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Linking a claim to its evaluation and cohort", { placeholder: "title" });
    const w = 2.8, h = 1.85;
    const node = (x, y, k, v, hl) => shp(s, pres.shapes.OVAL, x, y, w, h, hl ? C.accent1 : C.accent4, [
      { text: k, options: { bold: true, fontSize: 16, color: hl ? C.accent4 : C.accent3, breakLine: true } },
      { text: v, options: { fontSize: 18, color: hl ? C.background1 : C.text1, bold: !!hl } },
    ], { margin: 4 });
    const P = [[0.45, 1.5], [3.55, 2.45], [6.65, 1.5], [9.75, 2.45]];
    node(...P[0], "Question · Kim 2023", "Does increased connectivity add information about schizophrenia?");
    text(s, "resting-state fMRI · 268-region atlas · patients vs controls", 0.3, 3.4, 3.2, 0.5, { fontSize: 14, italic: true, color: C.text2, align: "center" });
    node(...P[1], "Claim", "Yes: increased + decreased together classify best", true);
    node(...P[2], "Evidence", "66 of 94 correct (70.2%); decreased alone 52%");
    node(...P[3], "Cohort", "47 + 47, matched for age, sex, scanner");
    for (let i = 0; i < 3; i++) curve(s, P[i][0] + w - 0.05, P[i][1] + h * 0.62, P[i + 1][0] + 0.1, P[i + 1][1] + h * 0.42, { arrow: true, width: 2.5 });
    node(3.55, 4.95, "Data", "ds000030 (UCLA CNP), versioned");
    // broken link from cohort to data
    curve(s, 10.8, 4.3, 9.6, 5.25, { color: C.accent2, width: 2.5, dash: "dash" });
    curve(s, 8.5, 5.55, 6.4, 5.85, { color: C.accent2, width: 2.5, dash: "dash", arrow: true });
    shp(s, pres.shapes.OVAL, 8.75, 5.05, 0.7, 0.7, C.accent2, "?", { fontSize: 28, bold: true, color: C.background1 });
    text(s, [{ text: "Partial link: ", options: { bold: true, color: C.accent2 } }, { text: "authors' OSF data + code reproduce 66/94; not given: which ds000030 participant each matrix is" }], 9.7, 5.15, 3.2, 1.4, { fontSize: 18, color: C.text1, valign: "middle" });
    s.addNotes("1:30. Terms: Kim et al. 2023 classified schizophrenia patients versus controls from resting-state connectivity between 268 brain regions (Shen atlas). Leave-one-out means: train on 93 people, predict the 94th, repeat for every person; 70.2% means 66 of the 94 predictions were right (50% is chance for a 47/47 sample; permutation p = 0.001). The question is the paper's own, verbatim from the end of its Introduction: 'Does increased connectivity add information regarding schizophrenia?' (the abstract frames the same aim as the direction of the connectivity alteration). The claim answers it: within a cohort, adding increased to decreased connections improves classification ('combining information from both increased and decreased rsFC substantially improved prediction accuracy'); across cohorts, 'the prediction model using decreased rsFC performed best' (UCLA to COBRE 61.5%), with decreased connections mostly 'within and between the motor networks'. Evidence, re-run here: the authors' OSF project (https://osf.io/agqtn/) has UCLA_data.mat — the 94 connectivity matrices and labels — and their MATLAB code; a Python port gives exactly 70.2% (66/94) with both directions, and also the two numbers the paper does not report: 52.1% with decreased connections alone and 61.7% with increased alone. Cohort: 50 patients and 120 controls in ds000030, motion exclusions (excluded IDs in the supplementary material), then propensity-score matching on age, sex and scanner to 47 + 47. So the link is partial, not missing: the data and code to reproduce the result are public; what is not given is which ds000030 participant each matrix is. Speaker note: earlier drafts paraphrased the question twice and stated the cohort link as missing; both were corrected after reading the paper and its OSF project. Lesson: record the participant manifest with every analysis.\n\n" + fromOld(13, 12));
  }


  // 8a Spot the error
  const statements = [
    ["A", "Each UCLA participant left out once: 66 of 94 (70.2%) classified correctly."],
    ["B", "Connectivity predicts schizophrenia with 70.2% accuracy in any cohort."],
    ["C", "70.2% proves a causal disease mechanism."],
  ];
  function stmtCards(s, reveal) {
    const verdict = [["Supported, in scope", C.accent1], ["Scope dropped", C.accent2], ["Not in the source", C.accent2]];
    statements.forEach(([k, v], i) => {
      const y = 1.5 + i * 1.7;
      shp(s, pres.shapes.OVAL, 0.6, y + 0.05, 1.3, 1.3, reveal ? verdict[i][1] : C.text2, k, { fontSize: 36, bold: true, color: C.background1 });
      shp(s, pres.shapes.ROUNDED_RECTANGULAR_CALLOUT, 2.25, y, reveal ? 7.6 : 10.45, 1.35, C.background2, `“${v}”`, { fontSize: 24, margin: 12, align: "left", line: "C9D3D7" });
      if (reveal) {
        shp(s, pres.shapes.OVAL, 10.3, y - 0.12, 2.35, 1.6, C.background1, verdict[i][0], { fontSize: 18, bold: true, color: verdict[i][1], line: verdict[i][1], lineWidth: 3, rotate: -8, margin: 8 });
      }
    });
  }

  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Exercise: evaluating claims against a source", { placeholder: "title" });
    stmtCards(s, false);
    text(s, "All three cite the same quote from Kim 2023. Which would you accept?", 0.7, 6.6, 12, 0.5, { fontSize: 22, italic: true, color: C.accent2 });
    s.addNotes("0:45. Audience exercise: 30 seconds. All three statements carry the same exact evidence span. Statement C was actually run through the StructSense span validator in the pilot and passed it; B is constructed for this exercise to show scope loss (cross-dataset transfer was 61.5% in one direction and not above chance in the other).\n\n" + fromOld(18));
  }
  // 8b Reveal
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Quotation checks and scientific entailment", { placeholder: "title" });
    stmtCards(s, true);
    s.addNotes("0:30. Reveal. Say: a graph will store B and C just as faithfully as A, so someone still has to check scope and whether the statement follows from the source. Exact-span checking is lexical: it confirms that the words exist in the source, not that the statement follows from them. In the pilot, C passes the upstream span validator; separate semantic review rejects it. This is a demonstrated limit of lexical validation, not a demonstrated autonomous semantic gate.\n\n" + fromOld(18, 15));
  }

  // 4e Joining graphs
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Joining graphs through shared identifiers", { placeholder: "title" });
    shp(s, pres.shapes.OVAL, 0.55, 1.5, 2.3, 2.3, C.accent1, [
      { text: "Our ABIDE graph", options: { bold: true, fontSize: 20, breakLine: true } },
      { text: "cohorts, derivatives, results", options: { fontSize: 15 } },
    ], { color: C.background1, margin: 10 });
    for (const [i, J] of ABIDE.joins.entries()) {
      const y = 1.4 + i * 1.13, cy = y + 0.5;
      curve(s, 2.83, 2.65, 4.5, cy, { color: C.accent3, width: 2 });
      shp(s, pres.shapes.OVAL, 4.5, y + 0.05, 0.9, 0.9, i === 3 ? C.accent2 : C.text2);
      n += 1;
      s.addImage({ data: await icon(fa[J.icon]), x: 4.72, y: y + 0.27, w: 0.46, h: 0.46, objectName: `join${n}` });
      text(s, [
        { text: J.name, options: { bold: true, fontSize: 18, color: C.text2 } },
        ...(J.src ? [{ text: "  " + J.src, options: { fontSize: 14, color: C.accent3 } }] : []),
        { text: "   key: " + J.key, options: { fontSize: 14, italic: true, color: C.accent1, breakLine: true } },
        { text: J.result, options: { fontSize: 16, color: C.text1 } },
      ], 5.55, y - 0.02, 7.35, 1.08, { valign: "middle" });
    }
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 0.35, 4.0, 3.0, 2.95, C.accent5, null, { line: C.accent2, rectRadius: 0.1 });
    text(s, [
      { text: "Same term, different measure", options: { bold: true, fontSize: 16, color: C.accent2, breakLine: true } },
      { text: "Cortical grey matter (UBERON:0000956; UBERON = anatomy vocabulary)", options: { bold: true, fontSize: 14, breakLine: true } },
      { text: "ANTs vs FreeSurfer: r 0.85, ratio 1.01", options: { fontSize: 14, breakLine: true } },
      { text: "ANTs vs FSL: r 0.72, ratio 0.84", options: { fontSize: 14, breakLine: true } },
      { text: "CSF (UBERON:0001359)", options: { bold: true, fontSize: 14, breakLine: true } },
      { text: "FSL total CSF vs ANTs ventricles: ~200× apart, r 0.23", options: { fontSize: 14 } },
    ], 0.5, 4.1, 2.75, 2.75, { color: C.text1, valign: "top", paraSpaceAfter: 2 });
    s.addNotes("1:30. Terms: ABIDE I is the Autism Brain Imaging Data Exchange, resting-state fMRI from 17 sites; NIDM is a vocabulary for neuroimaging records; simple2 is ReproNim's set of ABIDE records written in NIDM, one graph per site; OpenAlex is an open catalogue of scholarly papers; a DOI is a persistent identifier for a paper. Our ABIDE graph joined to five others, each through a different key, with what the join actually returned. ReproNim's simple2 NIDM graphs (27 site graphs, commit e0dff17) join on ndar:src_subject_id = SUB_ID: all 1,112 participants matched with no orphans, 1,035 have CC200 files, and 767 are in Analyst B's cohort; the link is a reviewed correspondence, not owl:sameAs. AbstractAtlas (OHBM 2026, commit 181652e2) joins only on the dataset name in abstract text: 35 abstracts, 17 of which state data use, and 15 of those 17 were correct on a hand check. OpenAlex joins on DOI and citation: 598 works cite Di Martino 2014 and name ABIDE. Brain Researcher's graph has one aggregate ABIDE node (2,226 subjects) and neither paper. A SynthScholar literature review joining on DOI plus cohort description found three papers sharing the 871-participant ABIDE I subset (Abraham 2017, Parisot 2018, Ktena 2017). The inset is the caution: a shared concept term (UBERON:0000956, cortical grey matter) let us join volumes across tools, but ANTs and FreeSurfer agree well (r = 0.85, median ratio 1.01), ANTs and FSL less (r = 0.72, ratio 0.84), and under 'CSF' (UBERON:0001359) FSL reports total CSF while ANTs and FreeSurfer report ventricles, so values differ about 200-fold (ANTs/FSL median ratio 0.005, r = 0.23; FSL/FreeSurfer 224): the term matched, the measurement definition did not. Sources: ABIDE_Collaboration_Experiment/results/simple2.json, simple2_tool_agreement.csv, publications.json.");
  }

  // 4f Harmonising graphs
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Harmonising graphs built by different people", { placeholder: "title" });
    blob(s, 0.35, 1.7, 2.2, 4.9, "BFE0E0", 4);
    text(s, [{ text: "Our ABIDE graph", options: { bold: true, breakLine: true } }, { text: "contributor A", options: { fontSize: 14, color: C.accent3 } }], 0.45, 3.6, 2.0, 0.9, { fontSize: 18, color: C.text2, align: "center", valign: "middle" });
    blob(s, 10.8, 1.7, 2.2, 4.9, "F2D4C5", 9);
    text(s, [{ text: "ReproNim simple2", options: { bold: true, breakLine: true } }, { text: "contributor B", options: { fontSize: 14, color: C.accent3 } }], 10.9, 3.6, 2.0, 0.9, { fontSize: 18, color: C.text2, align: "center", valign: "middle" });
    const L = [
      ["Shared identifiers", "dataset + version, participant ID, DOI, ORCID, RRID · Caltech, ours vs ReproNim simple2: 38\u00a0/\u00a038 participants matched"],
      ["Shared vocabularies", "concept tags (InterLex, nidm-terms), UBERON regions, Cognitive Atlas tasks · Caltech: 12\u00a0concepts shared"],
      ["Shared schema and validation", "PyNIDM LinkML schema → SHACL rules; the same checks for every contributor"],
      ["Reviewed mapping links", "Caltech: 28 variables (over half ADOS, ADI-R or SRS subscores) share a source variable but not a concept → listed for review as skos:exactMatch candidates, never auto-asserted"],
      ["One named graph per contributor, with PROV", "Caltech: 0 of 282 participant × concept values conflict (both from the same ABIDE table) · across tools, ‘CSF’ is total CSF in FSL, ventricles in ANTs/FreeSurfer (~200×)"],
      ["Federation instead of copying", "Neurobagel sends the query to each pond; only permitted results return"],
    ];
    L.forEach(([k, v], i) => {
      const y = 1.42 + i * 0.915;
      curve(s, 2.5, 4.15, 2.85, y + 0.43, { color: C.accent1, width: 1.5 });
      curve(s, 10.45, y + 0.43, 10.85, 4.15, { color: C.accent2, width: 1.5 });
      shp(s, pres.shapes.ROUNDED_RECTANGLE, 2.85, y, 7.6, 0.86, i % 2 ? C.background2 : C.accent6, [
        { text: `${i + 1}  ${k}`, options: { bold: true, fontSize: 16, color: C.text2, breakLine: true } },
        { text: v, options: { fontSize: 14, color: C.text1 } },
      ], { align: "left", margin: 6, rectRadius: 0.5 });
    });
    s.addNotes("1:00. Six layers let graphs built by different people be used together. First, shared identifiers: a dataset and its version, participant IDs, DOIs for papers, ORCIDs for people, RRIDs for tools; ReproNim's simple2 graphs join ours on the participant ID for all 1,112 ABIDE I participants. Second, shared vocabularies: tags that say what a variable is about (InterLex and nidm-terms concepts), UBERON for anatomy, Cognitive Atlas for tasks. Third, a shared schema with validation: the PyNIDM LinkML schema compiled to SHACL rules, so every contributor's graph passes the same checks. Fourth, where vocabularies differ, mapping links (exactMatch or closeMatch) that a named reviewer asserted, never a silent declaration that two things are identical. Fifth, one named graph per contributor with PROV, so disagreements stay visible instead of being overwritten: under the same UBERON term for CSF, FSL reports total CSF while ANTs and FreeSurfer report ventricles, about 200-fold apart; and two agents reconstructed the ABIDE cohorts differently (871-based versus 767). Sixth, federation instead of copying: Neurobagel sends the query to each pond and returns only permitted results. The Caltech numbers on the slide are a real comparison of two contributors' graphs for one site, our graph against ReproNim's simple2 NIDM, run by compare_graphs.py (sensein/agent_skills PR #49, skills/neuroimaging-kg/scripts/compare_graphs.py; output in examples/abide_one_site/demo_output.txt and graph/compare.md): all 38 participants match with none left over; 12 concepts are shared; 28 variables, over half of them ADOS, ADI-R and SRS subscores, carry the same source variable in both graphs but no shared concept, so they are written to a review file as proposed skos:exactMatch links and none is asserted automatically; and 0 of 282 participant-by-concept values conflict, which is expected because both graphs come from the same ABIDE phenotype table. The conflict that does appear is across tools, not contributors: the CSF definitions in layer 5.");
  }

  // 5b Participant coverage by data element
  {
    const EL = ABIDE.elements;
    const s = addSlide("CONTENT", MAIN);
    s.addText(EL.title, { placeholder: "title" });
    if (EL.figure) {
      await fitImage(s, EL.figure, 0.4, 1.35, 8.55, 5.65);
    } else {
      shp(s, pres.shapes.ROUNDED_RECTANGLE, 0.5, 1.45, 8.3, 5.6, C.background2, [{ text: "[pending]", options: { breakLine: true } }, { text: "data element × site, with totals", options: { fontSize: 16 } }], { color: C.accent3, line: "B8C4C9", dash: "dash", rectRadius: 0.1 });
    }
    EL.callouts.forEach((c, i) => {
      const x = 9.15 + (i % 2) * 1.9, y = 1.5 + Math.floor(i / 2) * 2.85;
      shp(s, pres.shapes.OVAL, x, y, 1.75, 1.75, i === 0 ? C.accent1 : C.accent4, c.value, { fontSize: c.value.includes("pending") ? 14 : 32, bold: true, color: i === 0 ? C.background1 : C.accent1 });
      text(s, c.label, x - 0.1, y + 1.8, 1.95, 0.9, { fontSize: 16, align: "center", color: C.text1 });
    });
    s.addNotes("0:45. Terms: FIQ, VIQ and PIQ are full-scale, verbal and performance IQ; ADOS is a clinician-administered autism assessment; SRS is the Social Responsiveness Scale; mean FD is average head movement between fMRI volumes; CC200 is a 200-region brain parcellation. The same graph read the other way: for each data element, how many participants have it, by site. The callouts are joins the graph answers directly, for example how many participants have phenotype, time series and image-derived phenotypes together. " + EL.notes);
  }

  // 9 ABIDE design
  {
    const CO = ABIDE.cohorts;
    const s = addSlide("CONTENT", MAIN);
    s.addText("ABIDE I: two analyses, two research questions", { placeholder: "title" });
    shp(s, pres.shapes.OVAL, 3.35, 1.45, 6.6, 5.55, C.background2, null, { line: "C9D3D7" });
    text(s, [{ text: "ABIDE I", options: { bold: true, fontSize: 22, breakLine: true } }, { text: "autism; 1,112 participants, 17 sites; 200-region time series", options: { fontSize: 16 } }], 4.45, 1.7, 4.4, 0.85, { color: C.text2, align: "center" });
    shp(s, pres.shapes.OVAL, 4.55, 2.6, 4.2, 3.45, C.accent2, null, { transparency: 35 });
    shp(s, pres.shapes.OVAL, 4.85, 3.05, 2.55, 2.55, C.accent1, null, { transparency: 25 });
    text(s, [{ text: CO.both, options: { bold: true, fontSize: 32, breakLine: true } }, { text: "A, all also in B", options: { fontSize: 16 } }], 4.9, 3.75, 2.45, 1.2, { color: C.text2, align: "center", valign: "middle" });
    text(s, [{ text: CO.bOnly, options: { bold: true, fontSize: 32, breakLine: true } }, { text: "B only", options: { fontSize: 16 } }], 7.3, 3.75, 1.35, 1.2, { color: C.text2, align: "center", valign: "middle" });
    text(s, "Shared graph: cohorts, derivatives, results and reviews, with who made each", 4.2, 6.15, 4.95, 0.7, { fontSize: 16, color: C.text2, align: "center", valign: "middle" });
    text(s, [
      { text: "Analyst A (illustrative)", options: { bold: true, fontSize: 16, color: C.accent3, breakLine: true } },
      { text: "Do autistic and non-autistic groups differ in connectivity?", options: { bold: true, fontSize: 22, color: C.accent1, breakLine: true } },
      { text: "group difference · association", options: { fontSize: 18, breakLine: true } },
      { text: "after Di Martino et al. 2014", options: { fontSize: 16, italic: true, color: C.accent3 } },
    ], 0.5, 2.6, 2.75, 3.4, { valign: "middle", paraSpaceAfter: 6 });
    text(s, [
      { text: "Analyst B (illustrative)", options: { bold: true, fontSize: 16, color: C.accent3, breakLine: true } },
      { text: "Does connectivity predict diagnosis at unseen sites?", options: { bold: true, fontSize: 22, color: C.accent2, breakLine: true } },
      { text: "prediction · leave-site-out", options: { fontSize: 18, breakLine: true } },
      { text: "after Abraham et al. 2017", options: { fontSize: 16, italic: true, color: C.accent3 } },
    ], 10.1, 2.6, 2.75, 3.4, { valign: "middle", paraSpaceAfter: 6 });
    s.addNotes("0:45. Cohorts from results/key_numbers.json: Analyst A's cohort (n = " + CO.aN + ", 9 sites) lies entirely inside Analyst B's (n = " + CO.bN + ", 20 sites); " + CO.bOnly + " participants are in B only. Under the stricter QC rule A loses " + CO.aRemoved + " and B loses " + CO.bRemoved + ". An earlier version of this slide showed 104 / 780 / 91 from a second agent's reconstruction built around an 871-participant cohort; the two agents reconstructed the same cohorts differently, which is itself a point for the comparison slide. Say: both use ABIDE, but they may not use the same participants, and they are asking different questions, so their claims need separate scopes. Second worked example, executed in the background on ABIDE I Preprocessed (CPAC, CC200 atlas). Analysts A and B are simulated, clearly labelled illustrative agents, not real people. A asks an associational question modelled on Di Martino et al. 2014 (Mol Psychiatry); B asks a predictive question modelled on Abraham et al. 2017 (NeuroImage), with leave-site-out evaluation. A group difference does not establish accurate individual prediction, and a shared dataset name does not establish identical samples. The graph records each collaborator's cohort, derivatives, results and reviews of the other's work as attributed PROV activities.");
  }


  // 10 ABIDE results
  {
    const R = ABIDE.results;
    const s = addSlide("CONTENT", MAIN);
    s.addText(R.title, { placeholder: "title" });
    if (R.figure) {
      s.addImage({ path: R.figure, altText: path.basename(R.figure), x: 0.6, y: 1.45, w: 12.1, h: 4.9, sizing: { type: "contain", w: 12.1, h: 4.9 } });
    } else {
      [["A", R.a, C.accent4], ["B", R.b, C.accent5]].forEach(([k, d, fill], i) => {
        const x = 0.6 + i * 6.2;
        card(s, x, 1.5, 5.9, 5.2, fill, [
          { text: `Analyst ${k}`, options: { bold: true, fontSize: 16, color: C.accent3, breakLine: true } },
          { text: d.headline, options: { bold: true, fontSize: 30, color: C.text2, breakLine: true } },
          ...d.lines.map((l, j) => ({ text: l, options: { fontSize: 18, italic: j === d.lines.length - 1, color: j === d.lines.length - 1 ? C.accent3 : C.text1, breakLine: j < d.lines.length - 1 } })),
        ], { valign: "top", margin: 16 });
        text(s, d.caption, x + 0.3, 6.1, 5.3, 0.45, { fontSize: 16, italic: true, color: C.accent3 });
      });
    }
    s.addNotes("1:00. Terms: FDR (false discovery rate) correction controls the share of false positives among the many connections tested; Cohen's d is the group difference in standard-deviation units; AUC is the area under the ROC curve, 0.5 is chance and 1 is perfect; tangent-space connectivity is a way of comparing whole connectivity matrices that respects their geometry; leave-site-out trains on all sites but one and tests on the held-out site. Say: these answer different questions, so neither result confirms or refutes the other. " + R.notes);
  }

  // 11a Predict
  {
    const P = ABIDE.predict;
    const s = addSlide("CONTENT", MAIN);
    s.addText(P.title, { placeholder: "title" });
    card(s, 0.7, 1.5, 12.0, 1.3, C.text2, P.change, { fontSize: 24, color: C.background1, bold: true });
    P.questions.forEach((q, i) => {
      card(s, 0.7, 3.15 + i * 1.1, 0.95, 0.95, C.accent2, String(i + 1), { fontSize: 28, bold: true, color: C.background1, align: "center" });
      text(s, q, 1.95, 3.15 + i * 1.1, 10.7, 0.95, { fontSize: 26, valign: "middle" });
    });
    text(s, "Write down your guesses.", 0.7, 6.5, 11, 0.5, { fontSize: 22, italic: true, color: C.accent2 });
    s.addNotes("0:30. Ask the room to guess before the reveal. " + P.notes);
  }
  // 11b Reveal
  {
    const R = ABIDE.reveal;
    const s = addSlide("CONTENT", MAIN);
    s.addText(R.title, { placeholder: "title" });
    const cx = 0.55, cy = 4.2;
    const rings = [[3.9, 1.7], [5.9, 2.2], [7.9, 2.65]];
    rings.slice().reverse().forEach(([rx, ry], i) => shp(s, pres.shapes.BLOCK_ARC, cx - rx, cy - ry, 2 * rx, 2 * ry, [C.accent4, C.accent6, C.background2][i], null, { angleRange: [270, 90], arcThicknessRatio: 0.995 }));
    rings.forEach(([rx, ry]) => shp(s, pres.shapes.BLOCK_ARC, cx - rx, cy - ry, 2 * rx, 2 * ry, C.accent3, null, { angleRange: [270, 90], arcThicknessRatio: 0.012 }));
    shp(s, pres.shapes.PIE, cx - 1.9, cy - 1.25, 3.8, 2.5, C.text2, null, { angleRange: [270, 90] });
    text(s, [{ text: "stricter", options: { breakLine: true } }, { text: "QC rule" }], 0.65, cy - 0.5, 1.5, 1.0, { fontSize: 20, bold: true, color: C.background1, valign: "middle" });
    const bands = [[2.5, 1.85], [4.5, 1.85], [6.5, 1.85]];
    R.stats.slice(0, 3).forEach((st, i) => {
      text(s, [
        { text: st.value, options: { bold: true, fontSize: isPending(st.value) ? 18 : 40, color: C.accent1, breakLine: true } },
        { text: st.label, options: { fontSize: 18, color: C.text1 } },
      ], bands[i][0], cy - 0.8, bands[i][1], 1.6, { align: "center", valign: "middle" });
    });
    const last = R.stats[3];
    shp(s, pres.shapes.OVAL, 9.55, 2.35, 3.2, 3.2, C.accent5, [
      { text: last.value, options: { bold: true, fontSize: isPending(last.value) ? 18 : 48, color: C.accent2, breakLine: true } },
      { text: last.label, options: { fontSize: 18, color: C.text1 } },
    ], { line: C.accent2, lineWidth: 2, margin: 10 });
    curve(s, 8.5, 4.3, 9.55, 3.95, { color: C.accent2, width: 2.5, arrow: true });
    text(s, "after targeted rerun", 9.55, 5.7, 3.2, 0.45, { fontSize: 16, italic: true, color: C.accent2, align: "center" });
    s.addNotes("0:45. Reveal. The sequence is: traverse the graph, flag the dependent results, rerun only those, record what changed. Say: a flagged result needs a second look; only the rerun tells us whether it actually changed. " + R.notes);
  }


  // 12a Datasets, publications and abstracts
  {
    const PB = ABIDE.pubs;
    const s = addSlide("CONTENT", MAIN);
    s.addText(PB.title, { placeholder: "title" });
    const num = (v) => ({ text: v, options: { bold: true, fontSize: v.includes("pending") ? 16 : 30, breakLine: true } });
    shp(s, pres.shapes.OVAL, 0.5, 2.9, 2.3, 2.3, C.text2, [{ text: "ABIDE I", options: { bold: true, fontSize: 24, breakLine: true } }, { text: "dataset", options: { fontSize: 16 } }], { color: C.background1 });
    shp(s, pres.shapes.OVAL, 3.9, 1.45, 2.3, 2.3, C.accent4, [num(PB.publications), { text: "publications", options: { fontSize: 16, breakLine: true } }, { text: "OpenAlex", options: { fontSize: 14, color: C.accent3 } }], { color: C.text2 });
    shp(s, pres.shapes.OVAL, 3.9, 4.25, 2.3, 2.3, C.accent6, [num(PB.abstracts), { text: "abstracts", options: { fontSize: 16, breakLine: true } }, { text: "AbstractAtlas", options: { fontSize: 14, color: C.accent3 } }], { color: C.text2 });
    shp(s, pres.shapes.OVAL, 7.15, 1.4, 2.45, 2.45, C.accent5, [num(PB.reviewed), { text: "studies reviewed", options: { fontSize: 16, breakLine: true } }, { text: "SynthScholar", options: { fontSize: 14, color: C.accent3 } }], { color: C.text2 });
    shp(s, pres.shapes.OVAL, 7.15, 4.2, 2.45, 2.45, C.accent5, [num(PB.claims), { text: "extracted claims", options: { fontSize: 16, breakLine: true } }, { text: "evidence types (ECO)", options: { fontSize: 14, color: C.accent3 } }], { color: C.text2 });
    shp(s, pres.shapes.OVAL, 10.5, 2.95, 2.45, 2.45, C.accent1, [{ text: PB.reconstructible + " / " + PB.reviewed, options: { bold: true, fontSize: 28, breakLine: true } }, { text: "cohorts", options: { fontSize: 16, breakLine: true } }, { text: "reconstructible", options: { fontSize: 16 } }], { color: C.background1 });
    curve(s, 2.75, 3.6, 3.9, 2.65, { arrow: true, width: 2.5, dash: "sysDot" });
    curve(s, 2.75, 4.5, 3.95, 5.4, { arrow: true, width: 2.5 });
    curve(s, 6.2, 2.6, 7.15, 2.6, { arrow: true, width: 2.5 });
    curve(s, 6.2, 5.4, 7.15, 5.4, { arrow: true, width: 2.5 });
    curve(s, 9.6, 2.65, 10.6, 3.6, { arrow: true, width: 2.5 });
    text(s, PB.subset + " reuse the 871-participant subset", 10.25, 5.5, 2.95, 0.7, { fontSize: 16, italic: true, color: C.accent1, align: "center" });
    // relation status legend
    text(s, "Relation status", 0.5, 6.65, 2.0, 0.45, { fontSize: 16, bold: true, color: C.text2, valign: "middle" });
    [["mentions", "sysDot"], ["uses data", "solid"], ["candidate", "dash"]].forEach(([t, d], i) => {
      shp(s, pres.shapes.ROUNDED_RECTANGLE, 2.55 + i * 1.75, 6.68, 1.6, 0.4, C.background1, t, { fontSize: 14, line: C.accent3, dash: d });
    });
    shp(s, pres.shapes.OVAL, 11.3, 1.25, 1.7, 1.45, C.background1, [{ text: "as of", options: { fontSize: 14, breakLine: true } }, { text: PB.asOf, options: { fontSize: 15, bold: true } }], { color: C.accent2, line: C.accent2, lineWidth: 2.5, rotate: -8, margin: 0 });
    s.addNotes("0:30. Start from the dataset and follow it outward: publications that cite and name ABIDE (counted from OpenAlex), a systematic review of those studies, abstracts in AbstractAtlas and the claims extracted from them with ECO evidence codes, and how many study cohorts can be rebuilt and so linked back to our graph. Each link carries a status: mentions, uses the data, or only a candidate. The counts are a dated snapshot, so the refresh date is part of the record. AbstractAtlas: abstractatlas.brainkb.org, code at github.com/sensein/abstractatlas. Two cautions: its author IDs are corpus-local, deduplicated by name and affiliation, so they should not be treated as global identities; and semantic similarity only proposes candidate relations, it does not verify support. " + PB.notes);
  }

  // 12b Asking Claude about the literature graph (tested exchange: slides/demo/literature_query_answer.md)
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Asking Claude about the literature graph", { placeholder: "title" });
    const head = async (Ic, fill, t, x, w) => {
      shp(s, pres.shapes.OVAL, x, 1.47, 0.46, 0.46, fill);
      n += 1;
      s.addImage({ data: await icon(Ic), x: x + 0.11, y: 1.58, w: 0.24, h: 0.24, objectName: `litHeadIcon${n}` });
      text(s, t, x + 0.56, 1.45, w - 0.56, 0.5, { fontSize: 18, bold: true, color: C.text2, valign: "middle" });
    };
    await head(fa.FaUser, C.accent1, "Participant asks", 0.45, 3.0);
    await head(fa.FaRobot, C.text2, "Claude writes and runs SPARQL", 3.65, 4.85);
    await head(fa.FaRobot, C.text2, "Claude answers", 8.7, 4.2);
    // prompt
    shp(s, pres.shapes.ROUNDED_RECTANGULAR_CALLOUT, 0.45, 2.1, 3.0, 3.15, C.accent4,
      "“Using only this graph: which studies tested their classifier by holding out whole sites, what accuracy did each report, and what verbatim quote supports it?”",
      { fontSize: 18, italic: true, color: C.text2, align: "left", valign: "middle", margin: 10 });
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 0.45, 5.5, 3.0, 0.72, C.accent5, [{ text: "88 s", options: { fontSize: 20, breakLine: true } }, { text: "Claude Code + pyoxigraph" }], { fontSize: 16, bold: true, color: C.accent2, line: C.accent2, rectRadius: 0.3, margin: 2 });
    text(s, "Headless run in a fresh folder holding only literature_kg.ttl", 0.45, 6.3, 3.0, 0.65, { fontSize: 14, color: C.accent3, align: "center" });
    // query (excerpt of the two queries in the answer)
    const CM = { color: "9FD3D4" }, CD = { color: "E8F1F2" };
    const code = [
      ["# studies + accuracy (trimmed)", CM],
      ["SELECT ?id ?acc ?basis ?snippet …", CD],
      ["WHERE {", CD],
      [" { ?pub ex:reportsPerformance ?perf .", CD],
      ["   ?perf ex:evaluationScheme", CD],
      ["         \"leave-site-out\" }", CD],
      [" UNION { ?pub a ex:Publication ;", CD],
      ["   ex:evaluationScheme", CD],
      ["         \"leave-site-out\" }", CD],
      [" OPTIONAL {", CD],
      ["   ?pub ex:reportsPerformance ?p2 .", CD],
      ["   ?p2 ex:accuracyPct ?acc ;", CD],
      ["       ex:basis ?basis }", CD],
      ["}", CD],
      ["# then the verbatim quotes", CM],
      ["?q prov:wasQuotedFrom ?pub ;", CD],
      ["   prov:value ?quote ;", CD],
      ["   ex:sourceQuoteVerified ?verified .", CD],
    ];
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 3.65, 2.1, 4.85, 4.8, C.text2, null, { rectRadius: 0.04 });
    s.addText(code.map(([t, o], i) => ({ text: t, options: { ...o, breakLine: i < code.length - 1 } })), { x: 3.78, y: 2.22, w: 4.62, h: 4.6, fontFace: "Courier New", fontSize: 14, valign: "top", paraSpaceAfter: 2, margin: 0, isTextBox: true, objectName: "litQuery" });
    // answer excerpt (rows copied from the answer's table)
    table(s, [
      ["Study", "Leave-site-out accuracy"],
      ["Abraham 2017", "66.8%"],
      ["S-030", "56% balanced accuracy"],
      ["S-062", "71% ± 6%"],
      ["S-071", "73.4% (CC200 atlas)"],
    ], { x: 8.7, y: 2.1, w: 4.2, colW: [1.55, 2.65], rowH: 0.42, fontSize: 16 });
    text(s, "Also in its table: S-072 ~62%; S-022 with no value", 8.7, 4.3, 4.2, 0.35, { fontSize: 14, italic: true, color: C.accent3 });
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 8.7, 4.75, 4.2, 2.15, C.accent5, null, { line: C.accent2, rectRadius: 0.1 });
    text(s, [
      { text: "What the graph can't tell you", options: { bold: true, color: C.accent2, breakLine: true } },
      { text: "S-022 ran the test, but the graph stores no accuracy for it", options: { bullet: true, breakLine: true } },
      { text: "Quotes are tied to papers, not to a specific accuracy value", options: { bullet: true } },
    ], 8.85, 4.85, 3.95, 1.95, { fontSize: 16, color: C.text1, valign: "top", paraSpaceAfter: 6 });
    s.addNotes("1:00. This exchange was run, not mocked up: Claude Code ran headless in a fresh folder that held only literature_kg.ttl, the review's graph, and answered in 88 s. A participant can do the same: open Claude Code in a folder containing the graph file and ask in plain language. It wrote the SPARQL itself (the middle panel is an excerpt of its two queries), ran it with pyoxigraph, and returned a table with a verbatim quote for each study; the prompt on the left is an excerpt, and the full answer is in slides/demo/literature_query_answer.md. Its numbers match the review's synthesis (literature_review/synthesis.md): 6 studies hold whole sites out and 5 of them report an accuracy, median 66.8%, range 56–73.4% (Abraham 2017 66.8%, S-030 56% balanced accuracy, S-062 71%, S-071 73.4%, S-072 about 62%). Equally important is what it did not do: S-022 says it ran the leave-site-out test, the graph stores no accuracy for it, and the assistant said so instead of borrowing that paper's 70.22% from pooled cross-validation. It also reported that quotes are linked to papers rather than to individual accuracy values, so it chose each quote from the graph's summary of what the quote supports, and that most values are the best of several models and S-030's is balanced accuracy, so they are not directly comparable.");
  }

  // 12c Evaluation schemes in the reviewed studies
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Evaluation schemes in 74 ABIDE studies", { placeholder: "title" });
    await fitImage(s, EXP + "/literature_review/figures/accuracy_by_evaluation.png", 0.6, 1.35, 12.1, 5.6);
    s.addNotes("0:30. Terms: pooled k-fold cross-validation mixes participants from all sites in training and test folds; leave-site-out holds out whole sites; leakage means information from the test data reached training (for example, harmonising sites before splitting). From a SynthScholar (v0.3.0) review: 994 records identified, 99 assessed, 74 studies included. Of 53 studies with a predictive claim, 26 use cross-validation that mixes sites across train and test folds and only 6 hold whole sites out. Median best accuracy is 73% under pooled k-fold cross-validation (23 studies; 70.9% without the 8 leakage-flagged ones) and 67% under leave-site-out (5 studies). These are different studies, models and subsets, so the gap is descriptive, not a controlled comparison; one study that reports both schemes for the same model drops from 64% to 56% balanced accuracy when sites are held out. Charting was done by AI agents with mechanical checks that each quoted value appears in the paper's full text; individual charting decisions were not verified by a person. Source: literature_review/synthesis.md, results_synthesis.json, figures/accuracy_by_evaluation.png.");
  }

  // 4d ReproPond and ReproLake
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("ReproPond and ReproLake as attributes on graph records", { placeholder: "title" });
    const WATER = "BFE0E0", LAKE = "8CC7C8";
    // ponds
    blob(s, 0.4, 1.4, 3.7, 1.35, WATER, 3);
    text(s, [{ text: "Site pond", options: { bold: true, breakLine: true } }, { text: "scanner B quirk; motion profile" }], 0.7, 1.55, 3.1, 1.05, { fontSize: 16, color: C.text2, align: "center", valign: "middle" });
    blob(s, 0.4, 2.85, 3.7, 1.35, WATER, 7);
    text(s, [{ text: "Lab pond", options: { bold: true, breakLine: true } }, { text: "FD rule, cohorts, reviews, skills" }], 0.7, 3.0, 3.1, 1.05, { fontSize: 16, color: C.text2, align: "center", valign: "middle" });
    blob(s, 0.25, 4.25, 5.0, 3.0, WATER, 11);
    n += 1;
    shp(s, pres.shapes.OVAL, 0.85, 4.6, 0.55, 0.55, C.accent2);
    s.addImage({ data: await icon(fa.FaLock), x: 0.99, y: 4.74, w: 0.27, h: 0.27, objectName: `lock${n}` });
    text(s, "Stays in the pond", 1.5, 4.62, 3.2, 0.5, { fontSize: 18, bold: true, color: C.accent2, valign: "middle" });
    s.addText([
      "consent scoped to study or named uses", "direct identifiers, full dates", "undefaced images", "quasi-identifiers, small cells", "restricted fields; linking keys",
    ].map((t, i, a) => ({ text: t, options: { bullet: true, breakLine: i < a.length - 1 } })), { x: 0.75, y: 5.15, w: 4.3, h: 1.75, fontSize: 16, color: C.text1, valign: "top", margin: 0, isTextBox: true, objectName: "staysList" });
    // lake
    blob(s, 8.45, 2.35, 4.5, 4.4, LAKE, 5);
    text(s, "ReproLake (shared)", 8.9, 2.75, 3.6, 0.45, { fontSize: 20, bold: true, color: C.text2, align: "center", valign: "middle" });
    s.addText(["BIDS spec and conventions", "published guidelines", "dataset records, scoped claims", "shared skills, variable definitions"].map((t, i, a) => ({ text: t, options: { breakLine: i < a.length - 1 } })),
      { x: 8.95, y: 3.25, w: 3.5, h: 1.9, fontSize: 16, color: C.text1, align: "center", valign: "middle", paraSpaceAfter: 4, isTextBox: true, objectName: "lakeList" });
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 9.35, 5.45, 2.7, 0.4, C.background1, "Deprecation / revision", { fontSize: 14, color: C.accent2, line: C.accent2, dash: "dash" });
    // streams with gates
    curve(s, 4.05, 2.1, 8.6, 3.35, { color: LAKE, width: 7 });
    curve(s, 4.05, 3.55, 8.55, 4.2, { color: LAKE, width: 7 });
    for (const [gx, gy] of [[6.1, 2.55], [6.1, 3.7]]) {
      shp(s, pres.shapes.OVAL, gx, gy, 0.5, 0.5, C.accent1, null, { line: C.background1, lineWidth: 2 });
      n += 1;
      s.addImage({ data: await icon(fa.FaFilter), x: gx + 0.13, y: gy + 0.13, w: 0.24, h: 0.24, objectName: `gate${n}` });
    }
    text(s, "pond → lake, through gates", 5.0, 4.35, 3.5, 0.4, { fontSize: 16, bold: true, color: C.accent1, align: "center" });
    const gates = [["generality across sites", 2.0], ["review", 1.3], ["consent covers broad sharing (DUO)", 3.38], ["licence", 1.0], ["persistent ID + version", 2.3], ["provenance", 3.38]];
    let gx = 5.05, gy = 4.8;
    gates.forEach(([t, w]) => { if (gx + w > 8.5) { gx = 5.05; gy += 0.4; } shp(s, pres.shapes.ROUNDED_RECTANGLE, gx, gy, w, 0.34, C.background1, t, { fontSize: 14, line: C.accent1 }); gx += w + 0.08; });
    // adoption back to the ponds
    curve(s, 8.9, 6.45, 5.35, 6.7, { color: C.text2, width: 2.5, arrow: true });
    text(s, "lake → pond: pin version, record local parameters, re-validate", 5.3, 6.82, 6.3, 0.4, { fontSize: 15, color: C.text2 });
    // federated query
    n += 1;
    shp(s, pres.shapes.OVAL, 4.55, 1.35, 0.55, 0.55, C.text2);
    s.addImage({ data: await icon(fa.FaSearch), x: 4.69, y: 1.49, w: 0.27, h: 0.27, objectName: `query${n}` });
    curve(s, 4.55, 1.62, 3.85, 1.9, { color: C.text2, width: 1.5, dash: "dash", arrow: true });
    curve(s, 4.6, 1.85, 3.9, 3.2, { color: C.text2, width: 1.5, dash: "dash", arrow: true });
    text(s, [{ text: "Federated query (Neurobagel): ", options: { bold: true } }, { text: "the query goes to the pond; only permitted results return." }], 5.25, 1.3, 7.6, 0.7, { fontSize: 16, color: C.text2, valign: "middle" });
    s.addNotes("1:00. ReproNim's terms, from the repronim.org tutorial 'Sharing and Searching Metadata Using a ReproPond and the ReproLake' (resources/tutorials/pond-lake). A ReproPond is a local FAIR metadata store, NIDM Turtle served by a Neurobagel node; ponds can be federated across sites. The ReproLake is a semantically aligned store of public datasets maintained by ReproNim. Neurobagel queries search across ponds and the lake. In our examples, ds000030 and ABIDE I are public, de-identified releases, so they are lake-eligible; the analysts' reviews, local QC rules and the illustrative collaboration records start in a pond. Example of what a global graph lacks: Brain Researcher's knowledge graph holds a single ABIDE node (2,226 subjects across ABIDE I and II) and neither Di Martino 2014 nor Abraham 2017. Our local graph holds the exact cohorts, for example the 871 participants in Analyst B's cohort, which matches Abraham's reported N; those cohort definitions and scoped claims are candidates to move from pond to lake, subject to the gates: generality beyond one site, review, consent that covers broad sharing (DUO), licence, a persistent identifier with a version, and provenance. Lake to pond: a template such as MNI152NLin2009cAsym is pinned to a version, local parameters are recorded, and it still needs per-participant registration QC. Some things stay in the pond: data whose consent is scoped to the study or to named uses rather than broad sharing (DUO-restricted, or limited by a DUA such as NDA or ABCD), direct identifiers and full dates, undefaced images, quasi-identifier combinations and small cells, restricted fields, and the keys that link pseudonymous IDs to people. Federated query lets the question travel to the pond so that only permitted answers come back.");
  }


  // N3 Live demos
  for (const [di, title, ps, inst, extra] of [
    [1, "Live demo: building a graph in Claude Code", [0, 1], true, "assistant overstated: 2 tools, not 3"],
    [2, "Live demo: querying and using the graph", [2, 3], false, null],
  ]) {
    const s = addSlide("CONTENT", MAIN);
    s.addText(title, { placeholder: "title" });
    const lines = [];
    if (inst) DEMO.install.forEach((c) => lines.push({ text: "$ " + c, options: { color: "9FD3D4", breakLine: true } }));
    ps.forEach((k, j) => {
      const P = DEMO.prompts[k];
      lines.push({ text: P.label, options: { bold: true, color: "FFFFFF", breakLine: true } });
      lines.push({ text: "> " + P.text, options: { color: "E8F1F2", breakLine: j < ps.length - 1 } });
    });
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 0.45, 1.35, 8.35, 5.6, C.text2, null, { rectRadius: 0.04 });
    s.addText(lines, { x: 0.6, y: 1.45, w: 8.05, h: 5.4, fontFace: "Courier New", fontSize: 16, valign: "top", paraSpaceAfter: 3, margin: 0, isTextBox: true, objectName: `demoCode${di}` });
    text(s, "Expected output (tested)", 9.0, 1.35, 3.9, 0.4, { fontSize: 18, bold: true, color: C.text2 });
    const outs = [];
    ps.forEach((k, j) => {
      const P = DEMO.prompts[k];
      outs.push({ text: P.label + " · " + P.duration, options: { bold: true, fontFace: "Calibri", color: C.accent1, breakLine: true } });
      P.expected.forEach((e, m) => outs.push({ text: e, options: { breakLine: !(j === ps.length - 1 && m === P.expected.length - 1) } }));
    });
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 9.0, 1.8, 3.9, extra ? 4.25 : 5.15, C.background2, null, { line: "C9D3D7", rectRadius: 0.05 });
    s.addText(outs, { x: 9.12, y: 1.9, w: 3.66, h: extra ? 4.05 : 4.95, fontFace: "Courier New", fontSize: 16, color: C.text1, valign: "top", paraSpaceAfter: 4, margin: 0, isTextBox: true, objectName: `demoOut${di}` });
    if (extra) shp(s, pres.shapes.ROUNDED_RECTANGLE, 9.0, 6.2, 3.9, 0.75, C.accent5, extra, { fontSize: 16, bold: true, color: C.accent2, line: C.accent2, rectRadius: 0.3 });
    s.addNotes(di === 1
      ? "1:45. Install the skill into this project only, then build a graph for one ABIDE I site (Caltech, 38 participants) from the phenotype table and ReproNim's NIDM file of brain volumes. Prompt 1 took 34 s in testing: the graph built, its checks passed, and a deliberately deleted 'derived from' link was caught. The assistant also said the volumes came from three tools (FreeSurfer, FSL, ANTs); Caltech's file has FreeSurfer and FSL only. That is a real check-against-the-graph moment: ask the room how we would verify it, and point out that one query over the software agents in the graph answers it. Prompt 2 (14 s) joins IQ from our table with FreeSurfer hippocampal volume from ReproNim's file through the shared participant ID: 18 autistic and 19 control participants. Repository and branch: " + DEMO.repo_branch + ". " + DEMO.note
      : "1:45. Prompt 3 (162 s, the slow one) traces participant 51456's left-hippocampus volume to its FreeSurfer run and the T1-weighted scan. The volume (4513.9 mm³) and its meaning are recorded; the link 'FreeSurfer ran on this scan' is not recorded, only implied by the subject ID appearing in a command line, and the FreeSurfer version appears only inside a path string. The graph shows where provenance is missing. Prompt 4 (55 s) applies the stricter motion rule, mean FD below 0.15 mm: participants 51456 and 51469 drop out, so the cohort becomes 17 autistic and 19 control, and the assistant flags two queries that ignore the cohort. " + DEMO.note);
  }

  // 14b The lecture's own provenance graph
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("The lecture's own provenance graph", { placeholder: "title" });
    const PQ = fs.existsSync(path.join(__dirname, "provenance_query.json")) ? JSON.parse(fs.readFileSync(path.join(__dirname, "provenance_query.json"), "utf8")) : { rows: [], triples: 0 };
    const nd = (x, y, w, h, fill, t, sub, col) => shp(s, pres.shapes.ROUNDED_RECTANGLE, x, y, w, h, fill, [{ text: t, options: { bold: true, fontSize: 15, breakLine: true } }, { text: sub, options: { fontSize: 12, color: col ? C.accent4 : C.accent3 } }], { color: col || C.text2, rectRadius: 0.4, margin: 4 });
    nd(0.5, 2.25, 2.3, 0.95, C.text2, "a slide", "“Joining graphs …”", C.background1);
    nd(3.6, 1.62, 2.6, 0.78, C.accent4, "production activity", "A: agent ran code");
    nd(6.65, 1.62, 2.15, 0.78, C.accent4, "agent", "coding agent");
    nd(3.6, 2.55, 2.6, 0.85, C.background2, "results/simple2.json", "a result file");
    nd(3.6, 3.65, 2.6, 0.85, C.accent5, "assessment", "re-run · validated");
    nd(6.55, 3.65, 2.3, 0.85, C.background2, "clean_room_verify", "evidence (.json)");
    const el = (t, x, y, w) => text(s, t, x, y, w, 0.3, { fontSize: 12, italic: true, color: C.accent1, align: "center" });
    curve(s, 2.8, 2.5, 3.6, 2.0, { arrow: true, width: 2, color: C.accent1 }); el("wasGeneratedBy", 2.2, 1.75, 1.6);
    arrow(s, 6.2, 2.01, 6.65, 2.01, { color: C.accent1, width: 2 }); el("associatedWith", 5.6, 1.36, 1.6);
    arrow(s, 2.8, 2.98, 3.6, 2.98, { color: C.accent1, width: 2 }); el("wasDerivedFrom", 2.45, 3.0, 1.6);
    curve(s, 3.6, 4.08, 2.8, 3.05, { arrow: true, width: 2, color: C.accent2 }); el("assesses", 2.3, 3.85, 1.3);
    arrow(s, 6.2, 4.08, 6.55, 4.08, { color: C.accent1, width: 2 }); el("wasDerivedFrom", 5.6, 4.5, 1.6);
    // the query and its answer
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 8.95, 1.38, 3.95, 1.12, C.text2, null, { rectRadius: 0.05 });
    s.addText("SELECT ?status (COUNT(?slide) AS ?n)\nWHERE { ?a talk:assesses ?slide ;\n           talk:checkingLabel ?status }\nGROUP BY ?status", { x: 9.05, y: 1.43, w: 3.8, h: 1.02, fontFace: "Courier New", fontSize: 12, color: "E8F1F2", valign: "top", margin: 0, isTextBox: true, objectName: "provQuery" });
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 8.95, 2.58, 3.95, 2.1, C.background2, null, { line: "C9D3D7", rectRadius: 0.05 });
    s.addText(PQ.rows.map((r, i) => ({ text: `${r.n}  ${r.status}`, options: { breakLine: i < PQ.rows.length - 1 } })), { x: 9.05, y: 2.63, w: 3.8, h: 2.0, fontFace: "Courier New", fontSize: 12, color: C.text1, valign: "top", margin: 0, isTextBox: true, objectName: "provAnswer" });
    // caught-by, compact
    text(s, "Caught by the speaker", 0.55, 4.75, 5.9, 0.35, { fontSize: 16, bold: true, color: C.accent2 });
    text(s, "Caught by automated checks", 6.85, 4.75, 5.9, 0.35, { fontSize: 16, bold: true, color: C.accent1 });
    s.addText(["Consent wording: scoped consent, not “no consent”", "Kim 2023 question paraphrased wrongly; fixed from source", "AbstractAtlas links dropped, then restored", "LLM-style footers and titles removed"].map((t, i, a) => ({ text: t, options: { bullet: true, breakLine: i < a.length - 1 } })), { x: 0.55, y: 5.15, w: 6.0, h: 1.8, fontSize: 15, color: C.text1, valign: "top", paraSpaceAfter: 3, margin: 0, isTextBox: true, objectName: "caughtSpeaker" });
    s.addText(["Failed ORCD job: invalid p-values", "Clean rebuild caught a blocked download (HTTP 403)", "Two agents reconstructed the same cohorts differently", "UMAP values drift across machines; all else matched"].map((t, i, a) => ({ text: t, options: { bullet: true, breakLine: i < a.length - 1 } })), { x: 6.85, y: 5.15, w: 6.0, h: 1.8, fontSize: 15, color: C.text1, valign: "top", paraSpaceAfter: 3, margin: 0, isTextBox: true, objectName: "caughtChecks" });
    s.addNotes("0:45. The lecture has its own provenance graph, talk_provenance.ttl, written by the deck build from a table of how each slide was made. Each slide is a node; it was generated by one or more production activities, each associated with an agent (the speaker, an LLM drafting from the speaker's instructions, an agent running code, an agent retrieving from sources, an external agent through MCP, or an earlier agentic session); it was derived from the result files it shows; and an assessment records how it was checked, derived from the evidence for that check (a rebuild comparison, a claim verification). The query on the right counts slides by checking status; it was run with pyoxigraph over the file (" + PQ.triples + " triples) and the answer is shown as returned. The badge in the corner of every slide is the same record. Corrections came from both directions: the speaker caught the consent wording, a paraphrase of Kim et al. 2023's research question that turned an association question into a prediction question, AbstractAtlas links that had been dropped, and LLM-style footers and titles; automated checks caught an ORCD job with invalid p-values, a clean rebuild that failed on a blocked download (HTTP 403), two agents that reconstructed the same ABIDE cohorts differently, and UMAP values that drift between machines while everything else matched.");
  }

  // 15 Five things this week
  {
    const s = addSlide("CONTENT", MAIN);
    s.addText("Practices to adopt now", { placeholder: "title" });
    const items = [
      [fa.FaThumbtack, "Pin your data", "commit or DataLad version, hashes"],
      [fa.FaListUl, "Save the manifest", "included, excluded, and the rule"],
      [fa.FaBullseye, "Scope each claim", "population, measure, contrast, evaluation"],
      [fa.FaCalculator, "Recompute one value", "from source, before trusting a table"],
      [fa.FaLink, "Use shared identifiers and terms", "IDs for papers, people and tools; shared variable terms"],
    ];
    shp(s, pres.shapes.OVAL, 0.6, 1.42, 0.26, 0.26, C.accent1);
    text(s, "Objective 1: represent results as a graph", 0.95, 1.33, 5.0, 0.42, { fontSize: 16, color: C.text2, valign: "middle" });
    shp(s, pres.shapes.OVAL, 6.3, 1.42, 0.26, 0.26, C.text2);
    text(s, "Objective 2: connect across graphs", 6.65, 1.33, 5.0, 0.42, { fontSize: 16, color: C.text2, valign: "middle" });
    const P0 = [1.0, 3.1], P1 = [6.65, 3.1], P2 = [6.65, 4.9], P3 = [12.3, 4.9];
    curve(s, P0[0], P0[1], P3[0], P3[1], { color: "C9DCDC", width: 14 });
    const bez = (t) => [0, 1].map((k) => (1 - t) ** 3 * P0[k] + 3 * (1 - t) ** 2 * t * P1[k] + 3 * (1 - t) * t ** 2 * P2[k] + t ** 3 * P3[k]);
    const ts = [0.04, 0.27, 0.5, 0.73, 0.96];
    for (let i = 0; i < items.length; i++) {
      const [Ic, head, sub] = items[i];
      const [x, y] = bez(ts[i]);
      const d = 1.15;
      shp(s, pres.shapes.OVAL, x - d / 2, y - d / 2, d, d, i < 4 ? C.accent1 : C.text2, null, { line: C.background1, lineWidth: 3 });
      n += 1;
      s.addImage({ data: await icon(Ic), x: x - 0.28, y: y - 0.28, w: 0.56, h: 0.56, objectName: `pIcon${n}` });
      const above = i % 2 === 1;
      const lw = 3.3, lx = Math.min(Math.max(x - lw / 2, 0.4), 12.95 - lw);
      text(s, [
        { text: head, options: { bold: true, fontSize: 22, color: C.text2, breakLine: true } },
        { text: sub, options: { fontSize: 17, color: C.accent3 } },
      ], lx, above ? y - d / 2 - 1.25 : y + d / 2 + 0.1, lw, 1.15, { align: "center", valign: above ? "bottom" : "top" });
    }
    s.addNotes("1:00. The take-home list; none of it needs an AI system, and each item supports one of the two objectives. For representing results (objective 1): pin your data with a DataLad version or commit and file hashes (connects to Yarik's STAMPED talk); save the participant manifest, which was the missing link in the Kim 2023 claim chain; scope each claim, keeping association and prediction apart as in the two ABIDE analyses; recompute one derived value from source, as in the Barratt check. For connecting graphs (objective 2): use shared identifiers and terms, such as DOIs for papers, ORCIDs for people, RRIDs or repository URLs for tools, and nidm-terms or InterLex concepts for variables, so that your graph can be joined to others; and check that a shared term really means the same measurement before relying on the join.");
  }


  // 16 Close
  {
    const s = addSlide("TITLE_DARK", MAIN);
    s.addText("Discussion", { placeholder: "title" });
    s.addText([
      { text: "Which links between your lab's graph and others would you need before using work done with an AI assistant?", options: { breakLine: true, fontSize: 26, bold: true } },
      { text: " ", options: { breakLine: true, fontSize: 12 } },
      { text: "Packages with code, graphs and results:", options: { breakLine: true, bold: true, fontSize: 22 } },
      { text: "CNP_Dataset_Publication_Knowledge_Graph.zip", options: { breakLine: true, fontSize: 20 } },
      { text: "ABIDE_Collaboration_Knowledge_Graph.zip", options: { breakLine: true, fontSize: 20 } },
      { text: "github.com/sensein/agent_skills · abstractatlas.brainkb.org", options: { fontSize: 20 } },
    ], { placeholder: "body" });
    s.addNotes("0:45 + discussion. Main-route total: 24:00 (opening: 0:20 title, 0:40 objectives, 0:45 the two datasets, 1:15 four-statement primer; objective 1: 1:15 dataset and publication components, 0:45 entities, 1:00 participant graph, 1:30 claim chain, 0:45 claim exercise, 0:30 quotation checks; objective 2: 1:30 joining graphs, 1:00 harmonising graphs, 0:45 coverage, 0:45 ABIDE design, 1:00 ABIDE results, 0:30 QC exercise, 0:45 dependency tracing, 0:30 publications and abstracts, 1:00 asking Claude about the literature graph, 0:30 evaluation schemes, 1:00 ReproPond and ReproLake; with an assistant: 1:45 demo 1, 1:45 demo 2, 0:45 the lecture's provenance graph; close: 1:00 practices, 0:45 discussion). Open the floor: which link in the chain (manifest, scope, derivative lineage, review) would your lab require before an agent's change is accepted? Offer a live look at the HTML experiment report if time allows.\n\n" + fromOld(28));
  }

  // ---------------------------------------------------------------- backup
  pres.addSection({ title: BACK });
  // 3a Poll
  const counts = [
    ["290", "Dataset description: sum of group counts"],
    ["272", "participants.tsv at the pinned commit"],
    ["261", "T1w + resting BOLD files present"],
    ["259", "T1w + stop-signal files present"],
    ["255", "2017 stop-signal analysis cohort"],
    ["94", "2023 matched UCLA analysis cohort"],
  ];
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("Poll: participant count in ds000030", { placeholder: "title" });
    const order = [3, 0, 5, 1, 4, 2]; // shuffled so the tokens do not read as a ranking
    order.forEach((ci, i) => {
      const d = 1.95, x = 0.65 + i * 2.05, y = i % 2 ? 3.75 : 1.75;
      shp(s, pres.shapes.OVAL, x, y, d, d, C.background2, [
        { text: counts[ci][0], options: { fontSize: 50, bold: true, color: C.text2, breakLine: true } },
        { text: String.fromCharCode(65 + i), options: { fontSize: 24, color: C.accent3 } },
      ], { line: "C9D3D7" });
    });
    text(s, "Hold up a letter, A–F", 0.7, 6.4, 11, 0.5, { fontSize: 22, italic: true, color: C.accent2 });
    s.addNotes("Backup (was a main-route slide).  Tokens are shuffled (A = 259, B = 290, C = 94, D = 272, E = 255, F = 261). Ask the audience to hold up fingers or call out a letter. Give 20 seconds. Then ask: which number would an agent return if you asked it 'how many subjects'?\n\n" + fromOld(34, 29));
  }

  // 3b Reveal
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("Participant counts in ds000030 by scope", { placeholder: "title" });
    counts.forEach(([v, lab], i) => {
      const d = 1.25 + ((Number(v) - 94) / (290 - 94)) * 0.75;
      const cx = 1.55 + i * 2.1, cy = 2.75 + i * 0.42;
      shp(s, pres.shapes.OVAL, cx - d / 2, cy - d / 2, d, d, i === 0 ? C.text2 : C.accent1, v, { fontSize: 44, bold: true, color: C.background1 });
      text(s, lab, cx - 0.97, cy + d / 2 + 0.12, 1.94, 1.0, { fontSize: 17, align: "center", color: C.text1 });
    });
    arrow(s, 0.9, 6.6, 11.9, 6.6, { color: C.accent3, width: 2 });
    text(s, "broadest scope", 0.9, 6.63, 3, 0.4, { fontSize: 16, italic: true, color: C.accent3 });
    text(s, "narrowest scope", 8.9, 6.63, 3, 0.4, { fontSize: 16, italic: true, color: C.accent3, align: "right" });
    s.addNotes("Reveal. Say: every one of these is a correct answer to a slightly different question, so whatever records the number has to record its scope too. 290 is the sum in the dataset's prose description (138/58/49/45); 272 is the pinned participants.tsv; 261 and 259 are file-availability joins (availability is not QC); 255 is the 2017 stop-signal model; 94 is Kim 2023's matched UCLA cohort (47+47). An agent with document search will happily return any of these. A graph that stores the scope with each count makes the question answerable.\n\n" + fromOld(34));
  }


  // 4c Types of knowledge and their homes
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("Types of knowledge and where they are recorded", { placeholder: "title" });
    const sets = [
      ["Graph", "records you query", 0.45, 1.95, 5.75, 5.25, C.accent1, fa.FaProjectDiagram],
      ["Skill", "procedure you follow", 4.85, 2.45, 3.95, 4.2, C.text2, fa.FaListOl],
      ["Harness check", "test that runs", 8.45, 2.75, 2.7, 3.6, C.accent3, fa.FaCheckCircle],
      ["Human review", "judgement you record", 10.8, 3.0, 2.1, 3.1, C.accent2, fa.FaUserCheck],
    ];
    const tint = [C.accent4, C.accent6, C.background2, C.accent5];
    sets.forEach(([nm, sub, x, y, w, h, col], i) => shp(s, pres.shapes.OVAL, x, y, w, h, tint[i], null, { transparency: 15, line: col, lineWidth: 2 }));
    for (const [i, [nm, sub, x, y, w, h, col, Ic]] of sets.entries()) {
      const lx = i === 0 ? 0.55 : x + 0.05, ly = i === 0 ? 1.3 : y - 0.72;
      shp(s, pres.shapes.OVAL, lx, ly, 0.55, 0.55, col);
      n += 1;
      s.addImage({ data: await icon(Ic), x: lx + 0.13, y: ly + 0.13, w: 0.29, h: 0.29, objectName: `setIcon${n}` });
      text(s, [{ text: nm, options: { bold: true, fontSize: 18, color: col, breakLine: true } }, { text: sub, options: { fontSize: 14, color: C.accent3 } }], lx + 0.62, ly - 0.05, i === 0 ? 3.2 : i === 2 ? 1.65 : 2.6, 0.65, { valign: "middle" });
    }
    const item = (t, tag) => [{ text: t, options: { bold: true, fontSize: 16, color: C.text2 } }, ...(tag ? [{ text: "  " + tag, options: { italic: true, fontSize: 14, color: C.accent2 } }] : [])];
    const graphOnly = TYPES.filter((t) => t[4] === "graph" && t[0] !== "Local knowledge");
    graphOnly.forEach((t, i) => text(s, item(t[0], t[5]), 0.95, 2.55 + i * 0.58, 3.85, 0.45, { align: "center", valign: "middle" }));
    text(s, [{ text: "Local", options: { bold: true, breakLine: true } }, { text: "knowledge", options: { bold: true } }], 4.85, 3.95, 1.35, 0.75, { fontSize: 16, color: C.text2, align: "center", valign: "middle" });
    TYPES.filter((t) => t[4] === "skill").forEach((t, i) => text(s, item(t[0]), 6.25, 3.55 + i * 0.6, 2.2, 0.45, { align: "center", valign: "middle" }));
    text(s, [{ text: "Failure modes", options: { bold: true, breakLine: true } }, { text: " ", options: { fontSize: 10, breakLine: true } }, { text: "Acceptance", options: { bold: true, breakLine: true } }, { text: "criteria", options: { bold: true } }], 8.65, 3.6, 2.3, 1.9, { fontSize: 16, color: C.text2, align: "center", valign: "middle" });
    text(s, [{ text: "Tacit", options: { bold: true, breakLine: true } }, { text: "judgement", options: { bold: true } }], 11.15, 4.2, 1.6, 0.75, { fontSize: 16, color: C.text2, align: "center", valign: "middle" });
    s.addNotes("Backup (was a main-route slide).  The practical question is where each kind of knowledge can be checked; write it there. Walk one example per column. A fact such as TR = 2 s for this scan goes in the graph with its source. Know-how such as registering BOLD → T1 → template and checking it is a skill, a written procedure. A failure mode such as leakage across cross-validation folds becomes a harness test that runs every time. Tacit judgement such as visual QC of a registration stays human, but is recorded as an attributed assessment. Heuristics such as 'exclude mean FD > 0.2 mm' live as skill parameters and must carry their derivation and limits, not just the number. Some kinds live in two places: definitions in the graph plus ontology terms; local lab knowledge in the graph plus a skill scoped to the site. The examples for every kind are in the backup table; the slide shows where each one lives. Local knowledge sits in the overlap because it needs both a graph record and a site-scoped skill.");
  }


  // 6 Recompute one derivative
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("Recomputing a derived score from source items", { placeholder: "title" });
    text(s, "sub-10159 · Barratt parcel 1", 0.6, 1.55, 6.8, 0.5, { fontSize: 24, bold: true, color: C.text2 });
    shp(s, pres.shapes.OVAL, 0.6, 2.4, 1.65, 1.65, C.accent4, [{ text: "item 19", options: { fontSize: 16, breakLine: true } }, { text: "2", options: { fontSize: 36, bold: true } }], { color: C.text2 });
    shp(s, pres.shapes.OVAL, 2.4, 2.4, 1.65, 1.65, C.accent4, [{ text: "item 17", options: { fontSize: 16, breakLine: true } }, { text: "2", options: { fontSize: 36, bold: true } }], { color: C.text2 });
    shp(s, pres.shapes.CHEVRON, 4.2, 2.75, 1.7, 0.95, C.text2, "mean", { margin: 0, fontSize: 18, bold: true, color: C.background1 });
    shp(s, pres.shapes.OVAL, 6.05, 2.4, 1.65, 1.65, C.accent1, [{ text: "result", options: { fontSize: 16, breakLine: true } }, { text: "2", options: { fontSize: 36, bold: true } }], { color: C.background1 });
    n += 1;
    shp(s, pres.shapes.OVAL, 0.6, 4.55, 0.75, 0.75, C.accent1);
    s.addImage({ data: await icon(fa.FaCheck), x: 0.8, y: 4.75, w: 0.35, h: 0.35, objectName: `check${n}` });
    text(s, "matches the reported value, 2", 1.55, 4.55, 5.7, 0.75, { fontSize: 24, color: C.text1, valign: "middle" });
    text(s, "Dictionary formula: mean of items 19 and 17", 0.6, 5.65, 6.7, 0.6, { fontSize: 20, color: C.accent3, valign: "middle" });
    shp(s, pres.shapes.BLOCK_ARC, 8.1, 1.45, 4.3, 4.3, C.accent1, null, { angleRange: [270, 269.5], arcThicknessRatio: 0.12 });
    text(s, "272 / 272", 8.1, 1.45, 4.3, 4.3, { fontSize: 48, bold: true, color: C.accent1, align: "center", valign: "middle" });
    text(s, "reported scores reproduced from their item responses", 7.85, 5.95, 4.8, 0.95, { fontSize: 22, color: C.text1, align: "center" });
    s.addNotes("Backup (was a main-route slide).  We checked this one formula across all 272 participants; other variables marked as derivatives in the dictionary have not been recomputed, so the flag alone tells us nothing about their lineage. Executed check. Dictionary formula from phenotype/barratt.json, item values from phenotype/barratt.tsv. The graph keeps formula, inputs, output and the agreement check as a recorded activity. Lesson for Monday: before trusting a derived table, recompute one derived value from source.\n\n" + fromOld(7));
  }


  // 13 Validate skill vs output
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("Checking agent outputs against the graph", { placeholder: "title" });
    card(s, 0.6, 1.45, 5.95, 2.45, C.accent4, [
      { text: "The skill, once per version", options: { bold: true, fontSize: 24, color: C.accent1, breakLine: true } },
      { text: "held-out cases with human answers", options: { bullet: true, breakLine: true } },
      { text: "injected faults it must catch", options: { bullet: true } },
    ], { fontSize: 22, valign: "top", margin: 16 });
    card(s, 6.78, 1.45, 5.95, 2.45, C.accent5, [
      { text: "Each output, every time", options: { bold: true, fontSize: 24, color: C.accent2, breakLine: true } },
      { text: "check against the source", options: { bullet: true, breakLine: true } },
      { text: "keep cohort, direction, method", options: { bullet: true } },
    ], { fontSize: 22, valign: "top", margin: 16 });
    text(s, "Faults we injected, and what caught them", 0.6, 4.2, 12, 0.5, { fontSize: 22, bold: true, color: C.text2 });
    const faults = [["Wrong offsets", "repaired and marked"], ["Invented quote", "dropped"], ["Number as text", "schema rejects"], ["Source edge removed", "SHACL rejects"]];
    faults.forEach(([f, r], i) => {
      card(s, 0.6 + i * 3.06, 4.85, 2.9, 1.85, C.background2, [
        { text: f, options: { bold: true, fontSize: 20, breakLine: true } },
        { text: r, options: { fontSize: 18, color: C.accent1 } },
      ], { align: "center", line: "C9D3D7" });
    });
    s.addNotes("Backup (was a main-route slide).  Say: these are smoke tests; we have not measured precision and recall on held-out papers. A skill can be sound while one output fails; a correct output does not validate the skill. The StructSense pilot (0.12.0, commit dde54251) used a frozen schema, six bounded records, the unmodified upstream span validator, Ajv JSON Schema and pySHACL. The four injected faults are executed checks (skill/pilot_report.json, skill/schema_validation.json, shacl_mutation_report.txt). It does not establish held-out precision/recall or long-run agent reliability.\n\n" + fromOld(16, 17, 14));
  }

  // 14 Comparison
  {
    const Cmp = ABIDE.comparison;
    const s = addSlide("BACKUP", BACK);
    s.addText(Cmp.title, { placeholder: "title" });
    table(s, [Cmp.header, ...Cmp.rows], { y: 1.45, fontSize: 16, rowH: 0.72, colW: [3.7, 4.0, 4.4] });
    s.addNotes("Backup (was a main-route slide).  One run per condition with one model, not blinded: treat it as a demonstration rather than a benchmark. " + Cmp.notes + "\n\n" + fromOld(22, 23));
  }

  const backups = [
    ["Scope of the ds000030 extraction", [["Layer", "Completed work"], ["Phenotype tables", "52 tables, 1,983 columns, 272 participants"], ["Observed / missing cells", "411,584 values / 127,792 missing cells"], ["MRI inventory", "2,531 file pointers, plus selected metadata"], ["Papers", "Three related papers, selected claims and methods"], ["Graph size", "834,327 NIDM triples before the claim bridge"]], [4], [3.5, 8.6]],
    ["NIDM and PROV roles for each record", [["Record", "NIDM / PROV representation"], ["Participant and visit", "prov:Person and nidm:Session"], ["Questionnaire or scan", "nidm:Acquisition activity"], ["Variable definition and value", "nidm:DataElement on an AcquisitionObject"], ["Processing and its output", "nidm:Derivative and DerivativeObject"]], [5], [4.5, 7.6]],
    ["Requirements for joining behaviour to image-derived measures", [["Link required", "State in ds000030"], ["Same participant and visit", "Participant IDs available; time alignment unresolved"], ["Imaging measure definition", "Region, atlas, laterality, units and method required"], ["Derived value to original image", "Stats file, processing record and source image required"], ["Example future join", "SSRT with thickness or regional volume"]], [8], [4.5, 7.6]],
    ["Research questions and results of the three papers", [["Paper / result", "Question, result and scope"], ["Poldrack 2016", "Data descriptor: enables dimensional study across diagnoses"], ["Gorgolewski 2017", "Reusable preprocessing and QC outputs"], ["Kim 2023", "Which direction of connectivity change is associated with schizophrenia; cross-dataset transfer"], ["Kim 70.2%", "UCLA, both directions, leave-one-out"], ["Kim 61.5%", "Train UCLA, test COBRE, decreased connectivity"], ["Kim reverse transfer", "No above-chance predictions reported"]], [11, 12], [3.5, 8.6]],
    ["StructSense extraction pilot", [["Stage", "What actually ran"], ["Contract", "Frozen schema for claims, scope and evidence"], ["Extraction", "Host-model extraction of six bounded records"], ["Alignment and review", "Explicit vocabulary lookup and source review"], ["Validation", "Upstream span code, Ajv schema, RDF checks"], ["Example record", "Statement, scope, exact span + hash, open gap"]], [14, 15], [3.5, 8.6]],
    ["Attribution across collaborators", [["Question the graph can answer", "Required records and constraints"], ["Who worked on this question?", "Person → activity → question, claim and outputs"], ["Which claims inform another question?", "Reviewed relevance or support relation with scope"], ["Who disagrees, and on what basis?", "Separate assessments, evidence and reviewer roles"], ["What changes when evidence is corrected?", "Traverse affected claims, questions and work items"], ["AbstractAtlas building blocks", "Semantic search, extracted claims with ECO codes, author records, cached provenance"]], [19, 20, 21], [4.5, 7.6]],
    ["Design for a graph-versus-search comparison", [["Controlled factor", "Proposed experiment"], ["Same corpus, model and tool budget", "Search only; skill only; graph only; both"], ["Held-out questions", "Single fact, cohort join, lineage and contradiction"], ["Scoring", "Correctness, evidence completeness, false claims"], ["Longer agent sessions", "Constraint violations and recovery"]], [22, 23], [4.5, 7.6]],
    ["Forms of drift and corresponding checks", [["Drift", "Enforcement mechanism"], ["Dataset or skill version changes", "Pin and compare artifact hashes"], ["A result loses its evaluation scope", "Require claim-to-evaluation links"], ["A derivative loses its source", "Reject at the provenance gate"], ["A report is treated as replication", "Preserve evidence status and review changes"], ["Still required", "Image bytes, IDPs, paper manifests, held-out skill studies"]], [24, 25], [4.5, 7.6]],
    ["Scan, events and phenotype details", [["Record (sub-10159)", "Observed value"], ["Resting BOLD TR / TE", "2 s / 0.03 s, 3 T, scanner 35343"], ["Stop-signal events", "256 rows: 96 GO, 32 STOP, 128 NULL"], ["STOP outcomes", "17 successful, 15 unsuccessful"], ["sst_ses_ssrt_quant / sst_ses_ssrt", "200.125 / 216.625, unit not specified"], ["T1w TR / TE: paper vs JSON", "1.9 s / 2.26 ms vs 2.53 s / 3.31 ms"]], [30, 31, 32, 43], [4.5, 7.6]],
    ["Registration and cross-source joins", [["Item", "What the evidence supports"], ["Functional → T1", "FreeSurfer BBR, 9 DOF (2017 paper)"], ["T1 → MNI152NLin2009cAsym", "ANTs SyN with affine initialization"], ["Seven missing-T1 IDs", "Same IDs in current metadata and 2017 Table 1"], ["Kim 2023 and ds000030", "Explicit accession and version link"], ["Kim 2023 and 2017 derivatives", "Reuse not established; different pipeline reported"]], [33, 35, 36], [4.5, 7.6]],
    ["Skills and pull requests referenced", [["Skill / PR", "Contribution"], ["structsense", "Entities and source-stated relations with evidence"], ["synthscholar", "Review protocols, corpus handling, retrieval provenance"], ["labnb / duct / orcd-remote", "Run records, resource logs, remote execution"], ["sensein PRs #33, #34, #36", "LinkML records, judge loop, MeSH search (open)"], ["K-Dense datalad #227 / STAMPED #265", "Retrieval provenance (merged) / evidence map (open)"]], [26, 37, 38, 39, 41], [4.5, 7.6]],
    ["Brain Researcher: reported benchmarks", [["Reported benchmark", "Without BR", "With BR"], ["First-choice route/tool selection", "23.3%", "93.6%"], ["Verified evidence grounding", "4.6%", "22.0%"], ["Source", "Chen et al., arXiv:2608.19902v1", "preprint"]], [27, 40], [6.1, 3.0, 3.0]],
    ["Workshop connections", [["Earlier session", "Reusable artifact this talk adds"], ["Brent: LLM interaction", "Task instructions with explicit inputs and outputs"], ["JB: analytical flexibility", "Named alternatives and comparable evaluation records"], ["Michelle: automation", "Validated inputs and inspectable tool execution"], ["Yarik: STAMPED", "Versioned components and evidence for replayability"], ["Johanna: Project-Pilot", "Reviewed changes to persistent skills and workflows"]], [42], [4.5, 7.6]],
    ["Sources", [["Source", "Locator"], ["ds000030 metadata, pinned", "OpenNeuroDatasets/ds000030 @ 4070b6ee"], ["Poldrack et al. 2016", "doi 10.1038/sdata.2016.110"], ["Gorgolewski et al. 2017 v2", "doi 10.12688/f1000research.11964.2"], ["Kim et al. 2023", "doi 10.3389/fpsyt.2023.1232015"], ["Skills and harness", "sensein/agent_skills · K-Dense scientific-agent-skills · brain-researcher-public"]], [44, 45], [4.5, 7.6]],
  ];
  for (const [title, rows, olds, colW] of backups) {
    const s = addSlide("BACKUP", BACK);
    s.addText(title, { placeholder: "title" });
    table(s, rows, { y: 1.4, fontSize: 18, colW, rowH: 0.62 });
    s.addNotes(fromOld(...olds));
  }
  // Kinds of knowledge, full table
  for (const [title, gs] of [["Entities in a neuroimaging knowledge graph (1 of 2)", ["What was studied", "How it was done"]], ["Entities in a neuroimaging knowledge graph (2 of 2)", ["What was found", "Who and in what context"]]]) {
    const s = addSlide("BACKUP", BACK);
    s.addText(title, { placeholder: "title" });
    const rows = [["Group", "Kind", "Standards / examples"]];
    KINDS.filter((k) => gs.includes(k[0])).forEach((k) => rows.push([k[0], k[1] + (k[4] ? " ●" : ""), k[3]]));
    table(s, rows, { y: 1.2, fontSize: 14, colW: [2.3, 2.9, 6.9], rowH: 0.42 });
    text(s, "● populated in the ds000030 or ABIDE packages", 3.2, 7.08, 8, 0.3, { fontSize: 13, italic: true, color: C.accent3 });
    s.addNotes("Full typology from talk_plan.md. Standards named here are pointers, not endorsements of completeness; several (ReproStim, reproseed, BABS) are ReproNim-adjacent tools. A graph only holds what someone recorded.");
  }

  // Types of knowledge, full table
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("Types of knowledge and where they are recorded: full table", { placeholder: "title" });
    table(s, [["Kind", "Neuroimaging example", "Where it lives"], ...TYPES.map((t) => [t[0], t[2], t[3]])], { y: 1.2, fontSize: 14, colW: [2.4, 5.8, 3.9], rowH: 0.37 });
    s.addNotes("Full table from talk_plan.md, section 'Types of knowledge, and where each lives'. Graph = records you query; skill = procedure you follow; harness check = test that runs; human review = judgement you record.");
  }

  // ReproPond and ReproLake, full table
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("ReproPond and ReproLake: full table and transitions", { placeholder: "title" });
    table(s, [["ReproPond (lab / site)", "ReproLake (shared)"],
      ["Scanner B phase-encoding quirk; site motion profile", "BIDS spec, scanner-independent conventions"],
      ["Lab QC threshold and its derivation (FD < 0.2 mm on our data)", "Published guideline / consensus (COBIDAS, OHBM best practices)"],
      ["Exact cohort manifests, exclusions, per-participant derivatives", "Dataset record, version, licence (OpenNeuro, DANDI, ABIDE)"],
      ["Lab skills and runbooks (how we register, how we QC)", "Shared skill repos (ReproNim/skills, sensein/agent_skills)"],
      ["Local variable names, site-specific instruments", "nidm-terms / InterLex concepts, ReproSchema library"],
      ["Unpublished findings, reviews, disagreements", "Publications, scoped claims in literature KGs"],
      ["Data with consent scoped to the study or named uses; DUA-limited data", "DUO codes; only de-identified, permitted summaries"]], { y: 1.1, fontSize: 12, colW: [6.05, 6.05], rowH: 0.32 });
    s.addText([
      { text: "pond → lake: ", options: { bold: true } }, { text: "generality beyond one site or sample, review, de-identification, consent that covers broad sharing (DUO), licence, persistent identifier and version, provenance retained.", options: { breakLine: true } },
      { text: "lake → pond: ", options: { bold: true } }, { text: "pin the version, record local parameters and deviations, re-validate on local data.", options: { breakLine: true } },
      { text: "Deprecation / revision: ", options: { bold: true } }, { text: "shared knowledge ages or is contradicted; flag local copies when the source changes.", options: { breakLine: true } },
      { text: "Stays in the pond: ", options: { bold: true } }, { text: "data whose consent does not cover broad sharing (consent scoped to the study or to named uses; DUO-restricted; DUA-limited); direct identifiers and full dates; undefaced structural images; quasi-identifier combinations and small cells; restricted fields; linking keys between pseudonymous IDs and people.", options: { breakLine: true } },
      { text: "Can flow after the gates: ", options: { bold: true } }, { text: "dataset-level metadata, dictionaries and term mappings, aggregate counts above a minimum cell size, de-identified consented records, derived measures where consent allows, skills, provenance with pseudonymous IDs, scoped claims." },
    ], { x: 0.6, y: 3.85, w: 12.1, h: 3.0, fontSize: 13, color: C.text1, valign: "top", paraSpaceAfter: 4, isTextBox: true, objectName: "transitions" });
    s.addNotes("Source: repronim.org tutorial 'Sharing and Searching Metadata Using a ReproPond and the ReproLake' (content/resources/tutorials/pond-lake.md). Scope levels: individual analyst → lab → institution / site → consortium → shared (registries, ontologies, literature-derived KGs such as BR-KG, AbstractAtlas). Each transition is recorded as a PROV activity with an agent and a review assessment. Pond-to-lake examples here: ABIDE claims and cohort definitions absent from BR-KG; an FD-threshold sweep as evidence for a guideline; local ABIDE variable mappings → nidm-terms; a lab registration skill → a shared skill repo.");
  }

  // Backup: provenance of a single ds000030 measurement
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("Provenance of a single phenotype measurement", { placeholder: "title" });
    const d = 2.4;
    const node = (x, y, fill, title, sub, light) => shp(s, pres.shapes.OVAL, x, y, d, d, fill, [
      ...title.split("\n").map((t) => ({ text: t, options: { bold: true, fontSize: 18, breakLine: true } })),
      { text: sub, options: { fontSize: 12, color: light ? C.accent4 : C.accent3 } },
    ], { color: light ? C.background1 : C.text1, margin: 2 });
    node(0.5, 1.5, C.text2, "sub-10159", "participant", true);
    node(3.6, 3.25, C.accent4, "Barratt\nquestionnaire\nsession", "nidm:Acquisition");
    node(6.75, 1.5, C.accent4, "Questionnaire\nrecord", "nidm:AcquisitionObject");
    node(10.1, 3.25, C.accent1, "‘acts\nimpulsively’\n= 2.0", "bis_parcel1", true);
    curve(s, 3.75, 4.1, 2.6, 3.4, { arrow: true, width: 2.5 }); edgeLabel(s, "with participant (role: subject)", 0.6, 4.35, 3.0);
    curve(s, 6.9, 3.2, 5.75, 3.85, { arrow: true, width: 2.5 }); edgeLabel(s, "was generated by", 4.9, 2.75, 2.2);
    curve(s, 9.0, 3.2, 10.25, 3.85, { arrow: true, width: 2.5 }); edgeLabel(s, "‘acts impulsively’ score", 8.9, 2.75, 2.6);
    shp(s, pres.shapes.ROUNDED_RECTANGLE, 6.45, 5.75, 3.0, 1.1, C.background2, [{ text: "barratt.tsv", options: { bold: true, fontSize: 20, breakLine: true } }, { text: "source row 2", options: { fontSize: 18, color: C.accent3 } }], { line: "B8C4C9", rectRadius: 0.25 });
    arrow(s, 7.95, 3.9, 7.95, 5.75); edgeLabel(s, "was derived from", 8.05, 4.65, 2.2);
    s.addNotes("Backup (was main-route slide). NIDM gives each record its neuroimaging role; PROV records where each value came from. A real record from the pinned ds000030 graph. The participant joins through a PROV qualified association with a subject role; the questionnaire record is generated by the assessment activity and derived from a specific row of a specific file; the value is a data element defined by the dataset dictionary. You do not need the vocabulary to adopt the habit: every value should point to its participant and its source row.\n\n" + fromOld(6, 5));
  }


  // AbstractAtlas building blocks
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("AbstractAtlas: building blocks", { placeholder: "title" });
    table(s, [["Available building block", "Pointer for this workflow"],
      ["Explore abstracts and related literature", "Semantic search, facets and NeuroScape map"],
      ["Inspect extracted claims", "Source text, evidence category and ECO annotations"],
      ["Connect authors to abstracts", "Author records and accepted poster identifiers"],
      ["Preserve computation history", "Source snapshots, model IDs and component caches"]], { y: 1.4, fontSize: 18, colW: [5.0, 7.1], rowH: 0.62 });
    text(s, "abstractatlas.brainkb.org · github.com/sensein/abstractatlas", 0.6, 4.9, 12, 0.45, { fontSize: 16, color: C.accent1 });
    s.addNotes(fromOld(19));
  }

  // 12b Resources and freshness
  {
    const RS = ABIDE.resources;
    const s = addSlide("BACKUP", BACK);
    s.addText(RS.title, { placeholder: "title" });
    card(s, 0.6, 1.35, 7.4, 0.6, C.text2, [
      { text: "Query  ", options: { bold: true, fontSize: 16, color: C.accent4 } },
      { text: `“${RS.query}”`, options: { fontSize: 18, color: C.background1 } },
    ], { margin: 10 });
    text(s, RS.snapshot, 8.2, 1.35, 4.6, 0.6, { fontSize: 14, italic: true, color: C.accent3, valign: "middle" });
    RS.results.forEach((r, i) => {
      const x = 0.6 + i * 4.1;
      card(s, x, 2.1, 0.5, 1.75, C.accent1, String(i + 1), { fontSize: 20, bold: true, color: C.background1, align: "center", margin: 0 });
      card(s, x + 0.55, 2.1, 3.4, 1.75, C.background2, [
        { text: r.tool, options: { bold: true, fontSize: 17, color: C.text2, breakLine: true } },
        { text: r.step, options: { fontSize: 14, italic: true, color: C.accent1, breakLine: true } },
        { text: r.activity, options: { fontSize: 14, color: C.text1, breakLine: true } },
        { text: r.asOf, options: { fontSize: 14, italic: true, color: C.accent2 } },
      ], { margin: 7, line: "C9D3D7", valign: "top" });
    });
    await fitImage(s, RS.figure, 0.6, 4.0, 12.2, 3.0);
    s.addNotes("Backup (was a main-route slide). " + RS.notes);
  }

  // ABIDE phenotype embedding (moved to backup)
  {
    const U = ABIDE.umap;
    const s = addSlide("BACKUP", BACK);
    s.addText(U.title, { placeholder: "title" });
    await fitImage(s, U.figure, 0.5, 1.25, 12.3, 3.3);
    s.addText(U.points.map((p, i) => ({ text: p, options: { bullet: true, breakLine: i < U.points.length - 1 } })), {
      x: 0.8, y: 4.8, w: 11.8, h: 1.9, fontSize: 20, color: C.text1, valign: "top", paraSpaceAfter: 8, isTextBox: true, objectName: "umapPoints",
    });
    s.addNotes("Backup (was a main-route slide). Before reading anything into clusters, colour by site and age. " + U.notes);
  }

  // Glossary
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("Glossary", { placeholder: "title" });
    const G1 = [
      ["ds000030", "UCLA Consortium for Neuropsychiatric Phenomics dataset (OpenNeuro): schizophrenia, bipolar disorder, ADHD and controls"],
      ["ABIDE I", "Autism Brain Imaging Data Exchange: resting-state fMRI and phenotypes, 17 sites, 1,112 participants"],
      ["ASD / TD", "autistic / typically developing comparison participants"],
      ["Barratt scale (BIS)", "30-item impulsivity questionnaire; items scored 1 rarely to 4 almost always"],
      ["bis_parcel1", "'acts impulsively': mean of items 17 and 19"],
      ["SSRT", "stop-signal reaction time: how long it takes to cancel a started response"],
      ["FIQ · SRS · ADOS", "full-scale IQ · Social Responsiveness Scale · Autism Diagnostic Observation Schedule"],
      ["Mean FD", "average head movement between fMRI volumes, in mm"],
      ["C-PAC · fMRIPrep", "preprocessing pipelines (ABIDE Preprocessed used C-PAC)"],
      ["CC200", "200-region functional brain parcellation; connectivity = correlation between regions"],
      ["BBR · ANTs SyN", "fMRI-to-anatomy registration · non-linear registration to a template"],
      ["CPM · linear SVM", "connectome-based predictive modelling · a standard linear classifier"],
    ];
    const G2 = [
      ["LOOCV · leave-site-out", "leave one participant out · train on all sites but one, test on the held-out site"],
      ["AUC · FDR · d", "0.5 = chance, 1 = perfect · false discovery rate correction · standardised effect size"],
      ["UMAP · trustworthiness", "2-D map placing similar participants close · how well neighbours are preserved"],
      ["Triple · query", "one statement: subject, relation, object · a statement pattern with blanks"],
      ["RDF · SPARQL · Oxigraph", "file format for statements · query language · a graph database"],
      ["NIDM · PROV", "neuroimaging data vocabulary · provenance standard (what produced what, from what)"],
      ["SHACL", "machine-checkable rules a graph must satisfy"],
      ["UBERON · InterLex · ECO", "anatomy vocabulary · shared variable definitions · evidence types for claims"],
      ["DUO · DOI · ORCID · RRID", "data-use conditions · persistent IDs for papers, people, tools"],
      ["PROBAST · ComBat", "risk-of-bias tool for prediction studies · site-effect harmonisation"],
      ["ReproPond · ReproLake", "a lab's local metadata store · shared store of public datasets"],
      ["Neurobagel · MCP", "sends a query to each pond, returns only permitted results · plug-in interface for AI tools"],
    ];
    [G1, G2].forEach((G, c) => s.addText(G.map(([k, v], i) => ([{ text: k + ": ", options: { bold: true, color: C.text2 } }, { text: v, options: { color: C.text1, breakLine: i < G.length - 1 } }])).flat(), {
      x: 0.5 + c * 6.25, y: 1.2, w: 6.05, h: 5.75, fontSize: 12, valign: "top", paraSpaceAfter: 3, margin: 0, isTextBox: true, objectName: `gloss${c}`,
    }));
    s.addNotes("Plain-language glossary from talk_plan.md; each term is also glossed on the main slide where it first appears.");
  }

  // Key to the badges
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("Key to the AI-involvement badges", { placeholder: "title" });
    text(s, "How it was produced", 0.6, 1.3, 7.4, 0.45, { fontSize: 20, bold: true, color: C.text2 });
    PROD_DEF.forEach(([L, name, def], i) => {
      shp(s, pres.shapes.OVAL, 0.6, 1.9 + i * 0.75, 0.55, 0.55, C.accent6, L, { fontSize: 18, bold: true, color: C.text2 });
      text(s, [{ text: name + ": ", options: { bold: true } }, { text: def }], 1.35, 1.82 + i * 0.75, 6.6, 0.7, { fontSize: 16, color: C.text1, valign: "middle" });
    });
    text(s, "How it was checked", 8.4, 1.3, 4.4, 0.45, { fontSize: 20, bold: true, color: C.text2 });
    CHECK_DEF.forEach(([w, def], i) => {
      text(s, [{ text: w, options: { bold: true, italic: true, color: C.accent3, breakLine: true } }, { text: def }], 8.4, 1.85 + i * 1.1, 4.4, 1.0, { fontSize: 16, color: C.text1 });
    });
    text(s, "Per-slide records are also exported as W3C PROV in talk_provenance.ttl.", 0.6, 6.55, 12, 0.4, { fontSize: 16, color: C.accent3 });
    s.addNotes("Badge key from talk_plan.md. Each slide's production letters and checking status are set in SLIDE_PROV in slides/build_deck.js and exported to talk_provenance.ttl (slides as prov:Entity, production activities associated with agent types, sources via prov:wasDerivedFrom, checking status as an attributed assessment).");
  }

  // CNP UMAP backup with figure
  {
    const s = addSlide("BACKUP", BACK);
    s.addText("ds000030 phenotype embedding from a graph query", { placeholder: "title" });
    s.addImage({ path: CNP_UMAP, altText: path.basename(CNP_UMAP), x: 1.6, y: 1.2, w: 10.1, h: 3.03 });
    table(s, [["Check", "Original", "Re-run (ORCD)"],
      ["UMAP trustworthiness, k = 15, seed 42", "0.874", "0.879"],
      ["PCA trustworthiness, same matrix", "0.805", "0.805"],
      ["UMAP seeds 43 / 44", "0.868 / 0.879", "0.878 / 0.870"],
      ["UMAP with 30 neighbours", "0.867", "0.860"],
      ["15-NN overlap with seed 42 (seeds 43 / 44)", "0.74 / 0.74", "0.75 / 0.73"]], { y: 4.35, fontSize: 14, colW: [6.1, 3.0, 3.0], rowH: 0.42 });
    s.addNotes("Original and re-run (ORCD job 25941523) side by side. Same seeds, different machine: UMAP is not bit-identical across platforms, and trustworthiness moved by at most 0.011; PCA matched exactly. The conclusion is unchanged: useful local structure with material layout and neighbourhood variation. Seeding alone does not make a stochastic method reproducible across environments; see ReproNim/reproseed (github.com/ReproNim/reproseed) for recording and propagating seeds. Source: codex_verification/orcd_rebuild/rebuild_comparison.md.\n\n" + fromOld(9, 10));
  }

  // ---------------------------------------------------------------- section tags (main slides)
  const O1 = "Objective 1", O2 = "Objective 2", AS = "With an assistant";
  const TAGS = {
    "The two example datasets": "Objectives 1 and 2", "A knowledge graph in four statements": O1, "Components of a dataset and a publication": O1, "Entities in a neuroimaging knowledge graph": O1,
    "Knowledge graph around a single participant": O1, "Linking a claim to its evaluation and cohort": O1, "Exercise: evaluating claims against a source": O1, "Quotation checks and scientific entailment": O1,
    "Joining graphs through shared identifiers": O2, "Harmonising graphs built by different people": O2, "Participant coverage by data element": O2, "ABIDE I: two analyses, two research questions": O2,
    "ABIDE I: group differences and site-held-out prediction": O2, "Exercise: consequences of a stricter motion threshold": O2, "Dependency tracing after a QC revision": O2,
    "Linking datasets, publications and abstracts": O2, "Asking Claude about the literature graph": O2, "Evaluation schemes in 74 ABIDE studies": O2, "ReproPond and ReproLake as attributes on graph records": O2,
    "Live demo: building a graph in Claude Code": AS, "Live demo: querying and using the graph": AS, "The lecture's own provenance graph": AS,
    "Practices to adopt now": "Objectives 1 and 2",
  };
  for (const [i, rec] of SLIDES.entries()) {
    const st = rec.section === MAIN ? STRIP[rec.title] : null;
    if (!st) continue;
    n += 1;
    rec.slide.addImage({ data: await icon(fa.FaProjectDiagram, "#0F7B7B", 128), x: 0.6, y: 1.06, w: 0.2, h: 0.2, objectName: `stripIcon${i}` });
    rec.slide.addText([{ text: "In the graph: ", options: { bold: true, color: C.accent1 } }, { text: st, options: { color: C.accent3 } }], { x: 0.88, y: 1.0, w: 12.0, h: 0.32, fontSize: 12, valign: "middle", margin: 0, isTextBox: true, objectName: `strip${i}` });
  }
  SLIDES.forEach((rec, i) => {
    const tag = rec.section === MAIN ? TAGS[rec.title] : null;
    if (!tag) return;
    const col = tag === O1 ? C.accent1 : tag === O2 ? C.text2 : tag === AS ? C.accent2 : C.accent3;
    rec.slide.addShape(pres.shapes.OVAL, { x: 10.2, y: 0.09, w: 0.14, h: 0.14, fill: { color: col }, line: { type: "none" }, objectName: `tagDot${i}` });
    rec.slide.addText(tag, { x: 10.4, y: 0.02, w: 2.5, h: 0.28, fontSize: 12, color: C.accent3, italic: true, valign: "middle", margin: 0, isTextBox: true, objectName: `tag${i}` });
  });

  // ---------------------------------------------------------------- badges and PROV export
  const missing = [];
  SLIDES.forEach((rec, i) => {
    const pv = SLIDE_PROV[rec.title];
    if (!pv) { missing.push(rec.title); return; }
    const dark = rec.master === "TITLE_DARK";
    const fill = dark ? "2F4A57" : "E3E9EC", fg = dark ? "FFFFFF" : "17303F", word = dark ? "C9D3D7" : "5E7A88";
    pv.production.forEach((L, k) => {
      rec.slide.addText(L, { shape: pres.shapes.OVAL, x: 0.3 + k * 0.33, y: 7.1, w: 0.29, h: 0.29, fill: { color: fill }, line: { type: "none" }, fontSize: 11, bold: true, color: fg, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: `badge${i}_${L}` });
    });
    const wordX = 0.36 + pv.production.length * 0.33, wordW = 0.08 * pv.checking.length + 0.1;
    const data = DATA[rec.title];
    if (data) {
      const fx = wordX + wordW + 0.15;
      rec.slide.addText("Data: " + data.join("; "), { x: fx, y: 7.08, w: 12.2 - fx, h: 0.33, fontSize: 11, color: dark ? "C9D3D7" : "5E7A88", valign: "middle", margin: 0, isTextBox: true, objectName: `data${i}` });
    }
    rec.slide.addText(pv.checking, { x: wordX, y: 7.08, w: wordW, h: 0.33, fontSize: 11, italic: true, color: word, valign: "middle", margin: 0, isTextBox: true, objectName: `badge${i}_check` });
  });
  if (missing.length) { console.error("No SLIDE_PROV entry for:", missing); process.exit(2); }
  const noStrip = SLIDES.filter((r) => r.section === MAIN && !STRIP[r.title] && !["Learning objectives", "Discussion"].includes(r.title) && r.master !== "TITLE_DARK").map((r) => r.title);
  if (noStrip.length) console.warn("Main slides without an In-the-graph strip:", noStrip);
  const esc = (t) => String(t).replace(/\\/g, "\\\\").replace(/"/g, '\\"');
  const iri = (src) => /^https?:/.test(src) ? `<${src}>` : `talk:file-${encodeURIComponent(src).replace(/%/g, "_")}`;
  const agentOf = { H: "talk:Speaker", L: "talk:LLMDrafter", A: "talk:CodingAgent", R: "talk:RetrievalAgent", M: "talk:BrainResearcherMCP", P: "talk:EarlierAgenticSession" };
  let ttl = `@prefix prov: <http://www.w3.org/ns/prov#> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n@prefix talk: <https://repronim.org/talks/kg-skills-2026#> .\n\n`;
  ttl += `talk:Speaker a prov:Agent, prov:Person ; rdfs:label "Speaker" .\n`;
  for (const [L, name, def] of PROD_DEF) ttl += `${agentOf[L]} a prov:Agent ; rdfs:label "${esc(name)}" ; rdfs:comment "${esc(def)}" .\n`;
  ttl += `talk:AutomatedChecks a prov:Agent, prov:SoftwareAgent ; rdfs:label "Automated checks (SHACL, schema, tests, render QA)" .\ntalk:IndependentRebuild a prov:Agent, prov:SoftwareAgent ; rdfs:label "Independent rebuild (ORCD)" .\ntalk:IndependentVerifier a prov:Agent, prov:SoftwareAgent ; rdfs:label "Independent agent checking claims against primary sources" .\n`;
  ttl += `talk:orcd-job-25941523 a prov:Activity ; rdfs:label "Clean rebuild of the ds000030 package on ORCD" ; talk:slurmJobId "25941523" ; prov:wasAssociatedWith talk:IndependentRebuild ; prov:used ${iri(CNP_ZIP)} .\n`;
  ttl += `talk:abide-clean-room-rebuild a prov:Activity ; rdfs:label "Clean-room rebuild of the ABIDE package from a fresh download" ; rdfs:comment "Ran in segments; 2,108/2,108 input hashes matched; 215/218 key numbers reproduced (the other 3 are run times); all 15 gold answers identical." ; prov:wasAssociatedWith talk:IndependentRebuild .\n`;
  ttl += `talk:orcd-job-25939932 a prov:Activity ; rdfs:label "ABIDE package run on a second machine (ORCD Linux node2803)" ; talk:slurmJobId "25939932" ; rdfs:comment "196/218 shared key numbers match within 1%; 15 differ only in run times or dates; 7 UMAP-derived values differ slightly; 9/12 shared gold answers identical (the rest differ in a snapshot timestamp or later wording)." ; prov:wasAssociatedWith talk:IndependentRebuild .\n`;
  ttl += `talk:claim-verification-2026-10-15 a prov:Activity ; rdfs:label "Claim verification against primary sources (39 confirmed, 0 contradicted, 1 could not access)" ; prov:wasAssociatedWith talk:IndependentVerifier .\n\n`;
  const sources = new Set();
  SLIDES.forEach((rec, i) => {
    const pv = SLIDE_PROV[rec.title], id = `talk:slide-${String(i + 1).padStart(2, "0")}`;
    ttl += `${id} a prov:Entity ; rdfs:label "${esc(rec.title)}" ; talk:section "${rec.section}" ; talk:position ${i + 1}`;
    pv.production.forEach((L) => { ttl += ` ;\n  prov:wasGeneratedBy ${id}-gen-${L}`; });
    pv.sources.forEach((src) => { sources.add(src); ttl += ` ;\n  prov:wasDerivedFrom ${iri(src)}`; });
    ttl += ` .\n`;
    pv.production.forEach((L) => { ttl += `${id}-gen-${L} a prov:Activity, talk:Production_${L} ; prov:wasAssociatedWith ${agentOf[L]} .\n`; });
    const evs = evidenceFor(rec.title, pv);
    ttl += `${id}-check a prov:Entity, talk:Assessment ; talk:assesses ${id} ; talk:checkingLabel "${esc(pv.checking)}"`;
    evs.forEach((e, k) => { ttl += ` ;\n  talk:hasEvidence ${id}-check-${k + 1}`; });
    ttl += ` .\n`;
    evs.forEach((e, k) => {
      ttl += `${id}-check-${k + 1} a prov:Entity, talk:CheckEvidence ; talk:checkingStatus "${e.status}"`;
      if (e.agent) ttl += ` ;\n  prov:wasAttributedTo ${e.agent}`;
      if (e.activity) ttl += ` ;\n  prov:wasGeneratedBy ${e.activity}`;
      if (e.file) { sources.add(e.file); ttl += ` ;\n  prov:wasDerivedFrom ${iri(e.file)}`; }
      ttl += ` .\n`;
    });
    ttl += `\n`;
  });
  for (const src of sources) ttl += `${iri(src)} a prov:Entity ; rdfs:label "${esc(src)}" .\n`;
  fs.writeFileSync(path.resolve(__dirname, "talk_provenance.ttl"), ttl);

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
}

main().catch((e) => { console.error(e); process.exit(1); });
