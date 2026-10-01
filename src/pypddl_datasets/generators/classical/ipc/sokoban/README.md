# sokoban (ipc)

Sokoban: a player walks on a grid and pushes stones (never pulls) onto goal cells; every push costs 1.

## Source

- **Domain:** IPC 2008 sequential Sokoban (`sokoban-sequential`), reused in IPC 2011
- **Generator:** the IPC tasks are not random: they are hand-made Microban levels by David W. Skinner, converted to PDDL by pddl-generators `sokoban/build-problems.py`. This generator draws random levels of similar size in exactly that encoding; pddl-generators' `sokoban/random/` (Madhu Srinivasan, IPC 2008 learning track, GPL) targets a different typed domain and was only a reference. Python implementation in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/sokoban-opt08-strips`, `data/classical/downward-benchmarks/sokoban-sat08-strips`, `data/classical/downward-benchmarks/sokoban-opt11-strips`, `data/classical/downward-benchmarks/sokoban-sat11-strips` (40 distinct Microban levels)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width`, `height` | bounding box of the level including walls | width 7–32, height 6–19 |
| `num_floor` | connected floor cells | 16–217 (mean 41.7) |
| `num_stones` | stones = goals | 1–12 (mean 4.8) |
| `num_pulls` | reverse pushes used to scramble (default 20 · num_stones) | – |
| `grid` | `square` (IPC) or `hex` (Hexoban: six directions, every second cell of the box) | IPC: square; Autoscale: 11 of 60 hex |
| `num_players` | players; all of them pull during scrambling | IPC: 1; Autoscale: 1–20 (22 of 60 tasks have several) |
| `style` | `ipc`, or `learning` for the IPC 2023 learning-track encoding (square grid, one player); `ipc_learning/sokoban` uses a different forward-walk generator with that encoding | IPC: ipc |
| `seed` | random seed | – |

## Distribution

### Objects
Players `player-01 …` in reading order; stones `stone-01 …` numbered in reading order; a location `pos-<col>-<row>` (1-based, zero-padded to the digits of the larger side) for every cell of the bounding box, walls and outside space included (hex: only cells with column + row even, as `build-problems.py`); directions `dir-up dir-down dir-left dir-right` (hex: `dir-east dir-west dir-northeast dir-northwest dir-southeast dir-southwest`, east/west two columns apart).

### Initial state
- Floor: a connected region of `num_floor` cells grown from a random cell inside the border; a frontier cell is added with weight 1 / (its floor neighbours), giving corridors and irregular rooms. Every non-floor cell touching the floor (8-neighbourhood; hex: the six neighbours) is a wall; the rest of the box is outside space. The box is cropped to the walls.
- Goals: `num_stones` random floor cells from which a stone can be pulled away (two free cells in a line).
- Several players (`num_players` > 1): they start on random non-goal floor cells; each pull is made by a random player that can pull, walking only through free floor (stones and the other players block). Players stay where their last pull leaves them, so they may end on goal cells.
- Stones and player (single player, the IPC case): stones start on the goals and are scrambled by up to `num_pulls` random pulls (pushes played backwards), weighted by (cells the player can still reach)³ and by 4 for stones still on a goal; then the player is placed on a random reachable cell. Of 3 scrambles, the one with the fewest stones left on goals is kept; a level with all stones on goals is redrawn.
- Facts as in `build-problems.py`: `is-goal`/`is-nongoal` for every location, `clear` for every non-wall cell without player or stone (outside space included), `move-dir` between every pair of adjacent non-wall cells, `at` for player and stones, `at-goal` for stones starting on a goal, `(= (total-cost) 0)`.

### Goal
`at-goal` for every stone; the player's final position is free.

### Other
Metric minimize `total-cost` (pushes). Problem name `sokoban-<cols>x<rows>-f<num_floor>-s<num_stones>[-p<players>][-<seed>]` (`hexoban-…` for hex); the ASCII level is included as a comment, as in the IPC files. Every task is solvable: reversing the scramble (each pull as a push, each walk backwards) is a plan; with several players it generally needs more than one of them. All output is lowercase.

## Comparison with reference tasks

Generator: 20 seeds for each of the 40 IPC levels, with that level's width, height, floor cells and stones.

| aspect | reference tasks | this generator |
|---|---|---|
| bounding box width, mean [min, max] | 12.05 [7, 32] | 10.50 [7, 29] |
| bounding box height, mean [min, max] | 9.57 [6, 18] | 9.35 [6, 18] |
| walls, mean [min, max] | 47.6 [24, 262] | 45.4 [22, 152] |
| walls per floor cell, mean | 1.15 | 1.13 |
| stones starting on a goal | 12.0 % | 15.8 % |
| `move-dir` facts, mean | 151.9 | 147.7 |
| `clear` facts, mean | 54.3 | 50.7 |
| solvable | 40/40 (hand-made) | by construction |

Multi-player and hex modes, against the 22 multi-player Autoscale tasks (10 hex, 12 square) regenerated at their box, floor cells, stones and players (5 seeds each); hex / square:

| aspect | reference tasks | this generator |
|---|---|---|
| directions (hex) | six (`dir-east` …) | six, same `move-dir` offsets |
| players, mean | 5.6 / 7.1 | as requested |
| walls | 31.3 / 41.9 | 39.6 / 43.2 |
| stones starting on a goal | 47 % / 38 % | 57 % / 44 % |
| players starting on a goal | 30 % / 34 % | 7 % / 12 % |

**Deviations:**
- Levels are random, not hand-designed: puzzle quality and difficulty for a given size are not comparable to Microban, and the plan length is not controlled.
- Levels are somewhat narrower than their bounding-box parameter (width 10.5 vs 12.1), because the grown region rarely touches every side; the largest level (29×19) gets fewer walls (152 vs 262), since Microban's biggest level is a sparse maze.
- Slightly more stones start on a goal (15.8 % vs 12.0 %).
- Multi-player levels: players start on goal cells less often (7–12 % vs 30–34 %) and slightly more stones start on a goal; hex levels have more walls (40 vs 31). The designed references park players on goals deliberately; here that only happens when a scramble leaves a player there.
