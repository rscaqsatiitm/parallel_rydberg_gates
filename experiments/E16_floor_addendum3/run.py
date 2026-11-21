# E16 (pre-registered README). Run from repo root.
import sys, json, itertools, importlib.util, numpy as np
sys.path[0:0] = ["src", "experiments/E02_error_map"]
_sp = importlib.util.spec_from_file_location("e6run", "experiments/E06_K3_fig6g/run.py"); e6 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(e6)
import run as e2
from prg.atomic import get_atom, contaminant_weights
from prg.model import Config, ThreeAtom, contaminant_increment
a = get_atom("Rb87"); E02 = json.load(open("experiments/E02_error_map/results.json"))
T, IRT = E02["T_us"], E02["I_r_over_T"]; IR = T * IRT * 1e-6
S = json.load(open("experiments/E02_error_map/summary.json"))
def amap(kind, bd):
    d = {eval(k): v for k, v in S[kind].items() if eval(k)[0] == bd}
    RS = sorted({k[1] for k in d}); AL = sorted({k[2] for k in d})
    Z = np.zeros((len(RS), len(AL), 3))
    for (b, R, al), v in d.items(): Z[RS.index(R), AL.index(al)] = v
    return np.array(RS, float), np.array(AL, float), Z
# ---- BBR rates into every n'P (300 K)
def rate(n2):
    r = 0.0
    for j in (0.5, 1.5):
        rT = a.getTransitionRate(53, 0, 0.5, n2, 1, j, temperature=300.0)
        down = a.getEnergy(n2, 1, j) < a.getEnergy(53, 0, 0.5)
        r += rT - (a.getTransitionRate(53, 0, 0.5, n2, 1, j, temperature=0) if down else 0.0)
    return r
NP = [n for n in range(33, 74)]
G = {n: rate(n) for n in NP}
r2 = {n: a.getRadialMatrixElement(53, 0, 0.5, n, 1, 1.5) ** 2 for n in NP}
C3res = (G[52] * r2[52] + G[53] * r2[53]) / (G[52] + G[53])
pc_res = (G[52] + G[53]) * IR
extra = [n for n in NP if n not in (52, 53)]
scale = {n: (C3res / r2[n]) ** (1 / 3) for n in extra}         # R -> R * scale
tot_bbr = 1 / a.getStateLifetime(53, 0, 0.5, temperature=300.0, includeLevelsUpTo=93) - 1 / a.getStateLifetime(53, 0, 0.5, temperature=0, includeLevelsUpTo=93)
print(f"p_c resonant {pc_res:.4e}; extra-channel rate {sum(G[n] for n in extra):.0f}/s of total {tot_bbr:.0f}/s "
      f"(resonant {G[52]+G[53]:.0f}); top extra: " + ", ".join(f"{n}P {G[n]:.0f}/s C3 ratio {r2[n]/C3res:.3f}" for n in sorted(extra, key=lambda n: -G[n])[:6]))
# ---- control: direct E_same for n' = 51, 54 vs rescaled
ts, pr, _ = e2.rydberg_population(); edges = np.linspace(0, T, 7); tons = 0.5 * (edges[1:] + edges[:-1])
wt = np.array([np.trapezoid(pr[(ts >= x) & (ts < y)], ts[(ts >= x) & (ts < y)]) for x, y in zip(edges[:-1], edges[1:])]); wt /= wt.sum()
sR, sA, sZ = amap("same_weighted", "z"); ctrl = {}
for npr in (51, 54):
    m = ThreeAtom(Config(nprime=npr, bfield_dir=(0, 0, 1.0)))
    w, _ = contaminant_weights("Rb87", 53, 0.5, npr); c0s = [m.ryd.index(lv) for lv in w if w[lv] > 0]; ws = np.array([w[m.ryd[c]] for c in c0s])
    base = contaminant_increment(m, (1e4, 0, 0), c0s)[1]
    for R in (8.571, 12.0, 17.0):
        Ed = sum(wt[i] * (ws * np.array([contaminant_increment(m, (R, 0, 0), c0s, t_on=tons[i], baseline=base)[0][c][0] for c in c0s])).sum() for i in range(6))
        Er = float(e6.E_interp(sR, sA, sZ, 0, np.array([[R * scale[npr], 0, 0]]))[0])
        ctrl[f"{npr} {R}"] = (Ed, Er); print(f"control n'={npr} R={R}: direct {Ed:.3e} rescaled {Er:.3e} ratio {Er/Ed if Ed else float('nan'):.2f}")
# ---- floors
def geom(pitch_pair, pax):
    ax_, ay_ = pitch_pair; sites = e6.lattice_sites(21, 21, ax_, ay_)
    tgt = np.argmin(np.linalg.norm(sites, axis=1)); srcs = np.delete(sites, tgt, axis=0)
    off = np.array([1.0, 0]) if pax == "x" else np.array([0, 1.0])
    atoms = np.concatenate([srcs - off, srcs + off]); rel = np.concatenate([atoms, np.zeros((len(atoms), 1))], 1)
    if pax == "y": rel = np.stack([rel[:, 1], -rel[:, 0], rel[:, 2]], 1)
    return rel
TAU = [96.0, 102.0]; out = {"control": ctrl, "rows": []}
for pitch in (8.571, 10.0):
    for (pp, pax, bd) in itertools.product([(12.0, pitch), (pitch, 12.0)], "xy", "xyz"):
        rel = geom(pp, pax)
        bm = {"x": {"x": "x", "y": "y", "z": "z"}, "y": {"x": "y", "y": "x", "z": "z"}}[pax][bd]; mb = "z" if bm == "z" else "x"
        sR, sA, sZ = amap("same_weighted", mb); fR, fA, fZ = amap("full_weighted", mb)
        res = pc_res * e6.E_interp(sR, sA, sZ, 0, rel).sum()
        ext = sum(G[n] * IR * e6.E_interp(sR, sA, sZ, 0, rel * scale[n]).sum() for n in extra)
        nfull = e6.E_interp(fR, fA, fZ, 0, rel).sum()
        nfull_x = sum(G[n] * IR * e6.E_interp(fR, fA, fZ, 0, rel * scale[n]).sum() for n in extra)
        prev = [(pc_res * nfull + nfull_x) / np.expm1(400.0 / tau) for tau in TAU]
        out["rows"].append(dict(pitch=pitch, pp=pp, pax=pax, bd=bd, res=res, extra=ext, prev_lo=min(prev), prev_hi=max(prev)))
json.dump(out, open("experiments/E16_floor_addendum3/results.json", "w"), indent=1)
for pitch in (8.571, 10.0):
    R = [r for r in out["rows"] if r["pitch"] == pitch]
    f = lambda k: (min(r[k] for r in R), max(r[k] for r in R))
    tot = [r["res"] + r["extra"] + r["prev_hi"] for r in R]
    fac = [(r["res"] + r["extra"]) / r["res"] for r in R]
    print(f"pitch {pitch}: resonant {f('res')[0]:.2e}-{f('res')[1]:.2e} | extra {f('extra')[0]:.2e}-{f('extra')[1]:.2e} | "
          f"earlier@400us {min(r['prev_lo'] for r in R):.2e}-{max(r['prev_hi'] for r in R):.2e} | total {min(tot):.2e}-{max(tot):.2e} | "
          f"same-layer factor {min(fac):.3f}-{max(fac):.3f} | total/resonant {min(t/r['res'] for t, r in zip(tot, R)):.3f}-{max(t/r['res'] for t, r in zip(tot, R)):.3f}")
