"""E19: Cs quantum defects (independent of ARC), energies and Coulomb-approximation radial matrix elements.

numpy/scipy/mpmath only. ARC is NOT imported anywhere in this experiment.
Every parameter below carries a pointer to a verbatim quote in literature/notes/cs_quantum_defects.md.
"""
import numpy as np
import scipy.constants as sc

# ---------------------------------------------------------------- parameters (see notes file for quotes)
# Primary set: Allinson et al., PRA 111, 062802 (2025), arXiv:2502.20961, Table I, "This work" rows.
# Modified Rydberg-Ritz: delta(n) = d0 + d2/(n-d0)^2 + d4/(n-d0)^4   (their Eq. 2).
ALLINSON = {               # (d0, d2, d4)                        quote: Q-A1..A4
    "S1/2": (4.049368, 0.2333, 0.8),
    "P1/2": (3.591606, 0.3569, 0.81),
    "P3/2": (3.559091, 0.3657, 1.17),
}
ALLINSON_SIG = {           # 1-sigma from Table I parentheses (diagonal of the published covariance)
    "S1/2": (3e-6, 0.0014, 0.2),
    "P1/2": (3e-6, 0.0013, 0.14),
    "P3/2": (3e-6, 0.0013, 0.14),
}
# Secondary nS set: Shen et al., PRL 133, 233005 (2024), arXiv:2410.19129, Table I "nS1/2 [this work]".
SHEN_S = (4.04935994, 0.238017, 0.1747)          # quote: Q-S2
# ARC's source (for comparison only; values quoted from the Deiglmayr 2016 PDF, NOT read from ARC):
DEIGLMAYR = {                                     # quote: Q-D1..D2 (and Allinson Table I "Collated Works")
    "S1/2": (4.0493532, 0.2391, 0.06, 11.0, -209.0),
    "P1/2": (3.5915871, 0.36273),
    "P3/2": (3.5590676, 0.37469),
}
# Ionisation energy (only needed for absolute term values; cancels in all Rydberg-Rydberg intervals)
E_ION_CM = 31406.46775148           # Shen 2024 weighted mean, cm^-1, quote Q-S3
E_ION_DEIGLMAYR_CM = 31406.4677325  # as quoted by Shen 2024 for Ref. [49] (= Deiglmayr 2016), quote Q-S3
R_CS_CM = 109736.8627304            # reduced-mass Rydberg constant for 133Cs, Shen 2024, quote Q-S1

C_CM = sc.c * 100.0                  # cm/s
R_INF_M = sc.physical_constants["Rydberg constant"][0]           # CODATA (scipy 1.18 -> CODATA 2022)
A0 = sc.physical_constants["Bohr radius"][0]
EH_HZ = sc.physical_constants["hartree-hertz relationship"][0]
# K = e^2 a0^2 / (4 pi eps0 h) = E_h a0^3 / h ; expressed in MHz um^3
K_MHZ_UM3 = sc.e**2 * A0**2 / (4 * np.pi * sc.epsilon_0 * sc.h) / 1e6 * 1e18


def delta(n, coeffs):
    """Modified Rydberg-Ritz quantum defect delta(n) = d0 + sum_k d_2k/(n-d0)^2k."""
    d0 = coeffs[0]
    return d0 + sum(c / (n - d0) ** (2 * (k + 1)) for k, c in enumerate(coeffs[1:]))


def nstar(n, coeffs):
    return n - delta(n, coeffs)


def term_cm(n, coeffs, e_ion=E_ION_CM, ryd=R_CS_CM):
    """Term value relative to the 6s1/2 centre of gravity, cm^-1."""
    return e_ion - ryd / nstar(n, coeffs) ** 2


def freq_ghz(n_i, c_i, n_f, c_f, ryd=R_CS_CM):
    """nu = E_f - E_i in GHz (signed; negative if final state is lower)."""
    return C_CM * ryd * (1.0 / nstar(n_i, c_i) ** 2 - 1.0 / nstar(n_f, c_f) ** 2) / 1e9


# ---------------------------------------------------------------- Numerov, Coulomb approximation
def numerov_inward(ns, l, h, x_in, rmax=None):
    """Radial function on a sqrt grid x = sqrt(r) (atomic units), pure -1/r potential, energy -1/(2 ns^2).

    Substitution R(r) = x^(-3/2) X(x) gives X'' = g X with
    g = 8 x^2 (V - E) + (2l+1/2)(2l+3/2)/x^2  (derived symbolically; see README).
    Integrated inward from rmax = 2 ns (ns + 15) to the inner cutoff r_in = x_in^2.
    Returns grid x (starting exactly at x_in, step h) and X normalised so that 2 int X^2 x^2 dx = 1.
    """
    if rmax is None:
        rmax = 2.0 * ns * (ns + 15.0)
    npts = int(np.ceil((np.sqrt(rmax) - x_in) / h)) + 1
    x = x_in + h * np.arange(npts)
    E = -0.5 / ns**2
    g = 8.0 * x**2 * (-1.0 / x**2 - E) + (2 * l + 0.5) * (2 * l + 1.5) / x**2
    f = 1.0 - h * h * g / 12.0
    X = np.zeros(npts)
    X[-1] = 0.0
    X[-2] = 1e-10
    for i in range(npts - 2, 0, -1):
        X[i - 1] = (2.0 * (1.0 + 5.0 * h * h * g[i] / 12.0) * X[i] - f[i + 1] * X[i + 1]) / f[i - 1]
        if abs(X[i - 1]) > 1e100:            # rescale to avoid overflow
            X[i - 1 :] /= 1e100
    # sign convention: positive at the outermost lobe (largest r), as in common Rydberg codes
    norm = 2.0 * np.trapezoid(X**2 * x**2, x)
    X /= np.sqrt(norm)
    return x, X


def radial_me(ns1, l1, ns2, l2, h=0.005, r_in=3.0):
    """<n1 l1 | r | n2 l2> in a0, both functions on a common sqrt grid starting at sqrt(r_in)."""
    x_in = np.sqrt(r_in)
    x1, X1 = numerov_inward(ns1, l1, h, x_in)
    x2, X2 = numerov_inward(ns2, l2, h, x_in)
    m = min(len(x1), len(x2))
    # R1 R2 r^3 dr = 2 X1 X2 x^4 dx
    return 2.0 * np.trapezoid(X1[:m] * X2[:m] * x1[:m] ** 4, x1[:m])


def c3_mhz_um3(R_a0):
    """C3 for nS1/2 mj=+1/2 <-> n'P3/2 mj=+3/2 (stretched): K * (R/sqrt3)^2."""
    return K_MHZ_UM3 * R_a0**2 / 3.0
