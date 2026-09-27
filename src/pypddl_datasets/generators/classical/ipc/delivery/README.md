# delivery (ipc)

One truck on a square grid delivers packages, one at a time, to a common goal cell. Not an IPC domain; it comes from the generalized-planning literature.

## Source

- **Domain:** `pddl-generators/delivery` (authors not named in the files); `tests/delivery` has an older version without the `(not (= ?from ?to))` move precondition
- **Generator:** port of `pddl-generators/delivery/generate.py` (Tarski-based); Python port in `generator.py`
- **Reference tasks:** `data/classical/tests/delivery` (one task, 2×2 grid, 1 package)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `grid_size` | side of the square grid | 2 |
| `num_packages` | packages | 1 |

## Distribution

### Objects
Cells `c_<x>_<y>`, packages `p1..`, truck `t1`.

### Initial state
- `adjacent` in both directions between 4-neighbours.
- Every package at a uniform cell; truck at a uniform cell, `empty`.

### Goal
All packages at one uniform goal cell; if all packages share a single start cell, the goal cell differs from it.

### Other
No costs or metric. Name `delivery-<n>x<n>-<p>`. Always solvable.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| structure of `tests/delivery/test-1` | 2×2 grid, 1 package, truck and package at distinct cells, one goal cell | same kind |

**Deviations:** none found (a single reference task).
