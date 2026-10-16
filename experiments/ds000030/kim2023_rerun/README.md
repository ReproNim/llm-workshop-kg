# Re-run of Kim et al. 2023 (UCLA, leave-one-out)

Kim et al. 2023, "Bidirectional connectivity alterations in schizophrenia: a multivariate, machine-learning
approach", Front. Psychiatry, doi:10.3389/fpsyt.2023.1232015. The authors share the preprocessed UCLA data
(94 connectivity matrices, Shen 268 regions, with patient/control labels) and MATLAB code on OSF:
https://osf.io/agqtn/ . The OSF project lists no licence, so the files are fetched, not redistributed.

- `fetch_osf.sh` downloads `UCLA_data.mat` and `UCLA_code.m` and checks their SHA-256.
- `rerun_ucla_cpm.py` is a Python port of `UCLA_code.m`: connectome-based predictive modelling (edges correlated
  with diagnosis at p < 0.05 in the 93 training participants, summed into increased and decreased scores),
  then a linear SVM, leave one participant out.
- `rerun_ucla_cpm.json` is the result: 70.2% (66 of 94) with both directions, as the paper reports; the paper
  does not report the single-direction models, which give 52.1% (decreased) and 61.7% (increased).

The 47 + 47 sample is propensity-score matched from ds000030 after motion exclusion (excluded IDs are in the
paper's supplementary material); which ds000030 participant each matrix is, is not given.
