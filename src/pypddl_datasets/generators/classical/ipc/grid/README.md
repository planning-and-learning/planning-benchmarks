# grid (ipc)

A robot moves on a grid with locked cells that open with keys of matching shape, carrying one key at a time to its goal cell.

## Source

- **Domain:** Drew McDermott, AIPS-1998 competition
- **Generator:** `grid/generate.py` from pddl-generators, the Python successor of `grid/grid.c` ((C) 2001 Albert Ludwigs University Freiburg); Python port in `generator.py`, with `style="ipc"` (default) following the IPC tasks and `style="autoscale"` reproducing upstream
- **Reference tasks:** `data/classical/downward-benchmarks/grid`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width`, `height` | grid size | 5x5–9x9 |
| `num_shapes` | key/lock shapes (default 4) | 4 |
| `num_keys` | keys, at least `num_shapes` (default `max(width, height) + 4`) | 9–13 (size + 4) |
| `num_locks` | locked cells (default `width * height // 4`) | 8–20 |
| `goal_probability` | probability that a key gets a goal (default 0.35) | 19 of 55 keys |
| `style` | `"ipc"` or `"autoscale"` | |

## Distribution

### Objects
Cells `node{x}-{y}`, shapes `triangle`, `diamond`, `square`, `circle` (then `shape{k}`), keys `key{k}`; untyped.

### Initial state
- The locked cells form one 4-connected region, grown from a uniformly random cell by adding uniformly random neighbouring cells. All locks share one uniformly random shape.
- Keys get shapes one per shape first, then uniformly at random.
- The robot starts on a uniformly random open cell with an empty arm.
- One key of the lock shape is placed in the region reachable from the robot; all other keys go on uniformly random cells, locked ones included.

### Goal
- Each key gets a goal with `goal_probability`, on a uniformly random cell (possibly its start). At least one key always gets a goal.
- The robot has no goal.

### Other
- No action costs.
- Problem name `grid-{w}-{h}-{shapes}-{keys}-{locks}`.
- Solvable by construction.
- `style="autoscale"`: upstream `generate.py`: locks on uniformly random cells, the first `num_shapes` locks one shape each, goals never at the key's start, `pos{x}-{y}`/`shape{k}` names, defaults 2 shapes, 2 keys, 2 locks, goal probability 1.0.

## Comparison with reference tasks

5 IPC tasks, each generated at its own size, keys and locks with the default shapes and goal probability (40 seeds per task):

| aspect | reference tasks | this generator | before (`style="autoscale"`) |
|---|---|---|---|
| lock shapes per task | 1 | 1 | 3.97 |
| locked regions per task | 1.2 | 1 | scattered cells |
| key shapes present | 4 | 4 | 4 |
| keys on locked cells | 0.30 | 0.22 | 0.18 |
| keys with a goal | 0.33 | 0.34 | 1.0 (old default) |
| goal key already at its goal | 1 of 19 | 11 of 752 | 0 |
| names | `node{x}-{y}`, `triangle`/… | same | `pos{x}-{y}`, `shape{k}` |

**Deviations:**
- The 9x9 IPC task has two locked regions; the generator always grows one.
- Slightly fewer keys on locked cells (0.22 vs 0.30, only 5 IPC tasks).
