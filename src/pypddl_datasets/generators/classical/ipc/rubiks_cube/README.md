# rubiks_cube (ipc)

Solve a 3×3×3 Rubik's Cube scrambled by random quarter turns; moves are conditional effects on corner and edge pieces.

## Source

- **Domain:** Bharath Muppasani, Biplav Srivastava, Clemens Büchner, Patrick Ferber, IPC 2023 (dedicated to the public domain)
- **Generator:** `generator.py` from [ipc2023-classical/domain-rubiks-cube](https://github.com/ipc2023-classical/domain-rubiks-cube) (same authors, public domain); Python port in `generator.py`. Upstream's optimal solver (Michael Reid) only writes reference plans and is not ported
- **Reference tasks:** `data/classical/downward-benchmarks/rubiks-cube-opt23-adl`, `data/classical/downward-benchmarks/rubiks-cube-sat23-adl` (same domain file, same 20 tasks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_moves` | random quarter turns applied to the solved cube | 1–20 |
| `seed` | random seed (upstream's, Python `random`) | 1087, 1129, 2999, 4007 |

## Distribution

### Objects
The six colours `yellow white blue green orange red`.

### Initial state
The solved cube scrambled by `num_moves` quarter turns drawn uniformly from the 12 moves (upstream without `--double-actions`, as in all IPC tasks). A move is redrawn while it turns the same face as the last move, or the face two moves back when the last move turned the opposite face; then again while it shares the last move's face. The state is written as 8 corner facts `(cube<i> c1 c2 c3)` and 12 edge facts `(edge<ij> c1 c2)`.

### Goal
The solved cube: all 20 piece facts in their solved colours.

### Other
No action costs. Name `rubiks-cube-shuffle-<num_moves>`. Solvable by construction (reverse the scramble).

## Comparison with reference tasks

Every IPC task regenerated at the seed and move count in its header comment:

| aspect | reference tasks | this generator |
|---|---|---|
| tasks reproduced exactly (whitespace-normalized, lowercase, comments dropped) | 40 | 40 |
| domain file | IPC file | same (lowercased outside comments) |

**Deviations:** none found. Upstream's `--double-actions` mode (U2, F2, …) is not ported, since no IPC task uses it.
