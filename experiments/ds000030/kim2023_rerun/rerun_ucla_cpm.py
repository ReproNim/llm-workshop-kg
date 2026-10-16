# /// script
# dependencies = ["numpy", "scipy", "scikit-learn"]
# ///
"""Python port of Kim et al. 2023 UCLA_code.m (OSF agqtn): CPM edge selection + linear SVM, leave-one-subject-out."""
import json, numpy as np, scipy.io as sio
from scipy import stats
from sklearn.svm import SVC
m = sio.loadmat("UCLA_data.mat")
X = m["Connectivity"]; y = m["class"].ravel().astype(int)
n_node, _, n = X.shape
iu = np.triu_indices(n_node, 1)
E = X[iu[0], iu[1], :].T          # subjects x edges (upper triangle == full-matrix sum / 2)
pred = {"increased": np.zeros(n, int), "decreased": np.zeros(n, int), "both": np.zeros(n, int)}
for i in range(n):
    tr = np.arange(n) != i
    Et, yt = E[tr], y[tr]
    Ec = Et - Et.mean(0); yc = yt - yt.mean()
    r = (Ec * yc[:, None]).sum(0) / np.sqrt((Ec**2).sum(0) * (yc**2).sum())
    t = r * np.sqrt((tr.sum() - 2) / (1 - r**2)); p = 2 * stats.t.sf(np.abs(t), tr.sum() - 2)
    pos, neg = (r > 0) & (p < 0.05), (r < 0) & (p < 0.05)
    fp, fn = Et[:, pos].sum(1), Et[:, neg].sum(1)
    tp, tn = E[i, pos].sum(), E[i, neg].sum()
    for name, F, f in (("increased", fp[:, None], [[tp]]), ("decreased", fn[:, None], [[tn]]),
                       ("both", np.c_[fp, fn], [[tp, tn]])):
        pred[name][i] = SVC(kernel="linear", C=1.0).fit(F, yt).predict(f)[0]
acc = {k: float((v == y).mean()) for k, v in pred.items()}
out = {"n": int(n), "patients": int(y.sum()), "controls": int((1 - y).sum()), "accuracy": acc,
       "correct_both": int((pred["both"] == y).sum()), "reported_both": 0.702}
print(json.dumps(out, indent=1)); json.dump(out, open("rerun_ucla_cpm.json", "w"), indent=1)
