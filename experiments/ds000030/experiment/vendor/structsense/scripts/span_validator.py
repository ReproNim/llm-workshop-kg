"""Validate NER spans against the source text.

After extraction (and especially after merging chunk results), every entity's
start/end must satisfy `text[start:end] == entity`. That is the one hard invariant;
everything else here is about not throwing away good items while enforcing it.

Two things this module deliberately does NOT assume:

**A span may cross sentence boundaries.** The `sentence` field is a *context window*,
not a single grammatical sentence. Gold-standard cell annotations put roughly a
quarter of spans across sentence boundaries even after sentence segmentation is
cleaned up (measured: 31.2% of gold spans looked multi-sentence with a naive splitter,
23.0% with a good one — so a fifth of them are genuinely multi-sentence, not artifacts).
An earlier version rejected any item whose surface was not a substring of `sentence`,
which silently deleted exactly that class: the extractor did its job, the window held
one of the sentences, and the item vanished with no diagnostic.

**Substring membership is not location.** `sentence in text` and `surface in sentence`
can both be true while the offsets point somewhere else entirely — common when a cell
name or a boilerplate sentence repeats, which in these papers is constant. Anchoring is
checked by offset, and `sentence` is only used as a *hint* for repair.
"""
from __future__ import annotations

from typing import Iterable, Optional, Tuple

# Minimum tolerance when comparing a span's start against its window's extent. The
# tolerance is otherwise the window's own length, so it scales with the evidence
# instead of being a fixed character count — a fixed slack large enough for a
# paragraph is vacuous on a short passage (a 200-char slack made every span
# "consistent" with every window in a 130-char text, i.e. the check did nothing).
_MIN_WINDOW_SLACK = 40


def _surface_of(item: dict) -> Optional[str]:
    """The item's surface form. `entity` for entities, `term` for key_terms."""
    return item.get("entity") or item.get("term")


def anchor_ok(text: str, item: dict) -> bool:
    """The one hard invariant: the offsets select exactly the surface form."""
    surface = _surface_of(item)
    start, end = item.get("start"), item.get("end")
    if surface is None or not isinstance(start, int) or not isinstance(end, int):
        return False
    if start < 0 or end > len(text) or start >= end:
        return False
    return text[start:end] == surface


def window_consistent(text: str, item: dict) -> bool:
    """True if `sentence` does not contradict the offsets.

    A missing or unfindable window is not a contradiction — it is missing evidence,
    and the anchor already proved the span. This returns False only when the window
    IS locatable and every one of its occurrences sits clear of the span, which means
    the two disagree about where in the document the item is.
    """
    window = item.get("sentence") or ""
    start, end = item.get("start"), item.get("end")
    if not window or not isinstance(start, int) or not isinstance(end, int):
        return True

    # Every occurrence of the window, since the same sentence can repeat.
    positions = []
    at = text.find(window)
    while at != -1:
        positions.append(at)
        at = text.find(window, at + 1)
    if not positions:
        return True  # window not in text (whitespace-normalised, truncated, …)

    # Constrain the span's START, not its end. That asymmetry is the whole point: a
    # multi-sentence span begins inside its window — typically the first of the
    # sentences it covers — and legitimately runs past the window's end. What is NOT
    # legitimate is a span beginning well before the window, which means the two are
    # describing different places in the document.
    slack = max(_MIN_WINDOW_SLACK, len(window))
    for w_start in positions:
        w_end = w_start + len(window)
        if (w_start - slack) <= start <= (w_end + slack):
            return True
    return False


def validate(text: str, item: dict) -> bool:
    """True if the item's offsets anchor its surface form and nothing contradicts."""
    return anchor_ok(text, item) and window_consistent(text, item)


def repair_span(text: str, item: dict) -> Optional[dict]:
    """Re-locate the surface form in `text`, preferring the occurrence nearest the
    item's own claim about where it is.

    A bare `text.index(surface)` returns the FIRST occurrence, which for a cell name
    used thirty times in a paper is almost never the right one. Since exhaustive
    extraction emits one item per occurrence, that also collapses distinct mentions
    onto one span, where `dedupe()` then discards them as duplicates — turning a
    repairable offset slip into lost mentions.
    """
    surface = _surface_of(item)
    if not surface:
        return None

    occurrences = []
    at = text.find(surface)
    while at != -1:
        occurrences.append(at)
        at = text.find(surface, at + 1)
    if not occurrences:
        return None

    # Preference order for "where this item claims to be": the window's position,
    # then the item's own start offset.
    anchor: Optional[int] = None
    window = item.get("sentence") or ""
    if window:
        w_at = text.find(window)
        if w_at != -1:
            local = window.find(surface)
            anchor = w_at + (local if local != -1 else 0)
    if anchor is None and isinstance(item.get("start"), int):
        anchor = item["start"]

    best = occurrences[0] if anchor is None else min(
        occurrences, key=lambda p: (abs(p - anchor), p)
    )
    new = dict(item)
    new["start"] = best
    new["end"] = best + len(surface)
    return new


def validate_all(text: str, items: Iterable[dict]) -> Tuple[list[dict], list[dict]]:
    """Partition items into (valid, dropped).

    Repaired items are placed in `valid` and carry `span_repaired: True` so a
    downstream reader can tell a reported offset from a reconstructed one — a silent
    repair is indistinguishable from a correct extraction, and one of those deserves
    a second look. Items that cannot be repaired go to `dropped` with
    `drop_reason` set, so "N items dropped" is never the whole story.
    """
    valid, dropped = [], []
    for it in items:
        if validate(text, it):
            valid.append(it)
            continue
        repaired = repair_span(text, it)
        if repaired is not None and validate(text, repaired):
            repaired["span_repaired"] = True
            valid.append(repaired)
            continue
        bad = dict(it)
        surface = _surface_of(it)
        if not surface:
            bad["drop_reason"] = "no surface form (entity/term missing)"
        elif surface not in text:
            bad["drop_reason"] = "surface form does not occur in the source text"
        elif not anchor_ok(text, it):
            bad["drop_reason"] = (
                f"offsets do not select the surface form and no occurrence was "
                f"consistent with the reported window "
                f"(start={it.get('start')!r}, end={it.get('end')!r})"
            )
        else:
            bad["drop_reason"] = "reported window contradicts the offsets"
        dropped.append(bad)
    return valid, dropped


if __name__ == "__main__":
    _text = ("Astrocytes were labelled in the medial cortex of adult mice. Microglia "
             "were not labelled here. Later, astrocytes were counted again.")
    _first_sentence = _text[:_text.index(".") + 1]
    _at = _text.index("in the medial")

    _cases = [
        ("correct single-sentence span",
         {"entity": "Astrocytes", "start": 0, "end": 10, "sentence": _first_sentence}),
        # The case the old validator silently deleted: the span runs past the window.
        ("span crossing a sentence boundary",
         {"entity": _text[_at:_at + 60], "start": _at, "end": _at + 60,
          "sentence": _first_sentence}),
        ("offsets wrong, surface real (repairable)",
         {"entity": "Microglia", "start": 999, "end": 1008, "sentence": ""}),
        ("surface absent (dropped with a reason)",
         {"entity": "tanycytes", "start": 0, "end": 9, "sentence": ""}),
    ]
    for _label, _item in _cases:
        _ok, _bad = validate_all(_text, [_item])
        if _ok:
            _r = " (repaired)" if _ok[0].get("span_repaired") else ""
            print(f"kept    {_label}{_r}: [{_ok[0]['start']}:{_ok[0]['end']}]")
        else:
            print(f"dropped {_label}: {_bad[0]['drop_reason']}")

