#!/bin/sh
# Rebuild phase 3 end to end (from literature_review/phase3).
set -e
S=~/software/sensein/agent_skills/skills/synthscholar/scripts
UV="uv run --project ${SYNTHSCHOLAR_ENV}"
cd "$(dirname "$0")"
python3 s1_integrity.py
python3 s2_quotes.py > /dev/null
python3 s4_synthesis.py > /dev/null
$UV python s3_assemble.py
cp review_draft.json ../review.json
$UV python $S/update_provenance.py ../review.json --provenance search_provenance_phase3.json --replace-queries --outdir prov_tmp --formats json
cp prov_tmp/review.json ../review.json && rm -r prov_tmp
$UV python $S/export_review.py ../review.json --check
$UV python $S/export_review.py ../review.json --outdir ../out --formats md ttl json
$UV python s5_kg.py
$UV python s5_sparql_checks.py
$UV --with matplotlib python s6_figures.py

# The synthscholar exporter writes a fixed sentence claiming human verification; replace it with what happened.
python3 - <<'PY'
import re, pathlib
p = pathlib.Path("../out/review.md")
s = p.read_text()
s = s.replace(
    "Studies were screened using AI-assisted batch screening with human verification. Title/abstract screening was inclusive; full-text screening was strict.",
    "Metadata screening was rule-based (open-access availability, publication type). Full-text screening, charting and appraisal were performed by AI agents (Claude Sonnet, eight parallel batches) following the protocol and charting instructions; every supporting quote was verified mechanically against the source text. No human verified individual screening or charting decisions in this run.")
p.write_text(s)
PY
