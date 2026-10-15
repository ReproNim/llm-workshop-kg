# Corpus selection rule (ABIDE I and II review)

Decided by the review owner: ~100 open-access papers, ABIDE I and II, agent-authored review.

1. Identification (OpenAlex, 2026-10-15; `code/search_openalex.py`):
   works citing Di Martino 2014 (W2167868121, ABIDE I descriptor) whose title or abstract
   mentions "ABIDE"; works citing Di Martino 2017 (W2590651237, ABIDE II descriptor) with the
   same filter; works citing Abraham 2017 (W2522924024; the seed already in the knowledge graph)
   with the same filter; plus the two release descriptors themselves (other sources).
2. Deduplication by OpenAlex work id.
3. Metadata pre-screen (`code/select_corpus.py`): open access required (protocol inclusion 4);
   OpenAlex type review/editorial/erratum/paratext/letter/dissertation/book excluded; titles that
   announce a review/survey/meta-analysis excluded. Records without a DOI excluded (DOI is the
   article's identity in the graph).
4. Ranking: by OpenAlex cited_by_count, descending, with quotas filled first, in this order:
   the three must-include papers (Di Martino 2014, Di Martino 2017, Abraham 2017);
   ≥ 25 papers seeded by or naming ABIDE II; ≥ 40 papers whose title/abstract matches a
   prediction vocabulary (classif|predict|machine/deep learning|neural network|SVM|accuracy|AUC|…);
   ≥ 30 papers matching a group-difference vocabulary (hypo/hyper-connectivity|altered|reduced|
   increased|differences|…) and not the prediction vocabulary. The vocabularies are a ranking
   heuristic only — claim type is decided at full-text charting (RQ3), not here.
   The top 200 ranked candidates (160 first; extended by 40 in citation order when the first pass yielded 90 PDFs) are sent to open-access retrieval.
5. Retrieval: `fetch_ezproxy.py --oa-only` (Unpaywall → OpenAlex → Semantic Scholar; no
   institutional access). The corpus is the first ~100 candidates, in rank order, whose PDF was
   retrieved and passes the text-layer check, keeping the quotas above where retrieval allows.
