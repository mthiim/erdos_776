# Erdős Problem #776: antichain-profile certificates

This is a preliminary, reproducible research package for the
Erdős–Trotter antichain problem ([Erdős Problem #776](https://www.erdosproblems.com/776)).
This package was assembled on 15 July 2026 from an AI-assisted investigation and is
being shared to invite mathematical scrutiny.

## Results contained in this package

The package gives a self-contained proof and executable checks for:

1. The classical squashed/colex characterization of feasible antichain
   profiles, expressed as an iterated Kruskal–Katona recurrence.
2. The exact value $g(27,11)=23$.
   In particular, the profile with 11 sets on every level 2 through 25 is
   impossible: its recurrence has
   $m_2=352>\binom{27}{2}=351$. A 23-level profile is explicitly
   constructed and checked.
3. The exact threshold $n_0(11)=27$.
   A core construction at $n=28$, followed by a two-point padding lemma,
   gives a full-profile antichain for every $n\ge 28$.

The mathematical argument is in
[`docs/TECHNICAL_NOTE.md`](docs/TECHNICAL_NOTE.md). These results have been
checked computationally but have not yet been peer reviewed.

## What is not claimed

Exploratory computations suggest

$$
n_0(r)=2r+5 \qquad (r\ge 11),
$$

but this package does **not** claim that uniform statement. A finite scan is
not a proof, and those computations are not used in the $r=11$ argument.
General proofs of the remaining capacity/cascade statements are still being
investigated. In particular, this repository should currently be cited as a
preliminary exact result for $r=11$, not as a complete solution of Erdős
Problem #776.

## Quick verification

The code uses only the Python standard library and requires Python 3.10 or
newer.

```bash
python3 tests/verify_r11.py
```

Expected final line:

```text
ALL RELEASE CHECKS PASSED
```

Individual commands:

```bash
# Impossibility of the 24-level profile at (n,r)=(27,11)
python3 src/ep776_profile.py full 27 11

# Full-profile construction at n=28
python3 src/ep776_profile.py full 28 11 --emit

# Explicit padding checks through n=33
python3 src/ep776_padding.py 11 --stages 3

# Check the supplied witnesses for r=11,...,20
python3 src/ep776_check.py certificates/2r_plus_6_r_11_to_20.txt

# Regenerate the explicit 23-level r=11 certificate
python3 tools/generate_certificates.py
```

The checker in `src/ep776_check.py` is independent of the
Kruskal–Katona/colex arithmetic: it performs direct pairwise containment and
profile tests on the constructed sets.

## Repository layout

```text
README.md                    this file
docs/TECHNICAL_NOTE.md
src/                         core algorithms and independent checker
tests/verify_r11.py          one-command release verification
tools/generate_certificates.py
certificates/                explicit witness files
computations/                optional exhaustive small-n validator
```

## Attribution and transparency

The investigation and code were developed with extensive language-model
assistance. 

The profile-squashing theorem is classical and is attributed here to
Clements and to Daykin–Godfrey–Hilton. See the references in the technical
note. The application to the $r=11$ instance is the point being offered for
review.
