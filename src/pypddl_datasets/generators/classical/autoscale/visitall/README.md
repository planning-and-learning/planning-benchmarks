# visitall (autoscale)

A robot on a grid must visit a set of cells.

## Source

- **Domain:** Nir Lipovetzky, IPC 2011
- **Generator:** `pddl-generators/visitall/grid.c` as called by Autoscale: `grid -x <x> -y <y> -r <r> -u 0 -s <seed>`; same distribution as `ipc/visitall`, which this package re-exports with Autoscale's `domain.pddl`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/visitall` (also `21.11-optimal-strips/visitall`)

## Parameters

| parameter | meaning | reference range (`domains.py`; agile tasks) |
|---|---|---|
| `width`, `height` | grid size | grid 3–8 + slope; square 7×7–94×94 |
| `goal_ratio` | goal probability per cell (`-r`) | 0.5, 0.75, 1; 0.72–0.80 (≈ 0.75) |
| `num_unavailable` | removed cells (`-u`) | 0 |

## Distribution

### Objects
See `ipc/visitall`.

### Initial state
See `ipc/visitall`: 4-neighbour `connected`; robot at a uniform random cell, which is `visited`.

### Goal
See `ipc/visitall`: each cell with probability `goal_ratio`, plus the start cell.

### Other
See `ipc/visitall`. No costs.

## Comparison with reference tasks

All 30 agile tasks.

| aspect | reference tasks | this generator |
|---|---|---|
| grid shape | square | square |
| robot start at centre | 0 / 30 (random) | random |
| goal ratio | 0.75 mean | `goal_ratio` |

**Deviations:** none found.
