PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX nidm: <http://purl.org/nidash/nidm#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ndar: <https://ndar.nih.gov/api/datadictionary/v2/dataelement/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
INSERT { GRAPH <urn:repronim:abide:graph/view/phenotype_matrix> { ?p ?de ?v . ?p ex:site ?site } }
WHERE { GRAPH <urn:repronim:abide:graph/core> {
  VALUES ?de { <urn:repronim:abide:variable/AGE_AT_SCAN> <urn:repronim:abide:variable/FIQ> <urn:repronim:abide:variable/VIQ>
               <urn:repronim:abide:variable/PIQ> <urn:repronim:abide:variable/SRS_RAW_TOTAL> <urn:repronim:abide:variable/DX_GROUP>
               <urn:repronim:abide:variable/SEX> <urn:repronim:abide:variable/func_mean_fd> }
  ?rec ex:participant ?p ; ?de ?v . ?p ex:site ?site } }