"""Find resources: SPARQL facet filters + BM25 over descriptions, ranked with a freshness factor.

The latest snapshot per resource is resolved by query (max prov:generatedAtTime); every activity
number is printed with its as-of time and age.

  uv run python code/find_resources.py "convert FreeSurfer stats to NIDM" [--step idp_extraction_to_nidm] [--usage executed] [--top 5]
  uv run python code/find_resources.py --examples      # run the saved example searches

Score = BM25(query, name + description + usage note + facet labels) * (0.5 + 0.5 * freshness),
freshness = exp(-days_since_last_default_branch_commit / 365) (last push when unknown) from the latest snapshot (0.5 when unknown).
"""

import datetime as dt
import json
import math
import re
import sys
from collections import Counter

import pyoxigraph as ox

from common import GRAPH, RESULTS

K1, B = 1.5, 0.75
EXAMPLES = [
    ("convert FreeSurfer stats to NIDM", {}),
    ("containerised reproducible execution on HPC", {}),
    ("harmonised assessment schema for phenotype questionnaires", {}),
    ("query brain volumes across software", {"step": "query_merge"}),
    ("quality control metrics", {}),
]

Q_RESOURCES = """PREFIX ex: <urn:repronim:abide:>
PREFIX schema: <http://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?r ?name ?desc ?usage ?note ?type (GROUP_CONCAT(DISTINCT ?stepLabel; separator=" ") AS ?steps)
       (GROUP_CONCAT(DISTINCT ?edamLabel; separator=" ") AS ?edam) WHERE {
  ?r a ex:Resource ; schema:name ?name ; schema:description ?desc ; ex:usageInExperiment ?usage ; ex:resourceType ?type .
  OPTIONAL { ?r ex:usageNote ?note }
  OPTIONAL { ?r ex:workflowStep ?s . ?s rdfs:label ?stepLabel }
  OPTIONAL { ?r ex:edamOperation|ex:edamTopic|ex:inputFormat|ex:outputFormat ?e . ?e rdfs:label ?edamLabel }
  %s
} GROUP BY ?r ?name ?desc ?usage ?note ?type"""

Q_LATEST = """PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
SELECT ?r ?t ?push ?lastCommit ?c90 ?c365 ?contrib ?rel ?relDate ?oa ?oaQuery WHERE {
  { SELECT ?r (MAX(?t0) AS ?t) WHERE { ?s0 ex:snapshotOf ?r ; prov:generatedAtTime ?t0 } GROUP BY ?r }
  ?s ex:snapshotOf ?r ; prov:generatedAtTime ?t .
  OPTIONAL { ?s ex:last_push ?push } OPTIONAL { ?s ex:last_commit_default_branch ?lastCommit } OPTIONAL { ?s ex:commits_90d ?c90 } OPTIONAL { ?s ex:commits_365d ?c365 }
  OPTIONAL { ?s ex:contributors_365d ?contrib } OPTIONAL { ?s ex:latest_release ?rel } OPTIONAL { ?s ex:latest_release_date ?relDate }
  OPTIONAL { ?s ex:openalex_count ?oa } OPTIONAL { ?s ex:openalex_query ?oaQuery }
}"""


def store() -> ox.Store:
    """In-memory store with the catalog and the activity snapshots as named graphs."""
    s = ox.Store()
    for name in ("resources", "resource_activity"):
        s.bulk_load(path=str(GRAPH / f"{name}.ttl"), format=ox.RdfFormat.TURTLE, to_graph=ox.NamedNode(f"urn:repronim:abide:graph/{name}"))
    return s


def tokens(text: str) -> list[str]:
    """Lower-case word tokens with crude plural folding."""
    return [w[:-1] if w.endswith("s") and len(w) > 3 else w for w in re.findall(r"[a-z0-9]+", text.lower())]


def search(s: ox.Store, query: str, step: str | None = None, usage: str | None = None, top: int = 5, now: dt.datetime | None = None) -> list[dict]:
    """Rank resources for a free-text query within optional facets."""
    filt = ""
    if step:
        filt += f"?r ex:workflowStep <urn:repronim:abide:step/{step}> ."
    if usage:
        filt += f' FILTER (?usage = "{usage}")'
    docs = {}
    for r in s.query(Q_RESOURCES % filt, use_default_graph_as_union=True):
        docs[r["r"].value] = {"name": r["name"].value, "type": r["type"].value, "usage": r["usage"].value, "steps": r["steps"].value,
                              "text": " ".join(x.value for x in (r["name"], r["desc"], r["note"], r["steps"], r["edam"]) if x is not None)}
    latest = {}
    for r in s.query(Q_LATEST, use_default_graph_as_union=True):
        rec = {k: (r[k].value if r[k] is not None else None) for k in ("t", "push", "lastCommit", "c90", "c365", "contrib", "rel", "relDate", "oa", "oaQuery")}
        for k in ("c90", "c365", "contrib", "oa"):
            rec[k] = int(rec[k]) if rec[k] is not None else None
        latest[r["r"].value] = rec
    now = now or dt.datetime.now(dt.timezone.utc)
    corpus = {u: tokens(d["text"]) for u, d in docs.items()}
    n = len(corpus)
    avg = sum(len(t) for t in corpus.values()) / max(n, 1)
    df = Counter(w for t in corpus.values() for w in set(t))
    q = tokens(query)
    out = []
    for u, toks in corpus.items():
        tf = Counter(toks)
        bm = sum(math.log(1 + (n - df[w] + 0.5) / (df[w] + 0.5)) * tf[w] * (K1 + 1) / (tf[w] + K1 * (1 - B + B * len(toks) / avg)) for w in q if w in tf)
        if bm <= 0:
            continue
        a = latest.get(u, {})
        snap_t = dt.datetime.fromisoformat(a["t"]) if a.get("t") else None
        ref = a.get("lastCommit") or a.get("push")
        push = dt.datetime.fromisoformat(ref.replace("Z", "+00:00")) if ref else None
        days_push = (snap_t - push).days if (snap_t and push) else None
        fresh = math.exp(-days_push / 365) if days_push is not None else 0.5
        out.append({
            "resource": u.rsplit("/", 1)[-1], "name": docs[u]["name"], "type": docs[u]["type"], "usage_here": docs[u]["usage"],
            "score": round(bm * (0.5 + 0.5 * fresh), 3), "bm25": round(bm, 3), "freshness": round(fresh, 3),
            "as_of": a.get("t"), "snapshot_age_hours": round((now - snap_t).total_seconds() / 3600, 2) if snap_t else None,
            "last_push": a.get("push"), "last_commit": a.get("lastCommit"), "days_since_push_at_snapshot": days_push,
            "commits_90d": a.get("c90"), "commits_365d": a.get("c365"), "contributors_365d": a.get("contrib"),
            "latest_release": a.get("rel"), "latest_release_date": a.get("relDate"), "openalex_count": a.get("oa"), "openalex_query": a.get("oaQuery"),
        })
    return sorted(out, key=lambda x: -x["score"])[:top]


def show(query: str, rows: list[dict], facets: dict) -> str:
    """Human-readable result block; activity numbers always carry their as-of time and age."""
    lines = [f'query: "{query}"  facets: {facets or "none"}']
    for i, r in enumerate(rows, 1):
        if r["as_of"]:
            act = (f"commits 90d={r['commits_90d']}, 365d={r['commits_365d']}, contributors 365d={r['contributors_365d']}, "
                   f"last default-branch commit {r['last_commit'] or 'n/a'} ({r['days_since_push_at_snapshot']} d before snapshot; last push {r['last_push']}), "
                   f"release {r['latest_release']}, OpenAlex={r['openalex_count']} "
                   f"[as of {r['as_of']}, {r['snapshot_age_hours']} h old]")
        else:
            act = "no activity snapshot"
        lines.append(f"{i}. {r['name']} ({r['type']}; used here: {r['usage_here']}) score={r['score']} (bm25 {r['bm25']} x freshness {r['freshness']})\n   {act}")
    return "\n".join(lines)


def main() -> None:
    """CLI."""
    s = store()
    if "--examples" in sys.argv:
        results, text = [], []
        for q, f in EXAMPLES:
            rows = search(s, q, **f)
            results.append({"query": q, "facets": f, "results": rows})
            text.append(show(q, rows, f))
        (RESULTS / "find_resources_examples.json").write_text(json.dumps(results, indent=1))
        (RESULTS / "find_resources_examples.txt").write_text("\n\n".join(text) + "\n")
        print("\n\n".join(text))
        return
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = {k: sys.argv[sys.argv.index(f"--{k}") + 1] for k in ("step", "usage", "top") if f"--{k}" in sys.argv}
    for k in opts:
        args.remove(opts[k])
    f = {k: v for k, v in opts.items() if k != "top"}
    print(show(" ".join(args), search(s, " ".join(args), top=int(opts.get("top", 5)), **f), f))


if __name__ == "__main__":
    main()
