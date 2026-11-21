# E19: an independent route to Cs nS–nP frequencies, radial matrix elements and C3 (no ARC)

**Purpose.** This is a second route to Cs Rydberg nS1/2 ↔ n'P_J frequencies and radial dipole matrix elements, to
compare with values computed elsewhere (not seen here). It does not import or call ARC. It uses a source set that is
independent of ARC's caesium data.

**Files.** `cs_qd.py` holds the parameters, the energies and the Numerov integration. `run.py` holds the results
and controls and writes `results.json`; its console output is in `output.txt`. Quotes are in
`literature/notes/cs_quantum_defects.md`, and `python3 tools/verify_quotes.py` passes on it (51/51).
Run: `python3 experiments/E19_cs_defects/run.py` (about 4 s on 4 CPUs, deterministic, no random numbers).

## Sources and parameters

| quantity | value | source (quote in notes) |
|---|---|---|
| δ0, δ2, δ4 nS1/2 | 4.049368(3), 0.2333(14), 0.8(2) | Allinson et al. 2025, arXiv:2502.20961, Table I "This work" |
| δ0, δ2, δ4 nP1/2 | 3.591606(3), 0.3569(13), 0.81(14) | same |
| δ0, δ2, δ4 nP3/2 | 3.559091(3), 0.3657(13), 1.17(14) | same |
| covariance of all δ | 27×27 published matrix | Allinson data set doi:10.15128/r2df65v802x (sha256 in notes) |
| alternative nS1/2 | 4.04935994(17), 0.238017(18), 0.1747(33) | Shen et al. 2024, arXiv:2410.19129, Table I |
| E_ion | 31406.46775148(14) cm⁻¹ | Shen 2024 (absolute terms only; cancels in every interval) |
| R_133Cs | 109736.8627304 cm⁻¹ | Shen 2024 (= R∞/(1+me/mcore)) |
| c, a0, e, ε0, h, R∞ | CODATA 2022 via scipy 1.18.1 | |
| K = e²a0²/(4πε0 h) | 9.7500856e-4 MHz µm³ | computed from CODATA |

Quantum defect: δ(n) = δ0 + δ2/(n−δ0)² + δ4/(n−δ0)⁴ (modified Ritz, Allinson Eq. 2). Then n* = n − δ(n) and
E = E_ion − R_Cs/n*².

**Independence from ARC.** The installed ARC 3.10.2 source (`alkali_atom_data.py`, class `Caesium`) takes its S,
P1/2 and P3/2 defects and its ionisation energy (31406.4677325 cm⁻¹) from Deiglmayr et al. 2016 (PRA 93, 013424).
Allinson 2025 is a different experiment: THz and rf Rydberg–Rydberg intervals in a thermal vapour, n = 14–38, with
its own global fit that uses no outside data. Shen 2024 is also a different experiment. The two routes share the
modified-Ritz functional form. They also share the Coulomb-approximation idea only if the other route uses it (ARC
normally uses a model potential).

**Caveat.** Allinson's fit covers n = 14–38. Every result at n = 50–80 is therefore an extrapolation of the δ2/δ4
terms. The δ0 values dominate at these n.

## Method

- Frequencies: ν = c R_Cs (1/n*_S² − 1/n*_P²), signed as E(final) − E(initial). The (n−1)P states lie below nS.
- Uncertainty: linear propagation through the published covariance, with correlations (σ_cov). The fit's S and P
  δ0 are strongly correlated, so the interval uncertainty is 3–4 times smaller than with the diagonal alone (σ_diag
  is in `results.json`).
- Radial matrix elements: Numerov integration of the pure −1/r Coulomb potential at E = −1/(2n*²) a.u. On a
  √r grid (x = √r, R = x^(−3/2) X) the equation is X'' = [8x²(V−E) + (2l+½)(2l+3/2)/x²] X. This form was derived
  symbolically with sympy in this session. The integration runs inward from r = 2n*(n*+15) to an inner cutoff
  r_in = 3 a0, with step h = 0.005 √a0. The function is normalised on [r_in, r_max], and R = ∫ R_nS R_n'P r³ dr. The
  sign convention is outermost lobe positive, which makes every R here positive. The J dependence enters only
  through n*. The reduced-mass scaling of lengths (about 4e-6) is neglected.
- C3 for the stretched pair |nS1/2, +1/2⟩ ↔ |n'P3/2, +3/2⟩: C3 = K·R²/3 (angular factor 1/3).

## Results (Allinson 2025 defects; ν in GHz, σ_cov in MHz; R in a0; C3 in MHz µm³)

| n | ν→(n−1)P1/2 | ν→(n−1)P3/2 | ν→nP1/2 | ν→nP3/2 | σ_cov (4 transitions) | R(n−1)P1/2 | R(n−1)P3/2 | R nP1/2 | R nP3/2 | C3 (n−1)P3/2 | C3 nP3/2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 50 | −37.438082 | −35.155835 | 30.582133 | 32.720063 | 0.080 0.070 0.077 0.068 | 2155.72 | 2257.12 | 2504.91 | 2412.18 | 1655.8 | 1891.1 |
| 52 | −32.921175 | −30.915647 | 26.929641 | 28.813479 | 0.073 0.064 0.070 0.062 | 2349.77 | 2460.14 | 2725.63 | 2624.58 | 1967.0 | 2238.8 |
| 55 | −27.413484 | −25.745017 | 22.466318 | 24.039336 | 0.063 0.055 0.060 0.053 | 2656.50 | 2781.04 | 3074.19 | 2959.97 | 2513.6 | 2847.5 |
| 60 | −20.671079 | −19.414633 | 16.985954 | 18.176777 | 0.050 0.044 0.048 0.042 | 3209.51 | 3359.58 | 3701.69 | 3563.75 | 3668.2 | 4127.6 |
| 65 | −15.970335 | −15.000684 | 13.152507 | 14.075569 | 0.040 0.035 0.039 0.034 | 3814.76 | 3992.72 | 4387.43 | 4223.53 | 5181.1 | 5797.5 |
| 70 | −12.593413 | −11.829510 | 10.391018 | 11.120938 | 0.033 0.029 0.032 0.028 | 4472.25 | 4680.48 | 5131.39 | 4939.31 | 7119.8 | 7929.0 |
| 80 | −8.231673 | −7.733101 | 6.812672 | 7.291929 | 0.022 0.019 0.021 0.019 | 5943.93 | 6219.84 | 6794.01 | 6538.83 | 12573.2 | 13895.9 |

**Dependence on the defect set (frequency differences in MHz, from `results.json` → `source_comparison`).**

| n | Deiglmayr(ARC source) − Allinson: (n−1)P1/2, (n−1)P3/2, nP1/2, nP3/2 | Shen nS + Allinson nP − Allinson |
|---|---|---|
| 50 | +0.31, +0.53, +0.25, +0.45 | −0.41 (all four) |
| 60 | +0.17, +0.31, +0.14, +0.27 | −0.25 |
| 70 | +0.10, +0.19, +0.09, +0.17 | −0.16 |
| 80 | +0.07, +0.13, +0.06, +0.12 | −0.11 |

These spreads are 3–7 σ_cov. **σ_cov understates the real uncertainty at n ≥ 50.** A realistic systematic on these
frequencies is about ±0.5 MHz at n = 50, falling roughly as n*⁻³. Changing the defect set moves R by ≤ 1.3e-5
relative (for example 2257.148 vs 2257.125 a0 for 50S–49P3/2).

## Controls

1. **Hydrogen against closed form.** The exact radial integrals come from explicit Laguerre polynomials at
   400-digit mpmath precision. The n = n' cases also match the Bethe–Salpeter formula (3/2)n√(n²−1).
   With r_in → 0 the relative error is ≤ 1.4e-8 at n = 50 and ≤ 3.5e-7 for 80s–79p. With the production cutoff
   r_in = 3 a0 it is 8e-6 at n = 50 and 2e-6 at n = 80, but 1.3e-3 at n = 10.
   PASS, since the production cases are at n ≥ 49.
2. **Inner-cutoff sensitivity** (Cs, r_in = 1…6 a0). The relative spread of R is 2.5e-5 at n = 50 and 5.5e-6 at
   n = 80, which gives C3 changes ≤ 5e-5. With r_in = 10 a0, R moves by 5e-5. PASS.
3. **Grid.** Halving h changes R by ≤ 3e-10. PASS.
4. **Reproducing quoted spectroscopic intervals (in-sample).** The fit reproduces all 30 s↔p rows of Allinson's
   measured data with a mean residual of +0.12 MHz, rms 0.93 MHz and a largest residual of 2.4 MHz (the stated
   measurement error is 0.5 MHz). Example: 20p1/2→20s1/2 measures −710.9264 GHz against a calculated −710.92651 GHz.
   The paper says its fit residuals are at the MHz level. Finding: the Table IV row printed "30p3/2 → 30s1/2
   −516.1775" is 31p3/2→30s1/2 in the authors' data file. The calculation gives −516.1780 GHz for 31p3/2→30s1/2.
5. **Held-out absolute check against Deiglmayr 2016 Table I** (6s c.o.g. → np, which entered no part of the Allinson
   or Shen fits). The calculation uses Allinson's P defects with Shen's E_ion. Residuals (measured − calculated):
   +5.0 MHz at n = 27, +0.69 MHz at 50P3/2, +0.19/+0.34 MHz at 56P1/2/56P3/2, about 0 at 62, and −0.28 to −0.02 MHz
   at 70–74. The n = 27 offset scales like n*⁻³, so absolute δ0 differs at about 1e-5 (about 3σ of a single δ0).
   With Deiglmayr's own defects and ionisation energy, the residuals are ≤ 0.11 MHz, which is consistent (that set
   was fitted to these data). Above n = 50 the independent route agrees with Deiglmayr's absolute data to
   ≤ 0.7 MHz.
6. **Rydberg constant.** CODATA R∞ (109737.31568157 cm⁻¹) together with Shen's R_Cs implies m(133Cs) =
   132.905467 u, consistent with a Cs-133 atom. This only checks consistency; no mass value was sourced.

## Not done / limits

- The Coulomb approximation is not compared with a model-potential calculation (core penetration and polarisation
  at r < r_in). The cutoff scan bounds only the sensitivity to the cutoff choice, not the core physics. In the
  hydrogen control, differences of order 1e-5 come from the cutoff alone.
- Weber & Sansonetti 1987, Lorenzen & Niemax 1984 and Goy et al. are paywalled and were not read. Song et al.
  2024 (Opt. Express, microwave nS→nP, n = 41–55, the closest in n) was seen only in a search summary and was
  not used.
- The Deiglmayr 2025 erratum was not read.

## Comparison with E11 (ARC) (appended by the parent session, 2026-11-21; compare_E11.txt)
Not pre-registered as a separate experiment: it is the independent route requested by Addendum 3 item 6, written by a
separate agent without ARC calls and without access to the E11 numbers; the E03 tolerance (2 % on matrix elements)
is used for C3, and no tolerance was fixed for frequencies.
**Lines:** E11 (ARC, Deiglmayr 2016 defects) minus E19 (Allinson 2025 defects): +0.06 to +0.53 MHz for n = 50-80
(n = 60: +0.14 to +0.31 MHz on lines of 17-21 GHz, i.e. < 2e-5 relative). The difference is 3-7 sigma of the Allinson
covariance but is an extrapolation from n <= 38; it is irrelevant for a broadband noise source and for every
prediction frozen in v1. **C3:** agreement to 2e-5 - 8.4e-5 relative (PASS against 2 %). Shared layers: the
modified Ritz formula and the Coulomb-type radial integration (ARC: model potential; E19: Coulomb approximation);
the quantum-defect data and the code are independent. **Verdict: the E11 lines and C3 values are confirmed by an
independent route.**
