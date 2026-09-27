# drone (numeric/ipc)

A UAV flies on a 3D integer grid, visits every grid point and recharges its battery at the origin.

## Source

- **Domain:** Enrico Scala (IPC 2023 numeric track)
- **Generator:** reconstruction from the reference tasks (no generator was published); the tasks are fully determined by the grid size, and this generator reproduces all of them
- **Reference tasks:** `data/numeric/ipc2023/drone`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `size_x`, `size_y`, `size_z` | grid points per axis | 1–10, 1–10, 1–5 |

## Distribution

### Objects
One location `x<i>y<j>z<k>` per grid point, `0 <= i < size_x` and so on.

### Initial state
- Drone at the origin: `(= (x) 0) (= (y) 0) (= (z) 0)`.
- Bounds `min_* = 0`, `max_* = size_*` (the drone may leave the point grid by one step).
- `xl`, `yl`, `zl` of every location.
- `battery-level = battery-level-full = 2 * (size_x + size_y + size_z) + 1`.

### Goal
Every location visited, and the drone back at the origin (numeric goal conditions on `x`, `y`, `z`).

### Other
Deterministic, no metric. Problem name `name`, domain name `domain_name`, as in the reference tasks. Solvable: the battery covers a round trip to the farthest point plus the visit.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| tasks reproduced (whitespace and comments normalized) | 20 | 20 |

**Deviations:** none found.
