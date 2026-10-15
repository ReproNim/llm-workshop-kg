# Use of ABIDE I and II resting-state data in autism connectivity and diagnostic-prediction studies

*Generated: 2026-10-15T19:37:21.681948+00:00 | PRISMA 2020 Compliant*


---

## Abstract

**Objective:** Characterise how published studies use the Autism Brain Imaging Data Exchange (ABIDE I and ABIDE II) resting-state fMRI releases: which subsets and quality-control rules define the analysed cohorts, which preprocessing pipelines and parcellations are used, whether the main claim is associational (group difference) or predictive (diagnostic classification/regression), how it is evaluated, what is found, and whether the analysed cohort can be reconstructed from released files, so that each publication can be linked to the dataset subset it used in a knowledge graph.

**Methods:** A systematic search of OpenAlex, Other sources was conducted. Studies were screened against predefined criteria. Risk of bias was assessed using JBI Critical Appraisal.

**Results:** 994 records were identified. After removing 268 duplicates and screening, 74 studies were included.

---

## 1. Introduction

### 1.1 Rationale (PRISMA Item 3)

Characterise how published studies use the Autism Brain Imaging Data Exchange (ABIDE I and ABIDE II) resting-state fMRI releases: which subsets and quality-control rules define the analysed cohorts, which preprocessing pipelines and parcellations are used, whether the main claim is associational (group difference) or predictive (diagnostic classification/regression), how it is evaluated, what is found, and whether the analysed cohort can be reconstructed from released files, so that each publication can be linked to the dataset subset it used in a knowledge graph.

### 1.2 Objectives (PRISMA Item 4)

- **Population:** Participants from ABIDE I and/or ABIDE II (autistic individuals and typically developing controls, all ages, all contributing sites) whose resting-state fMRI data were analysed
- **Intervention:** Analysis of ABIDE resting-state functional connectivity (raw or preprocessed releases, e.g. the Preprocessed Connectomes Project) for group-difference testing or diagnostic prediction
- **Comparison:** Autistic participants versus typically developing controls (or across-site / held-out-site evaluation for prediction studies)
- **Outcome:** Reported cohort composition and selection rules; connectivity group differences (direction, networks, effect size); diagnostic prediction performance (accuracy, AUC, sensitivity/specificity with confidence intervals); reproducibility information (code, participant lists)

---

## 2. Methods

### 2.1 Eligibility Criteria (PRISMA Item 5)

**Inclusion:** (1) Primary research article or data descriptor (peer-reviewed journal or conference paper, or preprint); (2) analyses resting-state fMRI data from ABIDE I and/or ABIDE II (stated explicitly in the methods); (3) reports either a group-difference analysis between autism and control groups or a diagnostic prediction/classification analysis, or describes the ABIDE release itself; (4) full text in English available open access.

**Exclusion:** (1) Reviews, meta-analyses, editorials, commentaries, theses and protocols without original ABIDE analysis; (2) studies that only cite ABIDE without analysing its data; (3) studies using only structural MRI, DTI or phenotypic data from ABIDE with no resting-state functional analysis; (4) studies whose ABIDE analysis is limited to software benchmarking with no autism-vs-control analysis (e.g. registration or motion-correction method tests); (5) non-English full text; (6) full text not openly accessible.

### 2.2 Information Sources (PRISMA Item 6)

Databases searched: OpenAlex, Other sources

Date of last search: 2026-10-15

Multi-hop citation navigation: up to 0 hops

### 2.3 Search Strategy (PRISMA Item 7)

Queries used:
- `OpenAlex (searched 2026-10-15): https://api.openalex.org/works?filter=cites:W2167868121,title_and_abstract.search:ABIDE | filters: title_and_abstract.search:ABIDE; citing the named descriptor/seed work | 598 records | seed ABIDE I (W2167868121)`
- `OpenAlex (searched 2026-10-15): https://api.openalex.org/works?filter=cites:W2590651237,title_and_abstract.search:ABIDE | filters: title_and_abstract.search:ABIDE; citing the named descriptor/seed work | 174 records | seed ABIDE II (W2590651237)`
- `OpenAlex (searched 2026-10-15): https://api.openalex.org/works?filter=cites:W2522924024,title_and_abstract.search:ABIDE | filters: title_and_abstract.search:ABIDE; citing the named descriptor/seed work | 220 records | seed Abraham 2017 (graph seed) (W2522924024)`
- `Other sources (searched 2026-10-15): release descriptors added by DOI: 10.1038/mp.2013.78, 10.1038/sdata.2017.10 | 2 records | Di Martino 2014 (ABIDE I) and Di Martino 2017 (ABIDE II) data descriptors`
- `Grey literature / other sources: none`
- `Search notes: Metadata screen (not a title/abstract reading): records excluded = not open access (310) plus non-primary publication types / review titles. Of the remaining open-access primary records, the top 200 by citation count (with quotas, search/selection_rule.md) were sought in full text; 99 retrieved; 99 form the corpus assessed for eligibility. Open-access primary records not in the top-ranked set were not sought (corpus-size decision by the review owner). Not retrieved (101): 47 no open-access PDF location known; 23 publisher OA URL returned a bot-check page instead of a PDF; 49 of the misses had a PMCID but PMC routes were blocked (Europe PMC ?pdf=render returned HTTP 403 (bot check); Europe PMC fullTextXML returned 500; NCBI PMC OA service returned 404 (2026-10-15)); 40 extension-batch misses not re-checked. Must-include not retrieved: 10.1038/mp.2013.78: Di Martino 2014 (ABIDE I descriptor): OA locations are a repository landing page (pure.knaw.nl) whose file link returned an HTML bot-check page, and PMC4162310 (PMC routes blocked); no PDF obtained`

### 2.4 Selection Process (PRISMA Item 8)

Metadata screening was rule-based (open-access availability, publication type). Full-text screening, charting and appraisal were performed by AI agents (Claude Sonnet, eight parallel batches) following the protocol and charting instructions; every supporting quote was verified mechanically against the source text. No human verified individual screening or charting decisions in this run. [Corrected 2026-10-15: the exporter's default text claimed human verification.]

### 2.5 Risk of Bias (PRISMA Item 11)

Risk of bias was assessed using **JBI Critical Appraisal**.

---

## 3. Results

### 3.1 PRISMA Flow (Item 16a)

| Stage | Count |
|-------|-------|
| PubMed | 0 |
| bioRxiv | 0 |
| medRxiv | 0 |
| Related articles | 0 |
| Citation hops | 0 |
| OpenAlex | 992 |
| Other sources | 2 |
| **Total identified** | **994** |
| Duplicates removed | 268 |
| Screened | 726 |
| Excluded (screening) | 314 |
| Reports sought for retrieval | 200 |
| Full text retrieved | 99 |
| Reports not retrieved | 101 |
| Assessed for eligibility | 99 |
| Excluded (eligibility) | 25 |
| **Included** | **74** |

#### Full-text access and screening basis

| Retrieval route | Reports |
|-----------------|---------|
| Unpaywall (open access PDF) | 96 |
| OpenAlex (open access PDF) | 3 |
| **Total retrieved** | **99** |

| Eligibility assessed on | Reports |
|--------------------------|---------|
| Full text | 98 |
| Abstract only (full text unavailable) | 1 |

99% of eligibility decisions were made with the full report available.

Of the 74 included studies, **74** were read in full text and **0** were included on the abstract alone.

**Exclusions at title/abstract screening**

| Reason | Reports |
|--------|---------|
| Not open access (metadata screen) | 310 |
| Non-primary publication type or review title (metadata screen) | 4 |

**Exclusions at eligibility assessment**

| Reason | Reports |
|--------|---------|
| Exclusion 3: structural/DTI/phenotype-only ABIDE use (no resting-state analysis) | 21 |
| Exclusion 4: ABIDE used only for methods benchmarking, no autism-vs-control analysis | 4 |

### 3.2 Study Characteristics (Item 17)

| Authors | Year | Journal | Design | RoB |
|---------|------|---------|--------|-----|
| Adriana Di Martino; David A. O’Connor; Bosi Chen; Kaat Alaerts; Jeffrey S. Anderson; Michal Assaf; Joshua Henk Balsters; Leslie C. Baxter; Anita Beggiato; Sylvie Bernaerts; Laura M. E. Blanken; Susan Y. Bookheimer; Brittany B. Braden; Lisa A. Byrge; F. Xavier Castellanos; Mirella Dapretto; Richard Delorme; Damien A. Fair; Inna Fishman; Jacqueline Fitzgerald; Louise Gallagher; R. Joanne Jao Keehn; Daniel P. Kennedy; Janet E. Lainhart; Beatríz Luna; Stewart H. Mostofsky; Ralph-Axel Müller; Mary Beth Nebel; Joel T. Nigg; Kirsten M. O’Hearn; Marjorie Solomon; Roberto Toro; Chandan J. Vaidya; Nicole Wenderoth; Tonya J.H. White; Richard Cameron Craddock; Catherine Lord; BENNETT L. LEVENTHAL; Michael Peter Milham | 2017 | Scientific Data | NR | Low |
| Adnan Ashraf; Qingjie Zhao; Waqas Haider Bangyal; Muddesar Iqbal | 2023 | IEEE Transactions on Consumer Electronics | NR | High |
| Rafi Ayub; Kevin Sun; Ryan E. Flores; Vicky T. Lam; Booil Jo; Manish Saggar; Lawrence K. Fung | 2021 | Translational Psychiatry | NR | Low |
| Dorothea L. Floris; José Osmar Alves Filho; Meng‐Chuan Lai; Steve Giavasis; Marianne Oldehinkel; Maarten Mennes; Tony Charman; Julian Tillmann; Guillaume Dumas; Christine Ecker; Flavio Dell’Acqua; Tobias Banaschewski; Carolin Moessnang; Simon Baron‐Cohen; Sarah Durston; Eva Loth; Declan Murphy; Jan K. Buitelaar; Christian F. Beckmann; Michael Peter Milham; Adriana Di Martino | 2021 | Molecular Autism | NR | Low |
| Oualid M. Benkarim; Casey Paquola; Bo‐yong Park; Valeria Kebets; Seok‐Jun Hong; Reinder Vos de Wael; Shaoshi Zhang; B.T. Thomas Yeo; Michael Eickenberg; Tian Ge; Jean‐Baptiste Poline; Boris C. Bernhardt; Danilo Bzdok | 2022 | PLoS Biology | NR | High |
| Taiane Coelho Ramos; Joana Bisol Balardin; João Ricardo Sato; André Fujita | 2019 | Frontiers in Systems Neuroscience | NR | Low |
| Xuehan Liu; Md Rakibul Hasan; Tom Gedeon; Md Zakir Hossain | 2024 | Computers in Biology and Medicine | NR | High |
| Pegah Kassraian; Caroline Matthis; Joshua Henk Balsters; Marloes H. Maathuis; Nicole Wenderoth | 2016 | Frontiers in Psychiatry | NR | Low |
| Sina Ghiassian; Russell Greiner; Ping Jin; Matthew Brown | 2016 | PLoS ONE | NR | Low |
| Jung Min Lee; S.-H. Kyeong; Eun Joo Kim; Keun-Ah Anna Cheon | 2016 | Frontiers in Neuroscience | NR | Unclear |
| Ryuzo Hanaie; Ikuko Mohri; Kuriko Kagitani‐Shimono; Masaya Tachibana; Junko Matsuzaki; Ikuko Hirata; Fumiyo Nagatani; Yoshiyuki Watanabe; Taiichi Katayama; Masako Taniike | 2018 | Frontiers in Human Neuroscience | NR | Low |
| Jinlong Hu; Lijie Cao; Tenghui Li; Shoubin Dong; Ping Li | 2021 | BMC Bioinformatics | NR | High |
| Md Shale Ahammed; Sijie Niu; Md Rishad Ahmed; Jiwen Dong; Xizhan Gao; Yuehui Chen | 2021 | Frontiers in Neuroinformatics | NR | High |
| Ahmed El-Gazzar; Mirjam Quaak; Leonardo Cerliani; Peter Bloem; Guido Alexander van Wingen; Rajat Mani Thomas | 2019 | Lecture notes in computer science | NR | High |
| Ying Chu; Guangyu Wang; Liang Cao; Lishan Qiao; Mingxia Liu | 2022 | Frontiers in Neuroinformatics | NR | Low |
| Wanyi Chen; Jianjun Yang; Zhongquan Sun; Xiang Zhang; Guangyu Tao; Yuan Ding; Jingjun Gu; Jiajun Bu; Haishuai Wang | 2024 | Translational Psychiatry | NR | Low |
| Wonsik Jung; Eunjin Jeon; Eunsong Kang; Heung‐Il Suk | 2023 | IEEE Transactions on Medical Imaging | NR | Low |
| Lucas Mahler; Qi Wang; Julius Steiglechner; Florian Birk; Samuel Heczko; Klaus Scheffler; Gabriele Lohmann | 2023 | Lecture notes in computer science | NR | Low |
| Alexandra M. Reardon; Kaiming Li; Xiaoping Philip Hu | 2021 | Frontiers in Computational Neuroscience | NR | Low |
| Meenakshi Khosla; Keith Wakefield Jamison; Amy F. Kuceyeski; Mert Rory Sabuncu | 2018 | Lecture notes in computer science | NR | Unclear |
| Cooper Mellema; Kevin P. Nguyen; Alex Treacher; Albert Montillo | 2022 | Scientific Reports | NR | Low |
| Xiaoxiao Li; Yufeng Gu; Nicha C. Dvornek; Lawrence H. Staib; Pamela E. Ventola; James S. Duncan | 2020 | Medical Image Analysis | NR | Unclear |
| Zeinab Sherkatghanad; Mohammadsadegh Akhondzadeh; Soorena Salari; Mariam Zomorodi Moghadam; Moloud Abdar; U. Rajendra Acharya; Reza Khosrowabadi; Vahid Salari | 2020 | Frontiers in Neuroscience | NR | Low |
| Bhaskar Sen; Neil C. Borle; Russell Greiner; Matthew Brown | 2018 | PLoS ONE | NR | Low |
| Hailong Li; Nehal A. Parikh; Lili He | 2018 | Frontiers in Neuroscience | NR | Low |
| Kaat Alaerts; Daniel Graham Woolley; Jean G. Steyaert; Adriana Di Martino; Stephan Patrick Swinnen; Nicole Wenderoth | 2013 | Social Cognitive and Affective Neuroscience | NR | Low |
| Xia-an Bi; Yang Wang; Shu Qing Ma; Qi Sun; Qian Xu | 2018 | Frontiers in Genetics | NR | High |
| Rajat Mani Thomas; Selene Gallo; Leonardo Cerliani; Paul Zhutovsky; Ahmed El-Gazzar; Guido Alexander van Wingen | 2020 | Frontiers in Psychiatry | NR | Low |
| Amirali Kazeminejad; Roberto C. Sotero | 2019 | Frontiers in Neuroscience | NR | Unclear |
| Rushil Anirudh; Jayaraman J. Thiagarajan | 2019 | IEEE International Conference on Acoustics Speech and Signal Processing | NR | High |
| Iva Ilioska; Marianne Oldehinkel; Alberto Llera; Sidhant Chopra; Tristan Looden; Roselyne J. Chauvin; Daan van Rooij; Dorothea L. Floris; Julian Tillmann; Carolin Moessnang; Tobias Banaschewski; Rosemary Holt; Eva Loth; Tony Charman; Declan Murphy; Christine Ecker; Maarten Mennes; Christian F. Beckmann; Alex Fornito; Jan K. Buitelaar; EU-AIMS LEAP Group | 2022 | Biological Psychiatry | NR | Low |
| Yongcheng Zong; Qiankun Zuo; Michael K. Ng; Baiying Lei; Shuqiang Wang | 2024 | IEEE Transactions on Pattern Analysis and Machine Intelligence | NR | High |
| Yaya Liu; Lingyu Xu; Jun Li; Jie Yu; Xuan Yu | 2020 | Experimental Neurobiology | NR | High |
| Ming–Hsuan Yang; Menglin Cao; Yuhao Chen; Yanni Chen; Geng Fan; Chenxi Li; Jue Wang; Tian Liu | 2021 | Frontiers in Human Neuroscience | NR | High |
| Xinyu Zhao; D. Rangaprakash; Bowen Yuan; Thomas S. Denney; Jeffrey S. Katz; Michael N. Dretsch; Gopikrishna Deshpande | 2018 | Frontiers in Applied Mathematics and Statistics | NR | Unclear |
| Ibrahim Salim; A. Ben Hamza | 2023 | Cognitive Computation | NR | High |
| Alexandre Abraham; Michael Peter Milham; Adriana Di Martino; Richard Cameron Craddock; Dimitris Samaras; Bertrand Thirion; Gael P. Varoquaux | 2016 | NeuroImage | NR | Low |
| Sarah Parisot; Sofia Ira Ktena; Enzo Ferrante; Matthew Lee; Ricardo Guerrero; Ben Glocker; Daniel Rueckert | 2018 | Medical Image Analysis | NR | Unclear |
| Jared Allen Nielsen; Brandon A. Zielinski; P. Thomas Fletcher; Andrew L. Alexander; Nicholas DE LANGE; Erin D. Bigler; Janet E. Lainhart; Jeffrey S. Anderson | 2013 | Frontiers in Human Neuroscience | NR | Low |
| Sofia Ira Ktena; Sarah Parisot; Enzo Ferrante; Martin Rajchl; Matthew Lee; Ben Glocker; Daniel Rueckert | 2017 | Lecture notes in computer science | NR | Unclear |
| Md Rishad Ahmed; Yuan Zhang; Omer T. Inan; Hongen Liao | 2020 | IEEE Journal of Biomedical and Health Informatics | NR | High |
| Enrico Glerean; Raj Kumar Pan; Juha Salmi; Rainer Kujala; Juha M. Lahnakoski; Ulrika Roine; Lauri Nummenmaa; Sami Leppämäki; Taina Nieminen‐von Wendt; Pekka Tani; Jari Saramäki; Mikko E. Sams; Iiro P. Jääskeläinen | 2015 | Human Brain Mapping | NR | Low |
| Pingting Lin; Shiyi Zang; Yi Bai; Haixian Wang | 2022 | Frontiers in Human Neuroscience | NR | Low |
| Olga Dona; Geoffrey B. Hall; Michael D. Noseworthy | 2017 | PLoS ONE | NR | Unclear |
| Elizabeth Barbara Torres; Kristina Denisova | 2016 | Scientific Reports | NR | Low |
| Sarah Itani; Dorina Thanou | 2021 | Medical Image Analysis | NR | Low |
| R. Nur Syahindah Husna; A. R. Syafeeza; Norihan Binti Abdul Hamid; Yan Chiew Wong; R. Atikah Raihan | 2021 | Jurnal Teknologi | NR | High |
| Giovanna Spera; Alessandra Retico; Paolo Bosco; Elisa Ferrari; Letizia Palumbo; P. Oliva; Filippo Muratori; Sara Calderoni | 2019 | Frontiers in Psychiatry | NR | Low |
| Ibrahim Nafisah; Nermine Mahmoud; Ahmed A. Ewees; Mohamed G. Khattap; Abdelghani Dahou; Safar M. Alghamdi; Ibrahim Ahmed Fares; Mohammed Azmi Al‐Betar; Mohamed Abd Elaziz | 2025 | Frontiers in Artificial Intelligence | NR | High |
| Muhammed Ali Bayram; İlyas Özer; Feyzullah Temurtaş | 2021 | Sakarya University Journal of Computer and Information Sciences | NR | High |
| Xingdan Liu; Jiacheng Wu; Wenqi Li; Qian Liu; Lixia Tian; Huifang Huang | 2023 | IEEE Transactions on Neural Systems and Rehabilitation Engineering | NR | Unclear |
| Ravi Tejwani; Liska et al. | 2017 | arXiv (Cornell University) | NR | Unclear |
| Lizhen Shao; Cong Fu; Xunying Chen | 2023 | BMC Bioinformatics | NR | High |
| Yiqian Luo; Qiurong Chen; Fali Li; Yi Liang; Peng Xu; Yangsong Zhang | 2025 | Neural Networks | NR | High |
| Chia-Min Chen; Pinchen Yang; Ming‐Tsang Wu; Tzu‐Chao Chuang; Teng‐Yi Huang | 2019 | Scientific Reports | NR | Unclear |
| Yapei Xie; Zhilei Xu; Mingrui Xia; Jin Liu; Xiao‐Jing Shou; Zaixu Cui; Xuhong Liao; Yong He | 2021 | Biological Psychiatry | NR | Low |
| Shile Qi; Robin Morris; Jessica A. Turner; Zening Fu; Rongtao Jiang; Thomas P. DeRamus; Dongmei Zhi; Vince D. Calhoun; Jing Sui （Beijing Normal University）， my correct affiliation is beijing normal university et al. | 2020 | Molecular Autism | NR | Low |
| Stefano Berto; Alex Treacher; Emre Caglayan; Danni Luo; Jillian R. Haney; Michael J. Gandal; Daniel H. Geschwind; Albert Montillo; Geneviève Konopka | 2022 | Nature Communications | NR | Low |
| Sara Saponaro; Francesca Lizzi; Giacomo Serra; Francesca Mainas; P. Oliva; Alessia Giuliano; Sara Calderoni; Alessandra Retico | 2024 | Brain Informatics | NR | High |
| Fahad Almuqhim; Fahad Saeed | 2021 | Frontiers in Computational Neuroscience | NR | Unclear |
| Johan Jönemo; David Abramian; Anders Eklund | 2023 | Diagnostics | NR | Unclear |
| Wenjing Jiang; Shuaiqi Liu; Hong Zhang; Xiuming Sun; Shuihua Wang‎; Jie Zhao; Jingwen Yan | 2022 | Frontiers in Aging Neuroscience | NR | High |
| Shuo Chen; Yishi Xing; Jian Kang | 2017 | Frontiers in Neuroscience | NR | High |
| Clara F. Weber; Valeria Kebets; Oualid M. Benkarim; Sara Larivière; Yezhou Wang; Alexander Ngo; Hongxiu Jiang; Xiaoqian J. Chai; Bo‐yong Park; Michael Peter Milham; Adriana Di Martino; Sofie Louise Valk; Seok‐Jun Hong; Boris C. Bernhardt | 2024 | Molecular Autism | NR | Low |
| Swati Rane; Eshin Jolly; Anne T. Park; Hojin Jang; Cameron Craddock | 2017 | Research Ideas and Outcomes | NR | High |
| Lei Wei; Yao Zhang; Wensheng Zhai; Huaning Wang; Junchao Zhang; Haojie Jin; Jianfei Feng; Qin Qin; Hao Xu; Baojuan Li; Jian Liu | 2022 | Frontiers in Neuroscience | NR | Unclear |
| Shuo Chen; Jian Kang; Guoqing Wang | 2015 | Frontiers in Neuroscience | NR | Unclear |
| Carla Caballero; Sejal Mistry; Elizabeth Barbara Torres | 2020 | Frontiers in Integrative Neuroscience | NR | Unclear |
| Christiane S. Rohr; Shanty Kamal; Signe Bray | 2019 | Developmental Cognitive Neuroscience | NR | Low |
| Pavithra Elumalai; Yasharth Yadav; Nitin Williams; Emil Saucan; Jürgen Jost; Areejit Samal | 2022 | Scientific Reports | NR | Low |
| Robert X. Smith; Kay Jann; Mirella Dapretto; Danny J.J. Wang | 2018 | Frontiers in Neuroscience | NR | Low |
| Archit Rathore; Sourabh Palande; Jeffrey S. Anderson; Brandon A. Zielinski; P. Thomas Fletcher; Bei Wang | 2019 | Lecture notes in computer science | NR | Low |
| Mohammed Isam Al-Hiyali; Norashikin Yahya; Ibrahima Faye; Zia Khan | 2021 | International Journal of Integrated Engineering | NR | High |
| Naseer Ahmed Khan; Samer Abdulateef Waheeb; Atif Riaz; Xuequn Shang | 2020 | Brain Sciences | NR | High |

### 3.3 Narrative Summary Table

| Source | Design / Sample / Dataset | Methods | Outcomes | Limitations | Relevance Notes | Review Q&A |
|--------|--------------------------|---------|----------|-------------|-----------------|------------|
| S-001 | Data descriptor; ABIDE II release; N=487 ASD, N=557 controls (1,044 datasets total) across 17 collections and 16 sites (9 ABIDE I charter sites + 7 new). | Describes data contribution, anonymization, and aggregation procedures across sites; diagnosis basis per collection (ADOS/ADI-R and/or clinical judgment); QC assessed with the Preprocessed Connectomes Project protocol (spatial and temporal metrics including mean FD) but not used to exclude data. | Cohort composition, demographic and phenotypic variable availability (SRS, RBS-R, ADOS/ADI-R), and QC metric distributions by collection are reported; no group-difference or classification analysis is performed. | Heterogeneity across sites in inclusion/exclusion criteria, scanners and acquisition parameters; no consensus QC threshold is applied, so users must select/exclude data themselves. | Defines the ABIDE II release structure (collections, sites, Ns, diagnosis basis, QC metrics) that downstream analysis papers subset from; central for linking any ABIDE II-using publication to its data provenance. |  |
| S-004 | Diagnostic prediction (CNN and transfer learning); ABIDE-I (1112 datasets: 539 ASD, 573 TC) and ABIDE-II (reported as 1114 or 1014 datasets: 521 ASD, 593 TC) across 17 sites; combined ABIDE-I+II analysis also reported. | MRI-derived images/heat maps from ABIDE rs-fMRI data are classified with an optimized CNN and a transfer-learning model (DTL-NN); results reported separately per data-collection site/resource and per age-based subgroup, with no described preprocessing pipeline, atlas, or train/test split. | Accuracy, sensitivity, specificity and F1-score reported per site and per dataset grouping; best combined ABIDE-I+II result: CNN 81.56% accuracy, DTL-NN 82.31% accuracy. | Authors note limitations from multi-site data collection (17 sites) and picture data availability (851 subjects); no cross-validation/held-out evaluation, no diagnosis-source documentation, no preprocessing/atlas details, inconsistent N reporting between abstract and tables. | Uses ABIDE I and II for diagnostic prediction but with minimal methodological transparency on cohort construction, QC, pipeline, and validation — illustrates reconstructibility and rigor gaps relevant to the dataset-publication link. |  |
| S-007 | Group-difference (associational) seed-based connectivity study; primary cohort is the authors' own lab sample (23 ASD, 20 TD); ABIDE-derived secondary/validation cohort: 58 ASD, 51 TD, matched by age/sex/IQ. | Both cohorts preprocessed identically with fMRIPrep v1.3.1; FD-based scrubbing (>0.5mm) and <80% TR-retention exclusion; whole-thalamus seed-based whole-brain GLM connectivity with site as a covariate in the ABIDE analysis; Bonferroni correction for five seeds. | Right thalamus hyperconnectivity with right precentral/postcentral gyri in ASD vs TD replicated in the ABIDE cohort (p=0.019, p=0.028), supporting thalamocortical hyperconnectivity in high-functioning adult ASD. | ABIDE selection process detailed only in an unretrieved supplement; diagnosis source for ABIDE subset not independently restated; whole-thalamus (not nuclei-specific) seeds used due to low-resolution imaging. | Demonstrates use of ABIDE as an independent validation cohort for an associational finding originating in a non-ABIDE sample, with explicit site-covariate handling and motion QC thresholds applied to the ABIDE subset. |  |
| S-008 | Group-difference (associational) voxel-wise R-fMRI study; ABIDE I+II discovery sample, N=1019 (82 F ASD, 362 M ASD, 166 NT F, 409 NT M) across 13 merged sites; replicated in EU-AIMS LEAP and GENDAAR. | Custom R-fMRI preprocessing (slice-timing, motion regression, CompCor, band-pass filter, BBR+ANTs registration) with ComBat site harmonisation; five metrics (PCC-iFC, VMHC, ReHo, DC, fALFF) analysed via voxel-wise GLM with diagnosis, sex and their interaction as regressors, age and mFD as covariates. | Main effects of diagnosis and sex converged on the default-network midline across PCC-iFC, ReHo and VMHC; a sex-by-diagnosis interaction on VMHC in dorsolateral occipital cortex (reduced VMHC in autistic females) replicated in EU-AIMS LEAP but not GENDAAR. | Lack of a priori harmonisation among discovery and replication datasets; diagnosis-confirmation method not restated in main text; replicability varied by metric and sample. | Large, methodologically transparent use of combined ABIDE I+II data with explicit QC thresholds, ComBat site harmonisation, and independent-sample replication — a strong example of reconstructible cohort definition. |  |
| S-011 | Diagnostic prediction study; ABIDE I+II, final N=297 (151 ASD, 146 TD) from 4 sites (NYU, PITT, USM, TCD), reduced to N=290 (145/145) after propensity-score matching on age, sex and site. | Rs-fMRI preprocessed with C-PAC (Preprocessed Connectomes Project); functional connectivity via a 100-region Schaefer-Yeo atlas; ASD vs TD classification under contiguous/diverse/random training-stratum sampling schemes with 10-fold CV, evaluated within- and out-of-distribution; linear-regression and ComBat deconfounding tested. | Prediction accuracy (AUC, F1) and extracted-pattern stability declined as participant diversity increased in ABIDE (opposite direction to HBN); deconfounding only partially reduced this diversity-performance relationship. | Propensity-score and deconfounding computations used the full sample rather than training-fold-only data, a leakage concern flagged by the authors; negligible female representation in ABIDE (<0.02%) limited sex-related analysis. | Directly interrogates how ABIDE's site/demographic composition (diversity) affects reproducibility of predictive findings; open code and data make the analysed cohort reconstructible; illustrates a leakage pattern (full-sample deconfounding) relevant to RQ4/CL5 across the corpus. |  |
| S-012 | Group-difference (associational) discovery + independent validation; ABIDE I discovery N=708 (432 TD, 276 ASD), ABIDE II validation N=585 (316 TD, 269 ASD, 11 sites). | Athena-pipeline-preprocessed rs-fMRI; FD-based motion scrubbing with >5%-removed exclusion rule; cortico-cerebellar connectivity via linear regression of 65 cortical ROIs against cerebellar PCs, with site as a covariate; FDR correction across tests. | Five ROIs showed reduced (hypo-) cortico-cerebellar connectivity in ASD in ABIDE I; three (right fusiform gyrus, right superior temporal gyrus, left middle temporal gyrus) replicated in the independent ABIDE II sample. | Incomplete cerebellar coverage in some individuals (particularly posterior cerebellum); diagnosis-source instrument not independently restated; no atlas-based parcellation named. | A clean discovery/validation example using both ABIDE I and ABIDE II with transparent QC and site-covariate handling, illustrating cross-release replication of an associational finding. |  |
| S-014 | Diagnostic prediction (deep ensemble); ABIDE I CPAC data, N=1035 (505 ASD, 530 TC) from 17 sites; NYU subset N=175 (78 ASD, 104 TC); self-selected 'proposed subset' N=645. | Functional connectivity computed via CPAC pipeline across three atlases (AAL, CC200, EZ), F-score feature selection, and a stacked sparse denoising autoencoder + MLP ensemble with demographic features, fused by weighted voting; evaluated with 10-fold cross-validation. | 75.20% accuracy on the whole ABIDE I dataset (SOTA, +4.4 points over prior best); 88.71% on a selector-defined 'proposed subset'; 96.40% on the NYU site subset. | F-score feature selection described as using the whole dataset rather than training folds only; the 'proposed subset' is defined by the selector model's own correct classifications, a circularity that inflates its reported accuracy; no site harmonisation or leave-site-out evaluation; diagnosis-source instrument not independently restated. | A fully reproducible (code-released), multi-atlas ABIDE I predictive study illustrating both best practice (open code, multiple atlases, demographic fusion) and a clear leakage pattern (selector-defined subset) relevant to the review's Analysis-domain checklist. |  |
| S-029 | Diagnostic prediction / methodological tutorial; ABIDE, N=154 (77 ASD, 77 TD), balanced and matched per site. | SPM12/DARTEL-preprocessed rs-fMRI; 200-ROI Craddock-atlas connectivity (19,900 features); six classifiers (LR, LassoLR, SVM, PNN, LDA, GNB) compared via nested 10x10-fold cross-validation with train-only feature selection and standardization. | Best out-of-the-box accuracy 63% (linear SVM), improving to 68% with per-site train-only standardization; a simulation shows incorrect whole-dataset feature selection can inflate accuracy to 91%, illustrating the 'peeking'/double-dipping pitfall. | Diagnosis-source instrument not independently restated; leave-one-site-out CV discussed but not reported as the authors' own executed analysis; relatively modest sample size (N=154). | A rare positive methodological exemplar in this corpus: explicitly demonstrates and guards against the leakage patterns (whole-dataset feature selection/standardization) that affect several other ABIDE predictive papers in this review. |  |
| S-032 | Diagnostic prediction (MHPC ensemble); ABIDE, N=1111 (573 controls, 538 ASD) from 17 institutions, split into 889 training / 222 hold-out test subjects. | SPM8-based preprocessing; 3D-HOG voxel-texture features from functional and/or structural MRI combined with personal characteristic data; MRMR feature selection and classifier/hyperparameter tuning via training-set cross-validation; single evaluation on a held-out test set. | Best ABIDE accuracy 65.0% (functional MRI + personal characteristics) vs 51.6% baseline, exceeding functional MRI alone (59.2%), structural MRI alone (60.1%) and PCD alone (59.6%). | No connectivity atlas/parcellation used; site of imaging used as a raw feature rather than harmonised; no specific motion-metric threshold reported. | A clear example of hold-out-set discipline (feature selection/tuning strictly on training data) for ABIDE predictive modelling, though site handling via raw feature inclusion is methodologically distinct from harmonisation or leave-site-out approaches used elsewhere in this corpus. |  |
| S-041 | Group-difference (associational) voxel-wise analysis; ABIDE I, N=975 (458 ASD, 517 TDC) after site/IQ/coverage-based exclusions from 1112 raw datasets. | SPM8-preprocessed rs-fMRI; whole-brain voxel-wise functional connectivity density (global, inter-hemispheric/contralateral, intra-hemispheric/ipsilateral) with a 2-tailed t-test (age, sex covariates), FDR-corrected P<0.05, 20-voxel minimum cluster size. | Decreased inter- and intra-hemispheric FCD in ASD vs TDC in posterior cingulate cortex, lingual/parahippocampal gyrus, and postcentral gyrus; ADOS-RRB negatively correlated with FCD in these and default-mode-network regions. | No motion-based subject-exclusion threshold reported; no site covariate or harmonisation despite pooling multiple sites; no atlas-based parcellation. | A voxel-wise (non-atlas) associational use of ABIDE I illustrating a common gap in this corpus: multi-site pooling without explicit site-effect statistical handling. |  |
| S-043 | Group-difference (associational) study; original non-ABIDE cohort (21 ASD/24 TD, Japan) plus an ABIDE II replication cohort of 42 ASD / 88 TD boys drawn from 5 sites (GU, KKI, NYU_1, NYU_2 [excluded], SDSU) | Seed-based ROI-to-ROI resting-state functional connectivity from cerebellar subregions (Diedrichsen probabilistic atlas) to cerebral cortex, using CONN toolbox/SPM12 preprocessing; two-sample t-tests with FD, FSIQ and site as covariates, FDR-corrected (original) / Bonferroni-corrected (replication) thresholds | 12 cerebellar-cerebral FC group differences found in the original dataset (mixed increased/decreased); one (right dentate nucleus-left IPL decreased FC, p=0.039) replicated significantly in ABIDE II; FC values correlated with motor, executive and socio-communicative measures in the original dataset | Small original sample; only partial replication in ABIDE II (1/12 findings surviving correction); no code or participant-list release found | Demonstrates use of a specific ABIDE II site/criteria subset purely as an independent replication sample for an externally-derived finding, with exact numeric selection rules reported. |  |
| S-053 | Diagnostic prediction study; ABIDE I, 1035 subjects (505 ASD, 530 HC), pooled across all contributing sites | CPAC-preprocessed resting-state functional connectivity (Harvard-Oxford atlas, 110 ROIs) classified with a novel graph attention network (GAT2) within a graph-learning-and-interpreting framework (GAT-LI); compared against SVM, RF, MLP, CNN and other GNN baselines using fivefold cross-validation | GAT2 achieved the best classification performance among compared models (accuracy 68.02%, sensitivity 74.06%, F1 69.31%, MCC 0.3426 with the HO atlas); GNNExplainer-based interpretation identified a set of discriminative functional connections, 3 of which showed uncorrected group differences (p<0.05) | No leave-site-out or site-covariate evaluation despite multi-site data; no motion/QC rule reported for the analysed subset; post-hoc connection-level tests uncorrected for multiple comparisons | Full ABIDE I 1035-subject PCP release used with CPAC/HO atlas; code and data source publicly linked, supporting reconstructibility of the pipeline though not an explicit subject-selection rule. |  |
| S-054 | Diagnostic prediction study; ABIDE I, NYU site only, 184 subjects (79 ASD, 105 TC) | CCS-preprocessed (filt_global) resting-state fMRI 3D volumes converted into 2D slice images, classified with a modified Darknet-19 CNN (DarkASDNet) | DarkASDNet achieved accuracy 94.7%, precision 94.5%, recall 92.5%, F1-score 95%, AUC 94.703%, reported as outperforming VGG16, MobileNetV2, SVM and several literature benchmarks on the NYU subset | No train/test split or cross-validation methodology described; single-site analysis limits generalisability; data available only on author request, no code repository found | Single-site (NYU) ABIDE-I subset with an explicit N and phenotype table, but the prediction pipeline lacks a stated validation scheme, limiting confidence in the reported accuracy. |  |
| S-058 | Diagnostic prediction study; ABIDE-I single-site cohorts (NYU 184, UM 110 subjects) and a multi-site cohort (19 sites, 1100 subjects) | C-PAC-preprocessed raw 4D resting-state fMRI volumes (4mm MNI) classified end-to-end with a hybrid 3D CNN + bidirectional 3D convolutional LSTM, evaluated with 5-fold cross-validation and compared against several published deep-learning ABIDE classifiers | 3DCNN C-LSTM achieved state-of-the-art single-site performance (NYU F1 0.78, UM F1 0.70), surpassing prior methods by 8-10%, but performance degraded substantially on the pooled multi-site ABIDE-I evaluation (F1 0.53), attributed to scanner/acquisition heterogeneity | No leave-site-out evaluation despite multi-site heterogeneity being identified as the cause of degraded performance; no motion/QC rule or diagnostic-instrument description reported; no code or data-availability statement | Illustrates that an end-to-end raw-4D-volume classifier that performs well at single sites degrades sharply under multi-site heterogeneity when evaluated with ordinary (non-site-stratified) cross-validation. |  |
| S-059 | Diagnostic prediction study; ABIDE I single-site cohorts, NYU (184 subjects: 79 ASD, 105 NC, primary) and UM (secondary) | DPARSF-preprocessed resting-state fMRI, multi-scale functional connectivity networks built from AAL (116 ROIs) and CC200 (200 ROIs) atlases, classified with a multi-scale graph convolutional network (MGRL) with feature fusion; evaluated with a repeated random 80/10/10 split (100 repeats) | MGRL outperformed single-scale GCN and handcrafted-feature baselines on both sites (NYU accuracy 0.795, AUC 0.886; UM accuracy 0.762, AUC 0.867), with multi-scale atlas fusion improving performance by at least 3% over single-atlas GCNs | Restricted to single sites to avoid inter-site heterogeneity rather than modelling it; no leave-site-out or pooled multi-site evaluation; diagnostic instrument/criteria and motion QC threshold not described; data availability limited to a general statement with no code link | Demonstrates an atlas-fusion GCN approach validated with a repeated-split uncertainty estimate on two separate ABIDE single-site subsets, explicitly avoiding rather than addressing multi-site heterogeneity. |  |
| S-066 | Diagnostic prediction study; two ABIDE I-derived multimodal benchmarks, ABIDE A (871 subjects: 403 ASD, 468 TC) and ABIDE B (949 subjects: 419 ASD, 530 TC) | C-PAC-preprocessed resting-state fMRI connectivity (CC200/AAL/Dosenbach160 atlases) combined with phenotypic and QC modalities, classified with a multimodal adversarial-regularized graph learning model (DeepASD) using patient similarity graphs and a GNN classifier; evaluated with 10-fold stratified, non-overlapping cross-validation | DeepASD outperformed 8 state-of-the-art baselines (accuracy 87.38% / AUC 92.76% on ABIDE A; accuracy 88.09% / AUC 93.59% on ABIDE B), an improvement of 13.25% accuracy, 7.69% AUC-ROC and 17.10% specificity over the best baseline; ablation confirmed fMRI as the most informative single modality, with other modalities adding further gains | Diagnostic label source/instrument not elaborated; site is incorporated as a demographic feature for graph construction rather than evaluated with a leave-site-out scheme despite the known multi-site heterogeneity of ABIDE | Both cohorts are explicitly reconstructible by citation to previously published preprocessing protocols (Parisot 2017, Wang 2020), and both preprocessed datasets plus analysis code are released with the paper. |  |
| S-067 | Diagnostic prediction study; ABIDE I, 880 subjects (418 ASD, 478 TD) across 17 sites after excluding incomplete/missing data | CPAC-preprocessed resting-state functional connectivity (Harvard-Oxford atlas, 110 ROIs) used to learn non-linear high-order functional associations via an explainability-guided ROI-selection stacked-autoencoder framework (EAG-RS), evaluated with stratified five-fold cross-validation | EAG-RS achieved AUC 0.760, accuracy 73.71%, sensitivity 64.56%, specificity 80.74%, outperforming comparative state-of-the-art and feature-selection methods; selected ROIs were linked to previously reported ASD-relevant brain regions and subtypes | No site covariate, harmonisation, or leave-site-out evaluation despite the pooled 17-site cohort; diagnostic instrument/criteria not elaborated; the paper itself notes it does not incorporate other neuroimaging modalities or clinical information | Exact exclusion rule, pipeline, atlas and analysis code (GitHub) are all reported, supporting reconstructibility of the analysed cohort from the released ABIDE I data. |  |
| S-074 | Diagnostic prediction study; ABIDE I, 406 ASD and 476 TC subjects (DPARSF-preprocessed PCP subset) across 17 sites | DPARSF-preprocessed resting-state fMRI connectivity from three atlases (AAL, CC200, Dosenbach160) classified with a multi-atlas transformer (METAFormer) using self-supervised masked-value pretraining, evaluated with 10-fold stratified cross-validation and a separate validation split per fold | Pretrained METAFormer achieved accuracy 83.7%, AUC 0.832, outperforming non-pretrained and single-atlas variants as well as previously published ABIDE I classifiers using comparable cross-validation | No explanation given for the reduction from the full 1112-subject ABIDE I release to the 406/476 analysed subset; no site covariate, harmonisation, or leave-site-out evaluation despite the pooled 17-site cohort; diagnostic instrument/criteria not elaborated | Pipeline, atlases and analysis code (GitHub) are all reported, and the leakage-aware CV design (separate validation fold) is an explicit methodological strength noted in the paper itself. |  |
| S-098 | Group-difference (associational) / methods-comparison study; ABIDE I, 850 subjects (355 ASD, 495 HC) from multiple sites | CCS-preprocessed resting-state functional connectivity (CC200 atlas, Fisher z-transformed), compared across three site-effect mitigation strategies (GLM, ComBat, and the proposed site-wise de-meaning) using Hedge's g effect size on a literature-anchored ASD finding (anterior-posterior DMN hypoconnectivity) | Site-wise de-meaning (SWD) improved ASD-vs-control effect size by 2.9-5.3% relative to uncorrected data, while GLM and ComBat reduced it by up to 11.4% and 7.5% respectively, indicating SWD better preserves disorder-related connectivity signal under multi-site harmonisation | Evaluation restricted to specific literature-selected ROI pairs rather than a whole-brain corrected analysis; no code repository identified beyond the public ABIDE data link | Directly addresses RQ on site handling (CL6) with a quantitative comparison of three site-effect mitigation strategies applied to ABIDE I resting-state connectivity. |  |
| S-006 | Diagnostic prediction (3D CNN) using ABIDE-I (10-fold CV training set, n=774: 379 ASD/395 TD, 17 sites) and ABIDE-II (independent held-out test, n=393: 163 ASD/230 TD, sites overlapping ABIDE-I). | CPAC/PCP-preprocessed connectivity fingerprints across seven atlases fed into a volumetric 3D CNN; compared against ridge regression, linear SVM, and fully-connected DNN baselines; evaluated via 10-fold CV on ABIDE-I and an independent held-out test on ABIDE-II. | 3D-CNN atlas-ensemble reached 73.3% CV accuracy (ABIDE-I) and 71.7% independent test accuracy (ABIDE-II), AUC 75.8% on the ABIDE-II test, outperforming all baselines and a prior ABIDE-I benchmark of up to 67%. | No code/participant-list availability statement; baseline hyperparameters tuned by maximising CV accuracy (acknowledged optimistic); no explicit site covariate/harmonisation; ABIDE-II test sites overlap with ABIDE-I training sites rather than being fully held out; diagnostic label source not described. | Demonstrates volumetric 3D-CNN classification with atlas-ensemble voting, trained on ABIDE-I and externally validated on an independent ABIDE-II cohort; a cross-release external-validation example linking the two ABIDE phases. |  |
| S-010 | Diagnostic prediction trained on the IMPAC dataset (n=915) and externally validated on ABIDE I (n=1045, all sites) and ABIDE II (n=761, all sites), restricted to subjects with a paired same-visit sMRI+rsfMRI scan. | fconn1000-derived functional connectivity (tangent-space embedding across seven atlases) plus FreeSurfer structural features; 12 ML model types trained/optimised on IMPAC only; ABIDE I/II used as untouched external test sets, with a secondary supervised-domain-adaptation analysis (10-fold CV). | Best IMPAC model: 80.4% AUROC (IMPAC); 86.0% AUROC (ABIDE I) and 79.2% AUROC (ABIDE II) without adaptation; 93.2%/90.5% after supervised domain adaptation. Cerebellar connectivity identified as a reproducible discriminative feature. | Exact per-diagnosis Ns for ABIDE are not reported (percentages only); no motion/QC rule or site harmonisation reported for the ABIDE external-validation cohort; diagnostic label source not described. | A strong example of cross-dataset external validation (IMPAC-trained, ABIDE-tested) with openly released code, pipeline and model weights, directly linking the ABIDE releases to an independently trained predictive model. |  |
| S-020 | Diagnostic prediction (federated learning) using ABIDE I resting-state fMRI from four sites: NYU (n=167: 73 ASD/94 HC), UM1 (n=88: 43/45), USM (n=52: 33/19), UCLA1 (n=63: 37/26). | CPAC-preprocessed ROI time series (Harvard-Oxford atlas, 0.01-0.1Hz band-pass, no GSR; CC200 atlas as replication) fed into MLP classifiers trained under a privacy-preserving federated-learning framework, with two domain-adaptation extensions (MoE, adversarial alignment); compared against single-site, cross-site, ensemble and pooled (Mix) training via 5-fold CV. | Federated learning (Fed) outperformed single-site and best cross-site training at every site (accuracy 0.647-0.849 across sites, HO atlas) and approached pooled (Mix) accuracy without centralising data; domain adaptation further improved accuracy at most sites; results replicated (at lower absolute accuracy) with the CC200 atlas. | No motion/FD-based QC rule or statistical site harmonisation (e.g. ComBat) reported; diagnostic label source not described; no code/participant-list availability statement; class balance (ASD%) varies by site (44-63%) without an explicit correction. | Demonstrates that privacy-preserving federated learning across four ABIDE I sites can approach the accuracy of pooled multi-site training without data sharing, directly relevant to the dataset's distributed, multi-site structure. |  |
| S-022 | Diagnostic prediction (1D CNN) using ABIDE I resting-state fMRI (1,112 subjects, 539 ASD/573 TD, 17 sites), reduced to 871 subjects after CPAC preprocessing QC (a separate statement reports 505 ASD/530 TD as the dataset used). | CPAC/PCP-preprocessed functional connectivity (CC400 atlas) fed into a 1D CNN; compared against optimised SVM, KNN and Random Forest; evaluated via 10-fold CV and a leave-site-out scheme across all 17 sites. | CNN achieved 70.22% 10-fold CV accuracy, outperforming SVM (69%), KNN (62%) and RF (60%); leave-site-out accuracy varied by site, exceeding 70% at KKI, SDSU and USM. | Exact ASD/TD split of the final 871-subject analysed sample not stated; no numeric motion/FD cut-off given; data available only on request, not openly released; within-fold leakage control for hyperparameter tuning not described. | Combines a standard pooled 10-fold CV evaluation with an explicit leave-site-out analysis across all 17 ABIDE I sites, making site-level generalisation directly reportable for the dataset-publication link. |  |
| S-023 | Diagnostic prediction (SVM on combined structural-texture and functional-ICA features) using ABIDE I (1111 scans, 573 HC/538 ASD, 17 sites), split 800 training / 311 hold-out test (case:control ratio preserved). | SPM8-preprocessed structural and resting-state fMRI; structural texture features from a sparse-autoencoder convolutional model and functional features from subject-level spatial ICA time courses, combined via linear SVM (LEFMSF); 5-fold CV for hyperparameter tuning within the training set, evaluated on an untouched hold-out set; explicit site-confound checks. | LEFMSF achieved 0.643 hold-out accuracy on ABIDE (specificity 0.683, sensitivity 0.600), the best known result using imaging data alone at publication, exceeding prior work by 0.042; a site-only baseline classifier scored only 55.0% and a site-balanced re-test gave 63.46%, arguing against a site-driven result. | No named ROI atlas/standard connectivity pipeline (features are ICA/texture-based); no motion/FD-based QC rule reported; diagnostic label source not described; exact ASD/TD counts within the hold-out test set not individually reported. | A methodologically careful example combining structural and functional ABIDE I features with an explicit, quantitative check that model performance is not driven by site identity, directly relevant to confound/leakage assessment in ABIDE-based prediction studies. |  |
| S-025 | Diagnostic prediction (deep transfer learning) using ABIDE I resting-state fMRI from four target sites (UM n=113: 48 ASD/65 healthy; UCLA n=75: 36/39; USM n=61: 38/23; LEUVEN n=61: 27/34), with offline SSAE pretraining on healthy subjects from the remaining 16 ABIDE sites. | CCS-preprocessed functional connectivity (AAL atlas, 90 ROIs) with site/age/gender/handedness regressed out via OLS; a stacked sparse autoencoder pretrained offline on non-target-site healthy subjects, transferred into a DTL-NN classifier and compared against DNN and SVM baselines via stratified 5-fold CV per site. | DTL-NN outperformed DNN and SVM at every site, with the best performance at USM (70.4% accuracy, 0.73 AUC) and an average of 67.1% accuracy/0.71 AUC across sites, significantly better than DNN for accuracy (p=0.03) and sensitivity (p=0.04). | No motion/FD-based QC threshold or pipeline version reported; diagnostic label source not described; no code/participant-list availability statement; small per-site sample sizes (61-113). | Demonstrates a transfer-learning design that explicitly separates offline pretraining data (non-target ABIDE sites) from target-site evaluation data, alongside an explicit site-covariate regression, both directly relevant to site-leakage assessment in ABIDE-based prediction studies. |  |
| S-026 | Group-difference (associational) analysis using ABIDE I resting-state fMRI (584 datasets: 278 ASD/306 TD, nine sites) as an independent replication of an original 15 ASD/15 TD task+resting-state sample. | Seed-based intrinsic functional connectivity of the right posterior superior temporal sulcus (pSTS), computed with the same in-house SPM-based procedure as the original sample; mean FD included as a nuisance covariate, with a motion-scrubbed secondary analysis; small-volume and whole-brain FWE-corrected statistics. | ABIDE replication confirmed reduced pSTS connectivity with right IPL, left premotor area, fusiform gyrus and bilateral superior occipital gyrus in ASD (replicating the original sample), plus increased pSTS connectivity with left thalamus and right IFG not seen in the original sample. | No named/versioned standard connectivity pipeline or atlas used for the ABIDE data (seed-based, in-house SPM procedure); no code/participant-list availability statement; cross-site IQ not matched. | An early (2013) example of using the full multi-site ABIDE release as an independent large-sample replication cohort for a seed-based connectivity finding from a small original sample, with an explicit motion (FD covariate + scrubbing) sensitivity analysis. |  |
| S-027 | Diagnostic prediction (ensemble SVM) using ABIDE I resting-state fMRI from subjects sharing one scan protocol, n=84 (45 ASD/39 TC) after excluding 23 subjects for excessive motion. | DPARSF-preprocessed functional connectivity (AAL atlas, 90 ROIs, 4,005 edges) plus graph-theory metrics, classified with a random cluster of 500 bootstrap/feature-subsampled SVMs (majority vote), evaluated on a single 70/30 train/test split. | The random SVM cluster achieved 96.15% test accuracy with an optimal 272-feature subset, far exceeding a single SVM; discriminative regions included inferior frontal gyrus, hippocampus, precuneus and cingulate gyrus. | Headline accuracy is derived from a single train/test split in which both the ensemble size and the feature-set dimensionality were tuned by maximising accuracy on that same test set, with no cross-validation or independent validation set; diagnostic label source not described; no code/participant-list availability statement; small, single-protocol sample. | A cautionary example for the review: the very high reported accuracy (96.15%) on a small single-protocol ABIDE subset is attributable to test-set leakage during hyperparameter/feature-set selection rather than independently validated generalisation performance. |  |
| S-030 | Diagnostic prediction (3D-CNN on voxel-wise rs-fMRI summary measures) using combined ABIDE I+II (N=2,085 after a minimum scan-duration QC cutoff; 993 ASD, 1,092 TD; 29 institutions). | C-PAC-preprocessed voxel-wise temporal summary measures (ReHo, ALFF, fALFF, degree/eigenvector centrality, LFCD, entropy, VMHC, autocorrelation lag) fed into per-measure and ensemble/combined 3D-CNN models and linear-SVM equivalents; evaluated via five-fold CV and a separate leave-site-out CV across the five largest sites. | Best model (MM-ensemble) reached 64% balanced accuracy/66% F1 under five-fold CV, comparable to the single ReHo measure, but dropped to 56% balanced accuracy/59% F1 under leave-site-out CV, generalising well only to the NYU site. | No motion/FD-based QC threshold reported (only a scan-duration cutoff); no atlas/ROI parcellation used; diagnostic label source not described; large drop in performance under leave-site-out evaluation indicates limited cross-site generalisation. | A methodologically strong example directly quantifying the gap between pooled cross-validation and leave-site-out generalisation on combined ABIDE I+II, with openly released code, highly relevant to assessing site-generalisation claims in ABIDE-based prediction studies. |  |
| S-033 | Diagnostic prediction (SVM on graph-theoretical features) using ABIDE I resting-state fMRI, 816 individuals across 22 sites, stratified into five age groups (exact ASD/HC split reported only in a supplementary table). | CPAC/PCP-preprocessed functional connectivity (AAL atlas, 116 ROIs; multiple connectivity measures) summarised into 817 graph-theoretical features, reduced to 10 via sequential feature selection and classified with a linear SVM per age group; evaluated via 10-fold CV with 10x10 Welch's t-test model comparisons (FDR-corrected). | Best model (>30 years age group) achieved ~95% accuracy, 97% sensitivity, 95% specificity; centrality measures were the most consistently informative features across age groups. | ASD/HC split not available in the extracted full text (only in a supplementary table); no numeric motion/FD threshold reported; unclear whether feature selection was confined to training folds; no site covariate/harmonisation across the pooled multi-site sample; data available only on request, not openly deposited. | An age-stratified ABIDE I analysis demonstrating that graph-theoretical centrality features combined with careful overfitting controls (linear kernel, few features, 10-fold CV) can achieve high accuracy in an older-age ASD subgroup, though feature-selection leakage risk is not fully resolved by the reported methods. |  |
| S-034 | Diagnostic prediction (ASD vs TC); ABIDE I preprocessed-connectomes-project release; 872 of 1112 subjects, 20 sites | C-PAC-preprocessed rs-fMRI parcellated with Harvard-Oxford atlas (111 ROIs); population-graph convolutional neural network ensemble (bootstrapped G-CNN) trained with edge dropout and compared against a single G-CNN and linear SVM baseline; 10-fold cross-validation matching a prior study's splits and code. | Bootstrapped G-CNN reached 70.86% accuracy (graph condition), outperforming the baseline G-CNN (69.50%) and linear SVM (66.8%), with improved robustness (67.85%/67.39%) under naive or noisy population graphs versus baseline (66.93%/66.35%). | No stated motion/QC threshold, no diagnosis-source statement, no leakage or site-handling description, single-split accuracy without confidence intervals. | Demonstrates a predictive, ABIDE-I-only, CPAC/Harvard-Oxford population-graph classification approach; cohort subset is a fixed N (872/1112) without a published selection rule. |  |
| S-039 | Group-difference (associational) mega-analysis; ABIDE I (369 autism/481 NT) and ABIDE II (205 autism/347 NT) combined with EU-AIMS LEAP (222/200) for a total of 796 autism/1028 NT across 32 sites | Pearson-correlation connectomes from Schaefer-400 cortical + 15 Harvard-Oxford subcortical ROIs; ComBat site harmonisation; per-edge GLM with diagnosis, age, sex, mean FD covariates assessed with the Network-Based Statistic at FWE-corrected thresholds; canonical correlation analysis linking connectivity to clinical symptom dimensions. | Autism showed brain-wide hypoconnectivity (13,001 edges, 17.1% of edges, pfwe<0.001), concentrated in sensory/somatomotor/attention networks, and hyperconnectivity (16,767 edges, 22% of edges, pfwe<0.001), concentrated in DMN/subcortical connections; pattern replicated separately in LEAP and in combined ABIDE I/II data. | Preprocessing pipeline name/version and exact exclusion criteria are deferred to a supplement not present in the extracted full text; analysis excluded the cerebellum due to poor scan coverage; most participants under 25 years old; sex ratio imbalanced between groups. | A large multi-site mega-analysis explicitly reporting ABIDE I and ABIDE II subsample sizes separately and replicating its connectome-wide findings within the combined ABIDE I/II data alone. |  |
| S-049 | Diagnostic prediction (ASD vs HC); ABIDE used as a secondary validation dataset alongside ADNI; release, N and sites not reported in available text | Diffusion-based generative brain-network construction (Brain Region Alignment Module, a DDPM-based registration network) combined with a graph-contrastive Brain Network Optimization Module (GCN-based), compared against brain networks built with the PANDA toolbox; five-fold cross-validation stated generically for the model. | ROI attention scores identified somatomotor network (SMN) connectivity and DMN-DAN/DMN-FPN connectivity as most important for ASD prediction; on ABIDE the proposed method's constructed networks had higher reliability (ICC 0.71 vs 0.64) and much lower construction time than PANDA; no numeric ASD classification accuracy/AUC table is present in the extracted text. | ABIDE cohort N, sites, release, diagnosis source, preprocessing pipeline and atlas are not reported; no quantitative ASD classification performance table (unlike the detailed ADNI 5-fold results in Table 5); authors note the model cannot explain pathogenesis and the dataset used is relatively small. | Illustrates a predictive deep-learning paper where ABIDE is a secondary, thinly-documented validation dataset; useful as a negative example for cohort/pipeline reporting completeness in the knowledge graph. |  |
| S-052 | Diagnostic prediction (ASD vs TC); ABIDE Preprocessed Connectomes Project release (ABIDE I), 506 ASD/548 TC across 17 sites | C-PAC-preprocessed rs-fMRI parcellated with the CC200 atlas; an Extra-Trees attention mechanism selected the top 1935 connectivity features, classified with a linear SVM; evaluated with pooled 10-fold cross-validation (nested CV for hyperparameters) and a supplementary intra-site stratified shuffle-split cross-validation. | 72.2% accuracy (68.6-68.8% sensitivity, 75.4% specificity) in pooled 10-fold CV, versus 67.7% mean accuracy (66.3% sensitivity, 68.9% specificity) under the intra-site evaluation; informative connections implicated social-cognition regions and reduced anterior-posterior DMN correlation in autism. | Exclusion rule limited to missing imaging data with no motion/QC threshold; diagnosis source not reported; feature selection appears to precede the cross-validation split, raising a leakage concern; pooled-CV accuracy exceeds the site-stratified accuracy, consistent with some site leakage. | A CC200/C-PAC predictive study with a clearly reported N and pipeline but an apparent feature-selection leakage gap and only a partial (non-leave-site-out) site-handling check. |  |
| S-060 | Diagnostic prediction (ASD vs NC); ABIDE-I, single NYU site only, 79 ASD / 105 NC (full ABIDE-I: 539 ASD/573 TC across 17 sites) | C-PAC-preprocessed rs-fMRI; group-ICA identified eight brain functional networks, subject-specific spatial maps via dual regression, classified with a modified 3-D VGG-Net with squeeze-and-excitation channel attention (MCSE-VGG); evaluated with 10-fold cross-validation. | MCSE-VGG achieved 77.74% accuracy (76.74% precision, 78.57% recall, F1 75.33%) versus a 69.58%-accuracy baseline; ASD showed hyperconnectivity between the salience network and DMN/central executive network and hypoconnectivity between precuneus and dorsal DMN, consistent with the under-connectivity hypothesis. | Single-site design chosen to avoid cross-site heterogeneity, so no cross-site generalization evidence; no separate validation dataset; ASD and NC groups differed significantly in age and IQ; no motion/QC threshold or leakage-control statement; no code/participant list released. | A well-documented single-site ABIDE-I predictive study illustrating a deliberate site-restriction strategy as an alternative to multi-site harmonisation. |  |
| S-075 | Associational, unsupervised-clustering correspondence analysis; ABIDE (consistent with ABIDE I), 7 sites, 454 subjects with complete phenotypic data (256 HC, 166 autism, 32 Asperger’s; PDD-NOS excluded) | rs-fMRI parcellated into 200 CC200 ROIs; static/dynamic functional and effective connectivity features selected via a genetic algorithm (compared against SFS and an in-house SFR method) to maximize similarity between connectivity-derived clusters (density peak clustering, OPTICS, hierarchical clustering) and clinical diagnosis or phenotypic groupings; no cross-validation during clustering. | For ASD, connectivity-based clusters matched the clinical diagnostic grouping better than the phenotypic grouping, with a peak similarity of 89.20% (GA feature selection, hierarchical clustering, 101 features, 3 clusters); no site-specific robustness check was possible for ASD because only one site had sufficient samples per group. | Preprocessing pipeline and motion/QC details deferred to an unavailable supplement; no site handling/leave-site-out evaluation for the pooled multi-site ASD analysis; no cross-validation, so similarity values reflect in-sample correspondence rather than held-out predictive performance. | Provides an ABIDE I cohort definition (454 subjects, 7 sites) and a connectivity-to-diagnosis correspondence finding (89.20% peak similarity) relevant to characterising how well unsupervised connectivity clusters recover clinical ASD groupings. |  |
| S-077 | Diagnostic prediction (ASD vs HC); ABIDE (consistent with ABIDE I), 871 of 1112 subjects (403 ASD, 468 HC) | C-PAC-preprocessed rs-fMRI parcellated with the Harvard-Oxford atlas; Fisher z-transformed Pearson connectivity, dimensionality-reduced via recursive feature elimination; a transductive population graph (nodes = imaging features, edges weighted by gender/age/acquisition site) classified with a proposed attention/skip-connection GCN (AN-GCN), evaluated with stratified 10-fold cross-validation against several GCN-based baselines. | AN-GCN achieved 96.91% accuracy and 96.86% AUC on ABIDE, far exceeding the strongest compared baseline (DS-MML, 87.62% accuracy, 92.00% AUC) and the basic GCN baseline (64.63% accuracy). | No diagnosis-source statement; feature elimination appears to precede the CV split; site/age/gender used directly as population-graph edge weights rather than controlled for, with no leave-site-out evaluation; the very high accuracy is substantially above the paper's own baselines and typical ABIDE benchmarks, suggesting possible leakage/inflation. | Illustrates a predictive, transductive population-graph GCN approach on ABIDE with a pipeline/atlas clearly reported but validation design raising leakage concerns given an unusually high accuracy. |  |
| S-002 | Diagnostic prediction; ABIDE I; 871 of 1112 participants (403 ASD, 468 TC) from 17 sites, after QA; subsamples of varying homogeneity also analysed (e.g. 736, 639, 420, 226 participants) | C-PAC-preprocessed ABIDE I data; systematic comparison of 6 atlas/parcellation methods x 3 connectivity measures x classifiers (SVC, ridge); leave-one-site-out and intra-site cross-validation with nested CV for hyperparameters and training-set-only ROI estimation | Best inter-site accuracy 66.8% (chance 53.7%) with MSDL atlas, tangent-space embedding, l2-regularized classifiers; accuracy increases with training sample size; discriminative connections implicate Default Mode Network, pareto-insular and semantic ROI networks | Diagnostic label source/criteria not detailed; heterogeneous site protocols; computationally very costly pipeline comparison (reported ~10 CPU-years without grid parallelization) | Methodological benchmark paper establishing which PCP/C-PAC pipeline + atlas + classifier choices work best on the full ABIDE I release, directly informing which pipeline/atlas combinations recur in later ABIDE classification work |  |
| S-019 | Diagnostic prediction; ABIDE I; 871 subjects (403 ASD, 468 controls) from 20 sites, same subset as Abraham et al. 2017 | C-PAC-preprocessed Harvard-Oxford ROI connectivity features; population graph with phenotypic (sex, site) edge weighting; spectral graph convolutional network with Chebyshev filters; feature selection via RFE/PCA/MLP/autoencoder compared; 10-fold stratified CV | Best result 70.4% accuracy / 0.75 AUC (K=4, phenotypic graph), exceeding ridge, random forest and MLP baselines; authors suggest ~70% may be an intrinsic ceiling for this heterogeneous dataset | CV is stratified by class, not by site, despite known inter-site heterogeneity; the GCN's transductive design includes test-node imaging/phenotypic features in the graph during training | A widely cited graph-based ABIDE classification method reusing the exact Abraham et al. 2017 cohort, pipeline and atlas, useful for linking methodological lineage within the dataset-publication graph |  |
| S-021 | Diagnostic prediction; ABIDE I; 964 subjects (447 autism, 517 typically developing) from 16 sites | Custom SPM8 preprocessing pipeline; whole-brain functional connectivity over a 7266-ROI gray-matter lattice; leave-one-subject-out classifier with age, age-squared, gender, handedness and site as covariates | Maximum 60% whole-brain classification accuracy, above chance but below the ~80% previously reported for single-site classification; most discriminative connections involved default mode network, parahippocampal/fusiform gyri, insula, Wernicke area, and intraparietal sulcus; classifier score correlated with symptom severity, social function, daily living skills and verbal IQ | Multisite heterogeneity substantially degrades classification accuracy relative to single-site results; accuracy was significantly higher for sites with longer BOLD scan durations | An early, influential multisite ABIDE I benchmark showing that cross-site connectivity classification underperforms single-site classification, motivating later work on pipeline/atlas choice and site-aware cross-validation |  |
| S-024 | Diagnostic prediction; ABIDE I; 871 subjects (403 ASD, 468 controls) from 20 sites | C-PAC-preprocessed Harvard-Oxford (110-ROI) connectivity graphs; siamese graph convolutional network learning a graph-distance metric from matching/non-matching subject pairs; k-nn (k=3) classification on learned distances compared to PCA/Euclidean distance | k-nn accuracy 62.9% across all sites with the learned GCN metric vs. 51.0% with PCA/Euclidean distance (11.9-point improvement); larger per-site improvements (e.g. site 18: 90.0% vs 50.0%); AUC improvements reported per site | Pair-based siamese training/testing with all 20 sites represented in both splits rather than held out; short conference format limits detail on diagnostic label source and on leakage control for pair construction | A graph-metric-learning method applied to the same well-characterised 871-subject ABIDE cohort used elsewhere in this corpus, useful for linking methodological lineage in the dataset-publication graph |  |
| S-036 | Diagnostic prediction; ABIDE I; 529 ASD and 573 typically developing individuals (1102 total) from 17 sites, each processed with four pipelines (CCS, C-PAC, DPARSF, NIAK) | A single-volume image generator converts each subject's whole-brain fMRI volume into glass-brain and stat-map images; CNN and VGG16-based deep ensemble classifiers evaluated with an 85%/15% train/test split, plus per-site (unit-site) classification | Unit-site classification accuracy up to 85% (glass-brain) and 84% (stat-map) for several sites; the third deep ensemble classifier configuration performed best across all four pipelines | Single random train/test split with no cross-validation; no leave-site-out evaluation for the pooled multi-site classifier despite known site heterogeneity | Provides a direct four-pipeline (CCS/C-PAC/DPARSF/NIAK) comparison on the same ABIDE cohort using a non-connectivity (whole-volume image) feature representation |  |
| S-038 | Associational (within-ASD symptom-severity correlation); ABIDE I; 27 ASD participants (no ABIDE controls) from 5 sites (CALTECH, CMU, PITT, UM_1, UM_2), used as a replication arm alongside a primary 13-ASD/13-control movie-watching fMRI sample | Custom FSL-based preprocessing with 24-parameter motion regression and framewise-displacement scrubbing; graph-theoretic subnetwork construction and scaled-inclusivity intersubject similarity; Mantel permutation test against ADI-R/ADOS score similarity | Ventro-temporal-limbic subnetwork intersubject similarity correlated significantly with ADI-R/ADOS symptom-severity similarity in the ABIDE replication cohort (p=0.0287, r=0.17), reproducing the primary movie-watching finding | No ABIDE control group (diagnostic scores unavailable for controls), so the ABIDE arm tests a within-ASD correlation rather than a group difference; no site or age covariate adjustment reported for the pooled 5-site ABIDE sample | An unusually well-documented example of an ABIDE subset reconstructible from the paper alone (explicit 27-subject ID list and public filtering code), useful as a high-confidence node in the dataset-publication knowledge graph |  |
| S-044 | Group-difference (associational); ABIDE I; 507 male subjects (209 ASD, 298 controls) from 14 sites, FIQ- and motion-matched | SPM8/DPARSF preprocessing with AAL-atlas time series; Hidden Markov Model identifying 19 recurring whole-brain states; fractional occupancy, lifetime, interval-time and transition-probability statistics compared between groups with Bonferroni-corrected two-sample t-tests, with and without regressing out site and FIQ | ASD subjects showed significantly decreased fractional occupancy in HMM states 4, 8, 9, 10 and increased occupancy in states 2, 3, 14, 17 relative to controls; transition-map community structure differed between ASD-related and HC-related modules | Male-only sample limits generalisability; site effects addressed via subject matching and covariate regression rather than formal harmonisation (e.g. ComBat) | A dynamic (HMM-based) rather than static connectivity analysis of a well-documented, site-matched ABIDE I subset, with explicit motion/FIQ inclusion thresholds and site-interaction checks |  |
| S-045 | Group-difference (associational); ABIDE I; 55 ASD and 55 age-matched typical controls (apparently single-scanner/site cohort, 3T GE Signa) | Custom AFNI-based pipeline (3dWarpDrive motion correction, N27 atlas warping); voxelwise fractal dimension (Hurst exponent) computed over 240 TT_Daemon ROIs; Z-score thresholding and Pearson correlation with ADI-R/ADOS severity scores | Significantly decreased signal complexity (fractal dimension) in ASD in the amygdala (p=0.001), vermis (p=0.02), basal ganglia (p=0.01) and hippocampus (p=0.02); no regions showed significantly increased complexity in ASD; FD in several ROIs correlated with ADI-R/ADOS scores | Sex ratio differs between groups without reported adjustment; no standard motion-exclusion threshold or explicit multiple-comparisons correction reported; most ASD patients were medicated and not excluded | A non-standard (fractal-dimension) connectivity analysis method applied to an ABIDE subset, useful for linking methodological diversity within the dataset-publication knowledge graph |  |
| S-047 | Group-difference (associational); ABIDE I; 605 participants (304 ASD, 301 typically developing controls) from 7 of 16 sites (UM_1, UM_2, USM, NYU, UCLA_1, OLIN, PITT) with raw, uncorrected resting-state scans | SPM8 realignment used to extract 6 rigid-body head-motion parameters from raw resting-state scans; Gamma-distribution noise-to-signal ratio and shape/scale parameters computed for linear and angular micro-movement speed; non-parametric distributional comparisons across sites, age groups, comorbidity and medication subgroups | ASD participants show significantly excess noise-to-signal ratio and randomness in head micro-movements relative to controls, consistently across sites, worsening with comorbidity, lower IQ, and greater autism severity, and present regardless of medication status | Diagnostic instrument/criteria for ASD/CT labels not restated; explicit multiple-comparisons correction across the many site x age x medication subgroup tests not clearly described; medication dosage and treatment duration data unavailable | An unconventional ABIDE analysis that repurposes head-motion time series (typically treated as a nuisance to regress out) as the primary biological signal, with explicit, reconstructible per-site inclusion criteria and N |  |
| S-055 | Diagnostic prediction; ABIDE I; 452 adolescents (201 ASD, 251 neurotypical) from 17 sites (primary sample), plus a 130-subject adult generalization subsample (63 ASD, 67 NT) | C-PAC-preprocessed rs-fMRI BOLD signals over AAL90 ROIs combined with an anatomical k-nearest-neighbor brain graph; Graph Signal Processing (extended Fukunaga-Koontz transform) features classified via an interpretable decision tree; Leave-One-Out Cross-Validation with inner CV for hyperparameter tuning | Averaged test accuracy up to 74.8% (m=3), significantly outperforming a structural-only (SFM) baseline and a functional-only (GFT) baseline; predictive markers implicate frontal and temporal lobe regions; framework also generalizes to an independent adult subsample with up to a 15-point accuracy gap over SFM | No leave-site-out evaluation despite 17-site heterogeneity; diagnostic-instrument source not restated; 'structural' network is an anatomical-distance graph rather than a diffusion-derived structural connectome | Demonstrates that combining a geometric/anatomical brain graph with rs-fMRI graph-signal features improves interpretable ASD classification over single-modality baselines on a well-specified ABIDE I adolescent subset |  |
| S-056 | Diagnostic prediction; ABIDE I+II full releases, 539/573 (ASD/TD) and 521/573 (ASD/TD) respectively, ages 5-64, sites not itemised. | 3D NIfTI volumes converted to 2D axial-plane image slices (MRIcron) and classified with pre-trained CNNs (VGG-16, ResNet-50) using a single train/test split. | ResNet-50 achieved 87.0% test accuracy (best model); VGG-16 achieved 63.4%; evaluated with accuracy, recall and precision. | No motion/QC rule, no connectivity pipeline or atlas, no cross-validation or site handling, and no participant-list/code availability statement. | Demonstrates ABIDE I+II used as raw image data for a non-connectivity CNN classifier; cohort cannot be reconstructed beyond the aggregate N reported. |  |
| S-062 | Both (group-difference + diagnostic prediction); ABIDE I subset of 190 male children (102 ASD, 88 TD), ages 6.5-13, from KKI, NYU, UCLA and UM. | CPAC-preprocessed rs-fMRI; functional connectivity under AAL, HO, CC and Power atlases; permutation testing for group differences; linear-SVM classification with leave-one-site-out cross-validation. | Best atlas (HO): leave-one-site-out mean AUC 0.75±0.05, accuracy 0.71±0.06, best fold AUC 0.83; hyper-connectivity in ASD between right angular gyrus-precuneus and right frontal operculum-left IFG, plus weaker connections elsewhere. | Restricted to male children at four sites; no study-specific participant list published; feature selection not attempted so no leakage-control procedure was needed or described in detail. | A methodologically thorough ABIDE I subset analysis combining connectivity group-difference findings with a properly site-cross-validated SVM classifier; selection rule is exact enough to approximate reconstruction but no ID list is given. |  |
| S-064 | Diagnostic prediction; ABIDE I, 505 ASD and 530 TC, post-QC total 1,035, split 623/308/104 train/validation/test, sites not itemised. | CPAC-preprocessed rs-fMRI; Pearson-correlation connectivity matrices from AAL, CC and EZ atlases; SSDAE+MLP hybrid deep-learning classifier with a modified Hiking Optimization Algorithm for feature selection. | Average accuracy 0.735, sensitivity 0.765, specificity 0.752 across the three atlas-based datasets; best per-atlas accuracy 83.82% (CC atlas). | Single fixed train/validation/test split with no cross-validation or site handling; no explicit leakage-control statement for feature selection/pre-training; no study-specific participant list or code. | Illustrates a deep-learning feature-selection approach on ABIDE I benchmarked against a prior published split strategy (Liu et al., 2024), but with limited reproducibility detail. |  |
| S-069 | Diagnostic prediction; ABIDE I, a commonly-cited 871-subject subset (403 ASD, 468 TC), sites not itemised. | BASC-atlas (scale 122) functional connectivity via Pearson correlation; RNN, BiRNN, LSTM, BiLSTM, CNN and CNN-hybrid classifiers evaluated with 10-fold cross-validation. | Best model (RNN): accuracy 74.74%, sensitivity 72.95%, specificity 76.28%, comparable to or better than several prior published results on the same subset (Table 3 comparison). | No preprocessing pipeline named, no motion/QC rule, pooled 10-fold CV with no site handling, no leakage-control statement, and no code or participant-list availability. | Uses the same widely-reused 871-subject ABIDE I subset as several prior studies, enabling direct accuracy comparison, but adds no new reproducibility information. |  |
| S-071 | Diagnostic prediction; all 1102 ABIDE I subjects from 17 sites, CPAC filter_noglobal preprocessing, no data screening applied, ASD/TD breakdown not in extractable text. | AAL (116 ROIs) and CC200 atlas functional connectivity; Low Rank and Class Discriminative Representation (LRCDR) domain-adaptation method with a linear SVM; leave-one-site-out inter-site cross-validation across all 17 sites. | Mean leave-one-site-out accuracy 73.1% (AAL) and 73.4% (CC200), outperforming compared domain-adaptation and multi-site ASD identification methods; top discriminative connections were mostly inter-network RSFCs. | No ASD/TD breakdown or QC/exclusion rule in the extractable text (explicitly no data screening applied); hyperparameter-search leakage control not described; no code or participant list, only supplementary material. | Demonstrates a domain-adaptation approach explicitly designed to handle ABIDE I site heterogeneity via leave-one-site-out evaluation on the full unscreened release. |  |
| S-072 | Both (group-difference + diagnostic prediction); ABIDE, four TR=2s sites (NYU, SDSU, UM, USM), 147 ASD and 146 healthy controls. | CPAC-preprocessed rs-fMRI; CC200 atlas sliding-window dynamic functional connectivity (node variability) and static node strength; SVM/RF/NB/MLP classifiers with intra-site 5-fold CV and inter-site leave-one-site-out evaluation. | ASD showed increased FC variability in regions of otherwise-low variability in controls; classification reached up to 65% accuracy (intra-site) and ~62% accuracy (inter-site leave-one-site-out, MLP). | No motion/QC threshold beyond a TR restriction; possible feature-selection leakage from choosing nodes by cross-site group differences; no code or participant-list availability. | An early dynamic-FC approach to ABIDE combining a group-difference finding with both pooled and leave-one-site-out classification evaluation. |  |
| S-076 | Diagnostic prediction; ABIDE I, a commonly-cited 871-subject subset (403 ASD, 468 HC) from 17 sites. | CPAC-preprocessed rs-fMRI; Harvard-Oxford atlas (111 ROIs) distance-correlation connectivity structured as a heterogeneous graph; heterogeneous graph convolutional attention network (HCAN) with MLP classification, evaluated with pooled 10-fold cross-validation and supplementary per-site 5-fold cross-validation. | Average ACC 82.9%, SEN 76.7%, SPE 86.6%, AUC 84.6% (10-fold CV), exceeding compared methods on the same 871-subject subset; per-site 5-fold CV mean ACC/SEN/SPE/AUC = 75.6%/72.6%/77.3%/83.0%, with performance varying notably by site (e.g. CMU n=11). | No specific motion/QC threshold; primary evaluation pools sites rather than leave-site-out; no leakage-control statement; no study-specific code or participant list. | A graph-neural-network approach on the widely-reused 871-subject ABIDE I subset, directly comparable to several prior published methods on the same subjects. |  |
| S-090 | Diagnostic prediction; ABIDE-I, 848 of the 1112-subject, 17-site release (396 ASD, 452 HC). | DPARSF-preprocessed rs-fMRI; AAL-atlas (116 ROI) functional connectivity; hierarchical functional-gradient-based graph network (ASD-HNet, ROI/community/global scales); pooled 10-fold cross-validation. | ASD-HNet achieved accuracy 73.57%, sensitivity 72.63%, specificity 74.90%, F1 71.04%, significantly outperforming eight compared methods (paired t-test p<0.05 each). | No explicit exclusion/QC rule or motion threshold for the 848-subject subset; pooled 10-fold CV with no site handling or stated leakage control. | Code is openly released, aiding reproducibility of the model though not of the exact cohort definition; benchmarked directly against several other ABIDE-I classification methods with matched or overlapping subsets. |  |
| S-091 | Both (biomarker group-difference derivation + ROC/AUC validation); ABIDE I+II (2095 subjects, 1001 ASD/1094 TD, 33 sites) for derivation, local KMUH cohort (21 ASD, 23 TD) for validation. | FSL-based lab-made pipeline; dual-regression functional connectivity against the Smith09 RSN10 template; FWE-corrected two-sample t-tests to derive 30 biomarker masks (R1-R10, A1-A20); ROC/AUC and FDR-corrected correlation analyses in the local cohort against SRS/SNAP-IV scores. | DMN and executive-control-network biomarkers differed significantly between ASD and TD; DMN connectivity was weaker in ASD; DMN-derived biomarker A4 reached AUC 0.745 in the local cohort, significantly outperforming its RSN-template-only counterpart (AUC 0.590); DMN biomarkers correlated negatively with SRS severity. | No age/sex/site covariate handling when pooling ABIDE I and II across 33 sites for the derivation step; no motion-exclusion threshold reported; underlying datasets available only on reasonable request (biomarker masks/pipeline are public). | A clear example of deriving a biomarker from the full ABIDE I+II release and testing its transfer to an independent, non-ABIDE clinical cohort, including an explicit ROC/AUC diagnostic-utility evaluation. |  |
| S-005 | Mega- and meta-analysis (associational) plus SVR prediction of SRS severity; ABIDE I+II, 939 participants (440 ASD/499 HC, all male), 18 sites | GRETNA-preprocessed rsfMRI, sliding-window dynamic connectomes (512-node random parcellation), multilayer-Louvain modular variability, GAM mega-analysis with ComBat site harmonisation and FDR correction, site-wise meta-analysis, SVR/LOOCV prediction of SRS scores, Allen Human Brain Atlas transcriptome association. | ASD showed higher mean / lower SD of whole-brain modular variability than HC; regionally higher variability in default-mode regions and lower in visual cortex (FDR p<.05); modular variability predicted SRS scores (r=.16, pperm=.002); alterations correlated with ASD-risk gene expression. | Male-only sample; gene expression reference from only 5 healthy post-mortem brains; medicated individuals not excluded; cross-sectional. | Detailed, numerically explicit ABIDE I+II QC pipeline (motion, scan length, IQ, age, site size) giving a reconstructible cohort definition; demonstrates site-harmonised mega-analysis plus leave-one-site-out sensitivity check as a model for site handling. |  |
| S-009 | Both associational (subtype vs TDC) and predictive (ADOS/SRS regression); ABIDE II discovery (229 ASD: 79 Asperger's/58 PDD-NOS/92 Autistic, 126 TDC, 9 sites) and ABIDE I replication (n=400, 17 sites) | SPM12 preprocessing, voxel-wise fALFF (functional) and GM volume (structural) maps, ADOS-guided MCCAR+jICA multimodal fusion, back-reconstruction for group differences, multiple linear regression cross-cohort prediction of ADOS/SRS, leave-one-site-out sensitivity analysis. | DLPFC and superior/middle temporal cortex are shared covarying regions across subtypes; each ASD subtype shows a unique subcortical fALFF alteration pattern linked to distinct ADOS subdomains; subtype-specific patterns predict symptoms only within the matching subtype when generalised from ABIDE II to ABIDE I. | Male-only sample, not generalisable to females or the general ASD population; voxel-wise fALFF rather than atlas-based connectivity; feature definition and prediction both drew on ABIDE II data before independent ABIDE I testing. | Demonstrates a discovery/replication design spanning ABIDE II and ABIDE I with explicit QC thresholds and code release (FIT toolbox), useful for cohort reconstructibility assessment; illustrates subtype-stratified (rather than binary ASD/TDC) analysis. |  |
| S-015 | Associational; ABIDE I+II, 37 sites, 710 ASD (79% male) / 606 CTL (87% male) after QC, ages 5-64 | C-PAC v1.8.0 preprocessing, fALFF and ReHo computed per voxel then parcellated into 11 Brodmann-area ROIs matched to post-mortem RNA-seq regions; site-mean correction; age/site/sex regressed out; Fisher r-to-z difference testing between ASD and CTL correlations, combined via Fisher's method, FDR-corrected. | 415 genes differentially correlated with fALFF/ReHo between ASD and controls (Diff Cor P<0.01, CTL FDR<0.05); effect size >1.8 for ~3% of expressed genes; developmental expression trajectories of these genes altered into adulthood. | Restricted to 11 cortical regions available from rare post-mortem ASD tissue; gene-expression comparison used a further random-subsampling procedure (e.g., ASD N=360 / Healthy N=302 in the depicted analysis) distinct from the full imaging QC sample. | Large, multi-site, well-documented ABIDE I+II QC and site-correction pipeline (CPAC, Brodmann atlas) linking imaging phenotypes to transcriptomic data; code publicly released. |  |
| S-016 | Diagnostic prediction; ABIDE I+II, 35 sites, 1383 males aged 5-40 (680 ASD/703 TD) | Freesurfer v6.0 structural morphometry (Desikan-Killiany-Tourville) and C-PAC functional connectivity (Harvard-Oxford, 103 regions), NeuroHarmonize site harmonization, deep-learning joint-fusion feature-reduction + classification network, nested 10-fold CV, SHAP feature importance. | Joint fusion AUC 0.78±0.04 outperformed structural-only (0.66±0.05, p<0.001 vs functional) and functional-only (0.76±0.04) models; top discriminative features in Default Mode Network and Social Brain regions. | Male-only sample; site harmonization (NeuroHarmonize) fit on the entire cohort prior to the nested CV split, risking leakage of test-fold information into the harmonization model. | Participant ID list published for reproducibility; demonstrates a multimodal structural+functional ABIDE classification pipeline with named atlases for both modalities. |  |
| S-028 | Diagnostic prediction; ABIDE-I, 17 sites, 1035 subjects (505 ASD/530 HC) | C-PAC-preprocessed CC200 functional connectivity, sparse autoencoder jointly trained with a two-layer softmax DNN classifier (ASD-SAENet); 10-fold CV on whole dataset and separate per-site 5-fold CV. | 70.8% accuracy and 79.1% specificity on the whole dataset (comparable to prior state-of-the-art but faster to train); outperformed comparators on 12/17 sites with 64.42% average per-site accuracy. | Cross-validation leakage control not explicitly described; no site harmonisation or leave-one-site-out test for the pooled model; per-site models limited by small site-level sample sizes. | Benchmarks a lightweight sparse-autoencoder classifier against prior ABIDE-I deep-learning baselines (ASD-DiagNet, Heinsfeld et al.) using the same C-PAC/CC200 preprocessing, with code released on GitHub. |  |
| S-063 | Diagnostic prediction; ABIDE I (ABIDE preprocessed), 539 ASD / 573 controls (1112 total) | CCS-pipeline ReHo derivative volumes (voxel-wise, no atlas) fed into a 3D CNN; 70/15/15 train/val/test split with early stopping and 10-fold cross-validation; multiple data-augmentation strategies (scaling, rotation, brightness, elastic deformation) compared. | Augmentation gave only minor test-accuracy improvements (0.6-2.2 percentage points depending on strategy/stopping rule); about half of augmentation strategies reduced accuracy; training accuracy >90% indicated overfitting. | No explicit motion/QC rule, no site handling, and authors note overfitting; absolute baseline accuracy values not stated numerically in text (only relative percentage-point changes and figures). | Uses the full ABIDE-I ABIDE-preprocessed release (CCS pipeline, ReHo) as a methodological testbed for augmentation rather than proposing a novel classifier; illustrates a predictive study with weak leakage/site-handling reporting. |  |
| S-070 | Diagnostic prediction; ABIDE I, 17 sites, 1112 initial subjects QC'd to 871 (403 ASD/468 TC) | CPAC-preprocessed raw 4D spatio-temporal fMRI (voxel-wise, downsampled to 28x28x28x32, no atlas) fed into a stacked small-kernel 3D-CNN + GRU network (CNNG); single 8:2 train/test split; compared against CNN-MLP, DiagNet, HI-GCN, GAT, SVC and an LSTM variant. | CNNG achieved 72.46% accuracy, 74.35% sensitivity, 79.25% specificity, AUC 0.79, outperforming all deep-learning comparators tested. | Single train/test split rather than cross-validation; qualitative (non-numeric) motion/QC exclusion; no site covariate, harmonisation or leave-one-site-out evaluation despite 17-site data. | Illustrative of voxel-wise spatio-temporal (non-atlas) deep-learning approaches to ABIDE classification, and of weak reporting on cross-validation/leakage/site handling relative to connectivity-matrix-based studies. |  |
| S-078 | Both associational (network detection) and predictive (SVM validation); single-site ABIDE I (University of Michigan), 48 ASD / 65 TC | C-PAC preprocessing, AAL atlas (90 ROIs), Pearson correlation + Fisher Z functional connectivity, a novel statistical graph network-detection/testing algorithm to identify abnormal subnetworks, SVM (RBF/linear) leave-one-out cross-validation using the detected subnetwork features. | Two abnormal connectivity subnetworks identified (middle temporal gyrus/precuneus; emotion/empathy-linked k-partite network); SVM classification using these features achieved 89% (RBF) and 84% (linear) leave-one-out accuracy. | Single ABIDE site only (acknowledged by authors as future work to extend to multiple sites/meta-analysis); classification features derived from full-sample network detection prior to cross-validation, risking leakage; no numeric motion-QC threshold reported. | Demonstrates a novel subnetwork-detection method on a well-characterised single ABIDE site, illustrating both an associational discovery step and a predictive validation step, useful as a methodological contrast to multi-site ABIDE classification studies. |  |
| S-080 | Group-difference (associational) analysis; ABIDE-I; n=211 males (103 ASD, 108 NT) from PITT, NYU, USM. | C-PAC-preprocessed rs-fMRI mapped to Conte69 cortical surface; vertex-wise functional connectivity combined with geodesic distance to derive connectivity distance (CD); ComBat site harmonization; vertex-wise t-tests with random field theory correction. | Widespread CD reductions in ASD vs NT concentrated in transmodal/paralimbic cortex, peak effect in the limbic intrinsic network (Cohen's d=-0.159); CD correlated positively with IQ but not age or ADOS severity. | Restricted to 3 of 17 ABIDE-I sites and to males only; cross-sectional; heterogeneity in autism limits generalizability (authors' own limitation). | Demonstrates a novel connectivity-distance (geodesic-weighted FC) derivative of ABIDE-I rs-fMRI, with explicit, reconstructible site/exclusion rules but no participant list. |  |
| S-081 | Diagnostic prediction demo; ABIDE I Preprocessed (full release), n=539 ASD / 573 controls. | Whole-brain grey-matter-masked voxel-wise ReHo features (C-PAC pipeline); scikit-learn logistic regression/SVM classifier; single random balanced split-half train/test division. | ~62% classification accuracy without dimensionality reduction or feature selection. | No cross-validation, no confidence interval, no site handling, no stated QC/exclusion rule; authors themselves frame this as a software prototype/proof-of-concept rather than a validated biomarker. | A Neurohackweek software-tool report demonstrating a reusable open classifier pipeline on the full public ABIDE I Preprocessed release. |  |
| S-082 | Group-difference (associational); ABIDE II, KKI site only; n=42 ASD / 127 TC (ages 8-13), after excluding 14 ASD/28 TC. | GRETNA v2.0.0 (SPM12) preprocessing; group ICA (GIFT) to identify 7 large-scale networks; 24 AAL-template ROIs; spectral DCM effective connectivity with PEB second-level group analysis. | ASD children showed decreased effective connectivity among VN, DMN, cerebellum, SMN and FPN vs TC; DMN(ANG_R)-to-SMN(PreCG_L) connectivity negatively correlated with ADOS stereotyped-behavior scores. | Single site (KKI); no quantitative motion threshold reported; diagnostic-label source not restated in the analysed sections. | Demonstrates effective-connectivity (spDCM/PEB) analysis of the KKI subset of ABIDE II with AAL-based ROI definition. |  |
| S-086 | Group-difference (associational), methods-illustration; ABIDE I, UCLA site only; n=41 ASD / 32 TC after motion exclusion. | Standard rs-fMRI preprocessing (slice-timing, motion correction, MNI registration, bandpass, smoothing); Pearson connectivity among first 90 AAL ROIs; novel empirical-Bayes local-fdr normalization applied before group comparison with fdr and NBS correction. | 44 connectivity features differed significantly (fdr q<0.1) between ASD and TC after normalization (none with raw correlations), all showing ASD hyper-connectivity across distant functional subsystems. | Single site; diagnostic criteria and motion threshold not quantitatively specified; paper's primary contribution is the statistical method, with the ABIDE analysis as one illustrative example. | Illustrates how a connectivity-normalization method changes group-difference detection on a single-site ABIDE I subset; relevant for methodological/processing comparisons in the knowledge graph rather than as a standalone clinical finding. |  |
| S-088 | Group-difference (associational), age-stratified; ABIDE I+II, all public sites; n=1,017 ASD / 1,127 TD. | Linear/angular head-motion speed extracted from rs-fMRI realignment parameters; bootstrapped resampling (100 subgroups of n=25); Gamma-distribution stochastic-signature analysis (NSR, MMS); Kruskal-Wallis pairwise age-group comparisons. | Involuntary head-motion statistics shift significantly with age in TD; ASD shows significantly different, non-uniform age-dependent shifts and overall elevated involuntary motor noise relative to age-matched TD. | Outcome is head-motion kinematics rather than functional connectivity; no named preprocessing pipeline for the underlying rs-fMRI; multiple-comparison correction across many pairwise tests not fully detailed; site pooled without explicit harmonisation. | Fully reconstructible cohort (participant indices uploaded to ABIDE, code on GitHub) spanning the whole public ABIDE I+II release, useful as a QC/motion covariate reference for other connectivity studies in the knowledge graph. |  |
| S-092 | Both (group-difference + predictive/regression); ABIDE-II, GU and KK sites; n=276 (85 ASD / 191 TD), ages 8-13. | FSL/AFNI preprocessing; Shen 268-node functional atlas; CPM with motion/site-masked edges; leave-one-out and split-half cross-validation with permutation testing for behavioral-regulation score prediction. | ASD scored significantly worse than TD on all BRIEF subscales; FC-based CPM significantly predicted inhibition (rs=.23) and, at trend level, shifting (rs=.19), but not emotion control, with distinct predictive network topographies for each subdomain. | Shifting model did not survive permutation testing at the conventional threshold; no formal site harmonisation (ComBat) or leave-site-out evaluation; no study-specific code/participant list release beyond the general CPM toolbox. | A rigorous two-site ABIDE-II CPM example combining explicit motion thresholds, a named atlas, and leakage-aware leave-one-out/permutation validation — useful methodological benchmark for the knowledge graph. |  |
| S-093 | Group-difference (associational); ABIDE-I; n=395 ASD / 425 TD (820 total) after QC exclusions from an initial N=1112. | CONN toolbox preprocessing; Schaefer 200-parcel atlas; Pearson FC; Forman-Ricci and Ollivier-Ricci graph curvature computed across 49 graph densities; two-sample t-tests with FDR correction. | ASD showed significantly lower average edge Forman-Ricci curvature than TD across most graph densities, with a similar but less consistent Ollivier-Ricci pattern; region-specific differences concentrated in Default Mode and Somatomotor networks, overlapping with NIBS (TMS/tDCS) target regions in the literature. | IQ not matched/excluded on (a deliberate choice for generalizability); diagnostic instrument not restated; no formal multi-site harmonisation. | A fully reconstructible, whole-ABIDE-I graph-curvature analysis with public FC matrices, networks and code — a strong candidate for cross-study replication in the knowledge graph. |  |
| S-094 | Group-difference (associational); multi-site ABIDE; n=85 ASD / 163 matched controls (N=248). | Custom FSL-based rs-fMRI preprocessing; Power 264-ROI/11-RSN atlas; PCA of FC matrices; wavelet-based temporal entropy; elastic-net (10-fold CV) regression of FC on RSN entropy, diagnosis-blind, compared post hoc between groups. | FC imbalance across 11 RSNs in ASD corresponded to a weaker FC-entropy relationship than controls; the diagnosis-blind entropy-model fit differed significantly between ASD and controls and correlated with ASD symptom severity. | No named/versioned preprocessing pipeline; no site covariate/harmonisation; diagnostic instrument not restated; no code/participant-list release found. | A methodologically detailed multi-site ABIDE example linking connectivity and temporal-entropy dynamics, using an elastic-net model as an associational (not diagnostic) tool. |  |
| S-096 | Diagnostic prediction; ABIDE I, 16 sites (CC200/CC400 C-PAC derivatives); n=505 ASD / 530 TDC (N=1035). | C-PAC-derived CC200/CC400 correlation matrices combined with topological features (persistence diagrams/images/landscapes); SVM, Random Forest, and hybrid NN classifiers; 5-fold stratified cross-validation with Monte-Carlo permutation significance testing. | Best accuracy 69.2% using a hybrid topological+correlation 3-layer NN; improvement from topological features over correlation alone was not always statistically significant. | No leave-site-out evaluation despite 16 pooled sites; no quantitative motion/QC threshold reported in this paper; no study-specific code/data release; authors themselves caution against overinterpreting topological-feature gains. | A self-critical benchmark of topological-data-analysis features for ABIDE ASD classification, useful as a cautionary methodological reference in the knowledge graph. |  |
| S-097 | Diagnostic prediction; ABIDE, 3 sites (CALTECH, CMU, KKI); n=41 ASD / 41 NC (N=82). | DPARSF preprocessing; AAL atlas (22 DMN ROIs); BOLD time series converted to wavelet scalogram images; pretrained CNN (DenseNet201/ResNet/GoogLeNet) feature extraction; SVM/KNN classification with k-fold cross-validation. | Best accuracy 85.9% (DenseNet201 + KNN), 86.5% with 10-fold cross-validation, exceeding cited prior ABIDE functional-connectivity classifiers (66.9-70.2%). | Small sample (N=82) from only 3 sites; no motion/QC threshold reported; no leave-site-out evaluation; no code/data release. | A DMN time-frequency/CNN-transfer-learning approach to ABIDE ASD classification, with a small, modest, non-reconstructible cohort. |  |
| S-099 | Diagnostic prediction; ABIDE-I, all 17 sites; n=505 ASD / 530 controls (N=1035) after removing subjects with missing information. | C-PAC-preprocessed data; AAL atlas (90 regions, 90x90 FC matrix); novel Teacher-Student deep-learning feature ranking plus Sequential Forward Feature Selection (SFFS); classifiers (LR, LD, SVM, RF, DT) evaluated with 10-fold (combined) and 5-fold (site-wise) cross-validation. | Maximum 82% 10-fold accuracy on the combined 17-site dataset (LR/LD), outperforming prior published ABIDE classifiers in the same comparison table, and outperforming state-of-the-art in 13/17 individual sites. | Feature selection (Teacher-Student + SFFS) appears performed prior to, rather than nested within, the reported cross-validation folds (potential leakage); all 17 sites pooled with explicitly ignored site variability and no leave-site-out evaluation; no motion/QC threshold or code/data release reported. | A full-ABIDE-I (17-site) classification benchmark illustrating a novel feature-selection method, useful for the knowledge graph's predictive-methods comparisons but with notable risk-of-bias caveats around leakage and site pooling. |  |

### 3.4 Synthesis

Computed by `phase3/s4_synthesis.py` from the charted records (quotes re-verified against each paper's full text). Counts are papers; only charted values are counted, and 'not reported' is reported. The corpus is the 99 open-access papers retrieved from 200 sought (see `out/review.md` for the PRISMA flow); this is a second-pass eligibility assessment over those reports, not a census of ABIDE papers.

#### In brief

- 74 of 99 papers analysed ABIDE resting-state data; 25 were excluded, almost all (21) because they used only structural or phenotypic ABIDE data.
- Most work is on ABIDE I alone (54 papers); 16 combine I and II; 4 use II alone.
- Prediction dominates: 46 predictive, 7 predictive plus group difference, 20 group difference only.
- Of 53 predictive papers, 26 use cross-validation that mixes sites in train and test folds; only 6 hold whole sites out. Median best accuracy is 73.3% under pooled CV (23 papers; 70.9% without the leakage-flagged ones) and 66.8% under leave-site-out (5 papers). These are different papers, models and subsets, so the gap is descriptive, not a controlled comparison. Two papers report both schemes with numbers for the same model: S-030 drops from 64% to 56% balanced accuracy when sites are held out; S-072 reports about 60% pooled and 62% leave-site-out.
- 8 predictive papers are flagged for leakage (feature selection, harmonisation or tuning using data outside the training folds).
- The analysed cohort can be rebuilt exactly for 17 papers (a published participant list for only 4), partly for 42, not at all for 15.
- The most reused subset is ABIDE I N = 871 (403 ASD / 468 TD): 9 papers, including Abraham et al. (S-002; NeuroImage 2017, corpus year 2016), Parisot et al. 2018 (S-019) and Ktena et al. 2017 (S-024).
- Leave-site-out also appears as a robustness check for group differences (S-005, S-009), which is why the site-handling table counts 8 papers with leave-site-out against 6 in the evaluation table.

#### Who got in

- Assessed for eligibility: **99**; included **74**, excluded **25**.
- Read in full text: 98; on abstract only: 1 (S-040 — the retrieved PDF is a different paper).

- Exclusion 3: structural/DTI/phenotype-only ABIDE use (no resting-state analysis): 21
- Exclusion 4: ABIDE used only for methods benchmarking, no autism-vs-control analysis: 4

#### Which release, which kind of claim

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

#### How prediction papers were evaluated

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

##### Leakage

PROBAST Analysis domain across the 53 predictive papers: High 25, Low 12, Unclear 12, no PROBAST Analysis domain charted 4.
Flagged for leakage (8): Analysis High *and* the charted reason is one of the specific patterns below. Other High ratings were for single splits without uncertainty, pooled CV ignoring site, or no stated validation — weaknesses, but not leakage by this rule.

- harmonisation/deconfounding outside CV: S-011, S-016
- feature selection outside CV: S-014, S-052, S-077, S-099
- tuning on the test set: S-027
- unsupervised feature derivation on full sample: S-060

#### Pipelines, atlases, site handling

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

#### Can the analysed cohort be rebuilt? (RQ6)

- Yes: 17 (23%) — of which a released participant list: 4; exact rules only: 13.
- Partly: 42 (57%).
- No: 15 (20%).

Code and/or participant list (CL7): yes 20, no 41, partly 13; code release mentioned in 18.

#### Papers analysing the same cohort

Grouped by identical release and charted N by diagnosis. The same N does not prove the same participants; it is the strongest signal the papers themselves give, since few publish a participant list.

##### ABIDE I, N = 871 (403 ASD / 468 TD) — 9 papers
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

##### ABIDE I, N = 1035 (505 ASD / 530 TD) — 6 papers
Pipelines: CPAC 6.

- S-014 Xuehan Liu 2024 — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder [CPAC; CC200, AAL, Eickhoff-Zilles (EZ); predictive; reconstructible: yes — exact rules]
- S-028 Fahad Almuqhim 2021 — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data [CPAC; CC200; predictive; reconstructible: no]
- S-053 Jinlong Hu 2021 — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification [CPAC; AAL, Harvard-Oxford; predictive; reconstructible: partly]
- S-064 Ibrahim Nafisah 2025 — Deep learning-based feature selection for detection of autism spectrum disorder [CPAC; AAL, Eickhoff-Zilles (EZ); predictive; reconstructible: no]
- S-096 Archit Rathore 2019 — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale [CPAC; CC200, CC400; predictive; reconstructible: partly]
- S-099 Naseer Ahmed Khan 2020 — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder [CPAC; AAL; predictive; reconstructible: partly]

##### ABIDE I, N = 184 (79 ASD / 105 TD) — 3 papers
Pipelines: CCS 1, DPARSF 1, CPAC 1.

- S-054 Md Shale Ahammed 2021 — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network [CCS; not reported / not applicable; predictive; reconstructible: partly]
- S-059 Ying Chu 2022 — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI [DPARSF; CC200, AAL; predictive; reconstructible: partly]
- S-060 Ming–Hsuan Yang 2021 — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model [CPAC; ICA / data-driven networks; predictive; reconstructible: no]

##### ABIDE I, N = 1112 (539 ASD / 573 TD) — 2 papers
Pipelines: CCS 1, CPAC 1.

- S-063 Johan Jönemo 2023 — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks [CCS; none (voxel/seed/vertex-wise); predictive; reconstructible: no]
- S-081 Swati Rane 2017 — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset [CPAC; none (voxel/seed/vertex-wise); predictive; reconstructible: partly]

##### ABIDE I, N = 1111 (538 ASD / 573 TD) — 2 papers
Pipelines: custom (SPM/FSL/AFNI/in-house) 2.

- S-023 Bhaskar Sen 2018 — A general prediction model for the detection of ADHD and Autism using structural and functional MRI [custom (SPM/FSL/AFNI/in-house); ICA / data-driven networks; predictive; reconstructible: yes — exact rules]
- S-032 Sina Ghiassian 2016 — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism [custom (SPM/FSL/AFNI/in-house); not reported / not applicable; predictive; reconstructible: partly]

##### ABIDE I, N = 1102 (529 ASD / 573 TD) — 2 papers
Pipelines: CPAC 2, DPARSF 1, CCS 1, NIAK 1.

- S-036 Md Rishad Ahmed 2020 — Single Volume Image Generator and Deep Learning-Based ASD Classification [CPAC, DPARSF, CCS, NIAK; not reported / not applicable; predictive; reconstructible: no]
- S-071 Xingdan Liu 2023 (total N only charted) — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study [CPAC; CC200, AAL; predictive; reconstructible: partly]



### 3.6 Risk of Bias Assessment (Items 18, 21)

Predictive papers (n=53) were appraised with PROBAST domains (Participants, Predictors, Outcome, Analysis); overall: High 24, Low 19, Unclear 10. The Analysis domain drove most High ratings (25 High): single train/test splits without uncertainty, cross-validation pooling sites, and in 8 papers leakage — feature selection, harmonisation or tuning on data outside the training folds (S-011, S-014, S-016, S-027, S-052, S-060, S-077, S-099). Group-difference papers and the data descriptor (n=21) were appraised with JBI analytical cross-sectional items; overall: Low 15, Unclear 6. The commonest weaknesses were unreported motion/QC thresholds (CL2), no site handling (28 of 73 analysis papers), and cohorts that cannot be rebuilt from released files (RQ6 no: 15).

### 3.7 Certainty of Evidence - GRADE (Item 22)

**Diagnostic classification of autism vs typical development from ABIDE rs-fMRI:** Very Low
  Very low certainty that the reported accuracies would hold on data from unseen sites.


### 3.8 Per-Study Design Analysis

*4 groups · 74 included articles · 0 unlabeled (excluded from analysis).*

**Overall caveats:** Computed from charted values by phase3/s3_assemble.py; see results_synthesis.json.


#### Diagnostic prediction *(n = 46)*

46 studies; releases ABIDE I 39, ABIDE I+II 7; median analysed N 872.

*Representative studies:* PMID:local_ad2b6012, PMID:local_748c6bc3, PMID:local_96f7c89f, PMID:local_f02fbc88, PMID:local_bfdf942b

**Group-specific Q&A:**

- **Q:** Which ABIDE release and subset sizes are typical in this group?
  **A:** Releases: ABIDE I 39, ABIDE I+II 7. Analysed total N median 872 (range 82–2226; 2 not reported).
  *Sources:* PMID:local_ad2b6012, PMID:local_748c6bc3, PMID:local_96f7c89f, PMID:local_f02fbc88, PMID:local_bfdf942b
  *Caveats:* Charted analysed N, not release size.
- **Q:** Which pipelines and parcellations recur?
  **A:** Pipelines: CPAC 29, DPARSF 6, custom (SPM/FSL/AFNI/in-house) 5, CCS 4, not reported 3, fconn1000 1, NIAK 1. Atlases (top 5): AAL 15, CC200 11, Harvard-Oxford 11, not reported / not applicable 6, none (voxel/seed/vertex-wise) 6.
  *Sources:* PMID:local_ad2b6012, PMID:local_748c6bc3, PMID:local_96f7c89f, PMID:local_f02fbc88, PMID:local_bfdf942b
  *Caveats:* Multi-label: a paper can use several.
- **Q:** How is site handled, and how often is leakage control reported?
  **A:** Site handling: none reported 21, per-site analyses 6, other site control 5, site used as a model input or graph feature 4, leave-site-out evaluation 4, single site 3, ComBat/NeuroHarmonize harmonisation 2, site covariate / regressed out 2. Leakage control reported (CL5): No 25, Yes 9, Partly 6, Unclear 6. Leakage-flagged (PROBAST Analysis High, specific pattern): 8.
  *Sources:* PMID:local_ad2b6012, PMID:local_748c6bc3, PMID:local_96f7c89f, PMID:local_f02fbc88, PMID:local_bfdf942b
- **Q:** How often can the analysed cohort be reconstructed from released files?
  **A:** Cohort reconstructible (RQ6): partly 24, no 13, yes 9.
  *Sources:* PMID:local_ad2b6012, PMID:local_748c6bc3, PMID:local_96f7c89f, PMID:local_f02fbc88, PMID:local_bfdf942b


#### Group-difference (associational) *(n = 20)*

20 studies; releases ABIDE I 12, ABIDE I+II 6, ABIDE II 2; median analysed N 584.

*Representative studies:* PMID:local_04f9ab5b, PMID:local_62f73884, PMID:local_0dbea86a, PMID:local_f07317a7, PMID:local_307f3aad

**Group-specific Q&A:**

- **Q:** Which ABIDE release and subset sizes are typical in this group?
  **A:** Releases: ABIDE I 12, ABIDE I+II 6, ABIDE II 2. Analysed total N median 584 (range 27–2144; 0 not reported).
  *Sources:* PMID:local_04f9ab5b, PMID:local_62f73884, PMID:local_0dbea86a, PMID:local_f07317a7, PMID:local_307f3aad
  *Caveats:* Charted analysed N, not release size.
- **Q:** Which pipelines and parcellations recur?
  **A:** Pipelines: custom (SPM/FSL/AFNI/in-house) 9, CONN 2, not reported 2, CPAC 2, fMRIPrep 1, Athena 1, CCS 1, DPARSF 1, GRETNA 1. Atlases (top 5): not reported / not applicable 5, none (voxel/seed/vertex-wise) 4, AAL 3, Harvard-Oxford 2, CC200 2.
  *Sources:* PMID:local_04f9ab5b, PMID:local_62f73884, PMID:local_0dbea86a, PMID:local_f07317a7, PMID:local_307f3aad
  *Caveats:* Multi-label: a paper can use several.
- **Q:** How is site handled, and how often is leakage control reported?
  **A:** Site handling: site covariate / regressed out 6, none reported 6, ComBat/NeuroHarmonize harmonisation 4, other site control 4, single site 2, per-site analyses 1. Leakage control reported (CL5): No 13, N/A 6, Partly 1. Leakage-flagged (PROBAST Analysis High, specific pattern): 0.
  *Sources:* PMID:local_04f9ab5b, PMID:local_62f73884, PMID:local_0dbea86a, PMID:local_f07317a7, PMID:local_307f3aad
- **Q:** How often can the analysed cohort be reconstructed from released files?
  **A:** Cohort reconstructible (RQ6): partly 12, yes 6, no 2.
  *Sources:* PMID:local_04f9ab5b, PMID:local_62f73884, PMID:local_0dbea86a, PMID:local_f07317a7, PMID:local_307f3aad


#### Both *(n = 7)*

7 studies; releases ABIDE I 3, ABIDE I+II 3, ABIDE II 1; median analysed N 293.

*Representative studies:* PMID:local_81234492, PMID:local_88791905, PMID:local_6a54db71, PMID:local_904dfa27, PMID:local_d46bcf61

**Group-specific Q&A:**

- **Q:** Which ABIDE release and subset sizes are typical in this group?
  **A:** Releases: ABIDE I 3, ABIDE I+II 3, ABIDE II 1. Analysed total N median 293 (range 113–2095; 0 not reported).
  *Sources:* PMID:local_81234492, PMID:local_88791905, PMID:local_6a54db71, PMID:local_904dfa27, PMID:local_d46bcf61
  *Caveats:* Charted analysed N, not release size.
- **Q:** Which pipelines and parcellations recur?
  **A:** Pipelines: CPAC 3, custom (SPM/FSL/AFNI/in-house) 3, GRETNA 1. Atlases (top 5): CC200 2, AAL 2, Harvard-Oxford 1, Power 264 1, ICA / data-driven networks 1.
  *Sources:* PMID:local_81234492, PMID:local_88791905, PMID:local_6a54db71, PMID:local_904dfa27, PMID:local_d46bcf61
  *Caveats:* Multi-label: a paper can use several.
- **Q:** How is site handled, and how often is leakage control reported?
  **A:** Site handling: leave-site-out evaluation 4, other site control 2, none reported 1, ComBat/NeuroHarmonize harmonisation 1, single site 1. Leakage control reported (CL5): Partly 3, No 2, Yes 2. Leakage-flagged (PROBAST Analysis High, specific pattern): 0.
  *Sources:* PMID:local_81234492, PMID:local_88791905, PMID:local_6a54db71, PMID:local_904dfa27, PMID:local_d46bcf61
- **Q:** How often can the analysed cohort be reconstructed from released files?
  **A:** Cohort reconstructible (RQ6): partly 6, yes 1.
  *Sources:* PMID:local_81234492, PMID:local_88791905, PMID:local_6a54db71, PMID:local_904dfa27, PMID:local_d46bcf61


#### Data descriptor *(n = 1)*

1 studies; releases ABIDE II 1; median analysed N 1044.

*Representative studies:* PMID:local_b363d94a

**Group-specific Q&A:**

- **Q:** Which ABIDE release and subset sizes are typical in this group?
  **A:** Releases: ABIDE II 1. Analysed total N median 1044 (range 1044–1044; 0 not reported).
  *Sources:* PMID:local_b363d94a
  *Caveats:* Charted analysed N, not release size.
- **Q:** Which pipelines and parcellations recur?
  **A:** Pipelines: n/a. Atlases (top 5): n/a.
  *Sources:* PMID:local_b363d94a
  *Caveats:* Multi-label: a paper can use several.
- **Q:** How is site handled, and how often is leakage control reported?
  **A:** Site handling: n/a. Leakage control reported (CL5): No 1. Leakage-flagged (PROBAST Analysis High, specific pattern): 0.
  *Sources:* PMID:local_b363d94a
- **Q:** How often can the analysed cohort be reconstructed from released files?
  **A:** Cohort reconstructible (RQ6): yes 1.
  *Sources:* PMID:local_b363d94a

---

## 4. Discussion

### 4.1 Limitations

Corpus: 200 of 412 open-access primary records were sought (top by citation count, with quotas) and 99 retrieved; 101 were not retrieved (47 no OA PDF location known; 23 publisher OA URL served a bot-check page; 49 of the misses had a PMCID but PMC routes were blocked on 2026-10-15), including the ABIDE I descriptor (Di Martino 2014). Paywalled work is absent by design. Full texts were extracted with PyMuPDF; tables may be garbled. One retrieved PDF (S-040, 10.1016/j.biopsych.2017.09.029) is a different paper, so that record was assessed on its abstract. Screening, charting and appraisal were done by AI charting agents (Claude Sonnet, 8 batches), single-charted, without human double extraction; every quote was mechanically re-verified against the full text (1743 checked, 8 dropped, all empty strings), but the judgments themselves were not independently re-rated. Evaluation-scheme, headline-accuracy and site-handling categories were assigned by the merge agent from charted text, each tied to a verbatim charted snippet. Accuracies are not comparable across papers (different subsets, pipelines, models, metrics), so the scheme-wise distributions are descriptive. Shared cohorts are inferred from identical stated N and release, not from participant lists.
---

## 6. Other Information

- **Registration:** Not registered
- **Protocol:** Not prepared
- **Funding:** None declared
- **Competing interests:** None declared
- **Amendments:** None

## References

1. Adriana Di Martino; David A. O’Connor; Bosi Chen; Kaat Alaerts; Jeffrey S. Anderson; Michal Assaf; Joshua Henk Balsters; Leslie C. Baxter; Anita Beggiato; Sylvie Bernaerts; Laura M. E. Blanken; Susan Y. Bookheimer; Brittany B. Braden; Lisa A. Byrge; F. Xavier Castellanos; Mirella Dapretto; Richard Delorme; Damien A. Fair; Inna Fishman; Jacqueline Fitzgerald; Louise Gallagher; R. Joanne Jao Keehn; Daniel P. Kennedy; Janet E. Lainhart; Beatríz Luna; Stewart H. Mostofsky; Ralph-Axel Müller; Mary Beth Nebel; Joel T. Nigg; Kirsten M. O’Hearn; Marjorie Solomon; Roberto Toro; Chandan J. Vaidya; Nicole Wenderoth; Tonya J.H. White; Richard Cameron Craddock; Catherine Lord; BENNETT L. LEVENTHAL; Michael Peter Milham (2017). Enhancing studies of the connectome in autism using the autism brain imaging data exchange II. *Scientific Data*. https://doi.org/10.1038/sdata.2017.10

2. Adnan Ashraf; Qingjie Zhao; Waqas Haider Bangyal; Muddesar Iqbal (2023). Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things. *IEEE Transactions on Consumer Electronics*. https://doi.org/10.1109/tce.2023.3328479

3. Rafi Ayub; Kevin Sun; Ryan E. Flores; Vicky T. Lam; Booil Jo; Manish Saggar; Lawrence K. Fung (2021). Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults. *Translational Psychiatry*. https://doi.org/10.1038/s41398-021-01221-0

4. Dorothea L. Floris; José Osmar Alves Filho; Meng‐Chuan Lai; Steve Giavasis; Marianne Oldehinkel; Maarten Mennes; Tony Charman; Julian Tillmann; Guillaume Dumas; Christine Ecker; Flavio Dell’Acqua; Tobias Banaschewski; Carolin Moessnang; Simon Baron‐Cohen; Sarah Durston; Eva Loth; Declan Murphy; Jan K. Buitelaar; Christian F. Beckmann; Michael Peter Milham; Adriana Di Martino (2021). Towards robust and replicable sex differences in the intrinsic brain function of autism. *Molecular Autism*. https://doi.org/10.1186/s13229-021-00415-z

5. Oualid M. Benkarim; Casey Paquola; Bo‐yong Park; Valeria Kebets; Seok‐Jun Hong; Reinder Vos de Wael; Shaoshi Zhang; B.T. Thomas Yeo; Michael Eickenberg; Tian Ge; Jean‐Baptiste Poline; Boris C. Bernhardt; Danilo Bzdok (2022). Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging. *PLoS Biology*. https://doi.org/10.1371/journal.pbio.3001627

6. Taiane Coelho Ramos; Joana Bisol Balardin; João Ricardo Sato; André Fujita (2019). Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder. *Frontiers in Systems Neuroscience*. https://doi.org/10.3389/fnsys.2018.00074

7. Xuehan Liu; Md Rakibul Hasan; Tom Gedeon; Md Zakir Hossain (2024). MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder. *Computers in Biology and Medicine*. https://doi.org/10.1016/j.compbiomed.2024.109083

8. Pegah Kassraian; Caroline Matthis; Joshua Henk Balsters; Marloes H. Maathuis; Nicole Wenderoth (2016). Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example. *Frontiers in Psychiatry*. https://doi.org/10.3389/fpsyt.2016.00177

9. Sina Ghiassian; Russell Greiner; Ping Jin; Matthew Brown (2016). Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism. *PLoS ONE*. https://doi.org/10.1371/journal.pone.0166934

10. Jung Min Lee; S.-H. Kyeong; Eun Joo Kim; Keun-Ah Anna Cheon (2016). Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database. *Frontiers in Neuroscience*. https://doi.org/10.3389/fnins.2016.00191

11. Ryuzo Hanaie; Ikuko Mohri; Kuriko Kagitani‐Shimono; Masaya Tachibana; Junko Matsuzaki; Ikuko Hirata; Fumiyo Nagatani; Yoshiyuki Watanabe; Taiichi Katayama; Masako Taniike (2018). Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder. *Frontiers in Human Neuroscience*. https://doi.org/10.3389/fnhum.2018.00454

12. Jinlong Hu; Lijie Cao; Tenghui Li; Shoubin Dong; Ping Li (2021). GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification. *BMC Bioinformatics*. https://doi.org/10.1186/s12859-021-04295-1

13. Md Shale Ahammed; Sijie Niu; Md Rishad Ahmed; Jiwen Dong; Xizhan Gao; Yuehui Chen (2021). DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network. *Frontiers in Neuroinformatics*. https://doi.org/10.3389/fninf.2021.635657

14. Ahmed El-Gazzar; Mirjam Quaak; Leonardo Cerliani; Peter Bloem; Guido Alexander van Wingen; Rajat Mani Thomas (2019). A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study. *Lecture notes in computer science*. https://doi.org/10.1007/978-3-030-32695-1_11

15. Ying Chu; Guangyu Wang; Liang Cao; Lishan Qiao; Mingxia Liu (2022). Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI. *Frontiers in Neuroinformatics*. https://doi.org/10.3389/fninf.2021.802305

16. Wanyi Chen; Jianjun Yang; Zhongquan Sun; Xiang Zhang; Guangyu Tao; Yuan Ding; Jingjun Gu; Jiajun Bu; Haishuai Wang (2024). DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data. *Translational Psychiatry*. https://doi.org/10.1038/s41398-024-02972-2

17. Wonsik Jung; Eunjin Jeon; Eunsong Kang; Heung‐Il Suk (2023). EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning. *IEEE Transactions on Medical Imaging*. https://doi.org/10.1109/tmi.2023.3337362

18. Lucas Mahler; Qi Wang; Julius Steiglechner; Florian Birk; Samuel Heczko; Klaus Scheffler; Gabriele Lohmann (2023). Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification. *Lecture notes in computer science*. https://doi.org/10.1007/978-3-031-44858-4_12

19. Alexandra M. Reardon; Kaiming Li; Xiaoping Philip Hu (2021). Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning. *Frontiers in Computational Neuroscience*. https://doi.org/10.3389/fncom.2021.762781

20. Meenakshi Khosla; Keith Wakefield Jamison; Amy F. Kuceyeski; Mert Rory Sabuncu (2018). 3D Convolutional Neural Networks for Classification of Functional Connectomes. *Lecture notes in computer science*. https://doi.org/10.1007/978-3-030-00889-5_16

21. Cooper Mellema; Kevin P. Nguyen; Alex Treacher; Albert Montillo (2022). Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning. *Scientific Reports*. https://doi.org/10.1038/s41598-022-06459-2

22. Xiaoxiao Li; Yufeng Gu; Nicha C. Dvornek; Lawrence H. Staib; Pamela E. Ventola; James S. Duncan (2020). Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results. *Medical Image Analysis*. https://doi.org/10.1016/j.media.2020.101765

23. Zeinab Sherkatghanad; Mohammadsadegh Akhondzadeh; Soorena Salari; Mariam Zomorodi Moghadam; Moloud Abdar; U. Rajendra Acharya; Reza Khosrowabadi; Vahid Salari (2020). Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network. *Frontiers in Neuroscience*. https://doi.org/10.3389/fnins.2019.01325

24. Bhaskar Sen; Neil C. Borle; Russell Greiner; Matthew Brown (2018). A general prediction model for the detection of ADHD and Autism using structural and functional MRI. *PLoS ONE*. https://doi.org/10.1371/journal.pone.0194856

25. Hailong Li; Nehal A. Parikh; Lili He (2018). A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes. *Frontiers in Neuroscience*. https://doi.org/10.3389/fnins.2018.00491

26. Kaat Alaerts; Daniel Graham Woolley; Jean G. Steyaert; Adriana Di Martino; Stephan Patrick Swinnen; Nicole Wenderoth (2013). Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism. *Social Cognitive and Affective Neuroscience*. https://doi.org/10.1093/scan/nst156

27. Xia-an Bi; Yang Wang; Shu Qing Ma; Qi Sun; Qian Xu (2018). Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster. *Frontiers in Genetics*. https://doi.org/10.3389/fgene.2018.00018

28. Rajat Mani Thomas; Selene Gallo; Leonardo Cerliani; Paul Zhutovsky; Ahmed El-Gazzar; Guido Alexander van Wingen (2020). Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks. *Frontiers in Psychiatry*. https://doi.org/10.3389/fpsyt.2020.00440

29. Amirali Kazeminejad; Roberto C. Sotero (2019). Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification. *Frontiers in Neuroscience*. https://doi.org/10.3389/fnins.2018.01018

30. Rushil Anirudh; Jayaraman J. Thiagarajan (2019). Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification. *IEEE International Conference on Acoustics Speech and Signal Processing*. https://doi.org/10.1109/icassp.2019.8683547

31. Iva Ilioska; Marianne Oldehinkel; Alberto Llera; Sidhant Chopra; Tristan Looden; Roselyne J. Chauvin; Daan van Rooij; Dorothea L. Floris; Julian Tillmann; Carolin Moessnang; Tobias Banaschewski; Rosemary Holt; Eva Loth; Tony Charman; Declan Murphy; Christine Ecker; Maarten Mennes; Christian F. Beckmann; Alex Fornito; Jan K. Buitelaar; EU-AIMS LEAP Group (2022). Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism. *Biological Psychiatry*. https://doi.org/10.1016/j.biopsych.2022.12.018

32. Yongcheng Zong; Qiankun Zuo; Michael K. Ng; Baiying Lei; Shuqiang Wang (2024). A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning. *IEEE Transactions on Pattern Analysis and Machine Intelligence*. https://doi.org/10.1109/tpami.2024.3442811

33. Yaya Liu; Lingyu Xu; Jun Li; Jie Yu; Xuan Yu (2020). Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas. *Experimental Neurobiology*. https://doi.org/10.5607/en.2020.29.1.27

34. Ming–Hsuan Yang; Menglin Cao; Yuhao Chen; Yanni Chen; Geng Fan; Chenxi Li; Jue Wang; Tian Liu (2021). Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model. *Frontiers in Human Neuroscience*. https://doi.org/10.3389/fnhum.2021.687288

35. Xinyu Zhao; D. Rangaprakash; Bowen Yuan; Thomas S. Denney; Jeffrey S. Katz; Michael N. Dretsch; Gopikrishna Deshpande (2018). Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning. *Frontiers in Applied Mathematics and Statistics*. https://doi.org/10.3389/fams.2018.00025

36. Ibrahim Salim; A. Ben Hamza (2023). Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation. *Cognitive Computation*. https://doi.org/10.1007/s12559-023-10224-6

37. Alexandre Abraham; Michael Peter Milham; Adriana Di Martino; Richard Cameron Craddock; Dimitris Samaras; Bertrand Thirion; Gael P. Varoquaux (2016). Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example. *NeuroImage*. https://doi.org/10.1016/j.neuroimage.2016.10.045

38. Sarah Parisot; Sofia Ira Ktena; Enzo Ferrante; Matthew Lee; Ricardo Guerrero; Ben Glocker; Daniel Rueckert (2018). Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer’s disease. *Medical Image Analysis*. https://doi.org/10.1016/j.media.2018.06.001

39. Jared Allen Nielsen; Brandon A. Zielinski; P. Thomas Fletcher; Andrew L. Alexander; Nicholas DE LANGE; Erin D. Bigler; Janet E. Lainhart; Jeffrey S. Anderson (2013). Multisite functional connectivity MRI classification of autism: ABIDE results. *Frontiers in Human Neuroscience*. https://doi.org/10.3389/fnhum.2013.00599

40. Sofia Ira Ktena; Sarah Parisot; Enzo Ferrante; Martin Rajchl; Matthew Lee; Ben Glocker; Daniel Rueckert (2017). Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks. *Lecture notes in computer science*. https://doi.org/10.1007/978-3-319-66182-7_54

41. Md Rishad Ahmed; Yuan Zhang; Omer T. Inan; Hongen Liao (2020). Single Volume Image Generator and Deep Learning-Based ASD Classification. *IEEE Journal of Biomedical and Health Informatics*. https://doi.org/10.1109/jbhi.2020.2998603

42. Enrico Glerean; Raj Kumar Pan; Juha Salmi; Rainer Kujala; Juha M. Lahnakoski; Ulrika Roine; Lauri Nummenmaa; Sami Leppämäki; Taina Nieminen‐von Wendt; Pekka Tani; Jari Saramäki; Mikko E. Sams; Iiro P. Jääskeläinen (2015). Reorganization of functionally connected brain subnetworks in high‐functioning autism. *Human Brain Mapping*. https://doi.org/10.1002/hbm.23084

43. Pingting Lin; Shiyi Zang; Yi Bai; Haixian Wang (2022). Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model. *Frontiers in Human Neuroscience*. https://doi.org/10.3389/fnhum.2022.774921

44. Olga Dona; Geoffrey B. Hall; Michael D. Noseworthy (2017). Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder. *PLoS ONE*. https://doi.org/10.1371/journal.pone.0190081

45. Elizabeth Barbara Torres; Kristina Denisova (2016). Motor noise is rich signal in autism research and pharmacological treatments. *Scientific Reports*. https://doi.org/10.1038/srep37422

46. Sarah Itani; Dorina Thanou (2021). Combining anatomical and functional networks for neuropathology identification: A case study on autism spectrum disorder. *Medical Image Analysis*. https://doi.org/10.1016/j.media.2021.101986

47. R. Nur Syahindah Husna; A. R. Syafeeza; Norihan Binti Abdul Hamid; Yan Chiew Wong; R. Atikah Raihan (2021). FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING. *Jurnal Teknologi*. https://doi.org/10.11113/jurnalteknologi.v83.16389

48. Giovanna Spera; Alessandra Retico; Paolo Bosco; Elisa Ferrari; Letizia Palumbo; P. Oliva; Filippo Muratori; Sara Calderoni (2019). Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning. *Frontiers in Psychiatry*. https://doi.org/10.3389/fpsyt.2019.00620

49. Ibrahim Nafisah; Nermine Mahmoud; Ahmed A. Ewees; Mohamed G. Khattap; Abdelghani Dahou; Safar M. Alghamdi; Ibrahim Ahmed Fares; Mohammed Azmi Al‐Betar; Mohamed Abd Elaziz (2025). Deep learning-based feature selection for detection of autism spectrum disorder. *Frontiers in Artificial Intelligence*. https://doi.org/10.3389/frai.2025.1594372

50. Muhammed Ali Bayram; İlyas Özer; Feyzullah Temurtaş (2021). Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images. *Sakarya University Journal of Computer and Information Sciences*. https://doi.org/10.35377/saucis.04.01.879735

51. Xingdan Liu; Jiacheng Wu; Wenqi Li; Qian Liu; Lixia Tian; Huifang Huang (2023). Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study. *IEEE Transactions on Neural Systems and Rehabilitation Engineering*. https://doi.org/10.1109/tnsre.2022.3233656

52. Ravi Tejwani; Liska, Adam; Hongyuan You; Jenna Reinen; Payel Das (2017). Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning. *arXiv (Cornell University)*. https://doi.org/10.48550/arxiv.1712.08041

53. Lizhen Shao; Cong Fu; Xunying Chen (2023). A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder. *BMC Bioinformatics*. https://doi.org/10.1186/s12859-023-05495-7

54. Yiqian Luo; Qiurong Chen; Fali Li; Yi Liang; Peng Xu; Yangsong Zhang (2025). Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data. *Neural Networks*. https://doi.org/10.1016/j.neunet.2025.107450

55. Chia-Min Chen; Pinchen Yang; Ming‐Tsang Wu; Tzu‐Chao Chuang; Teng‐Yi Huang (2019). Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database. *Scientific Reports*. https://doi.org/10.1038/s41598-019-45465-9

56. Yapei Xie; Zhilei Xu; Mingrui Xia; Jin Liu; Xiao‐Jing Shou; Zaixu Cui; Xuhong Liao; Yong He (2021). Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset. *Biological Psychiatry*. https://doi.org/10.1016/j.biopsych.2021.12.004

57. Shile Qi; Robin Morris; Jessica A. Turner; Zening Fu; Rongtao Jiang; Thomas P. DeRamus; Dongmei Zhi; Vince D. Calhoun; Jing Sui （Beijing Normal University）， my correct affiliation is beijing normal university, not Qingdao University of Science and Technology, please correct the current affiliation. Thank you (2020). Common and unique multimodal covarying patterns in autism spectrum disorder subtypes. *Molecular Autism*. https://doi.org/10.1186/s13229-020-00397-4

58. Stefano Berto; Alex Treacher; Emre Caglayan; Danni Luo; Jillian R. Haney; Michael J. Gandal; Daniel H. Geschwind; Albert Montillo; Geneviève Konopka (2022). Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder. *Nature Communications*. https://doi.org/10.1038/s41467-022-31053-5

59. Sara Saponaro; Francesca Lizzi; Giacomo Serra; Francesca Mainas; P. Oliva; Alessia Giuliano; Sara Calderoni; Alessandra Retico (2024). Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders. *Brain Informatics*. https://doi.org/10.1186/s40708-023-00217-4

60. Fahad Almuqhim; Fahad Saeed (2021). ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data. *Frontiers in Computational Neuroscience*. https://doi.org/10.3389/fncom.2021.654315

61. Johan Jönemo; David Abramian; Anders Eklund (2023). Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks. *Diagnostics*. https://doi.org/10.3390/diagnostics13172773

62. Wenjing Jiang; Shuaiqi Liu; Hong Zhang; Xiuming Sun; Shuihua Wang‎; Jie Zhao; Jingwen Yan (2022). CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification. *Frontiers in Aging Neuroscience*. https://doi.org/10.3389/fnagi.2022.948704

63. Shuo Chen; Yishi Xing; Jian Kang (2017). Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder. *Frontiers in Neuroscience*. https://doi.org/10.3389/fnins.2017.00125

64. Clara F. Weber; Valeria Kebets; Oualid M. Benkarim; Sara Larivière; Yezhou Wang; Alexander Ngo; Hongxiu Jiang; Xiaoqian J. Chai; Bo‐yong Park; Michael Peter Milham; Adriana Di Martino; Sofie Louise Valk; Seok‐Jun Hong; Boris C. Bernhardt (2024). Contracted functional connectivity profiles in autism. *Molecular Autism*. https://doi.org/10.1186/s13229-024-00616-2

65. Swati Rane; Eshin Jolly; Anne T. Park; Hojin Jang; Cameron Craddock (2017). Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset. *Research Ideas and Outcomes*. https://doi.org/10.3897/rio.3.e12733

66. Lei Wei; Yao Zhang; Wensheng Zhai; Huaning Wang; Junchao Zhang; Haojie Jin; Jianfei Feng; Qin Qin; Hao Xu; Baojuan Li; Jian Liu (2022). Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders. *Frontiers in Neuroscience*. https://doi.org/10.3389/fnins.2022.987248

67. Shuo Chen; Jian Kang; Guoqing Wang (2015). An empirical Bayes normalization method for connectivity metrics in resting state fMRI. *Frontiers in Neuroscience*. https://doi.org/10.3389/fnins.2015.00316

68. Carla Caballero; Sejal Mistry; Elizabeth Barbara Torres (2020). Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository. *Frontiers in Integrative Neuroscience*. https://doi.org/10.3389/fnint.2020.00023

69. Christiane S. Rohr; Shanty Kamal; Signe Bray (2019). Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder. *Developmental Cognitive Neuroscience*. https://doi.org/10.1016/j.dcn.2019.100747

70. Pavithra Elumalai; Yasharth Yadav; Nitin Williams; Emil Saucan; Jürgen Jost; Areejit Samal (2022). Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder. *Scientific Reports*. https://doi.org/10.1038/s41598-022-12171-y

71. Robert X. Smith; Kay Jann; Mirella Dapretto; Danny J.J. Wang (2018). Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach. *Frontiers in Neuroscience*. https://doi.org/10.3389/fnins.2018.00869

72. Archit Rathore; Sourabh Palande; Jeffrey S. Anderson; Brandon A. Zielinski; P. Thomas Fletcher; Bei Wang (2019). Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale. *Lecture notes in computer science*. https://doi.org/10.1007/978-3-030-32248-9_82

73. Mohammed Isam Al-Hiyali; Norashikin Yahya; Ibrahima Faye; Zia Khan (2021). Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network. *International Journal of Integrated Engineering*. https://doi.org/10.30880/ijie.2021.13.05.006

74. Naseer Ahmed Khan; Samer Abdulateef Waheeb; Atif Riaz; Xuequn Shang (2020). A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder. *Brain Sciences*. https://doi.org/10.3390/brainsci10100754


---

## Appendix A: Evidence Spans

- **PMID:local_b363d94a** (score: 1.00): "a new multi-site open data resource containing 1,044 independent datasets (ASD N = 487;
Controls N = 557)"
- **PMID:local_b363d94a** (score: 0.95): "The current ABIDE II dataset encompasses 17 collections of unique independent datasets (i.e., from
individuals whose data were not previously shared in ABIDE I) yielding 487 datasets classiﬁed as ASD
and 557 as controls (Fig. 1a, Table 1). These represent previously collected datasets across 16 sites,
including nine charter ABIDE I institutions and seven new members"
- **PMID:local_b363d94a** (score: 0.90): "ASD classiﬁcation was determined by either 1) combining clinical judgment with ‘gold standard’
diagnostic instruments—Autism Diagnostic Observation Scale34,35 and/or Autism Diagnostic Interview-
Revised36 [ADOS, ADI-R]; (n = 12 data collections; 368 ASD datasets) or 2) by using these ‘gold
standard’ diagnostic instruments only (n = 4 collections; 92 ASD datasets)"
- **PMID:local_b363d94a** (score: 0.85): "we used the Preprocessed Connectome Project quality assurance protocol49
(http://preprocessed-connectomes-project.github.io)"
- **PMID:local_b363d94a** (score: 0.90): "users regardless of data quality27. The rationale of this decision includes the lack of consensus on optimal
quality criteria in regards to speciﬁc measures or their combinations and cutoffs."
- **PMID:local_b363d94a** (score: 0.80): "All ABIDE II datasets can be accessed, after establishing a login and user password, through FCP/INDI
at the Neuroimaging Informatics Tools and Resources Clearinghouse (NITRC; http://fcon_1000.projects.
nitrc.org/indi/abide/). The datasets are organized by data collection and stored in.tar ﬁles, each
containing imaging and phenotypic data."
- **PMID:local_b363d94a** (score: 0.60): "The ABIDE II sample has increased the number of available datasets from females with
ASD from 65 in ABIDE I to 138 when ABIDE I+II are combined."
- **PMID:local_b363d94a** (score: 0.70): "Finally, to facilitate replications among studies using ABIDE data, we encourage users to provide
the ID list utilized for their published manuscripts in the manuscript section of the ABIDE
website (http://fcon_1000.projects.nitrc.org/indi/abide/manusc"
- **PMID:local_ad2b6012** (score: 0.90): "where ABIDE-I and 
ABIDE-II consists of 1112 rs- fMRI datasets from 573 typical 
control (TC) and 539 autism individuals, and 1114 rs-fMRI from 
521 autism and 593 typical control individuals respectively, 
which were collected from 17 different sites."
- **PMID:local_ad2b6012** (score: 1.00): "Our proposed 
optimized version of CNN achieved 81.56% accuracy. This 
outperforms prior conventional approaches presented only on 
the ABIDE I datasets."
- **PMID:local_ad2b6012** (score: 0.85): "The ABIDE-I dataset is 
composed of 1112 resting-state functional magnetic resonance 
imaging (rs-fMRI) datasets. Among these, 573 datasets belong 
to typically developing persons, while 539 datasets belong to 
individuals with autism. On the other hand, the ABIDE-II 
dataset consists of 1014 resting-state functional magnetic 
resonance imaging (rs-fMRI) datasets. Out of these, 521 
datasets are from individuals with autism, and 593 datasets are 
from typically developing control individuals."
- **PMID:local_ad2b6012** (score: 0.60): "Collecting the Abide dataset was a challenging task as the 
online data repository is only accessible for Neuro Informatics 
Tools and Resources Collaboratory (NITRC) members. 
Firstly,  applied for data access to NITRC through E-mail and 
submitted the thesis title, supervisor contact, problem 
statement and research objectives. Luckily, upon success after 
a couple of days that made us eligible to download available"
- **PMID:local_ad2b6012** (score: 0.70): "Collected dataset was organized in three groups: 
● 
ABIDE I 
● 
ABIDE II 
● 
ABIDE I+II "
- **PMID:local_ad2b6012** (score: 1.00): "TABLE XI 
CLASSIFICATION ACCURACY OF CONVOLUTION NEURAL NETWORK FOR ABIDE-II 
Dataset 
Model 
Acc 
Sensitivity 
Specificity 
F1-Score 
ABIDE - I+II 
CNN  
81.56  
81.5%  
80.5%  
88.0% 
DTL-NN   
82.31%  
83.3%  
80.7%  
87.0%"
- **PMID:local_ad2b6012** (score: 0.70): "Our analysis is limited by the method utilised to 
collect ABIDE data from 17 foreign clinical and research 
sites. Another limitation is picture data availability. The 
dataset has 851 subjects, which is significant."
- **PMID:local_ad2b6012** (score: 0.75): "ABIDE-II data download and labelling was a 
challenging task. Each image was manually labelled and 
assigned a group. Each group was tested separately to 
compare and analyze results of each set."
- **PMID:local_04f9ab5b** (score: 1.00): "The secondary cohort was a subset of the ABIDE database
consisting of 58 HFASD (25.4[7.8] years, 37.9% female) and 51 typically developing controls (24.4[6.7] years, 39.2%
female)."
- **PMID:local_04f9ab5b** (score: 0.90): "To validate our ﬁndings in a separate cohort, we iden-
tiﬁed 58 ASD and 51 TD individuals from ABIDE mat-
ched to the HFASD cohort by age, sex, and IQ (Table 2).
The selection process is detailed in Supplemental Infor-
mation."
- **PMID:local_04f9ab5b** (score: 0.95): "Func-
tional data from both the HFASD and ABIDE cohorts
were preprocessed identically using fMRIPrep v1.3.152, a
pipeline that uses a combination of tools from existing
neuroimaging software packages."
- **PMID:local_04f9ab5b** (score: 0.80): "In the ABIDE cohort, group-mean FD was
0.124 for ASD and 0.123 for TD (two sample t-test p =
0.8679)."
- **PMID:local_04f9ab5b** (score: 0.85): "Frames that exhibited an FD of over 0.5 mm were
censored from the timeseries, as well as one before and
two after the offending frame."
- **PMID:local_04f9ab5b** (score: 0.85): "Participants with <80% of
their TRs retained after motion scrubbing were removed
from the analysis. As a result, a total of 20 TD participants
and 23 ASD participants were analyzed from the HFASD
cohort (Table 1). From ABIDE, 51 TD participants and 58
ASD participants were analyzed (Table 2)."
- **PMID:local_04f9ab5b** (score: 0.90): "To account for potential con-
founding effects from differences in scan acquisition
parameters, we included site as a covariate in our ABIDE
GLM analysis as one-hot encoded variables."
- **PMID:local_04f9ab5b** (score: 1.00): "In the ABIDE GLM analysis, clusters were found that
had greater connectivity with the right thalamus in the
ASD group compared to the TD group. Two of these
clusters were located in the right precentral (p = 0.019)
and postcentral gyri (p = 0.028), validating the observed
hyperconnectivity of the same regions in our HFASD
cohort."
- **PMID:local_62f73884** (score: 1.00): "The final 
ABIDE I and II dataset of N = 1019 included N = 82 
females with autism, N = 362 males with autism, N = 166 
neurotypical females (NT F), and N = 409 neurotypical 
males (NT M), aggregated across 13 sites."
- **PMID:local_62f73884** (score: 0.90): "Briefly, we selected cases between 
7 and 18 years of age (the ages most represented across 
ABIDE sites), with MRI data successfully completing 
brain image co-registration and transformation to stand-
ard space, with FIQ between 70 and 148 and with mean 
framewise displacement (mFD) [54] within three times 
the interquartile range (IQR) + the third quartile (Q3) of 
the sample (i.e., mFD 0.39"
- **PMID:local_62f73884** (score: 0.75): "At each step, any sites with less than three individual 
datasets per diagnostic/sex groups were excluded."
- **PMID:local_62f73884** (score: 0.85): "R-fMRI image pre-processing 
steps included: slice time correction, 24 motion param-
eters regression [57], component-based noise reduction 
(CompCor) [58], removal of linear and quadratic trends, 
and band-pass filtering (0.01–0.1 Hz, for all metrics but 
fALFF)."
- **PMID:local_62f73884** (score: 0.90): "To account for site and collection time variability 
across each of the data collections in ABIDE I and II data 
repositories, site effects were removed using the ComBat 
function available in python [61] (https​://githu​b.com/
brent​p/comba​t.py). This approach has been shown to 
effectively account for scanner-related variance"
- **PMID:local_62f73884** (score: 1.00): "Discovery analyses in ABIDE revealed significant main effects of diagnosis and sex across the intrinsic func‑
tional connectivity of the posterior cingulate cortex, regional homogeneity and voxel-mirrored homotopic connectiv‑
ity (VMHC) in several cortical regions, largely converging in the default network midline."
- **PMID:local_62f73884** (score: 1.00): "Sex-by-diagnosis interactions 
were confined to the dorsolateral occipital cortex, with reduced VMHC in females with autism."
- **PMID:local_62f73884** (score: 0.60): "ABIDE I and II: Data are freely accessible in the publicly available Autism Brain 
Imaging Data Exchange repository (http://fcon_1000.projects.nitrc.org/indi/
abide)."
- **PMID:local_748c6bc3** (score: 1.00): "procedures resulted in a total of 297 par-
ticipants (151 ASD and 146 TD) from 4 different sites (i.e., New York University Langone
Medical Center [NYU], University of Pittsburgh, School of Medicine [PITT], University of
Utah, School of Medicine [USM], and Trinity Centre for Health Sciences [TCD]) in ABIDE."
- **PMID:local_748c6bc3** (score: 0.90): "For ABIDE, we considered data from all acquisition sites with at least 10 participants per
group and with both children and adults. After detailed quality control, only cases with accept-
able T1-weighted (T1w) MRI, surface extraction, and head motion in rs-fMRI were included."
- **PMID:local_748c6bc3** (score: 0.80): "Participants with ASD were diagnosed based on an in-person interview administered by
board-certified mental health professionals using the gold standard diagnostics of the Autism
Diagnostic Observation Schedule (ADOS) [51] and/or Autism Diagnostic Interview-Revised
(ADI-R) [52,53]."
- **PMID:local_748c6bc3** (score: 0.90): "For the resting-state functional brain scans in ABIDE, we built on data previously made
available by the Preprocessed Connectomes initiative (http://preprocessed-connectomes-
project.org/abide). The preprocessing was performed with C-PAC (https://fcp-indi.github.io)
and included slice time correction, head motion correction, skull stripping, and intensity nor-
malization. The rs-fMRI data were detrended and adjusted for common nuisance effects
related to head motion, white matter, and cerebrospinal fluid signals using CompCor [58], fol-
lowed by band-pass filtering (0.01 to 0.1 Hz)."
- **PMID:local_748c6bc3** (score: 0.85): "Func-
tional connectivity matrices were calculated at a single-participant level based on a widely used
parcellation atlas with 100 cortical regions [61]."
- **PMID:local_748c6bc3** (score: 0.85): "After matching, we ended up with 290 participants (145 participants per group)
in ABIDE and 126 (63 participants per group) in HBN, which were used subsequently for the
classification of ASD versus TD in both datasets."
- **PMID:local_748c6bc3** (score: 1.00): "Similar to the computation of the pro-
pensity scores, we performed deconfounding prior to our analyses, based on all the available
participants instead of using only the training"
- **PMID:local_748c6bc3** (score: 0.90): "In the ABIDE cohort, when we trained and
tested on data with similar distributions (first column), the contiguous scheme reached better
prediction performance than the diverse scheme, with the random scheme lying in between.
This trend remained stable as we increased the number of strata used for training."
- **PMID:local_748c6bc3** (score: 1.00): "we can observe a decline in performance in ABIDE as diversity increased in both within
(AUC: r = −0.630, F1 score: r = −0.568) and out-of-distribution (AUC: r = −0.671, F1 score:
r = −0.579) predictions."
- **PMID:local_748c6bc3** (score: 0.60): "Data Availability Statement: The imaging and
phenotypic data were provided, in part, by the
Autism Brain Imaging Data Exchange initiative
(ABIDE-I and II; https://fcon_1000.projects.nitrc.
org/indi/abide) and the Healthy Brain Network
(https://fcon_1000.projects.nitrc.org/indi/cmi_
healthy_brain_network). All imaging features,
phenotypic data, and code are openly available at
https://github.com/OualidBenkarim/ps_diversity."
- **PMID:local_0dbea86a** (score: 0.90): "we used functional magnetic resonance imaging (fMRI) of 708 subjects under a resting
state protocol provided by the ABIDE I Consortium."
- **PMID:local_0dbea86a** (score: 0.85): "ABIDE I is composed of 573
individuals with TD and 539 individuals with ASD (totaling
1 112 subjects). ABIDE II is composed of 593 individuals
with TD and 521 individuals with ASD (totaling 1 114
subjects)."
- **PMID:local_0dbea86a** (score: 0.95): "After preprocessing (described in section 2.2.), the
ABIDE I dataset was composed of 432 subjects with TD
(348 males, mean age ± standard deviation of 18.21 ±
8.04) and 276 individuals with ASD (241 males, 18.42 ±
8.38). The ABIDE II dataset was composed of 316 subjects
with TD (208 males, 12.80 ± 5.61) and 269 individuals
with ASD (234 males, 13.93 ± 7.07)."
- **PMID:local_0dbea86a** (score: 0.85): "We preprocessed the imaging data using the Athena pipeline
(www.nitrc.org/plugins/mwiki/index.php/neurobureau:Athena
Pipeline).
The
pipeline
focused
on
providing
systematic
processing of fMRI data, including the following main steps:
exclusion of the ﬁrst four scans; slice timing correction;"
- **PMID:local_0dbea86a** (score: 0.95): "Subjects that had more than 5% of the total number of scans
removed by scrubbing were excluded from the analysis. Head
motion across the dataset is measured by the FD, which presents
a mean of 0.137 mm and standard deviation of 0.102 mm on
the study dataset (ABIDE I) and a mean of 0.169 mm with
standard deviation of 0.132 mm on the independent dataset
(ABIDE II)."
- **PMID:local_0dbea86a** (score: 0.70): "A total of 93 subjects (53 TD and 40 ASD) in the
study dataset (ABIDE I) and 45 subjects (24 TD and 21 ASD) in
the independent dataset (ABIDE II) had scans removed by the
scrubbing process."
- **PMID:local_0dbea86a** (score: 1.00): ",
namely, the right fusiform gyrus [β = −0.042, t-value = −3.689,
p = 0.005 —t-test (GLM)], the right postcentral gyrus [β =
−0.038, t-value = −3.131, p = 0.027 — t-test (GLM)], the
right superior temporal gyrus [β = −0.034, t-value = −3.082,
p = 0.027 –t-test (GLM)], the right middle temporal gyrus
[β = −0.039, t-value = −3.783, p < 0.001 —t-test (GLM)],
and the left middle temporal gyrus [β = −0.056, t-va"
- **PMID:local_0dbea86a** (score: 1.00): "In
this validation analysis, three out of ﬁve cortical ROIs, namely,
the right fusiform gyrus [β
=
−0.028, t-value = −2.193,
p = 0.047 —t-test (GLM)], the right superior temporal gyrus
[β = −0.044, t-value = −3.495, p = 0.002 —t-test (GLM)],
and the left middle temporal gyrus [β
=
−0.033, t-value
= −2.583, p = 0.025—t-test (GLM)], conﬁrmed the reduced
functional connectivity in the ASD group"
- **PMID:local_0dbea86a** (score: 0.85): "Thus, to
minimize the site eﬀect in our analysis, we included it as a
covariate in group-level statistics as described in the section 2.3."
- **PMID:local_96f7c89f** (score: 0.90): "We use rs-fMRI and demographic data from ABIDE I [11], the first phase of ABIDE, with
505 autistic individuals and 530 Typical Controls (TCs)."
- **PMID:local_96f7c89f** (score: 0.90): "We, therefore,
leverage the CPAC pipeline, hereinafter referred to as the ABIDE I CPAC data."
- **PMID:local_96f7c89f** (score: 0.85): "Although Di Martino et al. [11] released the ABIDE I dataset with 1,112 samples, prepro-
cessing and quality control reduced this number to 1,035"
- **PMID:local_96f7c89f** (score: 1.00): "Whole dataset
1,035
75.20
82.90
69.70
Proposed subset
645
88.71
81.82
92.50
NYU subset
175
96.40
91.00
99.50"
- **PMID:local_96f7c89f** (score: 0.95): "We, therefore, train our model on the NYU dataset using the CC atlas, save this model and
repurpose it as a selector. We apply this pretrained model to classify ASD/TC instances across
the whole ABIDE I dataset, which correctly classifies 645 out of 1,035 samples (around 62.3%)."
- **PMID:local_96f7c89f** (score: 0.80): "The Automated Anatomical Labelling (AAL) atlas, with 116 ROIs, is widely
used in ASD diagnosis studies [16, 35, 36, 37] due to its ability to provide precise anatomical lo-
cations essential for identifying structural abnormalities caused by ASD. The Craddock 200 atlas
[38], with 200 ROIs, is based on functional connectivity and is particularly useful for analysing
resting-state fMRI data [39, 9, 36, 37], as it clusters the brain into functionally homogeneous
regions.
Recent studies have leveraged multiple atlases to capture diverse patterns related to ASD.
For instance, Mahler et al. [37] proposed a multi-atlas framework for ASD classification using
resting-state fMRI data, employing three atlases, including AAL and Craddock 200. Similarly,
Deng et al. [9] utilised the AAL, Craddock 200 and Craddock 400 atlases. Their experiment in-
dicates that Craddock 200 can outperform Craddock 400 in fMRI-based ASD diagnosis. Hence,
we selected the Craddock 200 atlas, hereinafter referred to as the CC atlas.
To further enhance the analysis, we leverage the Eickhoff-Zilles (EZ) atlas with 116 ROIs,
which has also been utilised in recent ASD diagnosis studies [40, 41]. Derived from cytoarchi-
tectonic mapping, the EZ atlas combines anatomical and functional data, offering a nuanced view
that bridges structural and functional aspects of brain regions"
- **PMID:local_96f7c89f** (score: 0.90): "Our model achieved an ac-
curacy score of 75.20%, which is a boost of 4.4 percentage points over the best prior work [20]
on 1,035 samples."
- **PMID:local_f02fbc88** (score: 1.00): "The inputs to the classification pipeline 
are the 77 ASD and 77 TD connectivity matrices (hence 154 data 
samples in total), where each connectivity matrix consists of 
19,900 features."
- **PMID:local_f02fbc88** (score: 0.85): "We balance the data per site, meaning that we take the same 
number of ASD subjects as TD subjects per site. Furthermore, 
we ensure that the 2 resulting classes (TD and ASD) with 77 
subjects each are similar on average with respect to IQ, age, and 
head movements. This prevents the classifier from separating"
- **PMID:local_f02fbc88** (score: 0.85): "Two hundred ROIs are determined from the Craddock atlas (15) (A). For each subject, the time series of voxel 
intensities are averaged over voxels with an ROI, and Pearson correlation coefficients are computed for all pairs of averaged time series (B), resulting in a 200"
- **PMID:local_f02fbc88** (score: 0.85): "Data presented in this study underwent standard fMRI pre-
processing (i.e., realignment, normalization, and smoothing) 
implemented in SPM12b. Data were preprocessed according to 
standard SPM protocols including realignment, normalization 
to a study specific template using DARTEL, smoothing, band-
pass filtering (0.01–0.05 Hz), and scrubbing to account for head 
movements (63)."
- **PMID:local_f02fbc88** (score: 1.00): "The performance of each classifier is assessed by nested cross-
validation: 10-folds are used in the outer cross-validation loop for 
the performance estimation, and 10-folds are used in the inner 
cross-validation loop to determine the optimal threshold value 
t for feature selection, or the optimal regularization parameter 
for lasso-regularized"
- **PMID:local_f02fbc88** (score: 0.95): "One pitfall is given when feature 
selection or selection of tuning parameters is performed on the full 
data, i.e., on data samples from both the training and the test set."
- **PMID:local_f02fbc88** (score: 1.00): "If, however, we use the entire dataset to select the 
features with a mean difference above a threshold value t = 0.10, 
classification with a linear SVM yields a test accuracy of 91%. If 
the feature selection is correctly applied using only the training 


9
Kassraian-Fard et al.
Classification of Psychiatric Imaging Data 
Frontiers in Psychiatry  |  www.frontiersin.org
December 2016  |  Volume 7  |  Article 177
set, the classification accuracy is between 45 and 56%."
- **PMID:local_f02fbc88** (score: 0.90): "We took the so far best performing classifier – the support 
vector machine – and applied it to the data set after this stand-
ardization was performed. The resulting classification accuracy 
increased from 63 to 68%."
- **PMID:local_f02fbc88** (score: 0.70): "Another possibility to assess the generalizability of the clas-
sifier to data from different sites is to form training and test sets 
from different sites. An example of this approach is leave-one-
site-out cross-validation, where the test set contains data from a 
site that has not been used in the training set (36)."
- **PMID:local_f02fbc88** (score: 0.60): "The MATLAB code as discussed is available at http://www.ncm.
hest.ethz.ch/downloads/software.html under “ABIDE 1 classifi-
cation and pitfalls."
- **PMID:local_bfdf942b** (score: 0.85): "This
dataset is comprised of resting state fMRI and T1-weighted structural MRI scans from 1112
subjects, including patients with autism and healthy controls. ABIDE participant data was col-
lected at 17 different institutions in North America and Europe."
- **PMID:local_bfdf942b** (score: 0.80): "We had to exclude one subject whose
data could not be preprocessed with our preprocessing pipeline, leaving us with a dataset of
1111 individuals, including 573 healthy controls and 538 patients with autism."
- **PMID:local_bfdf942b** (score: 0.90): "Therefore, we divided the ABIDE dataset into training and test sets by ran-
domly selecting a label-balanced 889 (4/5) of the ABIDE subjects as the training set, leaving
the remaining 222 (1/5) ABIDE subjects as the testing set."
- **PMID:local_bfdf942b** (score: 0.95): "Testing on the hold-out test set Dtest protected against overfitting in terms of algo-
rithm choice, feature selection, parameter values, a"
- **PMID:local_bfdf942b** (score: 0.85): "For preprocessing, we used SPM8, a software package designed for analyzing brain imaging
data and also for preprocessing fMRI data [27, 28] and our own in-house MATLAB code."
- **PMID:local_bfdf942b** (score: 1.00): "Table 16. ABIDE results summary.
Data Source(s)
Accuracy
Sensitivity
Speciﬁcity
Functional MRI
59.2%
72.2%
45.4%
Structural MRI
60.1%
70.4%
49.1%
Personal Characteristic
59.6%
60.9%
58.3%
Structural MRI + Personal Characteristic
64.1%
75.7%
51.9%
Functional MRI + Personal Characteristic
65.0%
71.3%
58.3%"
- **PMID:local_bfdf942b** (score: 0.60): "Data Availability Statement: All data used in this
paper are publicly available as follows: The ADHD-
200 dataset is available online at http://fcon_1000.
projects.nitrc.org/indi/adhd200/ The ABIDE dataset
is available online at http://fcon_1000.projects.
nitrc.org/indi/abide/."
- **PMID:local_f07317a7** (score: 0.90): "We used resting state fMRI data of 458 subjects with ASD and
517 TDCs (see Table 1 for additional demographic information)
among 1112 datasets from the ABIDE datasets"
- **PMID:local_f07317a7** (score: 0.90): "We excluded
datasets from the social brain Lab BCN NIC UMC Groningen
and Netherlands Institute for Neurosciences due to the missing
information of a full-scale intelligence quotient (IQ) for many
subjects. After preprocessing, we found that a large part of the
cerebellum was missing in the imaging dataset of Carnegie
Mellon University, and all datasets from Carnegie Mellon
University were excluded. To control for potential confounding
eﬀects of IQ in our analysis, we decided to exclude ﬁve datasets
that included some subjects with IQ lower than 70. Finally, we
performed voxel-wise group comparisons with 975 imaging
datasets."
- **PMID:local_f07317a7** (score: 0.90): "Datasets were preprocessed with SPM8 (http://www.ﬁl.ion.ucl.
ac.uk/spm/software/spm8/). The ﬁrst step was realignment for
head motion correction. Images were realigned to the ﬁrst
image and a mean echo planar image (EPI) was created during
this step. Subsequently, structural T1 images were coregistered
to their mean EPI data. Registered EPI data of each subject
were normalized to Montreal Neurological Institute (MNI)
template and spatially smoothed with 8 mm of full-width at half-
maximum. Then, in the temporal domain, the linearly increasing
trend due to heat absorption was removed at each voxel, and
the eﬀects of the head motion, white matter, cerebrospinal ﬂuid,
and global signal were regressed out. Lastly, temporal band-pass
ﬁltering was applied (0.01–0.08 Hz)."
- **PMID:local_f07317a7** (score: 0.90): "2-tailed t-test design with two covariates of age
and sex was used to compute the statistical signiﬁcance of the
FCD diﬀerences between the two groups. Statistical signiﬁcance
was based on the false discovery rate corrected P < 0.05 together
with requiring 20 voxels for the minimum continuous voxel
size within a cluster (corrected P < 0.05)."
- **PMID:local_f07317a7** (score: 0.70): "In several sites, the datasets contained clinical information
such
as
the
Autism
Diagnostic
Interview-Revised
(ADI-
R), the restricted and repetitive behavior subscore of the
Autism
Diagnostic
Observation
Schedule
(ADOS-RRB),
and communication subscore of the ADOS (ADOS-COM)."
- **PMID:local_307f3aad** (score: 0.90): "extracted from the Autism Brain Imaging Data Exchange (ABIDE) II"
- **PMID:local_307f3aad** (score: 0.60): "The ABIDE II consists of datasets from 487 individuals with ASD and 557 controls collected across 16 imaging sites."
- **PMID:local_307f3aad** (score: 0.90): "in order to collect samples similar to our original samples, we selected subjects who met following criteria: boys with FSIQ ≥80, age range: 6–16 years, right handed, with scores recorded on the SRS"
- **PMID:local_307f3aad** (score: 0.90): "Since no participants in the NYU_2 dataset had complete cerebellar coverage, this dataset was excluded. In addition, participants with excessive maximum head motion (>3 mm) or failure of normalization were excluded."
- **PMID:local_307f3aad** (score: 1.00): "The ﬁnal replication dataset consisted of 42 boys with ASD (mean age: 10.7 ± 1.8 years, range: 7.2–14.4 years) and 88 TD boys"
- **PMID:local_307f3aad** (score: 0.80): "Preprocessing for functional images consisted of realignment for motion correction, slice-timing correction, normalization to the standard MNI space, and smoothing with a 4-mm full width at half- maximum ﬁlter."
- **PMID:local_307f3aad** (score: 0.70): "Seed ROIs in the cerebellum were created using the probabilistic MR Atlas of the human cerebellum"
- **PMID:local_307f3aad** (score: 0.80): "mean FD scores were included as a nuisance covariate in t-tests. In addition, FSIQ and imaging sites were included as nuisance covariates. Bonferroni correction was performed for multiple comparisons (p = 0.004)."
- **PMID:local_307f3aad** (score: 0.90): "decreased FCs were identiﬁed between the following regions: the right lobule IX and right lobule VI; vermis VI and left MFG, left ITG, and right MdFG; right dentate nucleus and left IFG, left IPL"
- **PMID:local_307f3aad** (score: 1.00): "the ASD group showed signiﬁcantly decreased FC between the right dentate nucleus and left IPL (p = 0.039, Figure 4)"
- **PMID:local_0c61e485** (score: 0.90): "We experimentally compared GAT2 model’s performance on the  ABIDE I database from 1035 subjects"
- **PMID:local_0c61e485** (score: 1.00): "We used the resting-state fMRI data from 1035 subjects in the ABIDE I initiative [20]  for this study. The dataset includes 505 individuals diagnosed as having ASD and 530  HC."
- **PMID:local_0c61e485** (score: 0.90): "The data were preprocessed by the Configurable Pipeline for the Analysis of Con- nectomes (CPAC) pipeline [24] that included the following procedure: slice timing cor- rection, motion realignment, intensity normalization, regression of nuisance signals,  band-pass filtering (0.01–0.1 Hz) and registration of fMRI images to standard anatomi- cal space (MNI152)."
- **PMID:local_0c61e485** (score: 0.80): "We use the Harvard Oxford (HO) atlas [23], so we  have N = 110 nodes."
- **PMID:local_0c61e485** (score: 0.70): "After randomly perform- ing fivefold cross-validation data division, in each round of experiments, one-fold data    Page 11 of 20 Hu et al. BMC Bioinformatics          (2021) 22:379  	 were used for testing while other fourfold data were used for t"
- **PMID:local_0c61e485** (score: 1.00): "The GAT2 model achieved the best results in accuracy, sensitivity, F1 score, and MCC  indicators using fivefold cross-validation, with the accuracy of 68.02%, sensitivity of  74.06%, F1 score of 69.31%, and MCC of 0.3426."
- **PMID:local_0c61e485** (score: 0.60): "Compared  with the AAL atlas, using the HO atlas for construction of the brain network,  with the same model, the accuracy was increased by about 5%, the sensitivity was  increased by about 2%, and the F1 value was increas"
- **PMID:local_0c61e485** (score: 0.60): "3 rsFCs (the connection 4, 5, and 7) were statistically significant (p < 0.05)  between the ASD and HC groups."
- **PMID:local_0c61e485** (score: 0.80): "The datasets analyzed during the current study are available in the ABIDE Preprocessed Connectomes Project website of  http://​prepr​ocess​ed-​conne​ctomes-​proje​ct.​org/​abide/​downl​oad.​html. The source codes of GAT-LI are publicly available  at the project website of https://​github.​com/​large​app/​gat-​li."
- **PMID:local_0709116d** (score: 1.00): "Our model’s outcomes unveil that our proposed method established state-of-the-art accuracy of 94.70% to classify ASD vs. TC in ABIDE-I, NYU dataset."
- **PMID:local_0709116d** (score: 0.80): "In our experiments, we used ABIDE-I data processed through the Connectome Computation System (CCS) (Craddock et al., 2013)."
- **PMID:local_0709116d** (score: 0.80): "Among the 17 sites, we endeavor with the CCS-NYU (New York University Langone Medical Center) site."
- **PMID:local_0709116d** (score: 0.90): "TABLE 2 | NYU phenotypic data information for ABIDE-I database.
Total subjects
ASD
TC
Female
Male
Age range (Years)
Average age (SD)
ADOS score (SD)
ASD
TC
184
79
105
35
149"
- **PMID:local_0709116d** (score: 0.60): "data are selected from the ﬁlt_global preprocessing stratagem, which is band-pass ﬁltered (0.01–0.1 Hz) and spatially registered using a nonlinear method to MNI152 template space"
- **PMID:local_0709116d** (score: 0.60): "The original 3D fMRI data has 73 slices per volume according to the data description of ABIDE-I. In our experiments, from the 73 slices, we contemplated the last 50 slices because of the precise sketches of the brain images."
- **PMID:local_0709116d** (score: 1.00): "After testing our model for ASD classiﬁcation, we have achieved the highest accuracy of 94.7%, the precision of 94.5%, recall of 92.5%, f1-score of 95%, and the AUC score 94.703%."
- **PMID:local_0709116d** (score: 0.40): "The raw data supporting the conclusions of this article will be made available by the authors, without undue reservation."
- **PMID:local_7c21219e** (score: 1.00): "Our results show that the proposed model achieves state of the art results on single sites with F1-scores of 0.78 and 0.7 on NYU and UM sites, respectively."
- **PMID:local_7c21219e** (score: 0.80): "We preprocessed the data with the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) and the fMRI volumes are downsampled to 4 mm in MNI."
- **PMID:local_7c21219e** (score: 0.90): "For single sites experiments, we use the NYU and UM sites from ABIDE-I. Those provide the highest number of balanced (ASD/typically developing (TD)) subjects with 184 and 110 subjects respectively."
- **PMID:local_7c21219e** (score: 0.90): "For the multi-site experiment we used ABIDE-I with 19 sites and 1100 subjects."
- **PMID:local_7c21219e** (score: 0.70): "We report 5-fold cross validation mean F1-score and accuracy for the experiments in Table 1."
- **PMID:local_7c21219e** (score: 1.00): "The results show that the proposed architecture 3DCNN C-LSTM outperforms other models on single site experiments by achieving mean test accuracies and F1 scores of 0.77 and 0.78 respectively for the NYU site and 0.71 and 0.7 on the UM site."
- **PMID:local_7c21219e** (score: 0.80): "3DCNN C-LSTM however also shows a degraded performance in multi-site
environment as evidenced by the results on ABIDE-1 data that features 19 sites."
- **PMID:local_7c21219e** (score: 0.60): "We attribute the loss of performance of our model to the heterogeneity of the
data acquired from diﬀerent scanners with diﬀerent scanning parameters."
- **PMID:local_65679dfd** (score: 0.90): "The proposed MGRL is evaluated on 184 subjects from the public Autism Brain Imaging Data Exchange (ABIDE) database with rs-fMRI scans."
- **PMID:local_65679dfd** (score: 1.00): "In this work, we use rs-fMRI data from the New York University (NYU) site with the largest sample size collected in this database. Speciﬁcally, the NYU site includes 184 subjects, 79 of whom were from ASD and 105 NC cases."
- **PMID:local_65679dfd** (score: 0.80): "the remaining volumes are processed by a well- accepted pipeline with the Data Processing Assistant for Resting- State fMRI toolbox (DPARSF) (Yan et al., 2016)."
- **PMID:local_65679dfd** (score: 0.90): "by partitioning the brain into multiple ROIs using two atlases, i.e., Automated Anatomical Labeling (AAL) (Tzourio-Mazoyer et al., 2002) atlas with 116 ROIs and Craddock200 (CC200) (Craddock et al., 2012) atlas with 200 ROIs."
- **PMID:local_65679dfd** (score: 0.90): "Considering the small amount of subjects, we randomly select
80% of all the samples as training data, 10% of all samples as
validation data, and the remaining 10% as test data. We repeat the
random partition process 100 times and record the mean and SD
results of each method."
- **PMID:local_65679dfd** (score: 1.00): "MGRL (Ours)
0.795 ± 0.068
0.809 ± 0.146
0.823 ± 0.103
0.802 ± 0.075
0.886 ± 0.062"
- **PMID:local_65679dfd** (score: 0.70): "to avoid signiﬁcant inter-site heterogeneity, we mainly used rs-fMRI data from the NYU site. While ABIDE contains data from 21 sites, as a future work, we will evaluate the proposed method on all sites in ABIDE and design smart techniques to reduce inter-site data heterogeneity."
- **PMID:local_65679dfd** (score: 0.30): "The original contributions presented in the
study are included
in the article/supplementary material, further inquiries can be
directed to the corresponding author/s."
- **PMID:local_6fb7c550** (score: 0.70): "We apply DeepASD to the benchmarking Autism Brain Imaging Data Exchange (ABIDE) data with four modalities."
- **PMID:local_6fb7c550** (score: 1.00): "The dataset includes 871 subjects
(468 TC and 403 ASD subjects). We follow (Parisot, 2017) [19] for
the dataset settings and preprocessing."
- **PMID:local_6fb7c550** (score: 1.00): "ABIDE B, encompassing
949 subjects, adheres to the settings outlined by (Wang, 2020)
[10]. This cohort includes 419 individuals diagnosed with ASD and
530 TC subjects."
- **PMID:local_6fb7c550** (score: 0.70): "The dataset integrates three brain atlases (CC200,
AAL - Automated Anatomical Labeling, and DOS - Dosenbach160)"
- **PMID:local_6fb7c550** (score: 0.80): "For a fair comparison, all data are preprocessed using the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) based on the preprocessed fMRI datasets [22]."
- **PMID:local_6fb7c550** (score: 0.80): "we performed a 10-
fold stratiﬁed cross-validation strategy on the two datasets."
- **PMID:local_6fb7c550** (score: 0.80): "All experiments were conducted with a 10-fold cross-validation to divide the dataset into training and test sets, with 10% of the training set randomly selected as the validation set. Ultimately, the training, validation, and test sets were non-overlapping."
- **PMID:local_6fb7c550** (score: 1.00): "The model achieved the following performance metrics, presented in mean ± standard deviation format, on the ABIDE A dataset: accuracy (ACC) of 87.38 ± 2.87%, area under curve (AUC) of 92.76 ± 4.00%, speciﬁcity (SEN) of 88.35 ± 6.83%, and sensitivity (SPE) of 86.51 ± 8.41%."
- **PMID:local_6fb7c550** (score: 0.80): "showing an improvement of 13.25% in
accuracy, 7.69% in AUC-ROC, and 17.10% in speciﬁcity."
- **PMID:local_6fb7c550** (score: 0.50): "In the population-gcn [19] study, the construction of patient-patient relational graphs was based on demographic information, speciﬁcally sex and site."
- **PMID:local_6fb7c550** (score: 0.50): "The ABIDE dataset is available from ref. [21], and the preprocessed dataset ABIDE A and ABIDE B are provided with the paper."
- **PMID:local_6fb7c550** (score: 0.60): "An interactive code base for DeepASD implementation is available at https:// codeocean.com/capsule/6043886/tree."
- **PMID:local_9829a18a** (score: 0.60): "It
 consists of 1, 112 subjects, including 539 from individuals with ASD"
- **PMID:local_9829a18a** (score: 0.80): "from 17 international sites2. The ROIs fMRI series of all sites are downloaded from the pre-processed ABIDE dataset with a configurable pipeline for the analysis of connectomes (CPAC), band-pass filter- ing (0.01 −0.1Hz), and no global signal regression"
- **PMID:local_9829a18a** (score: 0.80): "it is parcellated using the Harvard-Oxford (HO) atlas. After downloading the pre-processed data, 110 ROIs are acquired using the HO atlas."
- **PMID:local_9829a18a** (score: 1.00): "samples with missing filenames and incomplete data are
excluded; and the remaining 880 samples across 17 international
sites are utilized, which include 418 ASD subjects and 478 TD subjects."
- **PMID:local_9829a18a** (score: 0.80): "stratified five-fold cross-
validation is conducted, where one fold is used for t"
- **PMID:local_9829a18a** (score: 1.00): "EAG-RS 0.760±0.033 73.71±2.83 64.56±8.36 80.74±8.28"
- **PMID:local_9829a18a** (score: 0.50): "https://github.com/ku-milab/EAG-RS"
- **PMID:local_d76b09c5** (score: 1.00): "Our framework utilizes resting-state functional mag-
netic resonance imaging data from the ABIDE I dataset, comprising 406 ASD and 476 typical control (TC) subjects."
- **PMID:local_d76b09c5** (score: 0.90): "In this work we use the preprocessed data from the DPARSF pipeline [31] comprising 406 ASD and 476 TC subjects."
- **PMID:local_d76b09c5** (score: 0.90): "METAFormer employs a multi-atlas approach, where flattened connectivity matrices from the AAL, CC200, and DOS160 atlases serve as input to the transformer encoder."
- **PMID:local_d76b09c5** (score: 0.90): "we employed 10-fold stratified cross-validation. For each fold, the model is trained
on the remaining nine training folds and evaluated on the held-out test fold.
Further, we set aside 30% of each training fold as validation sets"
- **PMID:local_d76b09c5** (score: 1.00): "METAFormer PT 0.837 ±0.030 0.819±0.045 0.901 ±0.044 0.856 ±0.023 0.832 ±0.032"
- **PMID:local_d76b09c5** (score: 0.60): "The code for our framework is available at github.com/Lugges991/METAFormer"
- **PMID:local_d76b09c5** (score: 0.50): "The raw dataset encompasses a total of 1112 subjects, 539 of which are diagnosed with ASD and 573 are TC."
- **PMID:local_1ee6bb17** (score: 0.80): "We present a site-wise de-meaning (SWD) strategy in multi-site FC analysis and compare its performance with two common site-effect mitigation methods, i.e., generalized linear model (GLM) and Combining Batches (ComBat) Harmonization."
- **PMID:local_1ee6bb17** (score: 1.00): "Resting-state fMRI data from 850 subjects in ABIDE I with an ASD DSM-IV-TR diagnosis (n = 355) and the corresponding HCs (n = 495) from the same sites were used in this study"
- **PMID:local_1ee6bb17** (score: 0.80): "The resting-state fMRI data was preprocessed using the
Connectome Computation System pipeline (Zuo et al., 2013)."
- **PMID:local_1ee6bb17** (score: 0.80): "The resting state fMRI data was then parcellated into
200 regions of interest (ROIs) using a spatially constrained
spectral clustering algorithm based on functional parcellations by
Cameron Craddock (Craddock et al., 2012)."
- **PMID:local_1ee6bb17** (score: 0.80): "The most common resting state
fMRI ﬁnding regarding ASD FC was anterior-posterior DMN
hypoconnectivity"
- **PMID:local_1ee6bb17** (score: 1.00): "For the ABIDE dataset, SWD improved the effect size between autistic and control subjects by 2.9–5.3%, while GLM and ComBat decreased the effect size by up to 11.4%."
- **PMID:local_1ee6bb17** (score: 0.40): "Autism data is publicly available from ABIDE (http://fcon_1000.projects.nitrc.org/indi/abide/)"
- **PMID:local_7623d661** (score: 0.95): "We showcase our approach on a challenging large-scale dataset (ABIDE, with N > 2, 000) and report state-of-the-art accuracy results on rs-fMRI- based discrimination of autism patients and healthy controls."
- **PMID:local_7623d661** (score: 0.70): "The ﬁrst phase of ABIDE (ABIDE-I) compiled data from 1112 individuals, comprising 539 individuals diagnosed with Autism Spec- trum Disorder (ASD) and 573 typical controls, from 17 sites. The second phase (ABIDE-II) was recently released, and consists of an additional 521 individuals with ASD and 593 healthy controls, from 19 sites."
- **PMID:local_7623d661** (score: 0.90): "In our experiments, we used ABIDE-I subject data that passed manual qual- ity assessments (QA) by all the functional raters. This yielded a ﬁnal sample size of 774 ABIDE-I subjects, comprising 379 subjects with ASD and 395 typical con- trols."
- **PMID:local_7623d661** (score: 0.95): "Since manual QA was not yet available for ABIDE-II, we per- formed an automatic quality control by selecting those subjects that retained at least 100 frames or 4 minutes of fMRI scans after motion scrubbing [19]. Motion scrubbing was performed based on Framewise Displacement (FD), dis- carding one volume before and two volumes after the frame with FD exceeding 0.5mm [15]. This step yielded a ﬁnal ABIDE-II sample size of 163 individuals with ASD and 230 healthy controls."
- **PMID:local_7623d661** (score: 0.85): "The Preprocessed Connectomes Project (PCP) released preprocessed versions of ABIDE using several pipelines [4]. We used the data processed through Conﬁgurable Pipeline for Analysis of Connectomes (CPAC). This pipeline includes slice timing correction, motion correction, global mean intensity normalization and standardization of functional data to MNI space (3x3x3 mm resolution) before the extraction of ROI time series."
- **PMID:local_7623d661** (score: 0.90): "First, we implemented a 10-fold cross-validation scheme for ABIDE-I to be consistent with previously reported classiﬁcation re- sults [1, 18]. Second, we trained each model on all of ABIDE-I and computed test performance on an independent held-out set from ABIDE-II. This is used for assessing the generalization behavior of diﬀerent classiﬁers. We report accu- racy and the receiver operating curves (ROC), along with corresponding area under the curves (AUC) for each of these scenarios."
- **PMID:local_7623d661** (score: 0.90): "Previous studies have reported cross- validated classiﬁcation accuracies up to 67% on ABIDE-I, the ﬁrst phase of the ABIDE study [1]. The proposed CNN approach improves this accuracy to above 73%."
- **PMID:local_7623d661** (score: 0.85): "The ensemble achieves an AUC of 75.8%."
- **PMID:local_afcc5b8c** (score: 0.95): "Our model achieves state-of-the-art 80% area under the ROC curve (AUROC) in diagnosis on test data from the IMPAC dataset; and 86% and 79% AUROC on the external ABIDE I and ABIDE II datasets (with further improvement to 93% and 90% after supervised domain adaptation)."
- **PMID:local_afcc5b8c** (score: 0.95): "Participants from all sites of the ABIDE I and ABIDE II were included for external validation, provided both sMRI and rsfMRI were obtained on the same visit. The first avail- able pair of sMRI and rsfMRI scans were used per subject. 1045 subjects from ABIDE I and 761 subjects from ABIDE II met this criteria."
- **PMID:local_afcc5b8c** (score: 0.80): "Table 3. Demographics of IMPAC participants, ABIDE I participants, and ABIDE II participants. Errors shown are standard deviations. IMPAC ABIDE I ABIDE II Female % 50 15 20 ASD % 46 48 52 Age (years) 17 ± 9.6 17 ± 8.1 17 ± 11 Total participants 915 1045 761"
- **PMID:local_afcc5b8c** (score: 0.85): "The IMPAC fMRI and sMRI were processed using the fconn1000 ­pipeline41. For the fMRI connectivity features, the TSE connectivity metric was fit on either the training data alone (IMPAC models) or the entire IMPAC dataset (ABIDE 1 and 2 datasets), and the TSE values per-ROI timeseries for the ABIDE dataset were calculated."
- **PMID:local_afcc5b8c** (score: 0.80): "The features were standard scaled by the mean and standard deviation of the IMPAC dataset."
- **PMID:local_afcc5b8c** (score: 0.95): "The top single model trained using IMPAC attained 80.4% AUROC on IMPAC held-out test data. When tested on ABIDE I, it achieved an AUROC of 86.0% (Table 2 underlined) and when tested on the ABIDE II it achieved a performance of 79.2%."
- **PMID:local_afcc5b8c** (score: 0.90): "These tuned models achieved AUROC as high as 93.2% on ABIDE-I and 90.5% on ABIDE-II, roughly a 4–9 basis point increase in performance relative to models without any adaptation."
- **PMID:local_afcc5b8c** (score: 0.70): "we are pleased to provide full analysis source code, saved models, and pipeline parameters at:"
- **PMID:local_c0ef18d3** (score: 0.90): "we downloaded Re- gions of Interests (ROIs) fMRI series of the top four largest sites (UM1, NYU, USM, UCLA1) from the preprocessed ABIDE dataset with Conﬁgurable Pipeline for the Analysis of Connec- tomes (CPAC), band-pass ﬁltering (0.01 - 0.1 Hz), no global signal regression, parcellated by Harvard-Oxford (HO) atlas."
- **PMID:local_c0ef18d3** (score: 0.90): "Skipping subjects lacking ﬁlename, we downloaded 106, 175, 72, 71 subjects from UM1, NYU, USM, UCLA1 separately. HO parcellated each brain into 111 ROIs. Since some sub- jects did not contain complete ROIs, we removed the incom- plete data, resulting in 88, 167, 52, 63 subjects for UM1, NYU, USM, UCLA1 separately."
- **PMID:local_c0ef18d3** (score: 0.85): "NYU UM USM UCLA Total Subject 167 88 52 63 ASD Subject 73 43 33 37 HC Subject 94 45 19 26 ASD Percentage 44% 49% 63% 59% fMRI Frames 176 296 236 116 Overlapping Trunc 145 265 205 85 Table 1: Data summary of the dataset used in our study"
- **PMID:local_c0ef18d3** (score: 0.95): "The mean accuracy of Fed was higher than the best Cross learning case for each single site. In addition, Fed was signiﬁcantly bet- ter than Single by two sample t test with p < 0.001 for each site."
- **PMID:local_c0ef18d3** (score: 0.90): "Single 0.601(0.064) 0.648(0.065) 0.695(0.108) 0.571(0.100) Ensemble 0.611(0.012) 0.638(0.054) 0.654(0.088) 0.634(0.064) Fed 0.647(0.049) 0.728(0.073) 0.849(0.124) 0.712(0.075) Fed-MoE 0.671(0.082) 0.728(0.083) 0.809(0.098) 0.744(0.130) Fed-Align 0.676(0.071) 0.751(0.053) 0.829(0.091) 0.712(0.089) Mix 0.671(0.035) 0.740(0.063) 0.829(0.137) 0.710(0.128) Table 3: Results of using diﬀerent training strategies"
- **PMID:local_c0ef18d3** (score: 0.70): "Overall, the accuracies of using CC200 was lower than the accuracies of us- ing HO. This could be caused by overﬁtting as the number of parameters required for training CC200 data is higher than HO due to the dimensionality of the input."
- **PMID:local_c0ef18d3** (score: 0.80): "Our results have demonstrated the advantage of using a fed- erated framework to utilize multi-site data without data shar- ing compared to alternative methods."
- **PMID:local_b72b2fbd** (score: 0.90): "detect ASD correctly with an accuracy of 70.22% using the ABIDE I dataset and the CC400"
- **PMID:local_b72b2fbd** (score: 0.80): "The inclusion criteria for sites was having at least 20 subjects meeting other criteria for inclusion like successful preprocessing with manual visual inspection of normalization to MNI space of MPRAGE."
- **PMID:local_b72b2fbd** (score: 0.90): "There are 1,112 subjects (539 diagnosed with ASD, and 573 typical controls) in the ABIDE I dataset, reduced to 871 subjects after preprocessing."
- **PMID:local_b72b2fbd** (score: 0.85): "The Preprocessed Connectomes Project (PCP) is a publicly available preprocessed version of data from both the 1,000 Functional Connectomes Project (FCP) and the International Neuroimaging Data-Sharing Initiative (INDI)3. We used data from the FCP using the conﬁgurable pipeline, the Analysis of Connectomes (CPAC)."
- **PMID:local_b72b2fbd** (score: 0.80): "We used the CC400 functional parcellation atlas of the brain throughout our study."
- **PMID:local_b72b2fbd** (score: 0.95): "We achieved an accuracy of 70.22 %, which is better than the rest of the reported works (Table 4)."
- **PMID:local_b72b2fbd** (score: 0.90): "we used a leave-site-out approach for our proposed CNN, SVM, KNN, and RF classiﬁers (Heinsfeld et al., 2018). In this method, each site is taken as one fold in the dataset, and we applied a cross-validation approach on the remaining sites instead of diﬀerent folds. Therefore, each time, one site out of 17 is used to test, and the other sites are used for training."
- **PMID:local_b72b2fbd** (score: 0.60): "DATA AVAILABILITY STATEMENT The datasets generated for this study are available on request to the corresponding author."
- **PMID:local_0a18ed38** (score: 0.95): "achieving an accuracy of 0.673 on the ADHD-200 holdout data and 0.643 on the ABIDE holdout data. Both of these results, obtained with the same LEFMSF framework, are the best known, over all hold-out accuracies on these datasets when only using imaging data—exceeding previously-published results by 0.012 for ADHD and 0.042 for Autism."
- **PMID:local_0a18ed38** (score: 0.95): "The ABIDE dataset consists of 1111 scans, taken from 17 sites consisting of 573 healthy controls and 538 patients with autism. To evaluate each learning model, we use 800 subjects (70%) for model training and 311 subjects (30%) for hold-out testing. We use the same case/control ratio (0.5157) for both training and test set."
- **PMID:local_0a18ed38** (score: 0.85): "For preprocessing fMRI and MRI scans, we used SPM8 (http://www.fil.ion.ucl.ac.uk/spm/ software/spm8/) and our own in-house MATLAB code. Preprocessing was identical to that used in Ghiassian et al. [13]."
- **PMID:local_0a18ed38** (score: 0.90): "the resulting hold-out accuracy for ADHD was 0.6491 (baseline 0.5497) and was 0.6233 for ABIDE (baseline 0.5157). The specificity, sensitivity and Jstat for ADHD (resp., ABIDE) are 0.8191, 0.4416 and 0.2607 (respectively, 0.6768, 0.5533 and 0.2301). To our knowl- edge, our holdout accuracies achieved on ADHD-200 test data and the ABIDE test data are the best known when only using fMRI scans."
- **PMID:local_0a18ed38** (score: 0.90): "We found that models trained using only site information achieved an accuracy of 66.0% on the ADHD data and 55.0% on the ABIDE data, while our models trained on MRI data achieved much higher accuracies: 67.4% and 64.3%, respectively."
- **PMID:local_0a18ed38** (score: 0.90): "We then tested those previously-trained classifiers on these new “site-balanced test sets” and found that the accuracies did not differ significantly from the original test set results: here, it was 69.88% for ADHD-200 and 63.46% for ABIDE."
- **PMID:local_0a18ed38** (score: 0.60): "Both datasets are available online publicly. The ADHD-200 dataset is available at: http://fcon_1000.projects.nitrc.org/ indi/adhd200/ The ABIDE dataset is available at: (http://fcon_1000.projects.nitrc.org/indi/abide/)."
- **PMID:local_2983df5d** (score: 0.90): "we compared the performance of our DTL-NN approach with a traditional deep neural network and support vector machine models across four ABIDE data sites that enrolled at least 60 subjects. As compared to traditional models, our DTL-NN approach achieved an improved performance in accuracy, sensitivity, speciﬁcity and area under receiver operating characteristic curve."
- **PMID:local_2983df5d** (score: 0.90): "The rs- fMRI data were processed using Connectome Computation System (Xu et al., 2015) pipeline, which includes slice timing correction, motion realignment, and intensity normalization. Nuisance variable regression (Fox et al., 2005; Lund et al., 2005) was implemented through band-pass ﬁltering and global signal regression strategies to clean confounding variations introduced by heartbeats and respirations, head motion, and low frequency scanner drifts. Furthermore, boundary-based rigid body and FMRIB’s linear & nonlinear image registration tools (Andersson et al., 2008; Ratziu et al., 2008) were used to register functional to anatomical images. Then, both functional and anatomical images were normalized to a standard template space, the Automated Anatomical Labeling atlas (Tzourio-Mazoyer et al., 2002)."
- **PMID:local_2983df5d** (score: 0.90): "Site bias was corrected among diﬀerent sites similar to an approach described previously by an ABIDE study (Heinsfeld et al., 2018). Speciﬁcally, a multiple regression analysis was conducted to control for potentially confounding variables (site, age, gender, and handedness). These variables were regressed from FC weights across connections among ROIs. When adjusting for the confounding factors, our regression model is: y = β0 + β1x1 + β2x2 + β3x3 + β4x4 + ε where y is the vector of FC weights, x1 to x4 represent the four explanatory variables, site, age, gender, and handedness. βi is the intercept and the corresponding regression coeﬃcients. ε is the residual vector. Using ordinary least squares (OLS) estimation, βi was estimated. Then, these cofounding variables were regressed out from the FC weights."
- **PMID:local_2983df5d** (score: 0.90): "we performed ASD classiﬁcation experiments on four individual data sites with at least 60 subjects, including University of Michigan (UM), University of California, Los Angeles (UCLA), University of Utah School of Medicine (USM), and Katholieke Universiteit Leuven (LEUVEN)."
- **PMID:local_2983df5d** (score: 0.90): "the independent healthy FC data from the remaining 16 sites from the ABIDE repository were accumulated as pre- collected data to train an SSAE prototype during oﬄine learning. Then, we randomly split the data from the target site into training and testing set. The data from the training set were applied on an SSAE prototype in the prior knowledge aided training step. The hold-out testing data were then used to evaluate the trained DTL-NN model."
- **PMID:local_2983df5d** (score: 0.85): "TABLE 2 | Demographic data of the healthy and autism spectrum disorder (ASD) subjects across seven data sites ordered by decreasing sample size. Site Class Target task sample size Age (years) Gender (male%) Handedness (right%)* Mean full-scale IQ* Ofﬂine learning sample size UM ASD 48 13.8 ± 2 81.30 75 107.6 ± 17.3 411 Healthy 65 15 ± 3.7 75.40 83.10 109 ± 9.5 UCLA ASD 36 13.3 ± 3 94.40 88.90 102.4 ± 12.8 437 Healthy 39 13.2 ± 1.8 84.60 92.30 106.4 ± 10.4 USM ASD 38 24.6 ± 9 100 92.10 99.7 ± 17.3 453 Healthy 23 22.3 ± 7.9 100 95.70 115.5 ± 15.6 LEUVEN ASD 27 18 ± 5 92.60 88.90 109.4 ± 13.1 442 Healthy 34 18.2 ± 5.1 85.30 85.30 114.8 ± 12.9 All ± values are mean ± SD. *Results were calculated after removing missing data. Number of IQ missing value: UM, ASD-1, Healthy-3; UCLA, ASD-0, Healthy-0; USM, ASD-0, Healthy-0; LEUVEN, ASD-13, Healthy-19"
- **PMID:local_2983df5d** (score: 0.90): "The highest ASD classiﬁcation performance metrics were observed from the USM site−70.4% accuracy, 72.5% sensitivity, 67.0% speciﬁcity and 0.73 AUC."
- **PMID:local_8a1f1b25** (score: 0.90): "Intrinsic FC of the right pSTS was further examined using 584 (278 ASD/306 controls) resting-state data of the"
- **PMID:local_8a1f1b25** (score: 0.90): "Analyses with the large independent ABIDE dataset replicated reductions in pSTS-iFC to fronto-parietal regions."
- **PMID:local_8a1f1b25** (score: 0.95): "The replication dataset consisted of 584 resting-state fMRI datasets from nine sites contributing to the ‘ABIDE’ release (Di Martino et al., 2013). In this sample, all participants with ASD (278) had a clinician’s DSM-IV-TR diagnosis of ASD, which was corroborated by the Autism Diagnostic Observation Schedule (ADOS) and the Autism Diagnostic Interview-Revised (Lord et al., 1994, 1999) for all sites except one."
- **PMID:local_8a1f1b25** (score: 0.90): "For the ABIDE-replication dataset (278 ASD/306 TD participants) (Supplementary Table S1), we computed iFC and mean FD scores using the same procedures as described above (Supplementary Figure S3B). Within each site, groups displayed comparable mean FD scores (except for one site). Across sites, micro-movements were greater within the ASD than in the TD group [F(1,566) ¼ 4.23, P ¼ 0.041] (Supplementary Table S1 and Figure S3B). As for the ori- ginal sample, we corrected for micro-movements by including mean FD scores as a nuisance covariate in the primary group analysis"
- **PMID:local_8a1f1b25** (score: 0.95): "Similar to findings emerging from the original dataset, we observed a significant reduction in pSTS-iFC with right IPL and left premotor area in the ASD compared with the TD group. Reduced pSTS-iFC was also observed with the fusiform gyrus and bilateral superior oc- cipital gyrus (Figure 6; Supplementary Table S3). Stronger pSTS-iFC in the ASD group was observed with left thalamus and right IFG"
- **PMID:local_8a1f1b25** (score: 0.75): "TD > ASD group differences remained similar in the secondary ‘scrubbed’ analyses (Supplementary Figure S4B), whereas primary findings of ASD > TD group differences were only identified subthreshold."
- **PMID:local_85ac52be** (score: 0.90): "Resting-state functional magnetic resonance imaging (fMRI) data of 46 TC and 61 ASD patients were obtained from the Autism Brain Imaging Data Exchange (ABIDE) database. Only 84 of 107 subjects are utilized in experiments because the translation or rotation of 7 TC and 16 ASD patients has surpassed ±2 mm or ±2◦."
- **PMID:local_85ac52be** (score: 0.90): "accuracy based on the optimal feature set could reach to 96.15%."
- **PMID:local_85ac52be** (score: 0.90): "Only 84 of 107 subjects are utilized in experiments because the translation or rotation of 7 TC and 16 ASD patients has surpassed ±2 mm or ±2◦. Then the random SVM cluster was proposed to distinguish TC and ASD. The results show that this method has an excellent classiﬁcation performance based on all the features. Furthermore, the accuracy based on the optimal feature set could reach to 96.15%. Abnormal brain regions could also be found, such as inferior frontal gyrus (IFG) (orbital and opercula part), hippocampus, and precuneus. It is indicated that the method of random SVM cluster may apply to the auxiliary diagnosis of ASD. Keywords: random support vector machine cluster, neuroimaging, autism spectrum disorder, classiﬁcation, feature selection INTRODUCTION Autism spectrum disorder (ASD) is mainly reﬂected in the communication and language barriers, diﬃculties in social communication, and it is a kind of neurological developmental disorder (Karten and Hirsch, 2015; Khundrakpam et al., 2017). The behavioral phenotype of ASD is well-depicted but its etiology and pathogenesis is rarely known (Amaral et al., 2008). According to the results of Hallmayer et al. (2011), the causes of ASD mainly include genetic and environmental risk factors. Some of the symptoms of ASD generally appear in about 2 years old (Ecker et al., 2015), thus the early diagnosis is needed (Plitt et al., 2015). It is recognized that traditional clinical methods cannot well distinguish patients from healthy controls (HC) (Mwangi et al., 2012). And it may not be complex enough to capture the abnormal brain regions in individuals who suﬀering from ASD (Uddin et al., 2011). To avoid this disadvantage, machine learning is introduced in the neuroimaging ﬁeld. It is a valid means to extract messages from neuroimaging data and further predict the future changes of the disease (Klöppel et al., 2012; Orrù et al., 2012). Among numerous machine learning methods, support vector machines (SVM) is an excellent classiﬁcation method Bi et al. Classiﬁcation of ASD Using Random-SVM-Cluster (Zhang et al., 2015). SVM has distinct merits such as the higher classiﬁcation accuracy (Zhang and Wu, 2012) and no need for a large number of training samples to avoid over-ﬁtting (Li et al., 2010). Thus, SVM has aroused widespread concern of researchers in the ﬁeld of neuroimaging (Sundermann et al., 2014). In the researches of machine learning, SVM has been applied to classify ASD from corresponding controls. Gori et al. (2015) extracted features from the gray matter subregions, then these features were used in SVM to identity ASD from HC and the area under ROC curve (AUC) is 0.74. Jin et al. (2015) proposed an original multi-kernel SVM classiﬁcation method to classify ASD from HC and the accuracy can reach to 76%. Chen et al. (2016) used the SVM to classify 112 adolescent subjects with ASD and 128 HC, and the classiﬁcation accuracy was 79.17%. Odriozola et al. (2015) used the SVM based on functional magnetic resonance imaging (fMRI) data to classify 20 children with ASD and 20 typically developing (TD) peers, and the result showed 85% classiﬁcation accuracy. Chanel et al. (2016) used the method of SVM and Recursive Feature Elimination (RFE) based on fMRI data to classify ASD from HC, and the result showed good classiﬁcation accuracy (up to 92.3%). These SVM classiﬁcation studies on ASD have achieved relatively high classiﬁcation accuracy in the range of 70–93% compared with traditional methods. They usually employed a single SVM and common features such as functional connections, gray matter volume to classify ASD from HC, and the classiﬁcation accuracy is generally lower than 90%. In this paper, a novel method of random SVM cluster is proposed and several graph metrics of brain functional connectivity (e.g., local eﬃciency, shortest path) are employed to classify ASD and typical controls (TC). This method has some good performance. Firstly, the classiﬁcation accuracy reaches to a higher level based on all the features. Then, we could ﬁnd out the optimal feature set, the classiﬁcation accuracy could also reach to the same level based on the optimal feature set. Thirdly, on the basis of the optimal feature set, we could ﬁnd out the abnormal brain regions such as inferior frontal gyrus (IFG) (orbital and opercula part), hippocampus, and precuneus. Thus, the random SVM cluster may apply to the auxiliary diagnosis of ASD. MATERIALS AND METHODS Demographic Information The Autism Brain Imaging Data Exchange (ABIDE) database (http://fcon_1000.projects.nitrc.org/indi/abide/) (Di Martino et al., 2014) contains a variety of neuroimaging data. And the resting-state fMRI data include 539 ASD and 573 age-matched TC. There are 12 kinds of image protocols. This study chooses one of the image protocols, details as follows. MRI scanner = 3.0- T Siemens, TR = 3,000 ms, TE = 28 ms, data matrix = 64∗64, Pixel Spacing X = 3.0 mm, Pixel Spacing Y = 3.0 mm, Flip Angle = 90◦, Slice Thickness = 0.0 mm, no slice gap, axial slices = 34, time points = 120. Finally, 61 subjects with ASD and 46 TC met the image protocol. The original studies included in ABIDE received approval from each site’s Institutional Review Board (IRB). All images were obtained with informed consent according to procedures established by human subject research boards. Only 84 of 107 subjects are utilized in experiments because the translation or the rotation of 7 TC and 16 ASD patients has surpassed ± 2 mm or ± 2◦."
- **PMID:local_85ac52be** (score: 0.85): "TABLE 1 | Basic information of ASD and TC. Variables (Mean ± SD) Autism (n = 45) TC (n = 39) P value Gender (M/F) 41/4 33/6 0.359 Age (years) 13.4 ± 2.4 12.9 ± 1.7 0.278 ASD, Autism spectrum disorder; TC, typical controls."
- **PMID:local_85ac52be** (score: 0.85): "all the fMRI images are preprocessed by the Data Processing Assistant for Resting- State fMRI (DPARSF) software (Cui et al., 2015) (http://d.rnet. co/DPABI/DPABI_V2.3_170105.zip). The whole preprocessing procedures include:(1) Converting DICOM to NIFTI, (2) Removing the ﬁrst 10 time points, (3) Slicing timing, (4) Realigning, (5) Normalizing with the echo-planar imaging (EPI) template, (6) Smoothing, (7) Removing the linear trend, (8) Temporal ﬁltering, (9) Removing covariates."
- **PMID:local_85ac52be** (score: 0.85): "fMRI image could be divided into 90 regions based on the Automatic Anatomical Labeling (AAL) (Tzourio-Mazoyer et al., 2002) atlas. We make these regions as the nodes of brain network, so there are 90 nodes. An average of the time series of a region’s all voxels can be used to capture the mean time series of this region (Khazaee et al., 2016). The average time series of every two brain regions can be employed to calculate the Pearson correlation coeﬃcient which is made as the link of the brain network (Khazaee et al., 2015), so there are 4,005 (90∗89/2) weighted edges."
- **PMID:local_85ac52be** (score: 0.90): "Firstly, the 84 samples are divided into 58 training samples and 26 test samples based on the ratio of 7:3. Then 50 samples are randomly selected from the 58 training samples and 62 features are randomly selected from 4,225 features, which form a single SVM using Radial Basis Function (RBF) as kernel provided by the SVM toolbox (http://see.xidian.edu.cn/faculty/chzheng/ bishe/indexﬁles/indexl.htm) (Gunn, 1998). The width argument of RBF equals to 3, and penalty coeﬃcient equals to Inf. The process is repeated for 500 times and these 500 SVMs constitute into a random SVM cluster."
- **PMID:local_85ac52be** (score: 0.90): "the accuracy of the random SVM cluster is as high as 96.15%. This is suﬃcient to show that the performance of the random SVM cluster is much better than a single SVM."
- **PMID:local_97b1be33** (score: 0.90): "We attained results competitive on this task for a combined ABIDE-I and II datasets of ~66%. When all summary measures were combined the result was still only as good as that of the best single measure which was regional homogeneity (ReHo)."
- **PMID:local_97b1be33** (score: 0.85): "The ABIDE I+II datasets is a collection of structural (T1w) and functional (rs-fMRI) brain images aggregated across 29 institutions (10), available for download2. It includes 1,028 participants with a diagnosis of autism, Asperger or pervasive developmental disorder-not otherwise speciﬁed (called ASD from now on), and 1,141 typically developing participants (CON)."
- **PMID:local_97b1be33** (score: 0.95): "We chose to cut off the minimum scan duration to 100-time points, which led us to include 96% of the whole ABIDE I+II dataset (N=2,085, N(ASD) =993), the vast majority of which (95%) with a minimum acquisition time of 4 min."
- **PMID:local_97b1be33** (score: 0.85): "The preprocessing was done using the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC, (12). We followed a preprocessing strategy adopted by the Preprocessed Connectome Project initiative3. This will allow others to replicate and extend the ﬁndings in this paper."
- **PMID:local_97b1be33** (score: 0.90): "For the leave-site-out CV procedure, we selected ﬁve sites with the highest number of total subjects (ASD/total), namely New York University (NYU) (90/159), Kennedy Krieger Institute - 1 (KKI-I) (88/114), University of Miami - 1 (UM-I) (50/96), University of California, Los Angeles (UCLA)-I (28/69), Oregon Health & Science University (OHSU)-I (42/64)."
- **PMID:local_97b1be33** (score: 0.90): "When assessed by ﬁve-fold CV procedure, all tested models performed at around 60% accuracy for the classiﬁcation task (Figure 2 and Table 2), with little variation between models' performances. On the contrary, the leave-site-out CV procedure shows high variability in terms of model performances with relatively good performance for the NYU site and poor performance for the other sites"
- **PMID:local_97b1be33** (score: 0.95): "The overall best performing model was the MM-ensemble, which achieved balanced accuracy of 64% and F1 score of 66%, averaged over the ﬁve-folds of the CV procedure. With the leave- site-out CV procedure the performance of the MM-ensemble dropped to an average balanced accuracy of mean 56% and F1 score of 59%, suggesting that this model does not do well in generalizing to new sites."
- **PMID:local_97b1be33** (score: 0.60): "The code used of all the experiments performed is available on GitHub1."
- **PMID:local_bb07b369** (score: 0.90): "In this study, we used the fMRI data of 816 individuals enrolled in the Autism Brain Imaging Data Exchange (ABIDE) to introduce a new biomarker extraction pipeline for ASD that relies on the use of graph theoretical metrics of fMRI-based functional connectivity to inform a support vector machine (SVM)."
- **PMID:local_bb07b369** (score: 0.95): "Our methodology achieved better results than most state-of-the-art investigations on this dataset with the best model for the >30 years age group achieving an accuracy, sensitivity, and speciﬁcity of 95, 97, and 95%, respectively."
- **PMID:local_bb07b369** (score: 0.90): "we used the preprocessed version of ABIDE I (Di Martino et al., 2014) data publicly available via the Preprocessed Connectome Project (Cameron et al., 2013b). The preprocessing pipeline we used for this study is the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) (Cameron et al., 2013a). Regions of interests (ROIs) were deﬁned as the 116 regions in the automatic anatomical labeling (AAL) atlas (Tzourio-Mazoyer et al., 2002)."
- **PMID:local_bb07b369** (score: 0.70): "Any subject that had a consistently 0 time-series was omitted from the dataset."
- **PMID:local_bb07b369** (score: 0.85): "All Sites 109 342 190 137 51 816 Number of participants from each site for each age group as well as the overall number of participants in a site that were used for this study. Last row shows the total number of subjects in each age-range."
- **PMID:local_bb07b369** (score: 0.90): "We then use a sequential feature selection technique to choose the top 10 features that contribute to this classiﬁcation."
- **PMID:local_bb07b369** (score: 0.90): "We minimized the risk of overﬁtting by using three limiting approaches. First, the simplest kernel (linear) was used for the SVM. Second, only 10 features were used to learn to classify between 104 subjects. Finally, using 10-fold cross validation ensured the model is only evaluated on data points that it has not experienced before."
- **PMID:local_bb07b369** (score: 0.60): "The raw data supporting the conclusions of this manuscript will be made available by the authors, without undue reservation, to any qualiﬁed researcher."
- **PMID:local_e610c0fe** (score: 0.90): "The ABIDE dataset: We present our results on the Autism
Brain Imaging Data Exchange (ABIDE) dataset [4] that con-
tains resting state fMRI data (rs-fMRI) for 1112 patients, as
part of the preprocessed connectomes project"
- **PMID:local_e610c0fe** (score: 0.95): "We follow the same preprocessing pipeline (C-PAC)
and atlases (Harvard-Oxford) as described in [16], in order
to facilitate easy comparison – this resulted in a dataset with
872 of the initial 1112 patients available, from 20 different
sites."
- **PMID:local_e610c0fe** (score: 0.80): "The task is to diagnose a patient as being of two classes
– Autism Spectrum Disorder (ASD) or Typical Control (TC)."
- **PMID:local_e610c0fe** (score: 0.85): "We use the same 10-fold cross validation as in
[7] of the ABIDE dataset, using their publicly released code"
- **PMID:local_e610c0fe** (score: 0.90): "We
out perform recent state of the art method [7] for ASD classiﬁ-
cation by nearly 1.5 percentage points, without any additional
information, and using the exact same training protocol"
- **PMID:local_e610c0fe** (score: 1.00): "Population Graph
Predictive Model
Accuracy
-
Linear SVM[16]
66.8
G
G-CNN [7]
69.50
Proposed
70.86
Naïve Graph
G-CNN [7]
66.93
Proposed
67.85
Noisy G
G-CNN [7]
66.35
Proposed
67.39"
- **PMID:local_c0914f68** (score: 0.90): "The study 
included resting-state fMRI and clinical data from the LEAP and the ABIDE I and II initiatives, 
of 1824 (796 with autism) participants with age range 5-58 years."
- **PMID:local_c0914f68** (score: 1.00): "ALL 
EU-AIMS LEAP 
ABIDE I 
ABIDE II 
 
Autism 
NT 
test 
value, 
p-value 
Autism 
NT 
test 
value, 
p-value 
Autism 
NT 
test 
value, 
p-value 
Autism 
NT 
test 
value, 
p-value 
n 
796 
1028 
.. 
222 
200 
.. 
369 
481 
.. 
205 
347 
.. "
- **PMID:local_c0914f68** (score: 0.60): "Resting-state fMRI and structural scans were obtained using 3T MRI scanners at 32 scanning 
sites (Supplement Section 3)."
- **PMID:local_c0914f68** (score: 0.85): "ComBat (36) was used to remove the confounding 
effects of scanning site from the fMRI data (Supplement Section 4)."
- **PMID:local_c0914f68** (score: 0.80): "To 
assess FC group differences, a general linear model was fitted to each edge, including 
diagnosis, age, sex, and mean framewise displacement (FD) as covariates."
- **PMID:local_c0914f68** (score: 1.00): "At the primary component-forming threshold of p<0.05, the NT>ASD contrast revealed 
hypoconnectivity in autism that encompassed 13,001 edges (17.1% of the total number of 
edges) linking 376 brain regions (pfwe<0.001; Figure 1A-C). The ASD>NT contrast revealed 
hyperconnectivity in autism, including 16,767 edges (22% of the total number of edges; 
pfwe<0.001) and linking all 390 brain regions"
- **PMID:local_c0914f68** (score: 0.75): "To further demonstrate the robustness and replicability of our findings we conducted the full 
FC mapping and analysis of group differences separately in the LEAP and 
ABIDE 1&2 data."
- **PMID:local_57c41fd4** (score: 0.70): "Validation on two datasets, ADNI and ABIDE, demonstrates that DGCL surpasses traditional methods and other deep
learning models in predicting disease development stages."
- **PMID:local_57c41fd4** (score: 0.40): "And the largest dataset for autism research comes
from Autism Brain Imaging Data Exchange (ABIDE) [11]."
- **PMID:local_57c41fd4** (score: 0.80): "For ASD, the ROIs of the dataset can be divided into
eight functional subnetworks: cerebellum and subcortical
structure (CB), visual network (VN), somatic motor network
(SMN), dorsal attention network (DAN), ventral attention
network (VAN), edge network (LN), frontoparietal network
(FPN), and default mode network (DMN)."
- **PMID:local_57c41fd4** (score: 0.85): "Specifically,
the attention score in the SMN region is high, indicating that
connectivity plays a crucial role in ASD prediction in SMN."
- **PMID:local_57c41fd4** (score: 0.85): "In addition, attention scores were higher in the
DMN, DAN, and FPN regions (highlighted in the red box),
indicating that functional connectivity between DMN and
DAN, as well as between DMN and FPN, is also crucial for
predicting ASD"
- **PMID:local_57c41fd4** (score: 0.60): "ABIDE 
PANDA 
7.25 × 102 
0.64 
technician-dependent 
DGCL 
2.19 × 100 
0.71 
highly-automated"
- **PMID:local_57c41fd4** (score: 0.50): "Five-fold 
cross-validation is used to evaluate the performance of the 
model."
- **PMID:local_57c41fd4** (score: 0.40): "our work has two main limitations: one is that the proposed
model still cannot explain the pathogenesis of the detected
abnormal brain connections; the other is that the dataset
used in the current study is relatively small."
- **PMID:local_f732b266** (score: 1.00): "With cross-validation strategy, our proposed method resulted in a mean classification ac-
curacy of 72.2% (sensitivity=68.6%, specificity=75.4%)."
- **PMID:local_f732b266** (score: 0.95): "We successfully downloaded a dataset 
of 1102 subjects from the Preprocessed Connectomes Project, 
and then excluded subjects whose imaging data shows some miss-
ing. Finally, data of 506 ASD individuals and 548 controls was 
included in our study."
- **PMID:local_f732b266** (score: 0.60): "There was no difference in the age, sex and FD between 
cases and controls (p>0.05)."
- **PMID:local_f732b266** (score: 0.85): "The rs-fMRI data utilized in this study was preprocessed with 
the Configurable Pipeline for the Analysis of Conenectomes (C-
PAC). The preprocessing procedure covers the operation of slice 
time and motion corrected, as well as voxel intensity normalized."
- **PMID:local_f732b266** (score: 0.75): "Finally, the 1935 top features were selected to 
perform the differentiation between individuals with ASD and TC 
via the SVM classifier. 
To ensure the reliability of experimental result, we utilized 10-
fold cross-validation to measure the accuracy of predicted label."
- **PMID:local_f732b266** (score: 0.70): "For the challenges of site-related 
variability, we also performed an intra-site prediction based on the 
stratified shuffle split cross-validation."
- **PMID:local_f732b266** (score: 0.90): "Inte-
grated simulation results revealed that the mean score on accuracy, 
sensitivity, and specificity are 72.2%, 68.8%, and 75.4% respectively."
- **PMID:local_f732b266** (score: 0.80): "For the intra-site cross validation, the 
highest accuracy resulted in 71.2%, and the mean classification 
accuracy was 67.7% (sensitivity=66.3%, specificity=68.9%) with a 
range of accuracy of 64.0% to 71.2% in individual folds."
- **PMID:local_f732b266** (score: 0.85): "manifested lower correlation between the anterior and posterior default mode network (DMN) in autis-
tic individuals than controls."
- **PMID:local_c8a23e0a** (score: 1.00): "Results: We collected 79 ASD patients and 105 NCs from the ABIDE-I dataset.
The mean accuracy of our classiﬁcation algorithm was 77.74% for classiﬁcation
of ASD versus NCs."
- **PMID:local_c8a23e0a** (score: 0.95): "The ﬁrst phase of ABIDE (ABIDE-I)
compiles a dataset of 1112 individuals from 17 sites and
consists of 539 individuals with ASD and 573 typical controls. 
Since the scan parameters vary across sites, ABIDE is a highly
heterogeneous dataset. To avoid the impact of data heterogeneity,
we collected raw rs-fMRI data from the whole NYU site,
consisting of 79 ASD subjects and 105 normal controls (NCs)."
- **PMID:local_c8a23e0a** (score: 0.80): "We preprocessed the data using a widely adopted pipeline called
Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC)
(Craddock et al., 2013), which involves skull striping, slice timing
correction, realignment to correct for motion, and bandpass
ﬁltering (0.01–0.1 Hz)."
- **PMID:local_c8a23e0a** (score: 0.75): "The independent
components were derived using Group-ICA, and further inspected to identify eight well deﬁned brain function networks (BFNs). (B) The selected BFNs were used to
extract subject-speciﬁc spatial maps using dual regression."
- **PMID:local_c8a23e0a** (score: 0.60): "A total of 10-fold cross validation strategy was used for evaluating classiﬁcation
performance."
- **PMID:local_c8a23e0a** (score: 0.70): "TABLE 4 | Classiﬁcation results comparison of different network architectures
using 10-fold cross-validation.
Method
Functional
network
ACC
(%)
Precision
(%)
Recall
(%)
F1
score
Baseline
All
69.58
69.43
65.54
67.43"
- **PMID:local_c8a23e0a** (score: 1.00): "MCSE-VGG
All
77.74
76.74
78.57
75.33"
- **PMID:local_c8a23e0a** (score: 0.90): "The SN-dDMN and SN-LCEN pairs showed
increased connectivity strength in ASD, and hypo-connectivity
was observed in the PCUN-dDMN pair of ASD."
- **PMID:local_c8a23e0a** (score: 0.50): "Our ﬁndings support the under-connectivity hypnosis in
autism proposed by Just et al. (2004)."
- **PMID:local_486d7d2c** (score: 0.90): "Four hundred and ﬁfty-four subjects with complete phenotypic
data were selected from the Autism Brain Imaging Data
Exchange (ABIDE) database (http://fcon_1000.projects.nitrc.
org/indi/abide/index.html). The sample consisted of 256 HC, 166
subjects with autism, and 32 subjects with Asperger’s."
- **PMID:local_486d7d2c** (score: 0.60): "Each subject was scanned at
one of the following seven diﬀerent sites: California Institute of
Technology (Caltech), Carnegie Mellon University (CMU), NYU
Langone Medical Center (NYU), University of Pittsburgh School
of Medicine (Pitt), San Diego State University (SDSU), Trinity
Center for Health Sciences (Trinity), and University of California
Los Angeles (UCLA)."
- **PMID:local_486d7d2c** (score: 0.75): "For most of the sites, diagnosis of ASD was consistent with
the Diagnostic and Statistical Manual of Mental Disorders,
Fourth Edition, Text Revision [DSM-IV-TR] criteria [70], and
classiﬁcation of either autism or Asperger’s was made by a
clinician based on the Autism Diagnostic Observation Schedule
[ADOS] [71] and Autism Diagnostic interview-Revised [ADI-
R] [72]."
- **PMID:local_486d7d2c** (score: 0.80): "each rs-
fMRI image was partitioned into 200 (for ADHD, AD, and ASD)
or 125 (for PTSD/PCS) functionally homogenous regions of
interests (ROIs) using spatially constrained spectral clustering
[cc200 template] [76]."
- **PMID:local_486d7d2c** (score: 0.70): "Site-speciﬁc analysis was applied on the ADHD dataset. We
could not apply this analysis on ASD dataset since there was only
one site that had enough samples for HC and disease subgroups"
- **PMID:local_486d7d2c** (score: 0.60): "TABLE 9 | Peak similarity (highlighted), corresponding number of features, and number of clusters obtained using SFR, SFS, and GA with different clustering methods for
ASD dataset."
- **PMID:local_486d7d2c** (score: 0.90): "GA
DPC
75.85
5
3
72.45
60
3
68.98
50
3
OPTICS
76.46
5
3
79.18
103
3
74.47
70
3
Hierarchical
76.63
5
3
89.20
101
3
75.66
54
3"
- **PMID:local_486d7d2c** (score: 0.95): "For ADHD and AD, highest similarity
was achieved between connectivity and phenotypic clusters, whereas for ASD
and PTSD/PCS, highest similarity was achieved between connectivity and clinical
diagnostic clusters."
- **PMID:local_486d7d2c** (score: 0.50): "Data and source code
used in this work is publicly available at https://github.com/xinyuzhao/identiﬁcation-of
-brain-based-disorders.git."
- **PMID:local_4a3d6782** (score: 0.95): "The Autism Brain Imaging Data Ex-
change (ABIDE)1 [39] initiative aggregates resting-state
functional magnetic resonance imaging (rs-fMRI) and phe-
notypic data of 1112 subjects from various international
brain imaging laboratories. We select a set of 871 subjects,
consisting of 403 ASD patients and 468 healthy controls
(HCs)."
- **PMID:local_4a3d6782** (score: 0.85): "For preprocessing of
the ABIDE dataset, we use the Configurable Pipeline for the
Analysis of Connectomes (C-PAC) [41], which includes skull
stripping, slice timing correction, motion correction, global
mean intensity normalization, nuisance signal regression, band-
pass filtering (0.01-0.1Hz), and registration of fMRI images to a
standard anatomical space. Then, the mean timeseries for a set
of cortical and subcortical regions of interest (ROIs) extracted
from the Har"
- **PMID:local_4a3d6782** (score: 0.80): "For the edge weights of the population graph
on the ABIDE datset, we incorporate the subject’s gender, age
and acquisition site as as phenotypic measures."
- **PMID:local_4a3d6782** (score: 0.60): "We use a stratified 10-fold cross-validation strategy."
- **PMID:local_4a3d6782** (score: 0.60): "GCN [15]
64.63
72.23
64.63
86.33
64.63
26.64
30.16"
- **PMID:local_4a3d6782** (score: 1.00): "AN-GCN (Ours)
96.91
96.86
97.16
96.91
97.00
93.76
93.86"
- **PMID:local_4a3d6782** (score: 0.80): "the results show that our model outperforms all the base-
line methods on the ABIDE dataset, achieving relative improve-
ments of 50.33%, 34.10%, 50.33%, 12.25% and 50.33% over
GCN in terms of accuracy, AUC, F1-score, recall and precision,
respectively."
- **PMID:local_4a3d6782** (score: 0.70): "Hence, we take the upper triangular
part and vectorize it to obtain a feature vector whose dimension
is then further reduced using recursive feature elimination via a
ridge classifier."
- **PMID:local_7fdaac96** (score: 0.90): "It compiles a dataset of 1112 R-fMRI par- ticipants by gathering data from 17 diﬀerent sites. Af- ter preprocessing, we selected 871 to meet quality criteria for MRI and phenotypic information."
- **PMID:local_7fdaac96** (score: 0.70): "all participants (871 individuals, 727 males and 144 fe- males, 6 to 64 years old) is the full set of individuals that passed QA"
- **PMID:local_7fdaac96** (score: 0.60): "Data were selected based on the results of quality visual in- spection by three human experts"
- **PMID:local_7fdaac96** (score: 0.80): "We speciﬁcally used the data processed with the Conﬁgurable Pipeline for the Analysis of Connectomes [34] (C-PAC)."
- **PMID:local_7fdaac96** (score: 0.80): "Note that the ROI were all deﬁned on the training set to avoid possible overﬁtting."
- **PMID:local_7fdaac96** (score: 0.80): "This validation with a leave-one- site-out cross-validation strategy reduces the risk of over- ﬁtting data from a single site"
- **PMID:local_7fdaac96** (score: 1.00): "For inter-site prediction, the highest accuracy obtained on the whole dataset is 66.8% (see Table 2) which ex- ceeds previously published ABIDE ﬁndings [53, 13, 54] and chance at 53.7%"
- **PMID:local_7fdaac96** (score: 0.80): "the best predicting pipeline is MSDL, tangent space embedding and l2-regularized classi- ﬁers (SVC-l2 and ridge classiﬁer)"
- **PMID:local_e9fef0b1** (score: 0.90): "We select the same set of 871 subjects used by Abraham et al. (2017) that met the imaging quality and phenotypic information criteria, comprising 403 individuals with ASD and 468 healthy controls. These subjects were regrouped based on location into 20 imaging sites."
- **PMID:local_e9fef0b1** (score: 0.80): "we use the same preprocessing pipeline, the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) (Craddock et al., 2013), which involves skull striping, slice timing correction, motion correction, global mean intensity normalisation, nuisance signal regression, band-pass ﬁltering (0.01- 0.1Hz)"
- **PMID:local_e9fef0b1** (score: 0.70): "the mean time series for a set of regions extracted from the Harvard Oxford (HO) atlas (Desikan et al., 2006) were computed and normalised to zero mean and unit variance"
- **PMID:local_e9fef0b1** (score: 0.70): "We evaluate our model on both the ADNI and ABIDE databases using a 10-fold stratiﬁed cross validation strategy."
- **PMID:local_e9fef0b1** (score: 0.60): "We focus our attention to the phenotypic graph (using default phenotypic measures), which corresponds to the graph constructed taking into account SEX and SITE information, weighted by the feature correlation similarity."
- **PMID:local_e9fef0b1** (score: 0.60): "In Parisot et al. (2017), we used a ridge classiﬁer to perform Recursive Feature Elimination (RFE) with a ﬁxed number of features C. It is an iterative process, where each iteration trains the ridge classiﬁer on the training set with the current feature vector."
- **PMID:local_e9fef0b1** (score: 1.00): "The best average performance is achieved for K = 4 with accuracy 70.4% and AUC 0.75."
- **PMID:local_e9fef0b1** (score: 0.60): "Our experiments suggest that an accuracy of approx. 70% could be an intrinsic limitation of the whole dataset."
- **PMID:local_1cbc0566** (score: 0.80): "We attempted to replicate the method and results using the Autism Brain Imaging Data Exchange (ABIDE) including resting state fMRI data obtained from 964 subjects and 16 separate international sites."
- **PMID:local_1cbc0566** (score: 0.90): "A total of 964 subjects met all inclusion criteria (517 typically developing subjects and 447 subjects with autism from 16 sites)."
- **PMID:local_1cbc0566** (score: 0.60): "Inclusion criteria for subjects were successful preprocessing with manual visual inspection of normalization to MNI space of MPRAGE, coregistration of BOLD and MPRAGE images, seg- mentation of MPRAG"
- **PMID:local_1cbc0566** (score: 0.60): "Motion scrubbing (Power et al., 2012) of framewise dis- placement and DVARS with removal of volumes before and after a root-mean-square displace"
- **PMID:local_1cbc0566** (score: 0.70): "Overall, a leave-one-out classiﬁer was used to generate a classiﬁcation score for each of the 964 subjects, leaving out one subject at a time and calculating the classiﬁcation score for the left out sub- ject."
- **PMID:local_1cbc0566** (score: 0.60): "Age, age-squared, gender, handedness, and site were included as covariates for the classiﬁer."
- **PMID:local_1cbc0566** (score: 1.00): "As high as 60% accuracy was obtained for whole brain classiﬁcation, with the best accuracy from connections involving regions of the default mode network, parahippocampaland fusiform gyri, insula, Wernicke Area, and intraparietal sulcus."
- **PMID:local_1cbc0566** (score: 0.80): "Multisite functional connectivity classiﬁcation of autism outperformed chance using a simple leave-one-out classiﬁer, but exhibited poorer accuracy than for single site results."
- **PMID:local_87840d2a** (score: 0.80): "we demonstrate the model performance on the functional connectivity graphs of 871 subjects from the challenging Autism Brain Imaging Data Exchange (ABIDE) database [5], which contains heterogeneous rs-fMRI data acquired at multiple"
- **PMID:local_87840d2a** (score: 0.90): "It includes N = 871 subjects from diﬀerent imaging sites that met the imaging quality and phenotypic information criteria, consisting of 403 individuals suﬀering from ASD and 468 healthy con- trols."
- **PMID:local_87840d2a** (score: 0.70): "has been preprocessed by the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) [2], which involves skull striping"
- **PMID:local_87840d2a** (score: 0.70): "We, subsequently, extract the mean time series for a set of regions from the Harvard Oxford (HO) atlas comprising R = 110 cortical and subcortical ROIs [4] and normalise them to zero mean and unit variance."
- **PMID:local_87840d2a** (score: 0.60): "We also ensure that subjects from all 20 sites are included in both training and test sets."
- **PMID:local_87840d2a** (score: 1.00): "Table 1: k-nn classiﬁcation results with k = 3 using the proposed metric and Euclidean distance following PCA. Classiﬁcation all sites site 6 site 9 site 14 site 16 site 18 PCA/Euclidean 51.0% 59.3% 25.0% 30.0% 64.3% 50.0% GCN 62.9% 81.5% 62.5% 70.0% 50.0% 90.0%"
- **PMID:local_87840d2a** (score: 1.00): "improving the performance of a simple k-nn classiﬁer by 11.9% compared to a traditional distance metric"
- **PMID:local_87840d2a** (score: 0.50): "source code available at https://github.com/sk1712/gcn_metric_learning"
- **PMID:local_9e370311** (score: 0.90): "We incorporated data from 529 ASD individuals and 573 typical controls (TC) for each pipeline, which is comprised of 17 different imaging sites."
- **PMID:local_9e370311** (score: 0.80): "Selected strategies are Connectome Computation System (CCS), Conﬁgurable Pipeline for the Analysis of Con- nectomes (CPAC), Data Processing Assistant for Resting-State fMRI (DPARSF) and Neuroimaging Analysis Kit (NIAK)."
- **PMID:local_9e370311** (score: 0.70): "in this work, ﬁrstly, we design an image genera- tor to generate single volume brain images from the whole-brain image of each subject."
- **PMID:local_9e370311** (score: 0.70): "we ﬁrst divided the whole dataset into two parts: training (85%), and testing (15%). From the generated training images, approximately 85% of the whole images were considered as the training set, and 15% as the validation set."
- **PMID:local_9e370311** (score: 0.60): "Table V represents the classiﬁcation performance for ensemble learning showing that the third ensemble classiﬁer performs better than other ensembles."
- **PMID:local_9e370311** (score: 1.00): "In our experiments, the highest accuracy for glass brain images is up to 85% belongs to several data sites and for stat map images the accuracy is up to 84% for several data sites as shown in the table."
- **PMID:local_9e370311** (score: 0.50): "therefore we performed unit-site classiﬁcation to pattern out"
- **PMID:local_4a257bf0** (score: 0.80): "Additional 27 individuals with ASD from the ABIDE resting-state database were included to  test the reproducibility of the results."
- **PMID:local_4a257bf0** (score: 0.80): "We selected only ASD participants from the ABIDE database since diagnostic scores were  not available for controls. We selected the same 5 datasets used in (1), that is sites with  codes: 'CALTECH' (n=19), 'CMU' (n=14), 'PITT' (n=30), 'UM_1' (n=55), 'UM_2' (n=13) for  a total of 131 ASD participants."
- **PMID:local_4a257bf0** (score: 0.90): "This yielded 27 subjects with IDs: 51457, 51464, 51468,  51474, 50642, 50643, 50645, 50646, 50647, 50649, 50651, 50652, 50653, 50655, 50002,  50003, 50004, 50006, 50007, 50012, 50016, 50019, 50022, 50024, 50025, 50053, 50056."
- **PMID:local_4a257bf0** (score: 0.60): "We applied scrubbing so that we kept 125 volumes with lowest framewise displacem"
- **PMID:local_4a257bf0** (score: 0.60): "Code used in this paper is available at  https://github.com/eglerean/hfASDmodules."
- **PMID:local_4a257bf0** (score: 1.00): "When repeating the intersubject similarity analysis for the 27 ABIDE participants, we  obtained similar results as those for the within ASD group i.e. only the VTL subnetwork  showed significant correlation between subnetwork intersubject similarity and joint ADI- R/ADOS score similarity (p=0.0287) with moderate effect size (r = 0.17, Figure S4)."
- **PMID:local_4a257bf0** (score: 0.50): "Between-group differences were observed in the composition of default-mode and a ventro- temporal-limbic (VTL) subnetwork."
- **PMID:local_44b7e3b7** (score: 0.90): "Speciﬁcally, the 507 subjects included 209 subjects with ASD and 298 well-matched health controls across 14 sites from the Autism Brain Imaging Data Exchange (ABIDE)."
- **PMID:local_44b7e3b7** (score: 0.80): "Only subjects with FIQ within 2 SD + mean across all the Autism Brain Imaging Data Exchange (ABIDE) samples and with mean framewise displacement (FD) below 2 SD + mean were included."
- **PMID:local_44b7e3b7** (score: 0.70): "All the preprocessing of resting state-fMRI was performed using the Statistical Parameter Mapping 8 (SPM8)"
- **PMID:local_44b7e3b7** (score: 0.70): "it was based on the automated anatomical labeling (AAL) template extract the averaged fMRI time series"
- **PMID:local_44b7e3b7** (score: 0.70): "we ﬁrst applied a data-driven algorithm that maximized the p-values of the group diﬀerence of age, FIQ, and mean FD (using two-sample t-tests). Then, to exclude the inﬂuence of the site interaction eﬀect, we"
- **PMID:local_44b7e3b7** (score: 1.00): "compared to HCs, we found that fractional occupancies of HMM states 4, 8, 9, and 10 for ASD subjects were signiﬁcantly decreased"
- **PMID:local_44b7e3b7** (score: 0.90): "And fractional occupancies 2, 3, 14, and 17 for ASD were signiﬁcantly increased"
- **PMID:local_44b7e3b7** (score: 0.50): "two-tailed two-sample, Bonferroni correction"
- **PMID:local_013df539** (score: 0.90): "Anatomical and functional data from fifty-five subjects with ASD (12.7 ± 2.4 y/o) and 55 age- matched (14.1 ± 3.1 y/o) healthy controls were accessed through the NITRC database and the ABIDE project."
- **PMID:local_013df539** (score: 0.60): "Diagnosis was established with the Autism Diagnostic Observation Schedule (ADOS) [39], the Autism Diagnostic Interview Revised (ADI-R) [40] as well as clini- cal consensus."
- **PMID:local_013df539** (score: 0.70): "The 240 regions of interest (ROIs) defined for this study were extracted from the TT_Daemon human brain atlas [43] provided with the AFNI package [44]."
- **PMID:local_013df539** (score: 0.60): "The rs-BOLD data were corrected for motion artifacts using a time series general affine registration for 12 parameters (3dWarpDrive/AFNI)."
- **PMID:local_013df539** (score: 1.00): "We found that the main regions, where signal complexity significantly decreased among ASD patients, were the amygdala (p = 0.001), the vermis (p = 0.02), the basal ganglia (p = 0.01) and the hippocampus (p = 0.02)."
- **PMID:local_013df539** (score: 0.70): "This indicates that there were no regions where signal complexity signifi- cantly increased respect to controls among the ASD patients."
- **PMID:local_013df539** (score: 0.80): "Overall, we found reduced signal complexity in the ASD subjects with respect to controls."
- **PMID:local_013df539** (score: 0.40): "We downloaded data from the publicly accessible ABIDE-1 database: http://fcon_1000.projects.nitrc.org/indi/abide/ abide_I"
- **PMID:local_af69918d** (score: 0.70): "In the current study, ABIDE sites were included that (i) deposited raw 
resting-state functional Magnetic Resonance Imaging (MRI) scans (i.e., no motion correction or “scru"
- **PMID:local_af69918d** (score: 0.70): "Seven of 16 ABIDE sites met these overall inclusion criteria: University of Michigan, Sample 1 
and Sample 2 (“UM_1” and “UM_2”, respectively), University of Utah School of Medicine (“USM”), New York 
University Langone Medical Center (“NYU”), University of California, Los Angeles, Sample 1 (“UCLA_1”), Olin, 
Institute of Living at Hartford Hospital (“OLIN”), and University of Pittsburgh School of Medicine (“PITT”)."
- **PMID:local_af69918d** (score: 0.90): "Datasets from a total of 605 participants were analyzed, including 304 individuals with Autism Spectrum 
Disorder (ASD) and 301 typically developing controls (CT)."
- **PMID:local_af69918d** (score: 1.00): "We 
find excess noise and randomness in the ASD cases, suggesting an uncertain motor-feedback signal."
- **PMID:local_af69918d** (score: 0.70): "In ASD, deleterious patterns of noise are consistently exacerbated 
with the presence of secondary (comorbid) neuropsychiatric diagnoses, lower verbal and performance 
intelligence, and autism severity."
- **PMID:local_af69918d** (score: 0.60): "Importantly, such patterns in ASD are present whether or not the 
participant takes psychotropic medication."
- **PMID:local_af69918d** (score: 0.60): "The output with the six motion parameters (3 translations in x, y, z directions, 
and 3 rotations: pitch (about x-axis), roll (about y-axis), and yaw (about z-axis)) is recor"
- **PMID:local_19021604** (score: 0.80): "In this study, we consider the ABIDE I preprocessed dataset (Di Martino
et al., 2014; Craddock et al., 2013). It includes BOLD time-series extracted
from rs-fMRI through a preprocessing pipeline which is fully detailed on the web
platforms related to the ABIDE collection"
- **PMID:local_19021604** (score: 0.80): "The time-series consid-
ered in our work were preprocessed according to the C-PAC pipeline, which
involves the following main steps: basic processing, noise signal removal, global
regression, band-pass ﬁltering (0.01-0.1 Hz), registration, time-series extrac-
tion"
- **PMID:local_19021604** (score: 0.70): "The selected mean time-series
correspond to the Automated Anatomical Labeling atlas on 90 regions of interest
(AAL90)"
- **PMID:local_19021604** (score: 0.90): "we consider patients who meet
the following inclusion criteria:
• eyes opened during fMRI acquisition;
• less than 18 years old;
• less than 0.2 mm in mean framewise displacement."
- **PMID:local_19021604** (score: 0.90): "The corresponding data subset consists of a total of 452 subjects, with respec-
tively 251 NT and 201 ASD subjects."
- **PMID:local_19021604** (score: 0.50): "Given the limited size of the dataset, we
co"
- **PMID:local_19021604** (score: 0.80): "In terms of classiﬁcation
accuracy, our framework outperforms other state-
of-the-art methods that are based on either the structural or the functional connectivity, i.e., the Graph Fourier Transform - GFT"
- **PMID:local_19021604** (score: 0.70): "The analysis of the results reveals the inﬂuence of the frontal and temporal
lobes in the diagnosis of the disorder.
This
ﬁnding is consistent with
previous reports of the literature of neuroscience."
- **PMID:local_33bed9bf** (score: 0.90): "ABIDE I dataset consists of 1112 
total samples including 539 patients and 573 typical 
controls (TC) subjects. While ABIDE II dataset consists 
of 1114 total samples with 521 patients and 573 
typical controls (TC) subjects."
- **PMID:local_33bed9bf** (score: 0.80): "The original format of the image dataset is NIfTI-1 
data format file (NII format) which is in 3-Dimensional 
(3D) form. MRIcron software was used to convert the 
3D data format into 2D data images."
- **PMID:local_33bed9bf** (score: 0.70): "In this research, the axial plane is used 
as the input samples."
- **PMID:local_33bed9bf** (score: 0.60): "The samples were separated into two folders 
which were the training file and test file."
- **PMID:local_33bed9bf** (score: 1.00): "The results achieved using CNN models namely 
VGG-16 and ResNet-50 are 63.4% and 87.0% accuracy, respectively."
- **PMID:local_33bed9bf** (score: 0.90): "The best CNN model in this project was 
achieved by ResNet50, with an accuracy of 87.0%."
- **PMID:local_33bed9bf** (score: 0.60): "The performance of the CNN pre-trained model was 
evaluated using several measurements such as 
recall, precision, and accuracy."
- **PMID:local_81234492** (score: 1.00): "we selected a 
subgroup of 190 subjects (102 with ASD and 88 TD) according to the following criteria: male 
children (age range: 6.5–13 years); rs-fMRI data acquired with open eyes; data from the 
University sites that provided the largest number of scans (KKI, NYU, UCLA, UM)."
- **PMID:local_81234492** (score: 0.90): "We analyzed the preprocessed data available on the ABIDE 
preprocessed homepage (29, 30), using the Configurable Pipeline 
for the Analysis of Connectomes (CPAC) (31), that includes slice-
timing, motion correction, intensity normalization, nuisance 
signal removal (e.g. tissue signals, low-frequency drifts), and 
registrations."
- **PMID:local_81234492** (score: 0.80): "Both anatomical and functional atlases were chosen to derive the 
FC measures; in particular, we chose Harvard-Oxford (HO) and 
Automatic Anatomical Labeling (AAL) as anatomical templates 
and Craddock-200 (CC) as functional templates to extract time 
series from brain regions"
- **PMID:local_81234492** (score: 0.90): "a leave-site out cross-validation scheme was performed: 
each training set was composed by all the sites except one, that 
was left out for validation."
- **PMID:local_81234492** (score: 1.00): "The mean L-SVM classification performance, 
in terms of the area under the ROC curve (AUC), was 0.75 ± 0.05. The highest performance 
was obtained using data from KKI, NYU and UCLA sites in training and data from UM as testing 
set (AUC = 0.83)."
- **PMID:local_81234492** (score: 0.90): "Specifically, stronger functional connectivity (FC) in ASD with respect to TD 
involve (p < 0.001) the angular gyrus with the precuneus in the right (R) hemisphere, and the 
R frontal operculum cortex with the pars opercularis of the left (L) inferior frontal gyrus."
- **PMID:local_81234492** (score: 1.00): "implementation of the HO atlas. The binary classification 
results between subjects with ASD and controls in a leave-one-
site-out cross-validation scheme achieved an average accuracy 
of 0.71 ± 0.06 and an average AUC of 0.75  ± 0.05."
- **PMID:local_81234492** (score: 0.50): "DATA AVAILABILITY
Publicly available datasets were analyzed in this study. This data 
can be found here: http://fcon_1000.projects.nitrc.org/indi/abide/"
- **PMID:local_730ab177** (score: 1.00): "The rs-fMRI data used in this study were sourced from
the ABIDE I dataset, comprising 505 autistic individuals and
530 typical controls (TCs)."
- **PMID:local_730ab177** (score: 0.90): "The data is preprocessed using the Conﬁgurable Pipeline for
the Analysis of Connectomes (CPAC) pipeline, which includes
essential steps such as slice timing correction, voxel intensity
normalization, motion correction, nuisance signal removal, global
signal regression, band-pass ﬁltering, and spatial registration."
- **PMID:local_730ab177** (score: 0.90): "After preprocessing and quality control, the ﬁnal dataset consists
of 1,035 samples distributed as follows: 623 samples for the
training set, 308 samples for the validation set, and 104 samples
for the test set."
- **PMID:local_730ab177** (score: 0.80): "Functional connectivity matrices are derived from three brain
atlases (AAL, CC, EZ) using Pearson correlation coeﬃcients, which
are ﬂattened into one-dimensional vectors."
- **PMID:local_730ab177** (score: 1.00): "Results: The proposed model is evaluated using multiple ASD datasets. The
performance metrics include an average accuracy of 0.735, sensitivity of 0.765,
and speciﬁcity of 0.752, surpassing the results of existing state-of-the-art
methods."
- **PMID:local_730ab177** (score: 0.90): "our developed
MHOA based on the SSDAE model has accuracy 66.35%, 70.19%,
and 83.82% for EZ, AAL, and CC, respectively."
- **PMID:local_730ab177** (score: 0.50): "Data availability statement
Publicly available datasets were analyzed in this study. This data
can be found here: https://www.nature.com/articles/s41598-022-
09821-6."
- **PMID:local_7424ae8d** (score: 1.00): "we used the same 871 samples from the ABIDE 1 data set [23], [24], [25]. Of the 871 subjects, 403 patients were ASD and 468 were TC patients."
- **PMID:local_7424ae8d** (score: 0.80): "In this study, we used multiscale functional brain parcels. Brain parcels were created using a method known as the bootstrap analysis of stable clusters called BASC [32]. Scales were selected using a data- based method called MSTEPS [33]. There are different scales in this method. In this study, the scale is set to 122."
- **PMID:local_7424ae8d** (score: 0.60): "An edge between a pair of ROIs is usually weighted with the Pearson correlation coefficient (PCC)."
- **PMID:local_7424ae8d** (score: 0.80): "Tests on the ABIDE I data set were carried out using the 10-fold cross-validation method. The main purpose of this process is to use each data for both training and testing."
- **PMID:local_7424ae8d** (score: 1.00): "Table 2 Average classification performances 
METHOD 
ACC 
SENS 
SPEC 
RNN 
74.74 
72.95 
76.28"
- **PMID:local_7424ae8d** (score: 0.90): "Table 2 shows the average classification performances obtained by 10-fold cross-validation tests. When the classification results are examined, it is seen that the highest performance value is provided by RNN with 74.74%."
- **PMID:local_62eceeaf** (score: 1.00): "The data used in the current study were provided by ABIDE I ( http://fcon_1000.projects.nitrc.org/indi/abide/), and we use all 1102 subjects (ﬁlter_noglobal) processed by the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) [22] for experiments."
- **PMID:local_62eceeaf** (score: 0.90): "We conduct experiments on all ABIDE I data (without any data screening), and obtain the mean 73.1%/73.4% accu-
racy on AAL/CC200 atlas"
- **PMID:local_62eceeaf** (score: 0.90): "To validate the effectiveness of the proposed LRCDR
method, we conduct inter-site cross-validation experiments on
17 sites from ABIDE database. Speciﬁcally, one site is left
as the target domain for testing, and the remaining 16 sites
as multiple source domains for training."
- **PMID:local_62eceeaf** (score: 0.70): "The mean time series from 116 regions of interest (ROIs)
based on the automated anatomical labeling (AAL) atlas [23] are used for experiments."
- **PMID:local_62eceeaf** (score: 0.90): "We also use the Craddock 200 (CC200) atlas [31] to
further verify the effectiveness of the LRCDR method and obtain the 73.4% mean accuracy."
- **PMID:local_62eceeaf** (score: 1.00): "For inter-site prediction on all ABIDE I data
(1102 subjects from 17 sites), LRCDR obtains the mean
accuracy of 73.1%, superior to the results of the compared
state-of-the-art domain adaptation methods and multi-site
ASD identiﬁcation methods."
- **PMID:local_62eceeaf** (score: 0.70): "In addition, we locate some
meaningful biomarkers: Most of the top important biomark-
ers are inter-network resting-state functional connectivi-
ties (RSFCs)."
- **PMID:local_88791905** (score: 1.00): "We limited ourselves to
acquisitions with repetition time of 2s (sites NYU, SDSU, UM, USM). This
resulted in a dataset of 147 subjects with ASD and 146 healthy controls."
- **PMID:local_88791905** (score: 0.80): "The pre-processed acquisitions are
available as part of the Pre-processed Connectome Project (http://preprocessed- connectomes-project.org/abide/, C-PAC pipeline)."
- **PMID:local_88791905** (score: 0.80): "We
extracted rsfMRI time series using a 200-region parcellation CC200[?], estimated
subject-wise time-resolved connectivity matrices with windows lengths ranging
from 10 to 20 volumes (20-40s) and calculated node variability."
- **PMID:local_88791905** (score: 0.80): "For inter-site, we employed a leave-
one-out-site approach that involved training the classiﬁer on all the sites
except the one left out for testing."
- **PMID:local_88791905** (score: 1.00): "Our analysis revealed that pa-
tients diagnosed with autism spectrum disorder (ASD) show increased
FC variability in several brain regions that are associated with low FC
variability in the typical brain."
- **PMID:local_88791905** (score: 0.90): "We then used the enhanced FC variability
of brain regions as features for training machine learning models for ASD
classiﬁcation and achieved 65%"
- **PMID:local_88791905** (score: 0.90): "Table 1 summarizes the performance of diﬀerent
classiﬁers on intra-site ASD prediction. The accuracy achieved by all classiﬁers
is comparable and is around 60%. The sensitivity varies between 60 to 65%. The
speciﬁcity is ˜60% for SVM and MLP, whereas RF and NB produce slightly lower
speciﬁcity."
- **PMID:local_88791905** (score: 0.90): "The results on inter-site classiﬁcation are presented in Table 3. Whereas
the classiﬁcation accuracy using MLP is ˜62% for all sites, the speciﬁcity and
sensitivity vary across sites, consistent with the results shown in Figure 1b."
- **PMID:local_696781dc** (score: 1.00): "This paper carries out research on the challenging public ABIDE I dataset [31], which 
aggregates data from 17 different international collection sites, sharing neuroimaging 
and phenotype data of 1112 subjects. In the experiment, 871 subjects (including 403 
ASD patients and 468 healthy controls) who meet the imaging quality and atypical 
information criteria were used."
- **PMID:local_696781dc** (score: 0.90): "Data preprocessing was performed using the configurable pipeline for the analysis of con- 
nectomes. According to the Harvard-Oxford atlas, there are 111 ROIs in the brain 
[32]."
- **PMID:local_696781dc** (score: 0.80): "a 10-fold cross-validation schema that mixes data from all 17 sites while keeping"
- **PMID:local_696781dc** (score: 1.00): "The proposed method is assessed on the autism brain imaging data 
exchange (ABIDE) repository. In total, 871 subjects in the ABIDE I dataset are used 
for the classification task. The best classification accuracy of 82.9% is achieved."
- **PMID:local_696781dc** (score: 1.00): "The proposed HCAN method achieves an average ACC of 82.9%, 
SEN of 76.7%, SPE of 86.6% and AUC of 84.6%."
- **PMID:local_696781dc** (score: 0.50): "Availability of data and materials
The datasets analysed during the current study are available from a world-wide multi-site database Autism Brain Imaging 
Data Exchange (ABIDE I) (http://​prepr​ocess​ed-​conne​ctomes-​proje​ct.​org/)."
- **PMID:local_3a3f7f6a** (score: 1.00): "we conducted the experiment on the publicly available ABIDE-I
dataset, including rs-fMRI and phenotypic data of 1112 sub-
jects from 17 different sites (Di Martino et al., 2014; Crad-
dock et al., 2013). In current study, we utilized rs-fMRI data
from 848 subjects, including 396 patients with ASD and 452
health controls (HCs)."
- **PMID:local_3a3f7f6a** (score: 0.70): "we used the data Processing As-
sistant for Resting-State fMRI (DPARSF) t"
- **PMID:local_3a3f7f6a** (score: 0.80): "(1) Discarding the first 5 volumes. (2) Correct-
ing of slice-related delay. (3) Correcting head movement.
(4) Using EPI template normalization in MNI space, resam-
pling to 3 mm resolution of 3 × 3 × 3. (5) Smoothing with a
4 mm full-width at half-maximum (FWHM) Gaussian ker-
nel. (6) Linear detrending and temporal band-pass filter-
ing of BOLD signal (0.01-0.10 Hz)."
- **PMID:local_3a3f7f6a** (score: 0.80): "we use the Automated Anatomical Labeling (AAL) tem-
plate (Tzourio-Mazoyer et al., 2002) to divide the brain into"
- **PMID:local_3a3f7f6a** (score: 0.80): "In our experiment, we employed the 10-fold cross-
validation strategy to conduct the comparison among dif-
ferent models."
- **PMID:local_3a3f7f6a** (score: 0.70): "The code is available
at https://github.com/LYQbyte/ASD-HNet."
- **PMID:local_3a3f7f6a** (score: 1.00): "ASD-HNet
73.57
72.63
74.90
71.04
-"
- **PMID:local_6a54db71** (score: 1.00): "This study included 1112 ABIDE I datasets 
from 17 sites and 983 ABIDE II datasets from 16 sites. The ABIDE datasets were obtained online15. In total, 2095 
ABIDE datasets were used (ASD: 1001 and TD: 1094; 5–64 years)."
- **PMID:local_6a54db71** (score: 0.90): "We recruited 21 patients with ASD and 23 individuals with neurotypical development (TD)."
- **PMID:local_6a54db71** (score: 0.80): "We subsequently applied 
dual-regression analysis18 by using the FSL general linear model (GLM) and the 10-brain resting-state networks 
(RSN10), “PNAS_Smith09_rsn10.nii.gz,” provided by Smith et. al.19,20 as a reference."
- **PMID:local_6a54db71** (score: 0.90): "(1) FC val-
ues significantly different [family-wise error (FWE)-corrected p < 0.05] between the ASD and TD groups and (2) 
voxels inside the corresponding R-masks to create A1–A20 masks (ASD > TD: A1 to A10 and ASD < TD: A11 to 
A20)."
- **PMID:local_6a54db71** (score: 1.00): "The results indicated that the biomarkers 
generated from the default mode and executive control networks significantly differed between the 
participants with ASD and TD. In particular, the biomarkers derived from the default mode network 
were negatively correlated with the raw scores and model factors of the SRS."
- **PMID:local_6a54db71** (score: 0.90): "The results of this study indicate that the FC of DMN in the ASD group was 
weaker than that of the TD group."
- **PMID:local_6a54db71** (score: 0.90): "The areas 
under the curve (AUCs) for the biomarkers were (0.590, 0.745, p < 0.05), (0.588, 0.646), and (0.646, 0.677) for 
(R4, A4), (R5, A15), and (R8, A18), respectively."
- **PMID:local_6a54db71** (score: 0.60): "The pipelines, as well as the 30 masks of this study, are available28. The 
open-science materials and tools, including the RSN10 template, C-PAC, ABIDE, and our pipeline, can be used 
to replicate the methods of this study."
- **PMID:local_6a54db71** (score: 0.50): "Data Availability
The datasets generated during and/or analyzed during the current study are available from the corresponding 
author on reasonable request."
- **PMID:local_904dfa27** (score: 1.00): "we conducted mega- and meta-analyses of resting-state functional magnetic resonance imaging data of 939 participants (440 ASD patients and 499 healthy controls, all males) from 18 independent sites, selected from the ABIDE (Autism Brain Imaging Data Exchange) dataset."
- **PMID:local_904dfa27** (score: 0.80): "had maximal head motion of less than 5 mm and 5 degrees, and mean framewise displacement (FD) (1) of less than 0.5 mm"
- **PMID:local_904dfa27** (score: 0.90): "Thus, after all selection criteria had been applied, we obtained a dataset consisting of scans from 939 participants (ASD/HC, 440/499) taken from 18 different sites"
- **PMID:local_904dfa27** (score: 0.80): "All rsfMRI data were preprocessed with a standardized and harmonized pipeline using the GRETNA package (36)."
- **PMID:local_904dfa27** (score: 0.70): "network nodes were defined as 512 regions of interest with uniform areas obtained from a random parcellation (38)"
- **PMID:local_904dfa27** (score: 1.00): "the ASD group showed a higher mean value (Cohen’s d = .18, p = .007) and a lower standard deviation (Cohen’s d = -.19, p = .004) in whole-brain modular variability than the HC group"
- **PMID:local_904dfa27** (score: 1.00): "the ASD group showed higher modular variability mainly in several default-mode regions, including the medial prefrontal cortex, posterior cingulate gyrus, and angular gyrus (Cohen’s d ranging from .19 to .33), and lower variability primarily in the visual cortex (Cohen’s d ranging from -.24 to -.19) (FDR corrected p < .05)"
- **PMID:local_904dfa27** (score: 0.90): "we found that brain dynamics was a significant predictor of SRS scores (r = .16, pperm = .002)"
- **PMID:local_904dfa27** (score: 0.70): "We performed a leave-one-site-out cross-validation to assess whether our main findings were biased by site specific sites."
- **PMID:local_d46bcf61** (score: 1.00): "DSM-IV-TR diagnosed Asperger’s disorder (n = 79), pervasive developmental disorder-not otherwise specified [PDD-NOS] (n = 58) and Autistic disorder (n = 92) from ABIDE II were used as discovery cohort, and ABIDE I (n = 400) was used for replication."
- **PMID:local_d46bcf61** (score: 0.90): "Subjects with ASD (n = 229) and the corresponding TDCs (n = 126) were selected from the ABIDE II [29, 30], which is hosted by the 1000 Functional Connectome Project/International Neuroimaging Data-sharing Ini- tiative (INDI) from multiple international sites (9 sites, Additional file 1: Table S1)."
- **PMID:local_d46bcf61** (score: 0.80): "we removed outlier datasets with mean FD exceeding 1 mm, as well as head motion exceeding 2.0 mm of maximal translation (in any direction of x, y or z) or 1.0° of maximal rotation through- out the course of scanning."
- **PMID:local_d46bcf61** (score: 0.70): "to calculate fALFF [34], the sum of the spectral amplitude values in the 0.01–0.08 Hz low-frequency power range was divided by the sum of the amplitudes over the entire detectable power spectrum (range: 0–0.25 Hz)."
- **PMID:local_d46bcf61** (score: 0.80): "the preprocessed multimodal MRI features were jointly analyzed by a fusion-with-reference model called “MCCAR + jICA”"
- **PMID:local_d46bcf61** (score: 0.90): "Dorsolateral prefrontal cortex and superior/middle temporal cortex are the primary common functional– structural covarying cortical brain areas shared among Asperger’s, PDD-NOS and Autistic subgroups."
- **PMID:local_d46bcf61** (score: 0.90): "negative fALFF in anterior cingulate cortex unique to PDD-NOS subtype; and negative thalamus–amygdala–caudate fALFF unique to the Autistic subtype."
- **PMID:local_d46bcf61** (score: 1.00): "The identified subtype-specific patterns are only predictive for ASD symptoms manifested in the corresponding subtypes, but not the other subtypes."
- **PMID:local_d46bcf61** (score: 0.90): "models can be generalized to predict ADOS and SRS scores for the corresponding subgroup from ABIDE I, but not for the other groups"
- **PMID:local_d46bcf61** (score: 0.70): "site-out analysis (details can be found in Additional file 1: “Reproducibility” section) in the ADOS-guided fALFF and GMV fusion on the whole ASD group to check whether the site effect will contribute to current ASD pattern."
- **PMID:local_a8b1e837** (score: 1.00): "We generated voxel-wise maps of fALFF and ReHo for a total of 1983 subjects from the ABIDE I and ABIDE II datasets (ASD = 916, CTL = 1067"
- **PMID:local_a8b1e837** (score: 1.00): "After the removal of subjects with image artifacts, high head movement, or poor MNI152 coregistration, we analyzed the data from the remaining 710 ASD (79% male), and 606 CTL (87% male) subjects, whose age ranges from 5 to 64 years."
- **PMID:local_a8b1e837** (score: 0.80): "scans meeting at least one of these three requirements were removed: (1) mean FWD > 0.30 mm, (2) greater than 50% of frames being scrubbed, or (3) scans with outlier mean, 1st, 2nd, or 3rd quantile DVARS values."
- **PMID:local_a8b1e837** (score: 0.80): "The package CPAC v1.8.0 was used for fMRI pre-processing including head motion correction, scrubbing, and nuisance regression."
- **PMID:local_a8b1e837** (score: 0.70): "We used the resulting 11 region atlas to assign a region label"
- **PMID:local_a8b1e837** (score: 0.70): "To reduce the impact of confounders, we regressed out age, site, and sex using a linear model."
- **PMID:local_a8b1e837** (score: 1.00): "415 differentially corre- lated genes (DC genes; Diff Cor P < 0.01, CTL FDR < 0.05"
- **PMID:local_a8b1e837** (score: 0.80): "DC genes showed an effect size larger than 1.8, resulting in ~3% of the gene expressed in our data"
- **PMID:local_a8b1e837** (score: 0.60): "our study includes ages from 5 to 64 years and data from 37 sites"
- **PMID:local_45051796** (score: 1.00): "we obtained a final sample of 1383 subjects (680 ASD and 703 TD) from 35 sites."
- **PMID:local_45051796** (score: 0.90): "To allow the reproducibility of the analysis, the identification numbers (IDs) of the participants selected in the final sample are reported in Additional file 1."
- **PMID:local_45051796** (score: 0.80): "The rs-fMRI scans selected from ABIDE I and ABIDE II cohorts were processed with the Configurable Pipe- line for the Analysis of Connectomes (C-PAC) [20]"
- **PMID:local_45051796** (score: 0.80): "The Harvard-Oxford (HO) atlas was used to extract time series from brain regions, obtaining 110 timeseries for each subject."
- **PMID:local_45051796** (score: 0.70): "62 structures (31 per hemisphere) from the Desikan-Killiany- Tourville Atlas"
- **PMID:local_45051796** (score: 0.90): "We esti- mated the NeuroHarmonize model parameters on the entire cohort of control subjects, by specifying the age as a covariate, whose effect is to be preserved during the harmonization process. Finally, we applied the esti- mated model on the entire sample of subjects with ASD and TD controls."
- **PMID:local_45051796** (score: 0.80): "The model was trained to distinguish subjects with ASD from TD according to a nested 10-fold cross-validation scheme."
- **PMID:local_45051796** (score: 1.00): "The AUC values of 0.66±0.05 and of 0.76±0.04 were obtained in the ASD vs. TD discrimination when only structural or functional features are considered, respectively. The joint fusion approach led to an AUC of 0.78±0.04."
- **PMID:local_45051796** (score: 0.80): "brain changes tend to occur in individuals with ASD in regions belonging to the Default Mode Network and to the Social Brain."
- **PMID:local_8e16e9b1** (score: 1.00): "This dataset consists 1,035 rs-fMRI data with 505 ASD subject, and 530 healthy control subjects that are collected from 17 diﬀerent sites."
- **PMID:local_8e16e9b1** (score: 0.80): "We used the preprocessed data using the Conﬁgurable Pipeline for the Analysis of Connectomes C-PAC pipeline (Craddock et al., 2013)"
- **PMID:local_8e16e9b1** (score: 0.80): "Craddock 200 (CC200) functional parcellation (Craddock et al., 2012)"
- **PMID:local_8e16e9b1** (score: 1.00): "ASD-SAENet exhibits comparable accuracy (70.8%), and superior speciﬁcity (79.1%) for the whole dataset as compared to other methods."
- **PMID:local_8e16e9b1** (score: 0.70): "we chose k as 10 to perform 10-fold cross validation using the whole dataset."
- **PMID:local_8e16e9b1** (score: 0.70): "we performed a 5-fold cross validation for each site because of the limitation of the size of the data."
- **PMID:local_8e16e9b1** (score: 0.80): "exhibits better accuracy for 12 out of the 17 sites. The average accuracy achieved by ASD-SAENet model was 64.42%"
- **PMID:local_8e16e9b1** (score: 0.60): "The implemented code is available on GitHub portal of our lab at: https:// github.com/pcdslab/ASD-SAENet."
- **PMID:local_e623bee8** (score: 1.00): "The 539 subjects with ASD and the 573 controls were split 70/15/15 into training, validation and test sets."
- **PMID:local_e623bee8** (score: 0.80): "we downloaded fMRI data (derivatives) pro- cessed with the Connectome Computation System (CCS) pipeline [9] which performs slice timing correction, motion realignment and global intensity normalisation."
- **PMID:local_e623bee8** (score: 0.80): "we chose to use Regional Homogeneity (ReHo) derivative for comparing different aug- mentation strategies."
- **PMID:local_e623bee8** (score: 0.70): "10-fold cross validation was used and the mean test accuracy was calculated."
- **PMID:local_e623bee8** (score: 0.90): "Compared to no augmentation, the best augmentation approach increases the test accuracy by 0.6 percentage units."
- **PMID:local_e623bee8** (score: 0.80): "elastic deformations seem to work best, with an improvement of 2.2 percentage units."
- **PMID:local_e623bee8** (score: 0.90): "Our conclusion is that augmentation only provides mi- nor improvements when training 3D CNNs for classiﬁcation of ASD versus controls"
- **PMID:local_fe9d4dc4** (score: 0.80): "The dataset brings together 1,112 subjects (539 ASD patients and 573 TCs) from 17 sites around worldwide"
- **PMID:local_fe9d4dc4** (score: 1.00): "A ﬁnal dataset of 871 subjects, including 403 ASD patients and 468 TCs, was obtained by removing the samples with incomplete brain coverage, high motion peaks, ghosting and other scanner artifacts."
- **PMID:local_fe9d4dc4** (score: 0.80): "The preprocessing method used in this paper is the conﬁgurable pipeline for the analysis of connectomes (CPAC)"
- **PMID:local_fe9d4dc4** (score: 0.80): "the spatial dimension of each image (61, 73, 61) is downsampled to (28, 28, 28). After the processing of temporal and spatial dimensions, the size of the obtained fMRI data is (28, 28, 28, 32)."
- **PMID:local_fe9d4dc4** (score: 0.70): "the data is categorized into a training set and a test set in a ratio of 8:2."
- **PMID:local_fe9d4dc4** (score: 1.00): "the proposed algorithm obtains an accuracy of 72.46% in the experiment of 871 subjects, which is 5.26% higher than that of HI-GCN, 4.44% higher than that of GAT, and 2.44% higher than that of CNN."
- **PMID:local_fe9d4dc4** (score: 0.80): "The proposed algorithm also obtains a speciﬁcity of 79.25% and a sensitivity of 74.35%."
- **PMID:local_fe9d4dc4** (score: 0.90): "the AUC value of the proposed algorithm is 0.79, which is 5.42% higher compared to GAT."
- **PMID:local_ef705029** (score: 1.00): "The publicly available data set comprises data from 48 people with ASD and 65 TCs, with no signiﬁcant diﬀerences in demographics between the two groups."
- **PMID:local_ef705029** (score: 0.90): "The data set was collected at the University of Michigan, one of the ABIDE data collection sites"
- **PMID:local_ef705029** (score: 0.70): "TCs were excluded for those who received a score of 10 or higher on the Social Communication Questionnaire 14 or a score of 6 or higher on the Obsessive/Compulsive subscale of the Spence Children’s Anxiety Scale (SCAS) 16."
- **PMID:local_ef705029** (score: 0.80): "we performed preprocessing based on the Conﬁgurable Pipeline for the Analysis of Connectomes"
- **PMID:local_ef705029** (score: 0.80): "Using automated anatomical labeling (AAL), we then used the ﬁrst 90 regions of interest (ROIs) as nodes"
- **PMID:local_ef705029** (score: 1.00): "The leave-one-out cross-validation results show that the accuracy rates are 89 and 84% correspondingly."
- **PMID:local_ef705029** (score: 0.80): "We further validate the detected subnetwork features by performing classiﬁcation analysis. We employ the support vector machine with radial basis function kernel and linear kernel as our classiﬁer."
- **PMID:local_ef705029** (score: 0.70): "we only utilize a subset of ABIDE data base, and we plan to compare results from diﬀerent study sites and perform meta-analysis in future work."
- **PMID:local_30f8d927** (score: 0.90): "We studied 211 males from three sites of the ABIDE-I dataset comprising 103 participants with an ASD diagnosis (mean ± SD age = 20.8 ± 8.1 years) and 108 neurotypical controls (NT, 19.2 ± 7.2 years)."
- **PMID:local_30f8d927** (score: 0.90): "Compared to NT, ASD participants presented with widespread reductions in CD, generally indicating shorter average connection length and thus suggesting reduced long-range connectivity but increased short-range connections."
- **PMID:local_30f8d927** (score: 0.70): "included imaging and  clinical data from three different sites that included data  from > = 10 ASD and NT respectively, i.e., University of  Pittsburgh School of Medicine (PITT), New York Univer­ sity Langone Medical Center (NYU), and University of  Utah School of Medicine (USM)."
- **PMID:local_30f8d927** (score: 0.80): "After excluding cases with high  head motion (cutoff: >2SD over mean framewise dis­ placement, n = 10), we obtained a sample size of n = 211  (103/108 ASD/NT)."
- **PMID:local_30f8d927** (score: 0.70): "based on  the configurable pipeline for the analysis of connectomes  (C-PAC) (https://fcp-indi.github.io/) [83], including slice- time and head motion correction, skull stripping and  intensity normalization."
- **PMID:local_30f8d927** (score: 0.70): "Subjects with a mean framewise displacement  (FD) > 0.3 mm in rs-fMRI (two SD from the mean across  all subjects) were excluded (n = 9)."
- **PMID:local_30f8d927** (score: 0.70): "Data were harmo­ nized for site effects while preserving effects of age and  ASD diagnosis using ComBat [86]"
- **PMID:local_30f8d927** (score: 0.80): "Effect sizes dif­ fered across seven intrinsic functional networks [21],  with higher effects towards transmodal compared to  sensory/motor networks and peak reductions in CD in  the limbic network (Cohen's d=-0.159, Fig.  3A)."
- **PMID:local_ef4bae49** (score: 0.80): "The ABIDE dataset contains 539 individuals with ASD and 573 control subjects."
- **PMID:local_ef4bae49** (score: 0.80): "First, participants were randomly divided into balanced split-half training and testing sets."
- **PMID:local_ef4bae49** (score: 0.80): "We specifically focused on the regional homogeneity (ReHo) fMRI derivative (Zang et al. 2004) from the Configurable Pipeline for the Analysis of Connectomes (CPAC) pipeline (Craddock et al. 2013)."
- **PMID:local_ef4bae49** (score: 0.90): "The accuracy of our model without any dimensionality reduction or feature selection was ~ 62%."
- **PMID:local_ef4bae49** (score: 0.90): "Using this program allowed us to build a sparse whole-brain biomarker that predicted diagnostic labels with 62% accuracy."
- **PMID:local_ef4bae49** (score: 0.50): "All data at ABIDE I Preprocessed are fully anonymized and hence are in compliance with HIPAA."
- **PMID:local_a7654842** (score: 0.90): "The subjects were 42 autistic children and 127 age-matched normal children from the ABIDE II dataset."
- **PMID:local_a7654842** (score: 0.80): "We used the KKI dataset in this study. The KKI dataset collected from 211 children aged 8 to 13 years, including 56 children with ASD and 155 children in the typical controls (TC) group."
- **PMID:local_a7654842** (score: 0.90): "a total of 14 children with ASD and 28 TC children were excluded, and the final sample included 42 children with ASD and 127 TC children."
- **PMID:local_a7654842** (score: 0.80): "Then 24 ROIs corresponding to 7 brain networks were selected using the AAL standard brain template provided by the Montreal Neurological Institute (MNI)."
- **PMID:local_a7654842** (score: 0.70): "Data processing was performed with the GRETNA toolbox (v2.0.0) (Wang et al., 2015) based on SPM12."
- **PMID:local_a7654842** (score: 0.90): "Compared with healthy controls, children with ASD showed decreased effective connectivity among some large- scale brain networks. These brain networks included VN, DMN, cerebellum, SMN, and FPN."
- **PMID:local_a7654842** (score: 0.70): "we also found signiﬁcant negative correlation
between the strength of the effective connectivity from right angular
gyrus (ANG_R) of DMN to left precentral gyrus (PreCG_L) of SMN and"
- **PMID:local_a7654842** (score: 0.60): "ADOS-G or ADOS-2 module 4 stereotyped behaviors and restricted interest
total (ADOS"
- **PMID:local_1f08c2f9** (score: 0.80): "This data set was collected at Brain Mapping Center in University of California, Los Angles (UCLA), one of the data collecting sites in the Autism Brain Imaging Data Exchange (ABIDE)"
- **PMID:local_1f08c2f9** (score: 0.70): "initially 33 participants (typical controls, TC) and 49 patients with the Autism spectrum disorders (ASD) were asked to lie as still as possible"
- **PMID:local_1f08c2f9** (score: 0.90): "Participants with large motions were removed from the dataset, resulting in 32 participants in the TC group and 41 in the ASD group."
- **PMID:local_1f08c2f9** (score: 0.80): "We then use the ﬁrst 90 AAL ROIs as nodes, and take the average of all voxels’ temporal proﬁles within each ROI as region level signal for all subjects"
- **PMID:local_1f08c2f9** (score: 0.90): "the analysis based on empirical Bayes normalized connectivity metrics shows signiﬁcant connectivity diﬀerences between the ASD and TC groups , and 44 connectivity features have fdr q- values less than 0.1."
- **PMID:local_1f08c2f9** (score: 0.80): "No signiﬁcant feature or network is identiﬁed after the correction for the original correlations (q-value 0.1 as threshold for local fdr and permutation p-value 0.05 for NBS)."
- **PMID:local_1f08c2f9** (score: 0.80): "The ASD group show higher function connectivity between pairs of ROIs for all"
- **PMID:local_1f08c2f9** (score: 0.80): "These results suggest that hyper-connectivity in ASD spans multiple functional subsystems of the human brain."
- **PMID:local_c998fc64** (score: 0.90): "This study includes all sites publicly available through ABIDE I and ABIDE II. They were comprised of 1,127 TD and 1,017 ASD."
- **PMID:local_c998fc64** (score: 0.70): "We find significant shifts in statistical features of typical
levels of involuntary head motions for different age groups."
- **PMID:local_c998fc64** (score: 0.90): "The results suggest that the levels of random involuntary
motor noise are elevated in autism across age groups."
- **PMID:local_c998fc64** (score: 0.80): "The comparisons of the age-groups with ASD also show shifting
statistical signatures across ages (Figure 5) and they were
significant at the 0.05 level for all comparisons in the NSR."
- **PMID:local_c998fc64** (score: 0.60): "The ABIDE data is publicly available. We have uploaded to ABIDE the indexes of the participants included in the current study."
- **PMID:local_c998fc64** (score: 0.50): "All methods and data types generated to produce the ﬁgures will be made available through Github, https://github.
com/torreselizabeth/Frontiers-Paper."
- **PMID:local_6d8e3dc5** (score: 0.90): "Using data  8  from two sites of the ABIDE II dataset comprising 276 children with and without ASD (8-13 years),  9  we identified functional brain networks whose FC predicted individual differences in two, of three,  10  behavioral regu"
- **PMID:local_6d8e3dc5** (score: 0.70): "Scores for all three subscales of behavioral regulation were significantly higher in 
6 
children with ASD than for TD children in all analyzed samples"
- **PMID:local_6d8e3dc5** (score: 0.80): "Twenty-six participants had excessive head motion on their fMRI scan (>4 mm maximum absolute 
20 
displacement)."
- **PMID:local_6d8e3dc5** (score: 0.80): "A functionally defined atlas, consisting of 268 cortical and subcortical regions-of-interest (‘nodes’)"
- **PMID:local_6d8e3dc5** (score: 0.90): "Significant models were built using negative edges for inhibition (rs=.23, p=0.0001) and shifting 
2 
(rs=.19, p=0.001), using leave-one-out prediction (N-1 at every iteration)."
- **PMID:local_6d8e3dc5** (score: 0.80): "The FC model of inhibition was significant by permutation testing 
5 
(rs=.23, p=0.037), while the FC model of shifting fell just shy of significance (rs=.19, p=0.067)."
- **PMID:local_6d8e3dc5** (score: 0.70): "inhibition revolved around edges in the somato-motor, visual and cerebellar 
7 
networks and was more posterior, while shifting appeared more focused on edges around the 
8 
frontoparietal and dorsal attention networks and was more anterior."
- **PMID:local_cb451a29** (score: 0.80): "we apply Forman–Ricci and Ollivier–Ricci curvatures to compare  networks of ASD and typically developing individuals (N = 1112) from the Autism Brain Imaging  Data Exchange I (ABIDE-I) dataset."
- **PMID:local_cb451a29** (score: 0.80): "First, the subjects with missing anatomical or functional files were 
excluded. Second, all subjects from the imaging site Stanford were excluded as it is the only site with spiral image 
acquisition protocol. Third, all subjects from the imaging site Leuven-1 were excluded due to unknown repeti-
tion times for the functional scans."
- **PMID:local_cb451a29** (score: 0.90): "After removing subjects based on these exclusion criteria, we were left with 395 subjects in the ASD group and 
425 subjects in the TD group"
- **PMID:local_cb451a29** (score: 0.80): "Subsequently, 200 regions of interest (ROIs)  or nodes were defined in the brain using the Schaefer atlas, and a 200 × 200 functional connectivity (FC) matrix  was generated for each subject by computing the Pearson correlation coefficient between the time-series of all  pairs of nodes."
- **PMID:local_cb451a29** (score: 0.70): "We used the CONN functional connectivity ­toolbox69 to process the rs- fMRI data from ABIDE-I."
- **PMID:local_cb451a29** (score: 0.90): "average edge FRC is significantly lower ( p < 0.05 , FDR-corrected) in the ASD group compared to the TD group 
in the graph density range 5–50%"
- **PMID:local_cb451a29** (score: 0.80): "We find brain-wide and region-specific ASD-related differences  for both Forman–Ricci and Ollivier–Ricci curvatures, with region-specific differences concentrated  in Default Mode, S"
- **PMID:local_cb451a29** (score: 0.60): "Functional connectivity matrices and networks generated in our study, and all original codes are deposited  on GitHub and are publically available at https://​github.​com/​asama​llab/​Curva​ture-​FCN-​ASD as of the date of  publication."
- **PMID:local_ddf52058** (score: 0.90): "Resting-state fMRI (rs-fMRI) and structural imaging data of 85 individuals with ASD and 163 matched controls from multiple sites of the ABIDE data set (Di Martino et al., 2014) were included in this study for a total of N = 248 individuals."
- **PMID:local_ddf52058** (score: 0.80): "Frames with excessive motion were identiﬁed and scrubbed  (Power et al., 2012) if the framewise displacement exceeded  0.3 mm. Individuals with >10% of their frames ﬂagged for  scrubbing were excluded."
- **PMID:local_ddf52058** (score: 0.80): "ROIs were deﬁned as 10 mm diameter spheres whose center coordinates are given in MNI atlas space (Power et al., 2011)."
- **PMID:local_ddf52058** (score: 0.90): "We observed that an imbalance in intra- and inter-network FC across 11 RSNs in ASD individuals (p = 0.002) corresponds to a weakened relationship with RSN
temporal entropy (p = 0.02)."
- **PMID:local_ddf52058** (score: 0.90): "Further, we observed that an estimated RSN entropy model
signiﬁcantly distinguished ASD from controls (p = 0.01) and was associated with level of
ASD symptom severity (p = 0.003)."
- **PMID:local_ddf52058** (score: 0.70): "Importantly, no information about group membership (i.e., ASD or control) has been explicitly passed to the model."
- **PMID:local_ddf52058** (score: 0.60): "The minimum MSE computed from a 10-fold cross validation
was 11.4 ± 7.2% of c1 variance, and was observed for α = 0.15."
- **PMID:local_757f29e4** (score: 0.70): "ABIDE dataset [4,7] consists of resting state fMRI brain scans from 16 diﬀerent imaging sites."
- **PMID:local_757f29e4** (score: 0.90): "We use Craddock 200 (CC200) data set, where the
imaging data is ﬁrst preprocessed using the Conﬁgurable Pipeline for Analysis
of Connectomes (CPAC) and then the mean blood oxygenation level dependent
(BOLD) signals for 200 regions of interest (ROIs) are extracted. After ﬁltering
for missing and invalid data, it contains 1035 subjects, of which 505 are ASD
patients and 530 are TDC (typically developing control subjects)."
- **PMID:local_757f29e4** (score: 0.50): "The present state-of-the-art machine learning model using deep learning has a
classiﬁcation accuracy of 70.2% on the ABIDE (Autism Brain Imaging Data Exchange) data
set."
- **PMID:local_757f29e4** (score: 0.90): "With this approach, even with a simple 3-layer neural network, we are able to achieve a
classiﬁcation accuracy of 69.2% on the
ABIDE data set."
- **PMID:local_757f29e4** (score: 0.90): "However, our experiments also show that the improvement due to topological features is not always statisti-
cally signiﬁcant. Therefore, we oﬀer a cautionary tale to the practitioners
regarding the limited discriminative power of topological features derived from
fMRI data for the classiﬁcation of autism."
- **PMID:local_757f29e4** (score: 0.80): "All results are
obtained by running a 5-fold stratiﬁed cross-validation scheme where we report the mean classiﬁca-
tion accuracy over all folds."
- **PMID:local_757f29e4** (score: 0.60): "we esti-
mate the p-values using a Monte-Carlo approximation with 100, 000 samples."
- **PMID:local_1a3d5c74** (score: 0.90): "The sample size is 82 subjects (41 ASD and 41 normal cases) collected from three different sites  of Autism Brain Imaging Data Exchange (ABIDE)."
- **PMID:local_1a3d5c74** (score: 0.70): "The resting-state fMRI data of 41 ASD and 41 normal control (NC) cases were gathered from the Autism Brain  Image Data Exchange (ABIDE) sources [16], taken from multiple independent neuroimaging sites."
- **PMID:local_1a3d5c74** (score: 0.70): "The DPARSF is a MATLAB toolbox for fMRI data pre-
processing and analysing [17]."
- **PMID:local_1a3d5c74** (score: 0.80): "The  automated anatomical labelling (AAL) is selected as the standard brain atlas to divide the brain into 116 regions of  interest (ROIs)"
- **PMID:local_1a3d5c74** (score: 0.90): "The extracted features are trained  using two classifiers: support vector machine (SVM) and K-nearest neighbours (KNN). The best prediction results  are 85.9% accuracy achieved by extracted the features from DenseNet201 network and classified these features by  KNN classifier."
- **PMID:local_606b4b83** (score: 0.90): "The original ABIDE dataset claimed to have 1112 subjects consisting of 539 ASD and 573 Healthy controls subjects. However, after removing subjects with missing information we have a total of 1035 subjects which is"
- **PMID:local_606b4b83** (score: 0.70): "We have used the ABIDE dataset that is pre-processed using Conﬁguration Pipeline for
the
Analysis of Connectome (CPAC) [54]"
- **PMID:local_606b4b83** (score: 0.80): "We have used the brain Automated anatomical labelling (AAL) template which divides the brain
into 90 regions."
- **PMID:local_606b4b83** (score: 0.90): "On the combined site data across 17 sites, we achieved the maximum 10-fold accuracy of 82% and for the individual site-wise data, based on 5-fold accuracy, our results outperformed other state of the art methods in 13 out of the total 17 site-wise comparisons."
- **PMID:local_606b4b83** (score: 0.60): "A comparison of our Stage feature selection-based classiﬁers with the state of the art methods is
presented in Table 11."

---

## Appendix B: Research-Question Charting

Every included study's answer to each of the 14 protocol research questions, charted from the full text. The same content is the `research_questions` block in the JSON export and `slr:ResearchQuestion` / `slr:ChartingQuestionAnswer` in the RDF export.

### Cohort

#### RQ1 — Release, subset and QC rule

**Question.** Which ABIDE release(s) and subset (N by diagnosis, sites, QC/exclusion rule) were analysed?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

descriptor — ABIDE II release: 1,044 datasets (ASD N=487, Controls N=557) across 17 collections/16 sites; no QC-based exclusion applied, all data released regardless of quality | quote: "users regardless of data quality27. The rationale of this decision includes the lack of consensus on optimal quality criteria in regards to speciﬁc measures or their combinations and cutoffs."

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

predictive — ABIDE-I: N=1112 (539 ASD, 573 controls), 17 sites; ABIDE-II: N reported inconsistently as 1114 (abstract) / 1014 (Table II) (521 ASD, 593 controls); no explicit QC/exclusion rule beyond removing missing/broken images (938 of 1112 ABIDE-I scans used after cleaning) | quote: "ABIDE-I and   ABIDE-II consists of 1112 rs- fMRI datasets from 573 typical   control (TC) and 539 autism individuals, and 1114 rs-fMRI from   521 autism and 593 typical control individuals respectively,   which were collected from 17 different sites."

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

associational — ABIDE subset: 58 ASD, 51 TD, matched to primary cohort by age/sex/IQ; participants with <80% TRs retained after motion scrubbing excluded; release (I vs II) not specified, both ABIDE I and ABIDE II papers cited as the data source | quote: "To validate our ﬁndings in a separate cohort, we iden- tiﬁed 58 ASD and 51 TD individuals from ABIDE mat- ched to the HFASD cohort by age, sex, and IQ (Table 2). The selection process is detailed in Supplemental Infor- mation."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

associational — ABIDE I+II discovery sample, N=1019 (82 F ASD, 362 M ASD, 166 NT F, 409 NT M), 13 merged sites; QC rule: age 7-18, successful registration, FIQ 70-148, mFD within 3xIQR+Q3 (~0.39mm), sites with <3 datasets per diagnostic/sex group excluded | quote: "The final ABIDE I and II dataset of N = 1019 included N = 82 females with autism, N = 362 males with autism, N = 166 neurotypical females (NT F), and N = 409 neurotypical males (NT M), aggregated across 13 sites."

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

predictive — ABIDE I+II combined ("both waves of the openly shared ABIDE initiative"), final N=297 (151 ASD, 146 TD) from 4 sites (NYU, PITT, USM, TCD); QC: sites with >=10/group and both children+adults, acceptable T1w MRI/surface extraction/head motion; after propensity matching N=290 (145/145) | quote: "procedures resulted in a total of 297 par- ticipants (151 ASD and 146 TD) from 4 different sites (i.e., New York University Langone Medical Center [NYU], University of Pittsburgh, School of Medicine [PITT], University of Utah, School of Medicine [USM], and Trinity Centre for Health Sciences [TCD]) in ABIDE."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

associational — discovery: ABIDE I post-QC N=708 (432 TD, 276 ASD); validation: ABIDE II post-QC N=585 (316 TD, 269 ASD, 11 sites); QC rule: >5% of scans removed by motion scrubbing excludes a subject | quote: "After preprocessing (described in section 2.2.), the ABIDE I dataset was composed of 432 subjects with TD (348 males, mean age ± standard deviation of 18.21 ± 8.04) and 276 individuals with ASD (241 males, 18.42 ± 8.38). The ABIDE II dataset was composed of 316 subjects with TD (208 males, 12.80 ± 5.61) and 269 individuals with ASD (234 males, 13.93 ± 7.07)."

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

predictive — ABIDE I only, raw N=1112 reduced to 1,035 after preprocessing/QC (505 ASD, 530 TC); no explicit FD/motion threshold given in the extracted main text (QC described generically as reducing N to 1035, consistent with prior studies) | quote: "Although Di Martino et al. [11] released the ABIDE I dataset with 1,112 samples, prepro- cessing and quality control reduced this number to 1,035"

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

predictive — ABIDE (release not specified as I vs II in extracted text, but cites ABIDE/Nielsen 2013 ABIDE results), N=154 (77 ASD, 77 TD), balanced per site and matched on IQ/age/head-movement; subjects with strong motion artifacts excluded | quote: "The inputs to the classification pipeline are the 77 ASD and 77 TD connectivity matrices (hence 154 data samples in total), where each connectivity matrix consists of 19,900 features."

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

predictive — ABIDE (1112 raw, 1 excluded for preprocessing failure, 1111 final: 573 controls, 538 ASD) across 17 institutions; randomly split into label-balanced 889-subject training and 222-subject hold-out test sets | quote: "Therefore, we divided the ABIDE dataset into training and test sets by ran- domly selecting a label-balanced 889 (4/5) of the ABIDE subjects as the training set, leaving the remaining 222 (1/5) ABIDE subjects as the testing set."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

associational — ABIDE I, N=975 (458 ASD, 517 TDC) after excluding sites/datasets for missing FIQ (Groningen), poor cerebellar coverage (Carnegie Mellon), and low IQ (<70, 5 datasets) from the original 1112 | quote: "We excluded datasets from the social brain Lab BCN NIC UMC Groningen and Netherlands Institute for Neurosciences due to the missing information of a full-scale intelligence quotient (IQ) for many subjects. After preprocessing, we found that a large part of the cerebellum was missing in the imaging dataset of Carnegie Mellon University, and all datasets from Carnegie Mellon University were excluded. To control for potential confounding eﬀects of IQ in our analysis, we decided to exclude ﬁve datasets that included some subjects with IQ lower than 70. Finally, we performed voxel-wise group comparisons with 975 imaging datasets."

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

ABIDE II used as a replication cohort (not the primary dataset): 5 of 16 ABIDE II sites selected (GU, KKI, NYU_1, NYU_2, SDSU) with sex/FSIQ/age/handedness/behavioural-score filters, then NYU_2 and motion/normalization failures excluded, yielding 42 ASD and 88 TD boys. | quote: "The ﬁnal replication dataset consisted of 42 boys with ASD (mean age: 10.7 ± 1.8 years, range: 7.2–14.4 years) and 88 TD boys"

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

ABIDE I, 1035 subjects (505 ASD, 530 HC); no explicit motion/QC exclusion rule stated beyond using the Preprocessed Connectomes Project release. | quote: "We used the resting-state fMRI data from 1035 subjects in the ABIDE I initiative [20]  for this study. The dataset includes 505 individuals diagnosed as having ASD and 530  HC."

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

ABIDE-I, single site (NYU), 184 subjects (79 ASD, 105 TC); no additional QC/exclusion rule beyond selecting the NYU site reported. | quote: "TABLE 2 | NYU phenotypic data information for ABIDE-I database.
Total subjects
ASD
TC
Female
Male
Age range (Years)
Average age (SD)
ADOS score (SD)
ASD
TC
184
79
105
35
149"

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

ABIDE-I single-site cohorts (NYU: 184 subjects; UM: 110 subjects) and a multi-site cohort (19 sites, 1100 subjects); no explicit motion/QC exclusion rule stated. | quote: "For single sites experiments, we use the NYU and UM sites from ABIDE-I. Those provide the highest number of balanced (ASD/typically developing (TD)) subjects with 184 and 110 subjects respectively."

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

ABIDE I, single-site subsets: NYU (184 subjects: 79 ASD, 105 NC, primary) and UM (145 subjects: 68 ASD, 77 NC, secondary); sites chosen specifically to avoid inter-site heterogeneity, no further motion/QC rule stated. | quote: "In this work, we use rs-fMRI data from the New York University (NYU) site with the largest sample size collected in this database. Speciﬁcally, the NYU site includes 184 subjects, 79 of whom were from ASD and 105 NC cases."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

Two ABIDE I-derived multimodal cohorts: ABIDE A (871 subjects, 403 ASD/468 TC, following Parisot 2017) and ABIDE B (949 subjects, 419 ASD/530 TC, following Wang 2020); both inherit the selection/QC rules of those prior published protocols rather than defining a new one. | quote: "The dataset includes 871 subjects
(468 TC and 403 ASD subjects). We follow (Parisot, 2017) [19] for
the dataset settings and preprocessing."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

ABIDE I, 17 sites; full release is 1,112 subjects (539 ASD, 573 TD), but after excluding samples with missing filenames/incomplete data the analysed cohort is 880 subjects (418 ASD, 478 TD). | quote: "samples with missing filenames and incomplete data are
excluded; and the remaining 880 samples across 17 international
sites are utilized, which include 418 ASD subjects and 478 TD subjects."

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

ABIDE I, 17 sites; DPARSF-preprocessed subset of 406 ASD and 476 TC subjects (out of the full 1112-subject, 539 ASD/573 TC release); no explicit additional motion/QC exclusion rule stated in this paper. | quote: "In this work we use the preprocessed data from the DPARSF pipeline [31] comprising 406 ASD and 476 TC subjects."

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

ABIDE I, 850 subjects (355 ASD with DSM-IV-TR diagnosis, 495 HC) from the same sites; no additional motion/QC exclusion rule beyond this stated in text. | quote: "Resting-state fMRI data from 850 subjects in ABIDE I with an ASD DSM-IV-TR diagnosis (n = 355) and the corresponding HCs (n = 495) from the same sites were used in this study"

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

predictive — ABIDE-I (1112 total; analysed 774: 379 ASD/395 TD, 17 sites, manual QA by all functional raters) used for training/10-fold CV; ABIDE-II (analysed 393: 163 ASD/230 TD, from sites overlapping ABIDE-I) used as independent held-out test after automatic motion-scrubbing QC. | quote: "In our experiments, we used ABIDE-I subject data that passed manual qual- ity assessments (QA) by all the functional raters. This yielded a ﬁnal sample size of 774 ABIDE-I subjects, comprising 379 subjects with ASD and 395 typical con- trols."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

predictive, external validation only — all ABIDE I/II sites included, restricted to subjects with a paired same-visit sMRI+rsfMRI scan: 1045 ABIDE I and 761 ABIDE II subjects (Table 3: ASD% 48 and 52 respectively; exact integer N by diagnosis not given). | quote: "Participants from all sites of the ABIDE I and ABIDE II were included for external validation, provided both sMRI and rsfMRI were obtained on the same visit. The first avail- able pair of sMRI and rsfMRI scans were used per subject. 1045 subjects from ABIDE I and 761 subjects from ABIDE II met this criteria."

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

ABIDE I — top four largest sites (UM1, NYU, USM, UCLA1): after excluding subjects with missing files or incomplete ROI time series, analysed N = 88 (UM1), 167 (NYU), 52 (USM), 63 (UCLA1); ASD/HC per site given in Table 1 (overall 186 ASD / 184 HC). | quote: "Skipping subjects lacking ﬁlename, we downloaded 106, 175, 72, 71 subjects from UM1, NYU, USM, UCLA1 separately. HO parcellated each brain into 111 ROIs. Since some sub- jects did not contain complete ROIs, we removed the incom- plete data, resulting in 88, 167, 52, 63 subjects for UM1, NYU, USM, UCLA1 separately."

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

ABIDE I: 1,112 individuals (539 ASD/573 TD, 17 sites), sites required >=20 subjects passing successful preprocessing/normalisation QC; after CPAC preprocessing the sample was reduced to 871 subjects (a separate statement reports 505 ASD/530 typical controls as the dataset used). | quote: "There are 1,112 subjects (539 diagnosed with ASD, and 573 typical controls) in the ABIDE I dataset, reduced to 871 subjects after preprocessing."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

ABIDE I: 1111 scans from 17 sites (573 HC, 538 ASD); split into 800 (70%) training and 311 (30%) hold-out test subjects, preserving the overall case:control ratio (0.5157) in both sets. | quote: "The ABIDE dataset consists of 1111 scans, taken from 17 sites consisting of 573 healthy controls and 538 patients with autism. To evaluate each learning model, we use 800 subjects (70%) for model training and 311 subjects (30%) for hold-out testing. We use the same case/control ratio (0.5157) for both training and test set."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

ABIDE I — four target sites with >=60 subjects each (UM: 48 ASD/65 healthy; UCLA: 36/39; USM: 38/23; LEUVEN: 27/34), with offline SSAE pretraining drawn from healthy subjects pooled across the remaining 16 ABIDE sites. | quote: "we performed ASD classiﬁcation experiments on four individual data sites with at least 60 subjects, including University of Michigan (UM), University of California, Los Angeles (UCLA), University of Utah School of Medicine (USM), and Katholieke Universiteit Leuven (LEUVEN)."

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

ABIDE I — 584 resting-state datasets (278 ASD/306 TD) from nine ABIDE sites, used as an independent replication sample; ASD diagnosis was a clinician DSM-IV-TR diagnosis corroborated by ADOS/ADI-R at all but one site; groups matched on age (and IQ within most sites). | quote: "The replication dataset consisted of 584 resting-state fMRI datasets from nine sites contributing to the ‘ABIDE’ release (Di Martino et al., 2013). In this sample, all participants with ASD (278) had a clinician’s DSM-IV-TR diagnosis of ASD, which was corroborated by the Autism Diagnostic Observation Schedule (ADOS) and the Autism Diagnostic Interview-Revised (Lord et al., 1994, 1999) for all sites except one."

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

ABIDE I — subjects selected by matching one specific MRI acquisition protocol (3.0T Siemens, TR=3000ms, TE=28ms) across the database (61 ASD/46 TC met the protocol); after excluding 7 TC and 16 ASD for motion >2mm translation or >2deg rotation, the final analysed sample was 45 ASD/39 TC (n=84). | quote: "TABLE 1 | Basic information of ASD and TC. Variables (Mean ± SD) Autism (n = 45) TC (n = 39) P value Gender (M/F) 41/4 33/6 0.359 Age (years) 13.4 ± 2.4 12.9 ± 1.7 0.278 ASD, Autism spectrum disorder; TC, typical controls."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

ABIDE I+II — full release 1,028 ASD/1,141 TD across 29 institutions; after a minimum-scan-duration cutoff (>=100 time points), 96% was retained (N=2,085, N(ASD)=993). | quote: "We chose to cut off the minimum scan duration to 100-time points, which led us to include 96% of the whole ABIDE I+II dataset (N=2,085, N(ASD) =993), the vast majority of which (95%) with a minimum acquisition time of 4 min."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

ABIDE I — 816 individuals across 22 sites, stratified into five age groups (5-10: 109, 10-15: 342, 15-20: 190, 20-30: 137, 30-65: 51); subjects with a consistently zero time-series were excluded; exact ASD/HC split is in a supplementary table not captured in the extracted full text. | quote: "All Sites 109 342 190 137 51 816 Number of participants from each site for each age group as well as the overall number of participants in a site that were used for this study. Last row shows the total number of subjects in each age-range."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

predictive | ABIDE I preprocessed-connectomes-project release, 872 of 1112 subjects analysed, 20 sites; no explicit QC/exclusion rule stated for the subset. | quote: "this resulted in a dataset with
872 of the initial 1112 patients available, from 20 different
sites."

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

associational | ABIDE I and ABIDE II combined with EU-AIMS LEAP; ABIDE I n=369 autism/481 NT, ABIDE II n=205 autism/347 NT (combined ABIDE total autism 574, NT 828); detailed exclusion rules referenced as "Supplement Section 2", not given in body text. | quote: "n 
796 
1028 
.. 
222 
200 
.. 
369 
481 
.. 
205 
347 
.. "

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

predictive | ABIDE release, N, sites and exclusion/QC rule are not reported in the available text; only the autism dataset's existence and ASD-vs-HC classification results are described. | quote: "And the largest dataset for autism research comes
from Autism Brain Imaging Data Exchange (ABIDE) [11]."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

predictive | ABIDE Preprocessed Connectomes Project release (consistent with ABIDE I's ~1112-subject pool); 1102 subjects downloaded, excluded those with missing imaging data, final N = 506 ASD / 548 TC across 17 sites | quote: "We successfully downloaded a dataset 
of 1102 subjects from the Preprocessed Connectomes Project, 
and then excluded subjects whose imaging data shows some miss-
ing. Finally, data of 506 ASD individuals and 548 controls was 
included in our study."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

predictive | ABIDE-I, restricted to the single NYU site (79 ASD/105 NC) out of the full ABIDE-I 539 ASD/573 TC across 17 sites, specifically to avoid cross-site scan-parameter heterogeneity; no further exclusion rule stated beyond site restriction | quote: "To avoid the impact of data heterogeneity,
we collected raw rs-fMRI data from the whole NYU site,
consisting of 79 ASD subjects and 105 normal controls (NCs)."

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

associational | ABIDE (consistent with ABIDE I, 7 sites including Caltech/CMU/NYU/Pitt/SDSU/Trinity/UCLA); 454 subjects with complete phenotypic data = 256 HC, 166 autism, 32 Asperger’s (198 ASD total); PDD-NOS and "Asperger’s or PDD-NOS" excluded to reduce class imbalance | quote: "Four hundred and ﬁfty-four subjects with complete phenotypic
data were selected from the Autism Brain Imaging Data
Exchange (ABIDE) database"

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

predictive | ABIDE (consistent with ABIDE I's 1112-subject pool); 871 of 1112 subjects selected (403 ASD, 468 HC); exact exclusion rule for the selected 871 not detailed | quote: "We select a set of 871 subjects,
consisting of 403 ASD patients and 468 healthy controls
(HCs)."

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

predictive | ABIDE I, 871 of 1112 participants (403 ASD, 468 TC) from 17 sites, selected after visual QA of MRI and phenotypic information. | quote: "Af- ter preprocessing, we selected 871 to meet quality criteria for MRI and phenotypic information."

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

predictive | Same ABIDE I 871-subject subset (403 ASD, 468 controls) as Abraham et al. 2017, from 20 sites. | quote: "We select the same set of 871 subjects used by Abraham et al. (2017) that met the imaging quality and phenotypic information criteria, comprising 403 individuals with ASD and 468 healthy controls."

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

predictive | ABIDE I, 964 of 1112 participants (447 autism, 517 TD) from 16 sites after preprocessing-success inclusion criteria. | quote: "A total of 964 subjects met all inclusion criteria (517 typically developing subjects and 447 subjects with autism from 16 sites)."

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

predictive | Same 871-subject ABIDE I cohort (403 ASD, 468 controls) from 20 sites as used by Abraham et al. 2017. | quote: "It includes N = 871 subjects from diﬀerent imaging sites that met the imaging quality and phenotypic information criteria, consisting of 403 individuals suﬀering from ASD and 468 healthy con- trols."

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

predictive | ABIDE I, 529 ASD and 573 TC (1102 total) from 17 sites, processed through four pipelines in parallel. | quote: "We incorporated data from 529 ASD individuals and 573 typical controls (TC) for each pipeline, which is comprised of 17 different imaging sites."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

associational (within-ASD correlation, no ABIDE controls) | ABIDE I, 27 of 131 candidate ASD participants from 5 sites (CALTECH, CMU, PITT, UM_1, UM_2), restricted by IQ>=100, male sex, and availability of ADI-R/ADOS scores; explicit 27-subject ID list given. | quote: "This yielded 27 subjects with IDs: 51457, 51464, 51468,  51474, 50642, 50643, 50645, 50646, 50647, 50649, 50651, 50652, 50653, 50655, 50002,  50003, 50004, 50006, 50007, 50012, 50016, 50019, 50022, 50024, 50025, 50053, 50056."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

associational | ABIDE I, 507 male subjects (209 ASD, 298 controls) from 14 sites, with FIQ and mean-FD each within 2 SD of the ABIDE-wide mean. | quote: "Speciﬁcally, the 507 subjects included 209 subjects with ASD and 298 well-matched health controls across 14 sites from the Autism Brain Imaging Data Exchange (ABIDE)."

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

associational | ABIDE I, 55 ASD and 55 age-matched controls accessed via NITRC/ABIDE; acquisition appears to be a single scanner/site (3T GE Signa, 32-channel coil), site not explicitly named. | quote: "Anatomical and functional data from fifty-five subjects with ASD (12.7 ± 2.4 y/o) and 55 age- matched (14.1 ± 3.1 y/o) healthy controls were accessed through the NITRC database and the ABIDE project."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

associational | ABIDE I, 605 participants (304 ASD, 301 typical controls) from 7 of 16 ABIDE sites (UM_1, UM_2, USM, NYU, UCLA_1, OLIN, PITT) meeting raw-scan, scan-duration and minimum-N inclusion criteria. | quote: "Datasets from a total of 605 participants were analyzed, including 304 individuals with Autism Spectrum  Disorder (ASD) and 301 typically developing controls (CT)."

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

predictive | ABIDE I, primary sample of 452 adolescents (201 ASD, 251 NT) from 17 sites, selected via eyes-open, age<18, mean-FD<0.2mm inclusion criteria; secondary adult generalization subsample of 130 (63 ASD, 67 NT). | quote: "The corresponding data subset consists of a total of 452 subjects, with respec-
tively 251 NT and 201 ASD subjects."

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

ABIDE I (1112 total: 539 ASD/573 TD) and ABIDE II (1114 total: 521 ASD/573 TD) full releases used, ages 5-64; no QC/exclusion rule reported. | quote: "ABIDE I dataset consists of 1112  total samples including 539 patients and 573 typical  controls (TC) subjects. While ABIDE II dataset consists  of 1114 total samples with 521 patients and 573  typical controls (TC) subjects."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

ABIDE I, a selected subgroup of 190 subjects (102 ASD, 88 TD) from four sites (KKI, NYU, UCLA, UM), restricted to male children aged 6.5-13 years with eyes-open rs-fMRI. | quote: "we selected a subgroup of 190 subjects (102 with ASD and 88 TD) according to the following criteria: male children (age range: 6.5–13 years); rs-fMRI data acquired with open eyes; data from the University sites that provided the largest number of scans (KKI, NYU, UCLA, UM)."

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

ABIDE I, 505 autistic individuals and 530 typical controls; after preprocessing and quality control the final analysed dataset was 1,035 samples; no explicit exclusion-rule text beyond mentioning QC. | quote: "The rs-fMRI data used in this study were sourced from the ABIDE I dataset, comprising 505 autistic individuals and 530 typical controls (TCs)."

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

ABIDE I, the same commonly-used 871-subject subset (403 ASD, 468 TC); no study-specific exclusion/QC rule is described beyond reusing this subset. | quote: "we used the same 871 samples from the ABIDE 1 data set [23], [24], [25]. Of the 871 subjects, 403 patients were ASD and 468 were TC patients."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

All 1102 ABIDE I subjects from 17 sites, CPAC filter_noglobal preprocessing, used without any data screening/QC exclusion; ASD/TD breakdown is not given in the extractable text. | quote: "we use all 1102 subjects (ﬁlter_noglobal) processed by the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) [22] for experiments."

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

ABIDE, restricted to the four sites with repetition time 2s (NYU, SDSU, UM, USM): 147 ASD and 146 healthy controls; no further exclusion rule described. | quote: "We limited ourselves to acquisitions with repetition time of 2s (sites NYU, SDSU, UM, USM). This resulted in a dataset of 147 subjects with ASD and 146 healthy controls."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

ABIDE I, the commonly-used 871-subject subset (403 ASD, 468 HC) from 17 sites, selected by "imaging quality and atypical information criteria" (no specific metric/threshold given). | quote: "In the experiment, 871 subjects (including 403 
ASD patients and 468 healthy controls) who meet the imaging quality and atypical 
information criteria were used."

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

ABIDE-I, 848 of the 1112 subjects across 17 sites (396 ASD, 452 HC); no explicit numeric exclusion/QC rule given for the subset selection. | quote: "we utilized rs-fMRI data
from 848 subjects, including 396 patients with ASD and 452
health controls (HCs)."

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

ABIDE I (1112, 17 sites) + ABIDE II (983, 16 sites) for biomarker derivation (2095 total, 1001 ASD/1094 TD), plus an independent local KMUH cohort (21 ASD, 23 TD) for validation; no further ABIDE QC/exclusion rule reported beyond using the full obtained datasets. | quote: "This study included 1112 ABIDE I datasets 
from 17 sites and 983 ABIDE II datasets from 16 sites."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

ABIDE I+II, QC'd to 939 participants (440 ASD/499 HC) across 18 sites, males only, age<35, FIQ>70, FD<0.5mm, scan length>=5min, sites with <10 participants per group excluded | quote: "Thus, after all selection criteria had been applied, we obtained a dataset consisting of scans from 939 participants (ASD/HC, 440/499) taken from 18 different sites"

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

ABIDE II (9 sites, discovery: ASD n=229 [Asperger's 79, PDD-NOS 58, Autistic 92], TDC n=126) and ABIDE I (17 sites, n=400, replication), males only, age<35 | quote: "Subjects with ASD (n = 229) and the corresponding TDCs (n = 126) were selected from the ABIDE II [29, 30], which is hosted by the 1000 Functional Connectome Project/International Neuroimaging Data-sharing Ini- tiative (INDI) from multiple international sites (9 sites, Additional file 1: Table S1)."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

ABIDE I+II across 37 sites (30 sites in the site-correction procedure), initial 916 ASD/1067 CTL (1983 total), QC'd to 710 ASD (79% male) / 606 CTL (87% male), ages 5-64 | quote: "After the removal of subjects with image artifacts, high head movement, or poor MNI152 coregistration, we analyzed the data from the remaining 710 ASD (79% male), and 606 CTL (87% male) subjects, whose age ranges from 5 to 64 years."

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

ABIDE I+II, 35 sites, 1383 males aged 5-40 (680 ASD/703 TD) after excluding subjects with missing multimodal data | quote: "we obtained a final sample of 1383 subjects (680 ASD and 703 TD) from 35 sites."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

ABIDE-I, 17 sites, 1035 subjects (505 ASD, 530 HC) | quote: "This dataset consists 1,035 rs-fMRI data with 505 ASD subject, and 530 healthy control subjects that are collected from 17 diﬀerent sites."

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

ABIDE I (ABIDE preprocessed), 539 ASD and 573 controls (1112 total); no explicit numeric QC/motion exclusion rule described beyond use of the ABIDE-preprocessed release | quote: "The 539 subjects with ASD and the 573 controls were split 70/15/15 into training, validation and test sets."

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

ABIDE I, 17 sites, 1112 subjects initially (539 ASD/573 TC), QC'd to 871 (403 ASD/468 TC) by removing incomplete coverage, high motion peaks, ghosting and other artifacts (no numeric threshold given) | quote: "A ﬁnal dataset of 871 subjects, including 403 ASD patients and 468 TCs, was obtained by removing the samples with incomplete brain coverage, high motion peaks, ghosting and other scanner artifacts."

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

Single ABIDE I site (University of Michigan), 48 ASD and 65 TC, no significant age/sex differences; TC inclusion/exclusion per ABIDE project criteria (IQ>=85, age>=7, SCQ<10, SCAS OC<6) | quote: "The publicly available data set comprises data from 48 people with ASD and 65 TCs, with no signiﬁcant diﬀerences in demographics between the two groups."

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

ABIDE-I, n=211 (103 ASD/108 NT) from 3 sites (PITT, NYU, USM); males only; excluded on >2SD mean FD (n=10) and rs-fMRI FD>0.3mm (n=9). | quote: "After excluding cases with high  head motion (cutoff: >2SD over mean framewise dis­ placement, n = 10), we obtained a sample size of n = 211  (103/108 ASD/NT)."

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

ABIDE I (full preprocessed release): 539 ASD, 573 controls; no QC/exclusion rule described in this report. | quote: "The ABIDE dataset contains 539 individuals with ASD and 573 control subjects."

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

ABIDE II, KKI site only: 211 children originally (56 ASD/155 TC, ages 8-13), 14 ASD and 28 TC excluded for poor normalization/excessive motion/spDCM non-convergence, final n=42 ASD/127 TC. | quote: "a total of 14 children with ASD and 28 TC children were excluded, and the ﬁnal sample included 42 children with ASD and 127 TC children."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

ABIDE I, UCLA site only: initially 49 ASD/33 TC, after removing participants with large head motion, final n=41 ASD/32 TC. | quote: "Participants with large motions were removed from the dataset, resulting in 32 participants in the TC group and 41 in the ASD group."

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

ABIDE I+II, all publicly available sites; N=1,017 ASD and 1,127 TD, age-stratified into 8 bins; no additional QC exclusion beyond the full public release. | quote: "This study includes all sites publicly available through ABIDE I and ABIDE II. They were comprised of 1,127 TD and 1,017 ASD."

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

ABIDE-II, two sites (GU n=82, KK n=194 before exclusion); final combined n=276 (85 ASD/191 TD), ages 8-13; excluded for missing behavioral data (n=9), behavioral outliers (>3SD) or inconsistency (>7), and >4mm maximum absolute head-motion displacement (26 participants). | quote: "Twenty-six participants had excessive head motion on their fMRI scan (>4 mm maximum absolute 
20 
displacement)."

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

ABIDE-I, N=1112 initially; excluded for missing files, Stanford site (spiral acquisition), Leuven-1 site (unknown TR), PCP rater quality fail, and QC-FC association/distance-dependence checks; final n=395 ASD/425 TD (820 total). | quote: "After removing subjects based on these exclusion criteria, we were left with 395 subjects in the ASD group and 
425 subjects in the TD group"

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

Multi-site ABIDE: 85 ASD, 163 matched controls, N=248; inclusion required T1 + rs-fMRI full coverage, full-scale IQ>100, a framewise-displacement criterion, and >=7 ASD/7 control per site; individuals with >10% scrubbed frames excluded. | quote: "Resting-state fMRI (rs-fMRI) and structural imaging data of 85 individuals with ASD and 163 matched controls from multiple sites of the ABIDE data set (Di Martino et al., 2014) were included in this study for a total of N = 248 individuals."

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

ABIDE I, 16 sites, C-PAC-derived CC200/CC400 Preprocessed Connectomes Project release; after filtering for missing/invalid data, N=1035 (505 ASD/530 TDC); no further custom exclusion rule described. | quote: "After ﬁltering
for missing and invalid data, it contains 1035 subjects, of which 505 are ASD
patients and 530 are TDC (typically developing control subjects)."

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

ABIDE, 3 sites (CALTECH, CMU, KKI): 41 ASD, 41 NC (N=82); no explicit QC/exclusion rule beyond site/subject counts reported. | quote: "The sample size is 82 subjects (41 ASD and 41 normal cases) collected from three different sites  of Autism Brain Imaging Data Exchange (ABIDE)."

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

ABIDE-I, all 17 sites; starting N=1112 (539 ASD/573 controls); after removing subjects with missing information, final N=1035 (505 ASD/530 controls); per-site breakdown given in Table 1. | quote: "The original ABIDE dataset claimed to have 1112 subjects consisting of 539 ASD and 573 Healthy controls subjects. However, after removing subjects with missing information we have a total of 1035 subjects which is"

### Processing

#### RQ2 — Pipeline and parcellation

**Question.** Which preprocessing pipeline (e.g. Preprocessed Connectomes Project CPAC/DPARSF/NIAK/CCS, strategy) and atlas/parcellation were used?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

Not applicable — raw/minimally processed data release, no connectivity pipeline or atlas applied by this paper

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

No pipeline or atlas/parcellation reported; the paper uses MRI-derived images/heat maps directly as CNN/transfer-learning input with no stated connectivity feature extraction

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

fMRIPrep v1.3.1 pipeline; no parcellation/atlas used (whole-thalamus seed-based voxelwise GLM, not a parcellation-based connectome) | quote: "Func- tional data from both the HFASD and ABIDE cohorts were preprocessed identically using fMRIPrep v1.3.152, a pipeline that uses a combination of tools from existing neuroimaging software packages."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

Custom preprocessing pipeline (slice-timing, 24-parameter motion regression, CompCor, detrending, band-pass filter, FSL BBR + ANTs registration); Harvard-Oxford atlas for cluster labelling; ComBat used for site harmonisation across ABIDE I/II collections | quote: "R-fMRI image pre-processing steps included: slice time correction, 24 motion param- eters regression [57], component-based noise reduction (CompCor) [58], removal of linear and quadratic trends, and band-pass filtering (0.01–0.1 Hz, for all metrics but fALFF)."

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

C-PAC pipeline (Preprocessed Connectomes Project) for rs-fMRI; FreeSurfer for structural; 100-region Schaefer-Yeo cortical parcellation atlas for connectivity | quote: "For the resting-state functional brain scans in ABIDE, we built on data previously made available by the Preprocessed Connectomes initiative (http://preprocessed-connectomes- project.org/abide). The preprocessing was performed with C-PAC (https://fcp-indi.github.io) and included slice time correction, head motion correction, skull stripping, and intensity nor- malization. The rs-fMRI data were detrended and adjusted for common nuisance effects related to head motion, white matter, and cerebrospinal fluid signals using CompCor [58], fol- lowed by band-pass filtering (0.01 to 0.1 Hz)."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

Athena pipeline; no cortical parcellation atlas named — analysis uses 65 cortical ROIs regressed against cerebellar principal components, not a specific named cortical atlas in the extracted text | quote: "We preprocessed the imaging data using the Athena pipeline (www.nitrc.org/plugins/mwiki/index.php/neurobureau:Athena Pipeline). The pipeline focused on providing systematic processing of fMRI data, including the following main steps: exclusion of the ﬁrst four scans; slice timing correction;"

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

CPAC pipeline (one of four Preprocessed Connectomes Project pipelines); three atlases: AAL (116 ROIs), Craddock 200 (CC), Eickhoff-Zilles (EZ) | quote: "We, therefore, leverage the CPAC pipeline, hereinafter referred to as the ABIDE I CPAC data."

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Custom SPM12/DARTEL preprocessing pipeline (realignment, normalization, smoothing, band-pass filter, scrubbing); 200-ROI Craddock atlas for connectivity matrices | quote: "Data presented in this study underwent standard fMRI pre- processing (i.e., realignment, normalization, and smoothing) implemented in SPM12b. Data were preprocessed according to standard SPM protocols including realignment, normalization to a study specific template using DARTEL, smoothing, band- pass filtering (0.01–0.05 Hz), and scrubbing to account for head movements (63)."

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

Custom SPM8 + in-house MATLAB preprocessing pipeline (motion correction, co-registration, MNI normalization); no atlas/parcellation — features are 3D-HOG voxel-based image-texture descriptors, not ROI connectivity | quote: "For preprocessing, we used SPM8, a software package designed for analyzing brain imaging data and also for preprocessing fMRI data [27, 28] and our own in-house MATLAB code."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

Custom SPM8 preprocessing pipeline (realignment, coregistration, MNI normalization, smoothing, nuisance regression, band-pass filter); no ROI atlas/parcellation — whole-brain voxel-wise functional connectivity density mapping | quote: "Datasets were preprocessed with SPM8 (http://www.ﬁl.ion.ucl. ac.uk/spm/software/spm8/). The ﬁrst step was realignment for head motion correction. Images were realigned to the ﬁrst image and a mean echo planar image (EPI) was created during this step. Subsequently, structural T1 images were coregistered to their mean EPI data. Registered EPI data of each subject were normalized to Montreal Neurological Institute (MNI) template and spatially smoothed with 8 mm of full-width at half- maximum. Then, in the temporal domain, the linearly increasing trend due to heat absorption was removed at each voxel, and the eﬀects of the head motion, white matter, cerebrospinal ﬂuid, and global signal were regressed out. Lastly, temporal band-pass ﬁltering was applied (0.01–0.08 Hz)."

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

CONN toolbox/SPM12 pipeline (realignment, slice-timing, MNI normalization, 4mm smoothing, CompCor); cerebellar seed ROIs from the Diedrichsen probabilistic MR atlas of the human cerebellum, not a whole-brain parcellation. | quote: "Seed ROIs in the cerebellum were created using the probabilistic MR Atlas of the human cerebellum"

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

CPAC pipeline (Preprocessed Connectomes Project); Harvard-Oxford atlas (110 ROIs) as the primary parcellation, with AAL atlas tested for comparison. | quote: "We use the Harvard Oxford (HO) atlas [23], so we  have N = 110 nodes."

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

CCS (Connectome Computation System) pipeline, filt_global preprocessing strategy; no ROI atlas/parcellation — raw 2D slice images used directly as CNN input. | quote: "In our experiments, we used ABIDE-I data processed through the Connectome Computation System (CCS) (Craddock et al., 2013)."

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

C-PAC pipeline, volumes downsampled to 4mm MNI; no ROI atlas or connectivity feature extraction — the model operates on raw 4D volumes. | quote: "We preprocessed the data with the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) and the fMRI volumes are downsampled to 4 mm in MNI."

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

DPARSF pipeline (head motion correction, nuisance regression, MNI standardization, band-pass filter); two parcellations used for multi-scale representation — AAL (116 ROIs) and CC200 (200 ROIs). | quote: "by partitioning the brain into multiple ROIs using two atlases, i.e., Automated Anatomical Labeling (AAL) (Tzourio-Mazoyer et al., 2002) atlas with 116 ROIs and Craddock200 (CC200) (Craddock et al., 2012) atlas with 200 ROIs."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

C-PAC pipeline; ABIDE A uses CC200-based fMRI connection networks (Parisot 2017 setup), ABIDE B uses three atlases — CC200, AAL, Dosenbach160. | quote: "The dataset integrates three brain atlases (CC200,
AAL - Automated Anatomical Labeling, and DOS - Dosenbach160)"

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

CPAC pipeline (band-pass filtered 0.01-0.1Hz, no global signal regression), Harvard-Oxford atlas (110 ROIs). | quote: "it is parcellated using the Harvard-Oxford (HO) atlas. After downloading the pre-processed data, 110 ROIs are acquired using the HO atlas."

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

DPARSF pipeline (SPM8-based, 24-parameter motion/WM/CSF regression, bandpass filtering); three atlases used jointly — AAL (116 ROIs), CC200 (200 ROIs), Dosenbach160. | quote: "METAFormer employs a multi-atlas approach, where flattened connectivity matrices from the AAL, CC200, and DOS160 atlases serve as input to the transformer encoder."

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

Connectome Computation System (CCS) pipeline; Craddock 200 (CC200) atlas (200 ROIs). | quote: "The resting state fMRI data was then parcellated into
200 regions of interest (ROIs) using a spatially constrained
spectral clustering algorithm based on functional parcellations by
Cameron Craddock (Craddock et al., 2012)."

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

CPAC (Configurable Pipeline for Analysis of Connectomes) via the Preprocessed Connectomes Project, v1.0.2a for ABIDE-II, with global signal regression and band-pass filtering; seven atlases: HO, EZ, TT, CC200, CC400, AAL, DOS160. | quote: "The Preprocessed Connectomes Project (PCP) released preprocessed versions of ABIDE using several pipelines [4]. We used the data processed through Conﬁgurable Pipeline for Analysis of Connectomes (CPAC). This pipeline includes slice timing correction, motion correction, global mean intensity normalization and standardization of functional data to MNI space (3x3x3 mm resolution) before the extraction of ROI time series."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

fconn1000 pipeline (same as used for the IMPAC challenge); seven functional atlases (BASC at 64/122/197 ROIs, Craddock 249-ROI atlas, and others) plus FreeSurfer structural features. | quote: "The IMPAC fMRI and sMRI were processed using the fconn1000 ­pipeline41. For the fMRI connectivity features, the TSE connectivity metric was fit on either the training data alone (IMPAC models) or the entire IMPAC dataset (ABIDE 1 and 2 datasets), and the TSE values per-ROI timeseries for the ABIDE dataset were calculated."

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

CPAC (Configurable Pipeline for Analysis of Connectomes) via the Preprocessed Connectomes Project, band-pass filter 0.01-0.1Hz, no global signal regression; Harvard-Oxford atlas (111 ROIs) primary, Craddock CC200 (200 ROIs) as a replication atlas. | quote: "we downloaded Re- gions of Interests (ROIs) fMRI series of the top four largest sites (UM1, NYU, USM, UCLA1) from the preprocessed ABIDE dataset with Conﬁgurable Pipeline for the Analysis of Connec- tomes (CPAC), band-pass ﬁltering (0.01 - 0.1 Hz), no global signal regression, parcellated by Harvard-Oxford (HO) atlas."

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

Preprocessed Connectomes Project, CPAC pipeline (slice timing correction, motion correction, voxel intensity normalisation, nuisance regression with 24 motion parameters, CompCor, band-pass filter 0.01-10Hz); CC400 functional parcellation atlas. | quote: "The Preprocessed Connectomes Project (PCP) is a publicly available preprocessed version of data from both the 1,000 Functional Connectomes Project (FCP) and the International Neuroimaging Data-Sharing Initiative (INDI)3. We used data from the FCP using the conﬁgurable pipeline, the Analysis of Connectomes (CPAC)."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

SPM8 plus in-house MATLAB code (preprocessing identical to a prior published pipeline); no named ROI atlas — functional features come from subject-level spatial ICA components rather than an ROI parcellation. | quote: "For preprocessing fMRI and MRI scans, we used SPM8 (http://www.fil.ion.ucl.ac.uk/spm/ software/spm8/) and our own in-house MATLAB code. Preprocessing was identical to that used in Ghiassian et al. [13]."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

Connectome Computation System (CCS) pipeline; Automated Anatomical Labeling (AAL) atlas (90 ROIs, 4,005 FC links); Pearson correlation connectivity with site/age/gender/handedness regressed out via OLS. | quote: "The rs- fMRI data were processed using Connectome Computation System (Xu et al., 2015) pipeline, which includes slice timing correction, motion realignment, and intensity normalization. Nuisance variable regression (Fox et al., 2005; Lund et al., 2005) was implemented through band-pass ﬁltering and global signal regression strategies to clean confounding variations introduced by heartbeats and respirations, head motion, and low frequency scanner drifts. Furthermore, boundary-based rigid body and FMRIB’s linear & nonlinear image registration tools (Andersson et al., 2008; Ratziu et al., 2008) were used to register functional to anatomical images. Then, both functional and anatomical images were normalized to a standard template space, the Automated Anatomical Labeling atlas (Tzourio-Mazoyer et al., 2002)."

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

No named standard ABIDE pipeline (e.g. CPAC/DPARSF) — iFC was computed using the same in-house SPM-based seed-based procedure as the original (non-ABIDE) sample; analysis is seed-based (right pSTS seed), not atlas/parcellation-based. | quote: "For the ABIDE-replication dataset (278 ASD/306 TD participants) (Supplementary Table S1), we computed iFC and mean FD scores using the same procedures as described above (Supplementary Figure S3B). Within each site, groups displayed comparable mean FD scores (except for one site). Across sites, micro-movements were greater within the ASD than in the TD group [F(1,566) ¼ 4.23, P ¼ 0.041] (Supplementary Table S1 and Figure S3B). As for the ori- ginal sample, we corrected for micro-movements by including mean FD scores as a nuisance covariate in the primary group analysis"

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

DPARSF preprocessing (DICOM-to-NIFTI, removal of first 10 volumes, slice timing, realignment, EPI-template normalisation, smoothing, linear-trend removal, temporal filtering, covariate removal); AAL atlas (90 ROIs, 4,005 pairwise connectivity edges) plus graph-theory metrics. | quote: "all the fMRI images are preprocessed by the Data Processing Assistant for Resting- State fMRI (DPARSF) software (Cui et al., 2015) (http://d.rnet. co/DPABI/DPABI_V2.3_170105.zip). The whole preprocessing procedures include:(1) Converting DICOM to NIFTI, (2) Removing the ﬁrst 10 time points, (3) Slicing timing, (4) Realigning, (5) Normalizing with the echo-planar imaging (EPI) template, (6) Smoothing, (7) Removing the linear trend, (8) Temporal ﬁltering, (9) Removing covariates."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

C-PAC (Configurable Pipeline for the Analysis of Connectomes), following a Preprocessed Connectomes Project strategy chosen for replicability; no ROI atlas used — voxel-wise summary-measure volumes (e.g. ReHo, ALFF) are fed directly into a 3D-CNN. | quote: "The preprocessing was done using the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC, (12). We followed a preprocessing strategy adopted by the Preprocessed Connectome Project initiative3. This will allow others to replicate and extend the ﬁndings in this paper."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

CPAC (Configurable Pipeline for the Analysis of Connectomes) via the Preprocessed Connectomes Project; AAL atlas (116 ROIs); multiple connectivity measures (Spearman, percentage-bend and partial correlation, SICE, mutual information). | quote: "we used the preprocessed version of ABIDE I (Di Martino et al., 2014) data publicly available via the Preprocessed Connectome Project (Cameron et al., 2013b). The preprocessing pipeline we used for this study is the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) (Cameron et al., 2013a). Regions of interests (ROIs) were deﬁned as the 116 regions in the automatic anatomical labeling (AAL) atlas (Tzourio-Mazoyer et al., 2002)."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

C-PAC pipeline, Harvard-Oxford atlas (111 ROIs) | quote: "We follow the same preprocessing pipeline (C-PAC)
and atlases (Harvard-Oxford) as described in [16]"

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

Pipeline name/version not reported in available text; Schaefer-400 cortical + Harvard-Oxford subcortical atlas used, ComBat for site harmonisation | quote: "Schaefer parcellation to divide the cortex of each participant into 400 functional regions of 
interest (ROIs) (37), combined with 15 subcortical ROIs from the Harvard-Oxford subcortical 
atlas (38)"

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

Not reported for the ABIDE experiment specifically; PANDA toolbox is used as the comparison baseline for ABIDE network construction, but the pipeline/atlas used for the proposed method's own ABIDE preprocessing is not described. | quote: "ABIDE 
PANDA 
7.25 × 102 
0.64 
technician-dependent 
DGCL 
2.19 × 100 
0.71 
highly-automated"

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

C-PAC pipeline (Preprocessed Connectomes Project), CC200 atlas | quote: "The rs-fMRI data utilized in this study was preprocessed with 
the Configurable Pipeline for the Analysis of Conenectomes (C-
PAC)."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

C-PAC pipeline; group-ICA-derived brain functional networks (no ROI atlas, data-driven ICA parcellation) with dual regression | quote: "We preprocessed the data using a widely adopted pipeline called
Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC)
(Craddock et al., 2013)"

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

CC200 atlas (200 ROIs, spatially constrained spectral clustering); preprocessing pipeline details deferred to an unavailable supplement | quote: "each rs-
fMRI image was partitioned into 200 (for ADHD, AD, and ASD)
or 125 (for PTSD/PCS) functionally homogenous regions of
interests (ROIs) using spatially constrained spectral clustering
[cc200 template]"

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

C-PAC pipeline, Harvard-Oxford atlas | quote: "For preprocessing of
the ABIDE dataset, we use the Configurable Pipeline for the
Analysis of Connectomes (C-PAC) [41]"

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

C-PAC (Preprocessed Connectomes Project); atlases compared: Harvard-Oxford, Yeo, ICA, MSDL, K-Means, Ward. | quote: "We speciﬁcally used the data processed with the Conﬁgurable Pipeline for the Analysis of Connectomes [34] (C-PAC)."

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

C-PAC pipeline; Harvard-Oxford (HO) atlas. | quote: "the mean time series for a set of regions extracted from the Harvard Oxford (HO) atlas (Desikan et al., 2006) were computed"

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

Custom SPM8 pipeline (not C-PAC/DPARSF/NIAK); 7266-ROI whole-brain gray-matter lattice (no named cortical atlas). | quote: "Preprocessing was performed in MATLAB (Mathworks, Natick, MA) using SPM8 (Wellcome Trust, London) software."

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

C-PAC pipeline; Harvard-Oxford atlas (110 ROIs). | quote: "We, subsequently, extract the mean time series for a set of regions from the Harvard Oxford (HO) atlas comprising R = 110 cortical and subcortical ROIs"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

Four Preprocessed Connectomes Project pipelines compared: CCS, C-PAC, DPARSF, NIAK; no ROI atlas used (whole-volume images rather than ROI connectivity). | quote: "Selected strategies are Connectome Computation System (CCS), Conﬁgurable Pipeline for the Analysis of Con- nectomes (CPAC), Data Processing Assistant for Resting-State fMRI (DPARSF) and Neuroimaging Analysis Kit (NIAK)."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

Custom FSL-based pipeline (not C-PAC/DPARSF/NIAK/CCS); no named cortical atlas — voxelwise 6mm-isotropic lattice. | quote: "We applied scrubbing so that we kept 125 volumes with lowest framewise displacem"

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

SPM8 and DPARSF pipeline; AAL atlas. | quote: "it was based on the automated anatomical labeling (AAL) template extract the averaged fMRI time series"

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

Custom AFNI-based pipeline (3dWarpDrive motion correction, N27 atlas spatial warping); TT_Daemon atlas (240 ROIs) for ROI-level analysis. | quote: "The 240 regions of interest (ROIs) defined for this study were extracted from the TT_Daemon human brain atlas [43] provided with the AFNI package [44]."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

No connectivity pipeline/atlas used; SPM8 realignment applied to raw scans to extract 6 rigid-body head-motion parameters, which are themselves the analysed signal. | quote: "The output with the six motion parameters (3 translations in x, y, z directions,  and 3 rotations: pitch (about x-axis), roll (about y-axis), and yaw (about z-axis)) is recor"

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

C-PAC pipeline; AAL90 atlas (90 ROIs). | quote: "The selected mean time-series
correspond to the Automated Anatomical Labeling atlas on 90 regions of interest
(AAL90)"

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

No connectivity pipeline or atlas; raw 3D NIfTI volumes converted to 2D axial-plane image slices with MRIcron for direct CNN input. | quote: "MRIcron software was used to convert the  3D data format into 2D data images."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

ABIDE Preprocessed Connectomes Project CPAC pipeline; four atlases compared (AAL, Harvard-Oxford, Craddock-200, Power). | quote: "using the Configurable Pipeline for the Analysis of Connectomes (CPAC) (31), that includes slice- timing, motion correction, intensity normalization, nuisance signal removal"

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

CPAC pipeline (slice timing, motion correction, nuisance regression, band-pass filtering); three atlases (AAL, CC, EZ) used to build Pearson-correlation connectivity matrices. | quote: "The data is preprocessed using the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) pipeline, which includes essential steps such as slice timing correction, voxel intensity normalization, motion correction, nuisance signal removal, global signal regression, band-pass ﬁltering, and spatial registration."

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

No named preprocessing pipeline (e.g. CPAC/DPARSF); connectivity derived using the BASC atlas (scale 122 via MSTEPS) and Pearson correlation. | quote: "we used multiscale functional brain parcels. Brain parcels were created using a method known as the bootstrap analysis of stable clusters called BASC [32]."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

CPAC (filter_noglobal) pipeline; AAL (116 ROIs) and CC200 atlases with Pearson-correlation connectivity. | quote: "The mean time series from 116 regions of interest (ROIs) based on the automated anatomical labeling (AAL) atlas [23] are used for experiments."

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

Preprocessed Connectomes Project CPAC pipeline; CC200 atlas, 200-region parcellation. | quote: "We extracted rsfMRI time series using a 200-region parcellation CC200[?], estimated subject-wise time-resolved connectivity matrices with windows lengths ranging from 10 to 20 volumes (20-40s) and calculated node variability."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

CPAC pipeline via the Preprocessed Connectomes Project; Harvard-Oxford atlas (111 ROIs), distance-correlation connectivity. | quote: "Data preprocessing was performed using the configurable pipeline for the analysis of con- 
nectomes. According to the Harvard-Oxford atlas, there are 111 ROIs in the brain 
[32]."

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

DPARSF pipeline (slice timing, head-movement correction, normalization, smoothing, band-pass filter, nuisance regression); AAL atlas (116 ROIs). | quote: "we used the data Processing As-
sistant for Resting-State fMRI (DPARSF) t"

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

Lab-made FSL pipeline (FSL-BET, FSL-BBreg, FSL-FNIRT, CompCor, dual regression), noted as similar to C-PAC; no ROI atlas, instead the Smith et al. 2009 RSN10 ICA template. | quote: "We subsequently applied 
dual-regression analysis18 by using the FSL general linear model (GLM) and the 10-brain resting-state networks 
(RSN10)"

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

GRETNA pipeline; 512-region random parcellation for dynamic connectome nodes | quote: "All rsfMRI data were preprocessed with a standardized and harmonized pipeline using the GRETNA package (36)."

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

SPM12-based preprocessing producing voxel-wise fALFF (functional) and GM volume (structural) maps; no atlas/parcellation used (voxel-wise, fused via MCCAR+jICA) | quote: "SPM12, wherein the above steps are integrated into a unified model [39]."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

C-PAC v1.8.0 pipeline; 11-region Brodmann-area atlas parcellation of fALFF and ReHo maps | quote: "The package CPAC v1.8.0 was used for fMRI pre-processing including head motion correction, scrubbing, and nuisance regression."

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

Freesurfer v6.0 recon-all (Desikan-Killiany-Tourville atlas) for structural; C-PAC for functional with Harvard-Oxford atlas (103 regions after exclusion) | quote: "The rs-fMRI scans selected from ABIDE I and ABIDE II cohorts were processed with the Configurable Pipe- line for the Analysis of Connectomes (C-PAC) [20]"

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

C-PAC pipeline (Preprocessed Connectomes Project) with CC200 functional parcellation | quote: "We used the preprocessed data using the Conﬁgurable Pipeline for the Analysis of Connectomes C-PAC pipeline (Craddock et al., 2013)"

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

CCS (Connectome Computation System) pipeline (slice timing, motion realignment, global intensity normalisation, global signal regression + bandpass filter strategy); ReHo derivative used, no ROI atlas (voxel-wise) | quote: "we downloaded fMRI data (derivatives) pro- cessed with the Connectome Computation System (CCS) pipeline [9] which performs slice timing correction, motion realignment and global intensity normalisation."

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

CPAC pipeline; no ROI atlas — raw downsampled 4D spatio-temporal fMRI volumes (28x28x28x32) used directly | quote: "The preprocessing method used in this paper is the conﬁgurable pipeline for the analysis of connectomes (CPAC)"

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

C-PAC pipeline; AAL atlas, first 90 ROIs as network nodes | quote: "Using automated anatomical labeling (AAL), we then used the ﬁrst 90 regions of interest (ROIs) as nodes"

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

C-PAC pipeline (slice-time/motion correction, CompCor, band-pass 0.01-0.1Hz, no GSR); surface-based Conte69 template, no standard ROI atlas. | quote: "based on  the configurable pipeline for the analysis of connectomes  (C-PAC) (https://fcp-indi.github.io/) [83]"

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

C-PAC pipeline, regional homogeneity (ReHo) derivative from the Preprocessed Connectomes Project; no ROI atlas (voxel-wise, grey-matter masked). | quote: "We speciﬁcally focused on the regional homogeneity (ReHo) fMRI derivative (Zang et al. 2004) from the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) pipeline"

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

GRETNA v2.0.0 (SPM12-based) preprocessing (slice timing, realignment, MNI normalization, 6mm FWHM smoothing); AAL atlas, 24 spherical (6mm radius) ROIs across 7 networks. | quote: "Data processing was performed with the GRETNA toolbox (v2.0.0) (Wang et al., 2015) based on SPM12."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

Slice-time and motion correction, MNI registration, bandpass filter (0.009-0.08Hz), 6mm FWHM smoothing (no named pipeline/version given); first 90 AAL ROIs as nodes. | quote: "We then use the ﬁrst 90 AAL ROIs as nodes, and take the average of all voxels’ temporal proﬁles within each ROI as region level signal for all subjects"

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

No connectivity pipeline/atlas used; head-motion (linear/angular speed) parameters derived directly from rs-fMRI realignment, analyzed via custom Gamma-distribution/stochastic signature methods.

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

FSL/AFNI preprocessing (deobliquing, motion correction via MCFLIRT, skull-stripping, 6mm FWHM smoothing); Shen 268-node functional atlas for connectivity ROIs. | quote: "A functionally defined atlas, consisting of 268 cortical and subcortical regions-of-interest (‘nodes’)"

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

CONN toolbox pipeline (motion correction, slice-timing correction, outlier detection, segmentation/normalization, denoising, 0.008Hz high-pass filter); Schaefer 200-parcel atlas. | quote: "We used the CONN functional connectivity ​toolbox69 to process the rs- fMRI data from ABIDE-I."

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

Custom FSL-based pipeline (MCFLIRT motion correction, FLIRT registration, scrubbing, 0.01-0.1Hz band-pass, nuisance regression); Power et al. (2011) 264-ROI atlas organized into 11 RSNs. | quote: "ROIs were deﬁned as 10 mm diameter spheres whose center coordinates are given in MNI atlas space (Power et al., 2011)."

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

C-PAC pipeline; Craddock CC200 and CC400 parcellations (Preprocessed Connectomes Project ABIDE derivatives). | quote: "We use Craddock 200 (CC200) data set, where the
imaging data is ﬁrst preprocessed using the Conﬁgurable Pipeline for Analysis
of Connectomes (CPAC)"

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

DPARSF preprocessing (discard first 5 volumes, slice-timing, motion realignment, MNI normalization, 8mm FWHM smoothing); AAL atlas (116 ROIs, 22 DMN ROIs used). | quote: "The DPARSF is a MATLAB toolbox for fMRI data pre-
processing and analysing [17]."

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

C-PAC pipeline (structural: skull stripping, tissue segmentation, MNI normalization; functional: slice-time correction, motion correction, band-pass filtering, registration); AAL atlas, 90 regions, 90x90 connectivity matrix. | quote: "We have used the brain Automated anatomical labelling (AAL) template which divides the brain
into 90 regions."

### Claim

#### RQ3 — Claim type

**Question.** Is the main claim associational (group difference) or predictive (classification/regression)?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

descriptor — this paper describes the ABIDE II data release itself rather than performing a group-difference or predictive analysis | quote: "a new multi-site open data resource containing 1,044 independent datasets (ASD N = 487; Controls N = 557)"

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

predictive — ASD vs control classification using CNN and transfer learning | quote: "Our proposed   optimized version of CNN achieved 81.56% accuracy. This   outperforms prior conventional approaches presented only on   the ABIDE I datasets."

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

associational — group-difference seed-based connectivity analysis (ABIDE used to validate a primary-cohort finding) | quote: "The secondary cohort was a subset of the ABIDE database consisting of 58 HFASD (25.4[7.8] years, 37.9% female) and 51 typically developing controls (24.4[6.7] years, 39.2% female)."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

associational — group-difference GLM analysis of diagnosis, sex and their interaction | quote: "Discovery analyses in ABIDE revealed significant main effects of diagnosis and sex across the intrinsic func‑ tional connectivity of the posterior cingulate cortex, regional homogeneity and voxel-mirrored homotopic connectiv‑ ity (VMHC) in several cortical regions, largely converging in the default network midline."

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

predictive — classification of ASD vs TD using functional connectivity, studying how population diversity affects prediction accuracy | quote: "In the ABIDE cohort, when we trained and tested on data with similar distributions (first column), the contiguous scheme reached better prediction performance than the diverse scheme, with the random scheme lying in between. This trend remained stable as we increased the number of strata used for training."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

associational — group-difference (ASD vs TD) cortico-cerebellar connectivity, with discovery + independent validation | quote: ", namely, the right fusiform gyrus [β = −0.042, t-value = −3.689, p = 0.005 —t-test (GLM)], the right postcentral gyrus [β = −0.038, t-value = −3.131, p = 0.027 — t-test (GLM)], the right superior temporal gyrus [β = −0.034, t-value = −3.082, p = 0.027 –t-test (GLM)], the right middle temporal gyrus [β = −0.039, t-value = −3.783, p < 0.001 —t-test (GLM)], and the left middle temporal gyrus [β = −0.056, t-va"

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

predictive — ASD vs TC diagnostic classification using a weighted deep ensemble network | quote: "We use rs-fMRI and demographic data from ABIDE I [11], the first phase of ABIDE, with 505 autistic individuals and 530 Typical Controls (TCs)."

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

predictive — ASD vs TD classification comparing six ML classifiers | quote: "The inputs to the classification pipeline are the 77 ASD and 77 TD connectivity matrices (hence 154 data samples in total), where each connectivity matrix consists of 19,900 features."

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

predictive — ASD vs control classification combining functional/structural MRI with personal characteristic data | quote: "This dataset is comprised of resting state fMRI and T1-weighted structural MRI scans from 1112 subjects, including patients with autism and healthy controls. ABIDE participant data was col- lected at 17 different institutions in North America and Europe."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

associational — group-difference (ASD vs TDC) voxel-wise functional connectivity density analysis

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

associational — group-difference analysis of ASD vs TD cerebellar-cerebral connectivity, with a replication test in ABIDE II; no classifier or prediction model. | quote: "The ASD group showed signiﬁcantly increased or decreased FCs between the cerebellar subregions and cerebral cortices, relative to the TD group in the original dataset."

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

predictive — graph attention network classification of ASD vs HC from functional brain networks. | quote: "GAT-LI, which learns to classify functional brain networks of ASD individuals versus healthy controls (HC)"

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

predictive — deep CNN (DarkASDNet) binary classification of ASD vs. TC from fMRI slice images. | quote: "we considered 3D fMRI data to predict binary classiﬁcation between ASD and typical control (TC)"

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

predictive — binary classification of ASD vs TD from raw 4D resting-state fMRI using a hybrid 3DCNN/3D-ConvLSTM. | quote: "We evaluate our proposed model on the publicly available ABIDE dataset to demonstrate the capability of our model to classify Autism Spectrum Disorder (ASD) from resting-state fMRI data."

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

predictive — multi-scale graph convolutional network classification of ASD vs NC. | quote: "The MGRL consists of three major components: (1) multi-scale FCNs construction using multiple brain atlases for ROI partition, (2) FCNs representation learning via multi-scale GCNs, and (3) multi-scale feature fusion and classiﬁcation for ASD diagnosis."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

predictive — multimodal graph-learning classification of ASD vs TC. | quote: "DeepASD, an end-to-end trainable regularized graph learning method for ASD prediction"

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

predictive — ASD vs TD classification using non-linear high-order functional connectivity and explainability-guided ROI selection. | quote: "we propose a novel explainability-guided region of interest (ROI) selection (EAG-RS) framework that identifies non-linear high-order functional associations among brain regions"

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

predictive — multi-atlas transformer classification of ASD vs TC with self-supervised pretraining. | quote: "we pro-
pose a novel Multi-Atlas Enhanced Transformer framework, METAFormer,
ASD classification."

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

associational — comparison of site-effect mitigation methods on preserving the ASD-vs-control functional connectivity group difference (effect size), not a diagnostic classifier. | quote: "Preservation of consistent FC alterations in patients were evaluated for each method through the effect sizes (Hedge’s g) of patients vs. controls."

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

predictive — autism vs. control diagnostic classification using a 3D CNN on connectivity fingerprints. | quote: "We showcase our approach on a challenging large-scale dataset (ABIDE, with N > 2, 000) and report state-of-the-art accuracy results on rs-fMRI- based discrimination of autism patients and healthy controls."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

predictive — ASD vs. TD diagnostic classification, trained on IMPAC and externally validated on ABIDE I/II. | quote: "Our model achieves state-of-the-art 80% area under the ROC curve (AUROC) in diagnosis on test data from the IMPAC dataset; and 86% and 79% AUROC on the external ABIDE I and ABIDE II datasets (with further improvement to 93% and 90% after supervised domain adaptation)."

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

predictive — ASD vs. HC classification using a privacy-preserving federated-learning framework with domain adaptation. | quote: "The mean accuracy of Fed was higher than the best Cross learning case for each single site. In addition, Fed was signiﬁcantly bet- ter than Single by two sample t test with p < 0.001 for each site."

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

predictive — ASD vs. control classification using a CNN on functional connectivity matrices. | quote: "detect ASD correctly with an accuracy of 70.22% using the ABIDE I dataset and the CC400"

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

predictive — ASD vs. control classification using combined structural-texture and functional-ICA features with an SVM. | quote: "achieving an accuracy of 0.673 on the ADHD-200 holdout data and 0.643 on the ABIDE holdout data. Both of these results, obtained with the same LEFMSF framework, are the best known, over all hold-out accuracies on these datasets when only using imaging data—exceeding previously-published results by 0.012 for ADHD and 0.042 for Autism."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

predictive — ASD vs. healthy classification using a deep transfer learning neural network. | quote: "we compared the performance of our DTL-NN approach with a traditional deep neural network and support vector machine models across four ABIDE data sites that enrolled at least 60 subjects. As compared to traditional models, our DTL-NN approach achieved an improved performance in accuracy, sensitivity, speciﬁcity and area under receiver operating characteristic curve."

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

associational — group-difference analysis of pSTS resting-state functional connectivity between ASD and TD. | quote: "Analyses with the large independent ABIDE dataset replicated reductions in pSTS-iFC to fronto-parietal regions."

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

predictive — ASD vs. TC classification using an ensemble (random cluster) of SVMs. | quote: "accuracy based on the optimal feature set could reach to 96.15%."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

predictive — ASD vs. control classification using 3D-CNNs on voxel-wise temporal summary measures of rs-fMRI, with a linear-SVM comparison. | quote: "We attained results competitive on this task for a combined ABIDE-I and II datasets of ~66%. When all summary measures were combined the result was still only as good as that of the best single measure which was regional homogeneity (ReHo)."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

predictive — ASD vs. HC classification using graph-theoretical connectivity features and a linear SVM, age-stratified. | quote: "In this study, we used the fMRI data of 816 individuals enrolled in the Autism Brain Imaging Data Exchange (ABIDE) to introduce a new biomarker extraction pipeline for ASD that relies on the use of graph theoretical metrics of fMRI-based functional connectivity to inform a support vector machine (SVM)."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

predictive — ASD vs typical control classification using graph convolutional networks | quote: "The task is to diagnose a patient as being of two classes
– Autism Spectrum Disorder (ASD) or Typical Control (TC)."

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

associational — connectome-wide group-difference mega-analysis between autism and neurotypical participants | quote: "Through a mega-analytic approach (the pooling of raw data acquired at multiple sites), we 
mapped connectome-wide differences between autistic and neurotypical individuals"

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

predictive — ASD vs HC classification using a diffusion-based graph contrastive learning model | quote: "Fig. 9. Subnetwork patterns of autism spectrum disorder. The red box
clearly indicates the difference between HC (left) and ASD (right)."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

predictive — ASD vs TC classification | quote: "Discrimination between ASD and TC subjects could be modeled 
as a supervised learning task."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

predictive — ASD vs NC classification using a 3-D CNN | quote: "The purpose of this work is to classify ASD and normal controls (NCs) using BFNs
derived from rs-fMRI."

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

associational — unsupervised clustering of connectivity compared to clinical diagnostic and phenotypic groupings (no held-out predictive classification) | quote: "For ADHD and AD, highest similarity
was achieved between connectivity and phenotypic clusters, whereas for ASD
and PTSD/PCS, highest similarity was achieved between connectivity and clinical
diagnostic clusters."

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

predictive — ASD vs HC node classification on a population graph | quote: "the aim is to separate
ASD subjects from healthy controls."

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

predictive — diagnostic classification of ASD vs typical control (TC). | quote: "Discriminating between ASD and TC individuals is a supervised-learning task."

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

predictive — ASD vs control classification via graph convolutional network. | quote: "With the ABIDE database, we aim to separate healthy controls from patients suﬀering from ASD."

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

predictive — classification of autism vs. typical development from whole-brain functional connectivity. | quote: "we evaluate clas- siﬁcation accuracy of whole-brain functional connectivity across sites"

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

predictive — ASD vs control classification using a learned graph-distance metric and k-nn classifier. | quote: "we use a simple k-nn classiﬁer with k = 3 based the estimated distances, and summarise results in Table 1"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

predictive — ASD vs. typical control classification from single-volume brain images. | quote: "we design an image genera- tor to generate single volume brain images from the whole-brain image of each subject."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

associational — within-ASD correlation between subnetwork similarity and symptom severity (no ASD-vs-control comparison in the ABIDE arm). | quote: "We selected only ASD participants from the ABIDE database since diagnostic scores were  not available for controls."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

associational — group difference in dynamic brain-state statistics between ASD and healthy controls. | quote: "we performed, respectively, two-tail two-sample t-tests for fractional occupancy, lifetimes, and interval times of HMM states between patients with subjects with ASD and HCs."

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

associational — group difference in rs-BOLD signal complexity (fractal dimension) between ASD and controls, plus correlation with ADI-R/ADOS severity. | quote: "To determine regions of the brain of ASD patients with increased or decreased signal complex- ity respect to a typical control group, we estimated the voxel-wise FD on every subject of both groups."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

associational — group difference in head-motion noise-to-signal ratio between ASD and typical controls. | quote: "We  find excess noise and randomness in the ASD cases, suggesting an uncertain motor-feedback signal."

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

predictive — classification of ASD vs. neurotypical subjects combining structural (anatomical graph) and functional (rs-fMRI) information. | quote: "The present work addresses the classiﬁcation of neu-
rotypical and ASD subjects by combining knowledge about both the structure
and the functional activity of the brain."

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

predictive — CNN (VGG-16, ResNet-50) classification of ASD vs non-ASD from 2D brain-image slices. | quote: "The results achieved using CNN models namely  VGG-16 and ResNet-50 are 63.4% and 87.0% accuracy, respectively."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

both — reports both group-difference (over/under-connectivity via permutation test) and diagnostic classification (linear SVM). | quote: "A permutation test was conducted to identify over-connectivity and under-connectivity alterations in the ASD group."

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

predictive — SSDAE+MLP hybrid deep-learning classifier for ASD vs TC. | quote: "Results: The proposed model is evaluated using multiple ASD datasets. The performance metrics include an average accuracy of 0.735, sensitivity of 0.765, and speciﬁcity of 0.752, surpassing the results of existing state-of-the-art methods."

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

predictive — RNN/LSTM/CNN and hybrid models classify ASD vs TC from functional connectivity. | quote: "The long short-term memory network (LSTM), convolutional neural network (CNN) , and hybrid models are used together for the classification process."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

predictive — a domain-adaptation (LRCDR) method with a linear SVM classifies ASD vs TD across sites. | quote: "we train a linear SVM based on the source domain data PT Xs to directly predict the labels of target domain data PT Xt."

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

both — reports a group-difference finding (increased FC variability in ASD) and machine-learning classification of ASD vs control. | quote: "pa- tients diagnosed with autism spectrum disorder (ASD) show increased FC variability in several brain regions that are associated with low FC variability in the typical brain."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

predictive — a heterogeneous graph convolutional attention network (HCAN) classifies ASD vs healthy controls. | quote: "The best classification accuracy of 82.9% is achieved."

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

predictive — ASD-HNet classifies ASD vs healthy controls from hierarchical functional-connectivity features. | quote: "ASD-HNet outperforms existing methods."

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

both — derives group-difference biomarkers (ASD vs TD, FWE-corrected t-test) in ABIDE and evaluates their diagnostic utility (ROC/AUC) in an independent local cohort. | quote: "a receiver operating characteristic analysis to evaluate the classification performances of the 
biomarkers."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

both — case-control group differences in modular dynamics (mega/meta-analysis) and prediction of SRS social-impairment severity via support vector regression | quote: "we found that brain dynamics was a significant predictor of SRS scores (r = .16, pperm = .002)"

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

both — group differences (ASD subtypes vs TDC) via back-reconstruction and dimensional prediction of ADOS/SRS scores via multivariate linear regression | quote: "The identified subtype-specific patterns are only predictive for ASD symptoms manifested in the corresponding subtypes, but not the other subtypes."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

associational — differential correlation between rs-fMRI measures (fALFF/ReHo) and gene expression, ASD vs controls | quote: "415 differentially corre- lated genes (DC genes; Diff Cor P < 0.01, CTL FDR < 0.05"

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

predictive — deep-learning ASD vs TD classification | quote: "The AUC values of 0.66±0.05 and of 0.76±0.04 were obtained in the ASD vs. TD discrimination when only structural or functional features are considered, respectively. The joint fusion approach led to an AUC of 0.78±0.04."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

predictive — ASD vs HC deep-learning classification | quote: "ASD-SAENet exhibits comparable accuracy (70.8%), and superior speciﬁcity (79.1%) for the whole dataset as compared to other methods."

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

predictive — 3D CNN classification of ASD vs controls | quote: "Our conclusion is that augmentation only provides mi- nor improvements when training 3D CNNs for classiﬁcation of ASD versus controls"

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

predictive — ASD vs TC deep-learning classification | quote: "the proposed algorithm obtains an accuracy of 72.46% in the experiment of 871 subjects, which is 5.26% higher than that of HI-GCN, 4.44% higher than that of GAT, and 2.44% higher than that of CNN."

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

both — network detection of case-control connectivity differences plus SVM classification validation | quote: "We further validate the detected subnetwork features by performing classiﬁcation analysis. We employ the support vector machine with radial basis function kernel and linear kernel as our classiﬁer."

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

associational — group-difference analysis of ASD vs NT connectivity distance, with brain-behavior correlations. | quote: "Compared to NT, ASD participants presented with widespread reductions in CD"

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

predictive — whole-brain voxel-wise classifier predicting ASD vs control diagnosis. | quote: "Using this program allowed us to build a sparse whole-brain biomarker that predicted diagnostic labels with 62% accuracy."

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

associational — group-difference analysis of effective connectivity between ASD and TC, plus brain-behavior correlation. | quote: "Compared with healthy controls, children with ASD showed decreased effective connectivity among some large- scale brain networks."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

associational — group-difference analysis of ASD vs TC connectivity using the proposed normalization method. | quote: "the analysis based on empirical Bayes normalized connectivity metrics shows signiﬁcant connectivity diﬀerences between the ASD and TC groups"

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

associational — group-difference analysis of involuntary head-motion statistics between ASD and TD, stratified and compared by age group. | quote: "The results suggest that the levels of random involuntary
motor noise are elevated in autism across age groups."

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

both — an explicit ASD-vs-TD group-difference test on behavioral-regulation scores, and a predictive (regression) connectome-based model (CPM) of those scores from resting-state FC. | quote: "Scores for all three subscales of behavioral regulation were significantly higher in 
6 
children with ASD than for TD children in all analyzed samples"

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

associational — brain-wide and region-specific group-difference analysis of graph Ricci curvature between ASD and TD. | quote: "we apply Forman–Ricci and Ollivier–Ricci curvatures to compare  networks of ASD and typically developing individuals"

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

associational — group-difference analysis of FC imbalance and FC-entropy coupling between ASD and control groups (the predictive elastic-net model is diagnosis-blind, used to relate entropy to connectivity, not to classify diagnosis). | quote: "Importantly, no information about group membership (i.e., ASD or control) has been explicitly passed to the model."

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

predictive — ASD vs TDC classification using correlation and topological features. | quote: "we explore the utility of topological features in the classiﬁcation of ASD versus typically developing control subjects."

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

predictive — ASD vs NC classification using CNN-extracted scalogram features. | quote: "The best prediction results  are 85.9% accuracy achieved by extracted the features from DenseNet201 network and classified these features by  KNN classifier."

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

predictive — ASD vs healthy-control classification using a novel feature-selection (Teacher-Student + SFFS) approach. | quote: "we have proposed a three-stage feature selection approach for the classiﬁcation of ASD on the preprocessed Autism Brain Imaging Data Exchange (ABIDE) rs-fMRI Dataset."

#### RQ4 — Evaluation

**Question.** How was the claim evaluated (statistical model and correction; CV scheme; held-out sites)?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

Not applicable — no hypothesis test or classifier is evaluated in this descriptor

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

No train/test split ratio or cross-validation scheme is reported; evaluation is reported separately per site/resource subset rather than leave-site-out | quote: "ABIDE-II data download and labelling was a   challenging task. Each image was manually labelled and   assigned a group. Each group was tested separately to compare and analyze results of each set."

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

Whole-brain seed-based GLM per seed, with site as a one-hot-encoded covariate in the ABIDE analysis; Bonferroni correction for five seeds (cluster threshold p=0.01); no leave-site-out evaluation | quote: "To account for potential con- founding effects from differences in scan acquisition parameters, we included site as a covariate in our ABIDE GLM analysis as one-hot encoded variables."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

Voxel-wise GLM with diagnosis/sex/interaction as regressors and age+mFD as covariates; voxel-level Z>3.1, cluster-level P<0.01 (Bonferroni-equivalent 0.05/5 metrics); robustness checked across alternate pipelines; no leave-site-out evaluation, but site effects removed via ComBat and findings checked for site consistency | quote: "Discovery analyses in ABIDE revealed significant main effects of diagnosis and sex across the intrinsic func‑ tional connectivity of the posterior cingulate cortex, regional homogeneity and voxel-mirrored homotopic connectiv‑ ity (VMHC) in several cortical regions, largely converging in the default network midline."

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

Propensity-score stratified train/holdout partitioning (contiguous/diverse/random schemes) with 10-fold CV within training strata; out-of-distribution evaluation in held-out strata; no explicit leave-site-out, but site is one of the matched/propensity covariates; deconfounding (linear regression, ComBat) tested but computed on all participants rather than training folds only | quote: "Similar to the computation of the pro- pensity scores, we performed deconfounding prior to our analyses, based on all the available participants instead of using only the training"

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

Linear regression (GLM) per cortical ROI vs. cerebellar PCs, with site as covariate; Benjamini-Hochberg FDR correction across 65 tests (significance threshold 5%); validated via an independent-sample (ABIDE II) replication rather than leave-site-out cross-validation | quote: "Thus, to minimize the site eﬀect in our analysis, we included it as a covariate in group-level statistics as described in the section 2.3."

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

10-fold cross-validation on each of three dataset variants (whole ABIDE I, a selector-defined 'proposed subset', and the NYU site subset); F-score feature selection described as computed on all features in the dataset rather than confined to training folds; no leave-site-out evaluation

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Nested 10x10-fold cross-validation (outer loop for performance estimation, inner loop for feature-selection/tuning-parameter optimisation); per-site z-standardization using train-only mean/SD; leave-one-site-out CV discussed as a further option but not reported as the authors' own primary result | quote: "The performance of each classifier is assessed by nested cross- validation: 10-folds are used in the outer cross-validation loop for the performance estimation, and 10-folds are used in the inner cross-validation loop to determine the optimal threshold value t for feature selection, or the optimal regularization parameter for lasso-regularized"

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

5-fold cross-validation on the training set only for feature selection (MRMR) and hyperparameter tuning, followed by a single evaluation on a completely held-out test set never used in model/feature selection; no leave-site-out evaluation — site is instead included as an input feature | quote: "Testing on the hold-out test set Dtest protected against overfitting in terms of algo- rithm choice, feature selection, parameter values, a"

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

Voxel-wise 2-tailed t-test with age and sex as covariates; FDR-corrected P<0.05 with minimum cluster size of 20 voxels; Benjamini-Hochberg correction for clinical-correlation analyses; no site covariate or leave-site-out evaluation reported | quote: "2-tailed t-test design with two covariates of age and sex was used to compute the statistical signiﬁcance of the FCD diﬀerences between the two groups. Statistical signiﬁcance was based on the false discovery rate corrected P < 0.05 together with requiring 20 voxels for the minimum continuous voxel size within a cluster (corrected P < 0.05)."

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

Two-sample t-tests on ROI-to-ROI connectivity; mean FD, FSIQ and imaging site included as nuisance covariates; Bonferroni correction (p=0.004) in the ABIDE II replication test; original dataset used voxel-height p<0.001 with FDR-corrected cluster threshold p<0.05. | quote: "mean FD scores were included as a nuisance covariate in t-tests. In addition, FSIQ and imaging sites were included as nuisance covariates. Bonferroni correction was performed for multiple comparisons (p = 0.004)."

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

Fivefold cross-validation with random pooled data split; no leave-site-out evaluation or site covariate reported; interpretation-stage rsFC group differences reported at uncorrected p<0.05. | quote: "After randomly perform- ing fivefold cross-validation data division, in each round of experiments, one-fold data"

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

No validation methodology (train/test split or cross-validation scheme) is described in the text; a single accuracy/precision/recall/F1/AUC result is reported without stated held-out procedure. | quote: "After testing our model for ASD classiﬁcation, we have achieved the highest accuracy of 94.7%, the precision of 94.5%, recall of 92.5%, f1-score of 95%, and the AUC score 94.703%."

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

5-fold cross-validation reported separately for each single site (NYU, UM) and for the pooled 19-site ABIDE-I multi-site cohort; no leave-site-out evaluation or site covariate/harmonisation described. | quote: "We report 5-fold cross validation mean F1-score and accuracy for the experiments in Table 1."

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

Random 80/10/10 train/validation/test split repeated 100 times with mean±SD reported, evaluated separately for NYU and UM (no site pooling, harmonisation, or leave-site-out). | quote: "Considering the small amount of subjects, we randomly select
80% of all the samples as training data, 10% of all samples as
validation data, and the remaining 10% as test data. We repeat the
random partition process 100 times and record the mean and SD
results of each method."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

10-fold stratified cross-validation with non-overlapping train/validation/test splits per fold; significance assessed with an independent two-sample t-test against baselines; site is incorporated as a demographic feature within the graph-construction step of a cited baseline (population-GCN) rather than via leave-site-out evaluation. | quote: "we performed a 10-
fold stratiﬁed cross-validation strategy on the two datasets."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

Stratified five-fold cross-validation, with separate validation and test folds per split and the remaining folds used for training; no site covariate, harmonisation, or leave-site-out evaluation reported despite the pooled 17-site cohort. | quote: "stratified five-fold cross-
validation is conducted, where one fold is used for t"

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

10-fold stratified cross-validation with 30% of each training fold held out as a separate validation set for hyperparameter tuning/early stopping, distinct from the held-out test fold; no site covariate, harmonisation, or leave-site-out evaluation reported for the pooled 17-site cohort. | quote: "we employed 10-fold stratified cross-validation. For each fold, the model is trained
on the remaining nine training folds and evaluated on the held-out test fold.
Further, we set aside 30% of each training fold as validation sets"

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

Group difference evaluated via Hedge's g effect size at literature-selected ROI pairs (MPFC-PCC/precuneus; frontal pole-temporal lobe), comparing original data, GLM, ComBat, and the proposed site-wise de-meaning (SWD); age and sex regressed out beforehand; no whole-brain multiple-comparison-corrected statistical test reported for this analysis. | quote: "The resting state fMRI data was then parcellated into
200 regions of interest (ROIs)"

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

10-fold cross-validation on ABIDE-I plus a fully independent test on ABIDE-II (trained on all of ABIDE-I); accuracy and ROC/AUC reported; baseline hyperparameters tuned by maximising CV accuracy itself (acknowledged optimistic). | quote: "First, we implemented a 10-fold cross-validation scheme for ABIDE-I to be consistent with previously reported classiﬁcation re- sults [1, 18]. Second, we trained each model on all of ABIDE-I and computed test performance on an independent held-out set from ABIDE-II. This is used for assessing the generalization behavior of diﬀerent classiﬁers. We report accu- racy and the receiver operating curves (ROC), along with corresponding area under the curves (AUC) for each of these scenarios."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

Models trained/tuned entirely on IMPAC; ABIDE I/II held out as external test sets with features scaled by IMPAC statistics; a second supervised-domain-adaptation analysis used 10-fold CV (early stopping on 10%, test on 90%). | quote: "The features were standard scaled by the mean and standard deviation of the IMPAC dataset."

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

5-fold cross-validation per site; accuracy compared across Single/Cross/Ensemble/Fed/Fed-MoE/Fed-Align/Mix training strategies with two-sample t-tests; no leave-site-out pooled classifier or explicit statistical site harmonisation. | quote: "The mean accuracy of Fed was higher than the best Cross learning case for each single site. In addition, Fed was signiﬁcantly bet- ter than Single by two sample t test with p < 0.001 for each site."

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

10-fold cross-validation as the primary evaluation; a leave-site-out evaluation (each of the 17 sites held out in turn) was also performed for CNN, SVM, KNN and RF. | quote: "we used a leave-site-out approach for our proposed CNN, SVM, KNN, and RF classiﬁers (Heinsfeld et al., 2018). In this method, each site is taken as one fold in the dataset, and we applied a cross-validation approach on the remaining sites instead of diﬀerent folds. Therefore, each time, one site out of 17 is used to test, and the other sites are used for training."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

5-fold CV within the 70% training set for hyperparameter selection, with final evaluation on a untouched 30% hold-out set; significance assessed via binomial tests (vs. chance and vs. prior state-of-the-art) and McNemar tests; an explicit site-confound check compared a site-only baseline classifier and re-evaluated on site-balanced test sets. | quote: "We found that models trained using only site information achieved an accuracy of 66.0% on the ADHD data and 55.0% on the ABIDE data, while our models trained on MRI data achieved much higher accuracies: 67.4% and 64.3%, respectively."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

5-fold stratified CV per target site; a multiple-regression site/age/gender/handedness correction applied to FC features; offline SSAE pretraining confined to the 16 non-target ABIDE sites to avoid leaking target-site data into pretraining. | quote: "the independent healthy FC data from the remaining 16 sites from the ABIDE repository were accumulated as pre- collected data to train an SSAE prototype during oﬄine learning. Then, we randomly split the data from the target site into training and testing set. The data from the training set were applied on an SSAE prototype in the prior knowledge aided training step. The hold-out testing data were then used to evaluate the trained DTL-NN model."

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

Two-sample group comparison of right pSTS seed-based iFC with mean framewise displacement included as a nuisance covariate; small-volume and whole-brain FWE-corrected statistics; a secondary motion-scrubbed analysis was run as a sensitivity check. | quote: "For the ABIDE-replication dataset (278 ASD/306 TD participants) (Supplementary Table S1), we computed iFC and mean FD scores using the same procedures as described above (Supplementary Figure S3B). Within each site, groups displayed comparable mean FD scores (except for one site). Across sites, micro-movements were greater within the ASD than in the TD group [F(1,566) ¼ 4.23, P ¼ 0.041] (Supplementary Table S1 and Figure S3B). As for the ori- ginal sample, we corrected for micro-movements by including mean FD scores as a nuisance covariate in the primary group analysis"

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

A single random 70/30 train/test split (58/26 subjects); the number of base SVMs and the feature-set dimensionality were both tuned by maximising accuracy on the same 26-subject test set, which was then reported as the final accuracy; no cross-validation or independent validation set was used. | quote: "Firstly, the 84 samples are divided into 58 training samples and 26 test samples based on the ratio of 7:3. Then 50 samples are randomly selected from the 58 training samples and 62 features are randomly selected from 4,225 features, which form a single SVM using Radial Basis Function (RBF) as kernel provided by the SVM toolbox (http://see.xidian.edu.cn/faculty/chzheng/ bishe/indexﬁles/indexl.htm) (Gunn, 1998). The width argument of RBF equals to 3, and penalty coeﬃcient equals to Inf. The process is repeated for 500 times and these 500 SVMs constitute into a random SVM cluster."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

Two complementary schemes: five-fold cross-validation (with a held-out validation split) and a leave-site-out cross-validation across the five largest sites, each held out as the test set in turn. | quote: "For the leave-site-out CV procedure, we selected ﬁve sites with the highest number of total subjects (ASD/total), namely New York University (NYU) (90/159), Kennedy Krieger Institute - 1 (KKI-I) (88/114), University of Miami - 1 (UM-I) (50/96), University of California, Los Angeles (UCLA)-I (28/69), Oregon Health & Science University (OHSU)-I (42/64)."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

10-fold cross-validation within each of five age groups; sequential (wrapper) feature selection reduced 817 features to 10; models compared via 10x10 Welch's t-tests with FDR correction; no explicit site covariate or harmonisation across the pooled multi-site sample. | quote: "We minimized the risk of overﬁtting by using three limiting approaches. First, the simplest kernel (linear) was used for the SVM. Second, only 10 features were used to learn to classify between 104 subjects. Finally, using 10-fold cross validation ensured the model is only evaluated on data points that it has not experienced before."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

10-fold cross-validation matching a prior published split; no leave-site-out or site covariate reported | quote: "We use the same 10-fold cross validation as in
[7] of the ABIDE dataset, using their publicly released code"

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

General linear model per edge with diagnosis, age, sex and mean FD covariates, Network Based Statistic with family-wise error correction (pfwe<.001); split-sample replication in LEAP vs ABIDE I/II, not leave-site-out | quote: "a general linear model was fitted to each edge, including 
diagnosis, age, sex, and mean framewise displacement (FD) as covariates"

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

Five-fold cross-validation is stated generically for the model; no ABIDE-specific leakage-control, site-handling or leave-site-out statement is given. | quote: "Five-fold 
cross-validation is used to evaluate the performance of the 
model."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

10-fold cross-validation with nested CV for hyperparameters; feature selection (top 1935 features) described prior to the CV split; a separate intra-site stratified shuffle-split CV was run to probe site effects (not leave-site-out) | quote: "we utilized 10-
fold cross-validation to measure the accuracy of predicted label. 
Any hyper-parameter operated in the method was internally set 
in the nested cross-validation."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

10-fold cross-validation; single-site design (not multi-site, so no leave-site-out); no explicit leakage-control statement for the group-ICA/dual-regression feature derivation step | quote: "A total of 10-fold cross validation strategy was used for evaluating classiﬁcation
performance."

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

Cluster similarity percentage across GA/SFS/SFR feature selection and DPC/OPTICS/hierarchical clustering combinations; explicitly no cross-validation during clustering; no site-specific/leave-site-out evaluation possible for ASD | quote: "we did not perform cross-validation during clustering."

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

Stratified 10-fold cross-validation with grid-search hyperparameter tuning on the training set; feature reduction (recursive feature elimination) described before the CV section; site used as a population-graph edge-weight feature rather than a covariate or leave-site-out split | quote: "We use a stratified 10-fold cross-validation strategy."

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

Leave-one-site-out cross-validation for inter-site evaluation, intra-site CV also reported, nested CV for hyperparameters, ROI estimation confined to training folds. | quote: "Note that the ROI were all deﬁned on the training set to avoid possible overﬁtting."

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

10-fold stratified cross-validation (not leave-site-out); RFE feature selection fit on the training set each fold. | quote: "We evaluate our model on both the ADNI and ABIDE databases using a 10-fold stratiﬁed cross validation strategy."

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

Leave-one-subject-out classifier with age, age-squared, gender, handedness and site as covariates. | quote: "Age, age-squared, gender, handedness, and site were included as covariates for the classiﬁer."

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

Random matching/non-matching pair split with subjects from all 20 sites present in both train and test sets; network hyperparameters chosen via cross-validation. | quote: "We also ensure that subjects from all 20 sites are included in both training and test sets."

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

Single random 85%/15% train/test split; separate per-site (unit-site) classification performed to assess site variability; no cross-validation or leave-site-out scheme reported for the main model. | quote: "we ﬁrst divided the whole dataset into two parts: training (85%), and testing (15%)."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

Mantel test with permutation-based significance testing on subnetwork intersubject similarity vs. ADI-R/ADOS score similarity. | quote: "only the VTL subnetwork  showed significant correlation between subnetwork intersubject similarity and joint ADI- R/ADOS score similarity (p=0.0287) with moderate effect size (r = 0.17, Figure S4)."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

Two-tailed two-sample t-tests with Bonferroni correction across 19 HMM states, reported both with and without regressing out site and FIQ; site x group interaction effects explicitly checked via a data-driven subject-matching algorithm. | quote: "two-tailed two-sample, Bonferroni correction"

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

Voxel-wise Z-scoring (|Z|>2.0 threshold) and region-wise comparisons with reported p-values; Pearson correlation (PPMC) between ROI Z-scores and ADI-R/ADOS scores; no explicit multiple-comparisons correction described. | quote: "We found that the main regions, where signal complexity significantly decreased among ASD patients, were the amygdala (p = 0.001), the vermis (p = 0.02), the basal ganglia (p = 0.01) and the hippocampus (p = 0.02)."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

Non-parametric distributional (Gamma-fit, Kolmogorov-Smirnov) comparisons across sites, age groups and medication subgroups. | quote: "Table 4 of the supplementary material reports the number of participants per class"

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

Leave-One-Out Cross-Validation with inner cross-validation for hyperparameter tuning on each training split; no leave-site-out evaluation reported despite 17 contributing sites. | quote: "Tuning is performed through an inner
cross-validation launched on each training split to select the best corresponding parameter value."

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

Single train/test split, evaluated with accuracy, recall and precision; no cross-validation, no leave-site-out, no statistical correction reported. | quote: "The samples were separated into two folders  which were the training file and test file."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

Leave-one-site-out cross-validation for classification; permutation testing with significance thresholds (p<0.01, 0.005, 0.001) for connectivity differences. | quote: "a leave-site out cross-validation scheme was performed: each training set was composed by all the sites except one, that was left out for validation."

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

Single fixed train/validation/test split (623/308/104); no cross-validation, no leave-site-out, no statistical correction reported. | quote: "the ﬁnal dataset consists of 1,035 samples distributed as follows: 623 samples for the training set, 308 samples for the validation set, and 104 samples for the test set."

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

10-fold cross-validation, pooled across sites, no site covariate or leave-site-out evaluation, no statistical correction reported. | quote: "Tests on the ABIDE I data set were carried out using the 10-fold cross-validation method."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

Leave-one-site-out inter-site cross-validation across all 17 sites; accuracy, sensitivity, specificity and F1 score reported; no stated statistical correction. | quote: "we conduct inter-site cross-validation experiments on 17 sites from ABIDE database. Speciﬁcally, one site is left as the target domain for testing, and the remaining 16 sites as multiple source domains for training."

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

Intra-site 5-fold cross-validation (pooled and site-balanced) and inter-site leave-one-site-out cross-validation; accuracy, sensitivity and specificity reported; no statistical correction stated. | quote: "For inter-site, we employed a leave- one-out-site approach that involved training the classiﬁer on all the sites except the one left out for testing."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

Pooled 10-fold cross-validation mixing all 17 sites in fixed proportion (not leave-site-out); supplementary per-site 5-fold cross-validation also reported; no statistical correction stated. | quote: "a 10-fold cross-validation schema that mixes data from all 17 sites while keeping"

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

Pooled 10-fold cross-validation across the whole dataset (no leave-site-out), with a paired t-test comparing ASD-HNet's per-fold accuracy against compared methods. | quote: "we employed the 10-fold cross-
validation strategy to conduct the comparison among dif-
ferent models."

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

Two-sample t-tests with FWE correction (FSL-randomise, 5000 permutations) for ABIDE group differences; Pearson correlation with FDR-adjusted p-values and ROC/AUC analysis in the KMUH validation cohort; no site covariate or leave-site-out scheme for the pooled ABIDE derivation step. | quote: "FC val-
ues significantly different [family-wise error (FWE)-corrected p < 0.05] between the ASD and TD groups"

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

GAM mega-analysis with ComBat site harmonisation, FDR correction, mean-FD covariate; meta-analysis across sites (inverse-variance random effects); leave-one-site-out cross-validation sensitivity analysis; LOOCV for SRS prediction with permutation testing | quote: "We performed a leave-one-site-out cross-validation to assess whether our main findings were biased by site specific sites."

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

ADOS-guided MCCAR+jICA fusion with back-reconstruction for group comparison; multiple linear regression trained on ABIDE II and cross-validated on independent ABIDE I; leave-one-site-out analysis for site-effect check | quote: "site-out analysis (details can be found in Additional file 1: “Reproducibility” section) in the ADOS-guided fALFF and GMV fusion on the whole ASD group to check whether the site effect will contribute to current ASD pattern."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

Fisher r-to-z test of ASD vs CTL correlation differences, combined by Fisher's method, Benjamini-Hochberg FDR correction; age/site/sex regressed out by linear model, site-mean correction applied | quote: "To reduce the impact of confounders, we regressed out age, site, and sex using a linear model."

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

Nested 10-fold cross-validation (training in inner loop, AUC/accuracy evaluated in outer loop); SHAP feature importance computed within the inner loop; site harmonization via NeuroHarmonize fit on the whole cohort before CV | quote: "The model was trained to distinguish subjects with ASD from TD according to a nested 10-fold cross-validation scheme."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

10-fold cross-validation on the whole dataset; separate 5-fold cross-validation per site to assess generalisability; no explicit leave-one-site-out evaluation or site harmonisation in the main model | quote: "we chose k as 10 to perform 10-fold cross validation using the whole dataset."

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

70/15/15 train/validation/test split with early stopping, plus 10-fold cross-validation for mean test accuracy; no site covariate or leave-site-out evaluation | quote: "10-fold cross validation was used and the mean test accuracy was calculated."

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

Single 8:2 train/test split; accuracy/sensitivity/specificity/AUC computed on the held-out test set; per-site average metrics also reported across the 17 sites; no leave-site-out or ComBat harmonisation | quote: "the data is categorized into a training set and a test set in a ratio of 8:2."

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

Novel statistical graph network-detection/testing algorithm applied to the full sample to identify abnormal subnetworks, then SVM (RBF/linear) with leave-one-out cross-validation used to validate classification accuracy; single site, so no site covariate/leave-site-out needed | quote: "The leave-one-out cross-validation results show that the accuracy rates are 89 and 84% correspondingly."

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

Vertex-wise two-tailed t-tests via BrainStat with random field theory correction; cluster-wise correlations FDR-corrected (q<0.05); ComBat site harmonization used instead of leave-site-out. | quote: "group differences between ASD and NT were  assessed in vertex-wise two-tailed Student’s t-tests using  the BrainStat toolbox"

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

Single random balanced split-half train/test division; accuracy compared predictions to true diagnoses; no cross-validation or leave-site-out reported for the example use-case (software supports stratified 5-fold CV for hyperparameter tuning only). | quote: "First, participants were randomly divided into balanced split-half training and testing sets."

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

Spectral dynamic causal modelling (spDCM) per subject, second-level group analysis via Parametric Empirical Bayes (PEB); single site (KKI), no cross-site or leave-site-out evaluation (single site study). | quote: "Parametric empirical Bayesian (PEB) was used to perform second-level group analysis"

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

Pairwise Pearson correlations (4005 pairs) tested with local false-discovery-rate (fdr q=0.1) and Network Based Statistics (permutation p=0.05) multiple-comparison correction; single site, no cross-validation or leave-site-out (not a predictive study). | quote: "the multiple testing correction methods including local fdr and Network Based Statistics (NBS) performed for both empirical Bayes normalized correlations and original correlations"

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

Bootstrapped resampling (100 subgroups of n=25) to standardize group sizes; Kruskal-Wallis non-parametric ANOVA for pairwise age-group comparisons (p<0.05/0.01); all ABIDE sites pooled, no leave-site-out evaluation (not a predictive study). | quote: "The comparisons of the age-groups with ASD also show shifting
statistical signatures across ages (Figure 5) and they were
significant at the 0.05 level for all comparisons in the NSR."

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

CPM edge selection (motion/site-masked), with leave-one-out cross-validation (N-1 per iteration) and split-half cross-validation; significance assessed by permutation testing (5000 shuffles) rather than parametric r-to-p conversion. | quote: "a leave-one-out cross-validation to evaluate the potential of models to predict  14  an unseen participant’s score"

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

Two-tailed two-sample t-tests with FDR correction (alpha=0.05) for brain-wide and node-level curvature comparisons across 49 graph densities (2-50%); single cohort analysis (not cross-validated/predictive, no leave-site-out). | quote: "we employed a two-tailed two-sample t test 
followed by FDR correction"

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

Wilcoxon rank-sum tests for group comparisons (FC PCA scores, motion equivalence); multilinear/elastic-net regression of FC-PCA scores on RSN entropy with 10-fold cross-validation; single ABIDE cohort pooled across sites, no leave-site-out evaluation. | quote: "The minimum MSE computed from a 10-fold cross validation
was 11.4 ± 7.2% of c1 variance, and was observed for α = 0.15."

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

5-fold stratified cross-validation reporting mean accuracy across folds; statistical significance of accuracy differences between models assessed via Monte-Carlo permutation testing (100,000 samples); no leave-site-out evaluation reported across the pooled 16-site sample. | quote: "All results are
obtained by running a 5-fold stratiﬁed cross-validation scheme where we report the mean classiﬁca-
tion accuracy over all folds."

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

k-fold cross-validation (5-, 10-, 15-fold reported); no leave-site-out evaluation across the three pooled sites. | quote: "Percentage of accuracy, sensitivity, specificity, and precision (± standard deviation) for DenseNet-
201+KNN model using k-fold cross-validation"

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

10-fold cross-validation on the combined all-17-site dataset and 5-fold cross-validation for individual site-wise comparisons; sites pooled ("ignoring the sites intrinsic variability") rather than evaluated with leave-site-out. | quote: "A comparison of our Stage feature selection-based classiﬁers with the state of the art methods is
presented in Table 11."

#### RQ5 — Main finding

**Question.** What is the direction and scope of the main finding (e.g. hypo/hyper-connectivity, which networks; accuracy/AUC with CI)?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

Not applicable — no connectivity or diagnostic-prediction finding is reported; only cohort/QC description

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

predictive — combined ABIDE-I+II: CNN 81.56% accuracy, DTL-NN 82.31% accuracy (no CI reported) | quote: "ABIDE - I+II  CNN   81.56   81.5%   80.5%   88.0%   DTL-NN    82.31%   83.3%   80.7%   87.0%"

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

Hyperconnectivity (ASD > TD) between right thalamus and right precentral gyrus (p=0.019) and right postcentral gyrus (p=0.028) in the ABIDE cohort, replicating the primary HFASD cohort's finding; other ABIDE clusters (insula, cuneus) did not match the primary cohort regions and did not correlate with clinical measures | quote: "In the ABIDE GLM analysis, clusters were found that had greater connectivity with the right thalamus in the ASD group compared to the TD group. Two of these clusters were located in the right precentral (p = 0.019) and postcentral gyri (p = 0.028), validating the observed hyperconnectivity of the same regions in our HFASD cohort."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

Main effects of diagnosis and sex across PCC-iFC, ReHo and VMHC converging on the default-network midline; sex-by-diagnosis interaction confined to VMHC in dorsolateral occipital cortex, with reduced VMHC in autistic females, replicated in EU-AIMS LEAP but not GENDAAR | quote: "Sex-by-diagnosis interactions were confined to the dorsolateral occipital cortex, with reduced VMHC in females with autism."

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

In ABIDE, prediction performance declined as diversity increased: within-distribution AUC r=-0.630 (F1 r=-0.568), out-of-distribution AUC r=-0.671 (F1 r=-0.579); opposite relationship found in the HBN cohort | quote: "we can observe a decline in performance in ABIDE as diversity increased in both within (AUC: r = −0.630, F1 score: r = −0.568) and out-of-distribution (AUC: r = −0.671, F1 score: r = −0.579) predictions."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

Hypoconnectivity: reduced cortico-cerebellar connectivity in ASD vs TD in five ROIs in ABIDE I discovery (right fusiform, right postcentral, right/left middle temporal, right superior temporal gyri), 3 of 5 (right fusiform, right superior temporal, left middle temporal) replicated in ABIDE II (p=0.047, 0.002, 0.025 respectively, FDR-corrected) | quote: "In this validation analysis, three out of ﬁve cortical ROIs, namely, the right fusiform gyrus [β = −0.028, t-value = −2.193, p = 0.047 —t-test (GLM)], the right superior temporal gyrus [β = −0.044, t-value = −3.495, p = 0.002 —t-test (GLM)], and the left middle temporal gyrus [β = −0.033, t-value = −2.583, p = 0.025—t-test (GLM)], conﬁrmed the reduced functional connectivity in the ASD group"

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

predictive — 75.20% accuracy (82.90% sensitivity, 69.70% specificity) on whole ABIDE I (N=1035); 88.71% on the proposed subset (N=645); 96.40% on the NYU subset (N=175); 4.4-percentage-point improvement over prior best on the same whole-dataset benchmark | quote: "Whole dataset 1,035 75.20 82.90 69.70 Proposed subset 645 88.71 81.82 92.50 NYU subset 175 96.40 91.00 99.50"

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Out-of-the-box classifiers achieved 57-63% accuracy (best: linear SVM at 63%), improving to 68% after per-site train-only standardization; all classifiers significantly above chance (p<0.001); a null-data simulation showed incorrect whole-dataset feature selection inflates accuracy to 91% vs. 45-56% when correctly confined to training data

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

predictive — best ABIDE hold-out accuracy 65.0% (baseline 51.6%) combining functional MRI with personal characteristic data; functional MRI alone 59.2%, structural MRI alone 60.1%, PCD alone 59.6%, structural+PCD 64.1% | quote: "Table 16. ABIDE results summary. Data Source(s) Accuracy Sensitivity Speciﬁcity Functional MRI 59.2% 72.2% 45.4% Structural MRI 60.1% 70.4% 49.1% Personal Characteristic 59.6% 60.9% 58.3% Structural MRI + Personal Characteristic 64.1% 75.7% 51.9% Functional MRI + Personal Characteristic 65.0% 71.3% 58.3%"

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

Hypoconnectivity: decreased inter- and intra-hemispheric FCD in ASD vs TDC in posterior cingulate cortex, lingual/parahippocampal gyrus, and postcentral gyrus; ADOS-RRB scores negatively correlated with FCD in these regions

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

Of the 12 aberrant cerebellar-cerebral FCs found in the original (non-ABIDE) dataset, decreased FC between right dentate nucleus and left IPL replicated significantly in the ABIDE II sample (p=0.039), with a non-significant trend for vermis VI-left MFG (p=0.071) that did not survive Bonferroni correction. | quote: "the ASD group showed signiﬁcantly decreased FC between the right dentate nucleus and left IPL (p = 0.039, Figure 4)"

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

GAT2 achieved the best classification performance among compared models: accuracy 68.02%, sensitivity 74.06%, F1 69.31%, MCC 0.3426 (HO atlas); 3 of the top 10 interpreted functional connections showed uncorrected significant group differences (p<0.05). | quote: "The GAT2 model achieved the best results in accuracy, sensitivity, F1 score, and MCC  indicators using fivefold cross-validation, with the accuracy of 68.02%, sensitivity of  74.06%, F1 score of 69.31%, and MCC of 0.3426."

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

DarkASDNet achieved accuracy 94.7%, precision 94.5%, recall 92.5%, F1-score 95%, and AUC 94.703% classifying ASD vs TC on the ABIDE-I NYU subset, reported as outperforming compared state-of-the-art methods on average. | quote: "Our model’s outcomes unveil that our proposed method established state-of-the-art accuracy of 94.70% to classify ASD vs. TC in ABIDE-I, NYU dataset."

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

3DCNN C-LSTM outperformed compared models on single sites (NYU accuracy 0.77/F1 0.78; UM accuracy 0.71/F1 0.70) but showed degraded performance on the multi-site ABIDE-I evaluation (accuracy 0.58/F1 0.53), attributed to scanner/acquisition heterogeneity. | quote: "The results show that the proposed architecture 3DCNN C-LSTM outperforms other models on single site experiments by achieving mean test accuracies and F1 scores of 0.77 and 0.78 respectively for the NYU site and 0.71 and 0.7 on the UM site."

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

MGRL outperformed single-scale GCN and handcrafted-feature baselines on both sites: NYU accuracy 0.795±0.068/AUC 0.886±0.062; UM accuracy 0.762±0.078/AUC 0.867±0.049; improvement of at least 3% over single-atlas GCNs attributed to complementary multi-scale topology information. | quote: "MGRL (Ours)
0.795 ± 0.068
0.809 ± 0.146
0.823 ± 0.103
0.802 ± 0.075
0.886 ± 0.062"

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

DeepASD achieved accuracy 87.38±2.87%/AUC 92.76±4.00% on ABIDE A and accuracy 88.09±2.92%/AUC 93.59±2.45% on ABIDE B, outperforming 8 baselines by 13.25% accuracy, 7.69% AUC-ROC and 17.10% specificity; ablation showed the fMRI modality was the single most informative, with auxiliary modalities (phenotype, QC metrics, other atlases) further improving performance. | quote: "The model achieved the following performance metrics, presented in mean ± standard deviation format, on the ABIDE A dataset: accuracy (ACC) of 87.38 ± 2.87%, area under curve (AUC) of 92.76 ± 4.00%, speciﬁcity (SEN) of 88.35 ± 6.83%, and sensitivity (SPE) of 86.51 ± 8.41%."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

EAG-RS achieved AUC 0.760±0.033, accuracy 73.71±2.83%, sensitivity 64.56±8.36%, specificity 80.74±8.28%, outperforming compared state-of-the-art and feature-selection baseline methods; selected ROIs were qualitatively linked to previously reported ASD-associated regions and subtypes. | quote: "EAG-RS 0.760±0.033 73.71±2.83 64.56±8.36 80.74±8.28"

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

Pretrained METAFormer achieved accuracy 83.7±3.0% and AUC 0.832±0.032, outperforming non-pretrained and single-atlas transformer variants as well as previously published ASD classifiers evaluated with 10-fold cross-validation on comparably sized ABIDE I samples. | quote: "METAFormer PT 0.837 ±0.030 0.819±0.045 0.901 ±0.044 0.856 ±0.023 0.832 ±0.032"

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

SWD improved the ASD-vs-control effect size by 2.9-5.3% relative to the original (uncorrected) data, while GLM and ComBat decreased it by up to 11.4%, for the literature-anchored anterior-posterior DMN hypoconnectivity finding (MPFC-PCC/precuneus, MPFC-MTG). | quote: "For the ABIDE dataset, SWD improved the effect size between autistic and control subjects by 2.9–5.3%, while GLM and ComBat decreased the effect size by up to 11.4%."

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

3D-CNN atlas-ensemble reached 73.3% CV accuracy (ABIDE-I) and 71.7% independent test accuracy (ABIDE-II), AUC 75.8%, outperforming linear/DNN baselines and a prior ABIDE-I benchmark of up to 67%; saliency maps highlighted the default mode network as discriminative. | quote: "Previous studies have reported cross- validated classiﬁcation accuracies up to 67% on ABIDE-I, the ﬁrst phase of the ABIDE study [1]. The proposed CNN approach improves this accuracy to above 73%."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

Without adaptation: 86.0% AUROC on ABIDE I, 79.2% AUROC on ABIDE II; with supervised domain adaptation: 93.2% (ABIDE-I) and 90.5% (ABIDE-II). Cerebellar connectivity identified as a reproducible discriminative feature. | quote: "The top single model trained using IMPAC attained 80.4% AUROC on IMPAC held-out test data. When tested on ABIDE I, it achieved an AUROC of 86.0% (Table 2 underlined) and when tested on the ABIDE II it achieved a performance of 79.2%."

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

Federated learning (Fed) achieved higher accuracy than the best cross-site model at every site (NYU 0.647, UM 0.728, USM 0.849, UCLA 0.712 with the HO atlas) and was significantly better than single-site training (p<0.001), approaching pooled (Mix) performance without sharing raw data; domain adaptation (Fed-MoE/Fed-Align) gave further improvement at most sites. | quote: "Single 0.601(0.064) 0.648(0.065) 0.695(0.108) 0.571(0.100) Ensemble 0.611(0.012) 0.638(0.054) 0.654(0.088) 0.634(0.064) Fed 0.647(0.049) 0.728(0.073) 0.849(0.124) 0.712(0.075) Fed-MoE 0.671(0.082) 0.728(0.083) 0.809(0.098) 0.744(0.130) Fed-Align 0.676(0.071) 0.751(0.053) 0.829(0.091) 0.712(0.089) Mix 0.671(0.035) 0.740(0.063) 0.829(0.137) 0.710(0.128) Table 3: Results of using diﬀerent training strategies"

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

CNN achieved 70.22% accuracy (10-fold CV) with the CC400 atlas, outperforming SVM/KNN/RF baselines; in the leave-site-out evaluation, KKI, SDSU and USM sites achieved accuracies above 70%, with performance varying by site. | quote: "We achieved an accuracy of 70.22 %, which is better than the rest of the reported works (Table 4)."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

Combined model (LEFMSF) achieved 0.643 hold-out accuracy on ABIDE, the best known result using imaging data alone, exceeding prior published results by 0.042; a site-only classifier achieved only 55.0% accuracy on ABIDE (near chance) and accuracy on a site-balanced test set (63.46%) was similar to the original, indicating the result is not a site-composition artifact. | quote: "achieving an accuracy of 0.673 on the ADHD-200 holdout data and 0.643 on the ABIDE holdout data. Both of these results, obtained with the same LEFMSF framework, are the best known, over all hold-out accuracies on these datasets when only using imaging data—exceeding previously-published results by 0.012 for ADHD and 0.042 for Autism."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

DTL-NN outperformed DNN and SVM at all four sites, with the best result at USM (70.4% accuracy, 0.73 AUC) and an average across sites of 67.1% accuracy/0.71 AUC, significantly better than DNN for accuracy and sensitivity. | quote: "The highest ASD classiﬁcation performance metrics were observed from the USM site−70.4% accuracy, 72.5% sensitivity, 67.0% speciﬁcity and 0.73 AUC."

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

ASD showed hypo-connectivity between pSTS and right IPL, left premotor area, fusiform gyrus and bilateral superior occipital gyrus, and hyper-connectivity between pSTS and left thalamus and right IFG, replicating the direction of the original sample's fronto-parietal hypoconnectivity finding. | quote: "Similar to findings emerging from the original dataset, we observed a significant reduction in pSTS-iFC with right IPL and left premotor area in the ASD compared with the TD group. Reduced pSTS-iFC was also observed with the fusiform gyrus and bilateral superior oc- cipital gyrus (Figure 6; Supplementary Table S3). Stronger pSTS-iFC in the ASD group was observed with left thalamus and right IFG"

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

The random SVM cluster achieved 96.15% test accuracy with an optimal 272-feature set, substantially higher than a single SVM; discriminative regions included inferior frontal gyrus, hippocampus and precuneus. | quote: "the accuracy of the random SVM cluster is as high as 96.15%. This is suﬃcient to show that the performance of the random SVM cluster is much better than a single SVM."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

5-fold CV: ~60-66% balanced accuracy across models, best for the MM-ensemble (64%/66% F1) and the ReHo single measure; leave-site-out CV: MM-ensemble dropped to 56% balanced accuracy/59% F1, with good performance only at the NYU site, showing that pooled cross-validation substantially overestimates cross-site generalisation. | quote: "When assessed by ﬁve-fold CV procedure, all tested models performed at around 60% accuracy for the classiﬁcation task (Figure 2 and Table 2), with little variation between models' performances. On the contrary, the leave-site-out CV procedure shows high variability in terms of model performances with relatively good performance for the NYU site and poor performance for the other sites"

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

Best model (>30 years age group) achieved ~95% accuracy, 97% sensitivity, 95% specificity; centrality measures (e.g., betweenness, eigenvector centrality) contributed most to classification across age groups. | quote: "Our methodology achieved better results than most state-of-the-art investigations on this dataset with the best model for the >30 years age group achieving an accuracy, sensitivity, and speciﬁcity of 95, 97, and 95%, respectively."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

Classification accuracy up to 70.86% with the proposed bootstrapped G-CNN versus 69.50% for the prior G-CNN baseline and 66.8% for linear SVM | quote: "Proposed
70.86"

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

Brain-wide hypoconnectivity (13,001 edges, 17.1%, pfwe<0.001) and hyperconnectivity (16,767 edges, 22%, pfwe<0.001) in autism; hypoconnectivity concentrated in sensory/somatomotor/attention networks, hyperconnectivity in DMN/subcortex | quote: "the NT>ASD contrast revealed 
hypoconnectivity in autism that encompassed 13,001 edges (17.1% of the total number of 
edges) linking 376 brain regions (pfwe<0.001"

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

Functional connectivity in SMN, and between DMN-DAN and DMN-FPN, identified as most important for ASD prediction; no numeric accuracy/AUC value specific to the ASD/ABIDE classification is given in the extracted text. | quote: "the
attention score in the SMN region is high, indicating that
connectivity plays a crucial role in ASD prediction in SMN."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

72.2% accuracy (sensitivity 68.6-68.8%, specificity 75.4%) classifying ASD vs TC; key finding of reduced anterior-posterior DMN correlation and social-cognition-region involvement in autism | quote: "our proposed method resulted in a mean classification ac-
curacy of 72.2% (sensitivity=68.6%, specificity=75.4%)."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

77.74% accuracy (76.74% precision, 78.57% recall, F1 75.33%) for ASD vs NC; hyperconnectivity in SN-dDMN/SN-LCEN and hypoconnectivity in PCUN-dDMN | quote: "MCSE-VGG
All
77.74
76.74
78.57
75.33"

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

For ASD, GA + hierarchical clustering gave the highest clinical-diagnosis-to-connectivity cluster similarity (89.20%, 101 features, 3 clusters), with connectivity matching clinical diagnosis better than phenotypic clusters | quote: "Hierarchical
76.63
5
3
89.20
101
3
75.66
54
3"

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

AN-GCN achieved 96.91% accuracy and 96.86% AUC on ABIDE, a 50.33% relative accuracy improvement over baseline GCN (64.63%) and above the strongest baseline DS-MML (87.62%) | quote: "AN-GCN (Ours)
96.91
96.86
97.16
96.91
97.00
93.76
93.86"

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

Best inter-site accuracy 66.8% (chance 53.7%) with MSDL + tangent embedding + l2-regularized classifier; abstract reports up to 67%. | quote: "the highest accuracy obtained on the whole dataset is 66.8% (see Table 2) which ex- ceeds previously published ABIDE ﬁndings [53, 13, 54] and chance at 53.7%"

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

Best accuracy 70.4%, AUC 0.75 using a phenotypic (sex+site) population graph with K=4. | quote: "The best average performance is achieved for K = 4 with accuracy 70.4% and AUC 0.75."

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

60% maximum whole-brain classification accuracy, best connections in default mode network, parahippocampal/fusiform gyri, insula, Wernicke area, intraparietal sulcus. | quote: "As high as 60% accuracy was obtained for whole brain classiﬁcation, with the best accuracy from connections involving regions of the default mode network, parahippocampaland fusiform gyri, insula, Wernicke Area, and intraparietal sulcus."

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

k-nn accuracy 62.9% (all sites) with the GCN distance metric vs. 51.0% with PCA/Euclidean distance, an 11.9-point improvement; larger gains for individual sites (up to 90.0% vs 50.0% for site 18). | quote: "PCA/Euclidean 51.0% 59.3% 25.0% 30.0% 64.3% 50.0% GCN 62.9% 81.5% 62.5% 70.0% 50.0% 90.0%"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

Unit-site classification accuracy up to 85% (glass-brain) and 84% (stat-map) for several sites; best deep ensemble classifier outperformed other configurations across all four pipelines. | quote: "the highest accuracy for glass brain images is up to 85% belongs to several data sites and for stat map images the accuracy is up to 84% for several data sites"

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

VTL subnetwork similarity correlates with ADI-R/ADOS symptom-severity similarity (p=0.0287, r=0.17), replicating the movie-watching sample's finding. | quote: "only the VTL subnetwork  showed significant correlation between subnetwork intersubject similarity and joint ADI- R/ADOS score similarity (p=0.0287) with moderate effect size (r = 0.17, Figure S4)."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

ASD showed decreased fractional occupancy in HMM states 4, 8, 9, 10 and increased occupancy in states 2, 3, 14, 17 versus controls. | quote: "compared to HCs, we found that fractional occupancies of HMM states 4, 8, 9, and 10 for ASD subjects were signiﬁcantly decreased"

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

Significantly decreased signal complexity (fractal dimension) in ASD in amygdala, vermis, basal ganglia and hippocampus; no regions significantly increased. | quote: "Overall, we found reduced signal complexity in the ASD subjects with respect to controls."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

Excess noise and randomness in head micro-movements in ASD vs. controls, exacerbated by comorbidity, lower IQ, and autism severity, independent of medication status. | quote: "We  find excess noise and randomness in the ASD cases, suggesting an uncertain motor-feedback signal."

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

Averaged test accuracy up to 74.8% (m=3), significantly outperforming the SFM structural-only baseline; frontal and temporal lobes identified as most predictive regions. | quote: "m SFM (%) Ours (%) p-value 2 69.1 ± 7.4 73.5 ± 6.9 0.026 3 70.4 ± 10.3 74.8 ± 9.5 0.016"

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

ResNet-50 achieved the best test accuracy of 87.0% versus VGG-16's 63.4%; no AUC or confidence interval reported. | quote: "The best CNN model in this project was  achieved by ResNet50, with an accuracy of 87.0%."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

Hyper-connectivity in ASD between right angular gyrus-precuneus (DMN) and right frontal operculum-left IFG; best leave-one-site-out classification AUC 0.75±0.05 (HO atlas), best single fold AUC 0.83. | quote: "The mean L-SVM classification performance, in terms of the area under the ROC curve (AUC), was 0.75 ± 0.05."

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

Average accuracy 0.735 (sensitivity 0.765, specificity 0.752) across three atlas-based datasets; best per-atlas accuracy 83.82% (CC atlas); no AUC or CI reported. | quote: "our developed MHOA based on the SSDAE model has accuracy 66.35%, 70.19%, and 83.82% for EZ, AAL, and CC, respectively."

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

Best model (RNN) reached 74.74% accuracy, 72.95% sensitivity, 76.28% specificity on 10-fold CV; no AUC or CI reported. | quote: "the highest performance value is provided by RNN with 74.74%."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

LRCDR achieved mean leave-one-site-out accuracy 73.1% (AAL) and 73.4% (CC200), the most discriminative connections being mostly inter-network RSFCs; no CI reported. | quote: "LRCDR obtains the mean accuracy of 73.1%, superior to the results of the compared state-of-the-art domain adaptation methods and multi-site ASD identiﬁcation methods."

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

ASD patients show increased dynamic FC variability in regions of low variability in controls; classification reached up to 65% accuracy (intra-site) and ~62% accuracy (inter-site, leave-one-site-out, MLP); no CI reported. | quote: "achieved 65%"

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

HCAN achieved ACC 82.9%, SEN 76.7%, SPE 86.6%, AUC 84.6% on pooled 10-fold CV; per-site 5-fold CV mean ACC/SEN/SPE/AUC = 75.6%/72.6%/77.3%/83.0%. | quote: "The proposed HCAN method achieves an average ACC of 82.9%, 
SEN of 76.7%, SPE of 86.6% and AUC of 84.6%."

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

ASD-HNet achieved accuracy 73.57%, sensitivity 72.63%, specificity 74.90%, F1 71.04%, the best among all compared methods (paired t-test p<0.05 for each comparison). | quote: "ASD-HNet
73.57
72.63
74.90
71.04
-"

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

DMN functional connectivity was weaker in ASD than TD; DMN-derived biomarker A4 achieved AUC 0.745 in the local cohort (vs 0.590 for its RSN-template counterpart R4, p<0.05); DMN biomarkers correlated negatively with SRS severity. | quote: "The results of this study indicate that the FC of DMN in the ASD group was 
weaker than that of the TD group."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

ASD showed higher mean (Cohen's d=.18) and lower SD (d=-.19) of whole-brain modular variability; regionally higher variability in default-mode regions (d=.19-.33) and lower in visual cortex (d=-.24 to -.19), FDR p<.05; modular variability predicted SRS scores (r=.16, pperm=.002) | quote: "the ASD group showed higher modular variability mainly in several default-mode regions, including the medial prefrontal cortex, posterior cingulate gyrus, and angular gyrus (Cohen’s d ranging from .19 to .33), and lower variability primarily in the visual cortex (Cohen’s d ranging from -.24 to -.19) (FDR corrected p < .05)"

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

Subtype-unique subcortical fALFF alterations (direction given in q8) correlated with ADOS subdomains (social interaction common to all subtypes); prediction models generalized from ABIDE II to ABIDE I only for the matching subtype | quote: "models can be generalized to predict ADOS and SRS scores for the corresponding subgroup from ABIDE I, but not for the other groups"

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

415 differentially correlated genes identified (Diff Cor P<0.01, CTL FDR<0.05), effect size >1.8 for ~3% of expressed genes, with regional emphasis on primary visual and inferior temporal cortex | quote: "415 differentially corre- lated genes (DC genes; Diff Cor P < 0.01, CTL FDR < 0.05"

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

Joint structural+functional fusion achieved AUC 0.78±0.04, exceeding structural-only (0.66±0.05) and functional-only (0.76±0.04) models; top features in Default Mode Network and Social Brain regions | quote: "The AUC values of 0.66±0.05 and of 0.76±0.04 were obtained in the ASD vs. TD discrimination when only structural or functional features are considered, respectively. The joint fusion approach led to an AUC of 0.78±0.04."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

70.8% accuracy / 79.1% specificity on the whole ABIDE-I dataset; outperformed comparators for 12/17 sites with 64.42% average per-site accuracy | quote: "ASD-SAENet exhibits comparable accuracy (70.8%), and superior speciﬁcity (79.1%) for the whole dataset as compared to other methods."

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

Augmentation gave only minor gains (best: 0.6 percentage points with early stopping, 2.2 with fixed epochs); half of augmentation strategies reduced accuracy; training accuracy >90% indicated overfitting | quote: "Compared to no augmentation, the best augmentation approach increases the test accuracy by 0.6 percentage units."

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

72.46% accuracy, 74.35% sensitivity, 79.25% specificity, AUC 0.79, outperforming CNN-MLP, DiagNet, HI-GCN and GAT | quote: "the AUC value of the proposed algorithm is 0.79, which is 5.42% higher compared to GAT."

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

Two abnormal connectivity subnetworks identified (middle temporal gyrus/precuneus; emotion/empathy-related k-partite network); SVM LOOCV accuracy 89% (RBF) / 84% (linear) | quote: "The leave-one-out cross-validation results show that the accuracy rates are 89 and 84% correspondingly."

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

Widespread CD reductions in ASD, peak effect in limbic network (Cohen's d=-0.159); positive correlation of CD to IQ, no significant correlation with age or ADOS. | quote: "peak reductions in CD in  the limbic network (Cohen’s d=-0.159, Fig.  3A)"

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

Whole-brain ReHo classifier achieved ~62% accuracy with no dimensionality reduction or feature selection. | quote: "The accuracy of our model without any dimensionality reduction or feature selection was ~ 62%."

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

ASD children showed decreased effective connectivity among VN, DMN, cerebellum, SMN and FPN vs TC; DMN(ANG_R)-to-SMN(PreCG_L) connectivity correlated negatively with ADOS stereotyped-behavior scores. | quote: "children with ASD showed decreased effective connectivity among some large- scale brain networks. These brain networks included VN, DMN, cerebellum, SMN, and FPN."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

44 connectivity features differed significantly (fdr q<0.1) between ASD and TC after empirical-Bayes normalization, all showing ASD hyper-connectivity across distant functional subsystems; no significant features found with raw correlations. | quote: "44 connectivity features have fdr q- values less than 0.1"

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

Random involuntary motor noise (NSR of head motion) is elevated in ASD vs TD across age groups, with non-uniform age-dependent shifts in ASD vs. a smooth downward trend with age in TD. | quote: "The results suggest that the levels of random involuntary
motor noise are elevated in autism across age groups."

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

FC-based CPM significantly predicted inhibition (rs=.23, permutation p=0.037) and (at trend level) shifting (rs=.19, p=0.067) but not emotion control; inhibition networks were posterior (somato-motor/visual/cerebellar), shifting networks anterior (frontoparietal/dorsal attention). | quote: "Significant models were built using negative edges for inhibition (rs=.23, p=0.0001) and shifting 
2 
(rs=.19, p=0.001), using leave-one-out prediction (N-1 at every iteration)."

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

Average edge Forman-Ricci curvature significantly lower in ASD vs TD across most graph densities (5-50%, FDR p<0.05); Ollivier-Ricci curvature showed a similar but less consistent pattern; region-specific differences concentrated in Default Mode and Somatomotor networks. | quote: "average edge FRC is significantly lower ( p < 0.05 , FDR-corrected) in the ASD group compared to the TD group 
in the graph density range 5–50%"

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

FC imbalance across 11 RSNs in ASD (p=0.002) corresponded to a weaker FC-entropy relationship (p=0.02); entropy-model fit distinguished ASD from controls (p=0.01) and correlated with ASD symptom severity (p=0.003). | quote: "Further, we observed that an estimated RSN entropy model
signiﬁcantly distinguished ASD from controls (p = 0.01) and was associated with level of
ASD symptom severity (p = 0.003)."

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

Best accuracy 69.2% (hybrid topological+correlation 3-layer NN); improvement due to topological features over correlation-only features was not always statistically significant. | quote: "However, our experiments also show that the improvement due to topological features is not always statisti-
cally signiﬁcant."

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

Best accuracy 85.9% (DenseNet201 + KNN); 10-fold CV gave 86.5 +/- 2.4% accuracy. | quote: "The best prediction results  are 85.9% accuracy achieved by extracted the features from DenseNet201 network and classified these features by  KNN classifier."

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

Maximum 10-fold accuracy of 82% on the combined 17-site dataset (LR/LD classifiers); outperformed state-of-the-art methods in 13/17 individual sites (5-fold accuracy). | quote: "On the combined site data across 17 sites, we achieved the maximum 10-fold accuracy of 82% and for the individual site-wise data, based on 5-fold accuracy, our results outperformed other state of the art methods in 13 out of the total 17 site-wise comparisons."

### Reproducibility

#### RQ6 — Cohort reconstructibility

**Question.** Can the analysed cohort be reconstructed from released files (participant list or exact rules published)?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

yes — exact rules | quote: "The current ABIDE II dataset encompasses 17 collections of unique independent datasets (i.e., from individuals whose data were not previously shared in ABIDE I) yielding 487 datasets classiﬁed as ASD and 557 as controls (Fig. 1a, Table 1)."

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

no — only aggregate N and site counts given; no participant ID list or exact per-dataset inclusion rule published | quote: "Our analysis is limited by the method utilised to   collect ABIDE data from 17 foreign clinical and research   sites. Another limitation is picture data availability. The dataset has 851 subjects, which is significant."

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

partly — N, matching criteria and FD/QC statistics are reported, but the exact ABIDE participant selection process is deferred to Supplemental Information not present in the retrieved full text | quote: "To validate our ﬁndings in a separate cohort, we iden- tiﬁed 58 ASD and 51 TD individuals from ABIDE mat- ched to the HFASD cohort by age, sex, and IQ (Table 2). The selection process is detailed in Supplemental Infor- mation."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

yes — exact rules — quantitative inclusion/exclusion thresholds (age, FIQ, mFD, site-minimum-N) are given in the main text with full detail in Supplementary Methods | quote: "Briefly, we selected cases between 7 and 18 years of age (the ages most represented across ABIDE sites), with MRI data successfully completing brain image co-registration and transformation to stand- ard space, with FIQ between 70 and 148 and with mean framewise displacement (mFD) [54] within three times the interquartile range (IQR) + the third quartile (Q3) of the sample (i.e., mFD 0.39"

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

yes — participant list — analysis code, imaging features and phenotypic data are openly released on GitHub, and figure-underlying data in supplementary S1 Data | quote: "Data Availability Statement: The imaging and phenotypic data were provided, in part, by the Autism Brain Imaging Data Exchange initiative (ABIDE-I and II; https://fcon_1000.projects.nitrc. org/indi/abide) and the Healthy Brain Network (https://fcon_1000.projects.nitrc.org/indi/cmi_ healthy_brain_network). All imaging features, phenotypic data, and code are openly available at https://github.com/OualidBenkarim/ps_diversity."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

partly — N by diagnosis/site and exact QC thresholds (5% scrubbing, FD descriptive stats) are reported, but no participant ID list or supplementary selection criteria document is referenced | quote: "After preprocessing (described in section 2.2.), the ABIDE I dataset was composed of 432 subjects with TD (348 males, mean age ± standard deviation of 18.21 ± 8.04) and 276 individuals with ASD (241 males, 18.42 ± 8.38). The ABIDE II dataset was composed of 316 subjects with TD (208 males, 12.80 ± 5.61) and 269 individuals with ASD (234 males, 13.93 ± 7.07)."

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

yes — exact rules — sample sizes, the CPAC/atlas pipeline, and the selector-based subset-construction procedure are fully described, and code/evaluations are released on GitHub

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

partly — N, site-balancing/matching procedure, and full pipeline/code are reported, but no explicit participant ID list is given | quote: "We balance the data per site, meaning that we take the same number of ASD subjects as TD subjects per site. Furthermore, we ensure that the 2 resulting classes (TD and ASD) with 77 subjects each are similar on average with respect to IQ, age, and head movements. This prevents the classifier from separating"

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

partly — N, QC exclusions, and the train/test split procedure (random, label-balanced) are reported, but the exact 889/222 participant assignment is not published as an ID list | quote: "Therefore, we divided the ABIDE dataset into training and test sets by ran- domly selecting a label-balanced 889 (4/5) of the ABIDE subjects as the training set, leaving the remaining 222 (1/5) ABIDE subjects as the testing set."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

partly — N and site/IQ-based exclusion rules are reported, but no participant ID list is published | quote: "We excluded datasets from the social brain Lab BCN NIC UMC Groningen and Netherlands Institute for Neurosciences due to the missing information of a full-scale intelligence quotient (IQ) for many subjects. After preprocessing, we found that a large part of the cerebellum was missing in the imaging dataset of Carnegie Mellon University, and all datasets from Carnegie Mellon University were excluded. To control for potential confounding eﬀects of IQ in our analysis, we decided to exclude ﬁve datasets that included some subjects with IQ lower than 70. Finally, we performed voxel-wise group comparisons with 975 imaging datasets."

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

partly — exact numeric selection rules (sex, FSIQ≥80, age range, handedness, behavioural score availability, motion >3mm, cerebellar coverage) and per-site Ns are reported, but no participant ID list is published. | quote: "we selected subjects who met following criteria: boys with FSIQ ≥80, age range: 6–16 years, right handed, with scores recorded on the SRS"

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

partly — N and diagnostic composition (505 ASD/530 HC of 1035) are stated and data/code are public, but no participant ID list or explicit inclusion/exclusion QC rule for the 1035 subset is given in text. | quote: "The datasets analyzed during the current study are available in the ABIDE Preprocessed Connectomes Project website"

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

partly — exact N and site (NYU, 79 ASD/105 TC) are given in Table 2, but no participant ID list and no explicit additional exclusion rule beyond site selection is reported. | quote: "Among the 17 sites, we endeavor with the CCS-NYU (New York University Langone Medical Center) site."

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

partly — exact per-site Ns (NYU 184, UM 110, multi-site 1100/19 sites) are given, but no participant ID list, no code repository, and no explicit QC/exclusion rule are reported. | quote: "For the multi-site experiment we used ABIDE-I with 19 sites and 1100 subjects."

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

partly — exact per-site N and diagnostic split (NYU 79 ASD/105 NC; UM in Table 1) are reported, but no participant ID list or code repository is given, only a general data-availability statement. | quote: "The original contributions presented in the
study are included
in the article/supplementary material, further inquiries can be
directed to the corresponding author/s."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

yes — exact rules — both cohorts follow fully specified, previously published selection/preprocessing protocols (Parisot 2017 for ABIDE A; Wang 2020 for ABIDE B), and the preprocessed datasets and analysis code are released with the paper. | quote: "The ABIDE dataset is available from ref. [21], and the preprocessed dataset ABIDE A and ABIDE B are provided with the paper."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

yes — exact rules — the exact exclusion rule (missing filenames/incomplete data) and resulting N by diagnosis are given, with the pipeline, atlas and analysis code (GitHub) all published. | quote: "https://github.com/ku-milab/EAG-RS"

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

partly — exact N, pipeline, atlases and analysis code (GitHub) are reported, but the paper does not explain why 406/476 (rather than the full 539/573 ASD/TC release) were used, so the exact exclusion rule is not stated. | quote: "The code for our framework is available at github.com/Lugges991/METAFormer"

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

partly — exact N by diagnosis and diagnosis source (DSM-IV-TR) are reported, and the data is from the public ABIDE release, but no participant ID list or additional site-level inclusion/exclusion rule is given beyond the N. | quote: "Autism data is publicly available from ABIDE (http://fcon_1000.projects.nitrc.org/indi/abide/)"

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

partly — ABIDE-II test cohort defined by an exact, quantitative QC rule (>=100 retained frames after FD>0.5mm scrubbing), but ABIDE-I training cohort relies on manual QA ratings by functional raters without a stated numeric rule or participant list. | quote: "Since manual QA was not yet available for ABIDE-II, we per- formed an automatic quality control by selecting those subjects that retained at least 100 frames or 4 minutes of fMRI scans after motion scrubbing [19]. Motion scrubbing was performed based on Framewise Displacement (FD), dis- carding one volume before and two volumes after the frame with FD exceeding 0.5mm [15]. This step yielded a ﬁnal ABIDE-II sample size of 163 individuals with ASD and 230 healthy controls."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

yes — exact rules — ABIDE inclusion rule (all sites, first available paired sMRI+rsfMRI scan per subject) stated exactly, with resulting Ns; demographic breakdown given in Table 3; code/pipeline publicly released. | quote: "we are pleased to provide full analysis source code, saved models, and pipeline parameters at:"

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

yes — exact rules — exact per-site inclusion numbers and the file/ROI-completeness exclusion rule are stated, and Table 1/2 give full per-site demographic and diagnostic breakdowns, though no public participant ID list or code repository is given. | quote: "NYU UM USM UCLA Total Subject 167 88 52 63 ASD Subject 73 43 33 37 HC Subject 94 45 19 26 ASD Percentage 44% 49% 63% 59% fMRI Frames 176 296 236 116 Overlapping Trunc 145 265 205 85 Table 1: Data summary of the dataset used in our study"

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

partly — ABIDE I release, site-inclusion rule (>=20 subjects, QC-passing) and the pre/post-preprocessing Ns are stated, but no participant list is published and the raw/derived data are available only on request. | quote: "DATA AVAILABILITY STATEMENT The datasets generated for this study are available on request to the corresponding author."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

yes — exact rules — exact total N, site count, class counts and the train/hold-out split rule are given, and both datasets are stated to be publicly available at their ABIDE/ADHD-200 source URLs. | quote: "Both datasets are available online publicly. The ADHD-200 dataset is available at: http://fcon_1000.projects.nitrc.org/ indi/adhd200/ The ABIDE dataset is available at: (http://fcon_1000.projects.nitrc.org/indi/abide/)."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

partly — exact per-site target and offline-pool sample sizes and demographics are tabulated (Table 2), but no participant ID list or code repository is given. | quote: "TABLE 2 | Demographic data of the healthy and autism spectrum disorder (ASD) subjects across seven data sites ordered by decreasing sample size. Site Class Target task sample size Age (years) Gender (male%) Handedness (right%)* Mean full-scale IQ* Ofﬂine learning sample size UM ASD 48 13.8 ± 2 81.30 75 107.6 ± 17.3 411 Healthy 65 15 ± 3.7 75.40 83.10 109 ± 9.5 UCLA ASD 36 13.3 ± 3 94.40 88.90 102.4 ± 12.8 437 Healthy 39 13.2 ± 1.8 84.60 92.30 106.4 ± 10.4 USM ASD 38 24.6 ± 9 100 92.10 99.7 ± 17.3 453 Healthy 23 22.3 ± 7.9 100 95.70 115.5 ± 15.6 LEUVEN ASD 27 18 ± 5 92.60 88.90 109.4 ± 13.1 442 Healthy 34 18.2 ± 5.1 85.30 85.30 114.8 ± 12.9 All ± values are mean ± SD. *Results were calculated after removing missing data. Number of IQ missing value: UM, ASD-1, Healthy-3; UCLA, ASD-0, Healthy-0; USM, ASD-0, Healthy-0; LEUVEN, ASD-13, Healthy-19"

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

partly — exact ABIDE site count, sample size and diagnostic-corroboration rule are stated, but no ABIDE participant ID list or code repository is given in this paper. | quote: "The replication dataset consisted of 584 resting-state fMRI datasets from nine sites contributing to the ‘ABIDE’ release (Di Martino et al., 2013). In this sample, all participants with ASD (278) had a clinician’s DSM-IV-TR diagnosis of ASD, which was corroborated by the Autism Diagnostic Observation Schedule (ADOS) and the Autism Diagnostic Interview-Revised (Lord et al., 1994, 1999) for all sites except one."

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

partly — exact cohort size, the motion-exclusion rule, and the scan-protocol selection criterion are given, but no ABIDE participant ID list or code repository is provided. | quote: "Only 84 of 107 subjects are utilized in experiments because the translation or rotation of 7 TC and 16 ASD patients has surpassed ±2 mm or ±2◦. Then the random SVM cluster was proposed to distinguish TC and ASD. The results show that this method has an excellent classiﬁcation performance based on all the features. Furthermore, the accuracy based on the optimal feature set could reach to 96.15%. Abnormal brain regions could also be found, such as inferior frontal gyrus (IFG) (orbital and opercula part), hippocampus, and precuneus. It is indicated that the method of random SVM cluster may apply to the auxiliary diagnosis of ASD. Keywords: random support vector machine cluster, neuroimaging, autism spectrum disorder, classiﬁcation, feature selection INTRODUCTION Autism spectrum disorder (ASD) is mainly reﬂected in the communication and language barriers, diﬃculties in social communication, and it is a kind of neurological developmental disorder (Karten and Hirsch, 2015; Khundrakpam et al., 2017). The behavioral phenotype of ASD is well-depicted but its etiology and pathogenesis is rarely known (Amaral et al., 2008). According to the results of Hallmayer et al. (2011), the causes of ASD mainly include genetic and environmental risk factors. Some of the symptoms of ASD generally appear in about 2 years old (Ecker et al., 2015), thus the early diagnosis is needed (Plitt et al., 2015). It is recognized that traditional clinical methods cannot well distinguish patients from healthy controls (HC) (Mwangi et al., 2012). And it may not be complex enough to capture the abnormal brain regions in individuals who suﬀering from ASD (Uddin et al., 2011). To avoid this disadvantage, machine learning is introduced in the neuroimaging ﬁeld. It is a valid means to extract messages from neuroimaging data and further predict the future changes of the disease (Klöppel et al., 2012; Orrù et al., 2012). Among numerous machine learning methods, support vector machines (SVM) is an excellent classiﬁcation method Bi et al. Classiﬁcation of ASD Using Random-SVM-Cluster (Zhang et al., 2015). SVM has distinct merits such as the higher classiﬁcation accuracy (Zhang and Wu, 2012) and no need for a large number of training samples to avoid over-ﬁtting (Li et al., 2010). Thus, SVM has aroused widespread concern of researchers in the ﬁeld of neuroimaging (Sundermann et al., 2014). In the researches of machine learning, SVM has been applied to classify ASD from corresponding controls. Gori et al. (2015) extracted features from the gray matter subregions, then these features were used in SVM to identity ASD from HC and the area under ROC curve (AUC) is 0.74. Jin et al. (2015) proposed an original multi-kernel SVM classiﬁcation method to classify ASD from HC and the accuracy can reach to 76%. Chen et al. (2016) used the SVM to classify 112 adolescent subjects with ASD and 128 HC, and the classiﬁcation accuracy was 79.17%. Odriozola et al. (2015) used the SVM based on functional magnetic resonance imaging (fMRI) data to classify 20 children with ASD and 20 typically developing (TD) peers, and the result showed 85% classiﬁcation accuracy. Chanel et al. (2016) used the method of SVM and Recursive Feature Elimination (RFE) based on fMRI data to classify ASD from HC, and the result showed good classiﬁcation accuracy (up to 92.3%). These SVM classiﬁcation studies on ASD have achieved relatively high classiﬁcation accuracy in the range of 70–93% compared with traditional methods. They usually employed a single SVM and common features such as functional connections, gray matter volume to classify ASD from HC, and the classiﬁcation accuracy is generally lower than 90%. In this paper, a novel method of random SVM cluster is proposed and several graph metrics of brain functional connectivity (e.g., local eﬃciency, shortest path) are employed to classify ASD and typical controls (TC). This method has some good performance. Firstly, the classiﬁcation accuracy reaches to a higher level based on all the features. Then, we could ﬁnd out the optimal feature set, the classiﬁcation accuracy could also reach to the same level based on the optimal feature set. Thirdly, on the basis of the optimal feature set, we could ﬁnd out the abnormal brain regions such as inferior frontal gyrus (IFG) (orbital and opercula part), hippocampus, and precuneus. Thus, the random SVM cluster may apply to the auxiliary diagnosis of ASD. MATERIALS AND METHODS Demographic Information The Autism Brain Imaging Data Exchange (ABIDE) database (http://fcon_1000.projects.nitrc.org/indi/abide/) (Di Martino et al., 2014) contains a variety of neuroimaging data. And the resting-state fMRI data include 539 ASD and 573 age-matched TC. There are 12 kinds of image protocols. This study chooses one of the image protocols, details as follows. MRI scanner = 3.0- T Siemens, TR = 3,000 ms, TE = 28 ms, data matrix = 64∗64, Pixel Spacing X = 3.0 mm, Pixel Spacing Y = 3.0 mm, Flip Angle = 90◦, Slice Thickness = 0.0 mm, no slice gap, axial slices = 34, time points = 120. Finally, 61 subjects with ASD and 46 TC met the image protocol. The original studies included in ABIDE received approval from each site’s Institutional Review Board (IRB). All images were obtained with informed consent according to procedures established by human subject research boards. Only 84 of 107 subjects are utilized in experiments because the translation or the rotation of 7 TC and 16 ASD patients has surpassed ± 2 mm or ± 2◦."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

yes — exact rules — the exact inclusion rule (minimum 100 time points) and resulting N (2,085, 993 ASD) are given, and all analysis code is released on GitHub, though no explicit participant ID list is published. | quote: "The code used of all the experiments performed is available on GitHub1."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

partly — exact per-site, per-age-group total Ns are tabulated and the exclusion rule is stated, but the ASD/HC split is only in a supplementary table not in the extracted text, and raw data are available only on request rather than openly deposited. | quote: "The raw data supporting the conclusions of this manuscript will be made available by the authors, without undue reservation, to any qualiﬁed researcher."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

no | quote: "this resulted in a dataset with
872 of the initial 1112 patients available, from 20 different
sites."

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

partly | quote: "Details about our 
exclusion 
criteria are provided in Supplement Section 2."

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

no | quote: "And the largest dataset for autism research comes
from Autism Brain Imaging Data Exchange (ABIDE) [11]."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

no | quote: "We successfully downloaded a dataset 
of 1102 subjects from the Preprocessed Connectomes Project, 
and then excluded subjects whose imaging data shows some miss-
ing."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

no | quote: "The original contributions presented in the study are included
in the article/supplementary material, further inquiries can be
directed to the corresponding author/s."

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

no | quote: "The details of data acquisition and preprocessing
are described in Supplementary Material: Data Acquisition and
Preprocessing."

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

no | quote: "We select a set of 871 subjects,
consisting of 403 ASD patients and 468 healthy controls
(HCs)."

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

partly — per-site/per-subsample participant counts given (Table A2) but no explicit released participant-ID list in the text. | quote: "Table A2: Count of subjects per site and per subsamples."

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

partly — exact cohort rule stated as reuse of Abraham et al. 2017's published 871-subject subset, but no independent participant-ID list given here. | quote: "We select the same set of 871 subjects used by Abraham et al. (2017) that met the imaging quality and phenotypic information criteria"

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

partly — exact inclusion rules stated (preprocessing success criteria, >=20 subjects per site) and demographic/N-by-site table given, but no explicit participant-ID list. | quote: "Inclusion criteria for sites were a total of at least 20 subjects meeting all other inclusion crite- ria."

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

partly — cohort is the published 871-subject ABIDE subset (403/468) with source code released, but no independent participant-ID list in this paper. | quote: "source code available at https://github.com/sk1712/gcn_metric_learning"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

no — overall N by diagnosis and site count reported, but no participant-ID list or code repository found in text. | quote: "We incorporated data from 529 ASD individuals and 573 typical controls (TC) for each pipeline, which is comprised of 17 different imaging sites."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

yes — participant list (explicit 27 ABIDE subject IDs given in supplementary methods). | quote: "This yielded 27 subjects with IDs: 51457, 51464, 51468,  51474, 50642, 50643, 50645, 50646, 50647, 50649, 50651, 50652, 50653, 50655, 50002,  50003, 50004, 50006, 50007, 50012, 50016, 50019, 50022, 50024, 50025, 50053, 50056."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

partly — exact inclusion thresholds (FIQ and mean FD within 2 SD of mean) and resulting N by site/diagnosis reported, but no participant-ID list given. | quote: "Only subjects with FIQ within 2 SD + mean across all the Autism Brain Imaging Data Exchange (ABIDE) samples and with mean framewise displacement (FD) below 2 SD + mean were included."

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

no — N and demographics reported but no participant-ID list or code repository found; data sourced from the general public ABIDE repository. | quote: "We downloaded data from the publicly accessible ABIDE-1 database: http://fcon_1000.projects.nitrc.org/indi/abide/ abide_I"

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

partly — exact site-level inclusion rules and per-site N by diagnosis reported, but no participant-ID list. | quote: "Seven of 16 ABIDE sites met these overall inclusion criteria: University of Michigan, Sample 1  and Sample 2 (“UM_1” and “UM_2”, respectively), University of Utah School of Medicine (“USM”), New York  University Langone Medical Center (“NYU”), University of California, Los Angeles, Sample 1 (“UCLA_1”), Olin,  Institute of Living at Hartford Hospital (“OLIN”), and University of Pittsburgh School of Medicine (“PITT”)."

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

partly — exact inclusion rules (eyes-open, age, mean FD threshold) and resulting N by diagnosis reported, but no participant-ID list given. | quote: "we consider patients who meet
the following inclusion criteria:
• eyes opened during fMRI acquisition;
• less than 18 years old;
• less than 0.2 mm in mean framewise displacement."

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

no — only aggregate ABIDE I/II sample counts are given; no participant list or exact inclusion/exclusion rule is published. | quote: "ABIDE I dataset consists of 1112  total samples including 539 patients and 573 typical  controls (TC) subjects."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

partly — exact numeric selection rules (age, sex, eye status, site) are given but no participant-ID list, and the data-availability statement only links to the general ABIDE repository. | quote: "Publicly available datasets were analyzed in this study. This data can be found here: http://fcon_1000.projects.nitrc.org/indi/abide/"

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

no — only aggregate N and split sizes are given; data-availability statement links to a general dataset reference, not a study-specific participant list or code. | quote: "Publicly available datasets were analyzed in this study. This data can be found here:"

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

no — reuses a commonly-cited ABIDE I subset (871 subjects) referenced to prior papers, with no participant-ID list or exact exclusion rule of its own. | quote: "we used the same 871 samples from the ABIDE 1 data set [23], [24], [25]."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

partly — the exact preprocessing variant (filter_noglobal) and the no-screening rule are stated, but no participant-ID list or ASD/TD breakdown is given. | quote: "We conduct experiments on all ABIDE I data (without any data screening), and obtain the mean 73.1%/73.4% accu-
racy on AAL/CC200 atlas"

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

no — only aggregate N and site names are given; no participant-ID list or code repository. | quote: "This resulted in a dataset of 147 subjects with ASD and 146 healthy controls."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

no — reuses a commonly-cited 871-subject ABIDE I subset with only a general qualitative selection criterion; data-availability statement links only to the general ABIDE resource, no participant-ID list or code. | quote: "The datasets analysed during the current study are available from a world-wide multi-site database Autism Brain Imaging 
Data Exchange (ABIDE I)"

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

partly — N by diagnosis and the source release (ABIDE-I, 17 sites) are given and code is public, but no participant-ID list or exact numeric exclusion rule for the 848-subject subset is published. | quote: "The code is available
at https://github.com/LYQbyte/ASD-HNet."

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

partly — the ABIDE-level N and sites are reported and the 30 biomarker masks/pipeline are public, but the underlying datasets (including the local cohort) are available only on reasonable request, not as an open participant list. | quote: "The datasets generated during and/or analyzed during the current study are available from the corresponding 
author on reasonable request."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

partly — exact numeric QC thresholds and counts by site/diagnosis are given, but no participant list or code repository is provided | quote: "Thus, after all selection criteria had been applied, we obtained a dataset consisting of scans from 939 participants (ASD/HC, 440/499) taken from 18 different sites"

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

partly — exact numeric inclusion rules (age<35, male only, DSM-IV-TR diagnosis, FD/motion thresholds) given and analysis code released, but no explicit participant list published | quote: "The multimodal MRI data used in this study can be accessed upon application from ABIDE consortium."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

yes — exact rules — explicit numeric QC thresholds given, though no individual participant list published (ABIDE access via NITRC registration) | quote: "scans meeting at least one of these three requirements were removed: (1) mean FWD > 0.30 mm, (2) greater than 50% of frames being scrubbed, or (3) scans with outlier mean, 1st, 2nd, or 3rd quantile DVARS values."

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

yes — participant list — participant IDs of the final analysed sample are published in supplementary material | quote: "To allow the reproducibility of the analysis, the identification numbers (IDs) of the participants selected in the final sample are reported in Additional file 1."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

no — cohort size and site breakdown are given but no participant list or exact per-subject exclusion rules are published beyond use of the PCP-preprocessed release | quote: "This dataset consists 1,035 rs-fMRI data with 505 ASD subject, and 530 healthy control subjects that are collected from 17 diﬀerent sites."

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

no — cohort size (539/573) is given but no participant ID list or exact numeric exclusion rule is published in this paper beyond relying on the ABIDE-preprocessed release | quote: "The 539 subjects with ASD and the 573 controls were split 70/15/15 into training, validation and test sets."

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

partly — initial release size and final QC'd N by diagnosis given, but exclusion rule is qualitative (no numeric motion threshold) and no participant list published | quote: "A ﬁnal dataset of 871 subjects, including 403 ASD patients and 468 TCs, was obtained by removing the samples with incomplete brain coverage, high motion peaks, ghosting and other scanner artifacts."

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

yes — exact rules — single-site cohort with explicit numeric TC inclusion/exclusion criteria from the ABIDE project are given, though no individual participant list is published in this paper | quote: "TCs were excluded for those who received a score of 10 or higher on the Social Communication Questionnaire 14 or a score of 6 or higher on the Obsessive/Compulsive subscale of the Spence Children’s Anxiety Scale (SCAS) 16."

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

no — exact cohort-definition rules (sites, motion thresholds, ADOS/male-only criteria) are given but no participant ID list or code repository is provided. | quote: "No datasets were generated or analysed during the current study."

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

partly — uses the full public ABIDE I Preprocessed release (no custom subsetting) but no participant list or code repository link is given in the text. | quote: "The ABIDE dataset contains 539 individuals with ASD and 573 control subjects."

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

partly — exact exclusion/QC rules given qualitatively (poor normalization, excessive motion, non-convergence) but no quantitative motion threshold or participant ID list is provided. | quote: "Some children were excluded from analysis after preprocessing due to poor normalization and excessive head motion."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

no — reuses public ABIDE data with only a qualitative motion-exclusion description; no participant list or code repository link is given.

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

yes — participant list: participant indices for the analysed cohort were uploaded to ABIDE and analysis code shared on GitHub. | quote: "We have uploaded to ABIDE the indexes of the participants included in the current study."

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

partly — exact inclusion/exclusion rules and motion threshold are given in detail, but no specific participant ID list or study-specific code repository is provided (CPM toolbox is a general public resource).

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

yes — exact rules: explicit site/QC/exclusion criteria given, and the derived FC matrices, networks and all code are publicly released on GitHub. | quote: "Functional connectivity matrices and networks generated in our study, and all original codes are deposited  on GitHub and are publically available at https://​github.​com/​asama​llab/​Curva​ture-​FCN-​ASD as of the date of  publication."

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

partly — explicit inclusion/exclusion and motion-scrubbing rules are given, but no participant ID list or code repository link is found in the text.

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

partly — uses the fully public PCP ABIDE CC200/CC400 release with a stated filtering step, but no participant ID list or study-specific code repository link is given.

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

no — site and subject counts are given but no participant ID list or code repository link is provided.

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

partly — per-site N by diagnosis given (Table 1) and a stated missing-information exclusion rule, but no participant ID list or code repository link is found in the text.

### Other charted questions

#### CL1 Cohort definition reported (inclusion/exclusion rules and…

**Question.** CL1 Cohort definition reported (inclusion/exclusion rules and resulting N by diagnosis)?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

Yes | quote: "The current ABIDE II dataset encompasses 17 collections of unique independent datasets (i.e., from individuals whose data were not previously shared in ABIDE I) yielding 487 datasets classiﬁed as ASD and 557 as controls (Fig. 1a, Table 1)."

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

Partly — Ns by diagnosis and site are given but with internally inconsistent totals, and exclusion rules are limited to removing missing/broken images | quote: "The ABIDE-I dataset is   composed of 1112 resting-state functional magnetic resonance   imaging (rs-fMRI) datasets. Among these, 573 datasets belong   to typically developing persons, while 539 datasets belong   to individuals with autism."

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

Partly | quote: "To validate our ﬁndings in a separate cohort, we iden- tiﬁed 58 ASD and 51 TD individuals from ABIDE mat- ched to the HFASD cohort by age, sex, and IQ (Table 2). The selection process is detailed in Supplemental Infor- mation."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

Yes | quote: "The final ABIDE I and II dataset of N = 1019 included N = 82 females with autism, N = 362 males with autism, N = 166 neurotypical females (NT F), and N = 409 neurotypical males (NT M), aggregated across 13 sites."

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

Yes | quote: "procedures resulted in a total of 297 par- ticipants (151 ASD and 146 TD) from 4 different sites (i.e., New York University Langone Medical Center [NYU], University of Pittsburgh, School of Medicine [PITT], University of Utah, School of Medicine [USM], and Trinity Centre for Health Sciences [TCD]) in ABIDE."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

Yes | quote: "After preprocessing (described in section 2.2.), the ABIDE I dataset was composed of 432 subjects with TD (348 males, mean age ± standard deviation of 18.21 ± 8.04) and 276 individuals with ASD (241 males, 18.42 ± 8.38). The ABIDE II dataset was composed of 316 subjects with TD (208 males, 12.80 ± 5.61) and 269 individuals with ASD (234 males, 13.93 ± 7.07)."

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

Yes | quote: "We use rs-fMRI and demographic data from ABIDE I [11], the first phase of ABIDE, with 505 autistic individuals and 530 Typical Controls (TCs)."

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Yes | quote: "We balance the data per site, meaning that we take the same number of ASD subjects as TD subjects per site. Furthermore, we ensure that the 2 resulting classes (TD and ASD) with 77 subjects each are similar on average with respect to IQ, age, and head movements. This prevents the classifier from separating"

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

Yes | quote: "We had to exclude one subject whose data could not be preprocessed with our preprocessing pipeline, leaving us with a dataset of 1111 individuals, including 573 healthy controls and 538 patients with autism."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

Yes | quote: "We excluded datasets from the social brain Lab BCN NIC UMC Groningen and Netherlands Institute for Neurosciences due to the missing information of a full-scale intelligence quotient (IQ) for many subjects. After preprocessing, we found that a large part of the cerebellum was missing in the imaging dataset of Carnegie Mellon University, and all datasets from Carnegie Mellon University were excluded. To control for potential confounding eﬀects of IQ in our analysis, we decided to exclude ﬁve datasets that included some subjects with IQ lower than 70. Finally, we performed voxel-wise group comparisons with 975 imaging datasets."

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

Yes | quote: "The ﬁnal replication dataset consisted of 42 boys with ASD (mean age: 10.7 ± 1.8 years, range: 7.2–14.4 years) and 88 TD boys"

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

Partly | quote: "The dataset includes 505 individuals diagnosed as having ASD and 530  HC."

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

Partly | quote: "TABLE 2 | NYU phenotypic data information for ABIDE-I database.
Total subjects
ASD
TC
Female
Male
Age range (Years)
Average age (SD)
ADOS score (SD)
ASD
TC
184
79
105
35
149"

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

Partly | quote: "For single sites experiments, we use the NYU and UM sites from ABIDE-I. Those provide the highest number of balanced (ASD/typically developing (TD)) subjects with 184 and 110 subjects respectively."

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

Yes | quote: "the NYU site includes 184 subjects, 79 of whom were from ASD and 105 NC cases"

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

Yes | quote: "This cohort includes 419 individuals diagnosed with ASD and
530 TC subjects."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

Yes | quote: "samples with missing filenames and incomplete data are
excluded; and the remaining 880 samples across 17 international
sites are utilized, which include 418 ASD subjects and 478 TD subjects."

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

Partly | quote: "Our framework utilizes resting-state functional mag-
netic resonance imaging data from the ABIDE I dataset, comprising 406 ASD and 476 typical control (TC) subjects."

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

Yes | quote: "Resting-state fMRI data from 850 subjects in ABIDE I with an ASD DSM-IV-TR diagnosis (n = 355) and the corresponding HCs (n = 495) from the same sites were used in this study"

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

Yes — training (ABIDE-I, 379 ASD/395 TD) and test (ABIDE-II, 163 ASD/230 TD) Ns reported with their respective QC rules. | quote: "In our experiments, we used ABIDE-I subject data that passed manual qual- ity assessments (QA) by all the functional raters. This yielded a ﬁnal sample size of 774 ABIDE-I subjects, comprising 379 subjects with ASD and 395 typical con- trols."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

Partly — inclusion rule and total N given exactly (1045 ABIDE I, 761 ABIDE II) with ASD% by Table 3, but exact integer counts by diagnosis are not given, only percentages. | quote: "Participants from all sites of the ABIDE I and ABIDE II were included for external validation, provided both sMRI and rsfMRI were obtained on the same visit. The first avail- able pair of sMRI and rsfMRI scans were used per subject. 1045 subjects from ABIDE I and 761 subjects from ABIDE II met this criteria."

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

Yes — exact per-site N, ASD/HC counts and ASD percentage reported in Table 1. | quote: "NYU UM USM UCLA Total Subject 167 88 52 63 ASD Subject 73 43 33 37 HC Subject 94 45 19 26 ASD Percentage 44% 49% 63% 59% fMRI Frames 176 296 236 116 Overlapping Trunc 145 265 205 85 Table 1: Data summary of the dataset used in our study"

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

Partly — ABIDE I totals (539 ASD/573 TD) and the post-preprocessing total (871) are given, but the exact ASD/TD split of the final 871 is not stated. | quote: "There are 1,112 subjects (539 diagnosed with ASD, and 573 typical controls) in the ABIDE I dataset, reduced to 871 subjects after preprocessing."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

Yes — total ABIDE N (1111: 573 HC/538 ASD, 17 sites) and the train/hold-out split rule are given, though the exact ASD/TD counts within the 311-subject hold-out set are not individually stated. | quote: "The ABIDE dataset consists of 1111 scans, taken from 17 sites consisting of 573 healthy controls and 538 patients with autism. To evaluate each learning model, we use 800 subjects (70%) for model training and 311 subjects (30%) for hold-out testing. We use the same case/control ratio (0.5157) for both training and test set."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

Yes — per-site ASD/healthy N for all four target sites, plus the offline-learning pool sizes, are tabulated. | quote: "TABLE 2 | Demographic data of the healthy and autism spectrum disorder (ASD) subjects across seven data sites ordered by decreasing sample size. Site Class Target task sample size Age (years) Gender (male%) Handedness (right%)* Mean full-scale IQ* Ofﬂine learning sample size UM ASD 48 13.8 ± 2 81.30 75 107.6 ± 17.3 411 Healthy 65 15 ± 3.7 75.40 83.10 109 ± 9.5 UCLA ASD 36 13.3 ± 3 94.40 88.90 102.4 ± 12.8 437 Healthy 39 13.2 ± 1.8 84.60 92.30 106.4 ± 10.4 USM ASD 38 24.6 ± 9 100 92.10 99.7 ± 17.3 453 Healthy 23 22.3 ± 7.9 100 95.70 115.5 ± 15.6 LEUVEN ASD 27 18 ± 5 92.60 88.90 109.4 ± 13.1 442 Healthy 34 18.2 ± 5.1 85.30 85.30 114.8 ± 12.9 All ± values are mean ± SD. *Results were calculated after removing missing data. Number of IQ missing value: UM, ASD-1, Healthy-3; UCLA, ASD-0, Healthy-0; USM, ASD-0, Healthy-0; LEUVEN, ASD-13, Healthy-19"

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

Yes — 584 datasets (278 ASD/306 TD) from nine named ABIDE sites, with the diagnostic corroboration rule stated. | quote: "The replication dataset consisted of 584 resting-state fMRI datasets from nine sites contributing to the ‘ABIDE’ release (Di Martino et al., 2013). In this sample, all participants with ASD (278) had a clinician’s DSM-IV-TR diagnosis of ASD, which was corroborated by the Autism Diagnostic Observation Schedule (ADOS) and the Autism Diagnostic Interview-Revised (Lord et al., 1994, 1999) for all sites except one."

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

Yes — exact pre- and post-exclusion N by diagnosis (45 ASD/39 TC of an initial 61/46) are given, with the exclusion rule stated. | quote: "TABLE 1 | Basic information of ASD and TC. Variables (Mean ± SD) Autism (n = 45) TC (n = 39) P value Gender (M/F) 41/4 33/6 0.359 Age (years) 13.4 ± 2.4 12.9 ± 1.7 0.278 ASD, Autism spectrum disorder; TC, typical controls."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

Yes — exact inclusion rule (minimum 100 time points) and resulting N (2,085 total, 993 ASD) are given. | quote: "We chose to cut off the minimum scan duration to 100-time points, which led us to include 96% of the whole ABIDE I+II dataset (N=2,085, N(ASD) =993), the vast majority of which (95%) with a minimum acquisition time of 4 min."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

Partly — total N (816), site and age-group distribution, and the zero-time-series exclusion rule are given, but the ASD/HC split is only in a supplementary table not captured in the extracted full text. | quote: "Any subject that had a consistently 0 time-series was omitted from the dataset."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

Partly — resulting N (872 of 1112) and site count given, but no inclusion/exclusion rule or N by diagnosis stated | quote: "this resulted in a dataset with
872 of the initial 1112 patients available, from 20 different
sites."

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

Partly — resulting N by diagnosis and dataset given in Table 1, exact exclusion rules deferred to an unavailable supplement | quote: "Our final sample for analysis included 796 individuals with autism (141 females; age-range: 
5-58) and 1028 NT individuals"

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

No | quote: "And the largest dataset for autism research comes
from Autism Brain Imaging Data Exchange (ABIDE) [11]."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

Partly — resulting N by diagnosis given, exclusion limited to "imaging data shows some missing" with no further rule | quote: "Finally, data of 506 ASD individuals and 548 controls was 
included in our study."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

Yes | quote: "we collected raw rs-fMRI data from the whole NYU site,
consisting of 79 ASD subjects and 105 normal controls (NCs)."

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

Yes | quote: "The sample consisted of 256 HC, 166
subjects with autism, and 32 subjects with Asperger’s."

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

Partly — resulting N by diagnosis given, no explicit exclusion rule | quote: "We select a set of 871 subjects,
consisting of 403 ASD patients and 468 healthy controls
(HCs)."

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

Yes | quote: "Total 403 468 356 413 292 337 198 222 107 119 Table A2: Count of subjects per site and per subsamples."

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

Yes | quote: "comprising 403 individuals with ASD and 468 healthy controls"

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

Yes | quote: "A total of 964 subjects met all inclusion criteria (517 typically developing subjects and 447 subjects with autism from 16 sites)."

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

Yes | quote: "consisting of 403 individuals suﬀering from ASD and 468 healthy con- trols"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

Yes | quote: "We incorporated data from 529 ASD individuals and 573 typical controls (TC) for each pipeline, which is comprised of 17 different imaging sites."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

Yes | quote: "This yielded 27 subjects with IDs: 51457, 51464, 51468,  51474, 50642, 50643, 50645, 50646, 50647, 50649, 50651, 50652, 50653, 50655, 50002,  50003, 50004, 50006, 50007, 50012, 50016, 50019, 50022, 50024, 50025, 50053, 50056."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

Yes | quote: "Only subjects with FIQ within 2 SD + mean across all the Autism Brain Imaging Data Exchange (ABIDE) samples and with mean framewise displacement (FD) below 2 SD + mean were included."

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

Yes | quote: "Anatomical and functional data from fifty-five subjects with ASD (12.7 ± 2.4 y/o) and 55 age- matched (14.1 ± 3.1 y/o) healthy controls were accessed through the NITRC database and the ABIDE project."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

Yes | quote: "Datasets from a total of 605 participants were analyzed, including 304 individuals with Autism Spectrum  Disorder (ASD) and 301 typically developing controls (CT)."

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

Yes | quote: "The corresponding data subset consists of a total of 452 subjects, with respec-
tively 251 NT and 201 ASD subjects."

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

Partly — N by diagnosis given for ABIDE I and ABIDE II but no inclusion/exclusion rule stated. | quote: "ABIDE I dataset consists of 1112  total samples including 539 patients and 573 typical  controls (TC) subjects."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

Yes — stepwise selection criteria and resulting N (102 ASD/88 TD) are given. | quote: "we selected a subgroup of 190 subjects (102 with ASD and 88 TD) according to the following criteria"

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

Partly — N by diagnosis given (505/530) and a post-QC total (1,035) stated, but no explicit inclusion/exclusion criteria text. | quote: "The rs-fMRI data used in this study were sourced from the ABIDE I dataset, comprising 505 autistic individuals and 530 typical controls (TCs)."

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

Partly — N by diagnosis given (403 ASD/468 TC) but defined only by reuse of a prior subset, with no exclusion rule of its own. | quote: "Of the 871 subjects, 403 patients were ASD and 468 were TC patients."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

Partly — total N (1102) and preprocessing variant given, but ASD/TD breakdown by diagnosis is not present in the extractable text and no exclusion rule was applied. | quote: "we use all 1102 subjects (ﬁlter_noglobal) processed by the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) [22] for experiments."

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

Partly — N by diagnosis and the TR=2s site restriction are given, but no further inclusion/exclusion criteria are described. | quote: "This resulted in a dataset of 147 subjects with ASD and 146 healthy controls."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

Partly — N by diagnosis given (403/468) with a general selection basis stated, but no precise exclusion rule or threshold. | quote: "871 subjects (including 403 
ASD patients and 468 healthy controls) who meet the imaging quality and atypical 
information criteria were used."

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

Partly — N by diagnosis given (396/452 of 848) but no explicit exclusion rule for how 848 of the 1112 release subjects were chosen. | quote: "we utilized rs-fMRI data
from 848 subjects, including 396 patients with ASD and 452
health controls (HCs)."

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

Yes — ABIDE I+II N by diagnosis given (1001 ASD/1094 TD), and the local cohort has explicit inclusion criteria and resulting N (21 ASD/23 TD). | quote: "In total, 2095 
ABIDE datasets were used (ASD: 1001 and TD: 1094; 5–64 years)."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

Yes | quote: "Thus, after all selection criteria had been applied, we obtained a dataset consisting of scans from 939 participants (ASD/HC, 440/499) taken from 18 different sites"

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

Yes | quote: "Subjects with ASD (n = 229) and the corresponding TDCs (n = 126) were selected from the ABIDE II [29, 30], which is hosted by the 1000 Functional Connectome Project/International Neuroimaging Data-sharing Ini- tiative (INDI) from multiple international sites (9 sites, Additional file 1: Table S1)."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

Yes | quote: "After the removal of subjects with image artifacts, high head movement, or poor MNI152 coregistration, we analyzed the data from the remaining 710 ASD (79% male), and 606 CTL (87% male) subjects, whose age ranges from 5 to 64 years."

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

Yes | quote: "we obtained a final sample of 1383 subjects (680 ASD and 703 TD) from 35 sites."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

Partly | quote: "This dataset consists 1,035 rs-fMRI data with 505 ASD subject, and 530 healthy control subjects that are collected from 17 diﬀerent sites."

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

Partly | quote: "The 539 subjects with ASD and the 573 controls were split 70/15/15 into training, validation and test sets."

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

Partly | quote: "A ﬁnal dataset of 871 subjects, including 403 ASD patients and 468 TCs, was obtained by removing the samples with incomplete brain coverage, high motion peaks, ghosting and other scanner artifacts."

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

Yes | quote: "The publicly available data set comprises data from 48 people with ASD and 65 TCs, with no signiﬁcant diﬀerences in demographics between the two groups."

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

Yes — three sites, N by diagnosis, male-only restriction and exclusion criteria stated. | quote: "We studied 211 males from three sites of the ABIDE-I dataset comprising 103 participants with an ASD  diagnosis"

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

Partly — N by diagnosis given (539/573) but no exclusion/QC rule stated. | quote: "The ABIDE dataset contains 539 individuals with ASD and 573 control subjects."

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

Yes — IQ cutoff, medical exclusion criteria, and N before/after exclusion by group are reported. | quote: "a total of 14 children with ASD and 28 TC children were excluded, and the ﬁnal sample included 42 children with ASD and 127 TC children."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

Partly — initial and final N by group given, but diagnostic inclusion criteria for ASD/TC are not detailed. | quote: "Participants with large motions were removed from the dataset, resulting in 32 participants in the TC group and 41 in the ASD group."

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

Yes — all public ABIDE I/II sites used, with N by diagnosis and age-group breakdown given. | quote: "This study includes all sites publicly available through ABIDE I and ABIDE II. They were comprised of 1,127 TD and 1,017 ASD."

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

Yes — detailed inclusion/exclusion criteria and N by site and diagnosis given (Table 1). | quote: "Twenty-six participants had excessive head motion on their fMRI scan (>4 mm maximum absolute 
20 
displacement)."

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

Yes — detailed, multi-step exclusion criteria with resulting N (395 ASD/425 TD). | quote: "After removing subjects based on these exclusion criteria, we were left with 395 subjects in the ASD group and 
425 subjects in the TD group"

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

Yes — explicit inclusion criteria and resulting N by diagnosis given. | quote: "Resting-state fMRI (rs-fMRI) and structural imaging data of 85 individuals with ASD and 163 matched controls from multiple sites of the ABIDE data set (Di Martino et al., 2014) were included in this study for a total of N = 248 individuals."

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

Partly — N by diagnosis after filtering is given, but the specific "missing and invalid data" filter is not quantified in detail. | quote: "After ﬁltering
for missing and invalid data, it contains 1035 subjects, of which 505 are ASD
patients and 530 are TDC (typically developing control subjects)."

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

Partly — site-level N by diagnosis given (Table 1), but no explicit inclusion/exclusion criteria beyond sourcing from ABIDE. | quote: "The sample size is 82 subjects (41 ASD and 41 normal cases) collected from three different sites  of Autism Brain Imaging Data Exchange (ABIDE)."

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

Yes — starting N, exclusion rule (missing information) and final per-site/total N by diagnosis given. | quote: "The original ABIDE dataset claimed to have 1112 subjects consisting of 539 ASD and 573 Healthy controls subjects. However, after removing subjects with missing information we have a total of 1035 subjects which is"

#### CL2 Motion/QC rule reported (metric and threshold, e.g. mean FD…

**Question.** CL2 Motion/QC rule reported (metric and threshold, e.g. mean FD cut-off; rater QC)?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

Partly — QC metrics (including mean FD) are computed and released, but no exclusion threshold is applied | quote: "users regardless of data quality27. The rationale of this decision includes the lack of consensus on optimal quality criteria in regards to speciﬁc measures or their combinations and cutoffs."

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

No — only a general statement that missing/broken images were removed (938 of 1112 used); no motion metric or threshold given

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

Yes | quote: "Frames that exhibited an FD of over 0.5 mm were censored from the timeseries, as well as one before and two after the offending frame. In the HFASD cohort, group-mean number of remaining frames out of 240 was 220.96 for ASD and 222.24 for TD (two sample t-test p = 0.8954). In the ABIDE cohort, group-mean percentage of frames remaining was 96.25% for ASD and 97.16% for TD (two sample t-test p = 0.2806). Participants with <80% of their TRs retained after motion scrubbing were removed from the analysis."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

Yes — mFD within three times the IQR plus Q3 of the sample (~0.39mm), with group mFD kept low (<0.2mm) via matching | quote: "Briefly, we selected cases between 7 and 18 years of age (the ages most represented across ABIDE sites), with MRI data successfully completing brain image co-registration and transformation to stand- ard space, with FIQ between 70 and 148 and with mean framewise displacement (mFD) [54] within three times the interquartile range (IQR) + the third quartile (Q3) of the sample (i.e., mFD 0.39"

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

Partly — "head motion in rs-fMRI" quality control is stated as an inclusion criterion but no specific FD metric/threshold value is given in the main text | quote: "For ABIDE, we considered data from all acquisition sites with at least 10 participants per group and with both children and adults. After detailed quality control, only cases with accept- able T1-weighted (T1w) MRI, surface extraction, and head motion in rs-fMRI were included."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

Yes — subjects with >5% of scans removed by FD-based scrubbing were excluded; mean FD reported per dataset | quote: "Subjects that had more than 5% of the total number of scans removed by scrubbing were excluded from the analysis. Head motion across the dataset is measured by the FD, which presents a mean of 0.137 mm and standard deviation of 0.102 mm on the study dataset (ABIDE I) and a mean of 0.169 mm with standard deviation of 0.132 mm on the independent dataset (ABIDE II)."

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

Partly — preprocessing/QC is stated to reduce N from 1,112 to 1,035 (and NYU 182 to 175), consistent with prior studies, but no specific motion metric/threshold value is given in the extracted main text | quote: "Although Di Martino et al. [11] released the ABIDE I dataset with 1,112 samples, prepro- cessing and quality control reduced this number to 1,035"

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Yes — subjects with strong head-movement artifacts excluded, and movement >0.5mm scrubbing applied; groups matched on head movement | quote: "Data presented in this study underwent standard fMRI pre- processing (i.e., realignment, normalization, and smoothing) implemented in SPM12b. Data were preprocessed according to standard SPM protocols including realignment, normalization to a study specific template using DARTEL, smoothing, band- pass filtering (0.01–0.05 Hz), and scrubbing to account for head movements (63)."

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

Partly — one subject excluded for a general preprocessing failure; no specific motion-metric (e.g. FD) threshold value is given in the main text | quote: "We had to exclude one subject whose data could not be preprocessed with our preprocessing pipeline, leaving us with a dataset of 1111 individuals, including 573 healthy controls and 538 patients with autism."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

No — head motion is regressed as a nuisance signal during preprocessing, but no explicit motion-based subject-exclusion metric or threshold (e.g. FD cutoff) is reported | quote: "Datasets were preprocessed with SPM8 (http://www.ﬁl.ion.ucl. ac.uk/spm/software/spm8/). The ﬁrst step was realignment for head motion correction. Images were realigned to the ﬁrst image and a mean echo planar image (EPI) was created during this step. Subsequently, structural T1 images were coregistered to their mean EPI data. Registered EPI data of each subject were normalized to Montreal Neurological Institute (MNI) template and spatially smoothed with 8 mm of full-width at half- maximum. Then, in the temporal domain, the linearly increasing trend due to heat absorption was removed at each voxel, and the eﬀects of the head motion, white matter, cerebrospinal ﬂuid, and global signal were regressed out. Lastly, temporal band-pass ﬁltering was applied (0.01–0.08 Hz)."

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

Yes | quote: "participants with excessive maximum head motion (>3 mm) or failure of normalization were excluded"

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

No — no motion metric or threshold is stated for the 1035-subject subset

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

No — no motion metric or threshold reported; only standard CCS preprocessing steps (motion realignment) are listed in Table 3

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

No — no motion metric or threshold is stated

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

No — head motion correction is listed as a preprocessing step, but no motion metric/threshold used to exclude subjects is reported

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

Partly — automated anatomical and functional QC metrics are used as model input modalities themselves, but no explicit motion/FD exclusion threshold is stated in this paper (inherited from the cited Parisot 2017 / Wang 2020 protocols)

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

No — exclusion is based on missing filenames/incomplete data, not a motion metric or threshold

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

No — standard DPARSF motion-correction/nuisance-regression steps are listed, but no motion metric or threshold used to exclude subjects is reported

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

No — motion correction is listed as a preprocessing step, but no motion metric or exclusion threshold is reported

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

Yes — ABIDE-II used an FD>0.5mm scrubbing threshold with a minimum 100-frame retention rule; ABIDE-I used manual QA by functional raters (no numeric threshold given). | quote: "Motion scrubbing was performed based on Framewise Displacement (FD), dis- carding one volume before and two volumes after the frame with FD exceeding 0.5mm [15]."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

No — no motion/FD-based QC rule is reported for the ABIDE external-validation subset; only the paired-scan-availability criterion is used.

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

No — exclusion is based on missing filenames/incomplete ROI time series only; no motion/FD-based QC threshold is reported.

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

Partly — site inclusion required successful preprocessing with manual visual inspection of MNI normalisation, and mean framewise displacement (FD) is mentioned as a quality measure, but no numeric FD threshold is given. | quote: "The inclusion criteria for sites was having at least 20 subjects meeting other criteria for inclusion like successful preprocessing with manual visual inspection of normalization to MNI space of MPRAGE."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

No — no motion/FD-based QC threshold is reported; preprocessing includes rigid-body motion correction but no exclusion rule based on a motion metric.

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

No — no motion/FD-based numeric QC threshold is reported; motion correction is described as a preprocessing step only.

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

Yes — mean framewise displacement (FD) was computed and included as a nuisance covariate in the primary analysis, with a secondary motion-scrubbed analysis as a sensitivity check. | quote: "For the ABIDE-replication dataset (278 ASD/306 TD participants) (Supplementary Table S1), we computed iFC and mean FD scores using the same procedures as described above (Supplementary Figure S3B). Within each site, groups displayed comparable mean FD scores (except for one site). Across sites, micro-movements were greater within the ASD than in the TD group [F(1,566) ¼ 4.23, P ¼ 0.041] (Supplementary Table S1 and Figure S3B). As for the ori- ginal sample, we corrected for micro-movements by including mean FD scores as a nuisance covariate in the primary group analysis"

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

Yes — subjects with translation or rotation exceeding ±2mm or ±2 degrees were excluded. | quote: "Only 84 of 107 subjects are utilized in experiments because the translation or rotation of 7 TC and 16 ASD patients has surpassed ±2 mm or ±2◦. Then the random SVM cluster was proposed to distinguish TC and ASD. The results show that this method has an excellent classiﬁcation performance based on all the features. Furthermore, the accuracy based on the optimal feature set could reach to 96.15%. Abnormal brain regions could also be found, such as inferior frontal gyrus (IFG) (orbital and opercula part), hippocampus, and precuneus. It is indicated that the method of random SVM cluster may apply to the auxiliary diagnosis of ASD. Keywords: random support vector machine cluster, neuroimaging, autism spectrum disorder, classiﬁcation, feature selection INTRODUCTION Autism spectrum disorder (ASD) is mainly reﬂected in the communication and language barriers, diﬃculties in social communication, and it is a kind of neurological developmental disorder (Karten and Hirsch, 2015; Khundrakpam et al., 2017). The behavioral phenotype of ASD is well-depicted but its etiology and pathogenesis is rarely known (Amaral et al., 2008). According to the results of Hallmayer et al. (2011), the causes of ASD mainly include genetic and environmental risk factors. Some of the symptoms of ASD generally appear in about 2 years old (Ecker et al., 2015), thus the early diagnosis is needed (Plitt et al., 2015). It is recognized that traditional clinical methods cannot well distinguish patients from healthy controls (HC) (Mwangi et al., 2012). And it may not be complex enough to capture the abnormal brain regions in individuals who suﬀering from ASD (Uddin et al., 2011). To avoid this disadvantage, machine learning is introduced in the neuroimaging ﬁeld. It is a valid means to extract messages from neuroimaging data and further predict the future changes of the disease (Klöppel et al., 2012; Orrù et al., 2012). Among numerous machine learning methods, support vector machines (SVM) is an excellent classiﬁcation method Bi et al. Classiﬁcation of ASD Using Random-SVM-Cluster (Zhang et al., 2015). SVM has distinct merits such as the higher classiﬁcation accuracy (Zhang and Wu, 2012) and no need for a large number of training samples to avoid over-ﬁtting (Li et al., 2010). Thus, SVM has aroused widespread concern of researchers in the ﬁeld of neuroimaging (Sundermann et al., 2014). In the researches of machine learning, SVM has been applied to classify ASD from corresponding controls. Gori et al. (2015) extracted features from the gray matter subregions, then these features were used in SVM to identity ASD from HC and the area under ROC curve (AUC) is 0.74. Jin et al. (2015) proposed an original multi-kernel SVM classiﬁcation method to classify ASD from HC and the accuracy can reach to 76%. Chen et al. (2016) used the SVM to classify 112 adolescent subjects with ASD and 128 HC, and the classiﬁcation accuracy was 79.17%. Odriozola et al. (2015) used the SVM based on functional magnetic resonance imaging (fMRI) data to classify 20 children with ASD and 20 typically developing (TD) peers, and the result showed 85% classiﬁcation accuracy. Chanel et al. (2016) used the method of SVM and Recursive Feature Elimination (RFE) based on fMRI data to classify ASD from HC, and the result showed good classiﬁcation accuracy (up to 92.3%). These SVM classiﬁcation studies on ASD have achieved relatively high classiﬁcation accuracy in the range of 70–93% compared with traditional methods. They usually employed a single SVM and common features such as functional connections, gray matter volume to classify ASD from HC, and the classiﬁcation accuracy is generally lower than 90%. In this paper, a novel method of random SVM cluster is proposed and several graph metrics of brain functional connectivity (e.g., local eﬃciency, shortest path) are employed to classify ASD and typical controls (TC). This method has some good performance. Firstly, the classiﬁcation accuracy reaches to a higher level based on all the features. Then, we could ﬁnd out the optimal feature set, the classiﬁcation accuracy could also reach to the same level based on the optimal feature set. Thirdly, on the basis of the optimal feature set, we could ﬁnd out the abnormal brain regions such as inferior frontal gyrus (IFG) (orbital and opercula part), hippocampus, and precuneus. Thus, the random SVM cluster may apply to the auxiliary diagnosis of ASD. MATERIALS AND METHODS Demographic Information The Autism Brain Imaging Data Exchange (ABIDE) database (http://fcon_1000.projects.nitrc.org/indi/abide/) (Di Martino et al., 2014) contains a variety of neuroimaging data. And the resting-state fMRI data include 539 ASD and 573 age-matched TC. There are 12 kinds of image protocols. This study chooses one of the image protocols, details as follows. MRI scanner = 3.0- T Siemens, TR = 3,000 ms, TE = 28 ms, data matrix = 64∗64, Pixel Spacing X = 3.0 mm, Pixel Spacing Y = 3.0 mm, Flip Angle = 90◦, Slice Thickness = 0.0 mm, no slice gap, axial slices = 34, time points = 120. Finally, 61 subjects with ASD and 46 TC met the image protocol. The original studies included in ABIDE received approval from each site’s Institutional Review Board (IRB). All images were obtained with informed consent according to procedures established by human subject research boards. Only 84 of 107 subjects are utilized in experiments because the translation or the rotation of 7 TC and 16 ASD patients has surpassed ± 2 mm or ± 2◦."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

Partly — a minimum scan-duration/time-point cutoff is used as the quality rule, but no motion/framewise-displacement threshold is reported.

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

No — no numeric motion/FD threshold is reported; only a consistently-zero-time-series exclusion rule and standard 24-parameter motion regression are described.

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

No | quote: "The pre-
processing includes slice-timing correction, motion correc-
tion, and intensity normalization, depending on the pipeline
used."

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

Partly — mean FD reported and used as covariate/table variable, but no exclusion threshold stated in body text | quote: "Head motion 
meanFD (mean 
± SD) 
0.079 
±0.037"

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

No | quote: "And the largest dataset for autism research comes
from Autism Brain Imaging Data Exchange (ABIDE) [11]."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

Partly — mean FD reported and compared between groups, but no exclusion threshold stated | quote: "There was no difference in the age, sex and FD between 
cases and controls (p>0.05)."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

No | quote: "realignment to correct for motion, and bandpass
ﬁltering (0.01–0.1 Hz)."

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

No | quote: "The details of data acquisition and preprocessing
are described in Supplementary Material: Data Acquisition and
Preprocessing."

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

No | quote: "which includes skull
stripping, slice timing correction, motion correction, global
mean intensity normalization, nuisance signal regression, band-
pass filtering (0.01-0.1Hz)"

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

Partly | quote: "Data were selected based on the results of quality visual in- spection by three human experts"

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

No | quote: "we use the same preprocessing pipeline, the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) (Craddock et al., 2013)"

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

Yes | quote: "Motion scrubbing (Power et al., 2012) of framewise dis- placement and DVARS with removal of volumes before and after a root-mean-square displace"

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

No | quote: "that met the imaging quality and phenotypic information criteria"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

No | quote: "Ta- ble I arranges for a summary of the distinct preprocessing steps and how they vary across pipelines."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

Yes | quote: "We applied scrubbing so that we kept 125 volumes with lowest framewise displacem"

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

Yes | quote: "Only subjects with FIQ within 2 SD + mean across all the Autism Brain Imaging Data Exchange (ABIDE) samples and with mean framewise displacement (FD) below 2 SD + mean were included."

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

Partly | quote: "The rs-BOLD data were corrected for motion artifacts using a time series general affine registration for 12 parameters (3dWarpDrive/AFNI)."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

Yes | quote: "In the current study, ABIDE sites were included that (i) deposited raw  resting-state functional Magnetic Resonance Imaging (MRI) scans (i.e., no motion correction or “scru"

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

Yes | quote: "less than 0.2 mm in mean framewise displacement."

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

No — no motion metric, threshold or QC rating is mentioned anywhere in the methods. | quote: "The age range for both  datasets is between 5-64years."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

Partly — motion correction is named as a CPAC preprocessing step but no specific motion metric or threshold for subject exclusion is given. | quote: "using the Configurable Pipeline for the Analysis of Connectomes (CPAC) (31), that includes slice- timing, motion correction, intensity normalization, nuisance signal removal"

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

Partly — motion correction and "quality control" are mentioned but no specific metric or threshold is given. | quote: "After preprocessing and quality control, the ﬁnal dataset consists of 1,035 samples distributed as follows"

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

No — no motion metric or QC threshold is reported. | quote: "Tests on the ABIDE I data set were carried out using the 10-fold cross-validation method."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

No — explicitly no data screening/QC exclusion was applied. | quote: "We conduct experiments on all ABIDE I data (without any data screening)"

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

No — no motion metric or QC threshold is reported beyond the repetition-time restriction. | quote: "We limited ourselves to acquisitions with repetition time of 2s (sites NYU, SDSU, UM, USM)."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

No — "imaging quality" is mentioned generically with no specific motion metric or threshold. | quote: "who meet the imaging quality and atypical 
information criteria were used."

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

Partly — head-movement correction is a named DPARSF preprocessing step, but no specific motion metric or subject-exclusion threshold is given. | quote: "(3) Correcting head movement."

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

Partly — 24 motion parameters are regressed out, but no subject-exclusion motion threshold (e.g. mean FD cut-off) is reported. | quote: "regressing out 24 motion parameters obtained 
after the realignment procedure16"

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

Yes | quote: "had maximal head motion of less than 5 mm and 5 degrees, and mean framewise displacement (FD) (1) of less than 0.5 mm"

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

Yes | quote: "we removed outlier datasets with mean FD exceeding 1 mm, as well as head motion exceeding 2.0 mm of maximal translation (in any direction of x, y or z) or 1.0° of maximal rotation through- out the course of scanning."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

Yes | quote: "scans meeting at least one of these three requirements were removed: (1) mean FWD > 0.30 mm, (2) greater than 50% of frames being scrubbed, or (3) scans with outlier mean, 1st, 2nd, or 3rd quantile DVARS values."

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

No

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

No

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

No

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

Partly | quote: "A ﬁnal dataset of 871 subjects, including 403 ASD patients and 468 TCs, was obtained by removing the samples with incomplete brain coverage, high motion peaks, ghosting and other scanner artifacts."

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

No

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

Yes — two explicit FD-based exclusion thresholds given. | quote: "Subjects with a mean framewise displacement  (FD) > 0.3 mm in rs-fMRI (two SD from the mean across  all subjects) were excluded (n = 9)."

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

No — no motion/QC metric or threshold is reported in the text.

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

Partly — motion-based exclusion is mentioned qualitatively ("excessive head motion") without a quantitative FD threshold. | quote: "Some children were excluded from analysis after preprocessing due to poor normalization and excessive head motion."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

Partly — motion exclusion stated qualitatively ("large motions") with no quantitative threshold given.

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

No — motion itself is the outcome variable of interest; no separate motion-based exclusion/QC threshold is applied to the fMRI data.

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

Yes — explicit quantitative threshold (>4mm maximum absolute displacement). | quote: "Twenty-six participants had excessive head motion on their fMRI scan (>4 mm maximum absolute 
20 
displacement)."

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

Yes — PCP rater quality-fail exclusion and QC-FC association/distance-dependence checks described, plus motion covariates in denoising. | quote: "We additionally excluded subjects that showed a noticeable correlation between quality  control (QC) variables and FC values, or if the QC-FC correlations showed a noticeable distance ­dependence"

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

Yes — explicit FD scrubbing threshold (0.3mm) and a >10% flagged-frames exclusion rule, plus a reported FD inclusion criterion. | quote: "Frames with excessive motion were identiﬁed and scrubbed  (Power et al., 2012) if the framewise displacement exceeded  0.3 mm. Individuals with >10% of their frames ﬂagged for  scrubbing were excluded."

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

No — no explicit motion/FD threshold is reported in this paper (relies on the upstream CC200/CC400 PCP release).

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

No — motion realignment is performed as a preprocessing step but no quantitative FD/QC exclusion threshold is reported.

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

No — no explicit motion/FD threshold given beyond relying on the upstream C-PAC-preprocessed ABIDE release.

#### CL3 Preprocessing pipeline and version reported

**Question.** CL3 Preprocessing pipeline and version reported?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

No — raw/minimally processed data release; no connectivity preprocessing pipeline is applied in this paper

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

No

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

Yes | quote: "Func- tional data from both the HFASD and ABIDE cohorts were preprocessed identically using fMRIPrep v1.3.152, a pipeline that uses a combination of tools from existing neuroimaging software packages."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

Yes | quote: "R-fMRI image pre-processing steps included: slice time correction, 24 motion param- eters regression [57], component-based noise reduction (CompCor) [58], removal of linear and quadratic trends, and band-pass filtering (0.01–0.1 Hz, for all metrics but fALFF)."

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

Yes — C-PAC (Preprocessed Connectomes Project) | quote: "For the resting-state functional brain scans in ABIDE, we built on data previously made available by the Preprocessed Connectomes initiative (http://preprocessed-connectomes- project.org/abide). The preprocessing was performed with C-PAC (https://fcp-indi.github.io) and included slice time correction, head motion correction, skull stripping, and intensity nor- malization. The rs-fMRI data were detrended and adjusted for common nuisance effects related to head motion, white matter, and cerebrospinal fluid signals using CompCor [58], fol- lowed by band-pass filtering (0.01 to 0.1 Hz)."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

Yes — Athena pipeline | quote: "We preprocessed the imaging data using the Athena pipeline (www.nitrc.org/plugins/mwiki/index.php/neurobureau:Athena Pipeline). The pipeline focused on providing systematic processing of fMRI data, including the following main steps: exclusion of the ﬁrst four scans; slice timing correction;"

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

Yes — CPAC pipeline (Preprocessed Connectomes Project) | quote: "We, therefore, leverage the CPAC pipeline, hereinafter referred to as the ABIDE I CPAC data."

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Yes — SPM12/DARTEL pipeline fully described | quote: "Data presented in this study underwent standard fMRI pre- processing (i.e., realignment, normalization, and smoothing) implemented in SPM12b. Data were preprocessed according to standard SPM protocols including realignment, normalization to a study specific template using DARTEL, smoothing, band- pass filtering (0.01–0.05 Hz), and scrubbing to account for head movements (63)."

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

Yes — SPM8 plus in-house MATLAB pipeline | quote: "For preprocessing, we used SPM8, a software package designed for analyzing brain imaging data and also for preprocessing fMRI data [27, 28] and our own in-house MATLAB code."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

Yes — SPM8-based custom pipeline | quote: "Datasets were preprocessed with SPM8 (http://www.ﬁl.ion.ucl. ac.uk/spm/software/spm8/). The ﬁrst step was realignment for head motion correction. Images were realigned to the ﬁrst image and a mean echo planar image (EPI) was created during this step. Subsequently, structural T1 images were coregistered to their mean EPI data. Registered EPI data of each subject were normalized to Montreal Neurological Institute (MNI) template and spatially smoothed with 8 mm of full-width at half- maximum. Then, in the temporal domain, the linearly increasing trend due to heat absorption was removed at each voxel, and the eﬀects of the head motion, white matter, cerebrospinal ﬂuid, and global signal were regressed out. Lastly, temporal band-pass ﬁltering was applied (0.01–0.08 Hz)."

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

Yes | quote: "All analyses were performed using the CONN toolbox2 and the Statistical Parametric Mapping 12 software."

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

Yes | quote: "The data were preprocessed by the Configurable Pipeline for the Analysis of Con- nectomes (CPAC) pipeline [24]"

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

Yes | quote: "In our experiments, we used ABIDE-I data processed through the Connectome Computation System (CCS) (Craddock et al., 2013)."

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

Yes | quote: "We preprocessed the data with the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) and the fMRI volumes are downsampled to 4 mm in MNI."

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

Yes | quote: "the remaining volumes are processed by a well- accepted pipeline with the Data Processing Assistant for Resting- State fMRI toolbox (DPARSF) (Yan et al., 2016)."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

Yes | quote: "For a fair comparison, all data are preprocessed using the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) based on the preprocessed fMRI datasets [22]."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

Yes | quote: "from 17 international sites2. The ROIs fMRI series of all sites are downloaded from the pre-processed ABIDE dataset with a configurable pipeline for the analysis of connectomes (CPAC), band-pass filter- ing (0.01 −0.1Hz), and no global signal regression"

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

Yes | quote: "In this work we use the preprocessed data from the DPARSF pipeline [31] comprising 406 ASD and 476 TC subjects."

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

Yes | quote: "The resting-state fMRI data was preprocessed using the
Connectome Computation System pipeline (Zuo et al., 2013)."

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

Yes — CPAC via the Preprocessed Connectomes Project, version v1.0.2a for ABIDE-II. | quote: "We preprocessed the ABIDE-II dataset following the same se- quence of steps listed for ABIDE-I in CPAC (v1.0.2a)."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

Yes — the open-source fconn1000 pipeline is named with a link to the exact code version used. | quote: "The IMPAC fMRI and sMRI were processed using the fconn1000 ­pipeline41. For the fMRI connectivity features, the TSE connectivity metric was fit on either the training data alone (IMPAC models) or the entire IMPAC dataset (ABIDE 1 and 2 datasets), and the TSE values per-ROI timeseries for the ABIDE dataset were calculated."

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

Partly — CPAC is named with band-pass filter and GSR settings, but no pipeline version number is given. | quote: "we downloaded Re- gions of Interests (ROIs) fMRI series of the top four largest sites (UM1, NYU, USM, UCLA1) from the preprocessed ABIDE dataset with Conﬁgurable Pipeline for the Analysis of Connec- tomes (CPAC), band-pass ﬁltering (0.01 - 0.1 Hz), no global signal regression, parcellated by Harvard-Oxford (HO) atlas."

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

Partly — CPAC via the Preprocessed Connectomes Project is named with preprocessing steps, but no pipeline version number is given. | quote: "The Preprocessed Connectomes Project (PCP) is a publicly available preprocessed version of data from both the 1,000 Functional Connectomes Project (FCP) and the International Neuroimaging Data-Sharing Initiative (INDI)3. We used data from the FCP using the conﬁgurable pipeline, the Analysis of Connectomes (CPAC)."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

Partly — SPM8 and in-house MATLAB code are named (by reference to a prior paper's identical pipeline), but no CPAC/DPARSF-style named pipeline or version number is given. | quote: "For preprocessing fMRI and MRI scans, we used SPM8 (http://www.fil.ion.ucl.ac.uk/spm/ software/spm8/) and our own in-house MATLAB code. Preprocessing was identical to that used in Ghiassian et al. [13]."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

Partly — the Connectome Computation System pipeline is named with its processing steps, but no version number is given. | quote: "The rs- fMRI data were processed using Connectome Computation System (Xu et al., 2015) pipeline, which includes slice timing correction, motion realignment, and intensity normalization. Nuisance variable regression (Fox et al., 2005; Lund et al., 2005) was implemented through band-pass ﬁltering and global signal regression strategies to clean confounding variations introduced by heartbeats and respirations, head motion, and low frequency scanner drifts. Furthermore, boundary-based rigid body and FMRIB’s linear & nonlinear image registration tools (Andersson et al., 2008; Ratziu et al., 2008) were used to register functional to anatomical images. Then, both functional and anatomical images were normalized to a standard template space, the Automated Anatomical Labeling atlas (Tzourio-Mazoyer et al., 2002)."

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

No — no named, versioned pipeline (e.g. CPAC/DPARSF) is given for the ABIDE data; processing followed the paper's own in-house SPM-based procedure.

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

Partly — DPARSF is named with a download link, but no explicit version number is stated in the processing-steps description. | quote: "all the fMRI images are preprocessed by the Data Processing Assistant for Resting- State fMRI (DPARSF) software (Cui et al., 2015) (http://d.rnet. co/DPABI/DPABI_V2.3_170105.zip). The whole preprocessing procedures include:(1) Converting DICOM to NIFTI, (2) Removing the ﬁrst 10 time points, (3) Slicing timing, (4) Realigning, (5) Normalizing with the echo-planar imaging (EPI) template, (6) Smoothing, (7) Removing the linear trend, (8) Temporal ﬁltering, (9) Removing covariates."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

Partly — C-PAC is named with its processing steps and an explicit replicability rationale, but no version number is stated. | quote: "The preprocessing was done using the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC, (12). We followed a preprocessing strategy adopted by the Preprocessed Connectome Project initiative3. This will allow others to replicate and extend the ﬁndings in this paper."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

Partly — CPAC via the Preprocessed Connectomes Project is named with preprocessing steps, but no version number is given. | quote: "we used the preprocessed version of ABIDE I (Di Martino et al., 2014) data publicly available via the Preprocessed Connectome Project (Cameron et al., 2013b). The preprocessing pipeline we used for this study is the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) (Cameron et al., 2013a). Regions of interests (ROIs) were deﬁned as the 116 regions in the automatic anatomical labeling (AAL) atlas (Tzourio-Mazoyer et al., 2002)."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

Partly — pipeline named, no version | quote: "We follow the same preprocessing pipeline (C-PAC)
and atlases (Harvard-Oxford) as described in [16]"

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

No | quote: "The Supplement also contains details on denoising efficacy 
(Supplement Section 6)"

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

Partly — PANDA named only as the comparison baseline for ABIDE network construction, not as the proposed method's own ABIDE preprocessing | quote: "ABIDE 
PANDA 
7.25 × 102 
0.64 
technician-dependent 
DGCL 
2.19 × 100 
0.71 
highly-automated"

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

Partly — C-PAC named, no version | quote: "The rs-fMRI data utilized in this study was preprocessed with 
the Configurable Pipeline for the Analysis of Conenectomes (C-
PAC)."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

Partly — C-PAC named, no version | quote: "We preprocessed the data using a widely adopted pipeline called
Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC)
(Craddock et al., 2013)"

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

No | quote: "The details of data acquisition and preprocessing
are described in Supplementary Material: Data Acquisition and
Preprocessing."

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

Partly — C-PAC named, no version | quote: "we use the Configurable Pipeline for the
Analysis of Connectomes (C-PAC) [41]"

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

Yes | quote: "We speciﬁcally used the data processed with the Conﬁgurable Pipeline for the Analysis of Connectomes [34] (C-PAC)."

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

Yes | quote: "we use the same preprocessing pipeline, the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) (Craddock et al., 2013)"

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

Yes | quote: "Preprocessing was performed in MATLAB (Mathworks, Natick, MA) using SPM8 (Wellcome Trust, London) software."

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

Yes | quote: "has been preprocessed by the Conﬁgurable Pipeline for the Analysis of Connectomes (C-PAC) [2], which involves skull striping"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

Yes | quote: "Selected strategies are Connectome Computation System (CCS), Conﬁgurable Pipeline for the Analysis of Con- nectomes (CPAC), Data Processing Assistant for Resting-State fMRI (DPARSF) and Neuroimaging Analysis Kit (NIAK)."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

Partly | quote: "We then preprocessed each subject using the same  parameters as per our dataset."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

Yes | quote: "All the preprocessing of resting state-fMRI was performed using the Statistical Parameter Mapping 8 (SPM8)"

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

Partly | quote: "The rs-BOLD data were corrected for motion artifacts using a time series general affine registration for 12 parameters (3dWarpDrive/AFNI)."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

Partly | quote: "The output with the six motion parameters (3 translations in x, y, z directions,  and 3 rotations: pitch (about x-axis), roll (about y-axis), and yaw (about z-axis)) is recor"

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

Yes | quote: "The time-series consid-
ered in our work were preprocessed according to the C-PAC pipeline"

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

No — only MRIcron is named, used solely for 3D-to-2D slice conversion, not a connectivity preprocessing pipeline. | quote: "MRIcron software was used to convert the  3D data format into 2D data images."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

Yes — CPAC named with the specific processing strategies used. | quote: "using the Configurable Pipeline for the Analysis of Connectomes (CPAC) (31)"

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

Yes — CPAC pipeline with its processing steps named. | quote: "The data is preprocessed using the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) pipeline"

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

No — no named preprocessing pipeline (e.g. CPAC/DPARSF) or version is given. | quote: "we used multiscale functional brain parcels. Brain parcels were created using a method known as the bootstrap analysis of stable clusters called BASC [32]."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

Yes — CPAC, filter_noglobal variant named. | quote: "processed by the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) [22] for experiments"

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

Partly — the CPAC pipeline is named via the Preprocessed Connectomes Project, but no version or specific strategy is detailed. | quote: "The pre-processed acquisitions are available as part of the Pre-processed Connectome Project (http://preprocessed- connectomes-project.org/abide/, C-PAC pipeline)."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

Yes — CPAC named via the Preprocessed Connectomes Project. | quote: "Data preprocessing was performed using the configurable pipeline for the analysis of con- 
nectomes."

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

Yes — DPARSF named with its processing steps. | quote: "we used the data Processing As-
sistant for Resting-State fMRI (DPARSF) t"

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

Yes — a detailed FSL-based lab-made pipeline is described step by step. | quote: "Anatomical 3D volumes and R-fMRI 4D volumes were 
processed in the FMRIB Software Library (FSL) environment."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

Yes | quote: "All rsfMRI data were preprocessed with a standardized and harmonized pipeline using the GRETNA package (36)."

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

Yes | quote: "SPM12, wherein the above steps are integrated into a unified model [39]."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

Yes | quote: "The package CPAC v1.8.0 was used for fMRI pre-processing including head motion correction, scrubbing, and nuisance regression."

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

Yes | quote: "The rs-fMRI scans selected from ABIDE I and ABIDE II cohorts were processed with the Configurable Pipe- line for the Analysis of Connectomes (C-PAC) [20]"

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

Yes | quote: "We used the preprocessed data using the Conﬁgurable Pipeline for the Analysis of Connectomes C-PAC pipeline (Craddock et al., 2013)"

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

Yes | quote: "we downloaded fMRI data (derivatives) pro- cessed with the Connectome Computation System (CCS) pipeline [9] which performs slice timing correction, motion realignment and global intensity normalisation."

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

Yes | quote: "The preprocessing method used in this paper is the conﬁgurable pipeline for the analysis of connectomes (CPAC)"

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

Yes | quote: "we performed preprocessing based on the Conﬁgurable Pipeline for the Analysis of Connectomes"

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

Partly — pipeline (C-PAC) named with processing steps but no explicit version number. | quote: "based on  the configurable pipeline for the analysis of connectomes  (C-PAC)"

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

Partly — C-PAC pipeline named via the ABIDE I Preprocessed release, no version number given. | quote: "from the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) pipeline (Craddock et al. 2013)"

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

Yes — GRETNA v2.0.0 (SPM12) with explicit preprocessing steps. | quote: "Data processing was performed with the GRETNA toolbox (v2.0.0) (Wang et al., 2015) based on SPM12."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

Partly — processing steps (slice-timing, motion correction, MNI registration, bandpass, smoothing) are listed without naming a pipeline/software version.

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

No — no named fMRI preprocessing pipeline/version is reported; only the custom motion-signature extraction/analysis method is described.

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

Partly — FSL and AFNI functions are named and steps detailed, but no single pipeline name/version (e.g. C-PAC/DPARSF) is given. | quote: "Data preprocessing was done using functions from FSL [54] and AFNI [55]; the specific functions are  17  denoted in brackets."

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

Yes — CONN toolbox pipeline with a full diagrammed processing sequence. | quote: "We used the CONN functional connectivity ​toolbox69 to process the rs- fMRI data from ABIDE-I."

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

Partly — a detailed custom FSL-based pipeline is described (tools named with citations) but not presented as a single named/versioned pipeline (e.g. C-PAC).

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

Partly — C-PAC pipeline named via CC200/CC400, no version number given. | quote: "the
imaging data is ﬁrst preprocessed using the Conﬁgurable Pipeline for Analysis
of Connectomes (CPAC)"

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

Yes — DPARSF named as the preprocessing toolbox. | quote: "The DPARSF is a MATLAB toolbox for fMRI data pre-
processing and analysing [17]."

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

Partly — C-PAC pipeline named with its general processing steps, but no version number given. | quote: "We have used the ABIDE dataset that is pre-processed using Conﬁguration Pipeline for
the
Analysis of Connectome (CPAC) [54]"

#### CL4 Atlas/parcellation reported

**Question.** CL4 Atlas/parcellation reported?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

No

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

No

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

No — whole-thalamus seed-based analysis, not an atlas-based parcellation

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

Yes — Harvard-Oxford atlas used for anatomical labelling of significant clusters

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

Yes — 100-region Schaefer-Yeo parcellation | quote: "Func- tional connectivity matrices were calculated at a single-participant level based on a widely used parcellation atlas with 100 cortical regions [61]."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

No — cortical ROIs used but no named standard atlas/parcellation is specified in the extracted text

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

Yes — AAL, Craddock 200 (CC), and Eickhoff-Zilles (EZ) atlases | quote: "The Automated Anatomical Labelling (AAL) atlas, with 116 ROIs, is widely used in ASD diagnosis studies [16, 35, 36, 37] due to its ability to provide precise anatomical lo- cations essential for identifying structural abnormalities caused by ASD. The Craddock 200 atlas [38], with 200 ROIs, is based on functional connectivity and is particularly useful for analysing resting-state fMRI data [39, 9, 36, 37], as it clusters the brain into functionally homogeneous regions. Recent studies have leveraged multiple atlases to capture diverse patterns related to ASD. For instance, Mahler et al. [37] proposed a multi-atlas framework for ASD classification using resting-state fMRI data, employing three atlases, including AAL and Craddock 200. Similarly, Deng et al. [9] utilised the AAL, Craddock 200 and Craddock 400 atlases. Their experiment in- dicates that Craddock 200 can outperform Craddock 400 in fMRI-based ASD diagnosis. Hence, we selected the Craddock 200 atlas, hereinafter referred to as the CC atlas. To further enhance the analysis, we leverage the Eickhoff-Zilles (EZ) atlas with 116 ROIs, which has also been utilised in recent ASD diagnosis studies [40, 41]. Derived from cytoarchi- tectonic mapping, the EZ atlas combines anatomical and functional data, offering a nuanced view that bridges structural and functional aspects of brain regions"

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Yes — 200-ROI Craddock atlas | quote: "Two hundred ROIs are determined from the Craddock atlas (15) (A). For each subject, the time series of voxel intensities are averaged over voxels with an ROI, and Pearson correlation coefficients are computed for all pairs of averaged time series (B), resulting in a 200"

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

No — voxel-based HOG texture features are used, not an ROI/atlas-based parcellation

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

No — whole-brain voxel-wise functional connectivity density analysis, not an atlas/ROI parcellation

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

Yes | quote: "Seed ROIs in the cerebellum were created using the probabilistic MR Atlas of the human cerebellum"

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

Yes | quote: "We use the Harvard Oxford (HO) atlas [23], so we  have N = 110 nodes."

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

No — no ROI atlas/parcellation is used; the model is trained on raw slice images

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

No — no ROI atlas or parcellation is used; raw 4D volumes are fed to the model

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

Yes | quote: "by partitioning the brain into multiple ROIs using two atlases, i.e., Automated Anatomical Labeling (AAL) (Tzourio-Mazoyer et al., 2002) atlas with 116 ROIs and Craddock200 (CC200) (Craddock et al., 2012) atlas with 200 ROIs."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

Yes | quote: "The dataset integrates three brain atlases (CC200,
AAL - Automated Anatomical Labeling, and DOS - Dosenbach160)"

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

Yes | quote: "it is parcellated using the Harvard-Oxford (HO) atlas. After downloading the pre-processed data, 110 ROIs are acquired using the HO atlas."

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

Yes | quote: "METAFormer employs a multi-atlas approach, where flattened connectivity matrices from the AAL, CC200, and DOS160 atlases serve as input to the transformer encoder."

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

Yes | quote: "The resting state fMRI data was then parcellated into
200 regions of interest (ROIs) using a spatially constrained
spectral clustering algorithm based on functional parcellations by
Cameron Craddock (Craddock et al., 2012)."

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

Yes — seven atlases named (HO, EZ, TT, CC200, CC400, AAL, DOS160).

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

Yes — seven atlases named (three BASC resolutions, Craddock, and others). | quote: "The rsfMRI was first parcellated into regions of interest (ROIs) using seven different atlases."

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

Yes — Harvard-Oxford (111 ROIs) as the primary atlas and Craddock CC200 (200 ROIs) as a replication atlas.

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

Yes — CC400 functional parcellation atlas. | quote: "We used the CC400 functional parcellation atlas of the brain throughout our study."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

No — features are derived from subject-level spatial ICA components and structural texture filters, not a named ROI atlas/parcellation.

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

Yes — Automated Anatomical Labeling (AAL) atlas (90 ROIs).

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

No — analysis is seed-based (right pSTS seed region), not based on a standard whole-brain atlas/parcellation.

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

Yes — AAL atlas, 90 ROIs. | quote: "fMRI image could be divided into 90 regions based on the Automatic Anatomical Labeling (AAL) (Tzourio-Mazoyer et al., 2002) atlas. We make these regions as the nodes of brain network, so there are 90 nodes. An average of the time series of a region’s all voxels can be used to capture the mean time series of this region (Khazaee et al., 2016). The average time series of every two brain regions can be employed to calculate the Pearson correlation coeﬃcient which is made as the link of the brain network (Khazaee et al., 2015), so there are 4,005 (90∗89/2) weighted edges."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

No — the analysis is voxel-wise on whole-brain summary-measure volumes, not based on an ROI atlas/parcellation.

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

Yes — AAL atlas, 116 ROIs. | quote: "we used the preprocessed version of ABIDE I (Di Martino et al., 2014) data publicly available via the Preprocessed Connectome Project (Cameron et al., 2013b). The preprocessing pipeline we used for this study is the Conﬁgurable Pipeline for the Analysis of Connectomes (CPAC) (Cameron et al., 2013a). Regions of interests (ROIs) were deﬁned as the 116 regions in the automatic anatomical labeling (AAL) atlas (Tzourio-Mazoyer et al., 2002)."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

Yes | quote: "and atlases (Harvard-Oxford) as described in [16]"

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

Yes | quote: "Schaefer parcellation to divide the cortex of each participant into 400 functional regions of 
interest (ROIs) (37), combined with 15 subcortical ROIs from the Harvard-Oxford subcortical 
atlas (38)"

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

Partly — eight functional subnetworks (CB, VN, SMN, DAN, VAN, LN, FPN, DMN) named for the ASD analysis, but the specific ROI atlas is not stated for ABIDE | quote: "For ASD, the ROIs of the dataset can be divided into
eight functional subnetworks: cerebellum and subcortical
structure (CB), visual network (VN), somatic motor network
(SMN), dorsal attention network (DAN), ventral attention
network (VAN), edge network (LN), frontoparietal network
(FPN), and default mode network (DMN)."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

Yes | quote: "taking the study object of brain connectivity measured with the resting-state functional 
magnetic resonance imaging (fMRI) data of CC200 atlas."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

Partly — data-driven group-ICA networks (8 BFNs) described instead of a fixed ROI atlas | quote: "The independent
components were derived using Group-ICA, and further inspected to identify eight well deﬁned brain function networks (BFNs)."

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

Yes | quote: "using spatially constrained spectral clustering
[cc200 template]"

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

Yes | quote: "the mean timeseries for a set
of cortical and subcortical regions of interest (ROIs) extracted
from the Har"

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

Yes | quote: "We considered the following predeﬁned atlases: Har- vard Oxford [40]"

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

Yes | quote: "the mean time series for a set of regions extracted from the Harvard Oxford (HO) atlas (Desikan et al., 2006) were computed"

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

Partly | quote: "we obtained pairwise functional connectivity measurements from a lattice of 7266 regions of interest covering the gray matter"

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

Yes | quote: "the Harvard Oxford (HO) atlas comprising R = 110 cortical and subcortical ROIs"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

No | quote: "in this work, ﬁrstly, we design an image genera- tor to generate single volume brain images from the whole-brain image of each subject."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

No | quote: "Additional 27 individuals with ASD from the ABIDE resting-state database were included to  test the reproducibility of the results."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

Yes | quote: "it was based on the automated anatomical labeling (AAL) template extract the averaged fMRI time series"

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

Yes | quote: "The 240 regions of interest (ROIs) defined for this study were extracted from the TT_Daemon human brain atlas [43] provided with the AFNI package [44]."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

No | quote: "We  find excess noise and randomness in the ASD cases, suggesting an uncertain motor-feedback signal."

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

Yes | quote: "The selected mean time-series
correspond to the Automated Anatomical Labeling atlas on 90 regions of interest
(AAL90)"

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

No — no atlas or parcellation is used; the predictor is a raw image slice. | quote: "In this research, the axial plane is used  as the input samples."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

Yes — four named atlases (AAL, HO, CC, Power). | quote: "we chose Harvard-Oxford (HO) and Automatic Anatomical Labeling (AAL) as anatomical templates and Craddock-200 (CC) as functional templates"

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

Yes — three named atlases (AAL, CC, EZ). | quote: "Functional connectivity matrices are derived from three brain atlases (AAL, CC, EZ) using Pearson correlation coeﬃcients"

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

Yes — BASC atlas at scale 122, selected via MSTEPS. | quote: "In this study, the scale is set to 122."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

Yes — AAL (116 ROIs) and CC200 atlases. | quote: "The mean time series from 116 regions of interest (ROIs) based on the automated anatomical labeling (AAL) atlas [23] are used for experiments."

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

Yes — CC200, 200-region parcellation. | quote: "We extracted rsfMRI time series using a 200-region parcellation CC200[?]"

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

Yes — Harvard-Oxford atlas, 111 ROIs. | quote: "According to the Harvard-Oxford atlas, there are 111 ROIs in the brain 
[32]."

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

Yes — AAL atlas, 116 ROIs. | quote: "we use the Automated Anatomical Labeling (AAL) tem-
plate (Tzourio-Mazoyer et al., 2002) to divide the brain into"

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

Partly — no discrete ROI atlas is used; instead the Smith et al. 2009 RSN10 ICA network template defines the networks. | quote: "the 10-brain resting-state networks 
(RSN10), “PNAS_Smith09_rsn10.nii.gz,” provided by Smith et. al.19,20 as a reference."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

Yes | quote: "network nodes were defined as 512 regions of interest with uniform areas obtained from a random parcellation (38)"

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

No

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

Yes | quote: "We used the resulting 11 region atlas to assign a region label"

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

Yes | quote: "The Harvard-Oxford (HO) atlas was used to extract time series from brain regions, obtaining 110 timeseries for each subject."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

Yes | quote: "Craddock 200 (CC200) functional parcellation (Craddock et al., 2012)"

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

No

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

No

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

Yes | quote: "Using automated anatomical labeling (AAL), we then used the ﬁrst 90 regions of interest (ROIs) as nodes"

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

Partly — surface template (Conte69, HCP pipelines) specified but not a standard ROI atlas; connectivity computed vertex-wise. | quote: "We resampled data to  the Conte69 surface template [79]"

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

No — analysis is voxel-wise whole-brain (grey-matter masked), no ROI atlas/parcellation used.

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

Yes — AAL standard brain template used to define 24 ROIs. | quote: "Then 24 ROIs corresponding to 7 brain networks were selected using the AAL standard brain template provided by the Montreal Neurological Institute (MNI)."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

Yes — first 90 AAL ROIs used as nodes. | quote: "We then use the ﬁrst 90 AAL ROIs as nodes"

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

No — not applicable; analysis is based on head-motion kinematics, not ROI connectivity.

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

Yes — Shen 268-node functional atlas. | quote: "A functionally defined atlas, consisting of 268 cortical and subcortical regions-of-interest (‘nodes’)"

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

Yes — Schaefer 200-parcel atlas. | quote: "Subsequently, 200 regions of interest (ROIs)  or nodes were defined in the brain using the Schaefer atlas"

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

Yes — Power et al. (2011) 264-ROI functional atlas, 11 RSNs. | quote: "ROIs were deﬁned as 10 mm diameter spheres whose center coordinates are given in MNI atlas space (Power et al., 2011)."

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

Yes — Craddock CC200 and CC400 parcellations. | quote: "We use Craddock 200 (CC200) data set"

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

Yes — AAL atlas (116 ROIs; 22 DMN ROIs used). | quote: "The  automated anatomical labelling (AAL) is selected as the standard brain atlas to divide the brain into 116 regions of  interest (ROIs)"

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

Yes — AAL atlas, 90 regions. | quote: "We have used the brain Automated anatomical labelling (AAL) template which divides the brain
into 90 regions."

#### CL5 Leakage control reported (feature selection/scaling/harmonisation…

**Question.** CL5 Leakage control reported (feature selection/scaling/harmonisation confined to training folds)?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

No — not applicable, no predictive model

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

No — no train/test or cross-validation protocol is described at all

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

No — not applicable, this is a group-difference GLM analysis, not a predictive model with train/test folds

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

No — not applicable, this is a group-difference GLM analysis, not a predictive model with train/test folds

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

No — the authors explicitly report that propensity-score computation and deconfounding (linear regression, ComBat) used all available participants rather than training data only | quote: "Similar to the computation of the pro- pensity scores, we performed deconfounding prior to our analyses, based on all the available participants instead of using only the training"

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

No — not applicable, this is a group-difference GLM/replication design, not a predictive train/test model

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

No — F-score feature selection is described as computed on all features in the dataset, and the 'proposed subset' is defined by a pretrained selector model's own correct classifications on the whole dataset rather than training-fold-only data

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Yes — nested cross-validation explicitly used for feature selection/tuning, and standardization is explicitly stated to use only training-set mean/SD to avoid double-dipping; the paper also demonstrates via simulation the magnitude of leakage if this rule is violated | quote: "The performance of each classifier is assessed by nested cross- validation: 10-folds are used in the outer cross-validation loop for the performance estimation, and 10-folds are used in the inner cross-validation loop to determine the optimal threshold value t for feature selection, or the optimal regularization parameter for lasso-regularized"

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

Yes — MRMR feature selection and hyperparameter tuning were performed via cross-validation strictly on the training set, with a single final evaluation on a held-out test set | quote: "Testing on the hold-out test set Dtest protected against overfitting in terms of algo- rithm choice, feature selection, parameter values, a"

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

No — not applicable, this is a group-difference voxel-wise GLM analysis, not a predictive train/test model

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

No — not applicable; this is a group-comparison study with no classifier, feature selection or scaling step reported

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

No — no statement that feature construction, scaling or selection was confined to training folds

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

No — no train/test split or fold procedure is described at all, so leakage control cannot be assessed

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

No — no statement that any scaling or feature construction step was confined to training folds

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

No — not stated whether FCN construction or normalization was performed only within the training partition of each repeated split

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

Yes | quote: "All experiments were conducted with a 10-fold cross-validation to divide the dataset into training and test sets, with 10% of the training set randomly selected as the validation set. Ultimately, the training, validation, and test sets were non-overlapping."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

Partly | quote: "stratified five-fold cross-
validation is conducted, where one fold is used for t"

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

Yes | quote: "we employed 10-fold stratified cross-validation. For each fold, the model is trained
on the remaining nine training folds and evaluated on the held-out test fold.
Further, we set aside 30% of each training fold as validation sets"

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

No — not applicable; this is a group-comparison/method-comparison study with no train/test classifier split

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

Partly — the CNN architecture/hyperparameters were fixed across folds, but baseline hyperparameters were chosen by maximising cross-validation accuracy itself, which the authors state is optimistic. | quote: "We test 10 linearly spaced values for the hyper-parameter α in the range [0.1,10] and report the highest cross-validation accuracy. Thus this baseline result reﬂects an optimistic estimate of performance."

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

Yes — ABIDE features were standard-scaled using the IMPAC (training) dataset's own mean/SD rather than refitting on ABIDE, and ABIDE was explicitly excluded from model training and hyperparameter optimisation. | quote: "The features were standard scaled by the mean and standard deviation of the IMPAC dataset."

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

Unclear — 5-fold CV is used per site/strategy, but the text does not state whether any feature selection/scaling step was fit only on training folds.

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

Unclear — classifier hyperparameters were tuned (e.g. SVM C, KNN k, RF depth/n_estimators), but the text does not state whether this tuning was confined to training folds within the CV scheme.

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

Yes — hyperparameters were selected via 5-fold CV confined to the 70% training set, with the 30% hold-out set reserved untouched for final evaluation. | quote: "The ABIDE dataset consists of 1111 scans, taken from 17 sites consisting of 573 healthy controls and 538 patients with autism. To evaluate each learning model, we use 800 subjects (70%) for model training and 311 subjects (30%) for hold-out testing. We use the same case/control ratio (0.5157) for both training and test set."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

Partly — the offline SSAE pretraining pool is explicitly restricted to non-target sites (avoiding target-site leakage into pretraining), and CV is stratified by diagnosis, but the text does not state whether the site/age/gender/handedness regression itself was refit within each CV fold. | quote: "the independent healthy FC data from the remaining 16 sites from the ABIDE repository were accumulated as pre- collected data to train an SSAE prototype during oﬄine learning. Then, we randomly split the data from the target site into training and testing set. The data from the training set were applied on an SSAE prototype in the prior knowledge aided training step. The hold-out testing data were then used to evaluate the trained DTL-NN model."

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

N/A — this is a group-difference (not predictive/cross-validated) analysis; no train/test split or feature selection applies.

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

No — the optimal number of base classifiers and the optimal feature-set size were both selected by maximising accuracy on the same held-out test set that was then reported as the final result, not on a separate validation set or via cross-validation. | quote: "Firstly, the 84 samples are divided into 58 training samples and 26 test samples based on the ratio of 7:3. Then 50 samples are randomly selected from the 58 training samples and 62 features are randomly selected from 4,225 features, which form a single SVM using Radial Basis Function (RBF) as kernel provided by the SVM toolbox (http://see.xidian.edu.cn/faculty/chzheng/ bishe/indexﬁles/indexl.htm) (Gunn, 1998). The width argument of RBF equals to 3, and penalty coeﬃcient equals to Inf. The process is repeated for 500 times and these 500 SVMs constitute into a random SVM cluster."

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

Yes — the five-fold scheme kept training/validation/test invariant within each fold, and the leave-site-out scheme used a separate validation split (90/10 of the remaining data) purely for model/epoch selection before testing on the held-out site, guarding against contamination. | quote: "For the leave-site-out CV procedure, we selected ﬁve sites with the highest number of total subjects (ASD/total), namely New York University (NYU) (90/159), Kennedy Krieger Institute - 1 (KKI-I) (88/114), University of Miami - 1 (UM-I) (50/96), University of California, Los Angeles (UCLA)-I (28/69), Oregon Health & Science University (OHSU)-I (42/64)."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

Unclear — 10-fold CV, a single linear kernel and only 10 selected features are used to limit overfitting, but the text does not explicitly state whether the sequential feature selection step was nested within each CV training fold. | quote: "We minimized the risk of overﬁtting by using three limiting approaches. First, the simplest kernel (linear) was used for the SVM. Second, only 10 features were used to learn to classify between 104 subjects. Finally, using 10-fold cross validation ensured the model is only evaluated on data points that it has not experienced before."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

No | quote: "We use the same 10-fold cross validation as in
[7] of the ABIDE dataset, using their publicly released code"

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

No | quote: "ComBat (36) was used to remove the confounding 
effects of scanning site from the fMRI data (Supplement Section 4)."

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

No | quote: "Five-fold 
cross-validation is used to evaluate the performance of the 
model."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

No | quote: "Finally, the 1935 top features were selected to 
perform the differentiation between individuals with ASD and TC 
via the SVM classifier. 
To ensure the reliability of experimental result, we utilized 10-
fold cross-validation to measure the accuracy of predicted label."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

No | quote: "We then randomly
split all subjects into training and validation sets."

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

No | quote: "we did not perform cross-validation during clustering."

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

No | quote: "Hence, we take the upper triangular
part and vectorize it to obtain a feature vector whose dimension
is then further reduced using recursive feature elimination via a
ridge classifier."

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

Yes | quote: "Note that the ROI were all deﬁned on the training set to avoid possible overﬁtting."

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

Partly | quote: "each iteration trains the ridge classiﬁer on the training set with the current feature vector"

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

Unclear | quote: "a leave-one-out classiﬁer was used to generate a classiﬁcation score for each of the 964 subjects, leaving out one subject at a time"

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

No | quote: "The diﬀerent network parameters are optimised using cross-validation."

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

No | quote: "we ﬁrst divided the whole dataset into two parts: training (85%), and testing (15%)."

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

N/A | quote: "This correlation was observed also within the controls, and"

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

N/A | quote: "we performed, respectively, two-tail two-sample t-tests for fractional occupancy, lifetimes, and interval times of HMM states between patients with subjects with ASD and HCs."

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

N/A | quote: "To determine regions of the brain of ASD patients with increased or decreased signal complex- ity respect to a typical control group, we estimated the voxel-wise FD on every subject of both groups."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

N/A | quote: "We  find excess noise and randomness in the ASD cases, suggesting an uncertain motor-feedback signal."

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

Yes | quote: "Tuning is performed through an inner
cross-validation launched on each training split to select the best corresponding parameter value."

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

No — no feature selection/scaling/harmonisation procedure or leakage control is described. | quote: "The samples were separated into two folders  which were the training file and test file."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

Partly — no feature selection was used (avoiding that leakage route) and the SVM C hyperparameter was fixed rather than tuned to avoid a nested-CV leak, but this is stated as a design choice rather than an explicit leakage-control procedure. | quote: "to avoid running optimization of hyperparameters, which would have required and additional nested cross validation"

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

No — the feature-selection (HOA) and autoencoder pre-training steps are described without stating whether they were fit on the training split only. | quote: "The SSDAE comprises two autoencoder layers: the ﬁrst encoding layer has 1,000 units, and the second reduces the representation to 600 units."

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

No — no statement that any preprocessing or feature step was confined to the training folds. | quote: "Tests on the ABIDE I data set were carried out using the 10-fold cross-validation method. The main purpose of this process is to use each data for both training and testing."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

No — the hyperparameter search is described but not stated to be confined to the source (training) domains only. | quote: "The parameters (α, β, γ, λ, η) are all searched in the set of {0.001, 0.01, 0.1, 1, 10, 100}."

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

No — node-subset feature selection is based on group differences computed across the same sites used for training/testing, with no stated train/test separation for that selection step. | quote: "nodes that show variability <0.9 in typical subjects and experience a positive group-level diﬀerence across the three big sites (NYU, UM, and USM)"

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

No — no statement that graph-construction or feature steps were confined to training folds. | quote: "a 10-fold cross-validation schema that mixes data from all 17 sites while keeping"

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

No — no statement that any preprocessing or feature step was confined to the training folds within the 10-fold scheme. | quote: "we employed the 10-fold cross-
validation strategy to conduct the comparison among dif-
ferent models."

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

Partly — biomarkers (A-masks) are derived entirely from ABIDE and then validated on the fully independent local KMUH cohort, which avoids a direct train/test leakage, but no leakage-control statement is given for the ABIDE-internal statistics themselves. | quote: "the A-masks were derived from the group analysis of the ABIDE 
RSN10 FC maps"

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

Yes | quote: "In each LOOCV fold, we included the feature selection, model learning, and testing."

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

Partly | quote: "a multiple linear regression model was trained on ABIDE II."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

N/A

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

Partly | quote: "We esti- mated the NeuroHarmonize model parameters on the entire cohort of control subjects, by specifying the age as a covariate, whose effect is to be preserved during the harmonization process. Finally, we applied the esti- mated model on the entire sample of subjects with ASD and TD controls."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

Unclear

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

Unclear

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

No

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

No | quote: "We further validate the detected subnetwork features by performing classiﬁcation analysis. We employ the support vector machine with radial basis function kernel and linear kernel as our classiﬁer."

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

No — study is not a predictive/ML analysis, no train/test split or feature selection described.

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

No — the reported example used no feature selection; the general software supports grid-search CV for hyperparameter tuning but this is not detailed as leakage-controlled for the example run.

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

No — not a predictive/ML study; no train/test or feature-selection leakage issue applies.

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

No — not a predictive/ML study; no train/test split.

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

No — not a predictive/ML study.

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

Yes — edges associated with motion or differing between sites were masked out before CPM modelling, and leave-one-out cross-validation rebuilds the model excluding the test participant at every iteration. | quote: "a leave-one-out cross-validation to evaluate the potential of models to predict  14  an unseen participant’s score, where N-1 participants are used to build the predictive model"

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

No — not a predictive/ML study; no train/test split.

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

Partly — the elastic-net regression (FC from entropy) used 10-fold cross-validation, but this model is diagnosis-blind; no leakage-control statement is given for the subsequent group-comparison of model fit.

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

Partly — 5-fold stratified cross-validation and permutation significance testing are used, but no explicit statement that feature/hyperparameter selection (grid search) was confined strictly within training folds only. | quote: "For both models, parameter estimation is done using grid search."

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

No — not explicitly described; pretrained ImageNet CNNs are used as fixed feature extractors but no statement confines any fitting step to training folds only.

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

No — the Teacher-Student feature-ranking and SFFS feature-selection steps are described as being performed on the dataset prior to the reported 10-fold cross-validation, with no statement that they were repeated within each training fold only.

#### CL6 Site handling reported (site covariate, harmonisation e.g.…

**Question.** CL6 Site handling reported (site covariate, harmonisation e.g. ComBat, or leave-site-out evaluation)?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

Partly — multisite heterogeneity (scanner, acquisition, inclusion/exclusion) is discussed as a factor users must account for, no harmonisation is performed by this paper | quote: "As data aggregation followed independent data collections across multiple sites, various sources of heterogeneity exist between collections."

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

Partly — results are tabulated separately per site/resource (e.g. UM, UCLA, USM, LEUVEN, BNI, EMC, ETH, GU) but this is descriptive reporting, not harmonisation or leave-site-out evaluation | quote: "ABIDE-II data download and labelling was a   challenging task. Each image was manually labelled and   assigned a group. Each group was tested separately to compare and analyze results of each set."

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

Yes — site included as a one-hot-encoded covariate in the ABIDE GLM analysis | quote: "To account for potential con- founding effects from differences in scan acquisition parameters, we included site as a covariate in our ABIDE GLM analysis as one-hot encoded variables."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

Yes — ComBat used to remove site/collection-time effects across ABIDE I and II data collections | quote: "To account for site and collection time variability across each of the data collections in ABIDE I and II data repositories, site effects were removed using the ComBat function available in python [61] (https​://githu​b.com/ brent​p/comba​t.py). This approach has been shown to effectively account for scanner-related variance"

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

Yes — site is one of the matched propensity-score covariates, and ComBat site harmonisation is tested as a deconfounding approach | quote: "Similar to the computation of the pro- pensity scores, we performed deconfounding prior to our analyses, based on all the available participants instead of using only the training"

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

Yes — site included as a covariate in group-level statistics to minimize the multicentric site effect | quote: "Thus, to minimize the site eﬀect in our analysis, we included it as a covariate in group-level statistics as described in the section 2.3."

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

No — no site covariate, harmonisation, or leave-site-out evaluation is reported; the NYU subset is analysed separately as a single-site benchmark, not as a held-out generalisation test

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Yes — per-site z-standardization (train-only) applied, improving SVM accuracy from 63% to 68%; leave-one-site-out cross-validation discussed as a further approach | quote: "We took the so far best performing classifier – the support vector machine – and applied it to the data set after this stand- ardization was performed. The resulting classification accuracy increased from 63 to 68%."

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

Partly — site of imaging is included as a personal-characteristic input feature rather than harmonised or evaluated via leave-site-out | quote: "The ABIDE dataset also provided an extensive array of non-imaging, personal characteristic information from which we used age, sex, handedness, full scale IQ, verbal IQ, performance IQ, site of the imaging and eyestat (which indicated whether the person kept his eyes open or not during the scan)."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

No — the GLM covariates were limited to age and sex; no site covariate, harmonisation, or leave-site-out evaluation is reported despite pooling multiple ABIDE sites | quote: "2-tailed t-test design with two covariates of age and sex was used to compute the statistical signiﬁcance of the FCD diﬀerences between the two groups. Statistical signiﬁcance was based on the false discovery rate corrected P < 0.05 together with requiring 20 voxels for the minimum continuous voxel size within a cluster (corrected P < 0.05)."

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

Yes | quote: "FSIQ and imaging sites were included as nuisance covariates"

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

No — cross-validation is described as a random pooled fivefold split with no site covariate or leave-site-out scheme

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

No — single-site (NYU only) analysis; no multi-site handling applicable or reported

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

No — multi-site evaluation uses pooled 5-fold cross-validation with no site covariate or leave-site-out scheme, despite acknowledged scanner heterogeneity effects

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

Partly | quote: "to avoid signiﬁcant inter-site heterogeneity, we mainly used rs-fMRI data from the NYU site. While ABIDE contains data from 21 sites, as a future work, we will evaluate the proposed method on all sites in ABIDE and design smart techniques to reduce inter-site data heterogeneity."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

Partly | quote: "In the population-gcn [19] study, the construction of patient-patient relational graphs was based on demographic information, speciﬁcally sex and site."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

No — no site covariate, harmonisation, or leave-site-out scheme is reported for the pooled 17-site cohort

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

No — no site covariate, harmonisation, or leave-site-out scheme is reported for the pooled 17-site cohort

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

Yes | quote: "We present a site-wise de-meaning (SWD) strategy in multi-site FC analysis and compare its performance with two common site-effect mitigation methods, i.e., generalized linear model (GLM) and Combining Batches (ComBat) Harmonization."

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

No — no site covariate or harmonisation is reported; the ABIDE-II test set is drawn from sites that overlap with ABIDE-I training sites rather than a leave-site-out design.

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

No — no site covariate, harmonisation, or leave-site-out scheme is reported; all ABIDE sites are pooled for external validation.

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

Partly — no statistical harmonisation (e.g. ComBat) is used; site heterogeneity is instead addressed via the federated-learning design itself plus two domain-adaptation strategies (Fed-MoE, Fed-Align), and Cross/Mix comparisons quantify cross-site generalisation. | quote: "Overall, the accuracies of using CC200 was lower than the accuracies of us- ing HO. This could be caused by overﬁtting as the number of parameters required for training CC200 data is higher than HO due to the dimensionality of the input."

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

Yes — a leave-site-out evaluation was performed across all 17 ABIDE I sites in addition to pooled 10-fold CV. | quote: "we used a leave-site-out approach for our proposed CNN, SVM, KNN, and RF classiﬁers (Heinsfeld et al., 2018). In this method, each site is taken as one fold in the dataset, and we applied a cross-validation approach on the remaining sites instead of diﬀerent folds. Therefore, each time, one site out of 17 is used to test, and the other sites are used for training."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

Partly — no ComBat/covariate harmonisation or leave-site-out scheme is used, but the authors explicitly test for site confounding via a site-only baseline classifier and a site-balanced test-set re-evaluation, both of which argue against a site-driven result. | quote: "We then tested those previously-trained classifiers on these new “site-balanced test sets” and found that the accuracies did not differ significantly from the original test set results: here, it was 69.88% for ADHD-200 and 63.46% for ABIDE."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

Yes — site (along with age, gender and handedness) was explicitly regressed out of FC weights via OLS multiple regression, following an approach from a prior ABIDE study. | quote: "Site bias was corrected among diﬀerent sites similar to an approach described previously by an ABIDE study (Heinsfeld et al., 2018). Speciﬁcally, a multiple regression analysis was conducted to control for potentially confounding variables (site, age, gender, and handedness). These variables were regressed from FC weights across connections among ROIs. When adjusting for the confounding factors, our regression model is: y = β0 + β1x1 + β2x2 + β3x3 + β4x4 + ε where y is the vector of FC weights, x1 to x4 represent the four explanatory variables, site, age, gender, and handedness. βi is the intercept and the corresponding regression coeﬃcients. ε is the residual vector. Using ordinary least squares (OLS) estimation, βi was estimated. Then, these cofounding variables were regressed out from the FC weights."

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

Partly — groups were matched on age (and largely IQ) within and across the nine sites, and motion was handled as a covariate, but no explicit site covariate or ComBat-style harmonisation of connectivity values themselves is reported.

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

No — subjects were selected by matching a single scan protocol rather than analysing multiple sites, and no site covariate or harmonisation is reported.

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

Yes — an explicit leave-site-out cross-validation was run across the five largest ABIDE sites in addition to pooled five-fold CV. | quote: "For the leave-site-out CV procedure, we selected ﬁve sites with the highest number of total subjects (ASD/total), namely New York University (NYU) (90/159), Kennedy Krieger Institute - 1 (KKI-I) (88/114), University of Miami - 1 (UM-I) (50/96), University of California, Los Angeles (UCLA)-I (28/69), Oregon Health & Science University (OHSU)-I (42/64)."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

No — sites are pooled within each age group with no explicit site covariate, harmonisation, or leave-site-out evaluation reported.

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

No | quote: "from 20 different
sites."

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

Yes | quote: "ComBat (36) was used to remove the confounding 
effects of scanning site from the fMRI data (Supplement Section 4)."

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

No | quote: "And the largest dataset for autism research comes
from Autism Brain Imaging Data Exchange (ABIDE) [11]."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

Partly — an intra-site stratified shuffle-split cross-validation was performed to probe site effects, but this is not a leave-site-out design and no site covariate/harmonisation is used in the main pooled result | quote: "For the challenges of site-related 
variability, we also performed an intra-site prediction based on the 
stratified shuffle split cross-validation."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

N/A — single-site analysis (NYU only), chosen specifically to avoid cross-site heterogeneity | quote: "To avoid the impact of data heterogeneity,
we collected raw rs-fMRI data from the whole NYU site"

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

No | quote: "Site-speciﬁc analysis was applied on the ADHD dataset. We
could not apply this analysis on ASD dataset since there was only
one site that had enough samples for HC and disease subgroups"

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

Partly — site is used directly as a phenotypic edge-weight feature in the population graph, not corrected for or used in a leave-site-out split | quote: "For the edge weights of the population graph
on the ABIDE datset, we incorporate the subject’s gender, age
and acquisition site as as phenotypic measures."

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

Yes | quote: "This validation with a leave-one- site-out cross-validation strategy reduces the risk of over- ﬁtting data from a single site"

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

Partly | quote: "the phenotypic graph (using default phenotypic measures), which corresponds to the graph constructed taking into account SEX and SITE information"

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

Yes | quote: "Age, age-squared, gender, handedness, and site were included as covariates for the classiﬁer."

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

Partly | quote: "We also ensure that subjects from all 20 sites are included in both training and test sets."

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

Partly | quote: "therefore we performed unit-site classiﬁcation to pattern out"

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

No | quote: "We selected the same 5 datasets used in (1), that is sites with  codes: 'CALTECH' (n=19), 'CMU' (n=14), 'PITT' (n=30), 'UM_1' (n=55), 'UM_2' (n=13) for  a total of 131 ASD participants."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

Yes | quote: "we ﬁrst applied a data-driven algorithm that maximized the p-values of the group diﬀerence of age, FIQ, and mean FD (using two-sample t-tests). Then, to exclude the inﬂuence of the site interaction eﬀect, we"

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

No | quote: "Subjects were scanned using a 3T GE Signa MRI and a 32-channel RF- coil."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

Yes | quote: "Note that these group differences held independently for NYU, UCLA_1,  OLIN, and PITT sites and are presented for both linear speed (LS) and angular speed (AS) micro-movements"

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

No | quote: "our sample is heterogeneous by the range of the patients’ ages (between 6 and 18 years old), the multisite nature of the data (seventeen sites contributed to the ABIDE-I dataset)"

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

No — no site covariate, harmonisation or leave-site-out evaluation is reported. | quote: "The samples were separated into two folders  which were the training file and test file."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

Yes — leave-one-site-out cross-validation across the four sites. | quote: "a leave-site out cross-validation scheme was performed: each training set was composed by all the sites except one, that was left out for validation."

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

No — no site covariate, harmonisation or leave-site-out evaluation is reported; evaluation is a pooled random split. | quote: "the ﬁnal dataset consists of 1,035 samples distributed as follows: 623 samples for the training set, 308 samples for the validation set, and 104 samples for the test set."

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

No — 10-fold cross-validation is pooled across subjects with no site covariate or leave-site-out evaluation. | quote: "Tests on the ABIDE I data set were carried out using the 10-fold cross-validation method."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

Yes — leave-one-site-out inter-site cross-validation across all 17 sites, which is the method's core domain-adaptation design. | quote: "we conduct inter-site cross-validation experiments on 17 sites from ABIDE database."

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

Yes — both a site-balanced intra-site variant and a leave-one-site-out inter-site evaluation are reported. | quote: "For inter-site, we employed a leave- one-out-site approach that involved training the classiﬁer on all the sites except the one left out for testing."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

Partly — the primary evaluation pools sites in proportion (not leave-site-out), though a supplementary per-site 5-fold cross-validation is also reported. | quote: "Then, 5-fold cross-validation on each site is performed separately."

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

No — 10-fold cross-validation pools all 17 sites with no site covariate or leave-site-out evaluation reported. | quote: "we employed the 10-fold cross-
validation strategy to conduct the comparison among dif-
ferent models."

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

No — ABIDE I (17 sites) and ABIDE II (16 sites) are pooled for the group-difference analysis with no site covariate, harmonisation, or leave-site-out evaluation reported. | quote: "This study included 1112 ABIDE I datasets 
from 17 sites and 983 ABIDE II datasets from 16 sites."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

Yes | quote: "We performed a leave-one-site-out cross-validation to assess whether our main findings were biased by site specific sites."

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

Yes | quote: "site-out analysis (details can be found in Additional file 1: “Reproducibility” section) in the ADOS-guided fALFF and GMV fusion on the whole ASD group to check whether the site effect will contribute to current ASD pattern."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

Yes | quote: "We accessed publicly available ABIDE data across 30 different sites."

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

Yes | quote: "We esti- mated the NeuroHarmonize model parameters on the entire cohort of control subjects, by specifying the age as a covariate, whose effect is to be preserved during the harmonization process. Finally, we applied the esti- mated model on the entire sample of subjects with ASD and TD controls."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

Partly | quote: "we performed a 5-fold cross validation for each site because of the limitation of the size of the data."

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

No

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

No

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

N/A | quote: "The data set was collected at the University of Michigan, one of the ABIDE data collection sites"

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

Yes — ComBat harmonization applied for site effects, validated against a surface-based linear model control. | quote: "Data were harmo­ nized for site effects while preserving effects of age and  ASD diagnosis using ComBat [86]"

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

No — no site covariate, harmonisation, or leave-site-out evaluation is reported.

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

No — single-site (KKI) study; no multi-site harmonisation or leave-site-out evaluation needed or reported.

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

No — single-site (UCLA) analysis; no multi-site harmonisation or leave-site-out evaluation.

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

No — all sites pooled without a stated site covariate or harmonisation; no leave-site-out evaluation (associational, not predictive).

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

Partly — edges differing significantly between sites (t-test) were masked out of the FC profile rather than a formal harmonisation (e.g. ComBat) or leave-site-out evaluation.

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

Partly — problematic sites (Stanford, Leuven-1) excluded outright, but no formal multi-site harmonisation (e.g. ComBat) or leave-site-out evaluation across the remaining sites.

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

No — sites pooled with a per-site minimum-N inclusion rule but no explicit site covariate, harmonisation, or leave-site-out evaluation.

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

No — 16 sites pooled with stratified (not leave-site-out) cross-validation; no site covariate or harmonisation reported.

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

No — three sites pooled with no site covariate, harmonisation, or leave-site-out evaluation reported.

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

No — the combined-dataset analysis explicitly pools all 17 sites "ignoring the sites intrinsic variability"; no harmonisation or leave-site-out evaluation reported for this headline result (site-wise results are reported separately per site, not as leave-site-out). | quote: "ﬁrst the correlation-based connectivity matrix is arranged on all the sites,
ignoring the sites intrinsic variability, then a 10-fold cross-validation-based accuracy, sensitivity and
speciﬁcity is given in the mentioned table."

#### CL7 Code and/or participant list available

**Question.** CL7 Code and/or participant list available?

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

Yes — full dataset and phenotypic files openly available via NITRC after registration | quote: "All ABIDE II datasets can be accessed, after establishing a login and user password, through FCP/INDI at the Neuroimaging Informatics Tools and Resources Clearinghouse (NITRC; http://fcon_1000.projects. nitrc.org/indi/abide/)."

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

No — no code repository or participant ID list is mentioned

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

No — no code repository or participant ID list is mentioned for the ABIDE subset

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

Partly — ABIDE raw data are openly available via FCP-INDI; exact participant selection criteria are published in Supplementary Methods, but no analysis code repository is mentioned | quote: "ABIDE I and II: Data are freely accessible in the publicly available Autism Brain Imaging Data Exchange repository (http://fcon_1000.projects.nitrc.org/indi/ abide)."

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

Yes — code, imaging features and phenotypic data openly available on GitHub | quote: "Data Availability Statement: The imaging and phenotypic data were provided, in part, by the Autism Brain Imaging Data Exchange initiative (ABIDE-I and II; https://fcon_1000.projects.nitrc. org/indi/abide) and the Healthy Brain Network (https://fcon_1000.projects.nitrc.org/indi/cmi_ healthy_brain_network). All imaging features, phenotypic data, and code are openly available at https://github.com/OualidBenkarim/ps_diversity."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

Partly — ABIDE data are openly available via the ABIDE Consortium website; no separate analysis code repository is mentioned

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

Yes — code and evaluations publicly released on GitHub

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

Yes — MATLAB code for all discussed pipelines publicly available | quote: "The MATLAB code as discussed is available at http://www.ncm. hest.ethz.ch/downloads/software.html under “ABIDE 1 classifi- cation and pitfalls."

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

Partly — the ABIDE and ADHD-200 datasets are publicly available online, but no separate analysis code repository is mentioned | quote: "Data Availability Statement: All data used in this paper are publicly available as follows: The ADHD- 200 dataset is available online at http://fcon_1000. projects.nitrc.org/indi/adhd200/ The ABIDE dataset is available online at http://fcon_1000.projects. nitrc.org/indi/abide/."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

No — ABIDE data are publicly available but no analysis code repository is mentioned

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

No — no code repository, data-availability statement or participant-ID list found in the full text

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

Yes — code | quote: "The source codes of GAT-LI are publicly available  at the project website of https://​github.​com/​large​app/​gat-​li."

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

Partly | quote: "The raw data supporting the conclusions of this article will be made available by the authors, without undue reservation."

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

No — no data-availability statement or code repository link found in the full text

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

Partly | quote: "The original contributions presented in the
study are included
in the article/supplementary material, further inquiries can be
directed to the corresponding author/s."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

Yes — code | quote: "An interactive code base for DeepASD implementation is available at https:// codeocean.com/capsule/6043886/tree."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

Yes — code | quote: "https://github.com/ku-milab/EAG-RS"

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

Yes — code | quote: "The code for our framework is available at github.com/Lugges991/METAFormer"

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

Partly | quote: "Autism data is publicly available from ABIDE (http://fcon_1000.projects.nitrc.org/indi/abide/)"

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

No — no statement of code or participant-list availability was found in the text.

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

Yes — full analysis source code, saved models, and pipeline parameters are released publicly. | quote: "we are pleased to provide full analysis source code, saved models, and pipeline parameters at:"

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

No — no statement of code or participant-list availability was found in the text.

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

No — data are available on request to the corresponding author, not openly released. | quote: "DATA AVAILABILITY STATEMENT The datasets generated for this study are available on request to the corresponding author."

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

Partly — the ABIDE and ADHD-200 datasets are stated to be publicly available (with source URLs), but no analysis code repository or participant ID list specific to this study is given. | quote: "Both datasets are available online publicly. The ADHD-200 dataset is available at: http://fcon_1000.projects.nitrc.org/ indi/adhd200/ The ABIDE dataset is available at: (http://fcon_1000.projects.nitrc.org/indi/abide/)."

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

No — no statement of code or participant-list availability was found in the text.

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

No statement of code or participant-list availability was found in the text.

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

No — no statement of code or participant-list availability was found in the text.

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

Yes — all experiment code is released on GitHub. | quote: "The code used of all the experiments performed is available on GitHub1."

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

Partly — raw data will be made available by the authors to any qualified researcher on request, rather than openly deposited at publication. | quote: "The raw data supporting the conclusions of this manuscript will be made available by the authors, without undue reservation, to any qualiﬁed researcher."

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

No | quote: "3https://github.com/parisots/population-gcn"

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

No | quote: "Details about our exclusion 
criteria are provided in Supplement Section 2."

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

No | quote: "And the largest dataset for autism research comes
from Autism Brain Imaging Data Exchange (ABIDE) [11]."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

No | quote: "For more details with the 
preprocessed data, please see http://preprocessed-connectomes-
project.org/abide/."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

No | quote: "The original contributions presented in the study are included
in the article/supplementary material, further inquiries can be
directed to the corresponding author/s."

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

Partly — analysis source code released on GitHub, but no participant list specific to the ABIDE subset | quote: "Data and source code
used in this work is publicly available at https://github.com/xinyuzhao/identiﬁcation-of
-brain-based-disorders.git."

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

No | quote: "We select a set of 871 subjects,
consisting of 403 ASD patients and 468 healthy controls
(HCs)."

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

Partly | quote: "http://team.inria.fr/parietal/files/2015/07/MSDL_ABIDE. zip"

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

Yes | quote: "The model implementation is publicly available at https://github.com/parisots/population-gcn."

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

No | quote: "available at http://fcon_1000.projects.nitrc.org/indi/abide/."

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

Yes | quote: "source code available at https://github.com/sk1712/gcn_metric_learning"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

No | quote: "We incorporated data from 529 ASD individuals and 573 typical controls (TC) for each pipeline"

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

Yes | quote: "Code used in this paper is available at  https://github.com/eglerean/hfASDmodules."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

No | quote: "Publicly available datasets were analyzed in this study. This data can be found here: http://fcon_1000.projects.nitrc.org/"

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

No | quote: "We downloaded data from the publicly accessible ABIDE-1 database: http://fcon_1000.projects.nitrc.org/indi/abide/ abide_I"

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

No | quote: "Datasets from a total of 605 participants were analyzed, including 304 individuals with Autism Spectrum  Disorder (ASD) and 301 typically developing controls (CT)."

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

No | quote: "In this study, we consider the ABIDE I preprocessed dataset (Di Martino
et al., 2014; Craddock et al., 2013)."

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

No — no code repository or participant list availability statement found. | quote: "The performance of the CNN pre-trained model was  evaluated using several measurements such as  recall, precision, and accuracy."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

No — data-availability statement only links to the general ABIDE repository, no study-specific participant list or code repository. | quote: "Publicly available datasets were analyzed in this study. This data can be found here: http://fcon_1000.projects.nitrc.org/indi/abide/"

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

No — data-availability statement only links to a general dataset reference, no code repository or participant list for this study. | quote: "Publicly available datasets were analyzed in this study. This data can be found here:"

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

No — no code repository or participant-list availability statement found. | quote: "we used the same 871 samples from the ABIDE 1 data set [23], [24], [25]."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

No — only supplementary material is linked via the journal DOI; no code repository or participant list. | quote: "This article has supplementary downloadable material available at"

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

No — no code repository or participant-list availability statement found. | quote: "The pre-processed acquisitions are available as part of the Pre-processed Connectome Project (http://preprocessed- connectomes-project.org/abide/, C-PAC pipeline)."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

No — data-availability statement only links to the general ABIDE/Preprocessed Connectomes Project resource; no study-specific code or participant list. | quote: "The datasets analysed during the current study are available from a world-wide multi-site database Autism Brain Imaging 
Data Exchange (ABIDE I)"

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

Yes (code only) — the authors' code is public on GitHub; no participant-ID list is given. | quote: "The code is available
at https://github.com/LYQbyte/ASD-HNet."

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

Partly — the 30 biomarker masks and pipeline are shared on GitHub, but the underlying datasets/participant list are available only on reasonable request. | quote: "The pipelines, as well as the 30 masks of this study, are available28."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

No

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

Yes | quote: "The supervised fusion code has been released and integrated in the Fusion ICA Toolbox (FIT"

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

Yes | quote: "Custom R code and data to support the data correction, correlation analysis, visualizations, functional, and gene set enrichments are available at https://github.com/konopkalab/"

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

Yes | quote: "To allow the reproducibility of the analysis, the identification numbers (IDs) of the participants selected in the final sample are reported in Additional file 1."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

Yes | quote: "The implemented code is available on GitHub portal of our lab at: https:// github.com/pcdslab/ASD-SAENet."

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

No

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

No

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

No

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

No — data availability statement reports no new datasets or code release. | quote: "No datasets were generated or analysed during the current study."

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

No — no code repository or participant list link appears in the text.

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

Partly — data availability statement says data are in the article/supplementary material and further inquiries can be directed to corresponding authors; no explicit code repository or participant ID list link. | quote: "The original contributions presented in this study are included in the article/supplementary material, further inquiries can be directed to the corresponding authors."

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

No — no code repository or participant list link found in the text.

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

Yes — participant indices uploaded to ABIDE and analysis code shared on GitHub. | quote: "All methods and data types generated to produce the ﬁgures will be made available through Github, https://github.
com/torreselizabeth/Frontiers-Paper."

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

Partly — the general CPM toolbox (BioImage Suite, MATLAB) is publicly available, but no study-specific participant ID list or analysis-code repository is given.

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

Yes — FC matrices, generated networks and all analysis code publicly deposited on GitHub. | quote: "Functional connectivity matrices and networks generated in our study, and all original codes are deposited  on GitHub and are publically available at https://​github.​com/​asama​llab/​Curva​ture-​FCN-​ASD as of the date of  publication."

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

No — no code repository or participant list link found in the text.

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

No — no study-specific code repository or participant list link found (only a general TDA library, sklearn-tda, is cited).

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

No — no code repository or participant list link found in the text.

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

No — no code repository or participant list link found in the text.

#### CL8 ABIDE relation of this paper

**Question.** CL8 ABIDE relation of this paper: uses-data | describes-release | mentions

*74 of 74 included studies charted.*

**S-001** — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II — 2017 (`local_b363d94a`)

describes-release | quote: "a new multi-site open data resource containing 1,044 independent datasets (ASD N = 487; Controls N = 557)"

**S-004** — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things — 2023 (`local_ad2b6012`)

uses-data | quote: "Collected dataset was organized in three groups:"

**S-007** — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults — 2021 (`local_04f9ab5b`)

uses-data | quote: "The secondary cohort was a subset of the ABIDE database consisting of 58 HFASD (25.4[7.8] years, 37.9% female) and 51 typically developing controls (24.4[6.7] years, 39.2% female)."

**S-008** — Towards robust and replicable sex differences in the intrinsic brain function of autism — 2021 (`local_62f73884`)

uses-data | quote: "The final ABIDE I and II dataset of N = 1019 included N = 82 females with autism, N = 362 males with autism, N = 166 neurotypical females (NT F), and N = 409 neurotypical males (NT M), aggregated across 13 sites."

**S-011** — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging — 2022 (`local_748c6bc3`)

uses-data | quote: "We examined resting-state functional MRI (rs-fMRI) and cortical thickness data from both waves of the openly shared ABIDE initiative (ABIDE I and II; http://fcon_1000.projects.nitrc. org/indi/abide) [29,30] and the HBN dataset [26], releases 1–8 collected between June 2017 and January 2020."

**S-012** — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder — 2019 (`local_0dbea86a`)

uses-data | quote: "ABIDE I is composed of 573 individuals with TD and 539 individuals with ASD (totaling 1 112 subjects). ABIDE II is composed of 593 individuals with TD and 521 individuals with ASD (totaling 1 114 subjects)."

**S-014** — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder — 2024 (`local_96f7c89f`)

uses-data | quote: "We use rs-fMRI and demographic data from ABIDE I [11], the first phase of ABIDE, with 505 autistic individuals and 530 Typical Controls (TCs)."

**S-029** — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example — 2016 (`local_f02fbc88`)

uses-data | quote: "The inputs to the classification pipeline are the 77 ASD and 77 TD connectivity matrices (hence 154 data samples in total), where each connectivity matrix consists of 19,900 features."

**S-032** — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism — 2016 (`local_bfdf942b`)

uses-data | quote: "This dataset is comprised of resting state fMRI and T1-weighted structural MRI scans from 1112 subjects, including patients with autism and healthy controls. ABIDE participant data was col- lected at 17 different institutions in North America and Europe."

**S-041** — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database — 2016 (`local_f07317a7`)

uses-data | quote: "We used resting state fMRI data of 458 subjects with ASD and 517 TDCs (see Table 1 for additional demographic information) among 1112 datasets from the ABIDE datasets"

**S-043** — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder — 2018 (`local_307f3aad`)

uses-data | quote: "extracted from the Autism Brain Imaging Data Exchange (ABIDE) II"

**S-053** — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification — 2021 (`local_0c61e485`)

uses-data | quote: "We experimentally compared GAT2 model’s performance on the  ABIDE I database from 1035 subjects"

**S-054** — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network — 2021 (`local_0709116d`)

uses-data | quote: "we used ABIDE-I data processed through the Connectome Computation System (CCS) (Craddock et al., 2013)"

**S-058** — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study — 2019 (`local_7c21219e`)

uses-data | quote: "We evaluate our proposed model on the publicly available ABIDE dataset to demonstrate the capability of our model to classify Autism Spectrum Disorder (ASD) from resting-state fMRI data."

**S-059** — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI — 2022 (`local_65679dfd`)

uses-data | quote: "The proposed MGRL is evaluated on 184 subjects from the public Autism Brain Imaging Data Exchange (ABIDE) database with rs-fMRI scans."

**S-066** — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data — 2024 (`local_6fb7c550`)

uses-data | quote: "We apply DeepASD to the benchmarking Autism Brain Imaging Data Exchange (ABIDE) data with four modalities."

**S-067** — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning — 2023 (`local_9829a18a`)

uses-data | quote: "We use pre-processed rs-fMRI data collected from the publicly available ABIDE1 dataset [34]."

**S-074** — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification — 2023 (`local_d76b09c5`)

uses-data | quote: "Our framework utilizes resting-state functional mag-
netic resonance imaging data from the ABIDE I dataset, comprising 406 ASD and 476 typical control (TC) subjects."

**S-098** — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning — 2021 (`local_1ee6bb17`)

uses-data | quote: "Resting-state fMRI data from 850 subjects in ABIDE I with an ASD DSM-IV-TR diagnosis (n = 355) and the corresponding HCs (n = 495) from the same sites were used in this study"

**S-006** — 3D Convolutional Neural Networks for Classification of Functional Connectomes — 2018 (`local_7623d661`)

uses-data

**S-010** — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning — 2022 (`local_afcc5b8c`)

uses-data

**S-020** — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results — 2020 (`local_c0ef18d3`)

uses-data

**S-022** — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network — 2020 (`local_b72b2fbd`)

uses-data

**S-023** — A general prediction model for the detection of ADHD and Autism using structural and functional MRI — 2018 (`local_0a18ed38`)

uses-data

**S-025** — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes — 2018 (`local_2983df5d`)

uses-data

**S-026** — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism — 2013 (`local_8a1f1b25`)

uses-data

**S-027** — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster — 2018 (`local_85ac52be`)

uses-data

**S-030** — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks — 2020 (`local_97b1be33`)

uses-data

**S-033** — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification — 2019 (`local_bb07b369`)

uses-data

**S-034** — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification — 2019 (`local_e610c0fe`)

uses-data | quote: "We present our results on the Autism
Brain Imaging Data Exchange (ABIDE) dataset [4]"

**S-039** — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism — 2022 (`local_c0914f68`)

uses-data | quote: "Autism Brain 
Imaging Data Exchange, ABIDE-I and ABIDE-II (21) 
http://fcon_1000.projects.nitrc.org/indi/abide/"

**S-049** — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning — 2024 (`local_57c41fd4`)

uses-data | quote: "Validation on two datasets, ADNI and ABIDE, demonstrates that DGCL surpasses traditional methods and other deep
learning models in predicting disease development stages."

**S-052** — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas — 2020 (`local_f732b266`)

uses-data | quote: "our study was carried out on the heterogeneous 
rs-fMRI data from ABIDE."

**S-060** — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model — 2021 (`local_c8a23e0a`)

uses-data | quote: "We ran our study on the Autism Brain Imaging Data Exchange
(ABIDE) (Di Martino et al., 2014)"

**S-075** — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning — 2018 (`local_486d7d2c`)

uses-data | quote: "Four hundred and ﬁfty-four subjects with complete phenotypic
data were selected from the Autism Brain Imaging Data
Exchange (ABIDE) database"

**S-077** — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation — 2023 (`local_4a3d6782`)

uses-data | quote: "The Autism Brain Imaging Data Ex-
change (ABIDE)1 [39] initiative aggregates resting-state
functional magnetic resonance imaging (rs-fMRI) and phe-
notypic data of 1112 subjects"

**S-002** — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example — 2016 (`local_7fdaac96`)

uses-data | quote: "an application to the Autism Brain Imaging Data Exchange (ABIDE) database, a large (N=871) multi-site autism dataset."

**S-019** — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease — 2018 (`local_e9fef0b1`)

uses-data | quote: "The ABIDE database (Di Martino et al., 2014) aggregates data from diﬀerent international acquisition sites and openly shares neuroimaging (functional MRI) and phenotypic data of 1112 subjects"

**S-021** — Multisite functional connectivity MRI classification of autism: ABIDE results — 2013 (`local_1cbc0566`)

uses-data | quote: "ABIDE consists of 1112 datasets comprised of 539 autism and 573 typically developing individuals (Di Marti"

**S-024** — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks — 2017 (`local_87840d2a`)

uses-data | quote: "we demonstrate the model performance on the functional connectivity graphs of 871 subjects from the challenging Autism Brain Imaging Data Exchange (ABIDE) database"

**S-036** — Single Volume Image Generator and Deep Learning-Based ASD Classification — 2020 (`local_9e370311`)

uses-data | quote: "The present study was carried out using fMRI data from the ABIDE1, which is a particularly complex dataset due to its heterogeneity"

**S-038** — Reorganization of functionally connected brain subnetworks in high-functioning autism — 2015 (`local_4a257bf0`)

uses-data | quote: "Additional 27 individuals with ASD from the ABIDE resting-state database were included to  test the reproducibility of the results."

**S-044** — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model — 2022 (`local_44b7e3b7`)

uses-data | quote: "Speciﬁcally, the 507 subjects included 209 subjects with ASD and 298 well-matched health controls across 14 sites from the Autism Brain Imaging Data Exchange (ABIDE)."

**S-045** — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder — 2017 (`local_013df539`)

uses-data | quote: "Anatomical and functional data from fifty-five subjects with ASD (12.7 ± 2.4 y/o) and 55 age- matched (14.1 ± 3.1 y/o) healthy controls were accessed through the NITRC database and the ABIDE project."

**S-047** — Motor noise is rich signal in autism research and pharmacological treatments — 2016 (`local_af69918d`)

uses-data | quote: "These included individuals with  autism spectrum disorders (ASD) and healthy-controls in shared data from the Autism Brain Imaging  Data Exchange (ABIDE) and the Attention-Deficit Hyperactivity Disorder (ADHD-200) databases."

**S-055** — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder — 2021 (`local_19021604`)

uses-data | quote: "In this study, we consider the ABIDE I preprocessed dataset (Di Martino
et al., 2014; Craddock et al., 2013)."

**S-056** — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING — 2021 (`local_33bed9bf`)

uses-data | quote: "The results achieved using CNN models namely  VGG-16 and ResNet-50 are 63.4% and 87.0% accuracy, respectively."

**S-062** — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning — 2019 (`local_81234492`)

uses-data | quote: "We analyzed the preprocessed data available on the ABIDE preprocessed homepage"

**S-064** — Deep learning-based feature selection for detection of autism spectrum disorder — 2025 (`local_730ab177`)

uses-data | quote: "The rs-fMRI data used in this study were sourced from the ABIDE I dataset, comprising 505 autistic individuals and 530 typical controls (TCs)."

**S-069** — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images — 2021 (`local_7424ae8d`)

uses-data | quote: "Within the study's scope, ASD and healthy individuals were distinguished on 871 samples obtained from the ABIDE I data set."

**S-071** — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study — 2023 (`local_62eceeaf`)

uses-data | quote: "The data used in the current study were provided by ABIDE I"

**S-072** — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning — 2017 (`local_88791905`)

uses-data | quote: "The dataset analyzed in the study is the Autism Brain Imaging Data Exchange (ABIDE)[?], a large, publicly available dataset of rsfMRI acquisitions of subjects diagnosed with ASD and healthy controls."

**S-076** — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder — 2023 (`local_696781dc`)

uses-data | quote: "This paper carries out research on the challenging public ABIDE I dataset [31]"

**S-090** — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data — 2025 (`local_3a3f7f6a`)

uses-data | quote: "we conducted the experiment on the publicly available ABIDE-I
dataset"

**S-091** — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database — 2019 (`local_6a54db71`)

uses-data | quote: "we applied information from a 
large-scale dataset, the Autism Brain Imaging Data Exchange (ABIDE), to clinical applications."

**S-005** — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset — 2021 (`local_904dfa27`)

uses-data | quote: "Resting-state functional MRI (rsfMRI) data covering 2,156 participants was initially obtained from the ABIDE I (17 sites, ASD/HC: 539/573, 7-64 years) and ABIDE II (19 sites, ASD/HC: 487/557, 5-64 years) databases"

**S-009** — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes — 2020 (`local_d46bcf61`)

uses-data | quote: "DSM-IV-TR diagnosed Asperger’s disorder (n = 79), pervasive developmental disorder-not otherwise specified [PDD-NOS] (n = 58) and Autistic disorder (n = 92) from ABIDE II were used as discovery cohort, and ABIDE I (n = 400) was used for replication."

**S-015** — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder — 2022 (`local_a8b1e837`)

uses-data | quote: "We generated voxel-wise maps of fALFF and ReHo for a total of 1983 subjects from the ABIDE I and ABIDE II datasets (ASD = 916, CTL = 1067"

**S-016** — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders — 2024 (`local_45051796`)

uses-data | quote: "we obtained a final sample of 1383 subjects (680 ASD and 703 TD) from 35 sites."

**S-028** — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data — 2021 (`local_8e16e9b1`)

uses-data | quote: "This dataset consists 1,035 rs-fMRI data with 505 ASD subject, and 530 healthy control subjects that are collected from 17 diﬀerent sites."

**S-063** — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks — 2023 (`local_e623bee8`)

uses-data | quote: "The 539 subjects with ASD and the 573 controls were split 70/15/15 into training, validation and test sets."

**S-070** — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification — 2022 (`local_fe9d4dc4`)

uses-data | quote: "The dataset brings together 1,112 subjects (539 ASD patients and 573 TCs) from 17 sites around worldwide"

**S-078** — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder — 2017 (`local_ef705029`)

uses-data | quote: "The data set was collected at the University of Michigan, one of the ABIDE data collection sites"

**S-080** — Contracted functional connectivity profiles in autism — 2024 (`local_30f8d927`)

uses-data

**S-081** — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset — 2017 (`local_ef4bae49`)

uses-data

**S-082** — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders — 2022 (`local_a7654842`)

uses-data

**S-086** — An empirical Bayes normalization method for connectivity metrics in resting state fMRI — 2015 (`local_1f08c2f9`)

uses-data

**S-088** — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository — 2020 (`local_c998fc64`)

uses-data

**S-092** — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder — 2019 (`local_6d8e3dc5`)

uses-data

**S-093** — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder — 2022 (`local_cb451a29`)

uses-data

**S-094** — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach — 2018 (`local_ddf52058`)

uses-data

**S-096** — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale — 2019 (`local_757f29e4`)

uses-data

**S-097** — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network — 2021 (`local_1a3d5c74`)

uses-data

**S-099** — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder — 2020 (`local_606b4b83`)

uses-data

---

## Appendix C: Critical Appraisal Results

### S-001 — Enhancing studies of the connectome in autism using the autism brain imaging data exchange II

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Partial |

**Overall Concern**: Low

#### Domain 2: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition reported | Yes |

**Overall Concern**: Low

#### Domain 3: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | Partial |
| CL7 Code/participant list available | Yes |

**Overall Concern**: Low

---

### S-004 — Analysis of Brain Imaging Data for the Detection of Early Age Autism Spectrum Disorder Using Transfer Learning Approaches for Internet of Things

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Partial |
| CL2 Motion/QC rule reported | No |

**Overall Concern**: High

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline reported | No |
| CL4 Atlas/parcellation reported | No |

**Overall Concern**: High

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source reported | No |

**Overall Concern**: High

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | No |
| CL6 Site handling | Partial |
| CL7 Code/participant list available | No |

**Overall Concern**: High

---

### S-007 — Thalamocortical connectivity is associated with autism symptoms in high-functioning adults with autism and typically developing adults

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Partial |
| CL2 Motion/QC rule reported | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline reported | Yes |
| CL4 Atlas/parcellation reported | N/A |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source reported | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | Yes |
| CL7 Code/participant list available | No |

**Overall Concern**: Low

---

### S-008 — Towards robust and replicable sex differences in the intrinsic brain function of autism

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline reported | Yes |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source reported | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | Yes |
| CL7 Code/participant list available | Partial |

**Overall Concern**: Low

---

### S-011 — Population heterogeneity in clinical cohorts affects the predictive accuracy of brain imaging

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline reported | Yes |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source reported | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | No |
| CL6 Site handling | Yes |
| CL7 Code/participant list available | Yes |

**Overall Concern**: High

---

### S-012 — Abnormal Cortico-Cerebellar Functional Connectivity in Autism Spectrum Disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline reported | Yes |
| CL4 Atlas/parcellation reported | No |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source reported | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | Yes |
| CL7 Code/participant list available | Partial |

**Overall Concern**: Low

---

### S-014 — MADE-for-ASD: A multi-atlas deep ensemble network for diagnosing Autism Spectrum Disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline reported | Yes |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source reported | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | No |
| CL6 Site handling | No |
| CL7 Code/participant list available | Yes |

**Overall Concern**: High

---

### S-029 — Promises, Pitfalls, and Basic Guidelines for Applying Machine Learning Classifiers to Psychiatric Imaging Data, with Autism as an Example

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline reported | Yes |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source reported | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | Yes |
| CL6 Site handling | Yes |
| CL7 Code/participant list available | Yes |

**Overall Concern**: Low

---

### S-032 — Using Functional or Structural Magnetic Resonance Images and Personal Characteristic Data to Identify ADHD and Autism

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline reported | Yes |
| CL4 Atlas/parcellation reported | No |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source reported | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | Yes |
| CL6 Site handling | Partial |
| CL7 Code/participant list available | Partial |

**Overall Concern**: Low

---

### S-041 — Abnormalities of Inter- and Intra-Hemispheric Functional Connectivity in Autism Spectrum Disorders: A Study Using the Autism Brain Imaging Data Exchange Database

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline reported | Yes |
| CL4 Atlas/parcellation reported | N/A |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source reported | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | No |
| CL7 Code/participant list available | No |

**Overall Concern**: Some

---

### S-043 — Aberrant Cerebellar–Cerebral Functional Connectivity in Children and Adolescents With Autism Spectrum Disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

---

### S-053 — GAT-LI: a graph attention network based learning and interpreting method for functional brain network classification

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: High

---

### S-054 — DarkASDNet: Classification of ASD on Functional MRI Using Deep Neural Network

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | No |

**Overall Concern**: High

---

### S-058 — A Hybrid 3DCNN and 3DC-LSTM Based Model for 4D Spatio-Temporal fMRI Data: An ABIDE Autism Classification Study

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | No |

**Overall Concern**: High

---

### S-059 — Multi-Scale Graph Representation Learning for Autism Identification With Functional MRI

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

---

### S-066 — DeepASD: a deep adversarial-regularized graph learning method for ASD diagnosis with multimodal data

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

---

### S-067 — EAG-RS: A Novel Explainability-Guided ROI-Selection Framework for ASD Diagnosis via Inter-Regional Relation Learning

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

---

### S-074 — Pretraining is All You Need: A Multi-Atlas Enhanced Transformer Framework for Autism Spectrum Disorder Classification

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

---

### S-098 — Improving Between-Group Effect Size for Multi-Site Functional Connectivity Data via Site-Wise De-Meaning

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

---

### S-006 — 3D Convolutional Neural Networks for Classification of Functional Connectomes

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

---

### S-010 — Reproducible neuroimaging features for diagnosis of autism spectrum disorder with machine learning

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

---

### S-020 — Multi-site fMRI analysis using privacy-preserving federated learning and domain adaptation: ABIDE results

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

---

### S-022 — Automated Detection of Autism Spectrum Disorder Using a Convolutional Neural Network

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

---

### S-023 — A general prediction model for the detection of ADHD and Autism using structural and functional MRI

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

---

### S-025 — A Novel Transfer Learning Approach to Enhance Deep Neural Network Classification of Brain Functional Connectomes

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

---

### S-026 — Underconnectivity of the superior temporal sulcus predicts emotion recognition deficits in autism

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

---

### S-027 — Classification of Autism Spectrum Disorder Using Random Support Vector Machine Cluster

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | No |

**Overall Concern**: High

---

### S-030 — Classifying Autism Spectrum Disorder Using the Temporal Statistics of Resting-State Functional MRI Data With 3D Convolutional Neural Networks

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

---

### S-033 — Topological Properties of Resting-State fMRI Functional Networks Improve Machine Learning-Based Autism Classification

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| Domain rating | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Domain rating | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| Domain rating | Partial |

**Overall Concern**: Some

---

### S-034 — Bootstrapping Graph Convolutional Neural Networks for Autism Spectrum Disorder Classification

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported (inclusion/exclusion rules and resulting N by diagnosis)? | Partial |
| CL2 Motion/QC rule reported (metric and threshold)? | No |

**Overall Concern**: High

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Partial |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition reported? | No |

**Overall Concern**: High

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | No |
| CL6 Site handling reported? | No |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: High

---

### S-039 — Connectome-wide Mega-analysis Reveals Robust Patterns of Atypical Functional Connectivity in Autism

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Partial |
| CL2 Motion/QC rule reported? | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | No |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition reported? | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | N/A |
| CL6 Site handling reported? | Yes |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: Some

---

### S-049 — A New Brain Network Construction Paradigm for Brain Disorder via Diffusion-Based Graph Contrastive Learning

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | No |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: High

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Partial |
| CL4 Atlas/parcellation reported? | Partial |

**Overall Concern**: High

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition reported? | No |

**Overall Concern**: High

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | No |
| CL6 Site handling reported? | No |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: High

---

### S-052 — Attentional Connectivity-based Prediction of Autism Using Heterogeneous rs-fMRI Data from CC200 Atlas

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Partial |
| CL2 Motion/QC rule reported? | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Partial |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition reported? | No |

**Overall Concern**: High

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | No |
| CL6 Site handling reported? | Partial |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: High

---

### S-060 — Large-Scale Brain Functional Network Integration for Discrimination of Autism Using a 3-D Deep Learning Model

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Partial |
| CL4 Atlas/parcellation reported? | Partial |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition reported? | Partial |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | No |
| CL6 Site handling reported? | N/A |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: High

---

### S-075 — Investigating the Correspondence of Clinical Diagnostic Grouping With Underlying Neurobiological and Phenotypic Clusters Using Unsupervised Machine Learning

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | No |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition reported? | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | N/A |
| CL6 Site handling reported? | No |
| CL7 Code and/or participant list available? | Partial |

**Overall Concern**: Some

---

### S-077 — Classification of Developmental and Brain Disorders via Graph Convolutional Aggregation

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Partial |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Partial |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition reported? | No |

**Overall Concern**: High

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | No |
| CL6 Site handling reported? | Partial |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: High

---

### S-002 — Deriving reproducible biomarkers from multi-site resting-state data: An Autism-based example

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | Yes |
| CL6 Site handling reported? | Yes |
| CL7 Code/participant list available? | Partial |

**Overall Concern**: Low

---

### S-019 — Disease prediction using graph convolutional networks: Application to Autism Spectrum Disorder and Alzheimer's disease

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | Partial |
| CL6 Site handling reported? | Partial |
| CL7 Code/participant list available? | Yes |

**Overall Concern**: Some

---

### S-021 — Multisite functional connectivity MRI classification of autism: ABIDE results

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Partial |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | Unclear |
| CL6 Site handling reported? | Yes |
| CL7 Code/participant list available? | No |

**Overall Concern**: Some

---

### S-024 — Distance Metric Learning Using Graph Convolutional Networks: Application to Functional Brain Networks

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | No |
| CL6 Site handling reported? | Partial |
| CL7 Code/participant list available? | Yes |

**Overall Concern**: Some

---

### S-036 — Single Volume Image Generator and Deep Learning-Based ASD Classification

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | No |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | No |
| CL6 Site handling reported? | Partial |
| CL7 Code/participant list available? | No |

**Overall Concern**: High

---

### S-038 — Reorganization of functionally connected brain subnetworks in high-functioning autism

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Partial |
| CL4 Atlas/parcellation reported? | No |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | N/A |
| CL6 Site handling reported? | No |
| CL7 Code/participant list available? | Yes |

**Overall Concern**: Low

---

### S-044 — Reconfiguration of Brain Network Dynamics in Autism Spectrum Disorder Based on Hidden Markov Model

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | N/A |
| CL6 Site handling reported? | Yes |
| CL7 Code/participant list available? | No |

**Overall Concern**: Low

---

### S-045 — Temporal fractal analysis of the rs-BOLD signal identifies brain abnormalities in autism spectrum disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Partial |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | N/A |
| CL6 Site handling reported? | No |
| CL7 Code/participant list available? | No |

**Overall Concern**: Some

---

### S-047 — Motor noise is rich signal in autism research and pharmacological treatments

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Partial |
| CL4 Atlas/parcellation reported? | No |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | N/A |
| CL6 Site handling reported? | Yes |
| CL7 Code/participant list available? | No |

**Overall Concern**: Low

---

### S-055 — Combining Anatomical and Functional Networks for Neuropathology Identification: A Case Study on Autism Spectrum Disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | Yes |
| CL6 Site handling reported? | No |
| CL7 Code/participant list available? | No |

**Overall Concern**: Some

---

### S-056 — FUNCTIONAL MAGNETIC RESONANCE IMAGING FOR AUTISM SPECTRUM DISORDER DETECTION USING DEEP LEARNING

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 | Partial |
| CL2 | No |

**Overall Concern**: High

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 | No |
| CL4 | No |

**Overall Concern**: High

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| diagnosis source | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 | No |
| CL6 | No |
| CL7 | No |

**Overall Concern**: High

---

### S-062 — Evaluation of Altered Functional Connections in Male Children With Autism Spectrum Disorders on Multiple-Site Data Optimized With Machine Learning

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 | Yes |
| CL2 | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 | Yes |
| CL4 | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| diagnosis source | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 | Partial |
| CL6 | Yes |
| CL7 | No |

**Overall Concern**: Some

---

### S-064 — Deep learning-based feature selection for detection of autism spectrum disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 | Partial |
| CL2 | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 | Yes |
| CL4 | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| diagnosis source | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 | No |
| CL6 | No |
| CL7 | No |

**Overall Concern**: High

---

### S-069 — Deep Learning Methods for Autism Spectrum Disorder Diagnosis Based on fMRI Images

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 | Partial |
| CL2 | No |

**Overall Concern**: High

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 | No |
| CL4 | Yes |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| diagnosis source | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 | No |
| CL6 | No |
| CL7 | No |

**Overall Concern**: High

---

### S-071 — Domain Adaptation via Low Rank and Class Discriminative Representation for Autism Spectrum Disorder Identification: A Multi-Site fMRI Study

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 | Partial |
| CL2 | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 | Yes |
| CL4 | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| diagnosis source | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 | No |
| CL6 | Yes |
| CL7 | No |

**Overall Concern**: Some

---

### S-072 — Autism Classification Using Brain Functional Connectivity Dynamics and Machine Learning

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 | Partial |
| CL2 | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 | Partial |
| CL4 | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| diagnosis source | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 | No |
| CL6 | Yes |
| CL7 | No |

**Overall Concern**: Some

---

### S-076 — A heterogeneous graph convolutional attention network method for classification of autism spectrum disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 | Partial |
| CL2 | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 | Yes |
| CL4 | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| diagnosis source | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 | No |
| CL6 | Partial |
| CL7 | No |

**Overall Concern**: High

---

### S-090 — Hierarchical feature extraction on functional brain networks for autism spectrum disorder identification with resting-state fMRI data

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 | Partial |
| CL2 | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 | Yes |
| CL4 | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| diagnosis source | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 | No |
| CL6 | No |
| CL7 | Partial |

**Overall Concern**: Some

---

### S-091 — Deriving and validating biomarkers associated with autism spectrum disorders from a large-scale resting-state database

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 | Yes |
| CL2 | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 | Yes |
| CL4 | Partial |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| diagnosis source | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 | Partial |
| CL6 | No |
| CL7 | Partial |

**Overall Concern**: Some

---

### S-005 — Alterations in Connectome Dynamics in Autism Spectrum Disorder: A Harmonized Mega- and Meta-analysis Study Using the Autism Brain Imaging Data Exchange Dataset

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported (inclusion/exclusion rules and resulting N by diagnosis)? | Yes |
| CL2 Motion/QC rule reported (metric and threshold)? | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | Yes |
| CL6 Site handling reported? | Yes |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: Low

---

### S-009 — Common and unique multimodal covarying patterns in autism spectrum disorder subtypes

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | No |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | Partial |
| CL6 Site handling reported? | Yes |
| CL7 Code and/or participant list available? | Yes |

**Overall Concern**: Some

---

### S-015 — Association between resting-state functional brain connectivity and gene expression is altered in autism spectrum disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | N/A |
| CL6 Site handling reported? | Yes |
| CL7 Code and/or participant list available? | Yes |

**Overall Concern**: Low

---

### S-016 — Deep learning based joint fusion approach to exploit anatomical and functional brain information in autism spectrum disorders

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | Partial |
| CL6 Site handling reported? | Yes |
| CL7 Code and/or participant list available? | Yes |

**Overall Concern**: High

---

### S-028 — ASD-SAENet: A Sparse Autoencoder, and Deep-Neural Network Model for Detecting Autism Spectrum Disorder (ASD) Using fMRI Data

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Partial |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | Unclear |
| CL6 Site handling reported? | Partial |
| CL7 Code and/or participant list available? | Yes |

**Overall Concern**: Some

---

### S-063 — Evaluation of Augmentation Methods in Classifying Autism Spectrum Disorders from fMRI Data with 3D Convolutional Neural Networks

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Partial |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | No |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | Unclear |
| CL6 Site handling reported? | No |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: High

---

### S-070 — CNNG: A Convolutional Neural Networks With Gated Recurrent Units for Autism Spectrum Disorder Classification

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Partial |
| CL2 Motion/QC rule reported? | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | No |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | No |
| CL6 Site handling reported? | No |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: High

---

### S-078 — Latent and Abnormal Functional Connectivity Circuits in Autism Spectrum Disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported? | Yes |
| CL2 Motion/QC rule reported? | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported? | Yes |
| CL4 Atlas/parcellation reported? | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control reported? | No |
| CL6 Site handling reported? | N/A |
| CL7 Code and/or participant list available? | No |

**Overall Concern**: High

---

### S-080 — Contracted functional connectivity profiles in autism

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Partial |
| CL4 Atlas/parcellation reported | Partial |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Yes |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | Yes |
| CL7 Code/participant list available | No |

**Overall Concern**: Some

---

### S-081 — Developing predictive imaging biomarkers using whole-brain classifiers: Application to the ABIDE I dataset

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Partial |
| CL2 Motion/QC rule reported | No |

**Overall Concern**: High

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Partial |
| CL4 Atlas/parcellation reported | No |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | No |
| CL6 Site handling | No |
| CL7 Code/participant list available | No |

**Overall Concern**: High

---

### S-082 — Attenuated effective connectivity of large-scale brain networks in children with autism spectrum disorders

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Partial |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Yes |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | N/A |
| CL7 Code/participant list available | Partial |

**Overall Concern**: Some

---

### S-086 — An empirical Bayes normalization method for connectivity metrics in resting state fMRI

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Partial |
| CL2 Motion/QC rule reported | Partial |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Partial |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | N/A |
| CL7 Code/participant list available | No |

**Overall Concern**: Some

---

### S-088 — Age-Dependent Statistical Changes of Involuntary Head Motion Signatures Across Autism and Controls of the ABIDE Repository

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | No |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | No |
| CL4 Atlas/parcellation reported | N/A |

**Overall Concern**: Some

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | No |
| CL7 Code/participant list available | Yes |

**Overall Concern**: Low

---

### S-092 — Building functional connectivity neuromarkers of behavioral self-regulation across children with and without Autism Spectrum Disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Partial |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Partial |

**Overall Concern**: Low

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | Yes |
| CL6 Site handling | Partial |
| CL7 Code/participant list available | Partial |

**Overall Concern**: Low

---

### S-093 — Graph Ricci curvatures reveal atypical functional connectivity in autism spectrum disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Yes |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | N/A |
| CL6 Site handling | Partial |
| CL7 Code/participant list available | Yes |

**Overall Concern**: Low

---

### S-094 — Imbalance of Functional Connectivity and Temporal Entropy in Resting-State Networks in Autism Spectrum Disorder: A Machine Learning Approach

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | Yes |

**Overall Concern**: Low

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Partial |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | Partial |
| CL6 Site handling | No |
| CL7 Code/participant list available | No |

**Overall Concern**: Some

---

### S-096 — Autism Classification Using Topological Features and Deep Learning: A Cautionary Tale

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Partial |
| CL2 Motion/QC rule reported | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Partial |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | Partial |
| CL6 Site handling | No |
| CL7 Code/participant list available | No |

**Overall Concern**: Some

---

### S-097 — Autism Spectrum Disorder Detection Based on Wavelet Transform of BOLD fMRI Signals Using Pre-trained Convolution Neural Network

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Partial |
| CL2 Motion/QC rule reported | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Yes |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | No |
| CL6 Site handling | No |
| CL7 Code/participant list available | No |

**Overall Concern**: High

---

### S-099 — A Three-Stage Teacher, Student Neural Networks and Sequential Feed Forward Selection-Based Feature Selection Approach for the Classification of Autism Spectrum Disorder

#### Domain 1: Participants and cohort definition (PROBAST domain 1 / checklist CL1-CL2)

| Item | Rating |
|------|--------|
| CL1 Cohort definition reported | Yes |
| CL2 Motion/QC rule reported | No |

**Overall Concern**: Some

#### Domain 2: Predictors and features: preprocessing and parcellation (PROBAST domain 2 / CL3-CL4)

| Item | Rating |
|------|--------|
| CL3 Preprocessing pipeline and version reported | Partial |
| CL4 Atlas/parcellation reported | Yes |

**Overall Concern**: Low

#### Domain 3: Outcome: diagnostic labels and their source (PROBAST domain 3)

| Item | Rating |
|------|--------|
| Diagnosis source and label definition | Unclear |

**Overall Concern**: Some

#### Domain 4: Analysis: validation, leakage and site handling (PROBAST domain 4 / CL5-CL7)

| Item | Rating |
|------|--------|
| CL5 Leakage control | No |
| CL6 Site handling | No |
| CL7 Code/participant list available | No |

**Overall Concern**: High

---


---

## Provenance — How This Analysis Was Produced

*This section is auto-generated and exposes which phases were iterative vs zero-shot, the configuration that drove the run, the full plan-iteration history, the search trail, and per-invocation LLM telemetry. Source-grounded outputs (synthesis, evidence spans) are validated separately — see the Source Grounding section.*

### Run Configuration

| Field | Value |
|-------|-------|
| Started at | 2026-10-15T19:37:21.681948+00:00 |
| Model | `Charting: Claude Sonnet sub-agents (8 batches). Merge/verification/synthesis: Claude Opus 5.5 (claude-opus-5-5).` |
| Package version | `synthscholar 0.0.11 (da23314)` |
| Review ID | `review_local_20261015_abide_rsfmri` |
| CLI invocation | `python phase3/s3_assemble.py && update_provenance.py && export_review.py review.json --formats md ttl json` |

**Environment variables (presence only — values not stored):**

| Variable | Present |
|----------|---------|
| `OPENROUTER_API_KEY` | — |

### Iterative vs Zero-Shot Phases

**Zero-shot** = single LLM call, no loop. **Iterative** phases regenerate against feedback, fall back through providers, expand seeds, or shard-and-merge corpora.

| Phase | Mode | Calls |
|-------|------|-------|
| integrity check, quote re-verification, merge, synthesis | _validated_against_source_ | 1 |
| screening+charting+appraisal (full text) | zero_shot (per-target) | 8 |

### Search Iteration Trail

| # | Kind | Database | Query | Seeds | New PMIDs | Cumulative | Duration (ms) |
|---|------|----------|-------|-------|-----------|------------|---------------|
| 1 | initial_query | OpenAlex | `https://api.openalex.org/works?filter=cites:W2167868121,titl` | 0 | 0 | 598 | 0 |
| 2 | initial_query | OpenAlex | `https://api.openalex.org/works?filter=cites:W2590651237,titl` | 0 | 0 | 174 | 0 |
| 3 | initial_query | OpenAlex | `https://api.openalex.org/works?filter=cites:W2522924024,titl` | 0 | 0 | 220 | 0 |
| 4 | initial_query | Other sources | `release descriptors added by DOI: 10.1038/mp.2013.78, 10.103` | 0 | 0 | 2 | 0 |

### LLM Invocation Summary

**9** total invocations · **0** input tokens · **0** output tokens · **0.0s** cumulative LLM time

| # | Step | Mode | Model | Tokens (in/out) | Reqs | Tools | Target | OK |
|---|------|------|-------|-----------------|------|-------|--------|----|
| 1 | screening+charting+appraisal (full text) | zero_shot | `Claude Sonnet` | 0/0 | 0 | batches/charting_1_records.json (12 arti | batch-1 | ✓ |
| 2 | screening+charting+appraisal (full text) | zero_shot | `Claude Sonnet` | 0/0 | 0 | batches/charting_2_records.json (12 arti | batch-2 | ✓ |
| 3 | screening+charting+appraisal (full text) | zero_shot | `Claude Sonnet` | 0/0 | 0 | batches/charting_3_records.json (12 arti | batch-3 | ✓ |
| 4 | screening+charting+appraisal (full text) | zero_shot | `Claude Sonnet` | 0/0 | 0 | batches/charting_4_records.json (12 arti | batch-4 | ✓ |
| 5 | screening+charting+appraisal (full text) | zero_shot | `Claude Sonnet` | 0/0 | 0 | batches/charting_5_records.json (13 arti | batch-5 | ✓ |
| 6 | screening+charting+appraisal (full text) | zero_shot | `Claude Sonnet` | 0/0 | 0 | batches/charting_6_records.json (12 arti | batch-6 | ✓ |
| 7 | screening+charting+appraisal (full text) | zero_shot | `Claude Sonnet` | 0/0 | 0 | batches/charting_7_records.json (13 arti | batch-7 | ✓ |
| 8 | screening+charting+appraisal (full text) | zero_shot | `Claude Sonnet` | 0/0 | 0 | batches/charting_8_records.json (13 arti | batch-8 | ✓ |
| 9 | integrity check, quote re-verification, merge, synthesis | validated_against_source | `claude-opus-5-5` | 0/0 | 0 | 1743 quotes checked, 8 dropped |  | ✓ |

*Full prompts and one-line tool-call summaries are persisted in JSON exports and (when `--pg-dsn` + migration 005 are set) in the `review_telemetry` Postgres table.*


---
*Generated by SynthScholar on 2026-10-15. AI-assisted components should be verified before publication.*