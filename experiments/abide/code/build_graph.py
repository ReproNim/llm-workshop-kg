"""Build the NIDM/PROV knowledge graph for the ABIDE collaboration experiment.

Stages:
  v1     dataset + QC + papers + both analysts' v1 analyses and reviews, plus the proposed motion-rule
         revision (no recomputed results). Written to graph/abide_kg_v1.ttl.
  final  v1 content plus v2 analyses, v2 reviews and the revision-impact assessment.
         Written to graph/abide_kg.ttl.

Usage: uv run python code/build_graph.py v1|final
"""

import json
import math
import sys

import numpy as np
import pandas as pd
from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace, URIRef

from common import (
    CC200_REL,
    DATA,
    DERIVED,
    FIQ_RANGE,
    GRAPH,
    MIN_PER_GROUP_PER_SITE,
    MOTION_RULES,
    PHENO_PATH,
    RAW_T1_REL,
    RESULTS,
    ROOT,
    S3,
    THICK_REL,
    base_table,
    connectivity,
    load_pheno,
    raw_bold_url,
    sha256_bytes,
    sha256_file,
)

E = Namespace("urn:repronim:abide:")
NIDM = Namespace("http://purl.org/nidash/nidm#")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
SIO = Namespace("http://semanticscience.org/ontology/sio.owl#")
NDAR = Namespace("https://ndar.nih.gov/api/datadictionary/v2/dataelement/")
CRYPTO = Namespace("http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions#")
ONLI = Namespace("http://neurolog.unice.fr/ontoneurolog/v3.0/instrument.owl#")
NFO = Namespace("http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#")
DCTYPES = Namespace("http://purl.org/dc/dcmitype/")
OBO = Namespace("http://purl.obolibrary.org/obo/")
SDO = Namespace("http://schema.org/")
TERM_MAP = DATA / "repronim_simple2/bids_nidm_scripts/abide_phenotypic_v1_0b_vars_to_terms_v5.json"
TOOL_ROLE = NIDM.NIDM_0000164
TOOL_NS = {"cpac": URIRef("https://fcp-indi.github.io/"), "ants": URIRef("http://stnava.github.io/ANTs/")}

SKIP_COLUMNS = {"Unnamed: 0.1", "Unnamed: 0", "X", "source_row"}
MISSING = {"", "nan", "-9999", "-9999.0", "-9999.00"}
ILLUSTRATIVE = "illustrative scenario; hypothetical analyst, not a real person's contribution"
METHODS = ("demographic", "demographic_fd", "correlation", "tangent")


class Builder:
    """Small helper around an rdflib Graph."""

    def __init__(self) -> None:
        """Create the graph and bind prefixes."""
        self.g = Graph()
        for k, v in (("ex", E), ("nidm", NIDM), ("prov", PROV), ("dct", DCT), ("sio", SIO), ("ndar", NDAR), ("crypto", CRYPTO),
                     ("onli", ONLI), ("nfo", NFO), ("dctypes", DCTYPES), ("obo", OBO), ("schema", SDO)):
            self.g.bind(k, v)

    def add(self, s, p, o) -> None:
        """Add one triple, converting plain Python values to literals."""
        if not isinstance(o, (URIRef, Literal)):
            o = typed(o)
        self.g.add((s, p, o))

    def node(self, uri, *types, label=None):
        """Declare a node with types and an optional label."""
        for t in types:
            self.g.add((uri, RDF.type, t))
        if label is not None:
            self.g.add((uri, RDFS.label, Literal(label)))
        return uri

    def role(self, activity, agent, role, key) -> None:
        """Attach a PROV qualified association with a role."""
        a = self.node(E[f"association/{key}"], PROV.Association)
        self.add(activity, PROV.qualifiedAssociation, a)
        self.add(activity, PROV.wasAssociatedWith, agent)
        self.add(a, PROV.agent, agent)
        self.add(a, PROV.hadRole, role)


def typed(v) -> Literal:
    """Typed literal for numbers and booleans, plain literal otherwise."""
    if isinstance(v, (bool, np.bool_)):
        return Literal(bool(v), datatype=XSD.boolean)
    if isinstance(v, (int, np.integer)):
        return Literal(int(v), datatype=XSD.integer)
    if isinstance(v, (float, np.floating)):
        return Literal(float(v), datatype=XSD.double)
    return Literal(str(v))


def cell_literal(raw: str) -> Literal:
    """Source cell as xsd:double when numeric (lexical form kept), else string."""
    try:
        float(raw)
        return Literal(raw, datatype=XSD.double)
    except ValueError:
        return Literal(raw)


def load(name: str) -> dict:
    """Load a results JSON."""
    return json.loads((RESULTS / name).read_text())


def dataset_layer(b: Builder) -> None:
    """Participants, phenotype records, raw scan pointers, preprocessing, time series, connectivity, IDPs."""
    project = b.node(E.project, NIDM.Project, PROV.Activity, label="ABIDE I collaboration knowledge graph")
    b.add(project, DCTYPES.title, "ABIDE I collaboration knowledge graph")
    b.add(project, DCT.description, "ABIDE I Preprocessed (fcp-indi S3) phenotype, CPAC filt_noglobal CC200 time series, ANTs ROI thickness")
    for name in ("common.py", "build_graph.py", "analyst_a.py", "analyst_b.py", "reviews.py", "cohorts.py"):
        sa = b.node(E[f"software/{name}"], PROV.SoftwareAgent, PROV.Agent, label=name)
        b.add(sa, CRYPTO.sha256, sha256_file(ROOT / "code" / name))
    cpac = b.node(E["software/cpac"], PROV.SoftwareAgent, PROV.Agent, label="C-PAC (ABIDE Preprocessed release)")
    ants = b.node(E["software/ants"], PROV.SoftwareAgent, PROV.Agent, label="ANTs cortical thickness (ABIDE Preprocessed release)")
    for sw, key, name in ((cpac, "cpac", "C-PAC"), (ants, "ants", "ANTs")):
        b.add(sw, TOOL_ROLE, TOOL_NS[key])
        b.add(sw, SDO.name, name)
        b.add(sw, SDO.softwareVersion, "as released by ABIDE Preprocessed (2016); exact version not recorded per participant")
    cfg = b.node(E["resource/pipeline_config"], PROV.Entity, label="C-PAC pipeline_config.yml")
    b.add(cfg, PROV.atLocation, URIRef(f"{S3}/Resources/pipeline_config.yml"))
    b.add(cfg, CRYPTO.sha256, sha256_file(DATA / "Resources/pipeline_config.yml"))
    for k, v in {
        "strategy": "filt_noglobal (band-pass filtered, no global signal regression)",
        "nuisance": "CompCor 5 components; Friston 24 motion; linear and quadratic trend",
        "globalSignalRegression": False,
        "bandpassHz": "0.01-0.1",
        "scrubbing": False,
        "registration": "ANTS; BBR func-to-anat",
    }.items():
        b.add(cfg, E[k], v)
    atlas = b.node(E["resource/cc200"], PROV.Entity, label="Craddock 200 (CC200) atlas labels")
    b.add(atlas, PROV.atLocation, URIRef(f"{S3}/Resources/CC200_ROI_labels.csv"))
    b.add(atlas, CRYPTO.sha256, sha256_file(DATA / "Resources/CC200_ROI_labels.csv"))
    pheno_src = b.node(E["resource/phenotype_csv"], PROV.Entity, label=PHENO_PATH.name)
    b.add(pheno_src, PROV.atLocation, URIRef(f"{S3}/{PHENO_PATH.name}"))
    b.add(pheno_src, CRYPTO.sha256, sha256_file(PHENO_PATH))

    raw = pd.read_csv(PHENO_PATH, dtype=str, keep_default_na=False)
    raw_numeric = load_pheno()
    cols = [c for c in raw.columns if c not in SKIP_COLUMNS and c.strip()]
    term_map = {}
    for k, v in json.loads(TERM_MAP.read_text()).items():
        term_map[k.split("variable='")[1].rstrip("')")] = v
    b.g.add((NIDM.PersonalDataElement, RDFS.subClassOf, NIDM.DataElement))
    for c in cols:
        tm = term_map.get(c)
        de = b.node(E[f"variable/{c}"], NIDM.DataElement, PROV.Entity, label=(tm or {}).get("label") or c)
        b.add(de, NIDM.sourceVariable, c)
        b.add(de, PROV.wasDerivedFrom, pheno_src)
        if tm:
            b.add(de, RDF.type, NIDM.PersonalDataElement)
            b.add(de, E.termMapping, URIRef(f"https://github.com/ReproNim/simple2_NIDM_examples/blob/e0dff17629bd5031e246c05ff4bed174597552a2/bids_nidm_scripts/{TERM_MAP.name}"))
            if tm.get("description"):
                b.add(de, DCT.description, tm["description"])
            if tm.get("valueType"):
                b.add(de, NIDM.valueType, URIRef(tm["valueType"]))
            for slot in ("minValue", "maxValue", "hasUnit"):
                if tm.get(slot) not in (None, ""):
                    b.add(de, NIDM[slot], str(tm[slot]))
            about = tm.get("isAbout")
            for a in about if isinstance(about, list) else ([about] if about else []):
                b.add(de, NIDM.isAbout, URIRef(a["@id"]))
    for i, row in raw.iterrows():
        fid = row["FILE_ID"] if row["FILE_ID"] != "no_filename" else f"SUB_{row['SUB_ID']}"
        p = b.node(E[f"participant/{fid}"], PROV.Person, PROV.Agent, label=fid)
        b.add(p, E.subId, int(raw_numeric.at[i, "SUB_ID"]))
        b.add(p, NDAR.src_subject_id, Literal(str(int(raw_numeric.at[i, "SUB_ID"]))))
        b.add(p, E.site, row["SITE_ID"])
        ses = b.node(E[f"session/{fid}"], NIDM.Session, PROV.Activity)
        b.add(ses, DCT.isPartOf, project)
        b.add(ses, E.status, "reconstructed visit container; no date inferred")
        acq = b.node(E[f"acquisition/{fid}/phenotype"], NIDM.Acquisition, PROV.Activity, ONLI["instrument-based-assessment"])
        b.add(acq, DCT.isPartOf, ses)
        b.role(acq, p, SIO.Subject, f"{fid}/phenotype")
        rec = b.node(E[f"record/{fid}"], NIDM.AcquisitionObject, PROV.Entity, ONLI["assessment-instrument"])
        b.add(rec, PROV.wasGeneratedBy, acq)
        b.add(rec, PROV.wasDerivedFrom, pheno_src)
        b.add(rec, E.sourceRow, int(raw_numeric.at[i, "source_row"]))
        b.add(rec, E.participant, p)
        for c in cols:
            v = row[c].strip()
            if v.lower() in MISSING:
                b.add(rec, E.missingVariable, E[f"variable/{c}"])
            else:
                b.add(rec, E[f"variable/{c}"], cell_literal(v))

    thick_rel = b.node(E["resource/ants_roi_thickness_release"], PROV.Entity, PROV.Collection, label="ABIDE Preprocessed ANTs ROI thickness files")
    b.add(thick_rel, PROV.atLocation, URIRef(f"{S3}/Outputs/ants/roi_thickness/"))
    for name, label, about, unit, src in (
        ("ants_mean_cortical_thickness", "mean cortical thickness (ANTs ROI means, labels >= 1000)", OBO.UBERON_0000956, "mm", thick_rel),
        ("cc200_mean_fisher_z", "mean Fisher-z CC200 functional connectivity", None, None, atlas),
    ):
        de = b.node(E[f"variable/{name}"], NIDM.DataElement, PROV.Entity, label=label)
        b.add(de, NIDM.sourceVariable, name)
        b.add(de, PROV.wasDerivedFrom, src)
        b.add(de, PROV.wasAttributedTo, E["software/build_graph.py"])
        b.add(de, NIDM.valueType, XSD.double)
        if about is not None:
            b.add(de, NIDM.isAbout, about)
        if unit:
            b.add(de, NIDM.hasUnit, unit)
    d = base_table()
    Xc, fids = connectivity()
    fidx = {f: i for i, f in enumerate(fids)}
    for _, r in d.iterrows():
        fid = r.FILE_ID
        p = E[f"participant/{fid}"]
        for kind, url in (("rest", raw_bold_url(r)), ("T1w", f"{S3}/{RAW_T1_REL.format(site=fid.rsplit('_', 1)[0], sub=int(r.SUB_ID))}")):
            acq = b.node(E[f"acquisition/{fid}/{kind}"], NIDM.Acquisition, PROV.Activity)
            b.add(acq, DCT.isPartOf, E[f"session/{fid}"])
            b.role(acq, p, SIO.Subject, f"{fid}/{kind}")
            img = b.node(E[f"raw/{fid}/{kind}"], NIDM.AcquisitionObject, PROV.Entity, label=f"{fid} {kind}")
            b.add(img, PROV.wasGeneratedBy, acq)
            b.add(img, E.participant, p)
            b.add(img, PROV.atLocation, URIRef(url))
            b.add(img, PROV.Location, url)
            b.add(img, NFO.filename, "bids::" + url.split(f"/RawDataBIDS/{fid.rsplit('_', 1)[0]}/", 1)[-1])
            b.add(img, NIDM.hadAcquisitionModality, NIDM.MagneticResonanceImaging)
            b.add(img, NIDM.hadImageContrastType, NIDM.T1Weighted if kind == "T1w" else NIDM.T2StarWeighted)
            b.add(img, NIDM.hadImageUsageType, NIDM.Anatomical if kind == "T1w" else NIDM.Functional)
            if kind == "rest":
                b.add(img, NIDM.Task, "rest")
            b.add(img, E.contentRetrieved, False)
        pre = b.node(E[f"preprocess/{fid}"], NIDM.Derivative, PROV.Activity, label=f"C-PAC filt_noglobal {fid}")
        b.add(pre, PROV.used, E[f"raw/{fid}/rest"])
        b.add(pre, PROV.used, cfg)
        b.add(pre, PROV.used, atlas)
        b.add(pre, PROV.wasAssociatedWith, cpac)
        b.add(pre, DCT.isPartOf, project)
        b.role(pre, cpac, TOOL_ROLE, f"{fid}/cpac_tool")
        b.role(pre, p, SIO.Subject, f"{fid}/cpac_subject")
        b.add(pre, E.executionRecord, "output of the ABIDE Preprocessed release; per-run logs not retrieved")
        ts = b.node(E[f"timeseries/{fid}"], NIDM.DerivativeObject, PROV.Entity, label=f"{fid} CC200 time series")
        b.add(ts, PROV.wasGeneratedBy, pre)
        b.add(ts, PROV.wasDerivedFrom, E[f"raw/{fid}/rest"])
        b.add(ts, E.participant, p)
        b.add(ts, PROV.atLocation, URIRef(f"{S3}/{CC200_REL.format(fid=fid)}"))
        b.add(ts, CRYPTO.sha256, r.timeseries_sha256)
        b.add(ts, E.nTimepoints, int(r.n_timepoints))
        b.add(ts, E.nZeroVarianceRois, int(r.n_zero_variance_rois))
        b.add(ts, E.fullRoiCoverage, bool(r.full_roi_coverage))
        if fid in fidx:
            act = b.node(E[f"connectivity_activity/{fid}"], NIDM.Derivative, PROV.Activity)
            b.add(act, PROV.used, ts)
            b.add(act, PROV.wasAssociatedWith, E["software/common.py"])
            b.add(act, DCT.isPartOf, project)
            b.add(act, E.method, "Pearson correlation of CC200 time series, Fisher z, upper triangle (19900 edges)")
            conn = b.node(E[f"connectivity/{fid}"], NIDM.DerivativeObject, PROV.Entity)
            b.add(conn, PROV.wasGeneratedBy, act)
            b.add(conn, PROV.wasDerivedFrom, ts)
            b.add(conn, E.participant, p)
            vec = Xc[fidx[fid]]
            b.add(conn, CRYPTO.sha256, sha256_bytes(vec.tobytes()))
            b.add(conn, E.meanFisherZ, float(vec.mean()))
            b.add(conn, E["variable/cc200_mean_fisher_z"], float(vec.mean()))
        tpath = DATA / THICK_REL.format(fid=fid)
        tdf = pd.read_csv(tpath, sep="\t")
        vals = tdf.filter(like="Mean_").iloc[0].astype(float)
        ants_act = b.node(E[f"ants_thickness/{fid}"], NIDM.Derivative, PROV.Activity)
        b.add(ants_act, PROV.used, E[f"raw/{fid}/T1w"])
        b.add(ants_act, PROV.wasAssociatedWith, ants)
        b.add(ants_act, DCT.isPartOf, project)
        b.role(ants_act, ants, TOOL_ROLE, f"{fid}/ants_tool")
        b.role(ants_act, p, SIO.Subject, f"{fid}/ants_subject")
        idp = b.node(E[f"idp/{fid}/roi_thickness"], NIDM.DerivativeObject, PROV.Entity, label=f"{fid} ANTs ROI thickness")
        b.add(idp, PROV.wasGeneratedBy, ants_act)
        b.add(idp, PROV.wasDerivedFrom, E[f"raw/{fid}/T1w"])
        b.add(idp, E.participant, p)
        b.add(idp, PROV.atLocation, URIRef(f"{S3}/{THICK_REL.format(fid=fid)}"))
        b.add(idp, CRYPTO.sha256, sha256_file(tpath))
        cortical = vals[[c for c in vals.index if int(c.split("_")[1]) >= 1000]]
        b.add(idp, E.meanCorticalThickness, float(cortical.mean()))
        b.add(idp, E["variable/ants_mean_cortical_thickness"], float(cortical.mean()))
        b.add(idp, E.summaryDefinition, "mean of ANTs ROI means for labels >= 1000 (cortical DKT labels)")


def agents(b: Builder) -> None:
    """The two hypothetical analysts."""
    for k in ("A", "B"):
        a = b.node(E[f"analyst{k}"], PROV.Person, PROV.Agent, label=f"Analyst {k} (hypothetical)")
        b.add(a, E.scenarioStatus, ILLUSTRATIVE)


def qc_layer(b: Builder, stage: str) -> None:
    """QC rules, cohort selection activities and cohort collections."""
    rules = {
        "rater_qc": "qc_rater_1 != fail AND qc_anat_rater_2 in {OK,maybe} AND qc_func_rater_2 in {OK,maybe} AND qc_anat_rater_3 == OK AND qc_func_rater_3 == OK (nilearn fetch_abide_pcp quality_checked)",
        "coverage": "all 200 CC200 ROI time series have non-zero variance",
        "male": "SEX == 1",
        "fiq_range": f"{FIQ_RANGE[0]} <= FIQ <= {FIQ_RANGE[1]} (Di Martino 2014: within 2 SD of 108±15)",
        "site_min": f"site retains >= {MIN_PER_GROUP_PER_SITE} ASD and >= {MIN_PER_GROUP_PER_SITE} TD after other criteria",
    }
    for k, text in rules.items():
        r = b.node(E[f"rule/{k}"], E.SelectionRule, PROV.Entity, label=k)
        b.add(r, E.definition, text)
    for v, thr in MOTION_RULES.items():
        r = b.node(E[f"rule/motion_{v}"], E.SelectionRule, PROV.Entity, label=f"shared motion rule {v}")
        b.add(r, E.definition, f"func_mean_fd < {thr} mm")
        b.add(r, E.variable, E["variable/func_mean_fd"])
        b.add(r, E.threshold, float(thr))
        b.add(r, E.comparison, "lessThan")
    rev = b.node(E["activity/motion_rule_revision"], PROV.Activity, label="Analyst A tightens the shared motion rule")
    b.role(rev, E.analystA, E.Analyst, "motion_rule_revision")
    b.add(rev, PROV.used, E["rule/motion_v1"])
    b.add(E["rule/motion_v2"], PROV.wasGeneratedBy, rev)
    b.add(E["rule/motion_v2"], PROV.wasRevisionOf, E["rule/motion_v1"])
    b.add(E["rule/motion_v2"], PROV.wasAttributedTo, E.analystA)
    b.add(E["rule/motion_v1"], PROV.wasAttributedTo, E.analystA)

    cohorts = load("cohorts.json")
    specs = {
        "B": (E.analystB, ["rater_qc", "coverage"]),
        "A": (E.analystA, ["rater_qc", "coverage", "male", "fiq_range", "site_min"]),
    }
    versions = ("v1",) if stage == "v1" else ("v1", "v2")
    for who, (agent, rlist) in specs.items():
        for v in versions:
            c = cohorts[f"{who}_{v}"]
            sel = b.node(E[f"select/{who}_{v}"], PROV.Activity, label=f"Select cohort {who} {v}")
            b.role(sel, agent, E.Analyst, f"select/{who}_{v}")
            b.add(sel, PROV.used, E["resource/phenotype_csv"])
            for r in rlist + [f"motion_{v}"]:
                b.add(sel, PROV.used, E[f"rule/{r}"])
            coh = b.node(E[f"cohort/{who}_{v}"], E.Cohort, PROV.Collection, PROV.Entity, label=f"Cohort {who} {v}")
            b.add(coh, PROV.wasGeneratedBy, sel)
            b.add(coh, E.n, c["n"])
            for f in c["members"]:
                b.add(coh, PROV.hadMember, E[f"participant/{f}"])
            if v == "v2":
                b.add(coh, PROV.wasRevisionOf, E[f"cohort/{who}_v1"])
    rc = cohorts["abraham2017_reconstructed"]
    coh = b.node(E["cohort/abraham2017_reconstructed"], E.Cohort, PROV.Collection, PROV.Entity, label="Abraham 2017 cohort (reconstructed)")
    b.add(coh, E.n, rc["n"])
    b.add(coh, E.reconstructionStatus, f"reconstructed with rater QC only; {rc['n']} vs 871 reported; membership unverified")
    b.add(coh, E.selectedUsing, E["rule/rater_qc"])
    for f in rc["members"]:
        b.add(coh, PROV.hadMember, E[f"participant/{f}"])


def questions(b: Builder) -> None:
    """The analysts' research questions, linked to the paper questions they are modelled on."""
    for who, text, paper_q in (
        ("A", "Does CC200 functional connectivity differ between ASD and TD males after adjusting for age, FIQ, mean FD and site?", "paper/dimartino2014/DM_Q"),
        ("B", "Does CC200 connectivity predict ASD vs TD at unseen sites better than age, sex and mean FD alone?", "paper/abraham2017/AB_Q"),
    ):
        q = b.node(E[f"question/{who}"], E.ResearchQuestion, PROV.Entity, label=text)
        b.add(q, PROV.wasAttributedTo, E[f"analyst{who}"])
        b.add(q, E.modelledOn, E[paper_q])


def analysis_layer(b: Builder, v: str) -> None:
    """Both analysts' analyses, results, claims and cross-reviews for one motion-rule version."""
    a = load(f"analyst_a_{v}.json")
    act = b.node(E[f"analysis/A_{v}"], PROV.Activity, label=f"Analyst A edgewise GLM {v}")
    b.role(act, E.analystA, E.Analyst, f"analysis/A_{v}")
    b.add(act, PROV.used, E[f"cohort/A_{v}"])
    b.add(act, PROV.wasAssociatedWith, E["software/analyst_a.py"])
    b.add(act, E.addresses, E["question/A"])
    b.add(act, E.model, a["model"])
    for f in a["members"]:
        b.add(act, PROV.used, E[f"connectivity/{f}"])
    res = b.node(E[f"result/A_{v}"], E.Result, PROV.Entity, label=f"Analyst A result {v}")
    b.add(res, PROV.wasGeneratedBy, act)
    b.add(res, PROV.wasDerivedFrom, E[f"cohort/A_{v}"])
    for k in ("n", "n_fdr_significant", "n_hypo", "n_hyper", "hypo_fraction", "interhemispheric_fraction_hypo_edges", "median_abs_d_significant"):
        b.add(res, E[k], a[k])
    lo, hi = a["hypo_fraction_bootstrap_95ci"]
    b.add(res, E.hypo_fraction_ci_low, lo)
    b.add(res, E.hypo_fraction_ci_high, hi)
    b.add(res, E.resultFile, f"results/analyst_a_{v}.json")
    claim = b.node(E[f"claim/A_{v}"], E.Claim, PROV.Entity, label=f"In {a['n']} males, {a['n_hypo']} of {a['n_fdr_significant']} FDR-significant edges show lower connectivity in ASD")
    b.add(claim, E.claimType, "associational")
    b.add(claim, E.scope, f"cohort A_{v}; {len(a['sites'])} sites; CPAC filt_noglobal CC200; no GSR")
    b.add(claim, E.addresses, E["question/A"])
    b.add(claim, PROV.wasDerivedFrom, res)
    b.add(claim, PROV.wasAttributedTo, E.analystA)

    bres = load(f"analyst_b_{v}.json")
    act = b.node(E[f"analysis/B_{v}"], PROV.Activity, label=f"Analyst B leave-site-out classification {v}")
    b.role(act, E.analystB, E.Analyst, f"analysis/B_{v}")
    b.add(act, PROV.used, E[f"cohort/B_{v}"])
    b.add(act, PROV.wasAssociatedWith, E["software/analyst_b.py"])
    b.add(act, E.addresses, E["question/B"])
    b.add(act, E.cv, bres["cv"])
    members = set(bres["members"])
    site_of = base_table().set_index("FILE_ID").SITE_ID
    fold_results = {m: [] for m in METHODS}
    for fold in bres["folds"]:
        s = fold["held_out_site"]
        fa = b.node(E[f"fold/B_{v}/{s}"], E.Fold, PROV.Activity, label=f"B {v} hold out {s}")
        b.add(fa, DCT.isPartOf, act)
        b.add(fa, E.heldOutSite, s)
        for f in members:
            b.add(fa, E.testedOn if site_of[f] == s else E.trainedOn, E[f"connectivity/{f}"])
        for m in METHODS:
            r = b.node(E[f"result/B_{v}/{s}/{m}"], E.Result, PROV.Entity)
            b.add(r, PROV.wasGeneratedBy, fa)
            b.add(r, E.method, m)
            b.add(r, E.accuracy, fold[m]["accuracy"])
            if fold[m]["auc"] is not None:
                b.add(r, E.auc, fold[m]["auc"])
            b.add(r, E.nTest, fold["n_test"])
            fold_results[m].append(r)
    for m in METHODS:
        pr = b.node(E[f"result/B_{v}/pooled/{m}"], E.Result, PROV.Entity, label=f"B {v} pooled {m}")
        for r in fold_results[m]:
            b.add(pr, PROV.wasDerivedFrom, r)
        pm = bres["pooled"][m]
        b.add(pr, E.method, m)
        b.add(pr, E.accuracy, pm["accuracy"])
        b.add(pr, E.auc, pm["auc"])
        b.add(pr, E.auc_ci_low, pm["auc_95ci"][0])
        b.add(pr, E.auc_ci_high, pm["auc_95ci"][1])
    pt, pd_ = bres["pooled"]["tangent"], bres["pooled"]["demographic_fd"]
    claim = b.node(E[f"claim/B_{v}"], E.Claim, PROV.Entity, label=f"Leave-site-out tangent connectivity AUC {pt['auc']:.3f} vs age/sex/FD baseline {pd_['auc']:.3f}")
    b.add(claim, E.claimType, "predictive")
    b.add(claim, E.scope, f"cohort B_{v}; {bres['n_folds']} held-out sites; N={bres['n']}")
    b.add(claim, E.addresses, E["question/B"])
    b.add(claim, PROV.wasDerivedFrom, E[f"result/B_{v}/pooled/tangent"])
    b.add(claim, PROV.wasDerivedFrom, E[f"result/B_{v}/pooled/demographic_fd"])
    b.add(claim, PROV.wasAttributedTo, E.analystB)

    rv = load(f"reviews_{v}.json")
    for key, reviewer, target, sources in (
        ("A_reviews_B", E.analystA, E[f"claim/B_{v}"], [E[f"result/A_{v}"], E[f"result/B_{v}/pooled/correlation"]]),
        ("B_reviews_A", E.analystB, E[f"claim/A_{v}"], [E[f"result/A_{v}"], E[f"cohort/B_{v}"]]),
    ):
        r = rv[key]
        ract = b.node(E[f"activity/{key}_{v}"], PROV.Activity, label=f"{key} {v}")
        b.role(ract, reviewer, E.Reviewer, f"{key}_{v}")
        rev = b.node(E[f"review/{key}_{v}"], E.EvidenceAssessment, PROV.Entity, label=f"{key} {v}")
        b.add(rev, PROV.wasGeneratedBy, ract)
        b.add(rev, PROV.wasAttributedTo, reviewer)
        b.add(rev, E.target, target)
        for s in sources:
            b.add(ract, PROV.used, s)
            b.add(rev, PROV.wasDerivedFrom, s)
        b.add(rev, E.verdict, r["verdict"])
        b.add(rev, E.caveat, r["caveat"])
        for k2, v2 in r.items():
            if isinstance(v2, (int, float)) and not (isinstance(v2, float) and math.isnan(v2)):
                b.add(rev, E[k2], v2)
    if v == "v2":
        for n in ("result/A", "claim/A", "claim/B", "review/A_reviews_B", "review/B_reviews_A"):
            b.add(E[f"{n}_v2"], PROV.wasRevisionOf, E[f"{n}_v1"])
        for m in METHODS:
            b.add(E[f"result/B_v2/pooled/{m}"], PROV.wasRevisionOf, E[f"result/B_v1/pooled/{m}"])


def paper_comparisons(b: Builder) -> None:
    """Attributed comparability assessments between each analyst claim and its source paper claim."""
    for who, paper_claim, note in (
        ("A", "paper/dimartino2014/DM_C1", "Same direction is testable; pipeline differs (release C-PAC, Friston-24 vs alpha C-PAC, 6 motion parameters), cohort differs (A_v1 vs 763), CC200 only. Not a replication."),
        ("B", "paper/abraham2017/AB_C1", "Same question form; atlas differs (CC200 vs MSDL best), cohort differs (B_v1 vs 871), single classifier. Not a replication."),
    ):
        act = b.node(E[f"activity/compare_{who}_to_paper"], PROV.Activity)
        b.role(act, E[f"analyst{who}"], E.Reviewer, f"compare_{who}_to_paper")
        a = b.node(E[f"assessment/{who}_vs_paper"], E.EvidenceAssessment, PROV.Entity, label=f"Analyst {who} claim vs paper claim")
        b.add(a, PROV.wasGeneratedBy, act)
        b.add(a, PROV.wasAttributedTo, E[f"analyst{who}"])
        b.add(a, E.target, E[paper_claim])
        b.add(a, PROV.wasDerivedFrom, E[f"claim/{who}_v1"])
        b.add(a, PROV.wasDerivedFrom, E[paper_claim])
        b.add(a, E.verdict, "comparable question, non-equivalent analysis")
        b.add(a, E.caveat, note)


def revision_layer(b: Builder) -> None:
    """Flags from the graph traversal and the measured change after recomputation."""
    flags = load("revision_flags.json")
    impact = load("revision_impact.json")
    act = b.node(E["activity/revision_traversal"], PROV.Activity, label="SPARQL dependency traversal after motion-rule revision")
    b.add(act, PROV.used, E["rule/motion_v2"])
    b.add(act, PROV.wasAssociatedWith, E["software/revision.py"])
    b.node(E["software/revision.py"], PROV.SoftwareAgent, PROV.Agent, label="revision.py")
    for uri in flags["flagged_entities"]:
        b.add(URIRef(uri), E.flaggedForReassessmentBy, act)
    for key, rec in impact["changes"].items():
        n = b.node(E[f"change/{key}"], E.MeasuredChange, PROV.Entity, label=key)
        b.add(n, PROV.wasGeneratedBy, act)
        b.add(n, E.target, URIRef(rec["v1"]))
        b.add(n, E.revisedAs, URIRef(rec["v2"]))
        b.add(n, E.summary, rec["summary"])
        b.add(n, E.materialChange, bool(rec["material"]))


def main(stage: str) -> None:
    """Build and serialise the requested stage."""
    b = Builder()
    dataset_layer(b)
    agents(b)
    qc_layer(b, stage)
    questions(b)
    b.g.parse(GRAPH / "papers.ttl")
    analysis_layer(b, "v1")
    paper_comparisons(b)
    if stage == "final":
        analysis_layer(b, "v2")
        revision_layer(b)
    out = GRAPH / ("abide_kg_v1.ttl" if stage == "v1" else "abide_kg.ttl")
    b.g.serialize(out, format="turtle")
    (RESULTS / f"graph_summary_{stage}.json").write_text(json.dumps({"triples": len(b.g), "file": out.name}, indent=1))
    print(stage, len(b.g), "triples ->", out)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "v1")
