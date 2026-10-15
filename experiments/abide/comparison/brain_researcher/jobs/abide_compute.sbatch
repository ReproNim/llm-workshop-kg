#!/bin/bash
#SBATCH --job-name=abide-br
#SBATCH --partition=pi_satra
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=06:00:00
#SBATCH --output=%x-%j.out
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
SCR="$(readlink -f ~/orcd/scratch)"
export UV_CACHE_DIR="$SCR/uv-cache"
export N_JOBS=8
cd "$SCR/abide_br"
echo "host $(hostname) start $(date -Is)"
curl -sI https://s3.amazonaws.com/fcp-indi/data/Projects/ABIDE_Initiative/Phenotypic_V1_0b_preprocessed1.csv | head -1
uv run --python 3.12 --with nilearn==0.11.1 --with scikit-learn --with pandas --with scipy --with requests --with joblib \
  python abide_compute.py out
echo "end $(date -Is)"
