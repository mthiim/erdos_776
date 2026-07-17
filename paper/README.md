# Combined proof dossier

`erdos776_complete_thresholds.pdf` is the generated review document for the
complete threshold proof package. Its release identifier is
`v0.4.1-proof-claim`. It combines:

1. the prescribed-profile criterion and exact `r=11` proof;
2. the exact finite theorem `n_0(r)=2r+4` for `4<=r<=10`;
3. the L4 reverse-envelope proof; and
4. the uniform `r>=11` theorem.

The source notes now use the carry-centered assembly, the puncturing lemma
for free sets, the asymmetric profile criterion, and the lower-window segment
table. Lean proves the original-formulation least-threshold statement for every
`r>=4`; the cited `r=2,3` cases remain external.

Rebuild from the repository root with:

```bash
./paper/build_pdf.sh
```

The build requires Pandoc and XeLaTeX. After rebuilding, render the PDF and
inspect it for clipped text or broken mathematical glyphs before release.
