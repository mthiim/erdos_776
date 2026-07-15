# Certificates

`r11_n27_23_levels.txt` is the explicit 253-set lower-bound certificate for
$g(27,11)\ge23$. Regenerate it with:

```bash
python3 tools/generate_certificates.py
```

`2r_plus_6_r_11_to_20.txt` contains explicit full-profile witnesses at
$n=2r+6$ for each $r=11,\ldots,20$.

`r11_core_and_free_sets.txt` contains the complete 132-set core on 16
points and 11 explicitly listed free 12-subsets that sustain the indefinite
padding construction. The release verifier parses and checks this file
directly rather than regenerating it.

Both formats are parsed by `src/ep776_check.py`. The release test performs
direct profile and pairwise-containment checks and does not use shadow or
colex arithmetic to decide whether the emitted sets form an antichain.
