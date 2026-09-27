# snake (ipc)

A snake moves on a grid and must eat every apple; eaten apples respawn at predefined positions in a fixed order.

## Source

- **Domain:** Álvaro Torralba and Florian Pommerening, IPC 2018
- **Generator:** `snake/generate.py` by Álvaro Torralba and Florian Pommerening (with their June 2021 bugfix); Python port in `generator.py`, empty boards only
- **Reference tasks:** `data/classical/downward-benchmarks/snake-opt18-strips`, `snake-sat18-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width`, `height` | board size | 5×5 to 9×9 |
| `spawn_percentage` | spawning apples as a percentage of the free cells | 40, 55, 70, 85, 99/100 |
| `num_initial_apples` | apples on the board initially | 5 |
| `snake_size` | snake length − 1 | 1 |

## Distribution

### Objects
Positions `posX-Y` for every cell, plus the constant `dummypoint`.

### Initial state
- `isadjacent` holds for all 4-neighbours.
- The snake of `snake_size + 1` cells is placed at a random position with random orientation (`headsnake`, `tailsnake`, `nextsnake`).
- `num_initial_apples` apples go on uniformly random free cells (`ispoint`).
- The spawn apples form a `nextspawn` chain over random free cells, ending in `dummypoint`. There are ⌊pct · (cells − snake − initial apples)⌋ of them, with upstream's corrections for tiny boards and odd cell counts.

### Goal
`(not (ispoint p))` for every initial and every spawn apple position.

### Other
- No action costs.
- The problem is named `snake-empty-<W>x<H>-<size>-<initial>-<spawn>-<seed>`.
- On odd-cell boards, one fewer spawn apple is allowed (upstream's 2021 fix), so every empty-board task is solvable.

## Comparison with reference tasks

Fact counts per predicate, for all 40 IPC tasks regenerated at the parameters in their names:

| aspect | reference tasks | this generator |
|---|---|---|
| even-cell boards (25 tasks) | — | identical fact counts for all 25 |
| odd-cell boards 5×5, 7×7, 9×9 (15 tasks) | spawn apples N | N − 1 in all 15 (for example, 10 against 9 on 5×5 at 70%) |
| name suffix | `<seed><pct>`, for example `11170` | `<seed>` |

**Deviations:**
- On odd-cell boards, IPC has one more spawn apple, because the IPC 2018 tasks predate the 2021 fix. Those IPC tasks may have no Hamiltonian-path completion, so some could be unsolvable.
- The naming of the seed suffix differs.
