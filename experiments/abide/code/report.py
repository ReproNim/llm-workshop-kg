"""Single-file HTML report with embedded figures.

Usage: uv run python code/report.py
"""

import base64
import html
import json

from common import FIGURES, RESULTS, ROOT


def load(name: str) -> dict:
    """Load a results JSON."""
    return json.loads((RESULTS / name).read_text())


def img(stem: str, alt: str) -> str:
    """Inline PNG."""
    data = base64.b64encode((FIGURES / f"{stem}.png").read_bytes()).decode()
    return f'<figure><img alt="{html.escape(alt)}" src="data:image/png;base64,{data}"><figcaption>{html.escape(alt)}</figcaption></figure>'


def table(rows: list[tuple], head: tuple) -> str:
    """Simple HTML table."""
    h = "".join(f"<th>{html.escape(str(x))}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{html.escape(str(x))}</td>" for x in r) + "</tr>" for r in rows)
    return f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"


def f3(x: float) -> str:
    """Three decimals."""
    return f"{x:.3f}"


def extra_sections() -> str:
    """Sections for the ReproNim join, NIDM conformance, resources, scope and query engines."""
    s2, lv, sc = load("simple2.json"), load("linkml_validation.json"), load("scope.json")
    rc, ca = load("resources_catalog.json"), load("competency_answers.json")
    v, ij, ag = s2["verbatim_query"], s2["identity_join"], s2["tool_agreement"]
    out = [f"""<h2>9. Joining ReproNim's simple2 NIDM graphs</h2>
<p>{len([g for g in s2['named_graphs'] if g['kind'] == 'site NIDM'])} ABIDE site graphs and 3 tool CDE files from ReproNim/simple2_NIDM_examples
(commit {s2['simple2_commit'][:10]}) were loaded unmodified as named graphs. Their own <code>simple2_query.sparql</code>, unmodified, returns
{v['rows']:,} rows for {v['participants']} participants in {v['seconds']} s with Oxigraph.
It reproduces their shipped output for {v['keys_with_equal_values_rtol_1e-6']:,}/{v['participant_label_keys_in_both']:,} participant x measure keys;
the only differences are {len(v['labels_only_in_shipped_output'])} ANTs measures whose labels changed since that CSV was written
({', '.join(v['labels_only_in_shipped_output'])} -> {', '.join(v['labels_only_in_our_run'])}).
Identity join through the shared <code>ndar:src_subject_id</code> literal: {ij['matched']}/{ij['phenotype_rows']} matched, {ij['n_participants_with_any_conflict']}
age/sex/diagnosis/FIQ conflicts.</p>
{img("tool_agreement", "Same anatomical term, three programs")}
<p>Median Pearson r across {ag['regions_with_all_three_tools']} regions: """ + ", ".join(f"{k} {x:.2f}" for k, x in ag["median_r_by_pair"].items())
           + """. FSL's CSF is total CSF while FreeSurfer and ANTs report the ventricular label under the same UBERON term.</p>""",
           f"""<h2>10. Conforming to the current NIDM schema</h2>
<p>PyNIDM v4.5.5 ships a LinkML schema written for AI-assisted SPARQL generation. SHACL generated from it (open shapes):
""" + "; ".join(f"{t}: {r['open']['n_results']:,} results on {r['triples']:,} triples" for t, r in lv["targets"].items())
           + f""". The same three schema slots account for nearly all results, including in PyNIDM's own output and ReproNim's files
(association agents limited to persons, an export-activity shape that targets every prov:Activity, single-valued Derivative.used).
Terms the schema has no slot for are declared in graph/abide_extension.ttl ({lv['extension']['n_classes']} classes,
{lv['extension']['n_properties']} properties).</p>""",
           f"""<h2>11. Resources and how current they are</h2>
<p>{rc['n_resources']} resources (by use here: {', '.join(f'{k} {n}' for k, n in rc['by_usage'].items())}), each with a plain-language
description, workflow-step facets, EDAM terms and dated activity snapshots that are appended, never overwritten.</p>
{img("resource_map", "Resources by workflow step and activity age")}
<pre>{html.escape((RESULTS / 'find_resources_examples.txt').read_text()[:3500]) if (RESULTS / 'find_resources_examples.txt').exists() else ''}</pre>""",
           f"""<h2>12. ReproPond and ReproLake</h2>
<p>Items carry a knowledge scope (pond at analyst, lab or site level; consortium federation; lake), an access level and a sensitivity
profile with a derived egress decision. Promotion candidates record six gates.</p>
""" + table([(c["candidate"], c["status"], c["target"], ", ".join(c["unmet"]) or "none") for c in sc["promotion_candidates"]],
                ("candidate", "status", "target", "unmet gates"))]
    return "\n".join(out)


def main() -> None:
    """Write report.html."""
    c, k = load("cohorts.json"), load("key_numbers.json")
    a1, a2 = load("analyst_a_v1.json"), load("analyst_a_v2.json")
    b1, b2 = load("analyst_b_v1.json"), load("analyst_b_v2.json")
    r1 = load("reviews_v1.json")
    fl, im = load("revision_flags.json"), load("revision_impact.json")
    u, sh = load("umap.json"), load("shacl_summary.json")
    gold = json.loads((ROOT / "comparison/gold_answers.json").read_text())
    pe = load("paper_extraction.json")
    m_lab = {"demographic": "age + sex", "demographic_fd": "age + sex + mean FD", "correlation": "CC200 correlation", "tangent": "CC200 tangent"}
    b_rows = [(m_lab[m], f3(b1["pooled"][m]["accuracy"]), f"{f3(b1['pooled'][m]['auc'])} [{f3(b1['pooled'][m]['auc_95ci'][0])}, {f3(b1['pooled'][m]['auc_95ci'][1])}]",
               f3(b2["pooled"][m]["accuracy"]), f"{f3(b2['pooled'][m]['auc'])} [{f3(b2['pooled'][m]['auc_95ci'][0])}, {f3(b2['pooled'][m]['auc_95ci'][1])}]") for m in m_lab]
    ab, ba = r1["A_reviews_B"], r1["B_reviews_A"]
    up = u["umap_primary"]
    us = u["umap_with_srs"]
    body = f"""
<h1>ABIDE I: two analysts, one knowledge graph</h1>
<p class="lede">An executed, illustrative experiment. Two <em>hypothetical</em> analysts work on the same public dataset
(ABIDE I Preprocessed, C-PAC <code>filt_noglobal</code>, CC200 atlas). Analyst A asks a group-difference question in the style of
Di Martino et al. 2014; Analyst B asks a prediction question in the style of Abraham et al. 2017. Every number below
comes from <code>results/*.json</code>. Neither paper was replicated.</p>

<h2>1. Cohorts are queries, not facts</h2>
{img("cohort_flow", "How each selection rule narrows the sample")}
<p>Analyst A's cohort ({c['A_v1']['n']}) is a strict subset of B's ({c['B_v1']['n']}). Rater QC alone gives {c['rater_qc_pass']['n']}
participants; Abraham et al. report 871. The two-person difference is unresolved: the paper does not publish its list.</p>

<h2>2. Analyst A: group difference</h2>
<p>Edgewise model on {a1['n']} males from {len(a1['sites'])} sites: <code>{html.escape(a1['model'])}</code>.
{a1['n_fdr_significant']} of {a1['n_edges']} edges pass FDR; {a1['n_hypo']} show lower connectivity in ASD
(hypo fraction {f3(a1['hypo_fraction'])}, bootstrap 95% CI {f3(a1['hypo_fraction_bootstrap_95ci'][0])}-{f3(a1['hypo_fraction_bootstrap_95ci'][1])}).
Median |d| among significant edges is {f3(a1['median_abs_d_significant'])}: small effects.</p>

<h2>3. Analyst B: prediction at unseen sites</h2>
{table(b_rows, ("features", "v1 accuracy", "v1 AUC [95% CI]", "v2 accuracy", "v2 AUC [95% CI]"))}
{img("analyst_b_sites", "Per-site accuracy varies far more than the pooled interval suggests")}

<h2>4. They review each other</h2>
<p><b>A reviews B.</b> Of B's {ab['top_k_edges']} most heavily weighted edges, {ab['overlap_with_A_significant']} are among A's significant edges
(expected by chance {ab['expected_overlap_if_independent']:.1f}; hypergeometric p = {ab['hypergeometric_p']:.1e}); signs agree in
{ab['sign_agreement_in_overlap'][0]}/{ab['sign_agreement_in_overlap'][1]}. Verdict: {html.escape(ab['verdict'])}.</p>
<p><b>B reviews A.</b> On the {ba['n_independent_participants']} participants in B's cohort that A never used, A's hypoconnectivity
signature gives pooled d = {f3(ba['pooled_d_fixed_effect'])} (95% CI {f3(ba['pooled_d_95ci'][0])} to {f3(ba['pooled_d_95ci'][1])});
{ba['n_sites_direction_consistent']} of {ba['n_sites_usable']} sites point the same way. Verdict: {html.escape(ba['verdict'])}.
The signature correlates r = {f3(ba['signature_vs_global_mean_connectivity_r'])} with whole-brain mean connectivity, so it mostly measures
a global shift that global-signal regression would remove.</p>
{img("review_b_of_a_forest", "B's review of A, by held-out site")}

<h2>5. A changes a shared rule; the graph says what to recheck</h2>
<p>A tightens the shared motion rule from mean FD &lt; 0.2 mm to &lt; 0.15 mm. Before recomputing anything, SPARQL over the graph finds
{fl['affected_participants_by_cohort'].get('B_v1', 0)} affected participants in B's cohort and {fl['affected_participants_by_cohort'].get('A_v1', 0)} in A's,
{fl['n_folds_with_affected_test']} of {fl['n_folds_total']} folds with an affected test participant, all {fl['n_folds_with_affected_train']} with an affected
training participant, and one of A's sites ({', '.join(fl['cohort_A_sites_falling_below_minimum'])}) falling below the per-site minimum.
After recomputation, {im['n_material_changes']} of {im['n_result_families_compared']} result families changed materially
(rule: {html.escape(im['materiality_rule'])}).</p>
{img("revision_flagged_vs_changed", "Flagged by traversal versus measured change")}
{table([(k2, v['summary'], 'yes' if v['material'] else 'no') for k2, v in im['changes'].items()], ("result", "v1 -> v2", "material"))}

<h2>6. Phenotype embedding, joined to imaging</h2>
<p>UMAP of age, FIQ, VIQ and PIQ queried from the graph ({up['n_complete_cases']} complete cases, {up['n_dropped_missing']} dropped for
missing values, {up['n_sites']} sites). Trustworthiness (k=15) {f3(up['trustworthiness_umap'])} vs PCA {f3(up['trustworthiness_pca'])};
other seeds {', '.join(f3(x) for x in up['trustworthiness_other_seeds'])}; 15-neighbour overlap across seeds
{', '.join(f3(x) for x in up['neighbour_overlap_vs_other_seeds'])}. Silhouette by diagnosis {f3(up['silhouette_by_dx'])}, by site
{f3(up['silhouette_by_site'])}. Mean cortical thickness (ANTs) correlates with age at Spearman
{f3(up['joins']['thickness']['spearman_with_age'])}.</p>
{img("umap_primary", "Primary phenotype UMAP")}
<p>Adding SRS leaves {us['n_complete_cases']} complete cases from {us['n_sites']} sites: the missingness pattern, not biology, decides who is embedded.</p>
{img("umap_with_srs", "Adding SRS restricts the embedding to the sites that collected it")}

<h2>7. Validation</h2>
<p>Local SHACL profile ({sh['n_shapes']} shapes) over {sh['triples']:,} triples: conforms = {sh['conforms']}.
Mutation tests rejected: {sum(m['rejected'] for m in sh['mutations'])}/{len(sh['mutations'])}
({'; '.join(m['mutation'] for m in sh['mutations'])}). Paper quotes matching the source text verbatim: {pe['n_verbatim']}/{pe['n']}.
This checks structure and provenance, not scientific correctness.</p>

<h2>8. Gold answers for the shared questions</h2>
{table([(a['id'], a['question'], a['gold']) for a in gold['answers']], ("id", "question", "gold answer (from SPARQL)"))}

{extra_sections()}

<h2>What did not run</h2>
<ul>
<li>No raw MRI was downloaded or reprocessed; preprocessing is taken as released by ABIDE Preprocessed.</li>
<li>Neither paper was replicated: different pipeline versions, atlases, cohorts and models (see the comparability assessments in the graph).</li>
<li>The analysts, their reviews and the rule revision are a simulation; no real person's work is represented.</li>
<li>Abraham 2017 quotes are from the arXiv v1 preprint, not the journal version.</li>
</ul>
<p class="foot">{len(k)} key numbers in results/key_numbers.json. Rebuild: <code>bash rebuild.sh</code>.</p>
"""
    css = """
:root{--bg:#fff;--fg:#1d1d1f;--muted:#5f6368;--line:#e3e3e3;--accent:#DD8452}
@media (prefers-color-scheme:dark){:root{--bg:#151515;--fg:#eee;--muted:#aaa;--line:#333}}
body{background:var(--bg);color:var(--fg);font:16px/1.55 -apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:980px;margin:0 auto;padding:24px 16px}
h1{font-size:1.8em;margin-bottom:.2em}h2{margin-top:2em;border-bottom:1px solid var(--line);padding-bottom:.2em}
.lede{color:var(--muted);font-size:1.05em}code{font-size:.9em}
figure{margin:1em 0}img{max-width:100%;background:#fff;border-radius:4px}figcaption{color:var(--muted);font-size:.9em}
table{border-collapse:collapse;width:100%;font-size:.9em;margin:1em 0;display:block;overflow-x:auto}
td,th{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}.foot{color:var(--muted)}
"""
    page = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ABIDE Collaboration Graph</title><style>{css}</style></head><body>{body}</body></html>'
    (ROOT / "report.html").write_text(page)
    print("report.html", len(page) // 1024, "KB")


if __name__ == "__main__":
    main()
