# sokoban (ipc_learning)

A robot pushes boxes to their goal cells.

## Source

- **Domain:** IPC 2023 learning-track encoding (typed, direction constants, one goal cell per box)
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/—`), learning-track domain file; no morning generator existed; `ipc/sokoban` levels with `style="learning"` (reverse-pull scramble with tracked box identities)
- **Reference tasks:** `data/classical/ipc2023-learning/sokoban_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `sokoban/sokoban.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width`, `height` | level bounding box | grid 8–99 |
| `num_floor` | floor cells | — |
| `num_stones` | boxes | 1–79 |

## Distribution

### Objects
Every cell `loc_<row>_<col>`, boxes `box1..`.

### Initial state
`at-robot`, `at` for boxes, `clear` for free floor (robot cell included), `adjacent` with directions between floor cells.

### Goal
Each box at its own goal cell (the cell it was pulled from).

### Other
No action costs. Solvable by construction (reverse pulls; tested by BFS).

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| structural support (predicates, goals) | — | covered |

**Deviations:**
- Levels are grown floor regions scrambled by reverse pulls; the learning generator walks boxes forward on an N×N grid. Different level shapes, same encoding. The learning generator has no license, so it is not ported.
