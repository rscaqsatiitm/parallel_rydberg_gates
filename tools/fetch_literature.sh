#!/usr/bin/env bash
# Re-create literature/pdf and literature/text from arXiv. Usage: tools/fetch_literature.sh
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p literature/pdf literature/text
for id in $(cat literature/arxiv_ids.txt | grep -v '^#' | awk '{print $1}'); do
  f=literature/pdf/arXiv_$id.pdf
  [ -s "$f" ] || curl -sSL --max-time 120 -o "$f" "https://arxiv.org/pdf/$id"
  pdftotext "$f" "literature/text/arXiv_$id.raw.txt" 2>/dev/null
  pdftotext -layout "$f" "literature/text/arXiv_$id.txt" 2>/dev/null
done
