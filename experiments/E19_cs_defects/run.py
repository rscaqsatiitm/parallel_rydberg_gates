"""E19 run: frequencies, radial matrix elements, C3 and controls. Writes results.json next to this file.

Usage (from repo root):  python3 experiments/E19_cs_defects/run.py
No ARC. numpy / scipy / mpmath only.
"""
import hashlib, json, pathlib, platform, subprocess, sys, time
import numpy as np
import mpmath as mp
import scipy.constants as sc

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import cs_qd as Q  # noqa: E402

t0, c0 = time.time(), time.process_time()
NS = [50, 52, 55, 60, 65, 70, 80]
H_DEFAULT, RIN_DEFAULT = 0.005, 3.0
A = Q.ALLINSON
out = {"params": {}, "controls": {}, "results": [], "source_comparison": []}

# ------------------------------------------------------------ parameters used
out["params"] = {
    "allinson_2025_d0_d2_d4": A, "allinson_2025_sigma": Q.ALLINSON_SIG,
    "shen_2024_S": Q.SHEN_S, "deiglmayr_2016": Q.DEIGLMAYR,
    "E_ion_cm-1": Q.E_ION_CM, "R_Cs_cm-1": Q.R_CS_CM, "c_m_s": sc.c,
    "R_inf_m-1_CODATA": Q.R_INF_M, "a0_m": Q.A0, "K_MHz_um3": Q.K_MHZ_UM3,
    "numerov_h_sqrt_a0": H_DEFAULT, "r_in_a0": RIN_DEFAULT,
}

# ------------------------------------------------------------ covariance (Allinson data set, doi:10.15128/r2df65v802x)
COV_PATH = ROOT / "literature/pdf/E19_cs_defects/durham_data/Paper_Data/d4_Covariance_Matrix.txt"
cov = None
if COV_PATH.exists():
    out["params"]["covariance_sha256"] = hashlib.sha256(COV_PATH.read_bytes()).hexdigest()
    C = np.loadtxt(COV_PATH)          # order: d0 (9 series), d2 (9), d4 (9); series s1/2,p1/2,p3/2,d3/2,...
    idx = {s: [k, 9 + k, 18 + k] for k, s in enumerate(["S1/2", "P1/2", "P3/2"])}
    sel = idx["S1/2"] + idx["P1/2"] + idx["P3/2"]
    cov = C[np.ix_(sel, sel)]
    out["controls"]["cov_diag_sqrt_vs_tableI"] = np.sqrt(np.diag(cov)).tolist()


def freq_with(par, n, nf, sf):
    return Q.freq_ghz(n, par["S1/2"], nf, par[sf])


def freq_sigma(n, nf, sf):
    """1-sigma (MHz) of nS->n'P from the Allinson covariance (correlations included) and diagonal-only."""
    keys = ["S1/2", "P1/2", "P3/2"]
    p0 = np.array([v for k in keys for v in A[k]])
    def f(p):
        par = {k: tuple(p[3 * i:3 * i + 3]) for i, k in enumerate(keys)}
        return freq_with(par, n, nf, sf)
    J = np.zeros(9)
    for i in range(9):
        dp = np.zeros(9); dp[i] = 1e-7 * max(1.0, abs(p0[i]))
        J[i] = (f(p0 + dp) - f(p0 - dp)) / (2 * dp[i])
    diag = np.array([s for k in keys for s in Q.ALLINSON_SIG[k]]) ** 2
    s_diag = np.sqrt(J @ (diag * J)) * 1e3
    s_cov = np.sqrt(J @ cov @ J) * 1e3 if cov is not None else None
    return s_cov, s_diag


# ------------------------------------------------------------ main results
for n in NS:
    row = {"n": n, "nstar_S": Q.nstar(n, A["S1/2"])}
    for nf, sf in [(n - 1, "P1/2"), (n - 1, "P3/2"), (n, "P1/2"), (n, "P3/2")]:
        key = f"{nf}{sf}"
        nu = freq_with(A, n, nf, sf)
        s_cov, s_diag = freq_sigma(n, nf, sf)
        row[f"nu_GHz_{key}"] = nu
        row[f"sig_MHz_cov_{key}"] = s_cov
        row[f"sig_MHz_diag_{key}"] = s_diag
        R = Q.radial_me(Q.nstar(n, A["S1/2"]), 0, Q.nstar(nf, A[sf]), 1, H_DEFAULT, RIN_DEFAULT)
        row[f"R_a0_{key}"] = R
        if sf == "P3/2":
            row[f"C3_MHz_um3_{key}"] = Q.c3_mhz_um3(R)
    out["results"].append(row)
    # comparison with other defect sets (frequencies only)
    comp = {"n": n}
    for nf, sf in [(n - 1, "P1/2"), (n - 1, "P3/2"), (n, "P1/2"), (n, "P3/2")]:
        key = f"{nf}{sf}"
        comp[f"dnu_MHz_Deiglmayr_minus_Allinson_{key}"] = (freq_with(Q.DEIGLMAYR, n, nf, sf) - freq_with(A, n, nf, sf)) * 1e3
        mix = dict(A); mix["S1/2"] = Q.SHEN_S
        comp[f"dnu_MHz_ShenS_minus_Allinson_{key}"] = (freq_with(mix, n, nf, sf) - freq_with(A, n, nf, sf)) * 1e3
        Rd = Q.radial_me(Q.nstar(n, Q.DEIGLMAYR["S1/2"]), 0, Q.nstar(nf, Q.DEIGLMAYR[sf]), 1, H_DEFAULT, RIN_DEFAULT)
        comp[f"R_a0_Deiglmayr_defects_{key}"] = Rd
    out["source_comparison"].append(comp)

# ------------------------------------------------------------ control 1: hydrogen against closed form
mp.mp.dps = 400   # high precision: alternating Laguerre sums cancel strongly at n = 80


def hyd_R_exact(n1, l1, n2, l2):
    """<n1 l1|r|n2 l2> for hydrogen (infinite nuclear mass), exact via polynomial x exponential integrals."""
    def coeffs(n, l):
        k = n - l - 1
        a = 2 * l + 1
        N = mp.sqrt((mp.mpf(2) / n) ** 3 * mp.factorial(k) / (2 * n * mp.factorial(n + l)))
        # R = N e^{-r/n} (2r/n)^l L_k^a(2r/n); L_k^a(y) = sum_j (-1)^j C(k+a, k-j) y^j / j!
        c = {}
        for j in range(k + 1):
            coef = (-1) ** j * mp.binomial(k + a, k - j) / mp.factorial(j)
            c[l + j] = N * coef * (mp.mpf(2) / n) ** (l + j)
        return c
    c1, c2 = coeffs(n1, l1), coeffs(n2, l2)
    alpha = mp.mpf(1) / n1 + mp.mpf(1) / n2
    s = mp.mpf(0)
    for p1, a1 in c1.items():
        for p2, a2 in c2.items():
            p = p1 + p2 + 3
            s += a1 * a2 * mp.factorial(p) / alpha ** (p + 1)
    # sign: Laguerre L_k^a has sign (-1)^k at large y; convert to "outermost lobe positive" convention
    s *= (-1) ** (n1 - l1 - 1) * (-1) ** (n2 - l2 - 1)
    return float(s)


hyd = []
for (n1, l1, n2, l2) in [(10, 0, 9, 1), (10, 0, 10, 1), (50, 0, 49, 1), (50, 0, 50, 1), (80, 0, 79, 1), (80, 0, 80, 1)]:
    ex = hyd_R_exact(n1, l1, n2, l2)
    num = Q.radial_me(n1, l1, n2, l2, H_DEFAULT, RIN_DEFAULT)
    num0 = Q.radial_me(n1, l1, n2, l2, H_DEFAULT, 0.0004)   # cutoff ~ 0 (x_in = 0.02)
    entry = {"pair": f"{n1},{l1} -> {n2},{l2}", "exact_a0": ex, "numerov_a0_rin3": num,
             "rel_err_rin3": num / ex - 1, "numerov_a0_rin0": num0, "rel_err_rin0": num0 / ex - 1}
    if n1 == n2:   # Bethe-Salpeter closed form <n l|r|n l-1> = (3/2) n sqrt(n^2 - l^2), l = 1
        entry["bethe_salpeter_a0"] = 1.5 * n1 * np.sqrt(n1**2 - 1)
    hyd.append(entry)
out["controls"]["hydrogen"] = hyd

# ------------------------------------------------------------ control 2: inner cutoff and grid
cut = []
for n in [50, 80]:
    for nf, sf in [(n - 1, "P3/2"), (n, "P3/2"), (n - 1, "P1/2")]:
        a, b = Q.nstar(n, A["S1/2"]), Q.nstar(nf, A[sf])
        vals = {r: Q.radial_me(a, 0, b, 1, H_DEFAULT, r) for r in [0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 10.0]}
        ref = vals[RIN_DEFAULT]
        cut.append({"pair": f"{n}S1/2-{nf}{sf}", "R_by_rin": vals,
                    "rel_spread_1to6": (max(vals[r] for r in [1.0, 2.0, 3.0, 4.0, 6.0]) - min(vals[r] for r in [1.0, 2.0, 3.0, 4.0, 6.0])) / abs(ref),
                    "R_h_half": Q.radial_me(a, 0, b, 1, H_DEFAULT / 2, RIN_DEFAULT),
                    "rel_change_h_half": Q.radial_me(a, 0, b, 1, H_DEFAULT / 2, RIN_DEFAULT) / ref - 1})
out["controls"]["cutoff_and_grid"] = cut

# ------------------------------------------------------------ control 3: reproduce Allinson measured s<->p intervals (in-sample)
TRANS = ROOT / "literature/pdf/E19_cs_defects/durham_data/Paper_Data/All_Transition_Data_incneg.txt"
lab = {(0, 0.5): "S1/2", (1, 0.5): "P1/2", (1, 1.5): "P3/2"}
sp = []
if TRANS.exists():
    out["params"]["transitions_sha256"] = hashlib.sha256(TRANS.read_bytes()).hexdigest()
    D = np.loadtxt(TRANS, skiprows=1)
    for n1, l1, j1, n2, l2, j2, f, ef in D:
        if (l1, j1) in lab and (l2, j2) in lab:
            calc = Q.freq_ghz(int(n1), A[lab[(l1, j1)]], int(n2), A[lab[(l2, j2)]])
            sp.append({"transition": f"{int(n1)}{lab[(l1, j1)]}->{int(n2)}{lab[(l2, j2)]}",
                       "meas_GHz": f / 1e9, "calc_GHz": calc, "resid_MHz": (f / 1e9 - calc) * 1e3})
# the same comparison for the paper's Table IV (printed labels), typed from the PDF text (quote Q-A6/A7)
TABLE_IV = [((20, "P1/2"), (20, "S1/2"), -710.9264), ((21, "P3/2"), (22, "S1/2"), 606.1677),
            ((30, "P3/2"), (30, "S1/2"), -516.1775), ((30, "P3/2"), (32, "S1/2"), 494.7101),
            ((36, "P3/2"), (34, "S1/2"), -541.4330), ((35, "P1/2"), (33, "S1/2"), -590.2641)]
tab = []
for (a, b, f) in TABLE_IV:
    calc = Q.freq_ghz(a[0], A[a[1]], b[0], A[b[1]])
    tab.append({"transition": f"{a[0]}{a[1]}->{b[0]}{b[1]}", "meas_GHz": f, "calc_GHz": calc, "resid_MHz": (f - calc) * 1e3})
alt = Q.freq_ghz(31, A["P3/2"], 30, A["S1/2"])
out["controls"]["allinson_sp_intervals"] = {
    "n_rows": len(sp),
    "resid_MHz_mean": float(np.mean([s["resid_MHz"] for s in sp])) if sp else None,
    "resid_MHz_rms": float(np.sqrt(np.mean([s["resid_MHz"] ** 2 for s in sp]))) if sp else None,
    "resid_MHz_maxabs": float(np.max([abs(s["resid_MHz"]) for s in sp])) if sp else None,
    "rows": sp, "tableIV_printed_rows": tab,
    "calc_31P3/2->30S1/2_GHz": alt,
}

# ------------------------------------------------------------ control 4: held-out absolute 6s -> np (Deiglmayr 2016 Table I)
DEIG_T1 = {  # n: (nu_p1/2, nu_p3/2) cm^-1, typed from the extracted Table I (quote Q-D3..)
    27: (31206.1897698, 31206.7447505), 50: (None, 31355.5869323), 56: (31366.5144268, 31366.5639566),
    62: (31374.3012688, 31374.3370559), 70: (31381.5844610, 31381.6088174), 74: (31384.3314669, 31384.3519001)}
held = []
for n, (v12, v32) in DEIG_T1.items():
    for sf, v in (("P1/2", v12), ("P3/2", v32)):
        if v is None:
            continue
        calc_shen = Q.term_cm(n, A[sf], Q.E_ION_CM)
        calc_deig_ie = Q.term_cm(n, A[sf], Q.E_ION_DEIGLMAYR_CM)
        calc_deig_all = Q.term_cm(n, Q.DEIGLMAYR[sf], Q.E_ION_DEIGLMAYR_CM)
        held.append({"state": f"{n}{sf}", "meas_cm": v,
                     "resid_MHz_AllinsonQD_ShenIE": (v - calc_shen) * Q.C_CM / 1e6,
                     "resid_MHz_AllinsonQD_DeiglmayrIE": (v - calc_deig_ie) * Q.C_CM / 1e6,
                     "resid_MHz_DeiglmayrQD_DeiglmayrIE": (v - calc_deig_all) * Q.C_CM / 1e6})
out["controls"]["deiglmayr_absolute_heldout"] = held

# ------------------------------------------------------------ control 5: R_Cs against CODATA R_inf
r_inf_cm = Q.R_INF_M / 100.0
me_over_mcore = r_inf_cm / Q.R_CS_CM - 1.0
me_u = sc.physical_constants["electron mass in u"][0]
out["controls"]["rydberg"] = {"R_inf_cm-1": r_inf_cm, "R_Cs_cm-1_Shen": Q.R_CS_CM,
                              "implied_m_core_u": me_u / me_over_mcore,
                              "implied_m_atom_u": me_u / me_over_mcore + me_u}

# ------------------------------------------------------------ provenance
try:
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
except Exception:
    commit = None
out["meta"] = {"git_commit": commit, "python": platform.python_version(), "numpy": np.__version__,
               "scipy": __import__("scipy").__version__, "mpmath": mp.__version__,
               "wall_s": time.time() - t0, "cpu_s": time.process_time() - c0, "seed": None}
(HERE / "results.json").write_text(json.dumps(out, indent=1, default=float))

# ------------------------------------------------------------ print tables
print(f"K = {Q.K_MHZ_UM3:.7e} MHz um^3")
print("n | nu(n-1 P1/2) nu(n-1 P3/2) nu(n P1/2) nu(n P3/2) [GHz] | sigma_cov [MHz] | R(n-1P3/2) R(nP3/2) R(n-1P1/2) R(nP1/2) [a0] | C3(n-1P3/2) C3(nP3/2) [MHz um^3]")
for r in out["results"]:
    n = r["n"]; k = [f"{n-1}P1/2", f"{n-1}P3/2", f"{n}P1/2", f"{n}P3/2"]
    print(n, " ".join(f"{r['nu_GHz_'+x]:.6f}" for x in k), "|",
          " ".join(f"{r['sig_MHz_cov_'+x]:.3f}" for x in k), "|",
          " ".join(f"{r['R_a0_'+x]:.2f}" for x in [k[1], k[3], k[0], k[2]]), "|",
          f"{r['C3_MHz_um3_'+k[1]]:.1f} {r['C3_MHz_um3_'+k[3]]:.1f}")
for r in out["results"]:
    n = r["n"]; k = [f"{n-1}P1/2", f"{n-1}P3/2", f"{n}P1/2", f"{n}P3/2"]
    print(n, "sigma_diag [MHz]", " ".join(f"{r['sig_MHz_diag_'+x]:.3f}" for x in k))
print(json.dumps(out["controls"]["hydrogen"], indent=0))
for c in cut:
    print(c["pair"], {k: round(v, 4) for k, v in c["R_by_rin"].items()}, "spread", f"{c['rel_spread_1to6']:.2e}", "h/2", f"{c['rel_change_h_half']:.2e}")
a = out["controls"]["allinson_sp_intervals"]
print("Allinson s-p intervals: n", a["n_rows"], "mean", a["resid_MHz_mean"], "rms", a["resid_MHz_rms"], "max", a["resid_MHz_maxabs"])
for t in tab: print(t)
print("calc 31P3/2->30S1/2", alt)
for h in held: print(h)
print(out["controls"]["rydberg"])
for c in out["source_comparison"]: print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in c.items()})
print("wall", out["meta"]["wall_s"])
