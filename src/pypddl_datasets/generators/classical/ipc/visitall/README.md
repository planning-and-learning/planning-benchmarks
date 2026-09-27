# visitall (ipc)

A robot on a grid must visit a set of cells.

## Source

- **Domain:** Nir Lipovetzky, IPC 2011
- **Generator:** port of `pddl-generators/visitall/grid.c` (grid generator © 2001 Albert Ludwigs University Freiburg, goal-ratio flag by Nir Lipovetzky); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/visitall-{opt,sat}{11,14}-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width` | grid columns | 2–65 |
| `height` | grid rows (default `width`) | always equal to `width` |
| `goal_ratio` | probability that a cell is a goal | 1.0 or 0.5 (opt tracks' "half" tasks) |
| `num_unavailable` | removed cells | 0 |

## Distribution

### Objects
One `place` `loc-x<x>-y<y>` per available cell.

### Initial state
- `connected` in both directions between 4-neighbours.
- `num_unavailable` cells removed uniformly (never the centre cell).
- Robot `at-robot` a uniformly random available cell, which is `visited`.

### Goal
`visited` for each cell independently with probability `goal_ratio`, plus the start cell.

### Other
No costs or metric. Name `grid-<w>` (square) or `grid-<w>x<h>`. Solvable when the available cells are connected (always with `num_unavailable=0`).

## Comparison with reference tasks

All 80 IPC tasks.

| aspect | reference tasks | this generator |
|---|---|---|
| grid shape | square, 2×2 to 65×65 | square by default |
| removed cells | 0 | 0 by default |
| goal ratio | 1.0 (sat, opt "full"); 0.44–0.72 in opt "half" tasks | Bernoulli(`goal_ratio`) |
| robot start | centre cell `(w//2, h//2)` in 80/80 | uniform random cell |
| start cell in goal | 80/80 | always |
| problem name | `grid-<w>` | `grid-<w>` |

**Deviations:**
- Start cell: every IPC task starts the robot in the centre; `grid.c` (and this port) starts it at a uniform random cell. Autoscale 21.11 tasks do start randomly (0/30 at the centre).
