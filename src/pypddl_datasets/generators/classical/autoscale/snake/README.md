# snake (autoscale)

A snake moves on a grid and must eat every apple; eaten apples respawn at predefined positions in a fixed order.

## Source

- **Domain:** Álvaro Torralba and Florian Pommerening, IPC 2018
- **Generator:** `snake/generate.py` by Álvaro Torralba and Florian Pommerening (June 2021 bugfix), called as `generate.py empty-<x>x<y> 1 5 <pct>% {seed} pddl`; re-exports `ipc/snake` (same distribution, Autoscale's domain file)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/snake` (also `21.11-optimal-strips/snake`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width`, `height` | board size | 5×5 to 13×14 |
| `spawn_percentage` | spawning apples as a percentage of the free cells | 40, 55, 70, 85, 100 |
| `num_initial_apples` | initial apples (lowered to the spawn count on tiny boards) | 5 |
| `snake_size` | snake length − 1 | 1 |

## Distribution

### Objects
Grid positions `posX-Y` and `dummypoint`.

### Initial state
- Random snake placement.
- Initial apples on uniform free cells.
- A spawn chain over uniform free cells, one shorter on odd-cell boards. See `ipc/snake`.

### Goal
No apple left: `(not (ispoint p))` for every apple position.

### Other
- No action costs.
- The problem is named `snake-empty-<W>x<H>-<size>-<initial>-<spawn>-<seed>`, as in the agile tasks.
- Empty boards are always solvable.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| fact counts per predicate (30 agile tasks) | — | identical in 30/30, including odd-cell boards |

**Deviations:** none found.
