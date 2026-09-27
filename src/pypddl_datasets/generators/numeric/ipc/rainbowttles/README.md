# rainbowttles (numeric/ipc)

Sort coloured liquid segments so that every bottle holds one colour or nothing, then close all bottles.

## Source

- **Domain:** constant-free Rainbowttles by Alba Gragera (IPC 2026); `domain.pddl` is the IPC opt file (the sat file differs only in a comment line)
- **Generator:** reconstruction from the reference tasks; their `generate_rainbowttles_NO_constants.py` was not published; `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/rainbowttles-opt` (p11–p30), `data/numeric/ipc2026/rainbowttles-sat` (p31–p50)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_colours` | colours (red, green, blue, …, teal) | opt 3–6, sat 5–10 |
| `bottles_per_colour` | full bottles per colour in the solved state | 1 (≤7 colours), 2 (8–10 colours) |
| `num_spare` | empty bottles in the solved state | 2–4 |
| `capacity` | segments per bottle | 4 |
| `scramble_steps` | random reversed pours | opt 6–14, sat 13–41 |

## Distribution

### Objects
`bottle01..`, the colours and the extra colour object `empty` (wrapped eight per line, as the references).

### Initial state
Start from the solved state (shuffled bottles), then apply `scramble_steps` uniformly chosen reversed pours: split a top block onto a bottle without that colour, or move a bottle's only block entirely. Each colour stays one contiguous block per bottle. Facts: `real-colour`, `empty-colour empty`, capacities, per bottle `colour-segments` for every colour (and `empty`), `segments-filled`, `upper-colour` and the `colour-below` chain down to `empty`. No bottle starts closed.

### Goal
Every bottle `closed`.

### Other
No metric (as the references). Solvable by construction: the reversed scramble followed by closing every bottle is a plan.

## Comparison with reference tasks

All 40 reference tasks regenerated at their header parameters (5 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| mean segments per bottle | 2.83 | 2.83 |
| empty bottles | 8.0% | 9.1% |
| colour blocks per bottle (mean / max) | 1.98 / 4 | 1.92 / 4 |
| bottles already solved | 0.9% | 2.7% |

**Deviations:** the references' `profile` (optimal-prefix, hard-tail-*) is not reproduced; scrambles are uniform random walks.
