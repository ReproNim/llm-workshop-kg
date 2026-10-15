"""Dataset <-> publication links: AbstractAtlas (OHBM 2026 abstracts and extracted claims) and OpenAlex.

AbstractAtlas: the deployed site's content-addressed bundle ohbm2026.parquet (sha256 in the URL) is read,
not regenerated. Abstracts whose title or text mention ABIDE (or CNP / ds000030) become ex:Abstract nodes
with their AbstractAtlas claims (claim type, ECO codes, verified source quotes) and corpus-local author
IDs (no global sameAs). Each dataset link has a status:
  uses-data (stated)  a sentence says data/participants/scans came from the dataset
  mentions            the dataset is named without such a statement
OpenAlex: works citing Di Martino 2014 or Abraham 2017 whose title/abstract mention ABIDE, linked with
status candidate (cites a dataset paper and names the dataset; use not verified).
Link counts are recorded as dated snapshots (appended, never overwritten), like resource activity.

  uv run python code/publications.py             # build graph/publications.ttl from the pinned bundle + latest OpenAlex pull
  uv run python code/publications.py --refresh   # also append a link snapshot (network)

Writes graph/publications.ttl, graph/publication_links_activity.ttl, results/publications.json.
"""

import datetime as dt
import io
import json
import re
import sys
import urllib.parse
import urllib.request

import pandas as pd
import pyarrow.parquet as pq
from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace, URIRef

from common import DATA, GRAPH, RESULTS, ROOT, sha256_file, write_json

E = Namespace("urn:repronim:abide:")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
OBO = Namespace("http://purl.org/obo/")
AA_SHA = "dd1a1a8d88f7f505128733bf789c6a3fa4f48ed62e546bebfab2453587b0149f"
AA_URL = f"https://aadata.cirrusscience.org/{AA_SHA}/ohbm2026.parquet"
AA_REPO_COMMIT = "181652e2be0902a4926d292d9ec0e230dfd97b96"
AA_PATH = DATA / "abstractatlas/ohbm2026.parquet"
OPENALEX_CACHE = DATA / "openalex_abide.json"
SNAP = GRAPH / "publication_links_activity.ttl"
DATASETS = {
    "abide": (r"\bABIDE\b", "dataset/abide"),
    "cnp_ds000030": (r"\bds000030\b|Consortium for Neuropsychiatric Phenomics|\bUCLA\s+CNP\b|\bCNP\b", "dataset/ds000030"),
}
USE_PATTERN = re.compile(r"\b(data|dataset|participants|subjects|individuals|sample|scans|images|cohort|children|adults)\b[^.]{0,80}\b(from|of|in|obtained|drawn|downloaded|selected)\b[^.]{0,30}\b(the\s+)?(%s)",
                         re.IGNORECASE)
PAPERS = {"dimartino2014": "10.1038/mp.2013.78", "abraham2017": "10.1016/j.neuroimage.2016.10.045"}


def load_bundle() -> dict[str, pd.DataFrame]:
    """Read the AbstractAtlas container parquet into named tables."""
    if not AA_PATH.exists():
        AA_PATH.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(AA_URL, headers={"User-Agent": "abide-kg-rebuild/1.0 (+https://github.com/ReproNim)"})
        with urllib.request.urlopen(req, timeout=300) as r:
            AA_PATH.write_bytes(r.read())
    if sha256_file(AA_PATH) != AA_SHA:
        raise SystemExit("AbstractAtlas bundle hash mismatch")
    t = {r["table_name"]: r["table_bytes"] for r in pq.read_table(AA_PATH).to_pylist()}
    return {k: pq.read_table(io.BytesIO(t[k])).to_pandas() for k in ("abstracts", "authors", "enrichment_claims")}


def abstract_text(row) -> str:
    """Title plus all section texts."""
    parts = [str(row.title)]
    sec = row.sections
    if isinstance(sec, dict):
        parts += [str(v) for v in sec.values()]
    elif sec is not None:
        for s in list(sec):
            parts += [str(v) for v in (s.values() if isinstance(s, dict) else [s])]
    return re.sub(r"\s+", " ", " ".join(parts))


def get(url: str):
    """GET JSON."""
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.loads(r.read())


def openalex_pull() -> dict:
    """Works citing the two ABIDE papers that mention ABIDE in title/abstract (count + up to 50 most cited)."""
    out = {"pulled_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "by_paper": {}}
    for key, doi in PAPERS.items():
        w = get(f"https://api.openalex.org/works/doi:{doi}")
        wid = w["id"].rsplit("/", 1)[-1]
        q = "https://api.openalex.org/works?" + urllib.parse.urlencode({"filter": f"cites:{wid},title_and_abstract.search:ABIDE", "per_page": 50, "sort": "cited_by_count:desc"})
        body = get(q)
        out["by_paper"][key] = {"openalex_id": wid, "cited_by_count": w.get("cited_by_count"), "query": q, "count": body["meta"]["count"],
                                "sample": [{"id": r["id"], "doi": r.get("doi"), "title": r.get("title"), "year": r.get("publication_year"),
                                            "cited_by_count": r.get("cited_by_count")} for r in body["results"]]}
    OPENALEX_CACHE.write_text(json.dumps(out, indent=1))
    return out


def build(refresh: bool) -> dict:
    """Write the publications graph (and optionally a new snapshot)."""
    tabs = load_bundle()
    ab, au, cl = tabs["abstracts"], tabs["authors"], tabs["enrichment_claims"]
    oa = openalex_pull() if (refresh or not OPENALEX_CACHE.exists()) else json.loads(OPENALEX_CACHE.read_text())
    g = Graph()
    for k, v in (("ex", E), ("prov", PROV), ("dct", DCT)):
        g.bind(k, v)
    src = E["source/abstractatlas_ohbm2026"]
    g.add((src, RDF.type, PROV.Entity))
    g.add((src, RDFS.label, Literal("AbstractAtlas OHBM 2026 data bundle")))
    g.add((src, PROV.atLocation, URIRef(AA_URL)))
    g.add((src, E.sha256, Literal(AA_SHA)))
    g.add((src, E.codeRepository, URIRef(f"https://github.com/sensein/abstractatlas/tree/{AA_REPO_COMMIT}")))
    g.add((src, E.note, Literal("read only; AbstractAtlas pipeline not rerun. Claims are AbstractAtlas extractions, not verified here beyond their own quote check.")))
    DCAT = Namespace("http://www.w3.org/ns/dcat#")
    g.bind("dcat", DCAT)
    for ds, label, page in (
        ("dataset/abide", "ABIDE (Autism Brain Imaging Data Exchange), all releases", "https://fcon_1000.projects.nitrc.org/indi/abide/"),
        ("dataset/abide_i", "ABIDE I", "https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html"),
        ("dataset/abide_ii", "ABIDE II", "https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html"),
        ("dataset/ds000030", "UCLA CNP (OpenNeuro ds000030)", "https://openneuro.org/datasets/ds000030"),
    ):
        g.add((E[ds], RDF.type, E.Dataset))
        g.add((E[ds], RDF.type, DCAT.Dataset))
        g.add((E[ds], RDFS.label, Literal(label)))
        g.add((E[ds], DCAT.landingPage, URIRef(page)))
        g.add((E[ds], E.knowledgeScope, E["scope/lake"]))
        g.add((E[ds], E.accessLevel, Literal("public")))
    for part in ("dataset/abide_i", "dataset/abide_ii"):
        g.add((E["dataset/abide"], DCT.hasPart, E[part]))
    authors = {int(r.author_id): r for r in au.itertuples()}
    stats = {}
    claims_by = cl.groupby("poster_id")
    for key, (pat, ds) in DATASETS.items():
        rx = re.compile(pat)
        use = re.compile(USE_PATTERN.pattern % pat.replace("\\b", ""), re.IGNORECASE)
        n_m, n_u, n_claims = 0, 0, 0
        for row in ab.itertuples():
            text = abstract_text(row)
            if not rx.search(text):
                continue
            pid = int(row.poster_id)
            a = E[f"abstract/ohbm2026/{pid}"]
            g.add((a, RDF.type, E.Abstract))
            g.add((a, RDF.type, PROV.Entity))
            g.add((a, DCT.title, Literal(row.title)))
            g.add((a, E.posterId, Literal(pid, datatype=XSD.integer)))
            g.add((a, PROV.wasDerivedFrom, src))
            sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if rx.search(s)]
            stated = [s for s in sentences if use.search(s)]
            status = "uses-data (stated)" if stated else "mentions"
            n_u += bool(stated)
            n_m += not stated
            link = E[f"datalink/{key}/ohbm2026/{pid}"]
            g.add((link, RDF.type, E.DatasetPublicationLink))
            target = ds
            if key == "abide":
                rels = {("ABIDE II" if m.group(1) in ("II", "2") else "ABIDE I") for m in re.finditer(r"ABIDE[- ]?(II|I|1|2)\b", text)}
                targets = ["dataset/abide_i"] * ("ABIDE I" in rels) + ["dataset/abide_ii"] * ("ABIDE II" in rels) or ["dataset/abide"]
            else:
                targets = [target]
            for t in targets:
                g.add((link, E.dataset, E[t]))
            g.add((link, E.publication, a))
            g.add((link, E.status, Literal(status)))
            g.add((link, E.evidenceQuote, Literal((stated or sentences)[0][:400])))
            g.add((link, E.method, Literal("regex over title and sections of the AbstractAtlas bundle; 'stated' needs a data-source sentence")))
            if key == "abide":
                rel = sorted({("ABIDE II" if m.group(1) in ("II", "2") else "ABIDE I") for m in re.finditer(r"ABIDE[- ]?(II|I|1|2)\b", text)})
                g.add((link, E.abideReleaseNamed, Literal(", ".join(rel) if rel else "release not named")))
            for aid in list(row.author_ids)[:12]:
                ar = authors.get(int(aid))
                if ar is None:
                    continue
                an = E[f"aa_author/{int(aid)}"]
                g.add((an, RDF.type, PROV.Agent))
                g.add((an, RDFS.label, Literal(ar.name)))
                g.add((an, E.identityScope, Literal("AbstractAtlas corpus-local author id (name + primary affiliation); not a global identity")))
                g.add((a, DCT.creator, an))
            if pid in claims_by.groups:
                for c in claims_by.get_group(pid).itertuples():
                    cn = E[f"abstract/ohbm2026/{pid}/claim/{int(c.claim_index)}"]
                    g.add((cn, RDF.type, E.AbstractClaim))
                    g.add((cn, E.statedIn, a))
                    g.add((cn, RDFS.label, Literal(c.claim)))
                    g.add((cn, E.claimTypeAbstractAtlas, Literal(c.claim_type)))
                    g.add((cn, E.sourceQuote, Literal(c.source)))
                    g.add((cn, E.sourceQuoteVerified, Literal(bool(c.source_quote_verified))))
                    for eco in list(c.evidence_eco_codes):
                        g.add((cn, E.ecoCode, URIRef("http://purl.obolibrary.org/obo/" + str(eco).replace(":", "_"))))
                    n_claims += 1
        stats[key] = {"abstracts_matching": n_m + n_u, "uses_data_stated": n_u, "mentions_only": n_m, "claims": n_claims}
    rels = [str(o) for o in g.objects(None, E.abideReleaseNamed)]
    stats["abide"]["release_named"] = {r: rels.count(r) for r in sorted(set(rels))}
    stats["abide"]["hand_check_of_stated"] = "17 'uses-data (stated)' links read by hand on 2026-10-15: 15 correct; posters 1217 and 639 are not ABIDE data use (a regex match on a long sentence and a reference title)"
    for key, rec in oa["by_paper"].items():
        for w in rec["sample"]:
            pn = URIRef(w["id"])
            g.add((pn, RDF.type, E.Publication))
            g.add((pn, DCT.title, Literal(w["title"] or "")))
            if w.get("doi"):
                g.add((pn, DCT.identifier, URIRef(w["doi"])))
            g.add((pn, E.year, Literal(w["year"], datatype=XSD.integer)))
            link = E[f"datalink/abide/openalex/{w['id'].rsplit('/', 1)[-1]}"]
            g.add((link, RDF.type, E.DatasetPublicationLink))
            g.add((link, E.dataset, E["dataset/abide_i"]))
            g.add((link, E.publication, pn))
            g.add((link, E.status, Literal("candidate")))
            g.add((link, E.method, Literal(f"OpenAlex: cites {key} and title/abstract mention ABIDE")))
            g.add((link, E.query, URIRef(rec["query"])))
    g.serialize(GRAPH / "publications.ttl", format="turtle")

    snaps = Graph()
    if SNAP.exists():
        snaps.parse(SNAP)
    snaps.bind("ex", E)
    snaps.bind("prov", PROV)
    if refresh or len(snaps) == 0:
        now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
        stamp = now.strftime("%Y%m%dT%H%M%SZ")
        act = E[f"activity/refresh_publications/{stamp}"]
        snaps.add((act, RDF.type, E.RefreshActivity))
        snaps.add((act, RDF.type, PROV.Activity))
        snaps.add((act, E.script, Literal("code/publications.py --refresh")))
        snaps.add((act, E.scriptSha256, Literal(sha256_file(ROOT / "code/publications.py"))))
        for key, s in stats.items():
            sn = E[f"snapshot/publication_links/{key}/{stamp}"]
            snaps.add((sn, RDF.type, E.PublicationLinkSnapshot))
            snaps.add((sn, RDF.type, PROV.Entity))
            snaps.add((sn, E.snapshotOf, E[DATASETS[key][1]]))
            snaps.add((sn, PROV.generatedAtTime, Literal(now.isoformat(), datatype=XSD.dateTime)))
            snaps.add((sn, PROV.wasGeneratedBy, act))
            snaps.add((sn, E.abstractsLinked, Literal(s["abstracts_matching"], datatype=XSD.integer)))
            snaps.add((sn, E.abstractsUsesDataStated, Literal(s["uses_data_stated"], datatype=XSD.integer)))
            snaps.add((sn, E.abstractSource, URIRef(AA_URL)))
            if key == "abide":
                for pk, rec in oa["by_paper"].items():
                    snaps.add((sn, E[f"openalexCiting_{pk}_mentioningABIDE"], Literal(rec["count"], datatype=XSD.integer)))
                    snaps.add((sn, E.openalexQuery, URIRef(rec["query"])))
        snaps.serialize(SNAP, format="turtle")
    out = {"abstractatlas": {"bundle": AA_URL, "repo_commit": AA_REPO_COMMIT, "n_abstracts": len(ab), "n_claims_total": len(cl), "by_dataset": stats},
           "openalex": {k: {kk: v[kk] for kk in ("openalex_id", "cited_by_count", "count", "query")} | {"sample_n": len(v["sample"])} for k, v in oa["by_paper"].items()},
           "openalex_pulled_at": oa["pulled_at"], "snapshots": len(set(snaps.subjects(RDF.type, E.PublicationLinkSnapshot))), "triples": len(g)}
    write_json("publications.json", out)
    print(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    build("--refresh" in sys.argv)
