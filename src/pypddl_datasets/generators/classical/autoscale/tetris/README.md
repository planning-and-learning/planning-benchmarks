# tetris (autoscale)

Move tetromino-like pieces down a 4-column grid until the upper half is empty.

## Source

- **Domain:** Mauro Vallati, IPC 2014; `domain.pddl` is Autoscale's copy (the IPC file with reordered type declarations)
- **Generator:** re-export of `ipc/tetris` (port of pddl-generators `tetris/generator.py`)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-{agile,optimal}-strips/tetris`. Autoscale had no scaling generator for tetris and selected tasks from its own pool of upstream-generator runs (`tasks-of-domains-without-usable-generator/tetris` in the Autoscale repo, names `p-<type>-<rows>-<seed>`); none of the 60 tasks is an IPC task

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rows` | grid rows (even; 4 columns fixed) | 4–50 |
| `block_type` | 1 = only 1×1, 2 = only 2×1, 3 = only L, 4 = mix | type 1: 2 tasks, 2: 21, 3: 35, 4: 2 |

## Distribution

### Objects
Same as `ipc/tetris`: positions `f<row>-<col>f`, pieces of the drawn types, placeholder objects (`nothing`, `nada`, `nisba`) for absent piece types.

### Initial state
Same as `ipc/tetris` for the given `block_type`: the pieces of that type in the upper half (types 1–2 also on row num_rows/2, type 2 down to num_rows/2 + 1), `connected`, `clear` for free cells, `(= (total-cost) 0)`.

### Goal
`clear` for every cell of the upper half.

### Other
Action costs 1–3 per move and metric `minimize (total-cost)`, as in the Autoscale tasks. Problem name `tetris-<rows>-<block_type>-<n>`, as upstream.

## Comparison with reference tasks

All 60 tasks regenerated at their rows and block type (10 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| type 1: 1×1 pieces / clear cells (2 tasks) | 5.50 / 10.5 | 4.40 / 11.6 |
| type 2: 2×1 pieces / clear cells (21 tasks) | 7.33 / 50.5 | 8.18 / 48.8 |
| type 3: L-pieces / clear cells (35 tasks) | 4.80 / 107.9 | 7.00 / 101.3 |
| type 4: 1×1 / 2×1 / L pieces (2 tasks) | 4.50 / 5.50 / 4.00 | 3.65 / 3.95 / 4.50 |
| total-cost and metric | 60/60 | always |

**Deviations:**
- Type-3 tasks have fewer L-pieces than upstream draws (4.8 vs 7.0), presumably because Autoscale's pool lost upstream runs that hung or timed out on large piece counts.
