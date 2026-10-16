Using only `literature_kg.ttl`, six studies held out whole sites. Five of them report an accuracy for that test in the graph. The sixth (S-022) says it ran the test, but the graph has no accuracy for it.

| Study DOI | Leave-site-out accuracy | Supporting quote (verbatim from the paper) | Cohort size (N) |
|---|---|---|---|
| [10.1016/j.neuroimage.2016.10.045](https://doi.org/10.1016/j.neuroimage.2016.10.045) (S-002) | **66.8%** (best of the pipelines compared; chance 53.7%) | "For inter-site prediction, the highest accuracy obtained on the whole dataset is 66.8% (see Table 2) which exceeds previously published ABIDE findings [53, 13, 54] and chance at 53.7%" | 871 (403 ASD / 468 TD), ABIDE I, 17 sites |
| [10.3389/fnins.2019.01325](https://doi.org/10.3389/fnins.2019.01325) (S-022) | **Not in graph** (only 70.22% from pooled 10-fold CV is recorded) | "…each time, one site out of 17 is used to test, and the other sites are used for training." | 871 (ASD/TD split not reported) |
| [10.3389/fpsyt.2020.00440](https://doi.org/10.3389/fpsyt.2020.00440) (S-030) | **56% balanced accuracy** (64% under 5-fold CV) | "With the leave-site-out CV procedure the performance of the MM-ensemble dropped to an average balanced accuracy of mean 56% and F1 score of 59%, suggesting that this model does not do well in generalizing to new sites." | 2,085 (993 ASD / 1,092 TD), ABIDE I+II |
| [10.3389/fpsyt.2019.00620](https://doi.org/10.3389/fpsyt.2019.00620) (S-062) | **71% ± 6%** (HO atlas; AUC 0.75) | "The binary classification results between subjects with ASD and controls in a leave-one-site-out cross-validation scheme achieved an average accuracy of 0.71 ± 0.06 and an average AUC of 0.75 ± 0.05." | 190 (102 ASD / 88 TD) |
| [10.1109/tnsre.2022.3233656](https://doi.org/10.1109/tnsre.2022.3233656) (S-071) | **73.4%** (CC200 atlas; the graph records this one); 73.1% with AAL is the headline in the abstract | "We also use the Craddock 200 (CC200) atlas [31] to further verify the effectiveness of the LRCDR method and obtain the 73.4% mean accuracy." / "For inter-site prediction on all ABIDE I data (1102 subjects from 17 sites), LRCDR obtains the mean accuracy of 73.1%…" | 1,102 (ASD/TD split not reported) |
| [10.48550/arxiv.1712.08041](https://doi.org/10.48550/arxiv.1712.08041) (S-072) | **~62%** (MLP) | "Whereas the classification accuracy using MLP is ˜62% for all sites, the specificity and sensitivity vary across sites, consistent with the results shown in Figure 1b." | 293 (147 ASD / 146 TD), 4 sites |

**What the graph can't tell you:**
- **S-022:** the graph says the leave-site-out test was run but stores no accuracy for it.
- **Diagnosis split:** S-022 and S-071 are marked "not reported" for ASD vs TD counts.
- **"Best" values:** most accuracies are flagged as the best of several models or atlases, not one pre-specified model. S-030 reports balanced accuracy, so it isn't directly comparable to the others.
- **How quotes link to results:** quotes are tied to papers, not to a specific accuracy value. I picked each quote by reading the graph's one-line summary of what it supports. Every quote I used is flagged in the graph as checked against the full text.
- **Broader definitions:** I counted only studies coded as "leave-site-out". Five more are coded "external dataset" (e.g., train on ABIDE I, test on ABIDE II). That is a different kind of out-of-sample test, so they're not in the table.

**SPARQL used** (run with `uv run --with pyoxigraph python`). This query finds the studies, their accuracy and their cohort size:

```sparql
PREFIX ex: <urn:repronim:abide:>
SELECT ?pub ?id ?acc ?basis ?snippet ?nTotal ?nASD ?nTD
WHERE {
  { ?pub ex:reportsPerformance ?perf . ?perf ex:evaluationScheme "leave-site-out" }
  UNION
  { ?pub a ex:Publication ; ex:evaluationScheme "leave-site-out" }
  ?pub a ex:Publication ; ex:reviewSourceId ?id .
  OPTIONAL { ?pub ex:reportsPerformance ?p2 .
             ?p2 ex:evaluationScheme "leave-site-out" ;
                 ex:accuracyPct ?acc ; ex:basis ?basis ; ex:chartedSnippet ?snippet }
  OPTIONAL { ?link ex:publication ?pub ; ex:cohort ?c .
             OPTIONAL { ?c ex:nTotal ?nTotal } OPTIONAL { ?c ex:nASD ?nASD } OPTIONAL { ?c ex:nTD ?nTD } }
}
ORDER BY ?id
```

This query pulls the verbatim quotes for those studies:

```sparql
PREFIX ex: <urn:repronim:abide:>
PREFIX prov: <http://www.w3.org/ns/prov#>
SELECT ?id ?q ?claim ?quote ?verified WHERE {
  VALUES ?id { "S-002" "S-022" "S-030" "S-062" "S-071" "S-072" }
  ?pub ex:reviewSourceId ?id .
  ?q prov:wasQuotedFrom ?pub ; prov:value ?quote ;
     ex:supportsClaim ?claim ; ex:sourceQuoteVerified ?verified .
} ORDER BY ?id ?q
```

I also checked `ex:siteHandling "leave-site-out evaluation"` as a second route; it found no further leave-site-out studies.
