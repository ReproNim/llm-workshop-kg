"""Append a dated activity snapshot for every catalog resource (never overwrites earlier snapshots).

Per GitHub resource: last push, commits in the last 90/365 days, distinct commit authors in the last
365 days, issues and PRs opened/closed in the last 90 days, open issue count, latest release and date.
Per resource with a DOI or search phrase: OpenAlex count (works citing the DOI, or works matching the
repository URL / phrase), with the exact query recorded.

  uv run python code/refresh_activity.py [--only id1,id2] [--min-interval-minutes N]

Appends to graph/resource_activity.ttl and results/resource_activity_log.jsonl; a full refresh also appends a
dataset-publication link snapshot (code/publications.py --refresh).
"""

import datetime as dt
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace, URIRef

from common import GRAPH, RESULTS, ROOT, sha256_file
from resources_catalog import R

E = Namespace("urn:repronim:abide:")
PROV = Namespace("http://www.w3.org/ns/prov#")
OUT = GRAPH / "resource_activity.ttl"
LOG = RESULTS / "resource_activity_log.jsonl"
API = "https://api.github.com/"
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or subprocess.run(["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()


def get(url: str, headers: dict | None = None) -> tuple[object, dict]:
    """GET JSON with retries; returns (body, response headers)."""
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers or {})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read() or b"null"), dict(r.headers)
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 409, 451):
                return None, {}
            time.sleep(2 * (attempt + 1))
        except Exception:  # noqa: BLE001
            time.sleep(2 * (attempt + 1))
    return None, {}


def gh(path: str, params: dict | None = None) -> tuple[object, dict]:
    """GitHub REST GET."""
    q = f"?{urllib.parse.urlencode(params)}" if params else ""
    return get(API + path + q, {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"})


def paged(path: str, params: dict, limit_pages: int = 30) -> list:
    """All pages of a list endpoint (100 per page)."""
    items = []
    for page in range(1, limit_pages + 1):
        body, _ = gh(path, {**params, "per_page": 100, "page": page})
        if not body:
            break
        items += body
        if len(body) < 100:
            break
    return items


def github_metrics(repo: str, now: dt.datetime) -> dict:
    """Activity metrics for one repository."""
    d90 = (now - dt.timedelta(days=90)).isoformat(timespec="seconds").replace("+00:00", "Z")
    d365 = (now - dt.timedelta(days=365)).isoformat(timespec="seconds").replace("+00:00", "Z")
    meta, _ = gh(f"repos/{repo}")
    meta = meta or {}
    commits = paged(f"repos/{repo}/commits", {"since": d365})
    head, _ = gh(f"repos/{repo}/commits", {"per_page": 1})
    last_commit = ((head or [{}])[0].get("commit", {}).get("committer", {}) or {}).get("date")
    c90 = [c for c in commits if (c.get("commit", {}).get("committer", {}) or {}).get("date", "") >= d90]
    authors = {(c.get("author") or {}).get("login") or (c.get("commit", {}).get("author") or {}).get("email") for c in commits}
    issues = paged(f"repos/{repo}/issues", {"state": "all", "since": d90})
    isp = [i for i in issues if "pull_request" in i]
    isi = [i for i in issues if "pull_request" not in i]
    rel, _ = gh(f"repos/{repo}/releases", {"per_page": 1})
    latest = rel[0] if rel else None
    tag = None
    if not latest:
        tags, _ = gh(f"repos/{repo}/tags", {"per_page": 1})
        tag = tags[0]["name"] if tags else None
    return {
        "last_push": meta.get("pushed_at"),
        "last_commit_default_branch": last_commit,
        "commits_90d": len(c90),
        "commits_365d": len(commits),
        "contributors_365d": len({a for a in authors if a}),
        "issues_opened_90d": sum(i["created_at"] >= d90 for i in isi),
        "issues_closed_90d": sum((i.get("closed_at") or "") >= d90 for i in isi),
        "prs_opened_90d": sum(i["created_at"] >= d90 for i in isp),
        "prs_closed_90d": sum((i.get("closed_at") or "") >= d90 for i in isp),
        "open_issues_and_prs": meta.get("open_issues_count"),
        "stars": meta.get("stargazers_count"),
        "latest_release": (latest or {}).get("tag_name") or tag,
        "latest_release_date": (latest or {}).get("published_at"),
        "archived": meta.get("archived"),
    }


def openalex(r: dict) -> dict:
    """OpenAlex reference count with the query that produced it."""
    if r["doi"]:
        q = f"https://api.openalex.org/works?filter=cites:{{id}}&per_page=1"
        w, _ = get(f"https://api.openalex.org/works/doi:{r['doi']}")
        if not w:
            return {"openalex_query": f"works/doi:{r['doi']}", "openalex_count": None}
        wid = w["id"].rsplit("/", 1)[-1]
        return {"openalex_query": q.replace("{id}", wid), "openalex_count": w.get("cited_by_count"), "openalex_measure": "cited_by_count of the DOI"}
    phrase = r["openalex"] or (f"github.com/{r['repo']}" if r["repo"] else None)
    if not phrase:
        return {}
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"search": f'"{phrase}"', "per_page": 1})
    body, _ = get(url)
    return {"openalex_query": url, "openalex_count": (body or {}).get("meta", {}).get("count"), "openalex_measure": "works matching the quoted phrase (title, abstract, full text)"}


def snapshot(r: dict, now: dt.datetime) -> dict:
    """One resource's snapshot record."""
    rec = {"resource": r["id"], "generated_at": now.isoformat(timespec="seconds")}
    if r["repo"]:
        rec.update(github_metrics(r["repo"], now))
    rec.update(openalex(r))
    return rec


def latest_time(g: Graph) -> dict:
    """Most recent snapshot time per resource in an existing graph."""
    out = {}
    for s, t in g.subject_objects(PROV.generatedAtTime):
        res = g.value(s, E.snapshotOf)
        if res is not None:
            out[str(res)] = max(out.get(str(res), ""), str(t))
    return out


def main() -> None:
    """Append one snapshot per selected resource."""
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))
    min_int = float(sys.argv[sys.argv.index("--min-interval-minutes") + 1]) if "--min-interval-minutes" in sys.argv else 0
    g = Graph()
    if OUT.exists():
        g.parse(OUT)
    for k, v in (("ex", E), ("prov", PROV)):
        g.bind(k, v)
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    prev = latest_time(g)
    todo = []
    for r in R:
        if only and r["id"] not in only:
            continue
        last = prev.get(str(E[f"resource/{r['id']}"]))
        if last and (now - dt.datetime.fromisoformat(last)).total_seconds() < min_int * 60:
            continue
        todo.append(r)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    act = E[f"activity/refresh/{stamp}"]
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip() or "not a git checkout"
    g.add((act, RDF.type, E.RefreshActivity))
    g.add((act, RDF.type, PROV.Activity))
    g.add((act, PROV.startedAtTime, Literal(now.isoformat(), datatype=XSD.dateTime)))
    g.add((act, E.script, Literal("code/refresh_activity.py")))
    g.add((act, E.scriptSha256, Literal(sha256_file(ROOT / "code/refresh_activity.py"))))
    g.add((act, E.codeCommit, Literal(commit)))
    g.add((act, E.nResources, Literal(len(todo), datatype=XSD.integer)))
    with ThreadPoolExecutor(6) as pool:
        recs = list(pool.map(lambda r: snapshot(r, now), todo))
    ended = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    g.add((act, PROV.endedAtTime, Literal(ended.isoformat(), datatype=XSD.dateTime)))
    with LOG.open("a") as log:
        for rec in recs:
            s = E[f"snapshot/{rec['resource']}/{stamp}"]
            g.add((s, RDF.type, E.ResourceActivitySnapshot))
            g.add((s, RDF.type, PROV.Entity))
            g.add((s, E.snapshotOf, E[f"resource/{rec['resource']}"]))
            g.add((s, PROV.wasGeneratedBy, act))
            g.add((s, PROV.generatedAtTime, Literal(now.isoformat(), datatype=XSD.dateTime)))
            g.add((s, RDFS.label, Literal(f"{rec['resource']} activity as of {now.isoformat()}")))
            for k, v in rec.items():
                if k in ("resource", "generated_at") or v is None:
                    continue
                if k in ("last_push", "last_commit_default_branch", "latest_release_date"):
                    g.add((s, E[k], Literal(v, datatype=XSD.dateTime)))
                elif isinstance(v, bool):
                    g.add((s, E[k], Literal(v, datatype=XSD.boolean)))
                elif isinstance(v, int):
                    g.add((s, E[k], Literal(v, datatype=XSD.integer)))
                elif k == "openalex_query":
                    g.add((s, E[k], URIRef(v)))
                else:
                    g.add((s, E[k], Literal(v)))
            log.write(json.dumps(rec) + "\n")
    g.serialize(OUT, format="turtle")
    n_snap = len(set(g.subjects(RDF.type, E.ResourceActivitySnapshot)))
    print(f"appended {len(recs)} snapshots at {now.isoformat()} in {(ended - now).total_seconds():.0f}s; graph now holds {n_snap} snapshots")
    if not only:
        import publications

        publications.build(refresh=True)


if __name__ == "__main__":
    main()
