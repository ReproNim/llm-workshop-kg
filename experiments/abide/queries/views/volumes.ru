PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
INSERT { GRAPH <urn:repronim:abide:graph/view/volumes> {
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
}