# Data and third-party licences

The repository mixes code (Apache-2.0, `LICENSE`), our own text and slides (CC BY 4.0,
`LICENSE-content`) and material derived from public datasets, which keeps its source terms.

## ds000030 — UCLA Consortium for Neuropsychiatric Phenomics LA5c Study (OpenNeuro)

`dataset_description.json` at the pinned commit
[`4070b6ee`](https://github.com/OpenNeuroDatasets/ds000030/blob/4070b6eea231517bfeff42527a46d9d166ac4e13/dataset_description.json)
declares `"License": "CC0"`. The phenotype tables and dictionaries in
`experiments/ds000030/experiment/data/phenotype/` and everything derived from them are
therefore CC0. Please cite Poldrack et al. 2016 (doi:10.1038/sdata.2016.110).

## ABIDE I and ABIDE Preprocessed

The ABIDE I data usage agreement
(<https://fcon_1000.projects.nitrc.org/indi/abide/abide_I.html>, read 2026-10-15) states:

> "Creative Commons, Attribution-NonCommercial-Share Alike License"
> "data usage is unrestricted for non-commercial research purposes"

It also asks users to specify which datasets they used and to acknowledge the funding sources,
and requires registration with NITRC / the 1000 Functional Connectomes Project to download.
The datasets are anonymised under HIPAA guidelines.

Accordingly, every file in `experiments/abide/` that contains participant-level ABIDE values
(the phenotype CSV in `data/`, graphs in `graph/`, participant-level results, figures and the
participant-graph slide) is distributed under **CC BY-NC-SA**, for non-commercial research use,
with attribution to the ABIDE consortium (Di Martino et al. 2014, doi:10.1038/mp.2013.78) and the
Preprocessed Connectomes Project (Craddock et al. 2013). The time series themselves are not in
this repository; `experiments/abide/code/download.py` fetches them from the public
`fcp-indi` bucket and checks them against `data/expected_sha256.json`.

## ReproNim simple2 NIDM

`experiments/abide` links to, and pins by commit, the NIDM files in
<https://github.com/ReproNim/simple2_NIDM_examples> (commit e0dff17); they are fetched at build
time, not redistributed here.

## Literature review

`experiments/abide/literature_review/` contains bibliographic metadata, short verbatim quotes used
as evidence, charting records and the exported review. Article full text and PDFs are **not**
included: publisher licences vary. Each article keeps its `content_sha256`, so a re-fetched copy
can be checked; `scripts/strip_fulltext.py` records how the text was removed.

## Vendored code

`experiments/ds000030/experiment/vendor/` keeps each project's own licence:
UMAP-JS (`umap_LICENSE.txt`), Ajv (`ajv_LICENSE.txt`) and a StructSense subset
(`structsense_LICENSE.txt`).
