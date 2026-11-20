# Post-hoc consistency check (NOT pre-registered; the data had been seen): same-layer floor, Normal vs Sparse.
import sys, json, itertools, numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "experiments/E06_K3_fig6g")
import run as e6
S = json.load(open("experiments/E02_error_map/summary.json"))["same_weighted"]
def same_map(bd):
    RS = sorted({float(eval(k)[1]) for k in S}); A = [0.0, 90.0]; Z = np.zeros((len(RS), 2, 3))
    for k, v in S.items():
        b, R, al = eval(k)
        if b == bd: Z[RS.index(float(R)), A.index(float(al))] = v
    return np.array(RS), np.array(A), Z
Rg, Ag, M, pct = e6.load_map(); out = {}
for sparse in (False, True):
    vals = []
    for pax, pkey, bd in itertools.product("xy", e6.PITCHES, "xyz"):
        s = 2.0 if sparse else 1.0; ax_, ay_ = e6.PITCHES[pkey]; sites = e6.lattice_sites(15, 15, ax_ * s, ay_ * s)
        tgt = np.argmin(np.linalg.norm(sites, axis=1)); srcs = np.delete(sites, tgt, axis=0)
        off = np.array([1.0, 0]) if pax == "x" else np.array([0, 1.0])
        atoms = np.concatenate([srcs - off, srcs + off]); rel = np.concatenate([atoms, np.zeros((len(atoms), 1))], 1)
        if pax == "y": rel = np.stack([rel[:, 1], -rel[:, 0], rel[:, 2]], 1)
        bm = {"x": {"x": "x", "y": "y", "z": "z"}, "y": {"x": "y", "y": "x", "z": "z"}}[pax][bd]
        sR, sA, sZ = same_map("z" if bm == "z" else "x"); vals.append(pct * e6.E_interp(sR, sA, sZ, 0, rel).sum())
    out[sparse] = vals; print("sparse" if sparse else "normal", "floor min/max %.2e %.2e" % (min(vals), max(vals)))
d = [a - b for a in out[False] for b in out[True]]
print("normal - sparse floor difference x f (0.8..1.0): %.2e .. %.2e" % (0.8 * min(d), max(d)))
