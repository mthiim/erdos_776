# Combined proof dossier

`erdos776_complete_thresholds.pdf` is the stable review document for the
complete threshold candidate. It combines:

1. the prescribed-profile criterion and exact `r=11` proof;
2. the exact finite theorem `n_0(r)=2r+4` for `4<=r<=10`;
3. the L4 reverse-envelope proof; and
4. the uniform `r>=11` theorem candidate.

Rebuild from the repository root with:

```bash
./paper/build_pdf.sh
```

The build requires Pandoc and XeLaTeX. After rebuilding, render the PDF and
inspect it for clipped text or broken mathematical glyphs before release.
