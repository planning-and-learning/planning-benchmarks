# grid (autoscale)

A robot moves on a grid with locked cells that open with keys of matching shape, carrying one key at a time to its goal cell.

## Source

- **Domain:** Drew McDermott, AIPS-1998 competition (same domain file as the IPC)
- **Generator:** `grid/generate.py` from Autoscale's pddl-generators, called as `generate.py {x} {y} --shapes .. --keys .. --locks .. --prob-goal .. --seed ..`; `generator.py` calls `../../ipc/grid` with `style="autoscale"`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/grid`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/grid`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width`, `height` | grid size (Autoscale: grid attribute, x 3-10) | agile: 7x7-140x140 |
| `num_shapes` | key/lock shapes | agile: 2-7 |
| `num_keys` | keys (Autoscale: `shapes + extra_keys`) | agile: 3-8 |
| `num_locks` | locked cells (Autoscale: `x * y * percentage_cells_locked`, at least `shapes`) | agile: 24-9800 (about 50% of cells) |
| `goal_probability` | probability that a key gets a goal (Autoscale enum 0.5, 0.75, 1) | agile: 0.2-1.0 per task (measured goal fraction) |

## Distribution

### Objects
Cells `pos{x}-{y}`, `shape{k}` and `key{k}` (`ipc/grid`'s IPC style uses `node{x}-{y}` and named shapes).

### Initial state
Upstream `generate.py` (not the IPC style of `ipc/grid`):
- `num_locks` uniformly random cells are locked.
- The first `num_shapes` locks and keys get one shape each; the rest are random.
- The robot starts on a random open cell.
- Keys are placed by the reachability walk, so every lock can be opened.

### Goal
- Each key gets a goal with `goal_probability`, on a random cell other than its start. At least one key always gets a goal.

### Other
- No action costs.
- Problem name `grid-{x}-{y}-{shapes}-{keys}-{locks}`, the same scheme as Autoscale.
- Solvable by construction.

## Comparison with reference tasks

30 agile tasks, each generated at its own size, shapes, keys, locks and goal fraction:

| aspect | reference tasks | this generator |
|---|---|---|
| objects | 208551 | 208551 |
| init `place` / `conn` / `locked` / `open` / `lock-shape` | 208251 / 824216 / 104118 / 104133 / 104118 | identical |
| init `key` / `shape` / `at` | 165 / 135 / 165 | identical |
| every shape used by some lock | 30 of 30 | always |
| goal `at` | 88 | 90 |
| keys on locked cells (15 smallest tasks) | 20 of 60 | 17.8 (20 seeds) |

**Deviations:**
- None found.
