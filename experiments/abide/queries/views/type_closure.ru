PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
INSERT { GRAPH <urn:repronim:abide:graph/view/type_closure> { ?m a nidm:DataElement } }
WHERE { GRAPH ?g2 { ?c rdfs:subClassOf nidm:DataElement } GRAPH ?g1 { ?m a ?c } }