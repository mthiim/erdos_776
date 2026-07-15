# Optional computations

The main release check is `tests/verify_r11.py`.

`validate_profile_thm.py` is a slower, optional hostile check of the profile
criterion. It enumerates every antichain profile on $[n]$ for
$n=4,5,6$, then compares that set against the exact criterion for every
candidate profile vector within the level capacities.

Run from the repository root:

```bash
python3 computations/validate_profile_thm.py
```

The expected numbers of candidate vectors are 700, 17,424, and 1,053,696,
respectively.

