# rovers (ipc)

Rovers traverse a planet surface, take soil/rock samples and images, and communicate the data to a lander.

## Source

- **Domain:** Rovers (Derek Long and Maria Fox), IPC 2002, STRIPS version
- **Generator:** pddl-generators `rovers/rovgen.cc`; by default in its pre-2021 form (as used for IPC 2002), with `autoscale=True` in its June 2021 form; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/rovers`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rovers` | rovers (one store each) | 1–14 |
| `num_waypoints` | waypoints | 4–100 |
| `num_objectives` | objectives | 2–14 |
| `num_cameras` | cameras requested (imaging rovers without one get one more) | output: 1–18 cameras |
| `num_goals` | goal-count parameter `g` | output: 3–69 goals |
| `autoscale` | 2021 rovgen instead of the IPC form | `False` |

The per-task parameters listed in upstream's README (p01: 1 4 2 1 3, …) are counts read off the IPC tasks, not generator inputs.

## Distribution

### Objects
`general` (lander), modes `colour high_res low_res`, `rover{i}` with `rover{i}store`, `waypoint{i}`, `camera{i}`, `objective{i}`.

### Initial state
- A random directed `visible` graph (5 draws per waypoint), repaired to be connected; the lander at a uniform waypoint.
- Each rover: uniform start, soil/rock/imaging equipment from one of 7 non-empty combinations, and a breadth-first `can_traverse` area (each edge kept with probability 0.7, radius n/3 + rnd(n)); a waypoint visible from the lander is added to each rover's area when missing.
- Cameras on uniform rovers with a uniform calibration target and random modes; imaging rovers without a camera get one.
- Each objective is `visible_from` `waypoint0..waypoint{k-1}` with k uniform in 1..`num_waypoints` (the pre-2021 rovgen output); with `autoscale=True`, from a uniform random waypoint set. A camera's calibration target is made visible from its rover's area when it is not.
- Each waypoint has a soil and a rock sample with probability ≈ 1/2; 30% are sunny.

### Goal
Per type (soil, rock, image) `rnd(1..g) + g/3` draws of distinct reachable sample sites or objective/mode pairs of equipped rovers. By default the task is resampled until every type has at least one goal, as in all IPC tasks; with `autoscale=True` a type may have none.

### Other
No action costs. Problem name `roverprob{seed}`. Every goal uses a site or objective an equipped rover can reach, and every camera can be calibrated.

## Comparison with reference tasks

Generated 3 tasks per IPC task, with its rover, waypoint, objective and camera counts:

| aspect | reference tasks (40) | this generator (120) |
|---|---|---|
| tasks with a goal type missing | 0 / 40 | 0 / 120 |
| tasks whose objectives are all visible from a prefix `waypoint0..k` | 40 / 40 | 117 / 120 |
| `visible_from` per objective, as a fraction of the waypoints | 0.530 | 0.531 |
| cameras whose calibration target is unreachable | 0 / 337 | 0 / 1164 |
| imaging rovers without a camera, cameras on non-imaging rovers | 0, 0 | 0, 0 |

**Deviations:**
- In 3 of 120 generated tasks, the calibration repair extends one objective's prefix by a reachable waypoint; IPC tasks never needed it.
- The IPC generator's seeds are unknown, so goal counts per task can only be matched in distribution.
