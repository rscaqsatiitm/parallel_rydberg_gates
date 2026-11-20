# D002. PDFs and extracted full text are not committed

Date: 2026-11-20. Task: S0.

arXiv licences differ by paper and many grant arXiv, not third parties, the right to distribute.
The PDFs and full-text extractions therefore live only in the working tree (git-ignored).
`tools/fetch_literature.sh` re-creates them from arXiv; notes files carry short verbatim quotes
(fair-use length) that `tools/verify_quotes.py` checks after the fetch.
