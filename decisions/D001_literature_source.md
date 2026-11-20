# D001. Source of primary-PDF text for Stage 0

Date: 2026-11-20. Task: S0.

Rule 4.1 of the handover asks that quotes be read from the primary PDF in the owner's Drive
"Literature" folder (owner's Drive folder id 1QAlrqeLU6is0-S_i-pJnxzPSqgvyyYgM).

Found there (by title search, 2026-11-20): Evered et al. 2023 (parallel gates), Evered et al. 2026
(high-fidelity gates and nonlocal circuits), Perrin, Roger, Pupillo 2026, Pecorari et al. 2026.
Not found there: arXiv:2611.06613 (Zhang et al., JILA), Cong et al. 2022, arXiv:2411.04664, the
avalanche papers, Bluvstein et al. Nature 649, 39 (2026).

Decision: all quotes are taken from the arXiv PDF of each paper, downloaded with curl from
https://arxiv.org/pdf/<id> on 2026-11-20 and converted with poppler `pdftotext` (both reading-order
`*.raw.txt` and `-layout` `*.txt`). The Drive copies are not read through the Drive connector,
because it returns either a lossy text rendering or the whole PDF as base64 (too large to
process reliably). Consequence: the quoted version is the latest arXiv version on 2026-11-20, which
may differ from the journal version. Each notes file records the arXiv ID; journal-version checks
are an open task for a human (listed in docs/open_items.md).

Quotes are verified mechanically against the extracted text by `tools/verify_quotes.py`
(whitespace-, hyphenation- and case-insensitive substring match). Control: a real quote from
arXiv:2611.06613 passes and an invented sentence is reported missing (run 2026-11-20).
Limitation: text inside figures and some mathematical symbols are lost or garbled by pdftotext;
values read from figures are entered as ranges and flagged for a human check.
