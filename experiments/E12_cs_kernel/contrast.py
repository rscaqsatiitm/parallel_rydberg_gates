# E12 contrast table: C_min = 2.12 / (E sqrt(N)) (pre-registered definition). Settings: Ramsey t = 1 us, blockade
# Omega/2pi = 1 MHz (fixed choices), and best over the pre-registered grids (choice made after seeing results; flagged).
import json, numpy as np
out = json.load(open("experiments/E12_cs_kernel/results.json"))
def cmin(E, N): return 2.12 / (E * np.sqrt(N)) if E > 0 else np.inf
f = lambda x: f"{x:.2f}" if x <= 1 else ">1"
print("state       R  th | E_R(1us) Cmin1e3 Cmin1e4 | E_B(1MHz) Cmin1e3 Cmin1e4 | best E_R (t) | best E_B (Om)")
for o in out:
    if o["B"] != 5.0 or o["R"] not in (5, 10, 20) or o["theta"] not in (0, 90): continue
    er, eb = o["ramsey"]["1"][0], o["block"]["1"]
    br = max((v[0], t) for t, v in o["ramsey"].items()); bb = max((v, om) for om, v in o["block"].items())
    print(f"{o['state']:10} {o['R']:3} {o['theta']:3} | {er:.3f} {f(cmin(er,1e3)):>6} {f(cmin(er,1e4)):>6} | {eb:.3f} {f(cmin(eb,1e3)):>6} {f(cmin(eb,1e4)):>6}"
          f" | {br[0]:.3f} ({br[1]} us) | {bb[0]:.3f} ({bb[1]} MHz)")
