"""Curated resource catalog (software, specifications, vocabularies, datasets, papers, training, skills).

Each entry is described for retrieval (what it does, when to use it, what it needs, what it does not do),
faceted by workflow step, modality, graph classes consumed/produced and EDAM terms (resolved by exact
label against data/vocab/EDAM.tsv; a label that does not resolve is an error), and marked as
executed / data_source / pointer for this experiment.

  uv run python code/resources_catalog.py --refresh-pins   # fetch commit SHA, license, language via gh api
  uv run python code/resources_catalog.py                  # build graph/resources.ttl from pinned data

Writes data/resources_pinned.json (with --refresh-pins) and graph/resources.ttl.
"""

import datetime as dt
import json
import subprocess
import sys

import pandas as pd
from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace, URIRef

from common import DATA, GRAPH, RESULTS, write_json

E = Namespace("urn:repronim:abide:")
SDO = Namespace("http://schema.org/")
CM = Namespace("https://codemeta.github.io/terms/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
NIDM = Namespace("http://purl.org/nidash/nidm#")
PINS = DATA / "resources_pinned.json"

STEPS = [
    "acquisition", "conversion_to_bids", "phenotype_assessment_schema", "containerized_execution",
    "provenance_capture", "preprocessing", "idp_extraction_to_nidm", "qc_to_nidm", "query_merge",
    "statistics_results", "data_source", "training", "agent_skills",
]

GH = "https://github.com/"
R = []


def res(rid, name, rtype, steps, desc, usage, usage_note, *, repo=None, url=None, modality=("MRI",), consumes=(), produces=(),
        inputs=(), outputs=(), ops=(), topics=(), audience=("neuroimaging researchers",), doi=None, openalex=None):
    """Register one resource."""
    R.append(dict(id=rid, name=name, type=rtype, steps=list(steps), description=desc, usage=usage, usage_note=usage_note,
                  repo=repo, url=url or (GH + repo if repo else None), modality=list(modality), consumes=list(consumes),
                  produces=list(produces), inputs=list(inputs), outputs=list(outputs), ops=list(ops), topics=list(topics),
                  audience=list(audience), doi=doi, openalex=openalex))


# ---- NIDM specifications, vocabularies, libraries ----
res("nidm-specs", "NIDM specifications", "Specification", ["provenance_capture", "statistics_results"],
    "The Neuroimaging Data Model: PROV-based models for neuroimaging. NIDM-Results (released) describes mass-univariate results such as fMRI statistic maps; NIDM-Experiment and NIDM-Workflows describe raw data and workflows. Use it to decide which classes and relations to emit when describing studies, acquisitions and results as a knowledge graph. It is a specification, not software that converts your data.",
    "pointer", "Defines the nidm: classes this graph uses (Acquisition, AcquisitionObject, DataElement, Derivative).",
    repo="incf-nidash/nidm-specs", produces=["nidm:Acquisition", "nidm:AcquisitionObject", "nidm:DataElement", "nidm:Derivative"],
    outputs=["Turtle", "JSON-LD"], topics=["Ontology and terminology", "Neurology"])
res("nidm-experiment", "NIDM-Experiment terms", "Vocabulary", ["provenance_capture", "phenotype_assessment_schema"],
    "Controlled terminology for describing neuroscience experiments, initially MRI studies, built from existing ontologies with new terms only where none exist; every term has a resolvable URL. Use it to annotate acquisitions and data elements with stable term IRIs. It is a vocabulary under construction, not a validator.",
    "pointer", "Source of nidm: term IRIs referenced in the graph.", repo="incf-nidash/nidm-experiment",
    produces=["nidm:DataElement"], outputs=["OWL format", "Turtle"], topics=["Ontology and terminology"])
res("nidm-experiment-cob", "NIDM-Experiment based on COB (NEC)", "Vocabulary", ["provenance_capture"],
    "Ongoing conversion of NIDM-Experiment from a PROV-based terminology to an ontology grounded in BFO and the Core Ontology for Biology and Biomedicine. Use when you need ontologically sound experiment terms. Under construction; terms may be missing.",
    "pointer", "Successor ontology for NIDM-E terms.", repo="incf-nidash/NIDM-Experiment-COB", outputs=["OWL format"], topics=["Ontology and terminology"])
res("nidm-terms", "NIDM-Terms", "Vocabulary", ["phenotype_assessment_schema", "query_merge"],
    "Collaborative terminology work from the NIDM FAIR descriptors project (NIH RF1 MH120021): shared, defined terms for assessment and imaging variables so datasets can be queried together. Use it to find or propose a term for a variable before inventing a local one. Not a data converter.",
    "pointer", "Where variable-level isAbout terms come from or are proposed.", repo="NIDM-Terms/terms",
    consumes=["nidm:DataElement"], produces=["nidm:DataElement"], topics=["Ontology and terminology", "Data identity and mapping"])
res("pynidm", "PyNIDM", "SoftwareSourceCode", ["provenance_capture", "query_merge", "statistics_results"],
    "Python library and CLI for the Neuroimaging Data Model: bidsmri2nidm converts a BIDS dataset to NIDM, csv2nidm annotates tabular phenotype data with terms, and pynidm query runs SPARQL over NIDM files; it also has linear-regression and merge tools. Use it to build or query NIDM graphs from BIDS plus spreadsheets. Its in-memory query is slow on many files (the simple2 README warns it is too long beyond ~10 files).",
    "pointer", "Produced the BIDS and phenotype parts of the simple2 graphs (bidsmri2nidm + csv2nidm); not run here.",
    repo="incf-nidash/PyNIDM", consumes=["BIDS dataset", "phenotype table"], produces=["nidm:AcquisitionObject", "nidm:DataElement", "prov:Activity"],
    inputs=["CSV", "TSV", "nii"], outputs=["Turtle", "JSON-LD"], ops=["Conversion", "Query and retrieval", "Annotation"], topics=["Data submission, annotation and curation"])
res("nidmresults", "nidmresults", "SoftwareSourceCode", ["statistics_results"],
    "Python library to read and write NIDM-Results packs, the standard representation of mass-univariate (voxelwise) statistical results with their maps. Use it to load or produce results packs from SPM/FSL group analyses. It does not cover ROI or connectivity results like the ones in this experiment.",
    "pointer", "Results-level NIDM; our edgewise and classification results are not voxelwise maps.", repo="incf-nidash/nidmresults",
    produces=["ex:Result"], outputs=["Turtle"], topics=["Neurology"])
res("nidmresults-fsl", "NIDM-Results for FSL", "SoftwareSourceCode", ["statistics_results"],
    "Command-line exporter (nidmfsl) that turns an FSL FEAT directory into a NIDM-Results pack. Use it to share FSL task-fMRI results with provenance. Only for FEAT outputs.",
    "pointer", "Not applicable to resting-state connectivity here.", repo="incf-nidash/nidmresults-fsl", consumes=["FSL FEAT directory"], produces=["ex:Result"],
    outputs=["Turtle"], ops=["Conversion"])
res("bids-ld", "BIDS-LD", "Specification", ["conversion_to_bids", "provenance_capture"],
    "Linked-data (JSON-LD) context and terms for BIDS entities, so BIDS metadata can be read as RDF. Use it to map BIDS fields to IRIs. Repository has had no pushes since 2019.",
    "pointer", "Dormant; listed for completeness.", repo="incf-nidash/bids-ld", outputs=["JSON-LD"], topics=["Ontology and terminology"])

# ---- IDP / QC exporters to NIDM, BIDS apps ----
res("segstats_jsonld", "segstats_jsonld", "SoftwareSourceCode", ["idp_extraction_to_nidm"],
    "Exports FreeSurfer segmentation and parcellation statistics (aseg/aparc stats from mri_segstats) with provenance as JSON-LD and NIDM, mapping each measure to a common data element with anatomical isAbout terms. Use it to make FreeSurfer volumes queryable next to other tools. Needs a finished FreeSurfer subject directory; it does not run FreeSurfer.",
    "data_source", "Its FreeSurfer CDEs and outputs appear in the simple2 ABIDE graphs used here (fs: measures).",
    repo="ReproNim/segstats_jsonld", consumes=["FreeSurfer stats files"], produces=["nidm:DataElement", "ex:BrainVolume"],
    inputs=["TSV"], outputs=["JSON-LD", "Turtle"], ops=["Conversion"], topics=["Imaging", "Neurology"])
res("ants_seg_to_nidm", "ants_seg_to_nidm", "SoftwareSourceCode", ["idp_extraction_to_nidm"],
    "Exports ANTs-based structural segmentation volumes to NIDM, with a CDE file (ants_cde.ttl) that maps each ANTs measure to anatomy and units. Use it to add ANTs volumes to a NIDM dataset graph. Does not run ANTs.",
    "data_source", "ants_cde.ttl at a pinned commit was loaded to interpret ANTs volumes in the simple2 graphs.",
    repo="ReproNim/ants_seg_to_nidm", consumes=["ANTs segmentation outputs"], produces=["nidm:DataElement", "ex:BrainVolume"], outputs=["Turtle"], ops=["Conversion"])
res("fsl_seg_to_nidm", "fsl_seg_to_nidm", "SoftwareSourceCode", ["idp_extraction_to_nidm"],
    "Converts FSL FIRST (subcortical) and FAST (tissue) segmentation outputs to NIDM via fslsegstats2nidm, optionally appending them to a dataset's NIDM file; ships fsl_cde.ttl. Use it to add FSL volumes. Expects outputs of the ReproNim simple1 workflow.",
    "data_source", "fsl_cde.ttl at a pinned commit was loaded to interpret FSL volumes in the simple2 graphs.",
    repo="ReproNim/fsl_seg_to_nidm", consumes=["FSL FIRST/FAST outputs"], produces=["nidm:DataElement", "ex:BrainVolume"], inputs=["JSON"], outputs=["Turtle"], ops=["Conversion"])
res("stuff2nidm", "stuff2NIDM", "SoftwareSourceCode", ["qc_to_nidm", "idp_extraction_to_nidm"],
    "Worked recipe for adding any tool's results (e.g. fMRIPrep) to a NIDM graph: write results, a data dictionary and a tool description as three CSVs, then run pynidm csv2nidm. Use it when no dedicated exporter exists for your tool. It is a pattern with examples, not a converter for every tool.",
    "pointer", "The route to put this experiment's connectivity summaries into NIDM; not run here.", repo="ReproNim/stuff2NIDM",
    consumes=["results table", "data dictionary"], produces=["nidm:DataElement", "nidm:DerivativeObject"], inputs=["CSV"], outputs=["Turtle"], ops=["Conversion"])
res("freesurfer-nidm_bidsapp", "FreeSurfer NIDM BIDS App", "SoftwareSourceCode", ["containerized_execution", "idp_extraction_to_nidm"],
    "A BIDS App that runs only FreeSurfer 8.0.0 recon-all on T1w (and optional T2w) images and writes BIDS derivatives plus NIDM output with version tracking. Use it to produce FreeSurfer morphometry with provenance in one containerized step. It does not expose other FreeSurfer tools.",
    "pointer", "Would regenerate FreeSurfer volumes for ABIDE with NIDM output; not run here.", repo="ReproNim/freesurfer-nidm_bidsapp",
    consumes=["BIDS dataset"], produces=["ex:BrainVolume", "nidm:DerivativeObject"], inputs=["nii"], outputs=["Turtle"], ops=["Image analysis"], topics=["Imaging"])
res("ants-nidm_bidsapp", "ANTs NIDM BIDS App", "SoftwareSourceCode", ["containerized_execution", "idp_extraction_to_nidm"],
    "A BIDS App that segments a T1w image into about 100 labelled structures with multi-atlas joint label fusion (GPU registration via FireANTs) and writes per-structure volumes as CSV and NIDM Turtle. Use it for ANTs volumes that pool across studies. Needs a GPU for registration.",
    "pointer", "Would regenerate ANTs volumes with NIDM output; not run here.", repo="ReproNim/ants-nidm_bidsapp",
    consumes=["BIDS dataset"], produces=["ex:BrainVolume", "nidm:DerivativeObject"], inputs=["nii"], outputs=["CSV", "Turtle"], ops=["Image analysis"], topics=["Imaging"])
res("mriqc-nidm_bidsapp", "MRIQC NIDM BIDS App", "SoftwareSourceCode", ["containerized_execution", "qc_to_nidm"],
    "A BIDS App that runs MRIQC and converts its image-quality metrics to NIDM (Turtle or JSON-LD), optionally augmenting existing NIDM files. Use it to make QC metrics queryable alongside phenotype and IDPs. It does not make QC decisions.",
    "pointer", "QC metrics would complement the rater QC used to select cohorts here; not run.", repo="ReproNim/mriqc-nidm_bidsapp",
    consumes=["BIDS dataset"], produces=["nidm:DerivativeObject"], inputs=["nii", "JSON"], outputs=["Turtle", "JSON-LD"], ops=["Validation"], topics=["Imaging", "Quality affairs"])
res("simple2_bidsapp_babs", "simple2 BABS scripts", "SoftwareSourceCode", ["containerized_execution", "idp_extraction_to_nidm"],
    "Scripts that run the FreeSurfer, ANTs and MRIQC NIDM BIDS Apps on HPC with BABS and DataLad, site by site, on SIMPLE2-layout study datasets; validated end to end on the 38-subject ABIDE Caltech site. Use it to batch the NIDM BIDS Apps over a cohort on Slurm. Requires DataLad, BABS and container images.",
    "pointer", "The HPC route to regenerate simple2 IDPs; not run here.", repo="ReproNim/simple2_bidsapp_babs",
    consumes=["BIDS dataset"], produces=["ex:BrainVolume"], ops=["Image analysis"], audience=("neuroimaging researchers", "HPC users"))
res("openneuroderivatives-nidm", "OpenNeuroDerivatives-NIDM", "SoftwareSourceCode", ["idp_extraction_to_nidm", "query_merge"],
    "Experiments extracting NIDM descriptors for all OpenNeuroDerivatives datasets, starting with FreeSurfer outputs via segstats_jsonld, organised as DataLad/YODA datasets. Use it as a model for NIDM-ifying many derivative datasets at once.",
    "pointer", "Pattern for scaling the simple2 approach beyond ABIDE.", repo="ReproNim/OpenNeuroDerivatives-NIDM", produces=["ex:BrainVolume"], outputs=["Turtle"])
res("simple2_nidm_examples", "simple2 NIDM examples (ABIDE, ADHD200)", "Dataset", ["data_source", "query_merge"],
    "NIDM Turtle for ABIDE and ADHD200 built with bidsmri2nidm and csv2nidm (age, sex, diagnosis, FIQ/PIQ/VIQ) plus ANTs, FSL and FreeSurfer brain volumes, with example SPARQL queries (simple2_query.sparql, get_volumes.sparql). Use it as a ready-made, queryable phenotype + IDP graph for ABIDE. Volumes were computed by ReproNim, not re-derived here.",
    "data_source", "24 ABIDE site graphs loaded unmodified as named graphs; simple2_query.sparql executed unmodified; identity-joined to ABIDE Preprocessed.",
    repo="ReproNim/simple2_NIDM_examples", produces=["nidm:AcquisitionObject", "nidm:DataElement", "ex:BrainVolume"], outputs=["Turtle", "CSV"], ops=["Query and retrieval"])
res("fair_neuroimaging_with_nidm", "FAIR neuroimaging with NIDM and PyNIDM", "TrainingMaterial", ["training", "query_merge"],
    "Tutorial and paper materials (Zenodo 10.5281/zenodo.15850765) on producing a FAIR neuroimaging study with NIDM: recording study, acquisition, phenotype and derived data as a knowledge graph and querying it with PyNIDM. Use it to learn the NIDM workflow end to end.",
    "pointer", "Training counterpart of this experiment.", repo="ReproNim/FAIR_neuroimaging_with_NIDM", audience=("neuroimaging researchers", "students"), topics=["Data submission, annotation and curation"])

# ---- assessments ----
res("reproschema", "ReproSchema", "Specification", ["phenotype_assessment_schema"],
    "A schema for standardized survey and assessment data collection: items, activities and protocols as linked data with versioning, so questionnaires and their responses are harmonized across studies. Use it to define phenotype instruments once and reuse them. It defines forms and responses; it does not score or analyse them.",
    "pointer", "Would give ABIDE's phenotype instruments (ADOS, SRS, IQ) explicit, versioned definitions; not used here.", repo="ReproNim/reproschema",
    modality=("assessment",), produces=["nidm:DataElement"], outputs=["JSON-LD"], topics=["Data submission, annotation and curation"])
res("reproschema-py", "reproschema-py", "SoftwareSourceCode", ["phenotype_assessment_schema"],
    "Python library and CLI for ReproSchema: create, validate and convert protocols and activities (YAML-based authoring). Use it to validate an assessment schema or convert to and from other formats such as REDCap. Requires Python 3.10+.",
    "pointer", "", repo="ReproNim/reproschema-py", modality=("assessment",), inputs=["YAML"], outputs=["JSON-LD"], ops=["Validation", "Conversion"])
res("reproschema-library", "ReproSchema library", "Dataset", ["phenotype_assessment_schema"],
    "A library of reusable, form-based clinical, behavioural and neuropsychological assessments in ReproSchema (for example ASSQ, a screening checklist for autism spectrum characteristics). Use it to pick an existing instrument definition instead of writing your own.",
    "pointer", "Contains autism-related instruments relevant to ABIDE phenotypes.", repo="ReproNim/reproschema-library", modality=("assessment",), outputs=["JSON-LD"])
res("reproschema-ui", "ReproSchema UI", "SoftwareSourceCode", ["phenotype_assessment_schema", "acquisition"],
    "Web user interface that renders ReproSchema protocols and activities for participants to complete (text, numeric, audio, date and choice inputs). Use it to run a ReproSchema questionnaire in a browser.",
    "pointer", "", repo="ReproNim/reproschema-ui", modality=("assessment",), audience=("study coordinators", "participants"))

# ---- execution, containers, reproducibility ----
res("containers", "ReproNim containers", "Dataset", ["containerized_execution"],
    "A DataLad dataset of versioned Singularity/Apptainer images of popular neuroimaging tools, meant to be installed as a subdataset so data, code and exact environment stay linked (YODA). Use it to run a pinned tool version on HPC with datalad containers-run. Provides images, not workflows.",
    "pointer", "", repo="ReproNim/containers", audience=("neuroimaging researchers", "HPC users"))
res("neurodocker", "Neurodocker", "SoftwareSourceCode", ["containerized_execution"],
    "Command-line generator of Dockerfiles and Singularity recipes for neuroimaging software (FSL, FreeSurfer, ANTs, AFNI, conda environments and more), and a container minifier. Use it to build a reproducible image for a pipeline. Compatibility depends on the base image; check its build matrix.",
    "pointer", "", repo="ReproNim/neurodocker", audience=("neuroimaging researchers", "developers"), ops=["Formatting"], topics=["Software engineering"])
res("reproman", "ReproMan", "SoftwareSourceCode", ["containerized_execution", "provenance_capture"],
    "Tool to create and manage computing environments and run analyses on them (local, remote, cloud, HPC) while recording what was run. Use it to submit and track jobs with their environment. Linux and macOS only.",
    "pointer", "", repo="ReproNim/reproman", audience=("neuroimaging researchers", "HPC users"))
res("reprozip", "ReproZip (ReproNim fork)", "SoftwareSourceCode", ["containerized_execution", "provenance_capture"],
    "Traces operating-system calls during a command-line run and packs every binary, file and dependency into a bundle that others can unpack and re-execute. Use it to capture an analysis you cannot easily containerize. Linux tracing only.",
    "pointer", "", repo="ReproNim/reprozip")
res("reproseed", "reproseed", "SoftwareSourceCode", ["containerized_execution"],
    "A POSIX shell script that sets one REPROSEED value into the many tool-specific random-seed environment variables, so non-deterministic tools become reproducible where seeding allows. Use it around pipelines with random initialisation (e.g. UMAP, registration). Cannot fix nondeterminism from parallel reduction order.",
    "pointer", "Relevant to the UMAP seed handling here; we seed in code instead.", repo="ReproNim/reproseed")
res("testkraken", "TestKraken", "SoftwareSourceCode", ["containerized_execution", "statistics_results"],
    "Tests a scientific workflow across a matrix of parametrised environments (software versions, base images) and compares outputs. Use it to see how results move with the environment. Not maintained since 2021.",
    "pointer", "", repo="ReproNim/testkraken")
res("simple_workflow", "simple_workflow", "SoftwareSourceCode", ["containerized_execution", "statistics_results", "training"],
    "Code for 'A very simple, re-executable neuroimaging publication' (Ghosh et al., F1000Research): a small FSL-based analysis packaged to re-run in Docker or Singularity. Use it as a minimal template for a re-executable paper.",
    "pointer", "Ancestor of the simple2 NIDM work.", repo="ReproNim/simple_workflow", doi="10.12688/f1000research.10783.2")
res("babs-demo-ohbm2025", "BABS demo (OHBM 2025)", "TrainingMaterial", ["training", "containerized_execution"],
    "Course demo of BIDS App Bootstrap (BABS) on Slurm with a toy BIDS App that counts T1w volumes on ABIDE-I. Use it to learn how to run a BIDS App over a dataset on HPC with DataLad provenance.",
    "pointer", "", repo="ReproNim/babs-demo-ohbm2025", audience=("students", "HPC users"))

# ---- acquisition ----
res("reproin", "ReproIn", "SoftwareSourceCode", ["acquisition", "conversion_to_bids"],
    "A turnkey setup (HeuDiConv heuristic plus DataLad) that converts scanner DICOMs into version-controlled BIDS datasets automatically, based on how sequences are named at the scanner. Use it to get BIDS at acquisition time. Requires following its scanner naming convention.",
    "pointer", "", repo="ReproNim/reproin", inputs=["DICOM format"], outputs=["nii", "JSON"], ops=["Conversion"], topics=["Data acquisition", "MRI"])
res("reprostim", "ReproStim", "SoftwareSourceCode", ["acquisition"],
    "Video and audio capture suite that records the actual stimuli shown to each participant during a session and stores them alongside behavioural or imaging data in BIDS. Use it to keep a faithful record of what was presented.",
    "pointer", "", repo="ReproNim/reprostim", modality=("MRI", "behaviour"), topics=["Data acquisition"])

# ---- training, skills ----
res("reproinventory", "ReproInventory", "TrainingMaterial", ["training"],
    "A searchable inventory of ReproNim and community training resources, so teachers can find, reuse and adapt material instead of starting from scratch.",
    "pointer", "", repo="ReproNim/ReproInventory", audience=("teachers", "students"))
for mod, txt in (("module-intro", "introduction to reproducible neuroimaging"), ("module-reproducible-basics", "reproducible computational basics (shell, version control, environments)"),
                 ("module-FAIR-data", "FAIR data and data sharing"), ("module-dataprocessing", "reproducible data processing"), ("module-stats", "statistics for reproducible neuroimaging")):
    res(mod, f"ReproNim {mod}", "TrainingMaterial", ["training"], f"ReproNim teaching module on {txt}, built from the ReproNim lesson template.",
        "pointer", "", repo=f"ReproNim/{mod}", audience=("students",))
res("repronim-skills", "ReproNim skills", "SkillCollection", ["agent_skills"],
    "Repository intended for AI-agent skills (Agent Skills format) covering ReproNim tools such as DataLad, Neurodocker and ReproSchema. At the pinned commit it contains only a README and an empty skills/ directory: no skills yet.",
    "pointer", "Inspected: 0 skill files at the pinned commit.", repo="ReproNim/skills", modality=("software",), audience=("AI coding agents", "developers"))
res("sensein-agent-skills", "sensein agent_skills", "SkillCollection", ["agent_skills", "provenance_capture", "containerized_execution"],
    "A collection of agent skills (duct, kya, labnb, orcd-remote, structsense, synthscholar, brainkb and others), each a SKILL.md with optional scripts, for resource logging, lab notebooks, structured extraction and HPC execution. Use to give coding agents reusable, reviewable procedures.",
    "pointer", "orcd-remote informed the ORCD job; structsense was used in the earlier CNP package.", repo="sensein/agent_skills",
    modality=("software",), audience=("AI coding agents", "developers"))

# ---- federation: ReproPond / ReproLake via Neurobagel ----
res("neurobagel-federation-api", "Neurobagel federation API", "SoftwareSourceCode", ["query_merge"],
    "REST API that federates a query over many Neurobagel graph databases (nodes), so a question travels to each pond and only the answers each node permits come back. Use it to search across sites without pooling participant data. Each node decides what it returns.",
    "pointer", "The federation mechanism between ReproPonds and the ReproLake; not deployed here.", repo="neurobagel/federation-api",
    modality=("MRI", "phenotype"), consumes=["nidm:AcquisitionObject"], ops=["Query and retrieval"], audience=("consortia", "data stewards"))
res("neurobagel-api", "Neurobagel node API", "SoftwareSourceCode", ["query_merge"],
    "The API a single Neurobagel node (a ReproPond) exposes over its graph database of harmonized participant-level phenotype and imaging metadata. Use it to make a local store queryable by the federation. Returns participant-level or aggregate results as the node is configured.",
    "pointer", "", repo="neurobagel/api", modality=("MRI", "phenotype"), ops=["Query and retrieval"], audience=("data stewards",))
res("neurobagel-query-tool", "Neurobagel query tool", "SoftwareSourceCode", ["query_merge"],
    "Web interface for cohort discovery across Neurobagel nodes: filter by age, sex, diagnosis, assessment and imaging modality, then download matching participant or dataset results. Use it to find participants across ponds and the lake.",
    "pointer", "", repo="neurobagel/query-tool", modality=("MRI", "phenotype"), audience=("neuroimaging researchers",))
res("neurobagel-bagel-cli", "Neurobagel bagel-cli", "SoftwareSourceCode", ["phenotype_assessment_schema", "query_merge"],
    "Command-line tool that turns a phenotype table plus its annotated data dictionary (and optionally BIDS and derivatives) into Neurobagel graph-ready JSON-LD. Use it to put a local dataset into a Neurobagel node.",
    "pointer", "", repo="neurobagel/bagel-cli", modality=("phenotype",), consumes=["phenotype table"], outputs=["JSON-LD"], ops=["Conversion"])
res("reprolake", "ReproLake", "Dataset", ["data_source", "query_merge"],
    "ReproNim's semantically aligned store of publicly available datasets (OpenNeuro and others), queryable with Neurobagel. Use it as the public, lake-scoped counterpart of local ReproPonds.",
    "pointer", "Target scope for promoted, egress-permitted knowledge.", url="https://www.repronim.org/resources/tools/reprolake/",
    modality=("MRI", "phenotype"), audience=("neuroimaging researchers",))
res("repronim-pond-lake-tutorial", "Tutorial: ReproPond and ReproLake", "TrainingMaterial", ["training", "query_merge"],
    "ReproNim tutorial on sharing and searching metadata with a local ReproPond (NIDM served by a Neurobagel node, federable across sites) and the public ReproLake.",
    "pointer", "Source of the pond/lake scope terms used in this graph.", url="https://repronim.org/resources/tutorials/pond-lake/", audience=("students", "data stewards"))

# ---- datasets and papers ----
res("abide-preprocessed", "ABIDE Preprocessed (PCP)", "Dataset", ["data_source", "preprocessing"],
    "Preprocessed ABIDE I resting-state fMRI and structural derivatives from the Preprocessed Connectomes Project: four pipelines (C-PAC, CCS, DPARSF, NIAK), several strategies and atlases, ROI time series, FreeSurfer and ANTs outputs, and a phenotype table with three-rater QC. Public on S3 (fcp-indi).",
    "data_source", "Phenotype table, CC200 time series (C-PAC filt_noglobal), ANTs ROI thickness and the C-PAC config were downloaded and hashed.",
    url="http://preprocessed-connectomes-project.org/abide/", modality=("MRI", "fMRI", "phenotype"), produces=["nidm:DerivativeObject", "nidm:AcquisitionObject"],
    outputs=["CSV", "nii"], topics=["MRI", "Psychiatry"], openalex="Preprocessed Connectomes Project ABIDE")
res("abide-raw-bids", "ABIDE I raw data (BIDS, S3)", "Dataset", ["data_source", "acquisition"],
    "Raw ABIDE I T1w and resting BOLD scans from 1,112 participants at 17 international sites, in BIDS on S3 (fcp-indi RawDataBIDS).",
    "pointer", "Referenced by URL as source scans; not downloaded.", url="https://fcon_1000.projects.nitrc.org/indi/abide/",
    modality=("MRI", "fMRI"), produces=["nidm:AcquisitionObject"], outputs=["nii"], topics=["MRI", "Psychiatry"])
res("dimartino2014", "Di Martino et al. 2014 (ABIDE)", "ScholarlyArticle", ["data_source", "statistics_results"],
    "Introduces ABIDE and reports whole-brain functional connectivity differences in 763 males: both hypo- and hyperconnectivity, with hypoconnectivity dominating, especially cortico-cortical and interhemispheric.",
    "data_source", "Question, claim, cohort and methods extracted with verbatim quotes.", url="https://doi.org/10.1038/mp.2013.78", doi="10.1038/mp.2013.78",
    modality=("fMRI",), produces=["ex:Claim", "ex:ResearchQuestion"], topics=["Psychiatry", "MRI"])
res("abraham2017", "Abraham et al. 2017 (inter-site prediction)", "ScholarlyArticle", ["data_source", "statistics_results"],
    "Shows inter-site prediction of autism diagnosis from functional connectomes on 871 ABIDE participants (about 67% accuracy) and that region definition matters most among pipeline choices.",
    "data_source", "Question, claims, cohort and methods extracted with verbatim quotes (arXiv v1).", url="https://doi.org/10.1016/j.neuroimage.2016.10.045",
    doi="10.1016/j.neuroimage.2016.10.045", modality=("fMRI",), produces=["ex:Claim", "ex:ResearchQuestion"], topics=["Psychiatry", "Machine learning"])

# ---- software executed in this experiment ----
for rid, name, repo, steps, desc, ops in (
    ("nilearn", "nilearn", "nilearn/nilearn", ["statistics_results"], "Python machine learning and statistics for neuroimaging; used here for the tangent-space connectivity embedding fitted inside each training fold.", ["Statistical calculation"]),
    ("scikit-learn", "scikit-learn", "scikit-learn/scikit-learn", ["statistics_results"], "General machine learning library; used for scaling, logistic regression, cross-validation metrics, PCA and trustworthiness.", ["Statistical calculation"]),
    ("umap-learn", "UMAP", "lmcinnes/umap", ["statistics_results"], "Uniform Manifold Approximation and Projection for dimension reduction; used for the phenotype embedding (seeded).", ["Visualisation"]),
    ("rdflib", "RDFLib", "RDFLib/rdflib", ["provenance_capture", "query_merge"], "Python RDF library; used to construct the graph and run SHACL. Its in-memory SPARQL did not finish the simple2 query on one site in 27 minutes.", ["Query and retrieval"]),
    ("pyshacl", "pySHACL", "RDFLib/pySHACL", ["provenance_capture"], "SHACL validator for RDF graphs; used for the local shape profile and mutation tests.", ["Validation"]),
    ("pyoxigraph", "Oxigraph (pyoxigraph)", "oxigraph/oxigraph", ["query_merge"], "SPARQL 1.1 store and query engine in Rust with Python bindings; used to load named graphs and run all queries, including ReproNim's simple2 query unmodified.", ["Query and retrieval"]),
):
    res(rid, name, "SoftwareSourceCode", steps, desc, "executed", "Executed in this experiment (version pinned in uv.lock).", repo=repo, modality=("software",), ops=ops)
res("cpac", "C-PAC", "SoftwareSourceCode", ["preprocessing"],
    "Configurable Pipeline for the Analysis of Connectomes; produced the ABIDE Preprocessed filt_noglobal CC200 time series used here (config hashed).",
    "data_source", "Outputs used as released; not run here.", repo="FCP-INDI/C-PAC", modality=("fMRI",), produces=["nidm:DerivativeObject"], ops=["Image analysis"])


def resolve_edam() -> dict:
    """Map every EDAM label used in the catalog to its class IRI; fail on any unknown label."""
    e = pd.read_csv(DATA / "vocab/EDAM.tsv", sep="\t", low_memory=False)
    e = e[e.Obsolete.astype(str) != "True"]
    by_label = {}
    for _, r in e.iterrows():
        by_label.setdefault(str(r["Preferred Label"]), r["Class ID"])
    used = {lab for r in R for lab in r["inputs"] + r["outputs"] + r["ops"] + r["topics"]}
    missing = sorted(lab for lab in used if lab not in by_label)
    if missing:
        raise SystemExit(f"EDAM labels not found: {missing}")
    return {lab: by_label[lab] for lab in used}


def gh(path: str) -> dict:
    """GitHub REST call through the gh CLI."""
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    return json.loads(out.stdout) if out.returncode == 0 else {}


def refresh_pins() -> None:
    """Record commit SHA, license, language and description for every GitHub resource."""
    pins = {"fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "repos": {}}
    for r in R:
        if not r["repo"]:
            continue
        meta = gh(f"repos/{r['repo']}")
        sha = gh(f"repos/{r['repo']}/commits/{meta.get('default_branch', 'main')}").get("sha")
        pins["repos"][r["repo"]] = {
            "default_branch": meta.get("default_branch"), "commit": sha, "license": (meta.get("license") or {}).get("spdx_id"),
            "language": meta.get("language"), "github_description": meta.get("description"), "archived": meta.get("archived"),
            "owner_login": (meta.get("owner") or {}).get("login"),
        }
        print(r["repo"], sha, flush=True)
    PINS.write_text(json.dumps(pins, indent=1, sort_keys=True))


def build() -> None:
    """Write graph/resources.ttl."""
    pins = json.loads(PINS.read_text())
    edam = resolve_edam()
    g = Graph()
    for k, v in (("ex", E), ("schema", SDO), ("codemeta", CM), ("dcat", DCAT), ("prov", PROV), ("dct", DCT), ("nidm", NIDM)):
        g.bind(k, v)
    g.bind("edam", Namespace("http://edamontology.org/"))
    stype = {"SoftwareSourceCode": SDO.SoftwareSourceCode, "Dataset": SDO.Dataset, "Specification": SDO.CreativeWork, "Vocabulary": SDO.DefinedTermSet,
             "TrainingMaterial": SDO.LearningResource, "SkillCollection": SDO.SoftwareSourceCode, "ScholarlyArticle": SDO.ScholarlyArticle}
    for r in R:
        u = E[f"resource/{r['id']}"]
        g.add((u, RDF.type, E.Resource))
        g.add((u, RDF.type, stype[r["type"]]))
        if r["type"] == "Dataset":
            g.add((u, RDF.type, DCAT.Dataset))
        g.add((u, E.resourceType, Literal(r["type"])))
        g.add((u, SDO.name, Literal(r["name"])))
        g.add((u, RDFS.label, Literal(r["name"])))
        g.add((u, SDO.description, Literal(r["description"])))
        g.add((u, SDO.url, URIRef(r["url"])))
        if r["repo"]:
            p = pins["repos"].get(r["repo"], {})
            g.add((u, SDO.codeRepository, URIRef(GH + r["repo"])))
            g.add((u, E.descriptionSource, URIRef(f"{GH}{r['repo']}/blob/{p.get('commit')}/README.md")))
            if p.get("commit"):
                g.add((u, SDO.version, Literal(p["commit"])))
                g.add((u, E.pinnedCommit, Literal(p["commit"])))
            g.add((u, SDO.license, Literal(p.get("license") or "none declared")))
            if p.get("language"):
                g.add((u, SDO.programmingLanguage, Literal(p["language"])))
            if p.get("owner_login"):
                g.add((u, CM.maintainer, Literal(p["owner_login"])))
            g.add((u, E.githubRepo, Literal(r["repo"])))
        else:
            g.add((u, E.descriptionSource, URIRef(r["url"])))
        if r["doi"]:
            g.add((u, SDO.identifier, URIRef(f"https://doi.org/{r['doi']}")))
            g.add((u, E.doi, Literal(r["doi"])))
        if r["openalex"]:
            g.add((u, E.openalexSearch, Literal(r["openalex"])))
        for s in r["steps"]:
            g.add((u, E.workflowStep, E[f"step/{s}"]))
            g.add((E[f"step/{s}"], RDFS.label, Literal(s.replace("_", " "))))
            g.add((E[f"step/{s}"], RDF.type, E.WorkflowStep))
            g.add((E[f"step/{s}"], E.order, Literal(STEPS.index(s), datatype=XSD.integer)))
        for m in r["modality"]:
            g.add((u, E.modality, Literal(m)))
        for a in r["audience"]:
            g.add((u, SDO.audience, Literal(a)))
        for c in r["consumes"]:
            g.add((u, E.consumes, Literal(c)))
        for c in r["produces"]:
            g.add((u, E.produces, Literal(c)))
        for f in r["inputs"]:
            g.add((u, E.inputFormat, URIRef(edam[f])))
        for f in r["outputs"]:
            g.add((u, E.outputFormat, URIRef(edam[f])))
        for o in r["ops"]:
            g.add((u, E.edamOperation, URIRef(edam[o])))
        for t in r["topics"]:
            g.add((u, E.edamTopic, URIRef(edam[t])))
        for lab, iri in edam.items():
            g.add((URIRef(iri), RDFS.label, Literal(lab)))
        g.add((u, E.usageInExperiment, Literal(r["usage"])))
        if r["usage_note"]:
            g.add((u, E.usageNote, Literal(r["usage_note"])))
    g.add((E["resource/simple2_nidm_examples"], E.loadedAs, E["activity/identity_join_simple2"]))
    g.serialize(GRAPH / "resources.ttl", format="turtle")
    counts = pd.DataFrame([{"type": r["type"], "usage": r["usage"]} for r in R])
    steps = pd.Series([s for r in R for s in r["steps"]]).value_counts().to_dict()
    write_json("resources_catalog.json", {
        "n_resources": len(R), "by_type": counts.type.value_counts().to_dict(), "by_usage": counts.usage.value_counts().to_dict(),
        "by_step": steps, "edam_terms_used": len(edam), "pins_fetched_at": pins["fetched_at"],
        "executed": [r["id"] for r in R if r["usage"] == "executed"], "data_source": [r["id"] for r in R if r["usage"] == "data_source"],
        "edam_labels_without_term": ["BIDS", "container", "provenance", "segmentation"],
        "triples": len(g)})
    print(len(R), "resources;", len(g), "triples")


if __name__ == "__main__":
    if "--refresh-pins" in sys.argv:
        refresh_pins()
    build()
