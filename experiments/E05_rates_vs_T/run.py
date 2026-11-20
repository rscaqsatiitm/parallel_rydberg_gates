"""E05: BBR contaminant rates and P-state lifetimes vs temperature (ARC 3.10.2). No fitted parameter."""
import sys, json, warnings
warnings.filterwarnings("ignore"); sys.path.insert(0, "src")
from prg.atomic import get_atom, bbr_rates
a = get_atom("Rb87"); out = {}
for T in (300.0, 188.0, 45.0, 4.0):
    r = bbr_rates("Rb87", 53, T)
    tS = a.getStateLifetime(53, 0, 0.5, temperature=T, includeLevelsUpTo=93)
    tP = {f"{n}P{j}": a.getStateLifetime(n, 1, j, temperature=T, includeLevelsUpTo=n + 40) for n in (52, 53) for j in (0.5, 1.5)}
    out[T] = {"rate_to_52P_53P": sum(r.values()), "by_level": {f"{k[0]}P{k[1]}": v for k, v in r.items()},
              "tau_53S_us": tS * 1e6, "tau_P_us": {k: v * 1e6 for k, v in tP.items()}}
    print(T, round(sum(r.values()), 1), round(tS * 1e6, 1), {k: round(v * 1e6, 1) for k, v in tP.items()})
tP0 = {f"{n}P{j}": a.getStateLifetime(n, 1, j) * 1e6 for n in (52, 53) for j in (0.5, 1.5)}
print("T=0 radiative", {k: round(v, 1) for k, v in tP0.items()}); out["radiative_only_tau_P_us"] = tP0
json.dump(out, open("experiments/E05_rates_vs_T/results.json", "w"), indent=1)
