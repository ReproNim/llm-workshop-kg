"""Explicitly illustrative collaboration records; no real person contributions inferred."""
from pathlib import Path
import json
from rdflib import Graph,Namespace,Literal,RDF,RDFS,URIRef
from pyshacl import validate
R=Path(__file__).resolve().parent;E=Namespace('urn:repronim:illustrative:');P=Namespace('http://www.w3.org/ns/prov#');C=Namespace('urn:repronim:cnp:expanded:');OLD=Namespace('urn:repronim:cnp:');g=Graph()
for k,v in [('ex',E),('prov',P),('cnp',C),('old',OLD)]:g.bind(k,v)
def n(id,type,label):
 u=E[id];g.add((u,RDF.type,type));g.add((u,RDFS.label,Literal(label)));g.add((u,E.scenarioStatus,Literal('illustrative; not a historical attribution')));return u
a=n('analystA',P.Person,'Hypothetical analyst A');b=n('analystB',P.Person,'Hypothetical analyst B');r=n('reviewerC',P.Person,'Hypothetical reviewer C')
for id,agent,question,source,role in [('analysisA',a,C.Q1,C.C1,E.Analyst),('analysisB',b,C.Q3,OLD.p2,E.Analyst),('reviewC',r,C.Q1,OLD.p2,E.Reviewer)]:
 act=n(id,P.Activity,id);g.add((act,E.addresses,question));g.add((act,P.used,source));ass=n(id+'association',P.Association,id+' role');g.add((act,P.qualifiedAssociation,ass));g.add((ass,P.agent,agent));g.add((ass,P.hadRole,role))
assessment=n('comparability',E.EvidenceAssessment,'Cross-paper processing comparability remains unresolved');g.add((assessment,RDF.type,P.Entity));g.add((assessment,P.wasGeneratedBy,E.reviewC));g.add((assessment,P.wasAttributedTo,r));g.add((assessment,E.target,C.C1));g.add((assessment,E.relatedQuestion,C.Q3));g.add((assessment,P.wasDerivedFrom,OLD.p2));g.add((assessment,P.wasDerivedFrom,OLD.p3));g.add((assessment,E.verdict,Literal('requires_source_manifest')));g.add((assessment,E.relationStatus,Literal('candidate relevance; not established support or contradiction')))
g.serialize(destination=R/'results/collaborative_example.ttl',format='turtle')
sh='''@prefix sh:<http://www.w3.org/ns/shacl#>. @prefix ex:<urn:repronim:illustrative:>. @prefix prov:<http://www.w3.org/ns/prov#>. ex:ReviewShape a sh:NodeShape;sh:targetClass ex:EvidenceAssessment;sh:property [sh:path prov:wasAttributedTo;sh:minCount 1;sh:class prov:Person];sh:property [sh:path prov:wasGeneratedBy;sh:minCount 1;sh:class prov:Activity];sh:property [sh:path ex:target;sh:minCount 1];sh:property [sh:path prov:wasDerivedFrom;sh:minCount 1];sh:property [sh:path ex:verdict;sh:minCount 1].'''
(R/'results/collaboration_shapes.ttl').write_text(sh);sg=Graph().parse(data=sh,format='turtle');ok,_,text=validate(g,shacl_graph=sg)
q='''PREFIX ex:<urn:repronim:illustrative:> PREFIX prov:<http://www.w3.org/ns/prov#> SELECT ?person ?role ?question ?input WHERE { ?activity ex:addresses ?question; prov:used ?input; prov:qualifiedAssociation ?association. ?association prov:agent ?person; prov:hadRole ?role. }'''
rows=[{str(k):str(v) for k,v in row.asdict().items()} for row in g.query(q)];g.remove((assessment,P.wasAttributedTo,None));bad,_,_=validate(g,shacl_graph=sg)
json.dump({'status':'Illustrative collaboration model, separate from factual dataset graph','conforms':ok,'missing_reviewer_rejected':not bad,'query':q,'results':rows},(R/'results/collaboration_query.json').open('w'),indent=2);print(ok,not bad,len(rows))
