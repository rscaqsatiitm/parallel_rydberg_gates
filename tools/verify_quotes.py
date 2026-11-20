"""Check that every verbatim quote in a notes file occurs in the extracted PDF text.

Quote syntax in notes (Markdown): a line
    Q[<source_stem>]: "<verbatim text>"
where <source_stem> is a file stem in literature/text (e.g. arXiv_2304.05420).
Matching normalises whitespace, removes soft hyphenation at line breaks, unifies
quote/dash characters and ignores case. Exit code 1 if any quote is missing.
"""
import re, sys, pathlib, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[1]
TXT = ROOT / "literature" / "text"

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"-\s*\n\s*", "", s)           # hyphenation across lines
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("−", "-"), ("ﬁ", "fi"), ("ﬂ", "fl")):
        s = s.replace(a, b)
    s = re.sub(r"\s+", "", s)                 # whitespace-free comparison (PDF spacing is unreliable)
    return s.lower()

_cache = {}
def corpus(stem):
    if stem not in _cache:
        parts = [p.read_text(errors="ignore") for p in TXT.glob(stem + "*.txt")]
        if not parts:
            raise FileNotFoundError(stem)
        _cache[stem] = [norm(p) for p in parts]
    return _cache[stem]

def main(paths):
    pat = re.compile(r'Q\[([^\]]+)\]:\s*"(.+?)"\s*$')
    bad = n = 0
    for p in paths:
        for i, line in enumerate(pathlib.Path(p).read_text().splitlines(), 1):
            m = pat.search(line)
            if not m:
                continue
            n += 1
            stem, q = m.groups()
            q = q.replace("…", "...")
            pieces = [norm(x) for x in q.split("...") if x.strip()]
            try:
                ok = all(any(pc in c for c in corpus(stem)) for pc in pieces)
            except FileNotFoundError:
                ok = False
            if not ok:
                bad += 1
                print(f"MISSING {p}:{i} [{stem}] {q[:120]}")
    print(f"{n} quotes checked, {bad} not found")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
