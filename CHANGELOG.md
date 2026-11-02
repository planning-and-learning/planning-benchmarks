# Changelog

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
