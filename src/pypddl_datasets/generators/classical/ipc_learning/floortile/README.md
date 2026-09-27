# floortile (ipc_learning)

Robots paint a grid of tiles in a checkerboard pattern.

## Source

- **Domain:** Tomás de la Rosa (IPC 2011); learning-track encoding without action costs
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/floortile`), learning-track domain file; `(:domain floortile)` instead of `floor-tile`, no `total-cost` and metric
- **Reference tasks:** `data/classical/ipc2023-learning/floortile_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `floortile/floortile.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rows` | rows | 3–34 |
| `num_columns` | columns | 3–28 |
| `num_robots` | robots | 1–28 |

## Distribution

### Objects
Tiles `tile_r-c` (plus an unpaintable bottom row), robots, colours white/black.

### Initial state
Grid adjacency, robots on distinct bottom tiles with a random colour, all other tiles clear.

### Goal
Every paintable tile painted in the checkerboard pattern.

### Other
No action costs.

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| goal painted per tile | 1.000 | 1.000 |
| colours | 2 | 2 |

**Deviations:**
- None found.
