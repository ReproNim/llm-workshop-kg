"""Collect every slide-worthy number into results/key_numbers.json (flat, diffable across runs).

Also: uv run python code/key_numbers.py --compare other/results/key_numbers.json [--rtol 0.02]

Usage: uv run python code/key_numbers.py
"""

import json
import math
import sys

from common import RESULTS, write_json


def load(name: str) -> dict:
    """Load a results JSON."""
    return json.loads((RESULTS / name).read_text())


def collect() -> dict:
    """Flatten the headline numbers."""
    c, k = load("cohorts.json"), {}
    for name in ("with_timeseries", "full_roi_coverage", "rater_qc_pass", "B_v1", "B_v2", "A_v1", "A_v2"):
        k[f"cohort.{name}.n"] = c[name]["n"]
        for dx, n in c[name]["by_dx"].items():
            k[f"cohort.{name}.{dx}"] = n
        k[f"cohort.{name}.sites"] = c[name]["n_sites"]
    k["cohort.overlap.A_v1_and_B_v1"] = c["overlap"]["A_v1_and_B_v1"]
    k["cohort.overlap.B_v1_removed_by_v2"] = c["overlap"]["n_B_v1_removed_by_v2"]
    k["cohort.overlap.A_v1_removed_by_v2"] = len(c["overlap"]["A_v1_removed_by_v2"])
    for v in ("v1", "v2"):
        a = load(f"analyst_a_{v}.json")
        for f in ("n", "n_fdr_significant", "n_hypo", "n_hyper", "hypo_fraction", "interhemispheric_fraction_hypo_edges", "median_abs_d_significant"):
            k[f"A_{v}.{f}"] = a[f]
        k[f"A_{v}.sites"] = len(a["sites"])
        k[f"A_{v}.hypo_fraction_ci_low"], k[f"A_{v}.hypo_fraction_ci_high"] = a["hypo_fraction_bootstrap_95ci"]
        b = load(f"analyst_b_{v}.json")
        k[f"B_{v}.n"], k[f"B_{v}.folds"] = b["n"], b["n_folds"]
        for m, p in b["pooled"].items():
            k[f"B_{v}.{m}.accuracy"] = p["accuracy"]
            k[f"B_{v}.{m}.auc"] = p["auc"]
            k[f"B_{v}.{m}.auc_ci_low"], k[f"B_{v}.{m}.auc_ci_high"] = p["auc_95ci"]
            k[f"B_{v}.{m}.mean_site_accuracy"] = p["mean_site_accuracy"]
        k[f"B_{v}.tangent_minus_demofd_auc"] = b["tangent_minus_demographic_fd_auc"]["point"]
        r = load(f"reviews_{v}.json")
        ab, ba = r["A_reviews_B"], r["B_reviews_A"]
        k[f"review_{v}.A_of_B.overlap"] = ab["overlap_with_A_significant"]
        k[f"review_{v}.A_of_B.expected"] = ab["expected_overlap_if_independent"]
        k[f"review_{v}.A_of_B.p"] = ab["hypergeometric_p"]
        k[f"review_{v}.B_of_A.pooled_d"] = ba["pooled_d_fixed_effect"]
        k[f"review_{v}.B_of_A.pooled_d_ci_low"], k[f"review_{v}.B_of_A.pooled_d_ci_high"] = ba["pooled_d_95ci"]
        k[f"review_{v}.B_of_A.sites_consistent"] = ba["n_sites_direction_consistent"]
        k[f"review_{v}.B_of_A.sites_usable"] = ba["n_sites_usable"]
        k[f"review_{v}.B_of_A.signature_global_r"] = ba["signature_vs_global_mean_connectivity_r"]
    fl, im = load("revision_flags.json"), load("revision_impact.json")
    for key, n in fl["affected_participants_by_cohort"].items():
        k[f"revision.affected_by_fd.{key}"] = n
    k["revision.folds_with_affected_test"] = fl["n_folds_with_affected_test"]
    k["revision.folds_with_affected_train"] = fl["n_folds_with_affected_train"]
    for kind, n in fl["flagged_by_kind"].items():
        k[f"revision.flagged.{kind}"] = n
    k["revision.A_sites_dropped"] = len(fl["cohort_A_sites_falling_below_minimum"])
    k["revision.material_changes"] = im["n_material_changes"]
    k["revision.families_compared"] = im["n_result_families_compared"]
    k["revision.sites_outside_v1_ci"] = im["n_sites_outside_v1_ci"]
    u = load("umap.json")
    for stem in ("umap_primary", "umap_with_srs"):
        s = u[stem]
        for f in ("n_complete_cases", "n_sites", "trustworthiness_umap", "trustworthiness_pca", "silhouette_by_dx", "silhouette_by_site"):
            k[f"{stem}.{f}"] = s[f]
        for i, t in enumerate(s["trustworthiness_other_seeds"]):
            k[f"{stem}.trustworthiness_seed{i + 1}"] = t
        for i, t in enumerate(s["neighbour_overlap_vs_other_seeds"]):
            k[f"{stem}.neighbour_overlap_seed{i + 1}"] = t
        for j, js in s["joins"].items():
            k[f"{stem}.join.{j}.spearman_age"] = js["spearman_with_age"]
            k[f"{stem}.join.{j}.spearman_umap1"] = js["spearman_with_umap1"]
    sh = load("shacl_summary.json")
    k["shacl.conforms"] = sh["conforms"]
    k["shacl.mutations_rejected"] = sum(m["rejected"] for m in sh["mutations"])
    k["shacl.mutations_total"] = len(sh["mutations"])
    k["graph.triples_final"] = load("graph_summary_final.json")["triples"]
    p = load("paper_extraction.json")
    k["papers.quotes_verbatim"], k["papers.quotes_total"] = p["n_verbatim"], p["n"]
    s2 = load("simple2.json")
    v, ij, ag = s2["verbatim_query"], s2["identity_join"], s2["tool_agreement"]
    k["simple2.named_graphs"] = s2["n_named_graphs"]
    k["simple2.verbatim_rows"], k["simple2.verbatim_participants"] = v["rows"], v["participants"]
    k["simple2.verbatim_seconds_oxigraph"] = v["seconds"]
    k["simple2.shipped_keys_reproduced"], k["simple2.shipped_keys_compared"] = v["keys_with_equal_values_rtol_1e-6"], v["participant_label_keys_in_both"]
    k["simple2.labels_drifted"] = len(v["labels_only_in_shipped_output"])
    k["simple2.identity_matched"], k["simple2.identity_conflicts"] = ij["matched"], ij["n_participants_with_any_conflict"]
    k["simple2.matched_in_B_v1"] = ij["matched_in_cohort_B_v1"]
    k["simple2.regions_three_tools"] = ag["regions_with_all_three_tools"]
    for pair, r in ag["median_r_by_pair"].items():
        k[f"simple2.median_r.{pair}"] = r
    for pair, r in ag["median_abs_pct_diff_by_pair"].items():
        k[f"simple2.median_abs_pct_diff.{pair}"] = r
    pn = load("pynidm_csv2nidm.json")
    k["pynidm.csv2nidm_seconds"], k["pynidm.columns_converted"] = pn["seconds"], pn["columns_converted"]
    lv = load("linkml_validation.json")
    for t, r in lv["targets"].items():
        k[f"linkml.{t}.open_results"] = r["open"]["n_results"]
        k[f"linkml.{t}.closed_results"] = r["closed"]["n_results"]
    k["linkml.extension_classes"], k["linkml.extension_properties"] = lv["extension"]["n_classes"], lv["extension"]["n_properties"]
    rc = load("resources_catalog.json")
    k["resources.n"] = rc["n_resources"]
    for t, n in rc["by_usage"].items():
        k[f"resources.usage.{t}"] = n
    k["resources.snapshots"] = sum(1 for _ in open(RESULTS / "resource_activity_log.jsonl"))
    sc = load("scope.json")
    for t, n in sc["by_scope"].items():
        k[f"scope.{t}"] = n
    k["scope.promotion_candidates"] = len(sc["promotion_candidates"])
    k["scope.fd015_site_max_excluded"] = sc["fd_sweep_0.15"]["site_max"]
    k["scope.fd015_asd_excluded"] = sc["fd_sweep_0.15"]["dx_excluded_fraction"]["ASD"]
    k["scope.fd015_td_excluded"] = sc["fd_sweep_0.15"]["dx_excluded_fraction"]["TD"]
    ca = load("competency_answers.json")
    k["competency.max_query_seconds"] = max(ca["query_seconds"].values())
    return k


def compare(other: str, rtol: float) -> None:
    """Report keys whose values differ beyond rtol."""
    a, b = collect(), json.loads(open(other).read())
    diffs = []
    for key in sorted(set(a) | set(b)):
        x, y = a.get(key), b.get(key)
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and not isinstance(x, bool):
            if not math.isclose(x, y, rel_tol=rtol, abs_tol=1e-9):
                diffs.append((key, x, y))
        elif x != y:
            diffs.append((key, x, y))
    print(f"{len(a)} keys here, {len(b)} there, {len(diffs)} differ (rtol={rtol})")
    for d in diffs:
        print(*d)


if __name__ == "__main__":
    if "--compare" in sys.argv:
        i = sys.argv.index("--compare")
        rtol = float(sys.argv[sys.argv.index("--rtol") + 1]) if "--rtol" in sys.argv else 0.0
        compare(sys.argv[i + 1], rtol)
    else:
        out = collect()
        write_json("key_numbers.json", out)
        print(len(out), "numbers")
