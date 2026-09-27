# ricochet_robots (ipc)

Robots slide on a walled board until they hit a barrier or another robot; one robot must reach a target cell.

## Source

- **Domain:** Daniel Fišer (IPC 2023), based on the board game Ricochet Robots and the ASP Competition 2015 problem
- **Generator:** `generate.py` + `asp-to-pddl.py` from [ipc2023-classical/domain-ricochet-robots](https://github.com/ipc2023-classical/domain-ricochet-robots) (Daniel Fišer); Python port in `generator.py`. Upstream's Rust solver filter (`solve-pddl.py`, 600 s limit) is replaced by an exact breadth-first search over robot configurations, bounded by `max_states`
- **Reference tasks:** `data/classical/downward-benchmarks/ricochet-robots-{opt,sat}23-adl` (identical domain files): 27 tasks translated from ASP Competition 2015 instances, 13 from `generate.py`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `board_size` | board side N | 10–22 (`generate.py` tasks), 16 (ASP tasks) |
| `num_barriers` | inner walls; default uniform in 5..5 + N²/3 as upstream | 7–119 (`generate.py` tasks), 50 (ASP tasks) |
| `board` | `random` (`generate.py`) or `asp2015` (the fixed ASP competition board, robots in the corners) | both |
| `max_states` | search bound of the solvability check | — |

## Distribution

### Objects
Cells `cell-x-y`, robots `robot-1..robot-4` (red, blue, green, yellow), directions `west east north south`.

### Initial state
- `next` for all neighbouring cells; `blocked` on the border and on both sides of every barrier.
- `random`: barriers at uniform cells and directions (no duplicates, never both sides listed twice); robots at distinct uniform cells. `asp2015`: the 50 barriers of the ASP competition board, robots at `(1,1)`, `(1,16)`, `(16,1)`, `(16,16)`.
- `free` for every cell without a robot, `(nothing-is-moving)`, costs `go-cost 1`, `step-cost 0`, `stop-cost 0`.

### Goal
One uniform robot at a uniform cell, plus `(nothing-is-moving)`.

### Other
`(:metric minimize (total-cost))`, i.e. the number of `go` actions. Only tasks that need at least one move and are provably solvable within `max_states` configurations are kept; others are redrawn, like upstream keeps only tasks its solver finishes. The problem name `ricochet-robots-NxN-<optimal moves>-<rand>` records the optimal move count (upstream: `None` for `generate.py` tasks).

## Comparison with reference tasks

Random boards at N = 10–16 (20 tasks) vs the 13 IPC `generate.py` tasks and the 27 ASP tasks:

| aspect | IPC ASP tasks | IPC `generate.py` tasks | this generator |
|---|---|---|---|
| inner barriers per cell | 0.195 | 0.176 | 0.187 (`random`), 0.195 (`asp2015`) |
| cells with two perpendicular walls, per cell | 0.082 | 0.032 | 0.038 (`random`) |
| target cell next to a wall | 0.04 | 0.38 | 0.30 |
| optimal moves | 13–25 | 6–13 (8 of 13 solved by our search) | 6.6–7.4 mean, max 11 (`random`); 9.1 mean, max 15 (`asp2015`) |
| `blocked`/`next` facts of the ASP board | — | — | identical (`asp2015`) |
| init predicates | `next blocked free at nothing-is-moving` | same | same |

**Deviations:**
- The IPC selection favours hard tasks (ASP instances with 13–25 moves); our draws are uniform over solvable tasks, so they are shorter on average.
- Boards whose solvability needs more than `max_states` configurations are rejected (5 of the 13 IPC `generate.py` tasks exceed 3M states); upstream's solver kept those it finished in 600 s.
