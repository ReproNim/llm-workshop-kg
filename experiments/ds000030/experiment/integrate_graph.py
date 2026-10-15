from pathlib import Path
import json,hashlib
from rdflib import Graph,Namespace,Literal,RDF,URIRef
R=Path(__file__).resolve().parent;O=R/'results';g=Graph();E=Namespace('urn:repronim:cnp:expanded:');P=Namespace('http://www.w3.org/ns/prov#');N=Namespace('http://purl.org/nidash/nidm#');OLD=Namespace('urn:repronim:cnp:');g.bind('ex',E);g.bind('nidm',N);g.bind('prov',P)
d=json.load((O/'embedding_input.json').open());runs=json.load((O/'umap_runs.json').open())
matrix=E.phenotypeMatrix;g.add((matrix,RDF.type,P.Entity));g.add((matrix,E.sha256,Literal(hashlib.sha256((O/'embedding_input.json').read_bytes()).hexdigest())));g.add((matrix,E.featureManifest,Literal(json.dumps(d['features']))));g.add((matrix,E.preparation,Literal(json.dumps(d['config']))));g.add((matrix,P.wasGeneratedBy,E.matrixPreparation));g.add((E.matrixPreparation,RDF.type,P.Activity));g.add((E.matrixPreparation,E.querySha256,Literal(hashlib.sha256((O/'matrix_query.sparql').read_bytes()).hexdigest())))
for p in d['participants']:
 for table in sorted({f.split('/')[0] for f in d['features']}):g.add((matrix,P.wasDerivedFrom,E['record/'+table+'/'+p['participant_id']]))
for r in runs:
 a=E[f'umap/seed{r["seed"]}/neighbors{r["nNeighbors"]}'];g.add((a,RDF.type,N.Derivative));g.add((a,RDF.type,P.Activity));g.add((a,P.used,matrix));g.add((a,P.wasAssociatedWith,E.umapJS));g.add((a,E.config,Literal(json.dumps({k:v for k,v in r.items() if k!='embedding'}))))
 for person,coords in zip(d['participants'],r['embedding']):
  o=URIRef(str(a)+'/'+person['participant_id']);g.add((o,RDF.type,N.DerivativeObject));g.add((o,RDF.type,P.Entity));g.add((o,P.wasGeneratedBy,a));g.add((o,P.wasDerivedFrom,matrix));g.add((o,E.participant,E[person['participant_id']]));g.add((o,E.umap1,Literal(coords[0])));g.add((o,E.umap2,Literal(coords[1])))
g.add((E.umapJS,RDF.type,P.SoftwareAgent));g.add((E.umapJS,E.commit,Literal('14abb51c523f71456550a7c6ef3f7062127b6bad')));g.add((E.umapJS,E.bundleSha256,Literal(hashlib.sha256((R/'vendor/umap-js.cjs').read_bytes()).hexdigest())))
old=json.load((R.parent/'output/cnp_graph/knowledge_graph.json').open())
for n in old['nodes']:
 if n['type']=='ex:ImageFileRecord':g.add((OLD[n['id'][3:]],E.describesArtifact,E['image/'+n['label']]))
g.serialize(destination=O/'embedding_provenance.ttl',format='turtle')
for f in [R.parent/'output/cnp_graph/knowledge_graph.ttl',O/'nidm_phenotypes.ttl',O/'claims_and_questions.ttl']:g.parse(f)
g.serialize(destination=O/'combined_graph.ttl',format='turtle');json.dump({'triples':len(g),'components':['original graph','NIDM phenotype and image inventory','claims/questions bridge','embedding provenance'],'qualification':'complete pinned phenotype-table representation; partial image and historical execution provenance'},(O/'combined_summary.json').open('w'),indent=2);print(len(g))
