# ABIDE I/II resting-state literature: what the charted papers did

Computed by `phase3/s4_synthesis.py` from the charted records (quotes re-verified against each paper's full text). Counts are papers; only charted values are counted, and 'not reported' is reported. The corpus is the 99 open-access papers retrieved from 200 sought (see `out/review.md` for the PRISMA flow); this is a second-pass eligibility assessment over those reports, not a census of ABIDE papers.

## In brief

- 74 of 99 papers analysed ABIDE resting-state data; 25 were excluded, almost all (21) because they used only structural or phenotypic ABIDE data.
- Most work is on ABIDE I alone (54 papers); 16 combine I and II; 4 use II alone.
- Prediction dominates: 46 predictive, 7 predictive plus group difference, 20 group difference only.
- Of 53 predictive papers, 26 use cross-validation that mixes sites in train and test folds; only 6 hold whole sites out. Median best accuracy is 73.3% under pooled CV (23 papers; 70.9% without the leakage-flagged ones) and 66.8% under leave-site-out (5 papers). These are different papers, models and subsets, so the gap is descriptive, not a controlled comparison. Two papers report both schemes with numbers for the same model: S-030 drops from 64% to 56% balanced accuracy when sites are held out; S-072 reports about 60% pooled and 62% leave-site-out.
- 8 predictive papers are flagged for leakage (feature selection, harmonisation or tuning using data outside the training folds).
- The analysed cohort can be rebuilt exactly for 17 papers (a published participant list for only 4), partly for 42, not at all for 15.
- The most reused subset is ABIDE I N = 871 (403 ASD / 468 TD): 9 papers, including Abraham et al. (S-002; NeuroImage 2017, corpus year 2016), Parisot et al. 2018 (S-019) and Ktena et al. 2017 (S-024).
- Leave-site-out also appears as a robustness check for group differences (S-005, S-009), which is why the site-handling table counts 8 papers with leave-site-out against 6 in the evaluation table.

## Who got in

- Assessed for eligibility: **99**; included **74**, excluded **25**.
- Read in full text: 98; on abstract only: 1 (S-040 — the retrieved PDF is a different paper).

- Exclusion 3: structural/DTI/phenotype-only ABIDE use (no resting-state analysis): 21
- Exclusion 4: ABIDE used only for methods benchmarking, no autism-vs-control analysis: 4

## Which release, which kind of claim

| ABIDE release | papers |
|---|---|
| ABIDE I | 54 |
| ABIDE I+II | 16 |
| ABIDE II | 4 |

| Main claim | papers |
|---|---|
| predictive | 46 |
| associational | 20 |
| both | 7 |
| descriptor | 1 |

Analysed sample size (total N, 71 papers reporting it): median 871, range 27–2226; 2 did not report a total.

## How prediction papers were evaluated

53 papers make a predictive claim (predictive only, or predictive plus a group difference). A paper can use more than one scheme.

| Evaluation scheme | papers | papers with a charted accuracy | accuracy median (range) | leakage-flagged |
|---|---|---|---|---|
| pooled k-fold CV | 26 | 23 | 73.3% (58.0–96.9) | 4 |
| leave-one-subject-out CV | 5 | 3 | 74.8% (60.0–89.0) | 0 |
| single train/test split | 9 | 8 | 68.7% (62.0–96.2) | 1 |
| leave-site-out | 6 | 5 | 66.8% (56.0–73.4) | 0 |
| external dataset | 4 | 1 | 71.7% (71.7–71.7) | 0 |
| within-site only | 12 | 10 | 77.4% (64.4–96.4) | 3 |
| other | 1 | 0 | — | — |
| not reported | 2 | 2 | 88.1% (81.6–94.7) | 0 |

Accuracy is each paper's best reported result for its own model under that scheme, as charted (two values are balanced accuracy; within-site rows use the cross-site average when the paper gives one, otherwise the best single site). Papers reporting only AUC, correlations or relative changes are not in the accuracy columns: S-005 (regression of SRS (r)), S-009 (regression of ADOS/SRS), S-010 (AUROC only), S-011 (AUC/F1 correlations only), S-016 (AUC only), S-049 (no ASD accuracy table in text), S-063 (relative change only), S-091 (AUC only), S-092 (regression (rs)).

Papers that report the same model under two schemes:

- S-006: pooled k-fold CV 73.3%; external dataset 71.7%
- S-014: pooled k-fold CV 75.2%; within-site only 96.4%
- S-028: pooled k-fold CV 70.8%; within-site only 64.42%
- S-030: pooled k-fold CV 64%; leave-site-out 56%
- S-052: pooled k-fold CV 72.2%; within-site only 67.7%
- S-058: pooled k-fold CV 58%; within-site only 77%
- S-072: pooled k-fold CV 60%; leave-site-out 62%
- S-076: pooled k-fold CV 82.9%; within-site only 75.6%

### Leakage

PROBAST Analysis domain across the 53 predictive papers: High 25, Low 12, Unclear 12, no PROBAST Analysis domain charted 4.
Flagged for leakage (8): Analysis High *and* the charted reason is one of the specific patterns below. Other High ratings were for single splits without uncertainty, pooled CV ignoring site, or no stated validation — weaknesses, but not leakage by this rule.

- harmonisation/deconfounding outside CV: S-011, S-016
- feature selection outside CV: S-014, S-052, S-077, S-099
- tuning on the test set: S-027
- unsupervised feature derivation on full sample: S-060

## Pipelines, atlases, site handling

Over the 73 included analysis papers (the ABIDE II data descriptor excluded); a paper can use several.

| Preprocessing pipeline | papers |
|---|---|
| CPAC | 34 |
| custom (SPM/FSL/AFNI/in-house) | 17 |
| DPARSF | 7 |
| not reported | 5 |
| CCS | 5 |
| CONN | 2 |
| GRETNA | 2 |
| fMRIPrep | 1 |
| Athena | 1 |
| fconn1000 | 1 |
| NIAK | 1 |

| Atlas / parcellation | papers |
|---|---|
| AAL | 20 |
| CC200 | 15 |
| Harvard-Oxford | 14 |
| not reported / not applicable | 11 |
| none (voxel/seed/vertex-wise) | 11 |
| ICA / data-driven networks | 4 |
| Schaefer | 3 |
| Eickhoff-Zilles (EZ) | 3 |
| Dosenbach 160 | 3 |
| CC400 | 3 |
| Talairach (TT) | 2 |
| BASC | 2 |
| Power 264 | 2 |
| Craddock (other scale) | 1 |
| MSDL | 1 |
| Yeo | 1 |
| random parcellation | 1 |
| Brodmann | 1 |
| Desikan-Killiany (structural) | 1 |
| Shen 268 | 1 |

| Site handling | all analysis papers | predictive papers |
|---|---|---|
| leave-site-out evaluation | 8 | 8 |
| ComBat/NeuroHarmonize harmonisation | 7 | 3 |
| site covariate / regressed out | 8 | 2 |
| other site control | 11 | 7 |
| per-site analyses | 7 | 6 |
| site used as a model input or graph feature | 4 | 4 |
| single site | 6 | 4 |
| none reported | 28 | 22 |

## Can the analysed cohort be rebuilt? (RQ6)

- Yes: 17 (23%) — of which a released participant list: 4; exact rules only: 13.
- Partly: 42 (57%).
- No: 15 (20%).

Code and/or participant list (CL7): yes 20, no 41, partly 13; code release mentioned in 18.

## Papers analysing the same cohort

Grouped by identical release and charted N by diagnosis. The same N does not prove the same participants; it is the strongest signal the papers themselves give, since few publish a participant list.

### ABIDE I, N = 871 (403 ASD / 468 TD) — 9 papers
Pipelines: CPAC 8, not reported 1.

- S-002 Alexandre Abraham 2016 — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example [CPAC; Harvard-Oxford, MSDL, ICA / data-driven networks, Yeo; predictive; reconstructible: partly]
- S-019 Sarah Parisot 2018 — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer’s disease [CPAC; Harvard-Oxford; predictive; reconstructible: partly]
- S-022 Zeinab Sherkatghanad 2020 (total N only charted) — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network [CPAC; CC400; predictive; reconstructible: partly]
- S-024 Sofia Ira Ktena 2017 — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks [CPAC; Harvard-Oxford; predictive; reconstructible: partly]
- S-066 Wanyi Chen 2024 — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data [CPAC; CC200, AAL, Dosenbach 160; predictive; reconstructible: yes — exact rules]
- S-069 Muhammed Ali Bayram 2021 — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images [not reported; BASC; predictive; reconstructible: no]
- S-070 Wenjing Jiang 2022 — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification [CPAC; none (voxel/seed/vertex-wise); predictive; reconstructible: partly]
- S-076 Lizhen Shao 2023 — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder [CPAC; Harvard-Oxford; predictive; reconstructible: partly]
- S-077 Ibrahim Salim 2023 — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation [CPAC; Harvard-Oxford; predictive; reconstructible: no]

### ABIDE I, N = 1035 (505 ASD / 530 TD) — 6 papers
Pipelines: CPAC 6.

- S-014 Xuehan Liu 2024 — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder [CPAC; CC200, AAL, Eickhoff-Zilles (EZ); predictive; reconstructible: yes — exact rules]
- S-028 Fahad Almuqhim 2021 — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data [CPAC; CC200; predictive; reconstructible: no]
- S-053 Jinlong Hu 2021 — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification [CPAC; AAL, Harvard-Oxford; predictive; reconstructible: partly]
- S-064 Ibrahim Nafisah 2025 — Deep learning-based feature selection for detection of autism spectrum disorder [CPAC; AAL, Eickhoff-Zilles (EZ); predictive; reconstructible: no]
- S-096 Archit Rathore 2019 — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale [CPAC; CC200, CC400; predictive; reconstructible: partly]
- S-099 Naseer Ahmed Khan 2020 — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder [CPAC; AAL; predictive; reconstructible: partly]

### ABIDE I, N = 184 (79 ASD / 105 TD) — 3 papers
Pipelines: CCS 1, DPARSF 1, CPAC 1.

- S-054 Md Shale Ahammed 2021 — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network [CCS; not reported / not applicable; predictive; reconstructible: partly]
- S-059 Ying Chu 2022 — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI [DPARSF; CC200, AAL; predictive; reconstructible: partly]
- S-060 Ming–Hsuan Yang 2021 — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model [CPAC; ICA / data-driven networks; predictive; reconstructible: no]

### ABIDE I, N = 1112 (539 ASD / 573 TD) — 2 papers
Pipelines: CCS 1, CPAC 1.

- S-063 Johan Jönemo 2023 — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks [CCS; none (voxel/seed/vertex-wise); predictive; reconstructible: no]
- S-081 Swati Rane 2017 — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset [CPAC; none (voxel/seed/vertex-wise); predictive; reconstructible: partly]

### ABIDE I, N = 1111 (538 ASD / 573 TD) — 2 papers
Pipelines: custom (SPM/FSL/AFNI/in-house) 2.

- S-023 Bhaskar Sen 2018 — A general prediction model for the detection of ADHD and Autism using structural and functional MRI [custom (SPM/FSL/AFNI/in-house); ICA / data-driven networks; predictive; reconstructible: yes — exact rules]
- S-032 Sina Ghiassian 2016 — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism [custom (SPM/FSL/AFNI/in-house); not reported / not applicable; predictive; reconstructible: partly]

### ABIDE I, N = 1102 (529 ASD / 573 TD) — 2 papers
Pipelines: CPAC 2, DPARSF 1, CCS 1, NIAK 1.

- S-036 Md Rishad Ahmed 2020 — Single Volume Image Generator and Deep Learning-Based ASD Classification [CPAC, DPARSF, CCS, NIAK; not reported / not applicable; predictive; reconstructible: no]
- S-071 Xingdan Liu 2023 (total N only charted) — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study [CPAC; CC200, AAL; predictive; reconstructible: partly]

