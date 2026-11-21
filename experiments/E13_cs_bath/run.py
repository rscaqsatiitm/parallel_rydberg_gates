# E13 (pre-registered README): bath rate model, polarisation factors, kernel m'-dependence.
import sys, json, numpy as np
sys.path.insert(0, "src")
from prg.bath import Bath, nbar
from prg.atomic import get_atom, dipole_q, Level
from prg.probe import ProbePair
a = get_atom("Cs133"); b = Bath(cache="experiments/E13_cs_bath/levels_A.npz"); L = b.levels; N = len(L)
BANDS = {"narrow": (13.6e9, 24.8e9), "broad": (1e9, 100e9)}
TEFF = [300, 1e3, 3e3, 1e4, 3e4, 1e5, 3e5, 1e6]
S60 = b.idx[(60, 0, 0.5)]; RES = [b.idx[(n, 1, j)] for n in (59, 60) for j in (0.5, 1.5)]; P59 = b.idx[(59, 1, 1.5)]
IR = 0.1925 * 1.215 / 1.0 * 1e-6                      # s, Omega/2pi = 1 MHz
def aug(Teff, band, inv_g=False):
    W = b.rates(Teff, band)
    if inv_g:                                           # corrupted input: degeneracy ratio inverted
        g = b.g(); nu = np.abs(b.E[:, None] - b.E[None, :]); nb = np.nan_to_num(nbar(np.maximum(nu, 1), Teff))
        W = b.A * (1 + nb) + (b.A.T * (g[:, None] / g[None, :])) * nb
    M = np.zeros((N + 1, N + 1)); M[:N, :N] = W.T - np.diag(W.sum(1) + b.sink); M[N, :N] = b.sink
    return W, M
def evolve(M, P0, ts):
    w, V = np.linalg.eig(M); c = np.linalg.solve(V, P0)
    return np.array([np.real(V @ (np.exp(w * t) * c)) for t in ts])
out = {"controls": {}}
# ---- controls
W, M = aug(300.0, (0, 0))
up = W[S60, b.idx[(60, 1, 1.5)]]; ref = a.getTransitionRate(60, 0, 0.5, 60, 1, 1.5, temperature=300.0)
out["controls"]["upward_rel_dev"] = abs(up / ref - 1)
Wc, _ = aug(300.0, (0, 0), inv_g=True); out["controls"]["corrupted_rel_dev"] = abs(Wc[S60, b.idx[(60, 1, 1.5)]] / ref - 1)
tot59 = W[P59].sum() + b.sink[P59]; out["controls"]["P59_total_vs_ARC"] = tot59 * a.getStateLifetime(59, 1, 1.5, temperature=300.0, includeLevelsUpTo=99)
P0 = np.zeros(N + 1); P0[S60] = 1; out["controls"]["conservation"] = float(abs(evolve(M, P0, [1e-4])[0].sum() - 1))
nuW = np.abs(b.E[:, None] - b.E[None, :])[b.A > 0]; out["controls"]["min_window_line_GHz_outside"] = None
print("controls:", out["controls"])
# ---- (a) gate exposure, (b) survival
TS = np.array([0, 10, 20, 50, 100, 150, 200, 300, 500, 750, 1000]) * 1e-6
for bn, band in BANDS.items():
    for T in TEFF:
        W, M = aug(T, band)
        P0 = np.zeros(N + 1); P0[S60] = 1; Pg = evolve(M, P0, [IR])[0]
        lin = W[S60, RES].sum() * IR
        P0 = np.zeros(N + 1); P0[P59] = 1; Pon = evolve(M, P0, TS)
        _, Moff = aug(300.0, (0, 0)); Poff = evolve(Moff, P0, TS)
        def tau(P):
            s = P[:, RES].sum(1); k = np.argmax(s < np.exp(-1))
            return float(np.interp(np.exp(-1), [s[k], s[k - 1]], [TS[k], TS[k - 1]]) * 1e6) if s[-1] < np.exp(-1) else None
        tfine = np.linspace(0, 20e-6, 201); sfine = evolve(M, P0, tfine)[:, RES].sum(1)
        tau_on = tau(Pon) or None
        if Pon[1, RES].sum() < np.exp(-1): tau_on = float(np.interp(np.exp(-1), sfine[::-1], tfine[::-1]) * 1e6)
        Gp = W[S60].sum() + b.sink[S60]
        out[f"{bn} {T:g}"] = dict(p_c=float(Pg[RES].sum()), p_lin=float(lin), P_S60=float(Pg[S60]), P_other=float(1 - Pg[RES].sum() - Pg[S60] - Pg[N]),
                                  P_sink=float(Pg[N]), tau_res_on_us=tau_on, tau_res_off_us=tau(Poff),
                                  S_on={f"{t*1e6:g}": float(p) for t, p in zip(TS, Pon[:, RES].sum(1))},
                                  S_off={f"{t*1e6:g}": float(p) for t, p in zip(TS, Poff[:, RES].sum(1))},
                                  end_on_100us=dict(res=float(Pon[4, RES].sum()), S60=float(Pon[4, S60]), other=float(1 - Pon[4, RES].sum() - Pon[4, S60] - Pon[4, N]), sink=float(Pon[4, N])),
                                  Gamma_probe_per_us=float(Gp * 1e-6))
        o = out[f"{bn} {T:g}"]
        print(f"{bn:6} T_eff {T:8.0f}: p_c {o['p_c']:.3e} lin {o['p_lin']:.3e} ratio {o['p_c']/o['p_lin']:.3f} | S60 {o['P_S60']:.3f} other {o['P_other']:.2e} sink {o['P_sink']:.2e}"
              f" | tau_res on {o['tau_res_on_us']} off {o['tau_res_off_us']} us | 100us on: {o['end_on_100us']} | Gprobe {o['Gamma_probe_per_us']:.3g}/us")
# ---- (c) polarisation factors (pure angular, ARC radial elements cancel within a level pair)
def ratio(i, fl, eps):
    num = sum(abs(sum(c * dipole_q("Cs133", f, i, q) for q, c in eps.items())) ** 2 for f in fl)
    iso = sum(dipole_q("Cs133", f, i, q) ** 2 for f in fl for q in (-1, 0, 1)) / 3
    return num / iso
POL = {"pi": {0: 1}, "sigma+": {1: 1}, "sigma-": {-1: 1}}
def beams(i, fl):
    r = {k: ratio(i, fl, e) for k, e in POL.items()}
    r["axial"] = (r["sigma+"] + r["sigma-"]) / 2; r["perp"] = (r["pi"] + r["axial"]) / 2; return r
from prg.atomic import manifold
pf = {}
S = Level(60, 0, 0.5, 0.5)
for nn in (59, 60):
    for J in (0.5, 1.5):
        pf[f"60S1/2 +1/2 -> {nn}P{J}"] = beams(S, [l for l in manifold(nn, 1) if l.j == J])
for m in (1.5, 0.5):
    i = Level(59, 1, 1.5, m)
    pf[f"59P3/2 {m:+} -> 60S1/2"] = beams(i, manifold(60, 0))
    pf[f"59P3/2 {m:+} -> 58D5/2"] = beams(i, [l for l in manifold(58, 2) if l.j == 2.5])
out["polarisation"] = pf
for k, v in pf.items(): print(k, {a_: round(x, 4) for a_, x in v.items()})
# m'-resolved contaminant weights for each polarisation from 60S +1/2 into 59P3/2, and E_B kernel per m'
pp = ProbePair("Cs133", 60, 59, 5.0); g0 = pp.pulse(None, 0, Level(59, 1, 1.5, 1.5), 1.0, np.pi)
EB = {}
for mp in (-1.5, -0.5, 0.5, 1.5):
    c = Level(59, 1, 1.5, mp); EB[mp] = 1 - (1 - pp.pulse(10.0, 0.0, c, 1.0, np.pi)) / (1 - g0)
wts = {}
for k, e in list(POL.items()) + [("iso", None)]:
    w = {mp: (sum(dipole_q("Cs133", Level(59, 1, 1.5, mp), S, q) ** 2 for q in (-1, 0, 1)) if e is None
              else abs(sum(c * dipole_q("Cs133", Level(59, 1, 1.5, mp), S, q) for q, c in e.items())) ** 2) for mp in EB}
    tot = sum(w.values()); wts[k] = {mp: x / tot for mp, x in w.items()}
harm = {k: sum(wts[k][mp] * EB[mp] for mp in EB) for k in wts}
out["kernel_m"] = dict(E_B_R10_th0_1MHz={str(k): v for k, v in EB.items()}, weights={k: {str(m): x for m, x in v.items()} for k, v in wts.items()},
                       harmful_factor_vs_iso={k: harm[k] / harm["iso"] for k in harm})
print("E_B per m' (59P3/2, R 10 um, th 0, 1 MHz):", EB); print("harm factor vs iso:", out["kernel_m"]["harmful_factor_vs_iso"])
json.dump(out, open("experiments/E13_cs_bath/results.json", "w"), indent=1)
