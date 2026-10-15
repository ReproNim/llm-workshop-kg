"""Pinned ds000030 phenotype graph; no inferred historical execution."""
from pathlib import Path
import csv,json,hashlib,collections,math
from rdflib import Graph,Namespace,URIRef,Literal,RDF,RDFS,XSD
ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
N=Namespace('http://purl.org/nidash/nidm#');P=Namespace('http://www.w3.org/ns/prov#');D=Namespace('http://purl.org/dc/terms/');E=Namespace('urn:repronim:cnp:expanded:');OLD=Namespace('urn:repronim:cnp:');SIO=Namespace('http://semanticscience.org/ontology/sio.owl#')
g=Graph()
for prefix,ns in [('nidm',N),('prov',P),('dct',D),('ex',E),('old',OLD),('sio',SIO)]:g.bind(prefix,ns)
def add(s,p,o):g.add((s,p,o))
def node(u,t,label=None):
 add(u,RDF.type,t)
 if label:add(u,RDFS.label,Literal(label))
 return u
def source(path):
 u=E['source/'+path.name];node(u,P.Entity,path.name);add(u,E.sha256,Literal(hashlib.sha256(path.read_bytes()).hexdigest()));add(u,P.atLocation,URIRef(BASE+'phenotype/'+path.name));return u
BASE='https://raw.githubusercontent.com/OpenNeuroDatasets/ds000030/4070b6eea231517bfeff42527a46d9d166ac4e13/'
project=node(E.project,N.Project,'CNP pinned metadata reconstruction');add(project,RDF.type,P.Activity);add(project,E.scope,Literal('Pinned Git metadata. Reconstructed activities have no recorded execution times.'))
run=node(E.parse,P.Activity,'Deterministic metadata-to-NIDM conversion');add(run,P.wasAssociatedWith,node(E.parser,P.SoftwareAgent,'build_nidm.py'));add(run,E.codeSha256,Literal(hashlib.sha256(Path(__file__).read_bytes()).hexdigest()))
participants=list(csv.DictReader((ROOT.parent/'research/participants.txt').open(),delimiter='\t')); pids={r['participant_id'] for r in participants}
for r in participants:
 pid=r['participant_id'];u=node(E[pid],P.Person,pid);add(u,RDF.type,P.Agent);add(u,E.diagnosis,Literal(r['diagnosis']));add(u,E.age,Literal(int(r['age'])));add(u,E.gender,Literal(r['gender']));add(u,E.scanner,Literal(r['ScannerSerialNumber']));add(u,E.ghost,Literal(r['ghost_NoGhost']));ses=node(E['session/'+pid],N.Session);add(ses,RDF.type,P.Activity);add(ses,D.isPartOf,project);add(ses,E.status,Literal('reconstructed_visit_container; no date inferred'))
def acquisition(pid,key):
 a=node(E['acquisition/'+pid+'/'+key],N.Acquisition);add(a,RDF.type,P.Activity);add(a,D.isPartOf,E['session/'+pid]);ass=node(E['association/'+pid+'/'+key],P.Association);add(a,P.qualifiedAssociation,ass);add(ass,P.agent,E[pid]);add(ass,P.hadRole,SIO.Subject);add(a,E.status,Literal('reconstructed_from_metadata'));return a
stats={'tables':0,'dictionary_variables':0,'table_variables':0,'rows':0,'observed_cells':0,'missing_cells':0,'missing_dictionary_columns':[],'unknown_participants':[],'duplicate_ids':[]}; matrix={pid:{} for pid in pids};catalog=[]
for path in sorted((ROOT/'data/phenotype').glob('*.tsv')):
 rows=list(csv.DictReader(path.open(),delimiter='\t'));d=json.load(path.with_suffix('.json').open());src=source(path);ds=source(path.with_suffix('.json'));stats['tables']+=1;stats['dictionary_variables']+=sum(k!='MeasurementToolMetadata' for k in d)
 cols=[c for c in rows[0] if c!='participant_id'];stats['table_variables']+=len(cols);seen=set()
 for col in cols:
  de=node(E['variable/'+path.stem+'/'+col],N.DataElement,col);add(de,RDF.type,P.Entity);add(de,N.sourceVariable,Literal(col));add(de,P.wasDerivedFrom,ds);info=d.get(col,{})
  if col not in d:stats['missing_dictionary_columns'].append(path.stem+'/'+col)
  if isinstance(info,dict):
   for k,v in info.items():add(de,E['dictionary_'+k],Literal(json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v))
   if info.get('Description'):add(de,D.description,Literal(info['Description']))
   if info.get('Units'):add(de,N.hasUnit,Literal(info['Units']))
  catalog.append({'table':path.stem,'variable':col,'uri':str(de),'metadata':info})
 for rownum,row in enumerate(rows,2):
  pid=row['participant_id'];stats['rows']+=1
  if pid in seen:stats['duplicate_ids'].append(path.stem+'/'+pid)
  seen.add(pid)
  if pid not in pids:stats['unknown_participants'].append(pid);continue
  a=acquisition(pid,path.stem);o=node(E['record/'+path.stem+'/'+pid],N.AcquisitionObject);add(o,RDF.type,P.Entity);add(o,P.wasGeneratedBy,a);add(o,P.wasDerivedFrom,src);add(o,E.sourceRow,Literal(rownum));add(o,E.participant,E[pid]);add(o,E.table,Literal(path.stem));add(o,E.importedBy,run)
  for col,val in row.items():
   if col=='participant_id':continue
   de=E['variable/'+path.stem+'/'+col]
   if val is None or val.strip().lower() in ('','n/a','na','nan'):
    stats['missing_cells']+=1;add(o,E.missingVariable,de);continue
   stats['observed_cells']+=1;add(o,de,Literal(val));matrix[pid][path.stem+'/'+col]=val
tree=json.load((ROOT.parent/'research/tree.txt').open())['tree'];scans=0
for ent in tree:
 path=ent['path']
 if not path.endswith('.nii.gz') or not path.startswith('sub-'):continue
 pid=path.split('/')[0];a=acquisition(pid,path);o=node(E['image/'+path],N.AcquisitionObject,path);add(o,RDF.type,P.Entity);add(o,P.wasGeneratedBy,a);add(o,E.participant,E[pid]);add(o,P.atLocation,URIRef(BASE+path));add(o,E.gitPointerBlob,Literal(ent['sha']));add(o,E.contentRetrieved,Literal(False));add(o,N.hadAcquisitionModality,N.MagneticResonanceImaging);add(o,E.importedBy,run);scans+=1
stats['image_inventory']=scans
# Auditable behavioral derivative: source dictionary explicitly specifies a mean.
checks=[]
for pid in sorted(pids):
 vals=matrix[pid];keys=['barratt/barratt19','barratt/barratt17','barratt/bis_parcel1']
 if all(k in vals for k in keys):
  x,y,z=map(lambda k:float(vals[k]),keys);result=(x+y)/2;ok=abs(result-z)<1e-6;checks.append({'participant_id':pid,'reported':z,'recomputed':result,'matches':ok})
  a=node(E['recompute/parcel1/'+pid],N.Derivative);add(a,RDF.type,P.Activity);add(a,P.used,E['record/barratt/'+pid]);add(a,D.isPartOf,project);add(a,E.formula,Literal('(barratt19 + barratt17) / 2'));add(a,P.wasAssociatedWith,E.parser)
  o=node(E['derived/parcel1/'+pid],N.DerivativeObject);add(o,RDF.type,P.Entity);add(o,P.wasGeneratedBy,a);add(o,P.wasDerivedFrom,E['record/barratt/'+pid]);add(o,E.participant,E[pid]);add(o,E['variable/barratt/bis_parcel1'],Literal(result));add(o,E.agreesWithReportedValue,Literal(ok))
stats['parcel1_check']={'n':len(checks),'matches':sum(c['matches'] for c in checks)};stats['triples']=len(g)
g.serialize(destination=OUT/'nidm_phenotypes.ttl',format='turtle');json.dump(stats,(OUT/'coverage.json').open('w'),indent=2);json.dump(catalog,(OUT/'variable_catalog.json').open('w'),indent=2);json.dump(checks,(OUT/'derivative_validation.json').open('w'),indent=2)
# Feature choice fixed by instrument and named score, before viewing embeddings.
features=['barratt/bis_2attimp','barratt/bis_2motimp','barratt/bis_2npimp','wais/voc_totalraw','wais/lns_totalraw','wais/mr_totalraw','stopsignal/sst_ses_ssrt_quant','ant/ant_conflict_rt_effect','cpt/cpt_hits','cpt/cpt_fa']
# Read projected values from RDF through SPARQL, rather than from matrix cache.
q='SELECT ?pid ?variable ?value WHERE { VALUES ?variable { '+ ' '.join('<'+str(E['variable/'+f])+'>' for f in features) +' } ?r ?variable ?value ; ex:participant ?pid . }'
projected={pid:{} for pid in pids}
for pid,var,value in g.query(q):
 key=str(var).split('/variable/')[-1] if '/variable/' in str(var) else str(var).split('variable/')[-1];projected[str(pid).split(':')[-1]][key]=str(value)
out={'participants':participants,'features':features,'values':[[projected[r['participant_id']].get(f) for f in features] for r in participants]};json.dump(out,(OUT/'matrix_from_graph.json').open('w'));(OUT/'matrix_query.sparql').write_text('PREFIX nidm: <'+str(N)+'>\nPREFIX ex: <'+str(E)+'>\n'+q)
print(json.dumps(stats,indent=2))
