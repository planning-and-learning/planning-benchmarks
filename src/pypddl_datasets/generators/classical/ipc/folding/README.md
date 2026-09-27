# folding (ipc)

A string of nodes on a 2D grid is folded by 90° rotations at inner nodes into a target shape without self-intersection.

## Source

- **Domain:** Daniel Fišer (IPC 2023), a reformulation of the ASP Competition 2011 problem Reverse Folding by Agostino Dovier, Andrea Formisano and Enrico Pontelli; dedicated to the public domain
- **Generator:** `generate.py` from [ipc2023-classical/domain-folding](https://github.com/ipc2023-classical/domain-folding) (Daniel Fišer, public domain); Python port in `generator.py` with the same random draws in the same order
- **Reference tasks:** `data/classical/downward-benchmarks/folding-{opt,sat}23-adl` (identical domain files; every task records its `./generate.py seed scenario length folds` call)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `scenario` | `zigzag` (rotation direction uniform), `spiral` (always clockwise), `bias-spiral` (clockwise with probability 3/4) | all three |
| `num_nodes` | length of the string | 8–30 |
| `num_folds` | rotations, at most one per node | 7–25 (spiral: up to about half the length) |
| `seed` | random seed; the IPC seed reproduces the IPC task | 1229–1373 |

## Distribution

### Objects
Nodes `n1..nN`, coordinates `c1..c(2N-1)`; directions and rotations are domain constants.

### Initial state
- The string is a vertical line from `(cN, cN)` upwards: `at` per node, `heading ... up` for all but the last node, `free` for every other grid point.
- Static: the eight `next-direction` facts, the `coord-inc` chain, `connected` consecutive nodes, `end-node nN`.
- Costs: `(= (total-cost) 0)`, `(= (rotate-cost) 1)`, `(= (update-cost) 0)`.

### Goal
The `at` position of every node after applying `num_folds` rotations at distinct random nodes (shuffled order, direction per scenario), plus `(not (rotating))`. Rotation sequences that intersect the string are redrawn (up to 10,000 times).

### Other
`(:metric minimize (total-cost))`, i.e. the number of rotations. The problem name `folding-<scenario>-<N>-<folds>-<rand>` includes upstream's extra random number. Solvable by construction; upstream records the rotation sequence as a plan (not reproduced).

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| tasks reproduced from their generator call | 40 | 40 identical (objects, init, goal and problem name) |

**Deviations:** none found. Parameter combinations upstream cannot satisfy (e.g. `spiral` with too many folds) raise `ValueError` instead of exiting.
