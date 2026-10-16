# /// script
# requires-python = ">=3.11"
# ///
"""Port a workspace build_deck.js into slides/ for this repository.

Rewrites absolute paths to repo-relative ones and replaces hand-entered experiment numbers
with V() lookups from slides/values_map.json. Every replacement that does not match is
reported, so a changed slide is fixed by hand rather than silently left hand-entered.

    uv run scripts/port_build_deck.py WORKSPACE/deck_build/build_deck.js
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATHS = [
    ('const { applyTheme } = require("./apply_theme.js");',
     'const { applyTheme } = require("./apply_theme.js");\nconst { V, ROOT } = require("./values.js");'),
    ('const OUT = path.resolve(__dirname, "../Knowledge_Graphs_Skills_Neuroimaging_v4.pptx");',
     'const OUT = path.resolve(__dirname, "Knowledge_Graphs_Skills_Neuroimaging_v4.pptx");'),
    ('const CNP_UMAP = "/Users/satra/.claude/jobs/ee89ed94/tmp/cnp/CNP_Harness_Experiment/experiment/results/phenotype_embedding.png";',
     'const CNP_UMAP = path.join(ROOT, "experiments/ds000030/experiment/results/phenotype_embedding.png");'),
    ('const EXP = "/Users/satra/Downloads/repronim-talk/ABIDE_Collaboration_Experiment";',
     'const EXP = path.join(ROOT, "experiments/abide");'),
    ('fs.writeFileSync(path.resolve(__dirname, "../talk_provenance.ttl"), ttl);',
     'fs.writeFileSync(path.resolve(__dirname, "talk_provenance.ttl"), ttl);'),
    ('const CNP_ZIP = "CNP_Dataset_Publication_Knowledge_Graph.zip";', 'const CNP_ZIP = "experiments/ds000030";'),
    ('const PLAN = "talk_plan.md";', 'const PLAN = "slides/talk_plan.md";'),
    ('const REBUILD = "codex_verification/orcd_rebuild/rebuild_comparison.md";',
     'const REBUILD = "experiments/ds000030/codex_verification/orcd_rebuild/rebuild_comparison.md";'),
    ('const VERIFY = "codex_verification/codex_claim_verification.md";',
     'const VERIFY = "experiments/ds000030/codex_verification/codex_claim_verification.md";'),
    ('const ABIDE_KEY = "ABIDE_Collaboration_Experiment/results/key_numbers.json";',
     'const ABIDE_KEY = "experiments/abide/results/key_numbers.json";'),
    ("slide.addImage({ path: file, x: x + ox,", "slide.addImage({ path: file, altText: path.basename(file), x: x + ox,"),
    ("s.addImage({ path: R.figure, x: 0.6,", "s.addImage({ path: R.figure, altText: path.basename(R.figure), x: 0.6,"),
    ("s.addImage({ path: CNP_UMAP, x: 1.6,", "s.addImage({ path: CNP_UMAP, altText: path.basename(CNP_UMAP), x: 1.6,"),
]

# Experiment numbers -> V() lookups (ids in slides/values_map.json).
VALUES = [
    ('publications: "598",', 'publications: V("pubs.openalex"),'),
    ('abstracts: "35",', 'abstracts: V("pubs.abstracts"),'),
    ('claims: "541",', 'claims: V("pubs.claims"),'),
    ('reviewed: "74",', 'reviewed: V("pubs.reviewed"),'),
    ('reconstructible: "17",', 'reconstructible: V("pubs.reconstructible"),'),
    ('cohorts: { aN: "441", bN: "767", both: "441", aOnly: "0", bOnly: "326", aRemoved: "69", bRemoved: "63" },',
     'cohorts: { aN: V("cohort.aN"), bN: V("cohort.bN"), both: V("cohort.aN"), aOnly: "0", bOnly: V("cohort.bOnly"), aRemoved: V("cohort.aRemoved"), bRemoved: V("cohort.bRemoved") },'),
    ('headline: "5,428 connections differ"', 'headline: `${V("a.edges")} connections differ`'),
    ('"FDR-corrected (false discovery rate); 99.6% weaker in ASD (95% CI 90.2–99.8%)"',
     '`FDR-corrected (false discovery rate); ${V("a.hypo")}% weaker in ASD (95% CI ${V("a.hypoLow")}–${V("a.hypoHigh")}%)`'),
    ('"52% of the weaker connections link the two hemispheres"', '`${V("a.interhem")}% of the weaker connections link the two hemispheres`'),
    ('"median effect size d = 0.30 (difference in SD units) · n = 441, 9 sites"', '`median effect size d = ${V("a.medianD")} (difference in SD units) · n = ${V("cohort.aN")}, ${V("a.sites")} sites`'),
    ('"Reviewed by B: not established in held-out participants (pooled d −0.08, −0.31 to 0.15)"',
     '`Reviewed by B: not established in held-out participants (pooled d ${V("rev.d")}, ${V("rev.dLow")} to ${V("rev.dHigh")})`'),
    ('headline: "AUC 0.74 (0.70–0.77)"', 'headline: `AUC ${V("b.auc")} (${V("b.aucLow")}–${V("b.aucHigh")})`'),
    ('"AUC: 0.5 = chance, 1 = perfect · tangent-space connectivity · tested on held-out sites, n = 767, 20 sites"',
     '`AUC: 0.5 = chance, 1 = perfect · tangent-space connectivity · tested on held-out sites, n = ${V("cohort.bN")}, ${V("b.sites")} sites`'),
    ('"correlation 0.72 · demographic + head motion 0.59 · demographic only 0.48"',
     '`correlation ${V("b.corr")} · demographic + head motion ${V("b.demofd")} · demographic only ${V("b.demo")}`'),
    ('"accuracy 66.9%; Abraham 2017 reported 66.8% on its own 871-participant cohort"', '`accuracy ${V("b.acc")}%; Abraham 2017 reported 66.8% on its own 871-participant cohort`'),
    ('"Reviewed by A: top edges overlap A\'s 90 vs 54 expected (p ≈ 4e−8)"',
     '`Reviewed by A: top edges overlap A\'s ${V("rev.overlap")} vs ${V("rev.expected")} expected (p ≈ 4e−8)`'),
    ('{ value: "63", label: "of B\'s 767 participants excluded" }', '{ value: V("cohort.bRemoved"), label: `of B\'s ${V("cohort.bN")} participants excluded` }'),
    ('{ value: "17 / 20", label:', '{ value: `${V("reveal.foldsAffected")} / ${V("reveal.folds")}`, label:'),
    ('{ value: "0 / 9", label:', '{ value: `${V("reveal.changed")} / ${V("reveal.families")}`, label:'),
    ('"604 of B\'s 767 with age, FIQ, VIQ and PIQ; 15 sites",', '`${V("umap.n")} of B\'s ${V("cohort.bN")} with age, FIQ, VIQ and PIQ; ${V("umap.sites")} sites`,'),
    ('"trustworthiness 0.977 (PCA 0.920); other seeds 0.973, 0.974",', '`trustworthiness ${V("umap.trust")} (PCA ${V("umap.pca")}); other seeds ${V("umap.seed1")}, ${V("umap.seed2")}`,'),
    # joins slide
    ('src: "ReproNim\'s ABIDE records, 27 sites", key: "participant ID", result: "1,112 / 1,112 matched, none left over · 1,035 with time series · 767 in B\'s cohort (reviewed link, not declared identical)" }',
     'src: `ReproNim\'s ABIDE records, ${V("joins.sites")} sites`, key: "participant ID", result: `${V("joins.matched")} / ${V("elements.participants")} matched, none left over · ${V("joins.timeseries")} with time series · ${V("joins.inB")} in B\'s cohort (reviewed link, not declared identical)` }'),
    ('result: "35 abstracts · 17 state data use · 15 / 17 correct on hand check" }', 'result: `${V("pubs.abstracts")} abstracts · ${V("pubs.statedUse")} state data use · 15 / ${V("pubs.statedUse")} correct on hand check` }'),
    ('result: "598 works cite Di Martino 2014 and name ABIDE" }', 'result: `${V("pubs.openalex")} works cite Di Martino 2014 and name ABIDE` }'),
    # dataset counts (source tables)
    ('"272 adults: 130 controls, 50 schizophrenia, 49 bipolar disorder, 43 ADHD"',
     '`${V("ds.total")} adults: ${V("ds.control")} controls, ${V("ds.schz")} schizophrenia, ${V("ds.bipolar")} bipolar disorder, ${V("ds.adhd")} ADHD`'),
    ('"1,112 participants (539 autistic, 573 typically developing) from 17 sites (20 site codes in the data)"',
     '`${V("abide.total")} participants (${V("abide.asd")} autistic, ${V("abide.td")} typically developing) from 17 sites (20 site codes in the data)`'),
    ('"200-region time series for 1,035 participants"', '`200-region time series for ${V("abide.timeseries")} participants`'),
    ('"→ 272 participants and their scores"', '`→ ${V("ds.total")} participants and their scores`'),
    ('["Participants and phenotypes", "272 participants; 52 tables, 1,983 columns"]', '["Participants and phenotypes", `${V("ds.total")} participants; 52 tables, 1,983 columns`]'),
]


def port(text):
    misses = []
    for old, new in PATHS + VALUES:
        if old in text:
            text = text.replace(old, new)
        else:
            misses.append(old)
    text = text.replace('"ABIDE_Collaboration_Experiment/', '"experiments/abide/')
    text = text.replace('x.startsWith("ABIDE_Collaboration_Experiment")', 'x.startsWith("experiments/abide")')
    text = text.replace("deck_build/build_deck.js", "slides/build_deck.js")
    text = text.replace("deck_build/demo/", "slides/demo/").replace("deck_build/prov_query.py", "slides/prov_query.py")
    text = re.sub(r'const DEMO_SOURCE = "[^"]*";', 'const DEMO_SOURCE = path.join(__dirname, "demo/claude_code_demo.md");', text)
    return text, misses


def main(src):
    text, misses = port(Path(src).read_text())
    (ROOT / "slides/build_deck.js").write_text(text)
    left = [ln for ln in text.splitlines() if "/Users/" in ln]
    for m in misses:
        print("NOT FOUND:", m[:110])
    for ln in left:
        print("ABSOLUTE PATH LEFT:", ln.strip()[:110])
    print(f"{len(misses)} replacements not found, {len(left)} absolute paths left")


if __name__ == "__main__":
    main(sys.argv[1])
