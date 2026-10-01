# sokoban (ipc_learning)

A robot pushes boxes to their goal cells.

## Source

- **Domain:** IPC 2023 learning-track encoding (typed, direction constants, one goal cell per box)
- **Generator:** callable adaptation of [`sokoban/sokoban.py` at revision `19d6a8ad4b354328154a2cc1f1a95f7c09fa9db6`](https://github.com/ipc2023-learning/benchmarks/blob/19d6a8ad4b354328154a2cc1f1a95f7c09fa9db6/sokoban/sokoban.py), restored from `learning-module-programs-verdog/ipc2023/sokoban/generator.py`. Sampling uses a local seeded random generator and preserves the upstream draw order. The BFS queue guard is corrected so unreachable destinations fail instead of hanging.
- **Reference tasks:** `data/classical/ipc2023-learning/sokoban_ipc2023_learning` (easy/medium/hard, 90 tasks).

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `grid_size` | square grid side including the border walls; at least 5 | 8–99 |
| `boxes` | box count; between 1 and `(grid_size - 4) ** 2` | 1–79 |
| `seed` | integer random seed; default 42 | — |

Call `make_problem(grid_size, boxes, seed=42)` or write a task to stdout with:

```sh
python -m pypddl_datasets.generators.classical.ipc_learning.sokoban.generator -g 8 -b 2 -s 60
```

The long flags are `--grid-size`, `--boxes`, and `--seed`.
Valid parameter bounds do not guarantee a successful sample: paths reserve
additional cells. Invalid parameters and sampling failures raise `ValueError`;
failed samples are never silently retried.

## Distribution

### Objects
Every cell `loc_<row>_<col>`, boxes `box1..`.

### Initial state
`at-robot`, `at` for boxes, `clear` for free floor (robot cell included), `adjacent` with directions between floor cells.

### Goal
Each box at its own goal cell, reached by its sampled forward push sequence.

### Other
Boxes start in the inner `(grid_size - 4)` square. For each box, the generator
walks the robot into position and pushes along up to three straight segments,
turning 90 degrees between segments when possible. Completed goal cells are
reserved while subsequent paths are built. Border walls surround the grid;
additional walls occupy a sampled 30–80% of the remaining unvisited interior
cells (at least one), preserving the constructed solution paths. There are no
action costs.

## Comparison with reference tasks

This uses the learning track's forward-walk sampling procedure, rather than the
reverse-pull floor-region generator in `ipc/sokoban`. Both can emit the learning
encoding, but their task distributions differ. The callable adaptation reports
failed samples as `ValueError` and does not retry them.
