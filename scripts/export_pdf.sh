#!/usr/bin/env bash
# Export a .pptx to PDF. Uses LibreOffice when present, otherwise Microsoft PowerPoint (macOS).
# PowerPoint cannot open two documents with the same name, so it works on a uniquely named copy.
#   scripts/export_pdf.sh slides/deck.pptx slides/deck.pdf
set -euo pipefail
src="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
dst="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"
if command -v soffice >/dev/null; then
  outdir="$(mktemp -d)"
  soffice --headless --convert-to pdf --outdir "$outdir" "$src"
  mv "$outdir/$(basename "${src%.pptx}").pdf" "$dst"
  exit 0
fi
# Sandboxed PowerPoint can always read and write inside its own container.
work="$HOME/Library/Containers/com.microsoft.Powerpoint/Data/tmp/export-$$"
mkdir -p "$work"
copy="$work/export-$$-$(basename "$src")"
cp "$src" "$copy"
osascript "$(dirname "$0")/export_pdf.applescript" "$copy" "$work/out.pdf"
mv "$work/out.pdf" "$dst"
rm -rf "$work"
