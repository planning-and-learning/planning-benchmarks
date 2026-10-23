# Optimally tractable fragments

Fragments of the classical domains where a lowest-cost plan can be found in
polynomial time. Each `<domain>/<fragment>.py` exposes `make_problem(...)` and a
CLI, uses the fixed `<domain>/domain.pddl` (copied from the `ipc/` or
`ipc_learning/` counterpart, the transport one with road-length costs), and starts
every task with the line

```
; optimal plan cost: N
```

computed by the polynomial algorithm in the module docstring. All costs were
checked against A* with LM-cut (Scorpion) on hundreds of small random tasks.
The directory name has a hyphen, so load modules by path or run them as scripts:

```sh
python src/pypddl_datasets/generators/classical/optimally-tractable/ferry/unrestricted.py -c 10 -l 5 -s 1
```

Fragments are listed per domain from easy to hard. "Whole distribution" marks
fragments that cover everything the IPC generator produces.

| domain | fragment | restriction | optimal cost |
|---|---|---|---|
| blocks_4 | `goal_on_table` | goal: every block on the table | 2 per block not on the table |
| blocks_4 | `init_on_table` | initially every block on the table, goal: random towers | 2 per goal `on` |
| blocks_4 | `clear_block` | goal: `(clear x)` | 2k - 1 for k blocks above x |
| blocks_4 | `on_pair` | goal: one `(on a b)` | 2 per block above a or b, +2 for a, +2 if a is higher up in b's tower |
| blocks_4 | `table_blocks` | goal: a random set X on the table | 2 per block of X off the table or above one of X |
| blocks_4 | `clear_blocks` | goal: a random set X clear | 2u for the u blocks above X, -1 if the last one held is not in X |
| blocks_3 | same six | same, 3-operator encoding | 1 per moved block (`clear_block` k, `clear_blocks` u) |
| gripper | `one_way` | IPC: all balls rooma → roomb (whole distribution) | 2n + 2⌈n/2⌉ - 1 |
| gripper | `two_way` | balls and goals in both rooms, robot anywhere | 2(a+b) + max(2⌈a/2⌉ - 1, 2⌈b/2⌉, 0) for a balls away from and b towards the robot's room |
| ferry | `common_origin` | all cars at one location | 4k - 1, +1 if the ferry starts elsewhere |
| ferry | `unrestricted` | IPC ferry (whole distribution) | 3k + minimum trail cover of the trip multigraph, from the ferry, minus 1 |
| miconic | `common_origin` | all passengers on one floor | 2n + destination floors (+1 to reach the origin) |
| miconic | `common_destination` | all passengers to one floor | 2n + origin floors + 1 (-1 if the lift starts at an origin) |
| miconic | `disjoint_floors` | no floor is both an origin and a destination | 2n + origin floors + destination floors (-1 if the lift starts at an origin) |
| childsnack | `exact_ingredients` | IPC childsnack (whole distribution) | 3 per child + occupied tables |
| spanner | `corridor` | IPC 2023 learning spanner (whole distribution) | locations + 1 + 2 per nut |
| satellite | `single_instrument` | one satellite, one instrument supporting all modes, image goals | 2 + images + turns (to the calibration target, then each other image direction) |
| visitall | `row` | one row of cells | (n - 1) + distance to the nearer end |
| visitall | `full_grid` | full rectangle, Hamiltonian-path start | cells - 1 |
| visitall | `tree_maze` | passages form a spanning tree | 2(cells - 1) - eccentricity of the start |
| grid | `single_key` | one key, locks that no key opens (walls) | BFS distances robot → key → goal + 2 |
| grid | `single_key_locks` | one key, locks it opens and walls | BFS robot → key (locks closed) + Dijkstra key → goal (lock cells cost 2) + 2 |
| transport | `common_route` | all packages share origin and destination, trucks hold them all (road-length costs) | nearest truck's distance + route length + 2 per package |
| logistics | `common_origin` | all packages at one location, one truck per city | loads/unloads per vehicle leg + unavoidable drives and flights (see docstring) |
| logistics | `common_destination` | all packages to one location, one truck per city | mirror of `common_origin`; one plane suffices (see docstring) |
| movie | `standard` | IPC movie (whole distribution) | 7 |
| delivery | `common_destination` | IPC delivery: one truck, all packages to one cell (whole distribution) | Σ(2·dist(g, p) + 2) + min_p(dist(t, p) - dist(p, g)) |
| delivery | `common_route` | several trucks, all packages share origin o and goal g | 2k + 2kD + Σ_{t∈S}(d_t - D): the closest truck plus every truck closer to o than D = dist(o, g), at most k |
| elevators | `common_origin` | one elevator serving all floors with room for everyone, all passengers on one floor (stop + rate·distance costs) | reach the origin, one stop per destination floor, sweep to the nearer end first |
| sokoban | `single_stone` | one stone in a random room | 0-1 BFS over (stone, player) states, pushes cost 1 |
| floortile | `single_column` | IPC floortile with one robot and one column | climb + 2 per paint + 1 per down + 5 per colour change, painting top-down |
| tpp | `exclusive_markets` | one truck, each good sold at one market, all places connected | 3 per demanded unit + markets visited + 1 |
| elevators | `common_destination` | as `common_origin`, all passengers to one floor | one stop per origin floor (the start is free) + the destination, covering the origins' range |
| transport | `common_destination` | one truck of capacity 1, all packages to one location | as delivery `common_destination` with shortest road distances |
| zenotravel | `common_origin` | one plane, all people in one city | 2 per person + m flights + max(0, m - initial fuel) refuels |
| zenotravel | `common_destination` | one plane, all people to one city | same, m = origin cities (except the plane's) + 1 |
| nomystery | `single_package` | one truck, one package, fuel costs | BFS over (location, fuel, package position) |
| ricochet_robots | `single_robot` | one robot, random barriers | BFS over the robot's cells |
| goldminer | `standard` | IPC 2023 learning gold miner (whole distribution) | laser along the gold row, then one bomb: \|r - s\| + 3\|s - g\| + 4C - 4 (or all bombs on three-column boards) |

Not covered: the general Blocksworld, Miconic, Logistics, Visitall and Grid
problems are NP-hard to solve optimally (and Sokoban is PSPACE-complete); these
fragments remove what makes them hard (deadlocked towers, ordering of stops, tours,
choice between sellers, interacting stones).
