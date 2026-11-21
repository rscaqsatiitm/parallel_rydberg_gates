# E11: Cs nS rates by final state, lifetimes, frequencies, exchange strength (pre-registered README).
import sys, json, numpy as np
sys.path.insert(0, "src")
from prg.atomic import get_atom, dipole_q, Level, K_DD
IRT, OT = 0.1925, 1.215            # I_r/T and Omega T/2pi (E02, D011)
def rates(sp, n, T=300.0, W=20):
    a = get_atom(sp); out = {}
    for n2 in range(max(n - W, 6), n + W + 1):
        for j in (0.5, 1.5):
            rT = a.getTransitionRate(n, 0, 0.5, n2, 1, j, temperature=T)
            down = a.getEnergy(n2, 1, j) < a.getEnergy(n, 0, 0.5)
            r0 = a.getTransitionRate(n, 0, 0.5, n2, 1, j, temperature=0) if down else 0.0
            out[(n2, j)] = rT - r0
    tot = 1 / a.getStateLifetime(n, 0, 0.5, temperature=T, includeLevelsUpTo=n + 40) - 1 / a.getStateLifetime(n, 0, 0.5, temperature=0, includeLevelsUpTo=n + 40)
    return out, tot
def row(sp, n):
    a = get_atom(sp); r, tot = rates(sp, n)
    res = {(n - 1, 0.5), (n - 1, 1.5), (n, 0.5), (n, 1.5)}
    rr = sum(r[k] for k in res); s = sum(r.values())
    f = {k: a.getTransitionFrequency(n, 0, 0.5, k[0], 1, k[1]) / 1e9 for k in r}
    # 90 % band: smallest |f| window around the lines ordered by rate
    order = sorted(r, key=lambda k: -r[k]); acc = 0; band = []
    for k in order:
        band.append(abs(f[k])); acc += r[k]
        if acc >= 0.9 * s: break
    tau = {f"{n2}P{j}": {T: a.getStateLifetime(n2, 1, j, temperature=T, includeLevelsUpTo=n2 + 40) * 1e6 for T in (300.0, 0.0)}
           for n2 in (n - 1, n) for j in (0.5, 1.5)}
    C3 = {f"{n2}P3/2": K_DD * dipole_q(sp, Level(n2, 1, 1.5, 1.5), Level(n, 0, 0.5, 0.5), 1) ** 2 for n2 in (n - 1, n)}
    pc = {f"{k[0]}P{k[1]}": {om: r[k] * IRT * OT / om * 1e-6 for om in (1.0, 5.0)} for k in res}
    return dict(n=n, rate={f"{k[0]}P{k[1]}": r[k] for k in r}, total_lifetime_diff=tot, sum_rates=s, resonant=rr,
                res_fraction=rr / tot, sum_check=s / tot, freq_GHz={f"{k[0]}P{k[1]}": f[k] for k in r},
                band90_GHz=[min(band), max(band)], tau_us=tau, C3_MHz_um3=C3,
                Rex_um={k: {om: (v / om) ** (1 / 3) for om in (1.0, 5.0)} for k, v in C3.items()}, p_c_per_gate=pc,
                p_c_per_us_ryd=rr * 1e-6)
if __name__ == "__main__":
    rb = rates("Rb87", 53)[0]; print("control Rb53:", round(rb[(52, 0.5)] + rb[(52, 1.5)]), round(rb[(53, 0.5)] + rb[(53, 1.5)]))
    out = [row("Cs133", n) for n in range(50, 81)]
    json.dump(out, open("experiments/E11_cs_rates/results.json", "w"), indent=1)
    print(" n  Gres(/s) frac  sumchk  f(n-1)P3/2 f(nP3/2) GHz  tau(n-1)P3/2 nP3/2 @300K us   C3(n-1)P3/2  Rex1MHz  pc(1MHz)")
    for o in out:
        n = o["n"]; fq = o["freq_GHz"]; t = o["tau_us"]
        print(f"{n:3d} {o['resonant']:7.0f} {o['res_fraction']:.3f} {o['sum_check']:.3f}  {fq[f'{n-1}P1.5']:7.2f} {fq[f'{n}P1.5']:7.2f}"
              f"   {t[f'{n-1}P1.5'][300.0]:6.1f} {t[f'{n}P1.5'][300.0]:6.1f}   {o['C3_MHz_um3'][f'{n-1}P3/2']:8.0f} {o['Rex_um'][f'{n-1}P3/2'][1.0]:6.1f}"
              f"  {o['p_c_per_us_ryd']*0.1925*1.215:.2e}  band90 {o['band90_GHz'][0]:.1f}-{o['band90_GHz'][1]:.1f}")
