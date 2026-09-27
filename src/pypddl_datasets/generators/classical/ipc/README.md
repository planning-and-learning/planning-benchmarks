# IPC generators

Generators for the International Planning Competition domains and our own
variants of them. This is the core: [`../autoscale`](../autoscale) re-exports
these generators wherever Autoscale's distribution is the same. All output is
lowercase. The reference distribution is the IPC instances in
[`data/classical/downward-benchmarks`](../../../../../data/classical/downward-benchmarks):

| generator | reference data |
|---|---|
| agricola | `agricola-{opt,sat}18-strips` |
| assembly | `assembly` (ADL; reconstruction from the AIPS-1998 tasks) |
| barman | `barman-{opt,sat}14-strips` (default); `action_costs=True` for `barman-{opt,sat}11-strips` |
| blocks_3, blocks_4 | `blocks`: blocks_4 defaults to the IPC single-tower goal (`goal="full"` for a full random goal state); blocks_3 is our 3-operator variant |
| cavediving | `cavediving-14-adl` |
| childsnack | `childsnack-{opt,sat}14-strips` |
| citycar | `citycar-{opt,sat}14-adl` (sat domain in `domain.pddl`, opt in `domain_citycar14opt.pddl`) |
| data_network | `data-network-{opt,sat}18-strips` |
| depots | `depot` (untyped; `typed=True` gives Autoscale's encoding) |
| driverlog | `driverlog` (untyped; `typed=True` gives Autoscale's encoding) |
| elevators | `elevators-{opt,sat}{08,11}-strips` |
| flashfill | `flashfill-sat18-adl` (per-task domain via `make_task`) |
| floortile | `floortile-{opt,sat}{11,14}-strips` |
| folding | `folding-opt23-adl` |
| freecell | `freecell` (IPC 2000 and 2002 deals via `style`) |
| grid | `grid` (`style="autoscale"` for Autoscale's lock shapes) |
| gripper | `gripper` |
| hiking | `hiking-{agl,opt,sat}14-strips` |
| labyrinth | `labyrinth-opt23-adl` |
| logistics | `logistics98` (`style="98"`, default) and `logistics00` (`style="00"`, `domain_logistics00.pddl`) |
| maintenance | `maintenance-{opt,sat}14-adl` |
| miconic | `miconic` (untyped; `typed=True` gives Autoscale's encoding) |
| miconic_fulladl | `miconic-fulladl` |
| miconic_simpleadl | `miconic-simpleadl` (re-exports `ipc/miconic`) |
| movie | `movie` |
| mprime | `mprime` |
| mystery | `mystery` (fitted to the IPC tasks; upstream `mystery.c` differs) |
| nomystery | `nomystery-{opt,sat}11-strips` (full `sum` table; `full_sum_table=False` for Autoscale) |
| nurikabe | `nurikabe-{opt,sat}18-adl` |
| openstacks | `openstacks-{opt,sat}08-adl` (default) and `openstacks` (IPC 2006 ADL, `style="06"`, `domain_openstacks06.pddl`) |
| parking | `parking-{opt,sat}{11,14}-strips` |
| pathways | `pathways` (per-task domain via `make_task`; `strips_wrapper=True` for Autoscale's optimal set) |
| pegsol | `pegsol-08-strips`, `pegsol-{opt,sat}11-strips` (random solvable positions; IPC uses a fixed puzzle library) |
| recharging_robots | `recharging-robots-opt23-adl` (`kind` selects the covers or single-source scenario) |
| ricochet_robots | `ricochet-robots-opt23-adl` (`board="asp2015"` for the fixed ASP Competition board) |
| rovers | `rovers` (IPC visibility and all goal types; `autoscale=True` for Autoscale) |
| rubiks_cube | `rubiks-cube-opt23-adl` |
| satellite | `satellite` (untyped, unpatched satgen; `typed=True, patched=True` gives Autoscale's) |
| scanalyzer | `scanalyzer-08-strips`, `scanalyzer-{opt,sat}11-strips` |
| schedule | `schedule` (follows the IPC tasks, not `schedule.c`) |
| settlers | `settlers-{opt,sat}18-adl` (`track`) |
| slitherlink | `slitherlink-opt23-adl` (grid puzzles; the generalized p18–p20 are not generated) |
| snake | `snake-{opt,sat}18-strips` |
| sokoban | `sokoban-{opt,sat}{08,11}-strips` (random solvable levels; IPC uses hand-made Microban levels; `grid="hex"` and `num_players` for Autoscale's Hexoban and multi-player levels) |
| spider | `spider-{opt,sat}18-strips` |
| storage | `storage` |
| termes | `termes-{opt,sat}18-strips` |
| tetris | `tetris-{opt,sat}14-strips` (`block_type` 1–3 for Autoscale's single-piece-type tasks) |
| tidybot | `tidybot-{opt,sat}11-strips`, `tidybot-opt14-strips` |
| tpp | `tpp` |
| transport | `transport-{opt,sat}{08,11,14}-strips` (IPC city generators; cost-free by default against `domain.pddl`, `action_costs=True` for the IPC encoding in `domain_action_costs.pddl`) |
| trucks | `trucks` (lifted ADL, IPC 2006) |
| visitall | `visitall-{opt,sat}{11,14}-strips` |
| woodworking | `woodworking-{opt,sat}{08,11}-strips` (IPC 2011 domain file; output also parses against Autoscale's) |
| zenotravel | `zenotravel` (untyped; `distance` randomizes initial fuel as in the IPC tasks; `typed=True` gives Autoscale's encoding) |

delivery, ferry, goldminer and spanner have no IPC instances in
`downward-benchmarks`; ferry and spanner are compared against
`data/classical/ipc2023-learning`.

The STRIPS versions of openstacks and trucks (`openstacks-*-strips`,
`trucks-strips`) are left out on purpose: they are ground per task, so there is
no lifted structure to learn. The packages below cover their lifted ADL versions.

IPC STRIPS domains without a public generator, and therefore without a
package: airport, ged, organic-synthesis, organic-synthesis-split,
parcprinter, petri-net-alignment, pipesworld-notankage, pipesworld-tankage,
psr-small, quantum-layout, thoughtful.

Our own variants without reference tasks (hiking_binary, transport_fuel) live
in [`../misc`](../misc).

Each package's `README.md` describes its distribution and compares it with
the reference tasks. Authors and license notices: [`../../CREDITS.md`](../../CREDITS.md).
