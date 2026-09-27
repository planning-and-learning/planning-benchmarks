# termes (autoscale)

A single TERMES robot builds block towers of given heights on a grid by carrying blocks from a depot and climbing on them.

## Source

- **Domain:** Sven Koenig and Satish Kumar, IPC 2018
- **Generator:** `termes/generate-autoscale.py` by Álvaro Torralba and Florian Pommerening, called with `--ensure_plan --dont_remove_slack`; re-exports `ipc/termes` (same distribution, Autoscale's domain file). The z3 plan check is replaced by an exact pure-Python scaffold check.
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/termes` (also `21.11-optimal-strips/termes`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `size_x`, `size_y` | board size | 6×6 to 10×10 |
| `min_height` | lowest height of the non-first towers | 1–3 (observed minimum tower height) |
| `max_height` | height of the first tower | 2–6 |
| `num_towers` | towers | 1–34 |

## Distribution

### Objects
Numbers `n0..n<max_height>` and positions `pos-X-Y`.

### Initial state
Empty board, with the robot at the border depot. See `ipc/termes`.

### Goal
- `num_towers` distinct uniform cells. The first has `max_height`, the others uniform heights in `min_height..max_height`.
- All other cells at 0.
- Resampled until a scaffold exists; the grid grows after 20 failures.

### Other
- No action costs.
- The problem is named `termes-<cells*height>-<X>x<Y>x<H>`, as in the agile tasks.
- Always solvable.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| name format | `termes-0098-7x7x2` | identical format |
| minimum tower heights | 1 (16 tasks), 3 (14 tasks) | set by `min_height` |
| board, numbers, depot row, zero goals | — | same construction as the ported upstream |

**Deviations:** none found in structure. Per-task parameters can only be read partially from the agile tasks, so the height distribution was not compared numerically.
