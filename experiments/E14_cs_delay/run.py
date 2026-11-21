# E14 (pre-registered README): delay law vs T_eff and shots.
import sys, json, numpy as np
sys.path.insert(0, "src")
from prg.probe import ProbePair
from prg.atomic import Level, contaminant_weights
E13 = json.load(open("experiments/E13_cs_bath/results.json"))
TEFF = [300, 1e3, 3e3, 1e4, 3e4, 1e5, 3e5, 1e6]; NA = [2, 3, 5, 10]; AS = [5.0, 10.0]; CS = [0.90, 0.95]
RS = sorted({a * k for a in AS for k in range(1, 10)})
# m'-averaged blockade kernel at theta = 90 deg, Omega/2pi = 1 MHz, isotropic 300 K weights over 59P and 60P
w = {}
for npr in (59, 60):
    ww, rates = contaminant_weights("Cs133", 60, 0.5, npr)
    for lv, x in ww.items(): w[lv] = x * sum(rates.values())
tot = sum(w.values()); w = {k: v / tot for k, v in w.items()}
EB = {}
for npr in (59, 60):
    pp = ProbePair("Cs133", 60, npr, 5.0)
    for lv in [l for l in w if l.n == npr]:
        g0 = pp.pulse(None, 0, lv, 1.0, np.pi)
        for R in RS:
            EB[R] = EB.get(R, 0) + w[lv] * (1 - (1 - pp.pulse(R, np.pi / 2, lv, 1.0, np.pi)) / (1 - g0))
print("m'-averaged E_B(R), theta 90, 1 MHz:", {R: round(v, 4) for R, v in EB.items()})
def eps0(pc, n, a):
    """eps(0) per probe (non-contaminant atom), averaged over probe positions, first order in p_c."""
    return np.mean([sum(pc * EB[abs(i - j) * a] for j in range(n) if j != i) for i in range(n)])
out = dict(EB={str(k): v for k, v in EB.items()}, rows=[])
print("scen T_eff     p_c     tau(us)  | shots (total, two points) for a = 5 um, C = 0.90 / 0.95: N_a = 2, 3, 5, 10 [independent probes; correlated x N_p]")
for scen in ("A", "B"):
    for T in TEFF:
        r = E13[f"narrow {T:g}"]; pc = r["p_c"]
        tau = r["tau_res_off_us"] if scen == "A" else r["tau_res_on_us"]
        S = r["S_off"] if scen == "A" else r["S_on"]
        line = f"  {scen}  {T:8.0f} {pc:.2e} {tau if tau else float('nan'):8.1f} |"
        for a in AS:
            for C in CS:
                for n in NA:
                    e0 = eps0(pc, n, a); e1 = e0 * np.exp(-1)              # delay law prediction at t = tau
                    q = C; Np = max(n * (1 - pc), 1)
                    Ns = sum(2 * q * (1 - q) / (Np * C ** 2 * (0.071 * e) ** 2) for e in (e0, e1))
                    out["rows"].append(dict(scenario=scen, T_eff=T, p_c=pc, tau_us=tau, a=a, C=C, N_a=n, eps0=e0,
                                            shots_indep=Ns, shots_corr=Ns * Np, Na_pc=n * pc))
                    if a == 5.0: line += f" {Ns:.1e}"
                line += " |" if a == 5.0 else ""
        print(line)
json.dump(out, open("experiments/E14_cs_delay/results.json", "w"), indent=1)
