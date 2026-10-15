"""Profile ReproNim's simple2 query by timing its blocks separately (pyoxigraph has no EXPLAIN).

Each block of simple2_query.sparql is run alone over all 24 site graphs + CDEs, with the row count, so
the cost of the measure-typing path, the tool-activity pattern and the six demographic joins can be
compared with the full query.

Writes results/simple2_profile.json.

Usage: uv run python code/profile_simple2.py
"""

import json
import time

from common import write_json
from store import open_store

P = """prefix prov: <http://www.w3.org/ns/prov#>
prefix ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
prefix nidm: <http://purl.org/nidash/nidm#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix ilx: <http://uri.interlex.org/>
prefix ncit: <http://ncitt.ncit.nih.gov/>
"""
BLOCKS = {
    "measure_typing_path (a/rdfs:subClassOf)": P + """SELECT (COUNT(*) AS ?n) WHERE { ?measure a/rdfs:subClassOf nidm:DataElement ; rdfs:label ?l ;
        nidm:measureOf <http://uri.interlex.org/base/ilx_0112559> ; nidm:datumType <http://uri.interlex.org/base/ilx_0738276> . }""",
    "measure_typing_view (materialized)": P + """SELECT (COUNT(*) AS ?n) WHERE { GRAPH <urn:repronim:abide:graph/view/type_closure> { ?measure a nidm:DataElement }
        ?measure rdfs:label ?l ; nidm:measureOf <http://uri.interlex.org/base/ilx_0112559> ; nidm:datumType <http://uri.interlex.org/base/ilx_0738276> . }""",
    "tool_activity_with_bnode_paths": P + """SELECT (COUNT(*) AS ?n) WHERE { ?tool_act a prov:Activity ;
        prov:qualifiedAssociation [prov:agent [nidm:NIDM_0000164 ?tool]] ; prov:qualifiedAssociation [prov:agent [ndar:src_subject_id ?ID]] . }""",
    "tool_entity_values": P + """SELECT (COUNT(*) AS ?n) WHERE { ?tool_entity a prov:Entity ; prov:wasGeneratedBy ?tool_act ; ?measure ?volume .
        ?tool_act prov:qualifiedAssociation [prov:agent [nidm:NIDM_0000164 ?tool]] . }""",
    "six_disconnected_demographic_blocks": P + """SELECT (COUNT(*) AS ?n) WHERE {
        {?a a nidm:PersonalDataElement ; nidm:isAbout ilx:ilx_0100400 .} {?s a nidm:PersonalDataElement ; nidm:isAbout <http://uri.interlex.org/base/ilx_0101292> .}
        {?d a nidm:PersonalDataElement ; nidm:isAbout ncit:Diagnosis .} {?f a nidm:PersonalDataElement ; nidm:isAbout <http://uri.interlex.org/base/ilx_0739365> .}
        {?p a nidm:PersonalDataElement ; nidm:isAbout <http://uri.interlex.org/base/ilx_0739363> .} {?v a nidm:PersonalDataElement ; nidm:isAbout <http://uri.interlex.org/base/ilx_0739359> .} }""",
    "demographic_entity_join": P + """SELECT (COUNT(*) AS ?n) WHERE {
        ?a a nidm:PersonalDataElement ; nidm:isAbout ilx:ilx_0100400 . ?f a nidm:PersonalDataElement ; nidm:isAbout <http://uri.interlex.org/base/ilx_0739365> .
        ?e ?a ?age ; ?f ?fiq ; prov:wasGeneratedBy ?act . ?act prov:qualifiedAssociation [prov:agent [ndar:src_subject_id ?ID]] . }""",
}


def main() -> None:
    """Time each block on the union of the simple2 graphs."""
    st = open_store()
    graphs = [g for g in st.named_graphs() if g.value.startswith("urn:repronim:simple2:")]
    out = {}
    for name, q in BLOCKS.items():
        kw = {"default_graph": graphs}
        if "view" in name:
            kw["named_graphs"] = [g for g in st.named_graphs() if g.value.endswith("view/type_closure")]
        t0 = time.time()
        n = int(next(iter(st.query(q, **kw)))[0].value)
        out[name] = {"rows": n, "seconds": round(time.time() - t0, 3)}
        print(name, out[name], flush=True)
    write_json("simple2_profile.json", {"engine": "pyoxigraph, on-disk store, 24 site graphs + 3 CDEs", "blocks": out,
                                        "note": "Blocks timed on Oxigraph only."})


if __name__ == "__main__":
    main()
