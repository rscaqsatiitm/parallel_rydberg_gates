# Cs (133Cs) quantum defects for nS1/2, nP1/2, nP3/2: independent source set (E19)

Read 2026-11-21. PDFs in `literature/pdf/E19_cs_defects/` (gitignored), text in `literature/text/<stem>.raw.txt`
(`pdftotext -layout`). Table values are quoted as the table rows appear in the extracted text. `verify_quotes.py`
ignores whitespace, so the thousands spacing in the numbers ("4.049 353 2") is part of the quote.

## Primary source: Allinson et al. 2025 (arXiv:2502.20961; Phys. Rev. A 111, 062802 (2025))

THz and rf spectroscopy of Rydberg-Rydberg intervals in a thermal Cs vapour (Durham). It gives one global fit of
δ0, δ2, δ4 for all series with ℓ ≤ 4. The fit uses intervals only, so it has no ionisation energy. **We use it as
the primary set for nS1/2, nP1/2 and nP3/2.**

Range and independence:
Q[arXiv_2502.20961]: "based on transition frequency measurements between Rydberg states (14 ≤ n ≤ 38) obtained"
Q[arXiv_2502.20961]: "measurements of the quantum defect parameters δ0,2,4 in ... Cs for all states with ℓ ≤ 4 without relying on any data"
Q[arXiv_2502.20961]: "Therefore the expansion is truncated at fourth order and ... three parameters (δ0,2,4 ) are quoted."

Model (Eq. 2, modified Rydberg-Ritz with (n−δ0) in the denominators; Eq. 1 for intervals):
Q[arXiv_2502.20961]: "using the modified Rydberg-Ritz equation as [51]"
Q[arXiv_2502.20961]: "(n − δ0 )2 (n − δ0 )4 (n − δ0 )6"
Q[arXiv_2502.20961]: "where c is the speed of light and R∞ is the Rydberg"
Q[arXiv_2502.20961]: "constant (in m−1 ) for the relevant species (Cs in this"
FIGURE/TABLE READ: Eq. (2), p. 3, read from the layout text as δ(n) = δ0 + δ2/(n−δ0)^2 + δ4/(n−δ0)^4 + …. The
extraction breaks the fraction into separate lines; the denominators are quoted above.

Table I (p. 5), "This work" rows. Columns are s1/2, p1/2, p3/2, d3/2, d5/2, f5/2, f7/2, g7/2, g9/2. Only the first
three columns are used.
Q[arXiv_2502.20961]: "s1/2 p1/2 p3/2 d3/2 d5/2 f5/2 f7/2 g7/2 g9/2"
Q[arXiv_2502.20961]: "δ0 4.049368(3) 3.591606(3) 3.559091(3) 2.475474(4) 2.466327(4)"
Q[arXiv_2502.20961]: "This work δ2 0.2333(14) 0.3569(13) 0.3657(13)"
Q[arXiv_2502.20961]: "δ4 0.8(2) 0.81(14) 1.17(14)"
Q[arXiv_2502.20961]: "TABLE I. Quantum defect values found in this work compared to a collation the most recent measurements."

Covariance (used for uncertainty propagation):
Q[arXiv_2502.20961]: "in Table I. The entire 27 × 27 covariance matrix derived"
Q[arXiv_2502.20961]: "from our global fit can be found at [53]."
Q[arXiv_2502.20961]: "[53] http://doi.org/10.15128/r2df65v802x"
DATA FILE (not a PDF, so no Q-quote is possible): `Paper_Data.zip` from doi:10.15128/r2df65v802x (Durham Research
Online). sha256 of the zip: 5bd5819cd2049dd7b45134b8242a16d1f3a63e4c6f942eaa37a6d77d0e9bc9d6. It contains
`d4_Covariance_Matrix.txt` (sha256 8f97bffc557e7683215c6ea693a58687619a770eb018c73c5ea45f2a94ce51d6) and
`All_Transition_Data_incneg.txt` (sha256 3cb359dc87b76184a589f99de146bad2589ffd0fbc5b013c3d7c107d58e0cd61).
Ordering: δ0 for the 9 series, then δ2 for the 9, then δ4 for the 9, with the series in Table I order. This is
checked in two ways: by `reorder_qds` in the authors' `Correlation_Plot.py`, and because the square roots of the
diagonal equal the Table I uncertainties (s1/2: 3.2e-6, 1.45e-3, 0.22). The Durham fit scripts use ARC only for
the Rydberg constant (`R = atom.scaledRydbergConstant` in `Fit_Resids.py`).

Measured s↔p intervals (Table IV, p. 10), used as an in-sample control:
Q[arXiv_2502.20961]: "20p1/2 → 20s1/2 -710.9264"
Q[arXiv_2502.20961]: "30p3/2 → 30s1/2 -516.1775"
Q[arXiv_2502.20961]: "The p → s and p → d measurements have errors of 0.5 MHz."
FINDING: the Table IV row printed as "30p3/2 → 30s1/2 -516.1775" is labelled 31p3/2 → 30s1/2 in the authors' data
file (`31 1 1.5 30 0 0.5 -516177468000`). The Table I defects give −516.1780 GHz for 31p3/2→30s1/2 and −179.43 GHz
for 30p3/2→30s1/2, so the printed label is a typo.

Comparison row that this paper collates (it is ARC's source, see below):
Q[arXiv_2502.20961]: "δ0 4.0493532(4) 3.5915871(3) 3.5590676(3)"
Q[arXiv_2502.20961]: "δ2 0.2391(5) 0.36273(16) 0.37469(14)"
Q[arXiv_2502.20961]: "1/2 , p1/2 , p3/2 , d5/2 , quantum defects are from [20]"
Q[arXiv_2502.20961]: "[20] J. Deiglmayr, H. Herburger, H. Saßmannshausen,"

## Secondary source: Shen et al. 2024 (arXiv:2410.19129; Phys. Rev. Lett. 133, 233005 (2024))

Absolute 6S→nS1/2 and 6S→nD frequencies in a field-free sample (n = 23–90). **It supplies the ionisation energy and
the reduced-mass Rydberg constant, and an alternative nS1/2 set used as a cross-check.** It has no nP data.

Q[arXiv_2410.19129]: "where EI is the ionization energy and R is the reduced"
Q[arXiv_2410.19129]: "mass Rydberg constant, equal to R∞ /(1 + me /mcore )."
Q[arXiv_2410.19129]: "R133 Cs = 109736.8627304 cm−1"
Q[arXiv_2410.19129]: "We constrain the quantum defects to a three-term"
Q[arXiv_2410.19129]: "nD5/2 [this work] nD5/2 [45] nD3/2 [this work] nD3/2 [46] nS1/2 [this work] nS1/2 [45]"
Q[arXiv_2410.19129]: "δ0 2.46631529(14) 2.46631524(63) 2.47545840(13) 2.4754562 4.04935994(17) 4.04935665(38)"
Q[arXiv_2410.19129]: "δ2 0.013431(65) 0.013577 0.008339(62) 0.009320 0.238017(18) 0.2377037"
Q[arXiv_2410.19129]: "δ4 −0.3613(61) −0.37457 −0.3769(95) −0.43498 0.1747(33) 0.255401"
Q[arXiv_2410.19129]: "The uncertainty-weighted average ionization energy is"
Q[arXiv_2410.19129]: "31406.46775148(14) cm−1 ."
Q[arXiv_2410.19129]: "higher than the most recent value presented in Ref. [49],"
Q[arXiv_2410.19129]: "31406.4677325(14) cm−1 ."
Q[arXiv_2410.19129]: "[49] J. Deiglmayr, H. Herburger, H. Saßmannshausen,"
The nS1/2 [this work] column (n = 23–90) is used: δ0 = 4.04935994, δ2 = 0.238017, δ4 = 0.1747. The table caption
says the comparison columns are ARC's values, but the nS1/2 [45] column (4.04935665) is not the ARC/Deiglmayr value
(4.0493532). That column is not used here.

## ARC's source, used only as the comparison reference: Deiglmayr et al. 2016 (arXiv:1601.08005; PRA 93, 013424)

UV 6s→np spectroscopy in an optical dipole trap. nP from n = 27–74. The nS1/2 defects come from combining their data
with older millimetre-wave intervals (Ref. [11] of that paper).
Q[arXiv_1601.08005]: "δ0 3.591 587 1(3) 3.559 067 6(3)"
Q[arXiv_1601.08005]: "δ2 0.362 73(16) 0.374 69(14)"
Q[arXiv_1601.08005]: "δ0 4.049 353 2(4) 2.466 314 4(6)"
Q[arXiv_1601.08005]: "δ2 0.239 1(5) 0.013 81(15)"
Q[arXiv_1601.08005]: "δ4 0.06(10) -0.392(12)"
Q[arXiv_1601.08005]: "δ6 11(7) -1.9(3)"
Q[arXiv_1601.08005]: "δ8 -209(150)"
Table I (absolute 6s1/2 c.o.g. → np wavenumbers, used as a held-out control):
Q[arXiv_1601.08005]: "of all observed transitions to np1/2 and"
Q[arXiv_1601.08005]: "27 31 206.189 769 8 14 31 206.744 750 5 -3"
Q[arXiv_1601.08005]: "50 – – 31 355.586 932 3 -20"
Q[arXiv_1601.08005]: "56 31 366.514 426 8 -14 31 366.563 956 6 -18"
Q[arXiv_1601.08005]: "62 31 374.301 268 8 -17 31 374.337 055 9 59"
Q[arXiv_1601.08005]: "70 31 381.584 461 0 -110 31 381.608 817 4 70"
Q[arXiv_1601.08005]: "74 31 384.331 466 9 -36 31 384.351 900 1 -17"
Q[arXiv_1601.08005]: "The estimated standard deviation of all"
Q[arXiv_1601.08005]: "line positions is 2 · 10−6 cm−1 ."
NOT READ: a web search summary said a 2025 erratum (PRA 112, 049902(E)) corrects the Deiglmayr ionisation energy for
an ac Stark shift. I did not read the erratum. Shen 2024 (quoted above) reports an ionisation energy 600 kHz higher.

## Is ARC's caesium data from the same source?

SOURCE-CODE READ (installed `arc` 3.10.2, `arc/alkali_atom_data.py`, class `Caesium`; no ARC function was called):
the docstring says "quantum defects for S_{1/2}, nP_{1/2}, nP_{3/2}, D_{5/2} are from
https://doi.org/10.1103/PhysRevA.93.013424". That DOI is Deiglmayr 2016. `quantumDefect` holds S
[4.0493532, 0.2391, 0.06, 11, -209], P1/2 [3.5915871, 0.36273], P3/2 [3.5590676, 0.37469], and
`ionisationEnergy = 31406.4677325 cm^-1` (Ref. jd2016, also Deiglmayr). **So ARC's S, P1/2 and P3/2 defects and its
ionisation energy are all from Deiglmayr 2016.** Allinson 2025 is a separate experiment (thermal vapour, THz
intervals, own global fit, n = 14–38) with no data shared with Deiglmayr, so it is independent of ARC's data.
Shen 2024 is also a separate experiment. Shared layers: both use the same modified Rydberg-Ritz form, and Allinson's
own fit code takes the reduced Rydberg constant from ARC. E19 takes R_Cs from Shen instead.

## Sources looked for but not used
Weber & Sansonetti 1987 (PRA 35, 4650), Lorenzen & Niemax 1984 (Z. Phys. A 315, 127) and Goy et al. 1982/1986 are
paywalled, with no arXiv copy, and were not read. Song et al., Opt. Express 2024 (doi:10.1364/oe.528290; microwave
nS→nP, n = 41–55) appeared only in a search-engine summary and was not read. Its numbers are not used.
