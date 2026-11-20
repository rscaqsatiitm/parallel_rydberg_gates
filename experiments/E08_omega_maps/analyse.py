# E08 analysis: p_c-weighted (n' = 52, 53) E_full (t_on = 0) and E_same (p_r-weighted over 6 t_on); verdicts as pre-registered.
import json, numpy as np
D = "experiments/E08_omega_maps/"
def load(om):
    if om == 4.6:
        d = json.load(open("experiments/E02_error_map/results.json"))
        pc = {int(k): v for k, v in d["p_c"].items()}
        full = {}
        for (np_, bd, R, al), v in d["full"]:
            if bd in "xz" and al in (0, 90): full.setdefault((bd, R, al), 0); full[(bd, R, al)] += pc[np_] / sum(pc.values()) * v[0]
        return dict(Omega=4.6, p_c=sum(pc.values()), T=d["T_us"], full=full, same=None)
    d = json.load(open(D + f"res_{om:g}.json")); pc = {int(k): v for k, v in d["p_c"].items()}; P = sum(pc.values())
    tons = d["t_on"]; wt = d["t_on_weight"]; full, same = {}, {}
    for (np_, bd, R, al, ton), v in d["res"]:
        k = (bd, R, al); f = pc[np_] / P
        if ton == 0.0: full[k] = full.get(k, 0) + f * v[0]
        else:
            i = min(range(6), key=lambda j: abs(tons[j] - ton)); same[k] = same.get(k, 0) + f * wt[i] * v[0]
    return dict(Omega=om, p_c=P, T=d["T_us"], full=full, same=same)
if __name__ == '__main__':
    out = {}
    for om in (2.3, 4.6, 9.2, 18.4):
        r = load(om); out[om] = r
        print(f"Omega/2pi = {om} MHz  T = {r['T']:.4f} us  p_c = {r['p_c']:.3e}")
        for bd in "xz":
            for al in (0, 90):
                Rs = [25, 30, 40]; E = [r["full"][(bd, R, al)] for R in Rs]
                s = np.polyfit(np.log(Rs), np.log(E), 1)[0]
                print(f"  B {bd} alpha {al:2d}: E_full 10/20/30 um = {r['full'][(bd,10,al)]:.3g} {r['full'][(bd,20,al)]:.3g} {r['full'][(bd,30,al)]:.3g}"
                      f"  tail slope {s:+.2f} {'PASS' if abs(s + 6) <= 0.3 else 'FAIL'}"
                      + (f"  E_same/E_full(30) {r['same'][(bd,30,al)]/r['full'][(bd,30,al)]:.2f}" if r['same'] else ""))
    print("\nOmega^-2 check at R = 30 um: E_full(2.3)/E_full(18.4) vs (18.4/2.3)^2 = 64")
    for bd in "xz":
        for al in (0, 90):
            q = out[2.3]["full"][(bd, 30, al)] / out[18.4]["full"][(bd, 30, al)]
            print(f"  B {bd} alpha {al:2d}: ratio {q:.1f}  (q/64 = {q/64:.3f})  {'PASS' if abs(q/64 - 1) <= 0.2 else 'FAIL'}")
    print("\nHalf-error radius (E_full = 0.5, log-interp), B z alpha 0, and p_c x E_full-weighted proxy")
    for om in (2.3, 4.6, 9.2, 18.4):
        r = out[om]; Rs = sorted({k[1] for k in r["full"] if k[0] == "z" and k[2] == 0}); E = [r["full"][("z", R, 0)] for R in Rs]
        R12 = next((np.exp(np.interp(np.log(0.5), [np.log(E[i+1]), np.log(E[i])], [np.log(Rs[i+1]), np.log(Rs[i])])) for i in range(len(Rs)-1) if E[i] >= 0.5 > E[i+1]), float("nan"))
        print(f"  {om:5} MHz  R_1/2 = {R12:.1f} um  p_c = {r['p_c']:.3e}  p_c*Omega = {r['p_c']*om:.3e}")
