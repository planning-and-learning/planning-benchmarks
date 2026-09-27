# pegsol (autoscale)

Peg solitaire on the English cross board: jump pegs until a single peg remains in the centre.

## Source

- **Domain:** IPC 2008 sequential encoding (author not named in the sources); `domain.pddl` is Autoscale's copy, identical to `ipc/pegsol`'s
- **Generator:** re-export of `ipc/pegsol` (random positions played backwards from the centre)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-{agile,optimal}-strips/pegsol`, all 60 from Autoscale's pool of pddl-generators puzzle-library conversions (`tasks-of-domains-without-usable-generator/pegsol`, the Solipeg 2.2 library of hand-designed puzzles); 30 of them are also IPC 2008/2011 tasks

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_pegs` | pegs on the board | 5–32 |

## Distribution

### Objects
The 33 board positions `pos-<x>-<y>`.

### Initial state
As `ipc/pegsol`: `num_pegs` pegs obtained by playing random reverse jumps from a single centre peg (for 32 pegs, one of the five holes that can end in the centre), `occupied`/`free` per cell, the static `in-line` jump triples, `move-ended`, `(= (total-cost) 0)`.

### Goal
Only the centre occupied, every other cell `free`.

### Other
`jump-new-move` costs 1, continuing jumps and `end-move` are free; metric `minimize (total-cost)`. Solvable by construction.

## Comparison with reference tasks

All 60 tasks regenerated at their peg count (10 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| pegs | 13.52 | 13.52 |
| mean peg distance to the centre (Manhattan) | 2.20 | 2.34 |

**Deviations:**
- The reference tasks are designed puzzles, the generated ones random reverse-play positions; structure matches, difficulty is not comparable.
