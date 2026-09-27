# tetris (ipc)

Move tetromino-like pieces down a 4-column grid until the upper half is empty.

## Source

- **Domain:** Mauro Vallati, IPC 2014
- **Generator:** pddl-generators `tetris/generator.py` (Mauro Vallati) with all four block types; the IPC tasks use type 4 (mix), the Autoscale 21.11 tasks types 1–4; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/tetris-opt14-strips`, `data/classical/downward-benchmarks/tetris-sat14-strips` (same domain file)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rows` | grid rows (even; 4 columns fixed) | 4–14 (opt: 4–10, sat: 10–14) |
| `block_type` | 1 = only 1×1, 2 = only 2×1, 3 = only L, 4 = mix | IPC: 4 |

## Distribution

### Objects
`num_rows × 4` positions `f<row>-<col>f`; pieces `rightl<i>` (L-shape), `straight<i>` (2×1), `square<i>` (1×1). A piece type without pieces gets a placeholder object (`nisba`, `nada`, `nothing`), as upstream and IPC.

### Initial state
- `connected`: 4-neighbourhood of the grid, both directions.

Block type 4 (IPC):
- L-pieces: count uniform in 1..(num_rows // 4) × 2; each on a uniform free anchor (row < num_rows/2, column < 3) covering the anchor, the cell below and the cell below-right.
- 2×1 pieces: every free vertical pair in rows 0..num_rows/2 − 1, columns 0–2, gets one with probability 1/2 (scanning top-down, left-right).
- 1×1 pieces: every remaining free cell in rows 0..num_rows/2 − 1, columns 0–2, gets one with probability 1/2.

Block types 1–3 place only one piece type:
- 1: 1..(num_rows / 2) × 4 1×1 pieces on uniform free cells of rows 0..num_rows/2 (upstream's inclusive bound, so the middle row too), any column.
- 2: 1..num_rows 2×1 pieces; each at a uniform free cell of rows 0..num_rows/2 with upstream's direction draw (up, right, down, left; up in row 0 falls through to right, right in the last column to left), so pieces may be horizontal and reach row num_rows/2 + 1.
- 3: the L-pieces of type 4 only.

- `clear` for every free cell; `(= (total-cost) 0)`.

### Goal
`clear` for every cell in rows 0..num_rows/2 − 1 (the upper half).

### Other
Action costs 1–3 per move; metric `minimize (total-cost)`. Problem name `tetris-<rows>-<block_type>-<random number>` as upstream. Upstream loops forever when no free anchor remains for the next L-piece (types 3–4) or no free pair for the next 2×1 piece (type 2); this port redraws the whole task instead (the same distribution conditioned on termination). Solvability is not guaranteed, as upstream.

## Comparison with reference tasks

Mean pieces per task (square / straight / L) for the 37 IPC tasks and 2000 generated tasks per grid size.

| aspect | reference tasks | this generator |
|---|---|---|
| 4 rows (2 tasks) | 2.50 / 0.50 / 1.00 | 1.13 / 0.56 / 1.50 |
| 6 rows (5 tasks) | 2.80 / 1.40 / 1.20 | 1.80 / 1.15 / 1.50 |
| 8 rows (5 tasks) | 2.60 / 0.60 / 3.00 | 2.04 / 1.35 / 2.43 |
| 10 rows (6 tasks) | 2.50 / 2.00 / 2.33 | 2.64 / 2.07 / 2.49 |
| 12 rows (9 tasks) | 4.22 / 2.22 / 3.00 | 3.02 / 2.31 / 3.24 |
| 14 rows (10 tasks) | 3.30 / 2.10 / 4.40 | 3.52 / 3.03 / 3.41 |
| columns used by 1×1 and 2×1 pieces | 0–2 | 0–2 |
| all 2×1 pieces vertical | yes | yes |
| total-cost and metric present | 37/37 | always |
| Autoscale type 2, mean 2×1 pieces (21 tasks) | 7.33 | 8.18 |
| Autoscale type 3, mean L-pieces (35 tasks) | 4.80 | 7.00 |

**Deviations:**
- On small grids the IPC tasks have more 1×1 pieces (2.5 vs 1.1 at 4 rows); with 2–5 tasks per size this is within what a selection of upstream samples produces, and the running upstream generator gives the same means as this port.
- Upstream's own output lacks `total-cost`; the port follows the IPC tasks (the Autoscale tasks have it too).
- Autoscale's type-3 tasks have fewer L-pieces than upstream draws (4.8 vs 7.0), presumably because Autoscale discarded upstream runs that hung or timed out on large piece counts.
