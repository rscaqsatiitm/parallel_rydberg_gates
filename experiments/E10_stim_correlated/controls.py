"""E10 controls C1-C4 (pre-registered in README)."""
import sys, json, numpy as np, stim
sys.path.insert(0, "experiments/E10_stim_correlated")
from model import build, layer_noise, PITCH
from sim import run, wilson
out = {}
# C1 planted zero
base, _ = build(5, 1e-3, 1, "base")
dz = {m: build(5, 1e-3, 1, m, scale_check=0.0)[0] for m in ("corr", "indep")}
kw = dict(decompose_errors=True, approximate_disjoint_errors=True, ignore_decomposition_failures=True)
db = str(base.detector_error_model(**kw))
c1 = {m: str(c.detector_error_model(**kw)) == db for m, c in dz.items()}
out["C1"] = dict(equal=c1, PASS=all(c1.values())); print("C1", out["C1"], flush=True)
# C2 / C3 marginal test on one layer of the d = 7 circuit
b7, _ = build(7, 0.0, 1, "base"); coords = b7.get_final_qubit_coordinates()
cx = [ins for ins in b7 if ins.name == "CX"][0]; t = [x.value for x in cx.targets_copy()]; pairs = list(zip(t[::2], t[1::2]))
qs = sorted({q for pr in pairs for q in pr}); N = 2_000_000
def marg_test(mode, mult):
    noise, f_true = layer_noise(pairs, coords, mult, mode, rng=np.random.default_rng(3))
    _, f_ref = layer_noise(pairs, coords, 100, "indep")          # reference marginals (correct inputs)
    c = stim.Circuit(); c.append("R", qs); c += noise; c.append("M", qs)
    s = c.compile_sampler(seed=11).sample(N).astype(np.float64); col = {q: i for i, q in enumerate(qs)}
    z = []
    for j, (a, b) in enumerate(pairs):
        for q in (a, b):
            r = s[:, col[q]].mean(); exp = f_ref[j] / 2; z.append((r - exp) / np.sqrt(exp * (1 - exp) / N))
    # joint excess between x-nearest neighbour pairs (first qubits)
    cen = {j: ((coords[a][0] + coords[b][0]) / 2, (coords[a][1] + coords[b][1]) / 2) for j, (a, b) in enumerate(pairs)}
    nb = [(j, k) for j in cen for k in cen if j < k and abs(cen[j][1] - cen[k][1]) < 1e-9 and abs(abs(cen[j][0] - cen[k][0]) - 4) < 1e-9]   # co-cluster: both x-neighbours of the site between
    zj = []
    for j, k in nb:
        x, y = s[:, col[pairs[j][0]]], s[:, col[pairs[k][0]]]; cov = (x * y).mean() - x.mean() * y.mean()
        zj.append(cov / np.sqrt(x.mean() * y.mean() / N))
    return dict(max_abs_z_marg=float(np.max(np.abs(z))), mean_f=float(np.mean(f_ref)), n_nb=len(nb),
                min_z_joint=float(np.min(zj)), max_z_joint=float(np.max(zj)), mean_z_joint=float(np.mean(zj)))
c2c = marg_test("corr", 100); c2i = marg_test("indep", 100)
out["C2"] = dict(corr=c2c, indep=c2i, PASS=bool(c2c["max_abs_z_marg"] < 4 and c2i["max_abs_z_marg"] < 4
                 and c2c["mean_z_joint"] > 4 and abs(c2i["mean_z_joint"]) < 4)); print("C2", out["C2"], flush=True)
c3 = marg_test("corr", 200)   # amended: p_c doubled (E_same x 2 exceeds 1)
out["C3"] = dict(corr_pc_doubled=c3, caught=bool(c3["max_abs_z_marg"] >= 4)); print("C3", out["C3"], flush=True)
# C4 null: pitch x 10
res = {}
for m in ("base", "corr", "indep"):
    k = run(3, 1e-3, 10, m, 1_000_000, pitch=(PITCH[0] * 10, PITCH[1] * 10)); res[m] = (k, wilson(k, 1_000_000))
ov = all(max(res[a][1][0], res[b][1][0]) <= min(res[a][1][2], res[b][1][2]) for a in res for b in res)
out["C4"] = dict(fails={m: res[m][0] for m in res}, PASS=bool(ov)); print("C4", out["C4"], flush=True)
json.dump(out, open("experiments/E10_stim_correlated/controls.json", "w"), indent=1)
