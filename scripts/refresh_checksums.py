# /// script
# requires-python = ">=3.11"
# ///
"""Refresh SHA256SUMS and SHA256SUMS.json in a package for files a recorded step rewrote.

    uv run scripts/refresh_checksums.py experiments/abide results/shacl_report.txt results/shacl_summary.json
"""

import hashlib
import json
import sys
from pathlib import Path

root, files = Path(sys.argv[1]), set(sys.argv[2:])
sha = lambda p: hashlib.sha256((root / p).read_bytes()).hexdigest()
sums = root / "SHA256SUMS"
lines = []
for line in sums.read_text().splitlines():
    digest, name = line.split(None, 1)
    name = name.lstrip("*").strip()
    lines.append(f"{sha(name)}  {name}" if name in files else line)
sums.write_text("\n".join(lines) + "\n")
manifest = root / "SHA256SUMS.json"
data = json.loads(manifest.read_text())
for name in files & set(data):
    data[name] = sha(name)
manifest.write_text(json.dumps(data, indent=1))
print(f"refreshed {len(files)} entries in {root}")
