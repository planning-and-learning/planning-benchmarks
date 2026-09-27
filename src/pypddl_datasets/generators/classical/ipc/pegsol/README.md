# pegsol (ipc)

Peg Solitaire on the 33-hole English board: jump pegs over each other until a single peg remains on the centre, paying 1 per move (a sequence of jumps by the same peg is one move).

## Source

- **Domain:** IPC 2008 sequential encoding (authors not named in the sources), reused in IPC 2011
- **Generator:** pddl-generators `pegsol/generator.rb` + `instances.rb` (converts the fixed Solipeg 2.2 puzzle library by J Cade Roux, derived from "Problems in Puzzle-Peg", Lubbers & Bell, 1924); `generator.py` keeps the output format but draws random positions instead
- **Reference tasks:** `data/classical/downward-benchmarks/pegsol-08-strips`, `data/classical/downward-benchmarks/pegsol-opt11-strips`, `data/classical/downward-benchmarks/pegsol-sat11-strips` (identical domain files; `domain.pddl` is that file, lowercased)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_pegs` | pegs in the initial position | 5–32 |
| `seed` | random seed | – |

## Distribution

### Objects
The 33 cells of the English cross board, `pos-<row>-<col>` (rows/columns 0–6, arms 3 wide), typed `location`; independent of the parameters.

### Initial state
`(= (total-cost) 0)`, `(move-ended)`, the 76 `in-line` triples (both directions of every horizontal and vertical line of three cells), `occupied` for the pegs and `free` for the other cells. The position is drawn by playing `num_pegs − 1` reverse jumps from a single peg on the centre in random order (depth-first with backtracking and random restarts); with 32 pegs the single hole is uniform over the five cells whose single-hole game can end on the centre: (0,3), (3,0), (3,3), (3,6), (6,3).

### Goal
`(occupied pos-3-3)` and `free` for the other 32 cells.

### Other
Action costs (`jump-new-move` costs 1, continuing jumps and `end-move` are free), `(:metric minimize (total-cost))`. Problem name `pegsolitaire-sequential-<n>pegs`. Every task is solvable by construction.

## Comparison with reference tasks

Statistics over the 36 distinct IPC puzzles and 10 seeds per IPC peg count.

| aspect | reference tasks | this generator |
|---|---|---|
| board / target | English 33 cells, centre (all tasks) | same |
| pegs | 5–32, mean 15.5 | same counts by construction |
| mean Manhattan distance of a peg to the centre | 2.32 | 2.39 |
| fraction of pegs on the arms (outside the central 3×3) | 0.62 | 0.68 |
| orthogonally adjacent peg pairs per peg | 0.91 | 0.91 |
| 32-peg tasks | centre hole only ("Plain") | hole uniform over the 5 valid cells |
| tasks whose library entry says diagonal moves are needed | 3 of 70 (puzzles 67 Banker, 73 Krazy Kat) | none: all solvable orthogonally |

**Deviations:**
- The IPC tasks are hand-designed puzzles from a fixed library, not samples; this generator draws random solvable end-game positions with the same board, target, goal and encoding. Positions are slightly more spread onto the arms (0.68 vs 0.62).
- IPC files carry the Solipeg GPL notice and the puzzle name as comments; generated tasks have no comments.
