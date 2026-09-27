# termes (ipc)

A single TERMES robot builds block towers of given heights on a grid by carrying blocks from a depot and climbing on them.

## Source

- **Domain:** Sven Koenig and Satish Kumar, IPC 2018 (single-robot version)
- **Generator:** `termes/generate-autoscale.py` and `gen_random_tower_boards.py` by Álvaro Torralba and Florian Pommerening, random-tower boards with `--ensure_plan --dont_remove_slack`; Python port in `generator.py`. Upstream's z3 plan check is replaced by an exact pure-Python scaffold check.
- **Reference tasks:** `data/classical/downward-benchmarks/termes-opt18-strips`, `termes-sat18-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `size_x`, `size_y` | board size | 4×3, 4×4 (random towers) |
| `min_height` | lowest height of the non-first towers | 2 (IPC `gen_board`) |
| `max_height` | height of the first tower, and the upper bound for the others | 3–9 |
| `num_towers` | towers | 1–6 |

## Distribution

### Objects
Numbers `n0..n<max_height>` and positions `pos-X-Y`.

### Initial state
- All heights are 0 and the robot stands at the depot.
- The depot is on the border row y=0, placed as upstream does.
- Grid `neighbor` relations and the `succ` chain on numbers.

### Goal
- `num_towers` distinct uniform cells. The first gets `max_height`, the others uniform heights in `min_height..max_height`.
- All other cells must end at height 0.
- Boards are resampled until a scaffold exists. After 20 failures the grid grows.

### Other
- No action costs.
- The problem is named `termes-<cells*height>-<X>x<Y>x<H>`.
- Every generated task is solvable, by the scaffold check.

## Comparison with reference tasks

The 30 IPC random-tower tasks, regenerated with `min_height=2` and the size, height, tower count and seed from their names:

| aspect | reference tasks | this generator |
|---|---|---|
| board size, number objects, tower count, max height | — | equal in 30/30 |
| depot on border row, init all 0, zero-height goals listed | — | equal in 30/30 |
| mean tower height | 3.71 | 3.68 |
| depot positions (most common) | (2,0) on 4×3: 13×; (1,0): 5× | (2,0) on 4×3: 14×; (1,0): 5× |
| structured boards (`wall` ×5, `empire` ×5 in sat18) | from fixed board files | not generated |

**Deviations:**
- The 10 sat18 tasks with `wall`/`empire` boards come from hand-made board files and are not produced.
- `min_height` must be set to 2 to match IPC. Autoscale uses values from 1.
- Naming drops IPC's plan-cost prefix and board label.
