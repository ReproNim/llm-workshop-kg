#!/usr/bin/env bash
# Rebuild the presentation and re-run the cheap checks, each step recorded with `datalad run`
# (command, inputs, outputs and commit), so `datalad rerun <commit>` replays it.
# Requires: datalad + git-annex, uv, node/npm. Run from the repository root.
#   scripts/build_all.sh            # all steps
#   scripts/build_all.sh deck       # one step: figures | deck | pdf | values | graphs
set -euo pipefail
cd "$(dirname "$0")/.."
step="${1:-all}"
ABIDE=experiments/abide
DS=experiments/ds000030/experiment

run_figures() {
  datalad run -m "Slide figures from the ABIDE results" \
    --input "$ABIDE/results/participant_ego.json" --input "$ABIDE/results/element_coverage.json" \
    --input "$ABIDE/graph/resources.ttl" --input "$ABIDE/results/resource_activity_log.jsonl" \
    --input slides/figs_slide/make_slide_figs.py \
    --output "slides/figs_slide/*.png" --output "slides/figs_slide/*.svg" \
    "uv run slides/figs_slide/make_slide_figs.py"
}

run_deck() {
  (cd slides && npm ci --silent)
  datalad run -m "Build the deck (pptx) and its slide provenance (talk_provenance.ttl)" \
    --input slides/build_deck.js --input slides/values.js --input slides/values_map.json \
    --input slides/apply_theme.js --input slides/old_deck_v3.md --input "slides/figs_slide/*.png" \
    --output slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pptx --output slides/talk_provenance.ttl \
    "cd slides && node build_deck.js"
}

run_pdf() {
  # Host step: LibreOffice where installed, otherwise Microsoft PowerPoint on macOS.
  datalad run -m "Export the deck to PDF (host step)" \
    --input slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pptx \
    --output slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pdf \
    "scripts/export_pdf.sh slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pptx slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pdf"
}

run_values() {
  datalad run -m "Check every mapped slide value against its result file" \
    --input slides/values_map.json --input slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pptx \
    --output provenance/slide_value_check.txt \
    "mkdir -p provenance && uv run scripts/check_slide_values.py > provenance/slide_value_check.txt"
}

run_graphs() {
  datalad run -m "Parse every Turtle file" \
    --output provenance/ttl_parse_report.json \
    "mkdir -p provenance && uv run scripts/parse_all_ttl.py provenance/ttl_parse_report.json"
  datalad run -m "ABIDE graph: SHACL validation and mutation tests" \
    --input "$ABIDE/graph/*.ttl" --input "$ABIDE/code/shapes.ttl" \
    --output "$ABIDE/results/shacl_report.txt" --output "$ABIDE/results/shacl_summary.json" \
    "cd $ABIDE && uv run --frozen python code/validate.py"
  datalad run -m "ds000030 graph: SHACL validation and missing-source mutation" \
    --input "$DS/results/combined_graph.ttl" --input "$DS/shapes.ttl" \
    --output "$DS/results/shacl_report.txt" --output "$DS/results/shacl_report.ttl" \
    --output "$DS/results/shacl_summary.json" --output "$DS/results/shacl_mutation_report.txt" \
    "uv run --with rdflib==7.1.4 --with pyshacl==0.30.1 python $DS/validate_graph.py"
}

case "$step" in
  figures) run_figures ;;
  deck) run_deck ;;
  pdf) run_pdf ;;
  values) run_values ;;
  graphs) run_graphs ;;
  all) run_figures; run_deck; run_pdf; run_values; run_graphs ;;
  *) echo "unknown step: $step" >&2; exit 2 ;;
esac
