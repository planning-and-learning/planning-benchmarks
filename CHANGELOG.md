# Changelog

## Unreleased

- Three new families with the benchmarks of the International Planning Competitions, each with
  a `tests` collection of the smallest task of every domain:
  - `temporal/`: every temporal domain of IPC 2002, 2004, 2006, 2008, 2011 and 2014 (92 domains,
    PDDL 2.1 durative actions, PDDL 2.2 timed initial literals, PDDL 3 constraints), from
    [potassco/pddl-instances](https://github.com/potassco/pddl-instances). The IPC 2018 temporal
    domains are not published anywhere we found.
  - `probabilistic/`: IPPC 2004 (the competition's PPDDL files), 2006 and 2008 (from
    [probfd/ppddl-benchmarks](https://github.com/probfd/ppddl-benchmarks); the competitions' own
    sites are offline). The IPPC 2006 warm-up tasks are not included.
  - `nondeterministic/`: the IPC 2008 FOND track (blocksworld, faults, first-responders, forest), as
    [QuMuLab/planner-for-relevant-policies](https://github.com/QuMuLab/planner-for-relevant-policies)
    distributes it, with its corrected forest tasks.
- Suites `<collection>-<family>` with `-test` companions (e.g. `ipc2011-temporal`,
  `ippc2008-probabilistic`, `ipc2008-nondeterministic`) and `tests-temporal`, `tests-probabilistic`,
  `tests-nondeterministic`.
- `Requirement` gains `NON_DETERMINISTIC`, `PROBABILISTIC_EFFECTS` and `REWARDS`.
- The data is validated with pypddl 1.15 (strict mode), which reads these formalisms. To pass
  it, the imported files were repaired, beyond their requirement lines (`strict_clean`):
  - files that hold a domain and its problem are split, and per-task domains are named
    `<task>-domain.pddl`;
  - a name declared twice in a typed list is declared once with both types, as `(either ...)`
    (IPC 2006/2011/2014 storage's `area`, IPC 2011/2014 temporal-machine-shop's kilns);
  - parent types used but not declared are declared as object types (e.g. tpp's `place`,
    crew-planning's `objects`, temporal-machine-shop's `piece`);
  - problem objects that their domain declares as constants are not declared again
    (IPC 2004 compiled time-window variants);
  - a predicate does not take the name of a type, which is a unary predicate: IPC 2008 FOND
    faults' `fault` predicate is `has_fault` (its type `fault` stays);
  - point fixes: IPPC 2004 file-world's missing `(:init)`, IPC 2004 airport-time-windows
    instance 5's doubled metric, IPC 2004 satellite-time-windows instance 31's
    `senty_image` (for `sent_image`), and IPPC 2008 tireworlds' bare `dead` (for `(dead)`).

- `downward-benchmarks/schedule/orig-domain.pddl` names its type `temperature-type`, as the
  collection's `domain.pddl` does: the type `temperature` was also a binary predicate's name,
  which pypddl 1.15 rejects in strict mode.
- `sokoban/single_stone` is replaced by `sokoban/single_box`: levels come from the IPC
  2023 learning-track generator (ipc_learning/sokoban) with one box, whose planted push
  route grows with the grid, instead of the IPC level generator, whose 20 reverse pulls
  kept the stone about 4 pushes from its goal. Parameters: `grid_size` and `seed`. The
  domain is the learning-track encoding (no action costs); the optimal cost counts
  moves and pushes.
- `visitall/tree_maze`: the maze is a uniformly random spanning tree (Wilson's
  algorithm) instead of a randomized-Prim tree, which favoured short, bushy mazes.

## 0.0.19

Optimally-tractable fragments: 30 generators now draw their tasks as the IPC generators
do, restricted only by their stated fragment, instead of with ad-hoc samplers. Their restrictions and optimal-cost formulas
are unchanged, and every `; optimal plan cost: N` stays exact: a blind optimal search
(`tests/test_optimally_tractable_costs.py`) and A* with LM-cut agree with the stated
costs on small tasks, and the mean cost now grows with size (10, 100, 1000 objects).

- `blocks_3/clear_block`, `clear_blocks`, `goal_on_table`, `init_on_table`, `on_pair`,
  `table_blocks` and the same six under `blocks_4` (12 fragments): initial towers, and
  the goal towers of `init_on_table`, are uniform over all states via the IPC
  generator's bwstates sampler instead of a coin flip per block; `clear_block` targets
  a uniformly random covered block instead of a random tower.
- `nomystery/single_package`: the IPC 2011 road network and fuel rule (ipc/nomystery):
  `edge_factor` roads per location with costs up to `max_edge_cost`, and
  `constrainedness` times the cheapest fuel, so no task is redrawn. Parameters
  `max_fuel` and `extra_roads` are gone; `edge_factor=1.5`, `max_edge_cost=25` and
  `constrainedness=1.0` are new. This also fixes tasks that declared fewer fuel levels
  than the largest road cost (invalid PDDL for `max_fuel` below 3).
- `sokoban/single_stone`: levels come from the IPC level generator with one stone (a
  connected room, the stone scrambled off its goal by reverse pulls, no redrawing) and
  its parameters: `wall_ratio` is gone, `num_floor` (required, as in the IPC) and
  `num_pulls` (default 20, the IPC's; scale it with the room for longer solutions)
  are new.
- `transport/common_destination`, `transport/common_route`: roads form the IPC
  Euclidean city (ipc/transport) instead of a tree plus a few roads. Parameter
  `extra_roads` is gone; `degree=3`, `size=1000` and `min_distance=100` are new.
- `ricochet_robots/single_robot`: `num_barriers` is optional and defaults to the IPC
  draw (uniform in 5..5 + size^2/3), drawn with the IPC barrier sampler.
- `grid/single_key_locks`: the key is placed on a cell the robot can reach and the
  goal on a cell the key can reach, instead of redrawing whole maps.
- `ferry/common_origin`: goals may equal the origin, as in the IPC generator (the cost
  counts misplaced cars). `miconic/common_origin`, `common_destination`,
  `disjoint_floors`: the lift starts at f0 as in the IPC tasks; `lift_start="random"`
  draws it as the IPC 2023 learning track does. `transport/*`: the IPC's
  `capacity-0..4` objects are kept. `ricochet_robots/single_robot`: gives up after the
  IPC's 1000 draws instead of looping when no solvable board exists.

- `grid/single_key`, `grid/single_key_locks`: the IPC's locked region (`num_locks`
  connected cells, default a quarter of the grid, grown as by ipc/grid) replaces
  cell-by-cell walls and locks; the key may lie on the robot's cell and the goal on
  the key's cell (cost 0) or, in `single_key_locks`, on a lock cell, as in the IPC.
  Parameters `lock_ratio` is gone, `num_locks` is new, and `wall_ratio` now defaults
  to 0 (walls are the fragment's extension; `single_key` has no ratio any more).
- `satellite/single_instrument`: directions, calibration targets, pointing and image
  goals are drawn as by ipc/satellite (satgen): parameters `num_targets` and
  `num_observations` replace `num_directions` and `num_images`; a draw without any
  image goal is repeated.
- `tpp/exclusive_markets`: supplies are the IPC's capped sums of per-market lots (the
  whole supply at the good's one market) and demands uniform up to the supply;
  `num_depots` (default 1) is new, the truck starts at a random depot.
- `zenotravel/common_origin`, `common_destination`: as in ipc/zenotravel, each person
  has a goal with probability 0.97 that may be its own city, and the plane has a goal
  city with probability 0.3; the cost counts people to move and the plane's extra
  flight.

- Second pass against the references: `init_on_table` (both encodings) emits the full
  goal state as the IPC generators do, `on_pair` draws any ordered pair (a satisfied one
  costs 0), `table_blocks` and `clear_blocks` draw a uniformly random non-empty set of
  blocks; `miconic/disjoint_floors` samples the IPC trips conditioned on disjointness
  exactly; `zenotravel/*` draw the fuel from the IPC's `distance` (new parameter,
  default 1000 as in the IPC tasks) and repeat goal-less draws; `transport/common_route`
  conditions the IPC's capacity draw (2..4) on holding every package; `visitall/row`
  exposes the IPC's `goal_ratio`; `ricochet_robots/single_robot` exposes the IPC's
  `board` ("asp2015") and needs a board of at least 3 as the IPC; `sokoban/single_stone`
  exposes the IPC's `grid` ("hex").

Shared code: the IPC generators now expose their samplers publicly: `completion_counts`
and `make_stacks` (blocks_3, blocks_4, ipc_learning blocksworld), `road_graph`
(nomystery), `city_roads` (transport) and `random_barriers` (ricochet_robots); their
tasks are byte-for-byte unchanged. `tests/optimal_solver.py` is a small blind optimal planner on
pypddl tasks for such checks.
