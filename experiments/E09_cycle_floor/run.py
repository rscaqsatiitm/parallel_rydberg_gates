import sys, json, itertools, numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "experiments/E06_K3_fig6g")
import run as e6
from prg.atomic import contaminant_weights
E05 = json.load(open("experiments/E05_rates_vs_T/results.json"))
Rg, Ag, M, pct300 = e6.load_map()
S = json.load(open("experiments/E02_error_map/summary.json"))["same_weighted"]
def same_map(bd):
    RS = sorted({float(eval(k)[1]) for k in S}); A = [0.0, 90.0]; Z = np.zeros((len(RS), 2, 3))
    for k, v in S.items():
        b, R, al = eval(k)
        if b == bd: Z[RS.index(float(R)), A.index(float(al))] = v
    return np.array(RS), np.array(A), Z
JW = {}
for npr in (52, 53):
    w, _ = contaminant_weights("Rb87", 53, 0.5, npr)
    for J in (0.5, 1.5): JW[(npr, J)] = 0.5 * sum(v for k, v in w.items() if k.j == J)
def surv_sum(t, T):     # sum_{j>=1} S(j t) for the decay-only model, exact geometric sum
    tau = E05[f"{T:.1f}"]["tau_P_us"]
    return sum(wj / (np.exp(t / tau[f"{n}P{J}"]) - 1) for (n, J), wj in JW.items())
def static_atoms(pax, pkey, s):
    ax_, ay_ = e6.PITCHES[pkey]; sites = e6.lattice_sites(21, 21, ax_ * s, ay_ * s)
    tgt = np.argmin(np.linalg.norm(sites, axis=1)); srcs = np.delete(sites, tgt, axis=0)
    off = np.array([1.0, 0]) if pax == "x" else np.array([0, 1.0])
    rel = np.concatenate([np.concatenate([srcs - off, srcs + off]), np.zeros((2 * len(srcs), 1))], 1)
    return np.stack([rel[:, 1], -rel[:, 0], rel[:, 2]], 1) if pax == "y" else rel
BMAP = {"x": {"x": "x", "y": "y", "z": "z"}, "y": {"x": "y", "y": "x", "z": "z"}}
SGRID = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.7, 2.0]; TGRID = np.arange(50, 3001, 10.0)
KIN = {"BLU25_surface_L4": (1.171e3, 1.527e3), "e40_A_L10": (24.9e3, 35.5e3), "e40_B_L10": (7.40e3, 15.5e3),
       "e40_C_L10": (3.90e3, 5.55e3), "e40_D_L10": (21.4e3, 23.7e3)}
def t_cross(curve, target):
    ok = np.where(curve <= target)[0]
    return np.inf if len(ok) == 0 else float(TGRID[ok[0]])
out = {}
Z = np.load(e6.D + "trajectories.npz"); times = [float(x) for x in Z["times"]]
e6.GAPS = [50.0 * k for k in range(1, 13)]
for T in (300.0, 45.0, 4.0):
    pc = pct300 * E05[f"{T:.1f}"]["rate_to_52P_53P"] / E05["300.0"]["rate_to_52P_53P"]
    rows = []
    for Ug, w0, pax, pkey, bd in itertools.product((0.5, 1.0, 2.0), (0.8, 1.0, 1.2), "xy", e6.PITCHES, "xyz"):
        bm = BMAP[pax][bd]
        sR, sA, sZ = same_map("z" if bm == "z" else "x")
        floors = {s: pc * e6.E_interp(sR, sA, sZ, 0, static_atoms(pax, pkey, s)).sum() for s in SGRID}
        s_min = next((s for s in SGRID if floors[s] < 1e-4), np.inf)
        nfull = {s: e6.E_interp(Rg, Ag, M[bm], 0, static_atoms(pax, pkey, s)).sum() for s in SGRID}
        prev_static = lambda s: np.array([pc * nfull[s] * surv_sum(t, T) for t in TGRID])
        # motion model at s = 1 on the 50-us grid (truncated at 1200 us); rescale p_c, tau via survival patch
        tauT = E05[f"{T:.1f}"]["tau_P_us"]
        e6._SURV.clear(); e6.survival = lambda t: sum(wj * np.exp(-t / tauT[f"{n}P{J}"]) for (n, J), wj in JW.items())
        em = e6.predict(Z[str((Ug, w0, pax, pkey, False))], times, Rg, Ag, M, pc, pkey, pax, False, bd, 0, False)
        tm = np.array(sorted(em)); vm = np.array([em[t] for t in tm])
        tE_motion = {eps: (float(tm[np.argmax(vm <= eps)]) if np.any(vm <= eps) else np.inf) for eps in (1e-4, 1e-5)}
        ps1 = prev_static(1.0)
        r = dict(Ug=Ug, w0=w0, pax=pax, pkey=pkey, bd=bd, floor_s1=floors[1.0], floors=floors, s_min=s_min,
                 tE_static={eps: t_cross(ps1, eps) for eps in (1e-4, 1e-5)}, tE_motion_50grid=tE_motion,
                 tP_s1=(t_cross(floors[1.0] + ps1, 1e-4) if floors[1.0] < 1e-4 else np.inf),
                 tP_smin=(t_cross(floors[s_min] + prev_static(s_min), 1e-4) if np.isfinite(s_min) else np.inf))
        rows.append(r)
    out[T] = dict(p_c=pc, rows=rows)
    fl = [r["floor_s1"] for r in rows]; sm = [r["s_min"] for r in rows]
    tE4 = [r["tE_static"][1e-4] for r in rows]; tE5 = [r["tE_static"][1e-5] for r in rows]
    tEm = [r["tE_motion_50grid"][1e-4] for r in rows]; tPs = [r["tP_smin"] for r in rows]
    print(f"T={T:5.0f} K p_c={pc:.2e}  floor(s=1) {min(fl):.2e}-{max(fl):.2e}  s_min {min(sm)}-{max(sm)}  "
          f"tP(s=1) {'inf' if all(np.isinf([r['tP_s1'] for r in rows])) else 'finite'}  tP(s_min) {min(tPs):.0f}-{max(tPs):.0f} us  "
          f"tE(1e-4) static {min(tE4):.0f}-{max(tE4):.0f}, motion(50-us grid) {min(tEm):.0f}-{max(tEm):.0f}  tE(1e-5) static {min(tE5):.0f}-{max(tE5):.0f} us")
    for name, (klo, khi) in KIN.items():
        L = 4 if "L4" in name else 10
        for lab, tw in (("E 1e-4", tE4), ("E 1e-5", tE5), ("P at s_min", tPs)):
            lo = (L * min(tw) + 45) / khi; hi = (L * max(tw) + 500) / klo
            print(f"    {name:18s} reading {lab:11s}: T_th {L*min(tw)+45:.0f}-{L*max(tw)+500:.0f} us  ratio {lo:.2f}-{hi:.2f}")
json.dump({str(k): v for k, v in out.items()}, open("experiments/E09_cycle_floor/results.json", "w"), default=float)
