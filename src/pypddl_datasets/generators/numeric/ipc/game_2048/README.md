# game_2048 (numeric/ipc)

The 2048 sliding puzzle without random tile spawns: merge the tiles of a 4×4 board into one target tile in the top-left corner.

## Source

- **Domain:** Christian Muise, Samantha Papais and Ronny Rochwerg; IPC 2026 numeric track
- **Generator:** reconstruction from the reference tasks (no generator was published with the IPC 2026 dataset)
- **Reference tasks:** `data/numeric/ipc2026/2048`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `target` | goal tile at p11 (power of two) | 128–8192 |
| `num_moves` | length of the recorded solution | 8–29 |
| `num_tiles` | tiles on the initial board (default uniform in 9..16) | 9–16 |
| `seed` | random seed | — |

## Distribution

### Objects
None besides the domain constants (positions, statuses, directions, indices).

### Initial state
- The fixed `pos-at`, `next`, `start-status` and `next-idx` facts of the reference tasks and `(free-to-play)`.
- Tile values from a backward search: starting from the goal board, `num_moves` inverse moves are applied; each undoes some merges (splitting tiles of at least 4 into two halves, so that the board ends near `num_tiles` tiles) and spreads each line's tiles over its cells in order, packed toward the edge of the preceding move (free for the initial board). A step is kept only if the forward move reproduces the board; dead ends backtrack.

### Goal
`(= (value p11) target)` and 0 on every other position.

### Other
No metric. The header comment records the solution sequence (`; solution sequence: up left …`) and both boards, as in the reference tasks; replaying it reaches the goal, so every task is solvable. Problem name `game-2048-t<target>-n<num_moves>`.

## Comparison with reference tasks

Three seeds per reference task at its target and number of moves:

| aspect | reference tasks | this generator |
|---|---|---|
| tile sum equals target | 20 of 20 | always |
| recorded solution solves the task (replayed with the domain's move rule) | 20 of 20 | always |
| tiles on the initial board | 13.5 (9–16) | 9.2 (4–15) |
| smallest tile, mean | 19 | 18 |

**Deviations:**
- Boards are sparser (9.2 vs 13.5 tiles): dense boards often have no pre-image, and when the search fails the tile target is lowered by one. Full 16-tile boards (5 reference tasks) are rarely produced.
