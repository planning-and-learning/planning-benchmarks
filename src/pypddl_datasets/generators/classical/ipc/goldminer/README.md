# goldminer (ipc)

A robot in a rock grid uses a laser and bombs to reach and pick up gold. IPC 2008 learning track domain; no reference tasks in this repository.

## Source

- **Domain:** Alan Fern, IPC 2008 learning track (`gold-miner-typed`)
- **Generator:** port of `pddl-generators/goldminer/gold-miner-generator.cpp` (© 2008 Madhu Srinivasan, GPL-2.0-or-later); Python port in `generator.py`
- **Reference tasks:** none

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rows` | grid rows (≥ 2) | – |
| `num_cols` | grid columns (≥ 3) | – |

## Distribution

### Objects
One `loc` `f<row>-<col>f` per cell.

### Initial state
- `connected` in both directions between 4-neighbours; `arm-empty`.
- Robot in column 0 at a uniform row; bomb and laser supply in column 0 at another uniform row; gold (under soft rock) in the last column at a uniform row.
- Other cells soft or hard rock with probability 1/2 each, then a random soft-rock path is carved from the gold towards column 1 (random up/down runs and left steps), as upstream.

### Goal
`(holds-gold)`.

### Other
No costs or metric. Name `goldminer-r<R>-c<C>`. Solvable by construction (laser through rock, bomb at the gold).

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| – | no reference tasks | – |

**Deviations:** none found (no reference).
