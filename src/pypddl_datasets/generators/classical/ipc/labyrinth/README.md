# labyrinth (ipc)

A robot walks through a board of cards with walls and pushes inner rows and columns until it can leave at the bottom-right corner.

## Source

- **Domain:** Rebecca Eifler, Daniel Fišer, IPC 2023 (dedicated to the public domain)
- **Generator:** `instance_generator/{generator,labyrinth,to_pddl}.py` from [ipc2023-classical/domain-labyrinth](https://github.com/ipc2023-classical/domain-labyrinth) (same authors, public domain); Python port in `generator.py`, with networkx replaced by a BFS
- **Reference tasks:** `data/classical/downward-benchmarks/labyrinth-opt23-adl`, `data/classical/downward-benchmarks/labyrinth-sat23-adl` (same domain file)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `size` | board side length | 3–8 |
| `num_rotations` | row/column pushes that disconnect the exit | 1–8 |
| `seed` | random seed (upstream's, Python `random`) | 1229–1373 |

## Distribution

### Objects
`pos0..pos<size-1>` (gridpos) and `card0..card<size²-1>`; card `x + y·size` starts at column `x`, row `y`.

### Initial state
- A random walk on the open board from the top-left to the bottom-right card; loops are cut out and immediate reversals are skipped. The walk is carved into an all-walls board, and the bottom-right card is open to the south.
- Every card then independently reopens each wall with probability 1/4, repeated until it has at most two walls.
- `num_rotations` pushes of an inner row or column (index 1..size-2, random direction) are applied. A push is kept only if the exit is then unreachable without pushing; a push directly undoing the previous one is skipped.
- Static `next`, `max-pos`, `min-pos`; `(robot-at card0)`, which stays top-left since outer rows and columns are never pushed; costs `move-robot-cost` 1 and `move-card` 1.

### Goal
`(left)`: the robot has left through the south side of the bottom-right card.

### Other
`(:metric minimize (total-cost))`. Name `labyrinth-size-<s>-rotations-<r>-seed-<seed>`, with upstream's header comment. Solvable by construction: undoing the pushes restores the carved walk. `size` must be at least 3.

## Comparison with reference tasks

Every IPC task regenerated at the size, rotations and seed in its name:

| aspect | reference tasks | this generator |
|---|---|---|
| tasks reproduced exactly (whitespace-normalized, lowercase) | 40 | 40 |
| domain file | IPC file | same (lowercased outside comments) |

**Deviations:** none found. Upstream loops forever if no disconnecting push exists; the port raises `ValueError` after 100 000 attempts instead, which never happens at IPC sizes.
