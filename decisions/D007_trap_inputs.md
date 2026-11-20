# D007. Tweezer inputs for the contaminant-motion model

Date: 2026-11-20. Task S1/S2. Sourced: wavelength 852 nm (BLU25, EVE26; literature/notes/blu25_fig6g_traps.md);
EVE23 trap depth ~1 mK and temperature ~10 uK (EVE26: ~12 uK). Not found in any paper: trap waist,
BLU25 trap depth, whether traps are at full depth during the benchmark gaps, photoionisation rates.
Choices: U_g = 1 mK nominal (EVE23, same apparatus family), with results also given at 0.5 and 2 mK as a
sensitivity (not a sourced range: flagged); waist w in {0.8, 1.0, 1.2} um as a sensitivity (unsourced;
only the escape time depends on it, v_inf does not); traps at full depth throughout the gaps.
The waist and the BLU25 depth are added to docs/questions_for_authors.md.
