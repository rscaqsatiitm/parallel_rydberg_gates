# E15 quench candidates (pre-registered README).
import sys, json, numpy as np
sys.path.insert(0, "src")
from prg.atomic import get_atom, dipole_q, Level
a = get_atom("Cs133")
HBAR, C, EPS0, E, A0 = 1.054571817e-34, 299792458.0, 8.8541878128e-12, 1.602176634e-19, 5.29177210903e-11
K = [(6, 0, 0.5), (7, 0, 0.5), (8, 0, 0.5), (9, 0, 0.5), (5, 2, 1.5), (5, 2, 2.5), (6, 2, 1.5), (6, 2, 2.5), (7, 2, 1.5), (7, 2, 2.5)]
REQ = 3.0e6                                   # removal rate, 1/s (95 % in 1 us)
out = []
for npr in (59, 60):
    for jp in (0.5, 1.5):
        for (nk, lk, jk) in K:
            if abs(jk - jp) > 1: continue
            nu = a.getTransitionFrequency(nk, lk, jk, npr, 1, jp)        # Hz, positive if P above k
            lam = C / abs(nu) * 1e9
            R = a.getRadialMatrixElement(npr, 1, jp, nk, lk, jk)
            # strongest Zeeman component
            best = max(abs(dipole_q("Cs133", Level(npr, 1, jp, mp), Level(nk, lk, jk, mk), q))
                       for mp in np.arange(-jp, jp + 1) for mk in np.arange(-jk, jk + 1) for q in (-1, 0, 1))
            if nk == 6 and lk == 0:
                Gk = 0.0
            else:
                Gk = 1 / a.getStateLifetime(nk, lk, jk, temperature=300.0, includeLevelsUpTo=nk + 40)
            if Gk == 0.0:
                Om = np.pi / 1e-6; note = "coherent pi pulse in 1 us (no decay of k); m-selective"
            elif Gk / 2 < REQ:
                Om = np.nan; note = "Gamma_k/2 < 3/us: cannot meet 1 us alone"
            else:
                # slow eigenvalue Gk/2 - sqrt(Gk^2/4 - Om^2) = REQ  ->  Om^2 = Gk^2/4 - (Gk/2 - REQ)^2
                Om = np.sqrt(Gk ** 2 / 4 - (Gk / 2 - REQ) ** 2); note = ""
            d = best * E * A0
            I = C * EPS0 * (HBAR * Om / d) ** 2 / 2 if np.isfinite(Om) else np.nan
            P = {w: I * np.pi * (w * 1e-6) ** 2 / 2 for w in (20, 100)}
            out.append(dict(P=f"{npr}P{jp}", k=f"{nk}{'SPDF'[lk]}{jk}", lam_nm=lam, R_a0=R, d_stretched_a0=best,
                            Gamma_k_per_us=Gk * 1e-6, Omega_over_2pi_MHz=Om / 2 / np.pi * 1e-6, I_W_m2=I,
                            P_W_w20=P[20], P_W_w100=P[100], note=note))
json.dump(out, open("experiments/E15_cs_quench/results.json", "w"), indent=1)
print(f"{'P':7} {'k':7} {'lam nm':>8} {'R a0':>8} {'d a0':>8} {'Gk /us':>7} {'Om/2pi MHz':>10} {'P(w20) W':>9} {'P(w100) W':>9} note")
for o in out:
    print(f"{o['P']:7} {o['k']:7} {o['lam_nm']:8.2f} {o['R_a0']:8.4f} {o['d_stretched_a0']:8.4f} {o['Gamma_k_per_us']:7.2f} {o['Omega_over_2pi_MHz']:10.3f} {o['P_W_w20']:9.2e} {o['P_W_w100']:9.2e} {o['note']}")
for k in ("7S0.5", "6D2.5"):
    l = {o["P"]: o["lam_nm"] for o in out if o["k"] == k}
    if "59P1.5" in l and "60P1.5" in l: print(f"line separation 59P3/2 vs 60P3/2 via {k}: {abs(l['59P1.5']-l['60P1.5'])*1e3:.1f} pm")
