# E03b - independent Coulomb-approximation check of Rb radial dipole matrix elements

No ARC, nothing from `src/` or the other experiments. Code: `coulomb_me.py`. Output: `results.json`.
To reproduce, run `python3 coulomb_me.py` in this folder. It takes about 7 s.

## Sources

| stem | paper | how obtained | title verified |
|---|---|---|---|
| `arXiv_1103.6221` | M. Mack et al., "Measurement of absolute transition frequencies of 87Rb to nS and nD Rydberg states by means of electromagnetically induced transparency", PRA 83, 052515 (2011) | arXiv PDF, v1 | yes, p. 1 |
| `PRA67_052502_Li2003` | W. Li, I. Mourachko, M. W. Noel, T. F. Gallagher, "Millimeter-wave spectroscopy of cold Rb Rydberg atoms in a magneto-optical trap: Quantum defects of the ns, np, and nd series", PRA 67, 052502 (2003) | **There is no arXiv version.** I searched the arXiv API by author, title and keywords, and ran a web search. I used the publisher PDF that Bryn Mawr College posts in its institutional repository (repository.brynmawr.edu/physics_pubs/19), downloaded through the typeset.io mirror because Cloudflare blocks direct downloads from the repository. | yes, p. 1-2 of PDF |

Files: `literature/pdf/arXiv_1103.6221.pdf` and `literature/text/arXiv_1103.6221.raw.txt`; `literature/pdf/PRA67_052502_Li2003.pdf` and `literature/text/PRA67_052502_Li2003.raw.txt`.
pdftotext garbles Table VI of Li 2003 (it splits the columns apart). I rendered page 6 with `pdftoppm -r 200` and read the image; a copy is saved as `Li2003_page6_TableVI.png`.

Q[arXiv_1103.6221]: "Measurement of absolute transition frequencies of 87 Rb to nS and nD Rydberg states"
Q[arXiv_1103.6221]: "is the Rydberg constant, corrected for the reduced electron mass in 87 Rb."
Q[arXiv_1103.6221]: "3289.82119466(2) THz"
Q[arXiv_1103.6221]: "A precise measurement of the modified Rydberg-Ritz parameters for the nS, nP and nD series of 85 Rb was performed by Li et al. [11]."
Q[arXiv_1103.6221]: "Within the accuracy of our measurements on n ≥ 19 Rydberg states, the inclusion of higher order terms in the approximation did not lead to improved results."
Q[arXiv_1103.6221]: "TABLE I. Modified Rydberg-Ritz parameters δ0 and δ2 of the nS and nD lines of 85 Rb following [11] and of 87 Rb as determined in this work."
Q[arXiv_1103.6221]: "3.131 180 7(8)"
Q[arXiv_1103.6221]: "0.178 7(2)"
Q[arXiv_1103.6221]: "nS quantum defects refer to the fine structure levels, corrected for shifts due to hyperfine structure."
Q[PRA67_052502_Li2003]: "Quantum defects of the ns, np, and nd series"
Q[PRA67_052502_Li2003]: "where R Rb is the Rydberg constant for the reduced electron mass in Rb."
Q[PRA67_052502_Li2003]: "109 736.605 cm"
Q[PRA67_052502_Li2003]: "TABLE VI. The previous and improved quantum defects for s, p, and d series."
Q[PRA67_052502_Li2003]: "2.654 884 9"
Q[PRA67_052502_Li2003]: "2.641 673 7"
Q[PRA67_052502_Li2003]: "85Rb atoms are held in a vapor loaded MOT"

## Parameters used (modified Rydberg-Ritz: delta(n) = delta0 + delta2/(n - delta0)^2; neither paper gives delta4)

| series | delta0 | delta2 | isotope | location |
|---|---|---|---|---|
| nS1/2 | 3.1311807(8) | 0.1787(2) | **87Rb** | Mack 2011, Table I, column "87Rb (this work)", p. 4 (text extraction is clean) |
| nP1/2 | 2.6548849(10) | 0.2900(6) | **85Rb** | Li 2003, Table VI, "Improved values", p. 052502-5 (TABLE READ from rendered page) |
| nP3/2 | 2.6416737(10) | 0.2950(7) | **85Rb** | Li 2003, Table VI, same place (TABLE READ). The text gives 2.641 673 7(3), 0.2950(3) before the uncertainties are combined. |
| nS1/2 (cross-check) | 3.1311804(10) | 0.1784(6) | 85Rb | Li 2003, Table VI (TABLE READ). Mack Table I reprints the same values. |

Neither source has 87Rb nP parameters. Mack measured only nS and nD. Li measured nS, nP and nD, but on 85Rb (Mack calls them "85Rb"). Using the 85Rb nP values for 87Rb is therefore an approximation. For nS, the 87Rb and 85Rb values agree within their errors. Replacing Mack's nS values with Li's changes the matrix elements by less than 6e-7 and the frequencies by less than 25 kHz (see `crosscheck_with_Li2003_85Rb_nS_defects` in results.json).

Rydberg constant: I used Mack Eq. (1), R* = R_inf/(1 + m_e/m_87Rb) with R_inf = 3289.82119466 THz. The papers do not give m_e/m_87Rb. I took m_e = 5.48579909065e-4 u (CODATA) and m(87Rb) = 86.909180531 u, which gives m_e/M = 6.312e-6 and R* = 3289.80042 THz. Li's R_Rb = 109 736.605 cm^-1 (times c = 3289.80050 THz, quoted for unspecified "Rb") changes the frequencies by about 6 ppm (≤ 0.17 MHz). Only the quantum defects enter the wavefunctions. The reduced mass rescales lengths by 1 + m_e/M, and I applied this factor (6 ppm).

## Method

- Coulomb approximation. Pure -1/r potential with E = -1/(2 n*^2), where n* = n - delta(n), in reduced-mass atomic units.
- Square-root grid x = sqrt(r) with u(r) = x^(1/2) chi(x), so chi'' = [(4l(l+1)+3/4)/x^2 - 8 + 4x^2/n*^2] chi. Uniform step h = 0.005 in x.
- Numerov integration inward from r_out = 2n*(n*+15) a0, about 2.6 times the outer turning point, down to an inner cutoff r_c = 1.0 a0, which is near the Rb+ core.
- Each function is normalised with ∫2x^2 chi^2 dx = 1, using Simpson's rule.
- Matrix element: <a|r|b> = ∫2x^4 chi_a chi_b dx.
- **Sign convention:** every u(r) = rR(r) is chosen positive in its outermost lobe. With this choice, all four Rb matrix elements come out positive.
- Frequency: nu = R* (1/n*_S^2 - 1/n*_P^2), which is E(P) - E(S). A negative value means the P state lies below 53S.

## Hydrogen control (delta = 0)

The reference values are exact. For n ≠ n' I implemented Gordon's formula with mpmath hypergeometric functions. For n = n' I used <n l|r|n l-1> = -(3/2) n sqrt(n^2-l^2). Both are checked a second way, by direct mpmath quadrature of the analytic Laguerre wavefunctions. The Numerov result is compared after converting the textbook sign (u > 0 at the origin) to the outer-lobe convention with the factor (-1)^(n-l-1)(-1)^(n'-l'-1). These runs use r_c = 1e-4 and h = 0.002.

| pair | exact (outer-lobe sign) | Numerov | rel. err | Gordon vs quadrature |
|---|---|---|---|---|
| 2s-2p | 5.196152 | 5.196152 | 6e-13 | 0 |
| 10s-10p | 149.248116 | 149.248116 | 1e-13 | 5e-9 |
| 30s-31p | 315.863255 | 315.863255 | 2e-12 | 2e-15 |
| 3p-5d | -2.968322 | -2.968322 | 8e-12 | 0 |
| 20p-21s | 127.603591 | 127.603591 | 5e-11 | 3e-12 |

All pairs pass the 1e-4 requirement by a wide margin.

## Convergence (maximum relative change over the four Rb matrix elements, compared with r_c = 1 a0, h = 0.005)

| setting | max rel. change |
|---|---|
| r_c = 0.5 a0 | 1.7e-6 |
| r_c = 2 a0 | 7.1e-7 |
| r_c = 3 a0 | 3.6e-6 |
| r_c = 5 a0 | 1.6e-5 |
| r_c = 8 a0 | 2.5e-5 |
| h = 0.01 | 3.9e-8 |
| h = 0.0025 | 2.0e-8 |

The result is insensitive to the cutoff. Over 0.5-8 a0 the change is far below the required 0.5 %.

## Results (87Rb; nP defects from 85Rb)

| transition | n*_S | n*_P | <S|r|P> (a0) | nu = E_P - E_S (GHz) |
|---|---|---|---|---|
| 53S1/2 - 52P1/2 | 49.868747 | 49.344996 | 2612.23 | -28.2308 |
| 53S1/2 - 52P3/2 | 49.868747 | 49.358205 | 2660.31 | -27.5078 |
| 53S1/2 - 53P1/2 | 49.868747 | 50.345001 | 2884.35 | +24.9095 |
| 53S1/2 - 53P3/2 | 49.868747 | 50.358210 | 2839.34 | +25.5903 |

Caveat: the Coulomb approximation ignores core polarisation and spin-orbit terms in the potential. Apart from that, the j dependence enters only through n*. The resulting model error is not quantified here. The 1e-5 figures above describe numerical error only.
