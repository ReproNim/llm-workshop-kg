"""Step 4: synthesis computed from charted values only -> results_synthesis.json + synthesis.md.

Every categorical value is derived from a charted field by a rule below. The two hand-curated
tables (EVAL and ACC) assign evaluation schemes and headline accuracies; each entry carries a
snippet that must occur verbatim in that paper's charted text, and the script fails if it does not.
"""
import collections
import json
import re
from common import ROOT, norm

RECS = json.load(open(ROOT / "phase3" / "records_verified.json"))
INTEGRITY = json.load(open(ROOT / "phase3" / "integrity.json"))
CORPUS_TITLES = {e["pmid"]: (e["title"], e.get("authors", ""), e.get("year", ""))
                 for e in json.load(open(ROOT / "corpus.json"))["items"]}
K = {
    "CL6": "CL6 Site handling reported (site covariate, harmonisation e.g. ComBat, or leave-site-out evaluation)?",
    "CL7": "CL7 Code and/or participant list available?",
}

# ---- evaluation schemes, from charted validation_methodology / RQ4 (snippet must be in that text) ----
POOLED, LOOCV, SPLIT, LSO, EXT, WITHIN, NR, OTHER = (
    "pooled k-fold CV", "leave-one-subject-out CV", "single train/test split", "leave-site-out",
    "external dataset", "within-site only", "not reported", "other")
SCHEMES = [POOLED, LOOCV, SPLIT, LSO, EXT, WITHIN, OTHER, NR]
EVAL = {
    "S-002": ([LSO, WITHIN], "Leave-one-site-out cross-validation (inter-site) and intra-site cross-validation"),
    "S-004": ([NR], "Not reported (no train/test split ratio or cross-validation scheme described)"),
    "S-005": ([LOOCV], "Leave-one-out cross-validation (LOOCV) for SRS prediction"),
    "S-006": ([POOLED, EXT], "10-fold cross-validation on ABIDE-I; independent held-out test on ABIDE-II"),
    "S-009": ([EXT], "cross-cohort replication/prediction in independent ABIDE I sample"),
    "S-010": ([EXT], "ABIDE I and ABIDE II used as untouched external test sets"),
    "S-011": ([OTHER], "Propensity-score-based stratified train/holdout partitioning"),
    "S-014": ([POOLED, WITHIN], "10-fold cross-validation; evaluated on whole ABIDE I CPAC dataset"),
    "S-016": ([POOLED], "Nested 10-fold cross-validation"),
    "S-019": ([POOLED], "10-fold stratified cross-validation"),
    "S-020": ([WITHIN], "5-fold cross-validation within each site/strategy"),
    "S-021": ([LOOCV], "Leave-one-subject-out cross-validation across all 964 subjects"),
    "S-022": ([POOLED, LSO], "10-fold cross-validation (primary); leave-site-out evaluation across all 17 ABIDE I sites"),
    "S-023": ([SPLIT], "70/30 train/hold-out split"),
    "S-024": ([SPLIT], "Random subject/pair split into training and test sets ensuring all 20 sites present in both"),
    "S-025": ([WITHIN], "5-fold cross-validation (stratified by ASD/NC proportion) per target site"),
    "S-027": ([SPLIT], "Single random 70/30 split"),
    "S-028": ([POOLED, WITHIN], "10-fold cross-validation on the whole ABIDE-I dataset; separate 5-fold cross-validation per site"),
    "S-029": ([POOLED], "Nested 10x10-fold cross-validation"),
    "S-030": ([POOLED, LSO], "Five-fold cross-validation (with an inner training/validation split) and a separate leave-site-out cross-validation"),
    "S-032": ([SPLIT], "final single evaluation on a held-out test set"),
    "S-033": ([POOLED], "10-fold cross-validation per age group"),
    "S-034": ([POOLED], "10-fold cross-validation"),
    "S-036": ([SPLIT, WITHIN], "Single random 85%/15% training/testing split; per-site (unit-site) classification also evaluated"),
    "S-049": ([POOLED], "Five-fold cross-validation"),
    "S-052": ([POOLED, WITHIN], "10-fold cross-validation (hyperparameters set via nested cross-validation), plus a supplementary intra-site stratified shuffle-split"),
    "S-053": ([POOLED], "Fivefold cross-validation (random split, pooled across sites; no leave-site-out)"),
    "S-054": ([NR], "Not reported"),
    "S-055": ([LOOCV], "Leave-One-Out Cross-Validation"),
    "S-056": ([SPLIT], "Single train/test split"),
    "S-058": ([POOLED, WITHIN], "5-fold cross-validation, run separately for the NYU single-site, UM single-site, and ABIDE-I 19-site multi-site cohorts"),
    "S-059": ([WITHIN], "evaluated separately on NYU and UM single-site cohorts"),
    "S-060": ([WITHIN], "single-site design"),
    "S-062": ([LSO], "Leave-one-site-out cross-validation across KKI, NYU, UCLA, UM"),
    "S-063": ([POOLED], "10-fold cross-validation for mean test accuracy"),
    "S-064": ([SPLIT], "Single fixed train/validation/test split"),
    "S-066": ([POOLED], "10-fold stratified cross-validation"),
    "S-067": ([POOLED], "Stratified five-fold cross-validation"),
    "S-069": ([POOLED], "10-fold cross-validation (pooled across sites; no leave-site-out)"),
    "S-070": ([SPLIT], "Single 8:2 train/test split"),
    "S-071": ([LSO], "Leave-one-site-out inter-site cross-validation across all 17 ABIDE I sites"),
    "S-072": ([POOLED, LSO], "Intra-site 5-fold cross-validation (pooled and site-balanced variants) and inter-site leave-one-site-out"),
    "S-074": ([POOLED], "10-fold stratified cross-validation"),
    "S-076": ([POOLED, WITHIN], "Pooled 10-fold cross-validation across all 17 sites"),
    "S-077": ([POOLED], "Stratified 10-fold cross-validation"),
    "S-078": ([LOOCV], "Leave-one-out cross-validation"),
    "S-081": ([SPLIT], "Single random balanced split-half train/test split"),
    "S-090": ([POOLED], "Pooled 10-fold cross-validation (no leave-site-out)"),
    "S-091": ([EXT], "independently validated (group difference, correlation, and ROC/AUC) on a separate local (KMUH) cohort"),
    "S-092": ([LOOCV], "Leave-one-out cross-validation and split-half cross-validation"),
    "S-096": ([POOLED], "5-fold stratified cross-validation"),
    "S-097": ([POOLED], "k-fold cross-validation (5-, 10-, 15-fold reported in a results table)"),
    "S-099": ([POOLED, WITHIN], "10-fold cross-validation (combined all-site dataset) and 5-fold cross-validation (site-wise)"),
}
# ---- headline accuracy per (paper, scheme): best reported value for the paper's own model ----
# (sid, scheme, value %, snippet in charted key_performance_results, basis)
ACC = [
    ("S-002", LSO, 66.8, "Best inter-site accuracy 66.8%", "best"),
    ("S-004", NR, 81.56, "ABIDE-I+II complete: CNN 81.56% acc", "best"),
    ("S-006", POOLED, 73.3, "73.3% 10-fold CV accuracy on ABIDE-I", "best"),
    ("S-006", EXT, 71.7, "71.7% independent test accuracy on ABIDE-II", "best"),
    ("S-014", POOLED, 75.20, "Whole dataset (N=1035): 75.20% accuracy", "best"),
    ("S-014", WITHIN, 96.40, "NYU subset (N=175): 96.40% accuracy", "single site"),
    ("S-019", POOLED, 70.4, "70.4% accuracy", "best"),
    ("S-020", WITHIN, 84.9, "USM 0.849", "best single site (no average reported)"),
    ("S-021", LOOCV, 60.0, "Best whole-brain classification accuracy was 60%", "best"),
    ("S-022", POOLED, 70.22, "CNN achieved 70.22% 10-fold CV accuracy", "best"),
    ("S-023", SPLIT, 64.3, "hold-out accuracy on ABIDE = 0.643", "best"),
    ("S-024", SPLIT, 62.9, "62.9% across all sites", "best"),
    ("S-025", WITHIN, 67.1, "averaged across sites DTL-NN reached 67.1% accuracy", "average across sites"),
    ("S-027", SPLIT, 96.15, "96.15% accuracy", "best"),
    ("S-028", POOLED, 70.8, "comparable accuracy (70.8%)", "best"),
    ("S-028", WITHIN, 64.42, "The average accuracy achieved by ASD-SAENet model was 64.42%", "average across sites"),
    ("S-029", POOLED, 68.0, "SVM accuracy increased to 68%", "best"),
    ("S-030", POOLED, 64.0, "balanced accuracy 64%", "best (balanced accuracy)"),
    ("S-030", LSO, 56.0, "dropped to 56% balanced accuracy", "best (balanced accuracy)"),
    ("S-032", SPLIT, 65.0, "Functional+PCD 65.0% (best)", "best"),
    ("S-033", POOLED, 95.0, "~95% accuracy", "best age group"),
    ("S-034", POOLED, 70.86, "accuracy 70.86%", "best"),
    ("S-036", WITHIN, 85.0, "Unit-site classification accuracy up to 85%", "best single site (no average reported)"),
    ("S-052", POOLED, 72.2, "Pooled 10-fold CV: accuracy 72.2%", "best"),
    ("S-052", WITHIN, 67.7, "mean accuracy 67.7%", "average across sites"),
    ("S-053", POOLED, 68.02, "accuracy 68.02%", "best"),
    ("S-054", NR, 94.7, "Accuracy 94.7%", "best"),
    ("S-055", LOOCV, 74.8, "74.8% (m=3)", "best"),
    ("S-056", SPLIT, 87.0, "ResNet-50 test accuracy 87.0%", "best"),
    ("S-058", POOLED, 58.0, "accuracy 0.58", "best"),
    ("S-058", WITHIN, 77.0, "NYU accuracy 0.77", "best single site (no average reported)"),
    ("S-059", WITHIN, 79.5, "accuracy 0.795", "best single site (no average reported)"),
    ("S-060", WITHIN, 77.74, "77.74% accuracy", "single site"),
    ("S-062", LSO, 71.0, "accuracy 0.71", "best"),
    ("S-064", SPLIT, 73.5, "Average accuracy 0.735", "average across atlases"),
    ("S-066", POOLED, 88.09, "accuracy 88.09", "best"),
    ("S-067", POOLED, 73.71, "accuracy 73.71", "best"),
    ("S-069", POOLED, 74.74, "accuracy 74.74%", "best"),
    ("S-070", SPLIT, 72.46, "accuracy of 72.46%", "best"),
    ("S-071", LSO, 73.4, "73.4% (CC200 atlas)", "best"),
    ("S-072", POOLED, 60.0, "intra-site 5-fold CV ~60% accuracy", "best"),
    ("S-072", LSO, 62.0, "MLP accuracy ~62%", "best"),
    ("S-074", POOLED, 83.7, "accuracy 83.7", "best"),
    ("S-076", POOLED, 82.9, "Average ACC 82.9%", "best"),
    ("S-076", WITHIN, 75.6, "75.6%", "average across sites"),
    ("S-077", POOLED, 96.91, "96.91% accuracy", "best"),
    ("S-078", LOOCV, 89.0, "accuracy rates are 89 and 84%", "best (single site)"),
    ("S-081", SPLIT, 62.0, "~62% accuracy", "best"),
    ("S-090", POOLED, 73.57, "accuracy 73.57%", "best"),
    ("S-096", POOLED, 69.2, "69.2% accuracy", "best"),
    ("S-097", POOLED, 86.5, "86.5 +/- 2.4% accuracy", "10-fold CV"),
    ("S-099", POOLED, 82.0, "combined 17-site dataset: 82%", "best"),
]
# accuracy not charted (AUC / correlation / relative change only)
NO_ACC_NOTE = {
    "S-005": "regression of SRS (r)", "S-009": "regression of ADOS/SRS", "S-010": "AUROC only",
    "S-011": "AUC/F1 correlations only", "S-016": "AUC only", "S-049": "no ASD accuracy table in text",
    "S-063": "relative change only", "S-091": "AUC only", "S-092": "regression (rs)",
    "S-022": None, "S-002": None,
}
LEAK_PATTERNS = [
    ("feature selection outside CV", r"f-score feature selection|feature selection may not|recursive feature elimination via a ridge classifier is described prior|sffs feature selection are both fit on the full dataset"),
    ("harmonisation/deconfounding outside CV", r"deconfounding .* using all available participants|harmoni[sz]ation of structural and functional features was fit on the full cohort"),
    ("tuning on the test set", r"selected by maximising accuracy on the same"),
    ("unsupervised feature derivation on full sample", r"group-ica and dual regression appear to have been performed on the full sample"),
]


def charted_text(r):
    c = r.get("charting", {})
    return " ".join([c.get("validation_methodology", ""), c.get("key_performance_results", ""),
                     c.get("custom_fields", {}).get("RQ4", ""), c.get("custom_fields", {}).get("RQ5", ""),
                     r.get("kg_link", {}).get("finding", "")])


def first_word(s):
    s = (s or "").strip()
    m = re.match(r"(yes|partly|partial|no|n/a)\b", s, re.I)
    return m.group(1).lower() if m else ("not reported" if not s else "other")


def pipeline_cats(p):
    t = norm(p)
    t = re.sub(r"similar to c-pac", "", t)
    cats = []
    rules = [("CPAC", r"c-?pac\b|configurable pipeline"), ("DPARSF", r"dparsf"),
             ("CCS", r"\bccs\b|connectome computation system"), ("NIAK", r"\bniak\b"),
             ("fMRIPrep", r"fmriprep"), ("CONN", r"\bconn\b"), ("GRETNA", r"gretna"),
             ("fconn1000", r"fconn1000"), ("Athena", r"athena")]
    for name, rx in rules:
        if re.search(rx, t):
            cats.append(name)
    if not cats:
        if not t or re.search(r"not reported|deferred to an unavailable|not described", t):
            cats = ["not reported"]
        elif re.search(r"spm|fsl|afni|custom|in-house|lab-made|matlab|slice-time|mricron|none \(", t):
            cats = ["custom (SPM/FSL/AFNI/in-house)"]
        else:
            cats = ["other"]
    return cats


ATLAS_RULES = [
    ("CC200", r"cc ?200|craddock[ -]?200|craddock 200|craddock cc200"), ("CC400", r"cc ?400|craddock cc200 and cc400"),
    ("AAL", r"\baal|automated anatomical labell?ing"), ("Harvard-Oxford", r"harvard|\bho\b"),
    ("Eickhoff-Zilles (EZ)", r"\bez\b|eickhoff"), ("Talairach (TT)", r"\btt\b|tt_daemon|talairach"),
    ("Dosenbach 160", r"dosenbach|dos160"), ("MSDL", r"msdl"), ("BASC", r"basc"), ("Schaefer", r"schaefer"),
    ("Power 264", r"power"), ("Shen 268", r"shen"), ("ICA / data-driven networks", r"\bica\b|group-ica|rsn10"),
    ("Craddock (other scale)", r"craddock \(249"), ("Brodmann", r"brodmann"),
    ("random parcellation", r"random parcellation"), ("Desikan-Killiany (structural)", r"desikan"),
    ("Yeo", r"\byeo\b"),
]


def atlas_cats(a):
    t = norm(a).replace("schaefer-yeo", "schaefer")
    if re.search(r"parcellation not stated|not stated", t):
        return ["not reported / not applicable"]
    cats = [n for n, rx in ATLAS_RULES if re.search(rx, t)]
    if not cats:
        if not t:
            cats = ["not reported / not applicable"]
        elif re.search(r"none|voxel|seed|vertex|lattice", t):
            cats = ["none (voxel/seed/vertex-wise)"]
        else:
            cats = ["other"]
    return cats


LSO_S, HARM, COV, FEAT, PERSITE, OTH, SINGLE, NONE = (
    "leave-site-out evaluation", "ComBat/NeuroHarmonize harmonisation", "site covariate / regressed out",
    "site used as a model input or graph feature", "per-site analyses", "other site control", "single site",
    "none reported")
SITE_ORDER = [LSO_S, HARM, COV, OTH, PERSITE, FEAT, SINGLE, NONE]
# (categories, snippet that must occur in the charted CL6 answer/quote + RQ4 + kg pipeline/sites)
SITE = {
    "S-002": ([LSO_S], "leave-one-site-out"), "S-004": ([PERSITE], "results are tabulated separately per site"),
    "S-005": ([HARM, LSO_S], "comBat site harmonisation"), "S-006": ([NONE], "no site covariate or harmonisation"),
    "S-007": ([COV], "one-hot-encoded covariate"), "S-008": ([HARM], "comBat used to remove site"),
    "S-009": ([LSO_S], "leave-one-site-out analysis for site-effect check"),
    "S-010": ([NONE], "no site covariate, harmonisation, or leave-site-out"),
    "S-011": ([HARM, OTH], "propensity-score covariates, and ComBat"), "S-012": ([COV], "site included as a covariate"),
    "S-014": ([NONE], "no site covariate, harmonisation, or leave-site-out"),
    "S-015": ([COV], "age/site/sex regressed out"), "S-016": ([HARM], "neuroharmonize"),
    "S-019": ([FEAT], "taking into account SEX and SITE"), "S-020": ([OTH], "federated-learning design"),
    "S-021": ([COV], "site were included as covariates"), "S-022": ([LSO_S], "leave-site-out evaluation was performed"),
    "S-023": ([OTH], "site-only baseline classifier"), "S-024": ([OTH], "all 20 sites are included in both training and test"),
    "S-025": ([COV], "explicitly regressed out of FC weights"), "S-026": ([OTH], "matched on age"),
    "S-027": ([SINGLE], "matching a single scan protocol"), "S-028": ([PERSITE], "5-fold cross validation for each site"),
    "S-029": ([OTH], "per-site z-standardization"), "S-030": ([LSO_S], "leave-site-out cross-validation"),
    "S-032": ([FEAT], "personal-characteristic input feature"), "S-033": ([NONE], "no explicit site covariate"),
    "S-034": ([NONE], "no leave-site-out or site covariate"), "S-036": ([PERSITE], "unit-site classification"),
    "S-038": ([NONE], "No"), "S-039": ([HARM], "comBat"), "S-041": ([NONE], "no site covariate"),
    "S-043": ([COV], "imaging sites were included as nuisance covariates"), "S-044": ([COV, OTH], "regressing out site"),
    "S-045": ([NONE], "No"), "S-047": ([PERSITE], "held independently for NYU"), "S-049": ([NONE], "no ABIDE-specific"),
    "S-052": ([PERSITE], "intra-site stratified shuffle-split"), "S-053": ([NONE], "no site covariate"),
    "S-054": ([SINGLE], "single-site"), "S-055": ([NONE], "no leave-site-out evaluation"),
    "S-056": ([NONE], "no site covariate"), "S-058": ([NONE], "no site covariate"), "S-059": ([PERSITE], "evaluated separately for NYU and UM"),
    "S-060": ([SINGLE], "single-site"), "S-062": ([LSO_S], "leave-one-site-out"), "S-063": ([NONE], "no site covariate"),
    "S-064": ([NONE], "no site covariate"), "S-066": ([FEAT], "site is incorporated as a demographic feature"), "S-067": ([NONE], "no site covariate"),
    "S-069": ([NONE], "no site covariate"), "S-070": ([NONE], "no leave-site-out or ComBat"),
    "S-071": ([LSO_S], "leave-one-site-out"), "S-072": ([LSO_S, OTH], "site-balanced"),
    "S-074": ([NONE], "no site covariate"), "S-075": ([NONE], "No"), "S-076": ([PERSITE], "per-site 5-fold cross-validation"),
    "S-077": ([FEAT], "phenotypic edge-weight feature"), "S-078": ([SINGLE], "single site"), "S-080": ([HARM], "comBat harmonization"),
    "S-081": ([NONE], "no site covariate"), "S-082": ([SINGLE], "single-site"), "S-086": ([SINGLE], "single-site"),
    "S-088": ([NONE], "without a stated site covariate"), "S-090": ([NONE], "no site covariate"),
    "S-091": ([NONE], "no site covariate"), "S-092": ([OTH], "masked out"), "S-093": ([OTH], "excluded outright"),
    "S-094": ([NONE], "no explicit site covariate"), "S-096": ([NONE], "no site covariate"), "S-097": ([NONE], "no site covariate"),
    "S-098": ([HARM, COV, OTH], "site-wise de-meaning"), "S-099": ([NONE], "ignoring the sites intrinsic variability"),
}


def site_cats(r):
    sid = r["source_id"]
    cats, snip = SITE[sid]
    cf = r["charting"]["custom_fields"]
    hay = norm(cf.get(K["CL6"], "") + " " + cf.get("RQ4", "") + " " + r["kg_link"].get("pipeline", "") + " " + str(r["kg_link"].get("sites", "")))
    assert norm(snip) in hay, f"SITE snippet not charted: {sid}: {snip}"
    fw = first_word(cf.get(K["CL6"], ""))
    if cats == [NONE]:
        assert fw == "no", (sid, fw)
    return cats


def main():
    inc = [r for r in RECS if r["screening"]["decision"] == "include"]
    exc = [r for r in RECS if r["screening"]["decision"] == "exclude"]
    res = {"_note": "Computed by phase3/s4_synthesis.py from charted values in phase3/records_verified.json. "
                    "Counts are of included articles unless stated."}
    # ---- screening ----
    reasons = collections.Counter()
    for r in exc:
        m = re.search(r"Exclusion (\d)", r["screening"]["reason"])
        lab = {"3": "Exclusion 3: structural/DTI/phenotype-only ABIDE use (no resting-state analysis)",
               "4": "Exclusion 4: ABIDE used only for methods benchmarking, no autism-vs-control analysis"}[m.group(1)]
        reasons[lab] += 1
    res["screening"] = {
        "assessed_for_eligibility": len(RECS), "included": len(inc), "excluded": len(exc),
        "excluded_reasons": dict(reasons),
        "assessed_on": dict(collections.Counter(r["screening"]["assessed_on"] for r in RECS)),
        "full_text_mismatched": INTEGRITY["mismatched"],
        "excluded_ids": {lab: [r["source_id"] for r in exc if f"Exclusion {lab.split(':')[0][-1]}" in r["screening"]["reason"]] for lab in reasons},
    }
    # ---- release, claim type ----
    res["release"] = dict(collections.Counter(r["kg_link"]["dataset"] for r in inc))
    res["claim_type"] = dict(collections.Counter(r["kg_link"]["claim_type"] for r in inc))
    rq3 = collections.Counter(r["charting"]["custom_fields"]["RQ3"].split()[0].strip(" —-|").lower() for r in inc)
    res["claim_type_rq3_crosscheck"] = dict(rq3)
    # ---- evaluation ----
    pred = [r for r in inc if r["kg_link"]["claim_type"] in ("predictive", "both")]
    pred_ids = sorted(r["source_id"] for r in pred)
    assert sorted(EVAL) == pred_ids, (set(EVAL) ^ set(pred_ids))
    by = {r["source_id"]: r for r in inc}
    for sid, (schemes, snip) in EVAL.items():
        c = by[sid]["charting"]
        hay = norm(c.get("validation_methodology", "") + " " + c["custom_fields"].get("RQ4", ""))
        assert norm(snip) in hay, f"EVAL snippet not in charted text: {sid}: {snip}"
    for sid, sch, val, snip, _ in ACC:
        assert sch in EVAL[sid][0], (sid, sch)
        assert norm(snip) in norm(charted_text(by[sid])), f"ACC snippet not charted: {sid}: {snip}"
    scheme_counts = collections.Counter(s for v in EVAL.values() for s in v[0])
    leak = {}
    for r in pred:
        for a in r["risk_of_bias"].get("assessments", []):
            if a["domain"] == "Analysis" and a["judgment"] == "High":
                for lab, rx in LEAK_PATTERNS:
                    if re.search(rx, norm(a["support"])):
                        leak[r["source_id"]] = lab
    analysis = collections.Counter()
    for r in pred:
        j = [a["judgment"] for a in r["risk_of_bias"].get("assessments", []) if a["domain"] == "Analysis"]
        analysis[j[0] if j else "no PROBAST Analysis domain charted"] += 1
    overall = collections.Counter(r["risk_of_bias"].get("overall", "") or "not charted" for r in pred)
    acc_rows = [{"source_id": s, "scheme": sch, "accuracy_pct": v, "charted_snippet": sn, "basis": b,
                 "leakage_flag": leak.get(s, ""), "title": by[s]["charting"].get("title", ""),
                 "year": by[s]["charting"].get("year", ""), "n_total": by[s]["kg_link"]["n_by_dx"].get("total")}
                for s, sch, v, sn, b in ACC]
    dist = {}
    for sch in SCHEMES:
        vals = sorted(x["accuracy_pct"] for x in acc_rows if x["scheme"] == sch)
        clean = sorted(x["accuracy_pct"] for x in acc_rows if x["scheme"] == sch and not x["leakage_flag"])
        if vals:
            med = lambda v: (v[len(v) // 2] if len(v) % 2 else (v[len(v) // 2 - 1] + v[len(v) // 2]) / 2) if v else None
            dist[sch] = {"n_papers_with_accuracy": len(vals), "min": vals[0], "median": med(vals), "max": vals[-1],
                         "n_leakage_flagged": len(vals) - len(clean), "median_excluding_leakage_flagged": med(clean)}
    paired = []
    for s in sorted({x["source_id"] for x in acc_rows}):
        d = {x["scheme"]: x["accuracy_pct"] for x in acc_rows if x["source_id"] == s}
        if len(d) > 1:
            paired.append({"source_id": s, **d})
    res["evaluation"] = {
        "n_predictive_or_both": len(pred), "papers_per_scheme": {k: scheme_counts.get(k, 0) for k in SCHEMES},
        "schemes_per_paper": {k: v[0] for k, v in sorted(EVAL.items())},
        "papers_with_leave_site_out": sorted(k for k, v in EVAL.items() if LSO in v[0]),
        "papers_with_charted_accuracy": len({x["source_id"] for x in acc_rows}),
        "papers_without_charted_accuracy": {s: n for s, n in NO_ACC_NOTE.items() if n},
        "accuracy_by_scheme": dist, "accuracy_rows": acc_rows,
        "within_paper_comparisons": paired,
        "probast_analysis_judgment": dict(analysis), "probast_overall": dict(overall),
        "leakage_flagged": leak, "leakage_flag_rule":
            "PROBAST Analysis = High AND the charted support names feature selection, harmonisation/"
            "deconfounding, hyperparameter/feature-number tuning, or unsupervised feature derivation done on "
            "data outside the training folds.",
    }
    # ---- pipeline / atlas / site / reconstructibility / availability ----
    analysed = [r for r in inc if r["kg_link"]["claim_type"] != "descriptor"]
    pc, ac, sc = collections.Counter(), collections.Counter(), collections.Counter()
    per = {}
    for r in analysed:
        p, a, s = pipeline_cats(r["kg_link"]["pipeline"]), atlas_cats(r["kg_link"]["atlas"]), site_cats(r)
        per[r["source_id"]] = {"pipeline": p, "atlas": a, "site_handling": s}
        pc.update(p); ac.update(a); sc.update(s)
    res["pipeline"] = {"n_papers": len(analysed), "counts_multi_label": dict(pc.most_common())}
    res["atlas"] = {"n_papers": len(analysed), "counts_multi_label": dict(ac.most_common())}
    pso = collections.Counter(x for r in pred for x in per[r["source_id"]]["site_handling"])
    res["site_handling"] = {"n_papers": len(analysed), "n_predictive": len(pred),
                            "counts_multi_label": {k: sc.get(k, 0) for k in SITE_ORDER},
                            "predictive_only": {k: pso.get(k, 0) for k in SITE_ORDER},
                            "other_site_control_detail": "site-wise z-scaling (S-029), de-meaning (S-098), masking site-differing edges (S-092), excluding problem sites (S-093), propensity/age matching (S-011, S-026, S-044), site-only confound check (S-023), site-stratified split (S-024), federated per-site training (S-020), site-balanced variant (S-072)"}
    res["per_paper_categories"] = per
    recon = collections.Counter(r["kg_link"]["reconstructible"] for r in inc)
    res["reconstructibility_RQ6"] = {"detail": dict(recon), "summary": {
        "yes": sum(v for k, v in recon.items() if k.startswith("yes")),
        "partly": recon.get("partly", 0), "no": recon.get("no", 0)}}
    cl7 = collections.Counter(first_word(r["charting"]["custom_fields"][K["CL7"]]) for r in inc)
    code = sum(1 for r in inc if re.search(r"github|code (is )?(public|released|available)|source code|code,|code only|matlab code|code repository on|code and evaluations publicly", norm(r["charting"]["custom_fields"][K["CL7"]])) and not norm(r["charting"]["custom_fields"][K["CL7"]]).startswith("no"))
    plist = sum(1 for r in inc if r["kg_link"]["reconstructible"] == "yes — participant list")
    res["availability_CL7"] = {"cl7_answer": dict(cl7), "code_released_mentioned": code,
                               "participant_list_released (RQ6)": plist}
    # ---- shared cohorts: identical release + N by diagnosis (or total when only total charted) ----
    groups = collections.defaultdict(list)
    for r in analysed:
        n = r["kg_link"]["n_by_dx"]
        if not n.get("total"):
            continue
        key = (r["kg_link"]["dataset"], n.get("total"), n.get("ASD"), n.get("TD"))
        groups[key].append(r)
    # attach total-only papers to a full-key group with the same release + total
    merged = {}
    for key, rs in groups.items():
        merged.setdefault(key, []).extend(rs)
    for key in [k for k in merged if k[2] is None]:
        twins = [k for k in merged if k[0] == key[0] and k[1] == key[1] and k[2] is not None]
        if len(twins) == 1:
            merged[twins[0]].extend(merged.pop(key))
    shared = []
    for (ds, tot, asd, td), rs in sorted(merged.items(), key=lambda kv: (-len(kv[1]), -kv[0][1])):
        if len(rs) < 2:
            continue
        members = []
        for r in sorted(rs, key=lambda r: r["source_id"]):
            pm = CORPUS_TITLES[r["pmid"]]
            members.append({"source_id": r["source_id"], "doi": r["doi"], "first_author": (pm[1].split(";")[0]).strip(),
                            "year": pm[2], "title": pm[0], "pipeline": per[r["source_id"]]["pipeline"],
                            "atlas": per[r["source_id"]]["atlas"], "n_by_dx": r["kg_link"]["n_by_dx"],
                            "claim_type": r["kg_link"]["claim_type"], "reconstructible": r["kg_link"]["reconstructible"]})
        pipes = collections.Counter(p for m in members for p in m["pipeline"])
        shared.append({"cohort_id": f"{ds.replace(' ', '').replace('+', '_')}-N{tot}" + (f"-{asd}ASD-{td}TD" if asd else ""),
                       "release": ds, "n_total": tot, "n_asd": asd, "n_td": td, "n_papers": len(members),
                       "pipelines": dict(pipes),
                       "same_pipeline": len(pipes) == 1 and len(members) == list(pipes.values())[0],
                       "members": members})
    res["shared_cohorts"] = {"rule": "identical release + identical charted N by diagnosis (papers charting only a "
                                     "total N are attached when exactly one same-release group has that total)",
                             "groups": shared}
    # n distribution
    ns = sorted(r["kg_link"]["n_by_dx"]["total"] for r in analysed if r["kg_link"]["n_by_dx"].get("total"))
    res["analysed_n"] = {"n_with_total": len(ns), "min": ns[0], "median": ns[len(ns) // 2], "max": ns[-1],
                         "not_reported": len(analysed) - len(ns)}
    json.dump(res, open(ROOT / "results_synthesis.json", "w"), indent=1, ensure_ascii=False)
    write_md(res)
    print(json.dumps({k: v for k, v in res.items() if k not in ("per_paper_categories", "shared_cohorts")}, indent=1)[:6000])
    for g in shared:
        print(g["cohort_id"], g["n_papers"], g["pipelines"], [m["source_id"] + " " + m["first_author"] + " " + m["year"] for m in g["members"]])


def brief(res):
    s, ev = res["screening"], res["evaluation"]
    d = ev["accuracy_by_scheme"]
    rc = res["reconstructibility_RQ6"]["summary"]
    big = res["shared_cohorts"]["groups"][0]
    p, lso = d.get(POOLED, {}), d.get(LSO, {})
    return [
        f"- {s['included']} of {s['assessed_for_eligibility']} papers analysed ABIDE resting-state data; {s['excluded']} were excluded, "
        f"almost all ({s['excluded_reasons'].get('Exclusion 3: structural/DTI/phenotype-only ABIDE use (no resting-state analysis)', 0)}) because they used only structural or phenotypic ABIDE data.",
        f"- Most work is on ABIDE I alone ({res['release'].get('ABIDE I', 0)} papers); {res['release'].get('ABIDE I+II', 0)} combine I and II; {res['release'].get('ABIDE II', 0)} use II alone.",
        f"- Prediction dominates: {res['claim_type'].get('predictive', 0)} predictive, {res['claim_type'].get('both', 0)} predictive plus group difference, "
        f"{res['claim_type'].get('associational', 0)} group difference only.",
        f"- Of {ev['n_predictive_or_both']} predictive papers, {ev['papers_per_scheme'][POOLED]} use cross-validation that mixes sites in train and test folds; "
        f"only {ev['papers_per_scheme'][LSO]} hold whole sites out. Median best accuracy is {p.get('median', 0):.1f}% under pooled CV "
        f"({p.get('n_papers_with_accuracy', 0)} papers; {p.get('median_excluding_leakage_flagged', 0):.1f}% without the leakage-flagged ones) "
        f"and {lso.get('median', 0):.1f}% under leave-site-out ({lso.get('n_papers_with_accuracy', 0)} papers). These are different papers, "
        "models and subsets, so the gap is descriptive, not a controlled comparison. Two papers report both schemes with numbers for the "
        "same model: S-030 drops from 64% to 56% balanced accuracy when sites are held out; S-072 reports about 60% pooled and 62% leave-site-out.",
        f"- {len(ev['leakage_flagged'])} predictive papers are flagged for leakage (feature selection, harmonisation or tuning using data outside the training folds).",
        f"- The analysed cohort can be rebuilt exactly for {rc['yes']} papers (a published participant list for only "
        f"{res['availability_CL7']['participant_list_released (RQ6)']}), partly for {rc['partly']}, not at all for {rc['no']}.",
        f"- The most reused subset is ABIDE I N = {big['n_total']} ({big['n_asd']} ASD / {big['n_td']} TD): {big['n_papers']} papers, "
        f"including Abraham et al. (S-002; NeuroImage 2017, corpus year 2016), Parisot et al. 2018 (S-019) and Ktena et al. 2017 (S-024).",
        "- Leave-site-out also appears as a robustness check for group differences (S-005, S-009), which is why the site-handling table "
        "counts 8 papers with leave-site-out against 6 in the evaluation table.",
    ]


def pct(n, d):
    return f"{n} ({100 * n / d:.0f}%)" if d else str(n)


def write_md(res):
    s, ev = res["screening"], res["evaluation"]
    ninc = s["included"]
    L = ["# ABIDE I/II resting-state literature: what the charted papers did", "",
         "Computed by `phase3/s4_synthesis.py` from the charted records (quotes re-verified against each paper's "
         "full text). Counts are papers; only charted values are counted, and 'not reported' is reported. "
         "The corpus is the 99 open-access papers retrieved from 200 sought (see `out/review.md` for the PRISMA flow); "
         "this is a second-pass eligibility assessment over those reports, not a census of ABIDE papers.", "",
         "## In brief", ""] + brief(res) + ["",
         "## Who got in", "",
         f"- Assessed for eligibility: **{s['assessed_for_eligibility']}**; included **{ninc}**, excluded **{s['excluded']}**.",
         f"- Read in full text: {s['assessed_on'].get('full_text', 0)}; on abstract only: {s['assessed_on'].get('abstract_only', 0)} "
         f"({', '.join(s['full_text_mismatched'])} — the retrieved PDF is a different paper).", ""]
    for k, v in s["excluded_reasons"].items():
        L.append(f"- {k}: {v}")
    L += ["", "## Which release, which kind of claim", "",
          "| ABIDE release | papers |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(res["release"].items())]
    L += ["", "| Main claim | papers |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(res["claim_type"].items(), key=lambda kv: -kv[1])]
    L += ["", f"Analysed sample size (total N, {res['analysed_n']['n_with_total']} papers reporting it): "
              f"median {res['analysed_n']['median']}, range {res['analysed_n']['min']}–{res['analysed_n']['max']}; "
              f"{res['analysed_n']['not_reported']} did not report a total.", "",
          "## How prediction papers were evaluated", "",
          f"{ev['n_predictive_or_both']} papers make a predictive claim (predictive only, or predictive plus a group "
          "difference). A paper can use more than one scheme.", "",
          "| Evaluation scheme | papers | papers with a charted accuracy | accuracy median (range) | leakage-flagged |",
          "|---|---|---|---|---|"]
    for sch, n in ev["papers_per_scheme"].items():
        d = ev["accuracy_by_scheme"].get(sch)
        if d:
            L.append(f"| {sch} | {n} | {d['n_papers_with_accuracy']} | {d['median']:.1f}% ({d['min']:.1f}–{d['max']:.1f}) | {d['n_leakage_flagged']} |")
        else:
            L.append(f"| {sch} | {n} | 0 | — | — |")
    L += ["", "Accuracy is each paper's best reported result for its own model under that scheme, as charted "
              "(two values are balanced accuracy; within-site rows use the cross-site average when the paper gives one, "
              "otherwise the best single site). Papers reporting only AUC, correlations or relative changes are not "
              f"in the accuracy columns: {', '.join(f'{k} ({v})' for k, v in ev['papers_without_charted_accuracy'].items())}.", "",
          "Papers that report the same model under two schemes:", ""]
    for p in ev["within_paper_comparisons"]:
        L.append("- " + p["source_id"] + ": " + "; ".join(f"{k} {v:g}%" for k, v in p.items() if k != "source_id"))
    L += ["", "### Leakage", "",
          f"PROBAST Analysis domain across the {ev['n_predictive_or_both']} predictive papers: "
          + ", ".join(f"{k} {v}" for k, v in ev["probast_analysis_judgment"].items()) + ".",
          f"Flagged for leakage ({len(ev['leakage_flagged'])}): Analysis High *and* the charted reason is one of the "
          "specific patterns below. Other High ratings were for single splits without uncertainty, pooled CV ignoring "
          "site, or no stated validation — weaknesses, but not leakage by this rule.", ""]
    byp = collections.defaultdict(list)
    for sid, lab in sorted(ev["leakage_flagged"].items()):
        byp[lab].append(sid)
    for lab, ids in byp.items():
        L.append(f"- {lab}: {', '.join(ids)}")
    L += ["", "## Pipelines, atlases, site handling", "",
          f"Over the {res['pipeline']['n_papers']} included analysis papers (the ABIDE II data descriptor excluded); "
          "a paper can use several.", "", "| Preprocessing pipeline | papers |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in res["pipeline"]["counts_multi_label"].items()]
    L += ["", "| Atlas / parcellation | papers |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in res["atlas"]["counts_multi_label"].items()]
    L += ["", "| Site handling | all analysis papers | predictive papers |", "|---|---|---|"]
    for k, v in res["site_handling"]["counts_multi_label"].items():
        L.append(f"| {k} | {v} | {res['site_handling']['predictive_only'].get(k, 0)} |")
    rc = res["reconstructibility_RQ6"]["summary"]
    av = res["availability_CL7"]
    L += ["", "## Can the analysed cohort be rebuilt? (RQ6)", "",
          f"- Yes: {pct(rc['yes'], ninc)} — of which a released participant list: {av['participant_list_released (RQ6)']}; exact rules only: {rc['yes'] - av['participant_list_released (RQ6)']}.",
          f"- Partly: {pct(rc['partly'], ninc)}.", f"- No: {pct(rc['no'], ninc)}.", "",
          f"Code and/or participant list (CL7): " + ", ".join(f"{k} {v}" for k, v in av["cl7_answer"].items())
          + f"; code release mentioned in {av['code_released_mentioned']}.", "",
          "## Papers analysing the same cohort", "",
          "Grouped by identical release and charted N by diagnosis. The same N does not prove the same participants; "
          "it is the strongest signal the papers themselves give, since few publish a participant list.", ""]
    for g in res["shared_cohorts"]["groups"]:
        nd = f"{g['n_asd']} ASD / {g['n_td']} TD" if g["n_asd"] else "N by diagnosis not charted"
        L.append(f"### {g['release']}, N = {g['n_total']} ({nd}) — {g['n_papers']} papers")
        L.append(f"Pipelines: {', '.join(f'{k} {v}' for k, v in g['pipelines'].items())}.")
        L.append("")
        for m in g["members"]:
            tot_only = " (total N only charted)" if m["n_by_dx"].get("ASD") is None else ""
            L.append(f"- {m['source_id']} {m['first_author']} {m['year']}{tot_only} — {m['title']} "
                     f"[{', '.join(m['pipeline'])}; {', '.join(m['atlas'])}; {m['claim_type']}; reconstructible: {m['reconstructible']}]")
        L.append("")
    open(ROOT / "synthesis.md", "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
