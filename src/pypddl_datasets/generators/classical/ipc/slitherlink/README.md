# slitherlink (ipc)

Draw a single closed loop along grid edges so that every numbered cell has exactly that many loop edges around it.

## Source

- **Domain:** IPC 2023; the repository names no author (its `generate-pddl.py` is public domain apart from a GPLv3 download helper, which is not ported)
- **Generator:** `generator-solver/generate.hs` (puzzle generator from [ctbo/slitherlink](https://github.com/ctbo/slitherlink) by Harald Bögeholz, BSD-2-Clause) and `generate-pddl.py gen rows cols` from [ipc2023-classical/domain-slitherlink](https://github.com/ipc2023-classical/domain-slitherlink); Python port in `generator.py` with a pure-Python uniqueness solver instead of the Haskell one
- **Reference tasks:** `data/classical/downward-benchmarks/slitherlink-opt23-adl`, `data/classical/downward-benchmarks/slitherlink-sat23-adl` (identical domain files)

## Parameters

| parameter | meaning | reference range (IPC task headers) |
|---|---|---|
| `rows`, `cols` | grid size | 3×4 to 10×11 (37 grid tasks) |

## Distribution

### Objects
`cap-0..cap-4`, nodes `n-<r>-<c>` of the (rows+1)×(cols+1) grid, cells `cell-<r>-<c>` plus the outside cells `cell-outside-<r>-{left,right}` and `cell-outside-<c>-{up,down}`.

### Initial state
- A random region is grown from a random cell (generate.hs `addSquare`: a random seed cell is added when none of the six cells ahead of it are inside), and every cell gets the number of region-boundary edges around it as clue. Clues are then removed in random order whenever the solution stays unique.
- `cell-capacity`: the clue for clued cells, `cap-4` for unclued cells, `cap-1` for outside cells; `cell-edge` for every grid edge with its two cells and nodes; `node-degree0` for every node; the capacity successor chain.

### Goal
Every node `(not (node-degree1 n))`, and `(cell-capacity c cap-0)` for every clued cell.

### Other
No action costs. Every puzzle has exactly one solution. Named `slitherlink-<rows>x<cols>-<seed>`; the clue grid is written as a comment header. Grids on which the growth rule only yields ambiguous regions (2×2) are rejected.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| PDDL writer, fed each task's own puzzle | — | objects, init and goal identical in 37/37 grid tasks |
| clue density (clues / cells, all sizes) | 0.421 | 0.417 |
| clue values 0 / 1 / 2 / 3 | 0.015 / 0.169 / 0.493 / 0.323 | 0.034 / 0.136 / 0.485 / 0.345 |
| unique solution | 33/37 proven by our solver (4 exceed its search budget) | always |

**Deviations:**
- Each uniqueness check has a search budget (`MAX_SOLVER_NODES`); a clue whose removal cannot be proven safe within it is kept, so the port never produces the hardest-to-prove puzzles (4 of the 37 IPC puzzles need more than 200,000 search nodes in our solver).
- The 3 opt tasks p18–p20 (`generalized_slitherlink`) are not grid puzzles: irregular cells with 1–4 edges (e.g. 276 of 530 cells with 3 edges in p18), from a source that is not in the repository. This generator cannot produce them.
