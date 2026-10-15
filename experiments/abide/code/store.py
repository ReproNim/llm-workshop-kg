"""Build the on-disk Oxigraph store: one named graph per source, plus materialized views with PROV.

Named graphs (urn:repronim:abide:graph/...):
  core, core_v1, papers (inside core), extension, embedding, link, resources, resource_activity, scope,
  pynidm_phenotype (PyNIDM csv2nidm output), and one graph per ReproNim simple2 file
  (urn:repronim:simple2:<path>).
Views (SPARQL Update files in queries/views/, executed in order):
  type_closure      ?m a nidm:DataElement for every instance of a DataElement subclass
  volume_measures   CDE measures that are volumes (measureOf/datumType), with region and side
  volumes           one observation per participant x tool x measure, keyed to our participant IRI
                    by the shared ndar:src_subject_id literal
  phenotype_matrix  participant -> analysis variables and IDPs, direct triples
Each view is recorded in graph view_provenance as an ex:MaterializeView activity that used its input
graphs (with their file hashes) and generated the view graph. The store is rebuilt when any input
file hash differs from data/derived/oxigraph_store.manifest.json.

Usage: uv run python code/store.py [--force]
"""

import glob
import json
import shutil
import sys
import time

import pyoxigraph as ox

from common import DATA, GRAPH, QUERIES, ROOT, sha256_bytes, sha256_file, write_json

STORE = DATA / "derived/oxigraph_store"
MANIFEST = DATA / "derived/oxigraph_store.manifest.json"
G = "urn:repronim:abide:graph/"
VIEWS = QUERIES / "views"
P = """PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
"""

VIEW_DEFS = {
    "type_closure": (["simple2:*"], P + """INSERT { GRAPH <urn:repronim:abide:graph/view/type_closure> { ?m a nidm:DataElement } }
WHERE { GRAPH ?g2 { ?c rdfs:subClassOf nidm:DataElement } GRAPH ?g1 { ?m a ?c } }"""),
    "volume_measures": (["simple2:*", "view/type_closure"], P + """INSERT { GRAPH <urn:repronim:abide:graph/view/volume_measures> {
    ?m a ex:VolumeMeasure ; ex:tool ?tool ; ex:region ?region ; ex:side ?side ; rdfs:label ?label } }
WHERE {
  GRAPH <urn:repronim:abide:graph/view/type_closure> { ?m a nidm:DataElement }
  GRAPH ?g { ?m nidm:measureOf <http://uri.interlex.org/base/ilx_0112559> ;
                nidm:datumType <http://uri.interlex.org/base/ilx_0738276> ; rdfs:label ?label .
             OPTIONAL { ?m nidm:isAbout ?about } OPTIONAL { ?m nidm:hasLaterality ?lat } }
  BIND (COALESCE(?about, ex:noRegion) AS ?region)
  BIND (COALESCE(?lat, "both") AS ?side)
  BIND (IRI(REPLACE(STR(?m), "^(.*[#/])[^#/]*$", "$1")) AS ?tool)
}"""),
    "volumes": (["simple2:*", "core", "view/volume_measures"], P + """INSERT { GRAPH <urn:repronim:abide:graph/view/volumes> {
    ?obs a ex:VolumeObservation ; ex:participant ?p ; ex:srcSubjectId ?id ; ex:tool ?tool ; ex:measure ?m ;
         ex:region ?region ; ex:side ?side ; ex:volume ?v ; ex:sourceGraph ?g } }
WHERE {
  GRAPH <urn:repronim:abide:graph/view/volume_measures> { ?m ex:region ?region ; ex:side ?side }
  GRAPH ?g { ?ent ?m ?v ; prov:wasGeneratedBy ?act .
             ?act prov:qualifiedAssociation ?a1 , ?a2 .
             ?a1 prov:agent ?sw . ?sw nidm:NIDM_0000164 ?tool .
             ?a2 prov:agent ?subj . ?subj ndar:src_subject_id ?id . }
  GRAPH <urn:repronim:abide:graph/core> { ?p ndar:src_subject_id ?id }
  BIND (IRI(CONCAT("urn:repronim:abide:volume/", ?id, "/", MD5(CONCAT(STR(?m), STR(?ent))))) AS ?obs)
}"""),
    "phenotype_matrix": (["core"], P + """INSERT { GRAPH <urn:repronim:abide:graph/view/phenotype_matrix> { ?p ?de ?v . ?p ex:site ?site } }
WHERE { GRAPH <urn:repronim:abide:graph/core> {
  VALUES ?de { <urn:repronim:abide:variable/AGE_AT_SCAN> <urn:repronim:abide:variable/FIQ> <urn:repronim:abide:variable/VIQ>
               <urn:repronim:abide:variable/PIQ> <urn:repronim:abide:variable/SRS_RAW_TOTAL> <urn:repronim:abide:variable/DX_GROUP>
               <urn:repronim:abide:variable/SEX> <urn:repronim:abide:variable/func_mean_fd> }
  ?rec ex:participant ?p ; ?de ?v . ?p ex:site ?site } }"""),
}


def sources() -> dict[str, str]:
    """Named graph IRI -> source file."""
    s = {
        G + "core": GRAPH / "abide_kg.ttl",
        G + "core_v1": GRAPH / "abide_kg_v1.ttl",
        G + "extension": GRAPH / "abide_extension.ttl",
        G + "embedding": GRAPH / "embedding_provenance.ttl",
        G + "link": GRAPH / "repronim_simple2_link.ttl",
        G + "resources": GRAPH / "resources.ttl",
        G + "resource_activity": GRAPH / "resource_activity.ttl",
        G + "scope": GRAPH / "scope.ttl",
        G + "publications": GRAPH / "publications.ttl",
        G + "publication_links_activity": GRAPH / "publication_links_activity.ttl",
        G + "pynidm_phenotype": DATA / "derived/pynidm/phenotype_pynidm.ttl",
    }
    for f in sorted(glob.glob(str(DATA / "repronim_simple2/datasets.datalad.org/abide/**/nidm.ttl"), recursive=True)) + sorted(glob.glob(str(DATA / "repronim_simple2/cde_tools/*.ttl"))):
        s["urn:repronim:simple2:" + f.split("repronim_simple2/")[1]] = f
    return {k: v for k, v in s.items() if __import__("pathlib").Path(v).exists()}


def build(force: bool = False) -> dict:
    """(Re)build the store if any input changed; return the manifest."""
    src = sources()
    hashes = {g: sha256_file(__import__("pathlib").Path(f)) for g, f in src.items()}
    view_hash = sha256_bytes(json.dumps({k: v[1] for k, v in VIEW_DEFS.items()}, sort_keys=True).encode())
    if not force and MANIFEST.exists() and STORE.exists():
        old = json.loads(MANIFEST.read_text())
        if old.get("input_sha256") == hashes and old.get("view_sha256") == view_hash:
            print("store up to date")
            return old
    shutil.rmtree(STORE, ignore_errors=True)
    t0 = time.time()
    st = ox.Store(str(STORE))
    load = {}
    for g, f in src.items():
        t = time.time()
        st.bulk_load(path=str(f), format=ox.RdfFormat.TURTLE, to_graph=ox.NamedNode(g))
        load[g] = round(time.time() - t, 2)
    VIEWS.mkdir(parents=True, exist_ok=True)
    views = {}
    prov = []
    for name, (inputs, update) in VIEW_DEFS.items():
        (VIEWS / f"{name}.ru").write_text(update)
        t = time.time()
        st.update(update)
        secs = round(time.time() - t, 2)
        gv = ox.NamedNode(G + f"view/{name}")
        n = sum(1 for _ in st.quads_for_pattern(None, None, None, gv))
        views[name] = {"quads": n, "seconds": secs, "inputs": inputs, "update": f"queries/views/{name}.ru"}
        act = f"<urn:repronim:abide:activity/materialize/{name}>"
        used = [g for g in src if any(g.startswith("urn:repronim:simple2:") if i == "simple2:*" else g == G + i for i in inputs)]
        used += [G + i for i in inputs if i.startswith("view/")]
        prov.append(f"{act} a ex:MaterializeView , prov:Activity ; prov:generated <{gv.value}> ; ex:updateQuery \"queries/views/{name}.ru\" ; "
                    f"ex:updateSha256 \"{sha256_bytes(update.encode())}\" ; ex:nQuads {n} ; " + " ; ".join(f"prov:used <{u}>" for u in used) + " .")
        prov.append(f"<{gv.value}> a ex:MaterializedView , prov:Entity ; prov:wasGeneratedBy {act} .")
        for u in used:
            if u in hashes:
                prov.append(f"<{u}> ex:sourceSha256 \"{hashes[u]}\" .")
        print(f"view {name}: {n} quads in {secs}s", flush=True)
    st.update(P + "INSERT DATA { GRAPH <urn:repronim:abide:graph/view_provenance> { " + "\n".join(prov) + " } }")
    st.optimize()
    st.flush()
    dumps = DATA / "derived/views"
    dumps.mkdir(parents=True, exist_ok=True)
    for name in list(VIEW_DEFS) + ["view_provenance"]:
        gname = G + (f"view/{name}" if name != "view_provenance" else name)
        st.dump(output=str(dumps / f"{name}.nt"), format=ox.RdfFormat.N_TRIPLES, from_graph=ox.NamedNode(gname))
    manifest = {"store": str(STORE.relative_to(ROOT)), "input_sha256": hashes, "view_sha256": view_hash, "load_seconds": load,
                "views": views, "quads": len(st), "build_seconds": round(time.time() - t0, 1), "pyoxigraph": ox.__version__}
    MANIFEST.write_text(json.dumps(manifest, indent=1))
    write_json("store_manifest.json", {k: v for k, v in manifest.items() if k != "input_sha256"} | {"n_named_graphs": len(src) + len(VIEW_DEFS) + 1})
    print(f"store: {manifest['quads']} quads, {len(src)} source graphs, built in {manifest['build_seconds']}s")
    del st
    return manifest


def open_store(read_only: bool = True) -> ox.Store:
    """Open the built store (read-only by default)."""
    return ox.Store.read_only(str(STORE)) if read_only else ox.Store(str(STORE))


if __name__ == "__main__":
    build(force="--force" in sys.argv)
