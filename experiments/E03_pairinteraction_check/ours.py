import sys, json, numpy as np
sys.path.insert(0, "src")
from prg.atomic import manifold, dipole_cartesian, level_energy_MHz, Level, K_DD
S = manifold(53, 0); P = manifold(52, 1); ryd = S + P
dx, dy, dz = dipole_cartesian("Rb87", ryd); d = [dx, dy, dz]
E = np.array([level_energy_MHz("Rb87", lv, 8.5) for lv in ryd])
iS = range(2); iP = range(2, 8)
basis = [(a, b) for a in iS for b in iP] + [(b, a) for a in iS for b in iP]
E0 = level_energy_MHz("Rb87", Level(53, 0, 0.5, 0.5), 8.5) + level_energy_MHz("Rb87", Level(52, 1, 1.5, 0.5), 8.5)
out = {}
for th in (0, 90):
    n = np.array([np.sin(np.radians(th)), 0, np.cos(np.radians(th))])
    for R in (6, 10, 20):
        H = np.zeros((len(basis), len(basis)), complex)
        for i, (a1, b1) in enumerate(basis):
            H[i, i] = E[a1] + E[b1] - E0
            for k, (a2, b2) in enumerate(basis):
                v = sum(d[x][a1, a2] * d[x][b1, b2] for x in range(3)) \
                    - 3 * sum(n[x] * d[x][a1, a2] for x in range(3)) * sum(n[y] * d[y][b1, b2] for y in range(3))
                H[i, k] += K_DD * v / R ** 3
        out[f"{th}_{R}"] = np.sort(np.linalg.eigvalsh(H)).tolist()
json.dump(out, open("experiments/E03_pairinteraction_check/ours.json", "w"))
print({k: np.round(v[20:28], 3).tolist() for k, v in out.items() if k == "0_10"})
