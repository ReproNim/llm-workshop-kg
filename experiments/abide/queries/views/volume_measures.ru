PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
INSERT { GRAPH <urn:repronim:abide:graph/view/volume_measures> {
    ?m a ex:VolumeMeasure ; ex:tool ?tool ; ex:region ?region ; ex:side ?side ; rdfs:label ?label } }
WHERE {
  GRAPH <urn:repronim:abide:graph/view/type_closure> { ?m a nidm:DataElement }
  GRAPH ?g { ?m nidm:measureOf <http://uri.interlex.org/base/ilx_0112559> ;
                nidm:datumType <http://uri.interlex.org/base/ilx_0738276> ; rdfs:label ?label .
             OPTIONAL { ?m nidm:isAbout ?about } OPTIONAL { ?m nidm:hasLaterality ?lat } }
  BIND (COALESCE(?about, ex:noRegion) AS ?region)
  BIND (COALESCE(?lat, "both") AS ?side)
  BIND (IRI(REPLACE(STR(?m), "^(.*[#/])[^#/]*$", "$1")) AS ?tool)
}