#!/usr/bin/env bash
# Copy the deck sources from a working directory back into slides/, then rebuild with provenance.
#   scripts/sync_from_workspace.sh /path/to/workspace/deck_build [/path/to/talk_plan.md]
# Paths inside the copied build_deck.js and make_slide_figs.py are rewritten to repo-relative ones,
# and hand-entered numbers must stay routed through values.js (check_slide_values.py enforces this).
set -euo pipefail
src="${1:?usage: sync_from_workspace.sh DECK_BUILD_DIR [TALK_PLAN]}"
plan="${2:-$src/../talk_plan.md}"
root="$(cd "$(dirname "$0")/.." && pwd)"
cp "$src/apply_theme.js" "$src/old_deck_v3.md" "$root/slides/"
cp "$src/figs_slide/make_slide_figs.py" "$root/slides/figs_slide/"
[ -f "$src/figs_slide/make_qr.py" ] && cp "$src/figs_slide/make_qr.py" "$root/slides/figs_slide/"
# repo-relative paths in the figure script
sed -i.bak -e 's#^SRC = Path(".*")\.expanduser()#SRC = Path(__file__).resolve().parents[2] / "experiments" / "abide"#' \
  -e 's#^OUT = Path(".*")\.expanduser()#OUT = Path(__file__).resolve().parent#' "$root/slides/figs_slide/make_slide_figs.py"
rm -f "$root/slides/figs_slide/make_slide_figs.py.bak"
grep -q "/// script" "$root/slides/figs_slide/make_slide_figs.py" || \
  { printf '# /// script\n# requires-python = ">=3.11"\n# dependencies = ["matplotlib>=3.9", "networkx>=3.3", "pandas>=2.2"]\n# ///\n'; cat "$root/slides/figs_slide/make_slide_figs.py"; } > "$root/slides/figs_slide/m.tmp" && mv "$root/slides/figs_slide/m.tmp" "$root/slides/figs_slide/make_slide_figs.py"
[ -f "$plan" ] && cp "$plan" "$root/slides/talk_plan.md"
# provenance-graph query (talk_provenance.ttl sits next to it in slides/)
if [ -f "$src/prov_query.py" ]; then
  sed -e 's#HERE.parent / "talk_provenance.ttl"#HERE / "talk_provenance.ttl"#' "$src/prov_query.py" > "$root/slides/prov_query.py"
  grep -q "/// script" "$root/slides/prov_query.py" || { printf '# /// script\n# requires-python = ">=3.11"\n# dependencies = ["pyoxigraph>=0.4"]\n# ///\n'; cat "$root/slides/prov_query.py"; } > "$root/slides/pq.tmp" && mv "$root/slides/pq.tmp" "$root/slides/prov_query.py"
fi
mkdir -p "$root/slides/demo"
[ -d "$src/demo" ] && cp "$src"/demo/*.md "$root/slides/demo/"
echo "Copied apply_theme.js, old_deck_v3.md, make_slide_figs.py and talk_plan.md."
uv run "$root/scripts/port_build_deck.py" "$src/build_deck.js"
echo "build_deck.js ported (paths made relative, mapped numbers routed through V()); fix any NOT FOUND lines by hand."
echo "Then rebuild with provenance:  scripts/build_all.sh"
