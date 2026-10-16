#!/usr/bin/env bash
# Download the Kim et al. 2023 UCLA data and code from the authors' OSF project (https://osf.io/agqtn/)
# and check them against the hashes recorded when this re-run was made (2026-10-16).
set -euo pipefail
cd "$(dirname "$0")"
fetch() { [ -f "$1" ] || curl -sL -o "$1" "https://osf.io/download/$2/"; echo "$3  $1" | shasum -a 256 -c -; }
fetch UCLA_data.mat z5k8m e39207af0de063a515bae524ac6df31ee16c589022bec0084b98d2562bd25e51
fetch UCLA_code.m   w7q2e d685f074d792218d2005b91420fb3191bffe056911eb2b484476b338e53a0d96
