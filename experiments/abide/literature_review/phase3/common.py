"""Shared helpers for phase 3: loading records and normalising text for quote verification."""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIG = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st"}
DASHES = {"‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "−": "-", "­": ""}
QUOTES = {"‘": "'", "’": "'", "“": '"', "”": '"', " ": " "}


def norm(s: str) -> str:
    """Normalise for substring matching: ligatures, dashes, quotes, line-wrap hyphenation, whitespace, case."""
    s = s or ""
    for t in (LIG, QUOTES):
        for k, v in t.items():
            s = s.replace(k, v)
    s = s.replace("­", "")
    for zw in ("​", "‌", "‍", "﻿"):
        s = s.replace(zw, "")
    # line-wrap hyphenation: "classi-\nfied" -> "classified" (before dash folding)
    s = re.sub(r"(\w)[-‐‑]\s*\n\s*(\w)", r"\1\2", s)
    for k, v in DASHES.items():
        s = s.replace(k, v)
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


def load_corpus():
    return json.load(open(ROOT / "corpus.json"))["items"]


def load_records():
    recs = []
    for i in range(1, 9):
        for r in json.load(open(ROOT / "batches" / f"charting_{i}_records.json")):
            r["_batch"] = i
            recs.append(r)
    return recs
