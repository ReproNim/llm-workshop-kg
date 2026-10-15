#!/bin/bash
#SBATCH -J cnp-rebuild
#SBATCH -p pi_satra
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=01:00:00
#SBATCH -o cnp-rebuild-%j.out
#SBATCH -e cnp-rebuild-%j.err
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
export UV_CACHE_DIR="$HOME/orcd/scratch/uv-cache"
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 NUMBA_NUM_THREADS=1
ROOT="$HOME/orcd/scratch/repronim-talk/CNP_rebuild"
cd "$ROOT"
NODE_BIN="$(cat "$ROOT/.node_bin" 2>/dev/null || command -v node)"
ts() { echo "=== $(date -Is) $*"; }
ts "host $(hostname) job ${SLURM_JOB_ID:-none} node=$NODE_BIN $("$NODE_BIN" --version)"
ts "STEP uv sync"; uv sync
cd experiment
for s in build_nidm.py prepare_embedding.py embed.cjs assess_embedding.py validate_schema.cjs integrate_graph.py validate_graph.py query_case_study.py collaborative_example.py; do
  ts "STEP $s"
  case "$s" in
    *.cjs) "$NODE_BIN" "$s" ;;
    *) uv run --no-sync --project "$ROOT" python "$s" ;;
  esac
done
cd "$ROOT"
ts "STEP compare"; uv run --no-sync python compare.py | tee compare_summary.txt
python3 - <<PY
import json,os
c=json.load(open("rebuild_comparison.json"))
json.dump({"job":os.environ.get("SLURM_JOB_ID"),"summary":c["summary"],"files_identical":c["files"]["identical"],"files_total":c["files"]["total"]},open("CNP_REBUILD_DONE.json","w"),indent=2)
PY
ts "DONE"
