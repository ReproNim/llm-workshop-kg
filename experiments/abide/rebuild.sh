#!/usr/bin/env bash
# Full non-interactive rebuild. Needs uv, and network access to s3.amazonaws.com, raw.githubusercontent.com,
# ebi.ac.uk and arxiv.org (inputs are verified against data/expected_sha256.json).
# Usage: bash rebuild.sh            (about 45-60 min on a laptop; most of it is Analyst B's tangent folds)
#        STEPS=graph bash rebuild.sh  (graph, query and report steps only; reuses existing analysis results)
set -euo pipefail
cd "$(dirname "$0")"
export PYTHONHASHSEED=0
export MPLBACKEND=Agg
uv sync --frozen
run() { echo "== $(date -u +%H:%M:%S) $*"; uv run --frozen python "$@"; }

run code/download.py                     # fetch inputs, verify hashes
if [ "${STEPS:-all}" = "all" ]; then
  run code/cohorts.py
  run code/papers.py
  run code/analyst_a.py v1
  run code/analyst_b.py v1
  run code/reviews.py v1
  run code/build_graph.py v1
  run code/revision.py flag                # graph traversal BEFORE any recomputation (Oxigraph)
  run code/analyst_a.py v2
  run code/analyst_b.py v2
  run code/reviews.py v2
  run code/revision.py compare
fi
run code/build_graph.py final
run code/pynidm_phenotype.py             # PyNIDM csv2nidm v4.5.5 (uvx), non-interactive
run code/repronim_simple2.py             # ReproNim simple2 NIDM: named graphs, verbatim query, identity join, tool agreement
run code/validate_linkml.py              # SHACL generated from PyNIDM's LinkML schema; declares our extension
run code/resources_catalog.py            # catalog from data/resources_pinned.json (no network)
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 NUMBA_NUM_THREADS=1 run code/umap_phenotype.py
run code/scope.py
run code/publications.py                # AbstractAtlas bundle (pinned by hash) + cached OpenAlex pull
run code/store.py --force                # on-disk Oxigraph store + materialized views
run code/participant_ego.py              # Q13 participant-centred view
run code/element_coverage.py             # Q14 data-element coverage
run code/competency.py                   # Q1-Q15
run code/profile_simple2.py
run code/validate.py
run code/find_resources.py --examples
run code/figures.py
run code/key_numbers.py
run code/report.py
echo "done: results/key_numbers.json, report.html"
# Not part of the rebuild (network- and time-dependent; snapshots are appended, never replaced):
#   uv run python code/refresh_activity.py
# Optional, not part of the package results (abandoned engine comparison):
#   uv run python code/query_bench.py --rdflib-timeout 300
