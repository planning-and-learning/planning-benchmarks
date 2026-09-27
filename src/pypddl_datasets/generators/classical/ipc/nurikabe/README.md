# nurikabe (ipc)

A robot paints islands of a simplified Nurikabe puzzle: starting on a numbered cell it paints that many connected cells, never touching a cell of another island.

## Source

- **Domain:** Álvaro Torralba, Florian Pommerening (IPC 2018)
- **Generator:** `pddl-generators/nurikabe/generate.py` (Álvaro Torralba, Florian Pommerening), `random` source; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/nurikabe-opt18-adl`, `data/classical/downward-benchmarks/nurikabe-sat18-adl`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width`, `height` | grid size (`height` defaults to `width`) | square, 3–12 (opt), 6–15 (sat) |
| `seed` | random seed; the IPC task name `random-NxN-SEED` records it | seeds listed in `generate-ipc-instances.py` |

## Distribution

### Objects
Cells `pos-x-y` for every grid position, numbers `n1..nmax` (largest island size; `n0` is a domain constant), groups `g0..` one per island.

### Initial state
- Walls grow from a uniform random cell as a branching random walk (stop chance 0.01 per step, branch chance 0.5) that never touches itself; every remaining island gets its size written on one of its cells (its `source`).
- Maps are redrawn (up to 1000 times) until at most size/2 islands have size 1 and every island is smaller than the grid side.
- The robot starts at `pos-0-0` in the moving state; `connected` is the 4-neighbourhood; cells next to one source are `part-of` that group, cells next to two sources are `blocked`, all others `available`; `remaining-cells` holds each island's size.

### Goal
Every group painted.

### Other
No action costs. Name `random-<w>x<h>-<seed>`, as upstream. The IPC tasks were made under Python 2, so draws use Python 2's `randint`/`choice` and Python 2's iteration order of the successor set; with that the seed in a task name reproduces it. Solvability is not checked: upstream's `generate-if-solvable.sh` filtered seeds with an external Nurikabe solver.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| tasks reproduced from the size and seed in their name | 40 | 40 identical (whitespace-normalized) |

**Deviations:** none in content. The IPC seeds were chosen among solvable draws; the generator does not filter for solvability.
