"""Generate the phenotype layer with PyNIDM itself (csv2nidm v4.5.5), as ReproNim's simple2 scripts do.

Runs `csv2nidm -json_map <ReproNim ABIDE term map> -no_concepts` non-interactively on the 75 phenotype columns
the map covers. PyNIDM runs in its own uvx environment (not in uv.lock); instance IRIs are random
UUIDs, so the file hash changes per run while the structure does not.

Writes data/derived/pynidm/phenotype_pynidm.ttl and results/pynidm_csv2nidm.json.

Usage: uv run python code/pynidm_phenotype.py
"""

import json
import re
import resource
import subprocess
import time

import pandas as pd

from common import DATA, PHENO_PATH, write_json

OUT = DATA / "derived/pynidm"
TERM_MAP = DATA / "repronim_simple2/bids_nidm_scripts/abide_phenotypic_v1_0b_vars_to_terms_v5.json"
PYNIDM = "pynidm==4.5.5"


def main() -> None:
    """Subset the CSV to mapped columns and run csv2nidm."""
    OUT.mkdir(parents=True, exist_ok=True)
    mapped = [re.search(r"variable='([^']+)'", k).group(1) for k in json.loads(TERM_MAP.read_text())]
    d = pd.read_csv(PHENO_PATH, dtype=str, keep_default_na=False)
    cols = [c for c in mapped if c in d.columns]
    d[cols].to_csv(OUT / "phenotype_for_csv2nidm.csv", index=False)
    cmd = ["uvx", "--python", "3.12", "--from", PYNIDM, "csv2nidm", "-csv", "phenotype_for_csv2nidm.csv", "-json_map", str(TERM_MAP),
           "-no_concepts", "-out", "phenotype_pynidm.ttl", "-log", "."]
    t0 = time.time()
    p = subprocess.run(cmd, cwd=OUT, stdin=subprocess.DEVNULL, capture_output=True, text=True)
    secs = time.time() - t0
    ru = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    out = {"pynidm": PYNIDM, "command": " ".join(cmd), "returncode": p.returncode, "seconds": round(secs, 1),
           "child_peak_rss_mb": round(ru / 1e6 if __import__("sys").platform == "darwin" else ru / 1e3, 1),
           "mapped_variables": len(mapped), "columns_converted": len(cols), "output_bytes": (OUT / "phenotype_pynidm.ttl").stat().st_size if p.returncode == 0 else None,
           "stderr_tail": [ln for ln in p.stderr.splitlines() if "AnnexRepo" not in ln][-5:]}
    write_json("pynidm_csv2nidm.json", out)
    print(json.dumps(out, indent=1))
    if p.returncode != 0:
        raise SystemExit("csv2nidm failed")


if __name__ == "__main__":
    main()
