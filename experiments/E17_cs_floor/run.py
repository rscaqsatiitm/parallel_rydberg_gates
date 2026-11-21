# E17 (pre-registered README). Run from repo root.
import sys, json, numpy as np
from scipy.linalg import expm
sys.path.insert(0, "src")
from prg.probe import ProbePair
from prg.atomic import contaminant_weights
from prg.bath import Bath
AS = [3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30]; OMS = [0.5, 1.0, 2.0, 5.0]; TEFF = [300.0, 1e3, 3e3, 1e4]; CS = [0.90, 0.95]
C6 = 101.6e3                                    # |C6| MHz um^6 (ARC, README)
RS = sorted({a * k for a in AS for k in (1, 2)})
# m' weights over 59P and 60P (isotropic, 300 K)
w = {}
for npr in (59, 60):
    ww, rates = contaminant_weights("Cs133", 60, 0.5, npr)
    for lv, x in ww.items(): w[lv] = x * sum(rates.values())
tot = sum(w.values()); w = {k: v / tot for k, v in w.items()}
def e_same_all(pp, levs, R, Om, nt=12):
    """Return {level: E_same} using one eigendecomposition per Hamiltonian (exact for piecewise-constant H)."""
    T = 1.0 / Om; dt = T / nt; tons = (np.arange(nt) + 0.5) * dt
    pr = np.sin(np.pi * Om * tons) ** 2; pr /= pr.sum()               # sin^2(Omega t / 2), Omega = 2 pi Om
    L = np.zeros((pp.dPr, pp.dPr), complex); L[1 + pp.ir, 0] = 1; Lp = (L + L.conj().T) / 2
    ep, Vp = np.linalg.eigh(pp.hP + Om * Lp); ef, Vf = np.linalg.eigh(pp.H0 + pp.Vdd(R, np.pi / 2) + Om * pp.Ldrive)
    U = lambda e, V, t: (V * np.exp(-2j * np.pi * e * t)) @ V.conj().T
    out = {lv: 0.0 for lv in levs}
    for t, p in zip(tons, pr):
        psi_p = U(ep, Vp, t)[:, 0]; Uf = U(ef, Vf, T - t)
        for lv in levs:
            psi = Uf @ pp.state(psi_p, lv)
            out[lv] += p * (1 - float(np.real(pp.probe_rho(psi)[0, 0])))
    return out
K = {}
for npr in (59, 60):
    pp = ProbePair("Cs133", 60, npr, 5.0)
    for Om in OMS:
        for R in RS:
            levs = [lv for lv in w if lv.n == npr]; es = e_same_all(pp, levs, R, Om)
            K[(Om, R)] = K.get((Om, R), 0) + sum(w[lv] * es[lv] for lv in levs)
print("E_same(R) theta 90:"); [print(f"  Omega {Om}: " + " ".join(f"{R:g}:{K[(Om,R)]:.3g}" for R in RS if R <= 30)) for Om in OMS]
b = Bath(cache="experiments/E13_cs_bath/levels_A.npz"); N = len(b.levels)
S60 = b.idx[(60, 0, 0.5)]; RES = [b.idx[(n, 1, j)] for n in (59, 60) for j in (0.5, 1.5)]
def pc_gamma(T_eff, Om):
    M = b.generator(T_eff, (13.6e9, 24.8e9)); w_, V = np.linalg.eig(M); P0 = np.zeros(N); P0[S60] = 1
    P = np.real(V @ (np.exp(w_ * (0.5 / Om) * 1e-6) * np.linalg.solve(V, P0)))
    G = b.rates(T_eff, (13.6e9, 24.8e9))[S60].sum() + b.sink[S60]
    return float(P[RES].sum()), float(G * 1e-6)
PC = {(T, Om): pc_gamma(T, Om) for T in TEFF for Om in OMS}
rows = []
for Om in OMS:
    for a in AS:
        v1 = C6 / a ** 6 <= 0.1 * Om
        for T in TEFF:
            pc, Gp = PC[(T, Om)]; pc0 = PC[(300.0, Om)][0]
            # mean over 3 atoms on a line: end atoms have 1 neighbour at a and 1 at 2a; middle has 2 at a
            eps = pc * ((2 * K[(Om, a)] + 2 * K[(Om, 2 * a)]) + 2 * K[(Om, a)]) / 3
            eps300 = pc0 * (4 * K[(Om, a)] + 2 * K[(Om, 2 * a)]) / 3
            d = eps - eps300
            v2, v3 = 3 * pc <= 0.1, Gp / Om <= 0.1
            sh = {C: (2 * (1 - C + eps) * (C - eps) / (3 * C ** 2 * (0.1 * d) ** 2) if T > 300.0 and d > 0 else None) for C in CS}
            rows.append(dict(Omega=Om, a=a, T_eff=T, p_c=pc, eps=eps, eps_minus_300=d, V1=v1, V2=v2, V3=v3,
                             shots_C090=sh[0.90], shots_C095=sh[0.95]))
json.dump(dict(C6_MHz_um6=-C6, kernel={f"{k[0]} {k[1]}": v for k, v in K.items()}, p_c={f"{k[0]} {k[1]}": v for k, v in PC.items()}, rows=rows),
          open("experiments/E17_cs_floor/results.json", "w"), indent=1)
for T in TEFF:
    print(f"\nT_eff {T:g} K: eps per atom [shots C=0.90] (flags: v = vdW crosstalk V1 violated, s = V2, b = V3)")
    for Om in OMS:
        line = f"  Omega {Om:3}: p_c {PC[(T, Om)][0]:.2e} |"
        for r in [r for r in rows if r["Omega"] == Om and r["T_eff"] == T]:
            fl = ("" if r["V1"] else "v") + ("" if r["V2"] else "s") + ("" if r["V3"] else "b")
            line += f" {r['a']}:{r['eps']:.1e}" + (f"[{r['shots_C090']:.0e}]" if r["shots_C090"] else "") + (f"{fl}" if fl else "")
        print(line)
