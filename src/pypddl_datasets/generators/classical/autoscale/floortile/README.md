# floortile (autoscale)

Robots with white and black paint move on a grid of tiles and paint them in a checkerboard pattern; painted tiles can no longer be stepped on.

## Source

- **Domain:** Tomas de la Rosa, IPC 2011 (the same domain as the IPC, up to the `(total-cost) - number` declaration)
- **Generator:** `floortile/floortile-generator.py` (Tomas de la Rosa, MIT license), called by Autoscale as `floortile-generator.py name {rows} {columns} {robots} seq {seed}`; `generator.py` re-exports `../../ipc/floortile`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/floortile`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/floortile`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rows` | rows to paint, plus row 0 (Autoscale: grid attribute) | agile: 2-42 |
| `num_columns` | columns | agile: 2-40 |
| `num_robots` | robots (Autoscale enum 2-5, capped at `num_columns`) | agile: 2, 4 |

## Distribution

### Objects
The same as `ipc/floortile`: tiles `tile_{row}-{col}` including row 0, `robot*`, `white`, `black`.

### Initial state
The same as `ipc/floortile`:
- Robots start in random rows and distinct random columns, with alternating white and black colors.
- Every tile not under a robot is clear, and the grid adjacency is complete.

### Goal
A checkerboard painting of rows 1..`num_rows`.

### Other
- Action costs with a `total-cost` metric.
- Autoscale names every problem `name`; this generator names them `floortile-r..-c..-rob..` unless `name` is passed.
- No solvability check is done.

## Comparison with reference tasks

30 agile tasks, each generated at its own rows, columns and robots (1 seed):

| aspect | reference tasks | this generator |
|---|---|---|
| tiles / robots / colors | 18766 / 116 / 60 | identical |
| init `clear` / `up` / `down` / `left` / `right` | 18650 / 18146 / 18146 / 18047 / 18047 | identical |
| init `robot-at` / `robot-has` / `available-color` | 116 / 116 / 60 | identical |
| goal `painted` | 18146 | 18146 |
| metric | 30 | 30 |

**Deviations:**
- Problem names differ; Autoscale uses the literal `name`.
- Otherwise none found. Robot start rows are uniform, see `ipc/floortile`.
