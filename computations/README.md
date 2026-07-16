# Exhaustive profile validation

The full release check is:

```bash
python3 tests/verify_all.py
```

`validate_profile_thm.py` is the slower exhaustive check of the profile
criterion included in that release suite. It enumerates every antichain
profile on $[n]$ for

$n=4,5,6$, then compares that set against the exact criterion for every
candidate profile vector within the level capacities.

Run from the repository root:

```bash
python3 computations/validate_profile_thm.py
```

The expected numbers of candidate vectors are 700, 17,424, and 1,053,696,
respectively.

