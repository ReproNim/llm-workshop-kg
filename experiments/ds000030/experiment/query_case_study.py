"""Executable graph competency queries, not an LLM benchmark."""
from pathlib import Path
import json,time
from rdflib import Graph
R=Path(__file__).resolve().parent;g=Graph().parse(R/'results/nidm_phenotypes.ttl');g.parse(R/'results/claims_and_questions.ttl')
prefix='PREFIX ex: <urn:repronim:cnp:expanded:> PREFIX nidm: <http://purl.org/nidash/nidm#> PREFIX prov: <http://www.w3.org/ns/prov#> '
queries={
 'participants':'SELECT (COUNT(?p) AS ?n) WHERE { ?p a prov:Person }',
 'barratt_source_lineage':'SELECT ?output ?source ?activity WHERE { VALUES ?output { <urn:repronim:cnp:expanded:derived/parcel1/sub-10159> } ?output prov:wasGeneratedBy ?activity; prov:wasDerivedFrom ?source . ?activity prov:used ?source }',
 'claims_addressing_transfer':'SELECT ?claim ?scope WHERE { ?claim ex:addresses ex:Q2; ex:scope ?scope }',
 'counterevidence_on_transfer':'SELECT ?claim WHERE { ?claim ex:qualifies ex:Q2 }',
 'phenotype_columns':'SELECT (COUNT(?v) AS ?n) WHERE { ?v a nidm:DataElement }'}
out={}
for k,q in queries.items():
 t=time.perf_counter();res=g.query(prefix+q);out[k]={'query':prefix+q,'rows':[{str(var):str(v) for var,v in row.asdict().items()} for row in res],'seconds':round(time.perf_counter()-t,4)}
json.dump({'scope':'Actual SPARQL execution. No LLM-only comparison performed.','queries':out},(R/'results/competency_queries.json').open('w'),indent=2);print(json.dumps(out,indent=2))
