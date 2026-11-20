# Verbatim copy of the handover Section 3 script (2026-11-20). Not a result; see README.
import numpy as np, warnings
warnings.filterwarnings("ignore")
from arc import Rubidium87, Caesium
K = 9.75e-7   # GHz um^3 per (e a0)^2
def study(atom, n, omegas_MHz, name, T=300.0):
    tau0 = atom.getStateLifetime(n, 0, 0.5)
    tauT = atom.getStateLifetime(n, 0, 0.5, temperature=T, includeLevelsUpTo=n + 40)
    g_bbr = 1 / tauT - 1 / tau0
    trig, c3 = 0.0, {}
    for n2 in (n - 1, n):
        for j2 in (0.5, 1.5):
            rT = atom.getTransitionRate(n, 0, 0.5, n2, 1, j2, temperature=T)
            lower = atom.getEnergy(n2, 1, j2) < atom.getEnergy(n, 0, 0.5)
            r0 = atom.getTransitionRate(n, 0, 0.5, n2, 1, j2, temperature=0) if lower else 0.0
            trig += rT - r0
            d = atom.getRadialMatrixElement(n, 0, 0.5, n2, 1, j2)
            c3[(n2, j2)] = K * d * d / 3
    print(name, n, tau0, tauT, g_bbr, trig, trig / g_bbr, c3)
    c3max = max(c3.values())
    for om in omegas_MHz:
        Om = 2 * np.pi * om * 1e6
        Tg, tR = 7.612 / Om, 2.947 / Om
        p_c = trig * tR
        Rc = (2 * np.pi * c3max * 1e9 * (Tg / 2)) ** (1 / 3)
        for px, py in ((8.6, 12.1), (5.0, 5.0), (20.0, 20.0)):
            xs = np.arange(-12, 13)
            X, Y = np.meshgrid(xs * px, xs * py); R = np.hypot(X, Y); R = R[R > 0]
            phase = 2 * np.pi * c3max * 1e9 / R**3 * (Tg / 2)
            n_eff = (np.sin(np.minimum(phase, np.pi / 2)) ** 2).sum()
            print(f"  Omega {om} MHz: gate {Tg*1e9:.0f} ns, p_c {p_c:.2e}, R_c {Rc:.1f} um, "
                  f"pitch {px}x{py}: neighbours {n_eff:.2f}, correlated error {p_c*n_eff:.2e}")
if __name__ == "__main__":
    study(Rubidium87(), 53, (4.6, 17.0), "Rb87")
    study(Caesium(), 60, (2.0, 5.0), "Cs133")
