from pathlib import Path
import json,time
from rdflib import Graph,Namespace,RDF
from pyshacl import validate
R=Path(__file__).resolve().parent;start=time.time();target=R/'results/combined_graph.ttl';g=Graph().parse(target);sh=Graph().parse(R/'shapes.ttl')
ok,report,txt=validate(g,shacl_graph=sh,inference='none',inplace=True)
(R/'results/shacl_report.txt').write_text(txt);report.serialize(destination=R/'results/shacl_report.ttl',format='turtle')
# Mutation check: missing source must fail on the exact shape that should reject it.
E=Namespace('urn:repronim:cnp:expanded:');P=Namespace('http://www.w3.org/ns/prov#');N=Namespace('http://purl.org/nidash/nidm#');obj=E['derived/parcel1/sub-10159'];src=list(g.objects(obj,P.wasDerivedFrom));g.remove((obj,P.wasDerivedFrom,None));bad,_,badtext=validate(g,shacl_graph=sh,focus_nodes=[str(obj)],inference='none',inplace=True)
(R/'results/shacl_mutation_report.txt').write_text(badtext);json.dump({'conforms':ok,'mutation_missing_source_rejected':not bad,'shapes':'local explicit profile; not certification against every NIDM rule','seconds':round(time.time()-start,1)},(R/'results/shacl_summary.json').open('w'),indent=2);print(ok,not bad)
