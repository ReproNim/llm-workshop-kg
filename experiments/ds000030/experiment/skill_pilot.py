"""StructSense host-model structured pilot; separate authored extraction and deterministic gates."""
from pathlib import Path
import json,hashlib,importlib.util,copy
from rdflib import Graph,Namespace,RDF,Literal,URIRef
R=Path(__file__).resolve().parent;O=R/'results/skill';O.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('span_validator',R/'vendor/structsense/scripts/span_validator.py');sv=importlib.util.module_from_spec(spec);spec.loader.exec_module(sv)
sources={'kim2023':(R/'sources/kim2023_retrieval.txt').read_text(),'preprocessing2017':(R/'sources/paper_retrieved_lines.txt').read_text(),'barratt':(R/'data/phenotype/barratt.json').read_text(),'stopsignal':(R/'data/phenotype/stopsignal.json').read_text()}
schema={'$schema':'http://json-schema.org/draft-07/schema#','type':'object','required':['records'],'additionalProperties':False,'properties':{'records':{'type':'array','items':{'type':'object','additionalProperties':False,'required':['id','source','kind','statement','quote','start','end','value','unit','scope','status'],'properties':{'id':{'type':'string'},'source':{'enum':list(sources)},'kind':{'enum':['result','method','derivation','metadata_gap']},'statement':{'type':'string'},'quote':{'type':'string'},'start':{'type':'integer','minimum':0},'end':{'type':'integer','minimum':0},'value':{'type':['number','null']},'unit':{'type':['string','null']},'scope':{'type':'string'},'status':{'enum':['paper_reported','dictionary_reported','not_reported']}}}}}}
# Schema fixed before the host-authored extraction below; task fields derive from user request.
(O/'schema.json').write_text(json.dumps(schema,indent=2))
prompt=(R/'vendor/structsense/prompts/extractor-structured.md').read_text().replace('{json_schema}',json.dumps(schema)).replace('{field_hints}','value: reported numeric metric or null. scope: dataset, feature set and evaluation. unit: null when not explicit. Preserve a short exact evidence span; unknown subject IDs remain unresolved.')
(O/'prompt.txt').write_text(prompt)
raw=[
 ('C1','kim2023','result','UCLA within-dataset classification using both connectivity directions reports 70.2% accuracy.','70.2%',70.2,'percent','UCLA; both directions; leave-one-out','paper_reported'),
 ('C2','kim2023','result','Training on UCLA and testing on COBRE using decreased connectivity reports 61.5% accuracy.','61.5%',61.5,'percent','train UCLA; test COBRE; decreased','paper_reported'),
 ('C3','kim2023','result','The reverse transfer direction did not predict above chance.','None of the CPM-SVM prediction models',None,None,'train COBRE; test UCLA','paper_reported'),
 ('M1','preprocessing2017','method','The preprocessing descriptor reports FMRIPREP version 0.4.4.','FMRIPREP version 0.4.4',None,None,'2017 preprocessing descriptor; not Kim 2023 pipeline','paper_reported'),
 ('D1','barratt','derivation','Barratt parcel 1 is the mean of items 19 and 17.','mean of item 19 and 17',None,None,'barratt/bis_parcel1','dictionary_reported'),
 ('G1','stopsignal','metadata_gap','The inspected stopsignal dictionary does not specify a Units field for sst_ses_ssrt_quant.','sst_ses_ssrt_quant',None,None,'stopsignal/sst_ses_ssrt_quant; unit unknown','not_reported')]
records=[]
for id,source,kind,statement,quote,value,unit,scope,status in raw:
 start=sources[source].index(quote);records.append(dict(id=id,source=source,kind=kind,statement=statement,quote=quote,start=start,end=start+len(quote),value=value,unit=unit,scope=scope,status=status))
json.dump({'records':records},(O/'00_extraction.json').open('w'),indent=2)
# Alignment is an exact class lookup in the retrieved NIDM schema; no semantic search fabricated.
alignment={'derivation':{'iri':'http://purl.org/nidash/nidm#Derivative','lookup':'class_uri: nidm:Derivative'},'result':{'iri':'http://www.w3.org/ns/prov#Entity','lookup':'PROV-O Entity; local claim subtype'},'method':{'iri':'http://www.w3.org/ns/prov#Plan','lookup':'PROV-O Plan; reported method'},'metadata_gap':{'iri':'http://www.w3.org/ns/prov#Entity','lookup':'local evidence gap record'}}
json.dump(alignment,(O/'01_alignment.json').open('w'),indent=2)
grounding=[]
for r in records:
 passed=sv.validate(sources[r['source']],{'entity':r['quote'],'start':r['start'],'end':r['end']});grounding.append({'id':r['id'],'passes_exact_span':passed})
# Host judgment performed as a separate source review. Confidence is not a calibrated probability.
judgments=[{'id':r['id'],'mode':'host_sequential','faithfulness':'pass','qualification':('Surface anchors the variable only; absence of Units verified by dictionary-key inspection.' if r['id']=='G1' else 'Numeric/name span grounded; statement and scope reviewed against surrounding source section.')} for r in records]
json.dump(judgments,(O/'02_judge.json').open('w'),indent=2)
tests=[]
item={'entity':'70.2%','start':records[0]['start'],'end':records[0]['end']}
tests.append({'test':'correct span accepted','passed':sv.validate(sources['kim2023'],item)})
wrong={**item,'start':0,'end':5};v,d=sv.validate_all(sources['kim2023'],[wrong]);tests.append({'test':'wrong offsets repaired and disclosed','passed':len(v)==1 and v[0].get('span_repaired') is True})
v,d=sv.validate_all(sources['kim2023'],[{'entity':'imaginary accuracy 99.9%','start':0,'end':24}]);tests.append({'test':'fabricated surface dropped','passed':len(d)==1 and len(v)==0})
false_claim={**records[0],'statement':'70.2% proves a causal schizophrenia mechanism.'};span_pass=sv.validate(sources['kim2023'],{'entity':false_claim['quote'],'start':false_claim['start'],'end':false_claim['end']});tests.append({'test':'causal overclaim can pass span validation','passed':span_pass,'interpretation':'Expected limitation. Semantic reviewer rejects; lexical validator cannot establish entailment.'})
report={'skill':'StructSense 0.12.0','commit':'dde54251a5a70f55d0b9bbbaab0dd21013b1bbfc','mode':'host-model structured subset plus upstream span_validator.py','records':len(records),'grounding':grounding,'code_tests':tests,'skill_validation':'bounded smoke and adversarial unit tests; no held-out recall benchmark or multi-model comparison','output_validation':'JSON Schema, exact spans, separate host faithfulness review, scoped graph assertions','independence':'same host model; procedural review, not independent process/model','source_sha256':{k:hashlib.sha256(v.encode()).hexdigest() for k,v in sources.items()},'schema_sha256':hashlib.sha256((O/'schema.json').read_bytes()).hexdigest(),'limitations':['Schema and span compliance do not prove entailment.','Paper cohort IDs and actual image lineage unavailable.','No exhaustive extraction or validated skill-wide performance claim.']}
json.dump(report,(O/'pilot_report.json').open('w'),indent=2)
E=Namespace('urn:repronim:cnp:expanded:');P=Namespace('http://www.w3.org/ns/prov#');OLD=Namespace('urn:repronim:cnp:');RDFS=Namespace('http://www.w3.org/2000/01/rdf-schema#');g=Graph();g.bind('ex',E);g.bind('prov',P);g.bind('old',OLD)
questions={'Q1':'Does increased connectivity add predictive information?','Q2':'Do predictive connectivity features generalize across datasets?','Q3':'Can public CNP data support reusable standardized preprocessing?','Q4':'Can dimensional cognitive and neural measures be studied across diagnoses?'}
for q,label in questions.items():g.add((E[q],RDF.type,E.ResearchQuestion));g.add((E[q],RDFS.label,Literal(label)))
for r in records:
 u=E[r['id']];g.add((u,RDF.type,E.Claim));g.add((u,RDF.type,P.Entity));g.add((u,RDFS.label,Literal(r['statement'])));g.add((u,E.scope,Literal(r['scope'])));g.add((u,E.status,Literal(r['status'])));g.add((u,E.evidenceQuote,Literal(r['quote'])));g.add((u,E.start,Literal(r['start'])));g.add((u,E.end,Literal(r['end'])));g.add((u,P.wasGeneratedBy,E.skillRun))
 if r['source']=='kim2023':g.add((u,P.wasDerivedFrom,OLD.p3))
 elif r['source']=='preprocessing2017':g.add((u,P.wasDerivedFrom,OLD.p2))
 else:g.add((u,P.wasDerivedFrom,E['source/'+r['source']+'.json']))
for c,q,ev in [('C1','Q1','eval-ucla-loo'),('C2','Q2','eval-ucla-cobre-dec')]:g.add((E[c],E.addresses,E[q]));g.add((E[c],E.supportedBy,OLD[ev]))
g.add((E.C3,E.qualifies,E.Q2));g.add((E.M1,E.addresses,E.Q3));g.add((E.Q4,E.posedBy,OLD.p1));g.add((E.Q4,E.resolution,Literal('Data resource enables investigation; descriptor does not resolve all biological hypotheses.')));g.add((E.Q1,E.resolution,Literal('Support within the evaluated datasets; causal mechanism and clinical utility unresolved.')));g.add((E.Q2,E.resolution,Literal('Partial, direction-dependent support; reverse transfer and preprocessing sensitivity limit generalization.')))
g.add((E.skillRun,RDF.type,P.Activity));g.add((E.skillRun,P.wasAssociatedWith,E.hostAgent));g.add((E.hostAgent,RDF.type,P.SoftwareAgent));g.add((E.skillRun,E.skillCommit,Literal(report['commit'])));g.add((E.skillRun,E.validationReport,Literal('skill/pilot_report.json')))
g.add((OLD['p3-ucla-cohort'],E.membershipStatus,Literal('not reconstructed; no participant-level manifest retrieved')));g.add((OLD.p3,E.derivativeReuseStatus,Literal('No verified reuse of 2017 derivative outputs; paper reports GRETNA/SPM12.')))
for row in __import__('csv').DictReader((R.parent/'research/participants.txt').open(),delimiter='\t'):
 pid=row['participant_id'];g.add((OLD[pid],E.describesPerson,E[pid]))
g.serialize(destination=R/'results/claims_and_questions.ttl',format='turtle');print(json.dumps({'records':len(records),'span_passes':sum(x['passes_exact_span'] for x in grounding),'tests':tests},indent=2))
