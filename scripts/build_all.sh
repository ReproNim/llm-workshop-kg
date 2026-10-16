#!/usr/bin/env bash
# Rebuild the presentation and re-run the cheap checks, each step recorded with `datalad run`
# (command, inputs, outputs and commit), so `datalad rerun <commit>` replays it.
# Requires: datalad + git-annex, uv, node/npm. Run from the repository root.
#   scripts/build_all.sh            # all steps
#   scripts/build_all.sh deck       # one step: figures | deck | pdf | values | pdftext | graphs
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
  # Two passes: the provenance-graph slide shows a query over talk_provenance.ttl, which the
  # first pass writes; prov_query.py runs that query, and the second pass draws its result.
  datalad run -m "Build the deck (pptx) and its slide provenance (talk_provenance.ttl), two passes" \
    --input slides/build_deck.js --input slides/values.js --input slides/values_map.json \
    --input slides/apply_theme.js --input slides/old_deck_v3.md --input "slides/figs_slide/*.png" --input "slides/demo/*.md" \
    --input slides/prov_query.py \
    --output slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pptx --output slides/talk_provenance.ttl \
    --output slides/provenance_query.json \
    "cd slides && node build_deck.js && uv run prov_query.py && node build_deck.js"
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
    --input slides/values_map.json --input slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pptx --input "slides/demo/*.md" \
    --output provenance/slide_value_check.txt \
    "mkdir -p provenance && uv run scripts/check_slide_values.py > provenance/slide_value_check.txt"
}

run_pdftext() {
  datalad run -m "Check the deck PDF carries the deck's on-slide text" \
    --input slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pdf --input slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pptx \
    --output provenance/pdf_text_check.txt \
    "uv run scripts/check_pdf_text.py slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pdf slides/Knowledge_Graphs_Skills_Neuroimaging_v4.pptx > provenance/pdf_text_check.txt"
}

run_graphs() {
  datalad run -m "Parse every Turtle file" \
    --output provenance/ttl_parse_report.json \
    "mkdir -p provenance && uv run scripts/parse_all_ttl.py provenance/ttl_parse_report.json"
  datalad run -m "ABIDE graph: SHACL validation and mutation tests" \
    --input "$ABIDE/graph/*.ttl" --input "$ABIDE/code/shapes.ttl" \
    --output "$ABIDE/results/shacl_report.txt" --output "$ABIDE/results/shacl_summary.json" \
    --output "$ABIDE/SHA256SUMS" --output "$ABIDE/SHA256SUMS.json" \
    "(cd $ABIDE && uv run --frozen python code/validate.py) && uv run scripts/refresh_checksums.py $ABIDE results/shacl_report.txt results/shacl_summary.json"
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
  all) run_figures; run_deck; run_pdf; run_values; run_pdftext; run_graphs ;;
  pdftext) run_pdftext ;;
  *) echo "unknown step: $step" >&2; exit 2 ;;
esac
