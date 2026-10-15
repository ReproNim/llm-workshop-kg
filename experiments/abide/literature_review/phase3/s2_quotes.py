"""Step 2: re-verify every quote against its article's full_text; write verified records + a log."""
import copy
import json
import re
from common import ROOT, load_corpus, load_records, norm

QSEG = re.compile(r'["“]([^"“”]{20,}?)["”]')
ELLIPSIS = re.compile(r"\s*(?:\.\.\.|…|\[\s*\.\.\.\s*\]|\[…\])\s*")
MARK = "[quote dropped: not verbatim in full text]"


def make_checker(text):
    nt = norm(text)
    nt_nospace = nt.replace(" ", "")
    nt_nohyph = re.sub(r"-\s*", "", nt).replace(" ", "")

    def check(q):
        """Return 'exact' | 'ellipsis' | 'spacing' | None."""
        nq = norm(q).strip(" .,;:")
        if not nq:
            return None
        if nq in nt:
            return "exact"
        parts = [norm(p).strip(" .,;:") for p in ELLIPSIS.split(q)]
        parts = [p for p in parts if p]
        if len(parts) > 1 and all(p in nt for p in parts):
            return "ellipsis"
        # PDF extraction sometimes drops/inserts spaces ("stored in.tar"); tolerate spacing-only differences
        if nq.replace(" ", "") in nt_nospace:
            return "spacing"
        # line-wrap hyphenation rendered as "iden- tified" or "multi-\nsite" vs "multi-site"
        if re.sub(r"-\s*", "", nq).replace(" ", "") in nt_nohyph:
            return "hyphenation"
        return None
    return check


def main():
    corpus = {e["pmid"]: e for e in load_corpus()}
    integrity = json.load(open(ROOT / "phase3" / "integrity.json"))
    mismatched = set(integrity["mismatched"])
    out, log = [], []
    stats = {"checked": 0, "passed": 0, "dropped": 0, "empty_quotes": 0, "by_kind": {}, "by_basis": {}}

    def tally(kind, sid, loc, q, res):
        stats["checked"] += 1
        b = stats["by_kind"].setdefault(kind, {"checked": 0, "passed": 0, "dropped": 0})
        b["checked"] += 1
        if res:
            stats["passed"] += 1; b["passed"] += 1
            stats["by_basis"][res] = stats["by_basis"].get(res, 0) + 1
        else:
            stats["dropped"] += 1; b["dropped"] += 1
            log.append({"source_id": sid, "kind": kind, "location": loc, "quote": q[:400]})

    for r in load_records():
        r = copy.deepcopy(r)
        sid = r["source_id"]
        e = corpus[r["pmid"]]
        basis_text = e.get("abstract", "") if sid in mismatched else (e.get("full_text") or "")
        check = make_checker(basis_text)
        # evidence spans
        kept = []
        for i, sp in enumerate(r.get("evidence_spans", []) or []):
            res = check(sp.get("text", ""))
            tally("evidence_span", sid, f"evidence_spans[{i}]", sp.get("text", ""), res)
            if res:
                kept.append(sp)
        if "evidence_spans" in r:
            r["evidence_spans"] = kept
        # risk-of-bias support: quoted segments inside the support text
        for i, a in enumerate((r.get("risk_of_bias") or {}).get("assessments", []) or []):
            sup = a.get("support", "")
            for q in QSEG.findall(sup):
                res = check(q)
                tally("rob_support", sid, f"risk_of_bias.assessments[{i}] {a.get('domain','')}", q, res)
                if not res:
                    sup = sup.replace(q, MARK)
            a["support"] = sup.replace(f'"{MARK}"', MARK).replace(f"“{MARK}”", MARK)
        # custom_fields "answer | quote: "..."" (empty quotes are not quotes)
        cf = (r.get("charting") or {}).get("custom_fields") or {}
        for k, v in list(cf.items()):
            m = re.search(r'\s*\|\s*quote:\s*(.*)$', v, re.S)
            if not m:
                continue
            q = m.group(1).strip()
            if len(q) >= 2 and q[0] in '"“' and q[-1] in '"”':
                q = q[1:-1]
            if not q.strip():
                stats["empty_quotes"] += 1
                cf[k] = v[:m.start()]
                continue
            res = check(q)
            tally("custom_field", sid, f"custom_fields[{k[:4].strip()}]", q, res)
            if not res:
                cf[k] = v[:m.start()] + " | " + MARK
        # kg_link quotes
        kg = r.get("kg_link") or {}
        if kg.get("evidence_quotes"):
            kq = []
            for i, q in enumerate(kg["evidence_quotes"]):
                res = check(q)
                tally("kg_link", sid, f"kg_link.evidence_quotes[{i}]", q, res)
                if res:
                    kq.append(q)
            kg["evidence_quotes"] = kq
        if sid in mismatched:
            r["_quote_basis"] = "abstract (full text mismatched)"
        out.append(r)
    json.dump(out, open(ROOT / "phase3" / "records_verified.json", "w"), indent=1, ensure_ascii=False)
    json.dump({"stats": stats, "dropped": log, "quote_basis_note":
               "Quotes for full-text-mismatched items (" + ", ".join(sorted(mismatched)) + ") were checked against the corpus abstract."},
              open(ROOT / "phase3" / "quote_verification.json", "w"), indent=1, ensure_ascii=False)
    print(json.dumps(stats, indent=1))
    for d in log:
        print(d["source_id"], d["kind"], d["location"], "|", d["quote"][:160].replace("\n", " "))


if __name__ == "__main__":
    main()
