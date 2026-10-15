"""Phenotype UMAP queried from the graph, joined to image-derived phenotypes.

Primary inputs: AGE_AT_SCAN, FIQ, VIQ, PIQ for cohort B_v1, complete cases only, z-scored.
Secondary inputs: the same plus SRS_RAW_TOTAL (complete cases), to show how missingness patterns
concentrate an embedding on a few sites. Diagnosis, sex and site are never inputs; they colour the
plots. Joins: ANTs mean cortical thickness and mean CC200 Fisher z, both read from the graph.

Usage: uv run python code/umap_phenotype.py
"""

import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import umap
from rdflib import RDF, Graph, Literal, Namespace
from scipy.stats import spearmanr
from sklearn.decomposition import PCA
from sklearn.manifold import trustworthiness
from sklearn.metrics import silhouette_score
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

from common import FIGURES, GRAPH, QUERIES, RESULTS as RESULTS_DIR, SEED, sha256_bytes, write_json

E = Namespace("urn:repronim:abide:")
PROV = Namespace("http://www.w3.org/ns/prov#")
PRIMARY = ["AGE_AT_SCAN", "FIQ", "VIQ", "PIQ"]
SECONDARY = PRIMARY + ["SRS_RAW_TOTAL"]
K = 15
UMAP_PARAMS = {"n_neighbors": 15, "min_dist": 0.1, "metric": "euclidean"}
SEEDS = [SEED, 1, 2]

def query_matrix() -> pd.DataFrame:
    """Participant table from the graph: Oxigraph in memory, phenotype_matrix view, optimized query."""
    import pyoxigraph as ox

    from query_bench import OPT
    from store import VIEW_DEFS

    st = ox.Store()
    st.bulk_load(path=str(GRAPH / "abide_kg.ttl"), format=ox.RdfFormat.TURTLE, to_graph=ox.NamedNode("urn:repronim:abide:graph/core"))
    st.update(VIEW_DEFS["phenotype_matrix"][1])
    q = OPT["phenotype_matrix"]
    (QUERIES / "phenotype_matrix.rq").write_text(q)
    rows = {}
    for r in st.query(q):
        fid = r["fid"].value
        row = rows.setdefault(fid, {"FILE_ID": fid, "site": r["site"].value, "dx": "ASD" if float(r["dx"].value) == 1 else "TD",
                                    "sex": "M" if float(r["sex"].value) == 1 else "F",
                                    "thickness": float(r["thick"].value) if r["thick"] is not None else np.nan,
                                    "mean_conn": float(r["conn"].value) if r["conn"] is not None else np.nan})
        if r["var"] is not None:
            row[r["var"].value.rsplit("/", 1)[-1]] = float(r["value"].value)
    return pd.DataFrame(rows.values()).sort_values("FILE_ID").reset_index(drop=True)


def overlap(a: np.ndarray, b: np.ndarray) -> float:
    """Mean fraction of shared K nearest neighbours between two embeddings."""
    na = NearestNeighbors(n_neighbors=K + 1).fit(a).kneighbors(a, return_distance=False)[:, 1:]
    nb = NearestNeighbors(n_neighbors=K + 1).fit(b).kneighbors(b, return_distance=False)[:, 1:]
    return float(np.mean([len(set(x) & set(y)) / K for x, y in zip(na, nb)]))


def embed(df: pd.DataFrame, feats: list[str]) -> dict:
    """Complete-case z-scored UMAP with stability and structure diagnostics."""
    cc = df.dropna(subset=feats).reset_index(drop=True)
    X = StandardScaler().fit_transform(cc[feats].to_numpy())
    embs = {s: umap.UMAP(random_state=s, **UMAP_PARAMS).fit_transform(X) for s in SEEDS}
    Y = embs[SEED]
    pca = PCA(2, random_state=SEED).fit_transform(X)
    joins = {}
    for col in ("thickness", "mean_conn", "gm_FreeSurfer", "gm_ANTs", "gm_FSL", "hippo_L_FreeSurfer"):
        if col not in cc:
            continue
        ok = cc[col].notna().to_numpy()
        joins[col] = {
            "n": int(ok.sum()),
            "spearman_with_age": float(spearmanr(cc.loc[ok, col], cc.loc[ok, "AGE_AT_SCAN"]).statistic),
            "spearman_with_umap1": float(spearmanr(cc.loc[ok, col], Y[ok, 0]).statistic),
            "spearman_with_umap2": float(spearmanr(cc.loc[ok, col], Y[ok, 1]).statistic),
        }
    return {
        "cc": cc, "Y": Y,
        "summary": {
            "features": feats,
            "n_complete_cases": len(cc),
            "n_dropped_missing": int(len(df) - len(cc)),
            "by_dx": cc.dx.value_counts().to_dict(),
            "n_sites": int(cc.site.nunique()),
            "trustworthiness_umap": float(trustworthiness(X, Y, n_neighbors=K)),
            "trustworthiness_pca": float(trustworthiness(X, pca, n_neighbors=K)),
            "trustworthiness_other_seeds": [float(trustworthiness(X, embs[s], n_neighbors=K)) for s in SEEDS[1:]],
            "neighbour_overlap_vs_other_seeds": [overlap(Y, embs[s]) for s in SEEDS[1:]],
            "silhouette_by_dx": float(silhouette_score(Y, cc.dx)),
            "silhouette_by_site": float(silhouette_score(Y, cc.site)),
            "joins": joins,
            "embedding_sha256": sha256_bytes(np.round(Y, 6).tobytes()),
        },
    }


def plot(res: dict, stem: str, title: str) -> None:
    """Four-panel figure: diagnosis, site, age, thickness."""
    cc, Y = res["cc"], res["Y"]
    fig, ax = plt.subplots(1, 5, figsize=(22, 4.4), constrained_layout=True)
    for g_, c in (("TD", "#4C72B0"), ("ASD", "#DD8452")):
        m = cc.dx == g_
        ax[0].scatter(Y[m, 0], Y[m, 1], s=7, c=c, label=f"{g_} (n={m.sum()})", alpha=0.7)
    ax[0].legend(frameon=False, fontsize=8)
    ax[0].set_title("Diagnosis (not an input)")
    sites = sorted(cc.site.unique())
    cmap = plt.get_cmap("tab20", len(sites))
    for i, s in enumerate(sites):
        m = cc.site == s
        ax[1].scatter(Y[m, 0], Y[m, 1], s=7, color=cmap(i), label=s, alpha=0.8)
    ax[1].legend(frameon=False, fontsize=6, ncol=2, markerscale=1.5)
    ax[1].set_title(f"Site (not an input; {len(sites)} sites)")
    sc = ax[2].scatter(Y[:, 0], Y[:, 1], s=7, c=cc.AGE_AT_SCAN, cmap="viridis")
    fig.colorbar(sc, ax=ax[2], label="age (years)")
    ax[2].set_title("Age (an input)")
    sc = ax[3].scatter(Y[:, 0], Y[:, 1], s=7, c=cc.thickness, cmap="magma")
    fig.colorbar(sc, ax=ax[3], label="mean cortical thickness (mm)")
    ax[3].set_title("Image-derived: ANTs thickness (ABIDE Preprocessed)")
    sc = ax[4].scatter(Y[:, 0], Y[:, 1], s=7, c=cc.gm_FreeSurfer / 1000, cmap="cividis")
    fig.colorbar(sc, ax=ax[4], label="cortical GM volume, FreeSurfer (cm³)")
    ax[4].set_title("Image-derived: ReproNim simple2 NIDM (joined)")
    for a in ax:
        a.set_xticks([])
        a.set_yticks([])
    fig.suptitle(title, fontsize=11)
    for ext in ("png", "pdf"):
        fig.savefig(FIGURES / f"{stem}.{ext}", dpi=160)
    plt.close(fig)


def provenance(summary: dict, stem: str) -> None:
    """Record the embedding choices as a PROV activity in graph/embedding_provenance.ttl."""
    g = Graph()
    g.bind("ex", E)
    g.bind("prov", PROV)
    act = E[f"activity/{stem}"]
    out = E[f"embedding/{stem}"]
    g.add((act, RDF.type, PROV.Activity))
    g.add((act, PROV.used, E["cohort/B_v1"]))
    g.add((act, E.query, Literal("queries/phenotype_matrix.rq")))
    g.add((act, E.features, Literal(", ".join(summary["features"]))))
    g.add((act, E.missingness, Literal("complete cases only; -9999 and empty treated as missing; no imputation")))
    g.add((act, E.scaling, Literal("z-score per feature on complete cases")))
    g.add((act, E.umapParams, Literal(json.dumps({**UMAP_PARAMS, "random_state": SEED}))))
    g.add((act, E.excludedFromInputs, Literal("diagnosis, sex, site")))
    g.add((out, RDF.type, PROV.Entity))
    g.add((out, PROV.wasGeneratedBy, act))
    g.add((out, E.sha256, Literal(summary["embedding_sha256"])))
    g.add((out, E.nParticipants, Literal(summary["n_complete_cases"])))
    path = GRAPH / "embedding_provenance.ttl"
    if path.exists():
        g += Graph().parse(path)
    g.serialize(path, format="turtle")


def main() -> None:
    """Query, embed, assess, plot, record."""
    df = query_matrix()
    s2 = pd.read_csv(RESULTS_DIR / "simple2_idps.csv")
    df = df.merge(s2[["FILE_ID"] + [c for c in s2.columns if c.startswith(("gm_", "hippo_L_"))]], on="FILE_ID", how="left")
    (GRAPH / "embedding_provenance.ttl").unlink(missing_ok=True)
    out = {"query": "queries/phenotype_matrix.rq", "n_cohort_rows": len(df)}
    for stem, feats, title in (
        ("umap_primary", PRIMARY, "Phenotype UMAP (age, FIQ, VIQ, PIQ), cohort B_v1 complete cases"),
        ("umap_with_srs", SECONDARY, "Adding SRS: complete cases collapse to the few sites that collected it"),
    ):
        res = embed(df, feats)
        plot(res, stem, title)
        provenance(res["summary"], stem)
        res["cc"].assign(umap1=res["Y"][:, 0], umap2=res["Y"][:, 1]).to_csv(FIGURES.parent / "results" / f"{stem}_coordinates.csv", index=False)
        out[stem] = res["summary"]
    write_json("umap.json", out)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
