"""Independent Coulomb-approximation check of Rb Rydberg radial dipole matrix elements.

No ARC, no project src/. Everything is implemented here from scratch:
  * modified Rydberg-Ritz quantum defects (parameters from primary sources, see NOTES.md)
  * Numerov integration of the radial Schroedinger equation in a pure -1/r potential,
    inward from large r on a square-root grid x = sqrt(r), stopped at an inner cutoff r_c
  * radial matrix elements <n l j| r |n' l' j'>
  * hydrogen control against Gordon's closed formula (and an independent quadrature of the
    analytic hydrogen functions)

Units: atomic units of the reduced-mass atom (length a_mu = a0 (1 + m_e/M)); results are
converted to a0 by multiplying by (1 + m_e/M).

Sign convention: every radial function u(r) = r R(r) is chosen POSITIVE in its outermost lobe
(large r, before the exponential tail).  For hydrogen the textbook convention (u > 0 near r=0)
differs by (-1)^(n-l-1); the control converts between the two explicitly.

Run:  python3 coulomb_me.py      -> writes results.json next to this file
"""
import json, math, pathlib
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent

# ---------------------------------------------------------------- parameters (see NOTES.md)
# 87Rb nS1/2: Mack et al., PRA 83, 052515 (2011) = arXiv:1103.6221, Table I, "87Rb (this work)"
# nP1/2, nP3/2: Li et al., PRA 67, 052502 (2003), Table VI "Improved values" (measured on 85Rb;
#               no 87Rb nP values in either source) -- TABLE READ from rendered page 6.
QD = {
    ("S", 0.5): dict(d0=3.1311807, d2=0.1787, src="Mack2011 Tab.I 87Rb"),
    ("P", 0.5): dict(d0=2.6548849, d2=0.2900, src="Li2003 Tab.VI (85Rb)"),
    ("P", 1.5): dict(d0=2.6416737, d2=0.2950, src="Li2003 Tab.VI (85Rb)"),
}
QD_S_LI85 = dict(d0=3.1311804, d2=0.1784, src="Li2003 Tab.VI (85Rb)")   # cross-check only
L_OF = {"S": 0, "P": 1, "D": 2}

# Rydberg constant: Mack Eq. (1): R* = R_inf / (1 + m_e/m_87Rb), R_inf = h * 3289.82119466 THz
R_INF_THZ = 3289.82119466
ME_U = 5.48579909065e-4          # electron mass in u (CODATA 2018)          -- not from the papers
M87_U = 86.909180531             # 87Rb atomic mass in u (AME)                 -- not from the papers
MASS_RATIO = ME_U / M87_U
R_RB87_GHZ = R_INF_THZ * 1e3 / (1.0 + MASS_RATIO)
# Li Eq. (5): R_Rb = 109 736.605 cm^-1, c = 2.99792458e10 cm/s (cross-check)
R_RB_LI_GHZ = 109736.605 * 2.99792458e10 / 1e9


def delta(n, d0, d2):
    """Modified Rydberg-Ritz: delta(n) = d0 + d2/(n-d0)^2 (Li Eq. 6, Mack Eq. 2)."""
    return d0 + d2 / (n - d0) ** 2


def nstar(n, series, j, qd=None):
    p = qd if qd is not None else QD[(series, j)]
    return n - delta(n, p["d0"], p["d2"])


# ---------------------------------------------------------------- Numerov solver
def radial_wavefunction(ns, l, r_c=1.0, h=0.005, r_out_factor=None):
    """Coulomb-approximation radial function for effective quantum number ns and orbital l.

    Grid x = sqrt(r), uniform step h in x.  With u(r) = r R(r) = x^(1/2) chi(x):
        chi'' = [ (4 l(l+1) + 3/4)/x^2 - 8 + 4 x^2/ns^2 ] chi       (E = -1/(2 ns^2))
    Integrated inward from r_out = 2 ns (ns + 15) (far beyond the outer turning point
    ~2 ns^2) down to a fixed inner cutoff r_c (default 1 a0, i.e. near the Rb+ core);
    insensitivity to r_c in [0.5, 8] a0 is shown by the convergence scan in main().
    Returns (x, chi) with chi normalised so that  int u^2 dr = int 2 x^2 chi^2 dx = 1,
    sign fixed so that u > 0 in the outermost lobe.
    """
    r_out = 2.0 * ns * (ns + 15.0) if r_out_factor is None else r_out_factor * ns * ns
    x_out, x_in = math.sqrt(r_out), math.sqrt(r_c)
    N = int(math.ceil((x_out - x_in) / h)) + 1
    x = x_out - h * np.arange(N)            # descending
    x = x[x >= x_in - 1e-12]
    k = (4.0 * l * (l + 1) + 0.75) / x**2 - 8.0 + 4.0 * x**2 / ns**2   # chi'' = k chi
    chi = np.zeros_like(x)
    chi[0] = 1e-30
    chi[1] = 1e-30 * (1.0 + h * math.sqrt(max(k[0], 0.0)))           # decaying-tail start
    f = 1.0 - h * h * k / 12.0
    for i in range(1, len(x) - 1):
        chi[i + 1] = ((12.0 - 10.0 * f[i]) * chi[i] - f[i - 1] * chi[i - 1]) / f[i + 1]
        if abs(chi[i + 1]) > 1e250:   # rescale to avoid overflow in the tail start
            chi[: i + 2] *= 1e-200
    # sign: positive in outermost lobe -> look at the first lobe from the outside
    a = np.abs(chi)
    imax = 1
    while imax < len(a) - 1 and a[imax + 1] >= a[imax]:   # walk inward to the outermost extremum
        imax += 1
    if chi[imax] < 0:
        chi = -chi
    norm = np.sqrt(simpson_desc(2.0 * x**2 * chi**2, h))
    return x, chi / norm


def simpson_desc(y, h):
    """Simpson integral of samples on a uniform descending grid (returns positive measure)."""
    n = len(y)
    if n % 2 == 0:   # drop the innermost point (negligible; weight ~ r_c) to keep odd count
        y = y[:-1]
        n -= 1
    return h / 3.0 * (y[0] + y[-1] + 4.0 * y[1:-1:2].sum() + 2.0 * y[2:-1:2].sum())


def radial_me(ns1, l1, ns2, l2, r_c=1.0, h=0.005):
    """<1| r |2> = int u1 u2 r dr = int 2 x^4 chi1 chi2 dx, in reduced-mass atomic units."""
    r_out = 2.0 * max(ns1, ns2) * (max(ns1, ns2) + 15.0)
    x1, c1 = radial_wavefunction(ns1, l1, r_c, h, r_out / ns1**2)
    x2, c2 = radial_wavefunction(ns2, l2, r_c, h, r_out / ns2**2)
    m = min(len(x1), len(x2))
    assert np.allclose(x1[:m], x2[:m])
    return simpson_desc(2.0 * x1[:m] ** 4 * c1[:m] * c2[:m], h)


# ---------------------------------------------------------------- hydrogen controls
def gordon(n, l, n2, l2):
    """Gordon (1929) closed form for hydrogen <n l | r | n2 l2>, l2 = l -+ 1, n != n2,
    in the textbook sign convention (u > 0 near the origin). Written here as in
    Bethe & Salpeter Eq. (63.2), for the pair (n, l) and (n', l-1)."""
    if l2 == l + 1:                      # symmetric: swap to put larger l first
        return gordon(n2, l2, n, l)
    assert l2 == l - 1 and n != n2
    mp.mp.dps = 60
    np_ = n2
    nr, npr = n - l - 1, np_ - l
    pref = (mp.mpf(-1) ** (np_ - l)) / (4 * mp.factorial(2 * l - 1)) * mp.sqrt(
        mp.factorial(n + l) * mp.factorial(np_ + l - 1) / (mp.factorial(n - l - 1) * mp.factorial(np_ - l)))
    pref *= (4 * mp.mpf(n) * np_) ** (l + 1) * mp.mpf(n - np_) ** (n + np_ - 2 * l - 2) / mp.mpf(n + np_) ** (n + np_)
    z = -4 * mp.mpf(n) * np_ / mp.mpf(n - np_) ** 2
    F1 = mp.hyp2f1(-nr, -npr, 2 * l, z)
    F2 = mp.hyp2f1(-nr - 2, -npr, 2 * l, z)
    return float(pref * (F1 - (mp.mpf(n - np_) / (n + np_)) ** 2 * F2))


def hydrogen_same_n(n, l, l2):
    """<n l| r |n l-1> = -(3/2) n sqrt(n^2 - l^2) in the textbook convention (sign checked
    against quadrature below); symmetric in l <-> l2."""
    lm = max(l, l2)
    return -1.5 * n * math.sqrt(n * n - lm * lm)


def hydrogen_quadrature(n, l, n2, l2):
    """Independent check: direct high-precision quadrature of the analytic hydrogen u_{nl}
    (generalised Laguerre form), textbook sign convention."""
    mp.mp.dps = 40
    def u(nn, ll, r):
        rho = 2 * r / nn
        N = mp.sqrt((mp.mpf(2) / nn) ** 3 * mp.factorial(nn - ll - 1) / (2 * nn * mp.factorial(nn + ll)))
        return r * N * mp.e ** (-rho / 2) * rho**ll * mp.laguerre(nn - ll - 1, 2 * ll + 1, rho)
    rmax = 3 * max(n, n2) ** 2 + 60
    pts = list(np.linspace(0, rmax, 40))
    return float(mp.quad(lambda r: u(n, l, r) * u(n2, l2, r) * r, pts))


def hydrogen_control(r_c=1e-4, h=0.002):
    pairs = [(2, 0, 2, 1), (10, 0, 10, 1), (30, 0, 31, 1), (3, 1, 5, 2), (20, 1, 21, 0)]
    out = []
    for n, l, n2, l2 in pairs:
        exact = hydrogen_same_n(n, l, l2) if n == n2 else gordon(n, l, n2, l2)
        quad = hydrogen_quadrature(n, l, n2, l2)
        # convert textbook -> outer-lobe-positive convention
        sgn = (-1) ** (n - l - 1) * (-1) ** (n2 - l2 - 1)
        num = radial_me(float(n), l, float(n2), l2, r_c=r_c, h=h)
        out.append(dict(pair=f"{n}{'spdf'[l]}-{n2}{'spdf'[l2]}", exact_textbook=exact,
                        quadrature_textbook=quad, exact_outer_positive=sgn * exact,
                        numerov=num, rel_err=abs(num - sgn * exact) / abs(exact),
                        gordon_vs_quad_rel=abs(exact - quad) / abs(exact)))
    return out


# ---------------------------------------------------------------- Rb
TARGETS = [((53, "S", 0.5), (52, "P", 0.5)), ((53, "S", 0.5), (52, "P", 1.5)),
           ((53, "S", 0.5), (53, "P", 0.5)), ((53, "S", 0.5), (53, "P", 1.5))]


def lab(s):
    n, L, j = s
    return f"{n}{L}{int(2*j)}/2"


def rb_results(r_c=1.0, h=0.005, qd_s=None):
    res = []
    for a, b in TARGETS:
        nsa = nstar(a[0], a[1], a[2], qd_s if (qd_s and a[1] == "S") else None)
        nsb = nstar(b[0], b[1], b[2])
        me_mu = radial_me(nsa, L_OF[a[1]], nsb, L_OF[b[1]], r_c=r_c, h=h)
        me_a0 = me_mu * (1.0 + MASS_RATIO)
        f = R_RB87_GHZ * (1.0 / nsa**2 - 1.0 / nsb**2)          # E_b - E_a, GHz
        res.append(dict(transition=f"{lab(a)} - {lab(b)}", nstar_a=nsa, nstar_b=nsb,
                        radial_me_a0=me_a0, freq_GHz=f,
                        freq_GHz_LiRRb=R_RB_LI_GHZ * (1.0 / nsa**2 - 1.0 / nsb**2)))
    return res


def main():
    hyd = hydrogen_control()
    base = rb_results()
    # convergence: inner cutoff and step size
    conv = {}
    for rc in (0.5, 1.0, 2.0, 3.0, 5.0, 8.0):
        conv[f"r_c={rc}"] = [r["radial_me_a0"] for r in rb_results(r_c=rc)]
    for hh in (0.01, 0.0025):
        conv[f"h={hh}"] = [r["radial_me_a0"] for r in rb_results(h=hh)]
    ref = [r["radial_me_a0"] for r in base]
    conv_rel = {k: max(abs(v[i] - ref[i]) / abs(ref[i]) for i in range(4)) for k, v in conv.items()}
    li_s = rb_results(qd_s=QD_S_LI85)
    out = dict(
        description="Coulomb-approximation (Numerov, sqrt grid) radial matrix elements, Rb; no ARC",
        sign_convention="u(r)=rR(r) positive in outermost lobe for every state",
        units="radial ME in a0 (reduced-mass length converted with factor 1+me/M); freq = E(P)-E(S) in GHz",
        quantum_defects={f"n{k[0]}{int(2*k[1])}/2": v for k, v in QD.items()},
        quantum_defects_S_crosscheck_Li85=QD_S_LI85,
        R_Rb87_GHz=R_RB87_GHZ, R_Rb_Li2003_GHz=R_RB_LI_GHZ, me_over_M87=MASS_RATIO,
        numerics=dict(grid="x=sqrt(r), uniform h=0.005", r_out="2 n*(n*+15)", r_c_a0=1.0),
        results=base,
        convergence_max_rel_dev_vs_baseline=conv_rel,
        convergence_values=conv,
        crosscheck_with_Li2003_85Rb_nS_defects=[dict(transition=r["transition"], radial_me_a0=r["radial_me_a0"],
                                                     freq_GHz=r["freq_GHz"]) for r in li_s],
        hydrogen_control=hyd,
    )
    (HERE / "results.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(dict(results=base, conv=conv_rel, hyd=[(h["pair"], h["exact_outer_positive"], h["numerov"], h["rel_err"], h["gordon_vs_quad_rel"]) for h in hyd],
                          li_s=li_s), indent=1))


if __name__ == "__main__":
    main()
