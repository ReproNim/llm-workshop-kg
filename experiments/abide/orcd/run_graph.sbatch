#!/bin/bash
#SBATCH -J abide-kg-graph
#SBATCH -p mit_normal
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=02:00:00
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err
# Graph build, PyNIDM conversion, ReproNim simple2 merge, LinkML/SHACL validation, Oxigraph store,
# competency queries Q1-Q15 on a CPU node.
# Set RUN_FULL=1 to rerun the whole pipeline (including both analysts) instead of the graph steps.
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
export UV_CACHE_DIR="$HOME/orcd/scratch/uv-cache"
WORK="$HOME/orcd/scratch/repronim-talk/ABIDE_Collaboration_Experiment"
cd "$WORK"
echo "start $(date -u +%FT%TZ) host $(hostname) job ${SLURM_JOB_ID:-none} cpus ${SLURM_CPUS_PER_TASK:-?}"
command -v uv >/dev/null || { echo "uv not on PATH"; exit 2; }
uv sync --frozen
if [ "${RUN_FULL:-0}" = "1" ]; then STEPS=all; else STEPS=graph; fi
/usr/bin/time -v env STEPS=$STEPS bash rebuild.sh 2> >(tee rebuild_time.txt >&2)
uv run --frozen python - <<'PY'
import json, pathlib, socket, os
r = pathlib.Path("results")
k = json.loads((r / "key_numbers.json").read_text())
ca = json.loads((r / "competency_answers.json").read_text())
marker = {"host": socket.gethostname(), "job": os.environ.get("SLURM_JOB_ID"), "n_key_numbers": len(k),
          "competency_query_seconds": ca["query_seconds"], "graph_triples_final": k.get("graph.triples_final"), "shacl_conforms": k.get("shacl.conforms")}
pathlib.Path("ORCD_DONE.json").write_text(json.dumps(marker, indent=1))
print(json.dumps(marker, indent=1))
PY
echo "end $(date -u +%FT%TZ)"
