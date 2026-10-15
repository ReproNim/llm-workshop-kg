"""Compute every cohort used by the experiment and write results/cohorts.json.

Usage: uv run python code/cohorts.py
"""

from common import base_table, cohort_a, cohort_b, connectivity, write_json


def summarize(d, mask) -> dict:
    """Counts by diagnosis and site plus the sorted member FILE_IDs."""
    sub = d[mask]
    return {
        "n": int(mask.sum()),
        "by_dx": sub.dx.value_counts().sort_index().to_dict(),
        "n_sites": int(sub.SITE_ID.nunique()),
        "by_site": sub.groupby("SITE_ID").dx.value_counts().unstack(fill_value=0).to_dict(orient="index"),
        "members": sorted(sub.FILE_ID),
    }


def main() -> None:
    """Build the cohort file."""
    d = base_table()
    connectivity()
    out = {
        "phenotype_rows": 1112,
        "with_timeseries": summarize(d, d.FILE_ID.notna()),
        "full_roi_coverage": summarize(d, d.full_roi_coverage),
        "rater_qc_pass": summarize(d, d.rater_qc_pass),
        "abraham2017_reconstructed": {
            **summarize(d, d.rater_qc_pass),
            "status": "reconstructed via nilearn fetch_abide_pcp quality_checked rule; paper reports N=871",
        },
    }
    for rule in ("v1", "v2"):
        out[f"B_{rule}"] = summarize(d, cohort_b(d, rule))
        out[f"A_{rule}"] = summarize(d, cohort_a(d, rule))
    a1, b1, b2 = set(out["A_v1"]["members"]), set(out["B_v1"]["members"]), set(out["B_v2"]["members"])
    out["overlap"] = {
        "A_v1_and_B_v1": len(a1 & b1),
        "A_v1_only": len(a1 - b1),
        "B_v1_only": len(b1 - a1),
        "B_v1_removed_by_v2": sorted(b1 - b2),
        "n_B_v1_removed_by_v2": len(b1 - b2),
        "A_v1_removed_by_v2": sorted(a1 - set(out["A_v2"]["members"])),
    }
    write_json("cohorts.json", out)
    for k in ("with_timeseries", "full_roi_coverage", "rater_qc_pass", "B_v1", "A_v1", "B_v2", "A_v2"):
        print(k, out[k]["n"], out[k]["by_dx"], out[k]["n_sites"])
    print({k: v for k, v in out["overlap"].items() if not isinstance(v, list)})


if __name__ == "__main__":
    main()
