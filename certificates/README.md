# Certificates

## Exact range `4 <= r <= 10`

`small_r_full_witnesses_r4_to_10.txt` contains explicit full-profile
witnesses at `n=2r+5` for every `r=4,...,10`.

`small_r_cores_and_free_sets_r4_to_10.txt` contains the complete canonical
base core on `q=r+5` points and the `r` explicit free `(r+1)`-sets for each
of those seven values.

Regenerate both deterministically with:

```bash
python3 tools/generate_small_r_certificates.py
```

Verify them independently with:

```bash
python3 verification/verify_small_r_exact.py
```

## Exact `r=11` and nearby construction data

`r11_n27_23_levels.txt` is the explicit 253-set lower-bound certificate for
`g(27,11)>=23`.

`2r_plus_6_r_11_to_20.txt` contains explicit full-profile witnesses at
`n=2r+6` for each `r=11,...,20`.

`r11_core_and_free_sets.txt` contains the complete 132-set core on 16 points
and 11 explicitly listed free 12-subsets that sustain indefinite padding.

The release tests perform direct profile and pairwise-containment checks and
do not use shadow or colex arithmetic to decide whether the stored sets form
antichains.
