"""Second open-access pass for DOIs the skill's OA chain missed: Europe PMC render, then other OpenAlex OA locations."""
import json, sys, time, re
from pathlib import Path
import httpx

ROOT = Path(__file__).resolve().parent.parent
UA = "SynthScholar systematic review (mailto:satra@mit.edu)"


def is_pdf(b):
    return b[:5] == b"%PDF-"


def main(missing_file, outdir):
    out = Path(outdir); out.mkdir(exist_ok=True)
    recs = {(r.get("doi") or "").replace("https://doi.org/", "").lower(): r
            for r in json.load(open(ROOT / "search" / "openalex_records.json"))}
    manifest, log = {}, []
    with httpx.Client(timeout=40, follow_redirects=True, headers={"User-Agent": UA}) as c:
        for doi in [l.strip() for l in open(missing_file) if l.strip()]:
            r = recs.get(doi, {})
            tries = []
            pmcid = (r.get("ids") or {}).get("pmcid", "")
            if pmcid:
                pid = pmcid.rstrip("/").split("/")[-1]
                tries.append(("europe_pmc_oa", f"https://europepmc.org/articles/{pid}?pdf=render"))
            for loc in [r.get("best_oa_location")] + []:
                if loc and loc.get("pdf_url"):
                    tries.append(("openalex_pdf", loc["pdf_url"]))
            got = None
            for route, url in tries:
                try:
                    resp = c.get(url)
                    time.sleep(1)
                    if resp.status_code == 200 and is_pdf(resp.content):
                        got = (route, url, resp.content); break
                except Exception as e:
                    pass
            if got:
                name = doi.replace("/", "_") + ".pdf"
                (out / name).write_bytes(got[2])
                manifest[name] = {"doi": doi, "full_text_source": got[0]}
                log.append({"doi": doi, "status": "OK", "route": got[0], "url": got[1]})
                print("OK  ", doi, got[0], flush=True)
            else:
                log.append({"doi": doi, "status": "MISS", "tried": [u for _, u in tries]})
                print("MISS", doi, flush=True)
    (out / "retrieval_manifest.json").write_text(json.dumps(manifest, indent=2))
    (ROOT / "search" / "fetch_fallback_log.json").write_text(json.dumps(log, indent=2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
