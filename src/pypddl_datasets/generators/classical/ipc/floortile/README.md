# floortile (ipc)

Robots with white and black paint move on a grid of tiles and paint them in a checkerboard pattern; painted tiles can no longer be stepped on.

## Source

- **Domain:** Tomas de la Rosa, IPC 2011 (also IPC 2014)
- **Generator:** `floortile/floortile-generator.py` (Tomas de la Rosa, MIT license), `seq` mode; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/floortile-opt11-strips`, `data/classical/downward-benchmarks/floortile-sat11-strips`, `data/classical/downward-benchmarks/floortile-opt14-strips`, `data/classical/downward-benchmarks/floortile-sat14-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rows` | rows to paint; the grid has one extra row 0 | 3-7 |
| `num_columns` | columns | 3-7 |
| `num_robots` | robots (<= `num_columns`) | 2-4 |
| `name` | problem name | IPC: `prob001`, `p01-432`, ... |

## Distribution

### Objects
Tiles `tile_{row}-{col}` for rows 0..`num_rows` and columns 1..`num_columns`, robots `robot1..`, and colors `white` and `black`.

### Initial state
- Each robot starts in a uniformly random row (0..`num_rows`) and in a column that no other robot starts in.
- Robots alternate their colors: odd-numbered robots have white, even-numbered black.
- Both colors are `available-color`.
- Every tile not under a robot is `clear`.
- `up`, `down`, `left` and `right` define the grid.

### Goal
Every tile in rows 1..`num_rows` is `painted` in checkerboard colors: white where `row + col` is even.

### Other
- Action costs, with `(= (total-cost) 0)` and `(:metric minimize (total-cost))`.
- Problem name `floortile-r{rows}-c{cols}-rob{robots}`, or `name`.
- No solvability check is done; upstream does none either. Painting order matters, since painted tiles block movement, so plans can reach dead ends.

## Comparison with reference tasks

80 IPC tasks, each generated at its own rows, columns and robots (20 seeds per task):

| aspect | reference tasks | this generator |
|---|---|---|
| robots in distinct columns | 80 of 80 tasks | always |
| alternating robot colors | 80 of 80 | always |
| checkerboard goal over all rows | 80 of 80 | always |
| robot start in row 0 | 35 of 181 (19.3%) | 22.6 of 181 (12.5%) |
| robot start in the last row | 24 of 181 (13.3%) | 30.6 of 181 (16.9%) |
| mean relative start row | 0.47 | 0.52 |
| metric | 80 | always |

**Deviations:**
- Problem names differ.
- Row 0 is somewhat more common in IPC starts, 2.8 sd above our uniform row draw. The per-grid histograms show no systematic pattern, so this is likely noise.
- The domain file differs from IPC only in declaring `(total-cost) - number`.
