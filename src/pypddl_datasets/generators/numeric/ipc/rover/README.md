# rover (numeric/ipc)

Rovers with energy take samples and images on a planet and recharge in the sun.

## Source

- **Domain:** Rovers, IPC 2002 numeric track (motivated by the 2003 MER missions); IPC 2023 encoding with `in` for rover positions
- **Generator:** port of `pddl-generators/rovers/rovgen.cc` in numeric mode (`rovgen -n`): the STRIPS task of `classical/ipc/rovers` (the pre-2021 rovgen that produced the IPC 2002 tasks) plus the numeric additions; Python port in `generator.py`
- **Reference tasks:** `data/numeric/ipc2023/rover`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rovers` | rovers | 1–8 |
| `num_waypoints` | waypoints | 4–25 |
| `num_objectives` | objectives | 2–8 |
| `num_cameras` | cameras | 2–7 |
| `num_goals` | goal count parameter of rovgen | 3–20 |

## Distribution

### Objects
`general` lander, modes `colour high_res low_res`, `rover<i>` with store, `waypoint<i>`, `camera<i>`, `objective<i>`.

### Initial state
- Everything symbolic as in `classical/ipc/rovers` (IPC prefix visibility, every goal type present); rover positions use `in`.
- Each waypoint is in the sun with probability 0.3; like upstream `makeChargeable`, a rover none of whose traversal sources is sunny gets the source of a random traversal made sunny.
- Every rover starts with energy 50 (navigate costs 8, recharging requires sun); `recharges` 0.

### Goal
As `classical/ipc/rovers`: soil, rock and image data to communicate, every type present.

### Other
`(:metric minimize (recharges))`. Name `roverprob<seed>`.

## Comparison with reference tasks

All 20 tasks regenerated at their object counts and goal count, 5 seeds each:

| aspect | reference tasks | this generator |
|---|---|---|
| sunny waypoints | 0.321 | 0.321 |
| every rover can recharge | 20/20 | 100/100 |
| every goal type present | 20/20 | 100/100 |
| rover energy | 50 | 50 |

**Deviations:** none found beyond `classical/ipc/rovers`'.
