# CNP package rebuild vs original

Checks: 24 matched, 5 differed, 0 could not run.
Byte-identical result files: 22 / 32.

| Check | Slide | Original | Rebuilt | Status |
|---|---|---|---|---|
| participants (SPARQL count) | 272 | 272 | 272 | matched |
| phenotype tables | 52 | 52 | 52 | matched |
| table columns | 1983 | 1983 | 1983 | matched |
| observed cells | 411584 | 411584 | 411584 | matched |
| missing cells | 127792 | 127792 | 127792 | matched |
| image inventory pointers | 2531 | 2531 | 2531 | matched |
| NIDM triples | 834327 | 834327 | 834327 | matched |
| combined graph triples | 1113959 | 1113959 | 1113959 | matched |
| Barratt parcel1 matches (n) | 272 | 272 | 272 | matched |
| Barratt parcel1 checked (n) | 272 | 272 | 272 | matched |
| embedding participants | 272 | 272 | 272 | matched |
| embedding features | 10 | 10 | 10 | matched |
| imputed cells | 3 | 3 | 3 | matched |
| UMAP trustworthiness seed42 k15 | 0.874 | 0.8739 | 0.8792 | differed |
| PCA trustworthiness k15 | 0.805 | 0.8047 | 0.8047 | matched |
| UMAP trustworthiness seed43 | 0.868 | 0.8676 | 0.8779 | differed |
| UMAP trustworthiness seed44 | 0.879 | 0.8793 | 0.8701 | differed |
| UMAP trustworthiness 30 neighbours | 0.867 | 0.8669 | 0.8603 | differed |
| 15-NN overlap seed43 vs 42 (~74%) | 0.74 | 0.7358 | 0.7515 | differed |
| 15-NN overlap seed44 vs 42 (~74%) | 0.74 | 0.7382 | 0.7331 | matched |
| SHACL conforms | True | True | True | matched |
| SHACL mutation (missing source) rejected | True | True | True | matched |
| JSON Schema valid | True | True | True | matched |
| JSON Schema wrong numeric type rejected | True | True | True | matched |
| collaboration SHACL conforms | True | True | True | matched |
| collaboration missing reviewer rejected | True | True | True | matched |
| T1w entries (recomputed from pinned Git tree) | 265 | 265 | 265 | matched |
| resting BOLD entries (recomputed from pinned Git tree) | 268 | 268 | 268 | matched |
| T1w + rest candidates (recomputed from pinned Git tree) | 261 | 261 | 261 | matched |

Not re-run: skill_pilot.py extraction (frozen host-model artifacts; needs original web snapshots); claims_and_questions.ttl (frozen input); make_report.py (HTML report)

Files that differ byte-wise:

- combined_graph.ttl
- competency_queries.json
- embedding_assessment.json
- embedding_provenance.ttl
- nidm_phenotypes.ttl
- participant_embedding.csv
- phenotype_embedding.pdf
- phenotype_embedding.png
- shacl_summary.json
- umap_runs.json
