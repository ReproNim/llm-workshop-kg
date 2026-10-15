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
[ -f "$plan" ] && cp "$plan" "$root/slides/talk_plan.md"
echo "Copied apply_theme.js, old_deck_v3.md, make_slide_figs.py and talk_plan.md."
echo "build_deck.js is NOT overwritten: merge workspace changes into slides/build_deck.js by hand,"
echo "keeping V() lookups for mapped values, e.g.  diff -u slides/build_deck.js $src/build_deck.js"
echo "Then rebuild with provenance:  scripts/build_all.sh"
