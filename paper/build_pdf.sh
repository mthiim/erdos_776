#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_MD="$ROOT/paper/erdos776_complete_thresholds.md"
OUT_PDF="$ROOT/paper/erdos776_complete_thresholds.pdf"
{
  cat "$ROOT/paper/frontmatter.md"
  printf '\n# Part I: prescribed profiles and the exact case r=11\n\n'
  cat "$ROOT/docs/TECHNICAL_NOTE.md"
  printf '\n\\newpage\n\n# Part II: exact thresholds for 4 <= r <= 10\n\n'
  cat "$ROOT/docs/SMALL_R_NOTE.md"
  printf '\n\\newpage\n\n# Part III: the L4 reverse-envelope theorem\n\n'
  cat "$ROOT/docs/L4_PROOF.md"
  printf '\n\\newpage\n\n# Part IV: the uniform theorem for r >= 11\n\n'
  cat "$ROOT/docs/UNIFORM_THEOREM.md"
} > "$OUT_MD"

python3 - "$OUT_MD" <<'PYFIX'
from pathlib import Path
import sys
p = Path(sys.argv[1])
s = p.read_text(encoding="utf-8").replace("∎", r"\(\square\)")
for name in ("TECHNICAL_NOTE.md", "SMALL_R_NOTE.md", "L4_PROOF.md", "UNIFORM_THEOREM.md"):
    s = s.replace(f"]({name}", f"](../docs/{name}")
p.write_text(s, encoding="utf-8")
PYFIX

pandoc "$OUT_MD" \
  --from=markdown+raw_tex+tex_math_single_backslash \
  --pdf-engine=xelatex \
  -V mainfont="DejaVu Serif" \
  -V monofont="DejaVu Sans Mono" \
  -V mathfont="DejaVu Math TeX Gyre" \
  -V linestretch=1.03 \
  -o "$OUT_PDF"

echo "wrote $OUT_MD"
echo "wrote $OUT_PDF"
