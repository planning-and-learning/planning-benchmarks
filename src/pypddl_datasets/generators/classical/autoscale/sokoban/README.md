# sokoban (autoscale)

Push stones onto goal cells.

## Source

- **Domain:** IPC 2008 sequential Sokoban; `domain.pddl` is Autoscale's copy, identical to `ipc/sokoban`'s
- **Generator:** re-export of `ipc/sokoban` (random levels scrambled from the goal by reverse pushes); use `grid="hex"` for the Hexoban tasks and `num_players` for multi-player levels
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-{agile,optimal}-strips/sokoban`, from Autoscale's pool (`tasks-of-domains-without-usable-generator/sokoban`): pddl-generators conversions of the Microban, Multiban and Hexoban level collections (by David W. Skinner and others) plus 12 IPC 2008 tasks

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width`, `height` | level bounding box | up to about 30 × 20 |
| `num_floor` | floor cells | from the level |
| `num_stones` | stones = goals | 2–16 |
| `grid` | `square` or `hex` | 49 square, 11 hex |
| `num_players` | players | 1–20 (22 of 60 tasks have several) |

## Distribution

### Objects
Players, stones, positions `pos-<x>-<y>` (hex: every second cell), four directions (hex: six).

### Initial state
As `ipc/sokoban`: a random connected floor region with walls, goal cells, stones scrambled from the goals by reverse pushes, `move-dir` for adjacent floor cells, and the player position.

### Goal
Every stone `at-goal`.

### Other
Metric `minimize (total-cost)` (pushes). Solvable by construction: reversing the pulls gives a plan.

## Comparison with reference tasks

The 49 square-grid tasks regenerated at their bounding box, floor size and stone count (5 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| goal cells | 6.18 | 6.18 |
| stones starting on a goal | 0.98 | 0.46 |
| `move-dir` facts | 155.0 | 191.4 |
| hexagonal levels (six directions) | 11 of 60 | with `grid="hex"` |
| multi-player levels | 22 of 60 | with `num_players` |
| multi-player: players / stones starting on a goal | 32 % / 42 % | 10 % / 50 % |

**Deviations:**
- Hexoban and multi-player levels are covered by `grid="hex"` and `num_players`; every player pulls during scrambling, so the tasks need several players, like the references. Players start on goal cells less often (10 % vs 32 % over the 22 multi-player tasks), since the references park them there by design.
- The reference levels are designed puzzles; generated levels have more `move-dir` facts (less wall-dense) and fewer stones starting on goals.
