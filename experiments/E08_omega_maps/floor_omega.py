# Derived application (not a pre-registered verdict): same-layer floor p_c * sum_i E_same(r_i) in the BLU25 zone
# geometry (D008, normal spacing, both pitch assignments, pair axis x/y, B x/y/z) vs Omega, with the E07
# floor procedure unchanged. At 4.6 MHz uses E02's 12-point E_same (reproduces E07 range = method control).
import sys, json, itertools, importlib.util, numpy as np
sys.path[0:0] = ["src", "experiments/E08_omega_maps"]
_sp = importlib.util.spec_from_file_location("e6run", "experiments/E06_K3_fig6g/run.py"); e6 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(e6)
from analyse import load
RS_ = [4, 6, 8, 10, 12, 14, 17, 20, 25, 30, 40]
def maps(om):
    if om == 4.6:
        S = json.load(open("experiments/E02_error_map/summary.json"))["same_weighted"]; pc = load(4.6)["p_c"]
        RS = sorted({float(eval(k)[1]) for k in S}); out = {}
        for bd in "xz":
            Z = np.zeros((len(RS), 2, 3))
            for k, v in S.items():
                b, R, al = eval(k)
                if b == bd: Z[RS.index(float(R)), (0, 90).index(al)] = v
            out[bd] = Z
        return np.array(RS), out, pc
    r = load(om); out = {}
    for bd in "xz":
        Z = np.zeros((len(RS_), 2, 3))
        for i, R in enumerate(RS_):
            for j, al in enumerate((0, 90)): Z[i, j, 0] = r["same"][(bd, R, al)]
        out[bd] = Z
    return np.array(RS_, float), out, r["p_c"]
res = {}
for om in (2.3, 4.6, 9.2, 18.4):
    Rg, Z, pc = maps(om); vals = []
    for pax, pkey, bd in itertools.product("xy", e6.PITCHES, "xyz"):
        ax_, ay_ = e6.PITCHES[pkey]; sites = e6.lattice_sites(15, 15, ax_, ay_)
        tgt = np.argmin(np.linalg.norm(sites, axis=1)); srcs = np.delete(sites, tgt, axis=0)
        off = np.array([1.0, 0]) if pax == "x" else np.array([0, 1.0])
        atoms = np.concatenate([srcs - off, srcs + off]); rel = np.concatenate([atoms, np.zeros((len(atoms), 1))], 1)
        if pax == "y": rel = np.stack([rel[:, 1], -rel[:, 0], rel[:, 2]], 1)
        bm = {"x": {"x": "x", "y": "y", "z": "z"}, "y": {"x": "y", "y": "x", "z": "z"}}[pax][bd]
        vals.append(pc * e6.E_interp(Rg, np.array([0.0, 90.0]), Z["z" if bm == "z" else "x"], 0, rel).sum())
    res[om] = (min(vals), max(vals)); print(f"Omega/2pi {om:5} MHz  p_c {pc:.3e}  floor per CZ (300 K) {min(vals):.2e} .. {max(vals):.2e}")
o = sorted(res); 
for a, b in zip(o[:-1], o[1:]):
    print(f"  local exponent {a}->{b} MHz: {np.log(res[b][0]/res[a][0])/np.log(b/a):+.2f} (min) {np.log(res[b][1]/res[a][1])/np.log(b/a):+.2f} (max)")
json.dump({str(k): v for k, v in res.items()}, open("experiments/E08_omega_maps/floor_omega.json", "w"))
