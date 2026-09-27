# rovers (autoscale)

Rovers traverse a planet surface, take soil/rock samples and images, and communicate the data to a lander.

## Source

- **Domain:** Rovers (Derek Long and Maria Fox), IPC 2002, STRIPS version; Autoscale's copy
- **Generator:** Autoscale's `pddl-generators/rovers/rovgen.cc` (June 2021 form), called as `rovgen {seed} {rovers} {waypoints} {objectives} {cameras} {goals}`; `../../ipc/rovers` with `autoscale=True`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/rovers`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/rovers`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rovers` | rovers | agile: 1–4, optimal: 1 |
| `num_waypoints` | waypoints | agile: 10–30, optimal: 6–34 |
| `num_objectives` | objectives | agile: 1–83, optimal: 4–25 |
| `num_cameras` | cameras requested (output may add some) | agile output: 6–43, optimal output: 2–5 |
| `num_goals` | goal-count parameter | agile output: 3–62 goals, optimal output: 5–44 goals |

## Distribution

### Objects
As in `../../ipc/rovers`.

### Initial state
As in `../../ipc/rovers`, except that each objective is visible from a uniform random waypoint set (the June 2021 fix) instead of a prefix `waypoint0..k`.

### Goal
Per type (soil, rock, image) `rnd(1..g) + g/3` draws over reachable sites and objective/mode pairs of equipped rovers, deduplicated; a type may end up without goals (no resampling).

### Other
No action costs. Problem name `roverprob{seed}`.

## Comparison with reference tasks

Generated 3 tasks per agile task, with its rover, waypoint, objective and camera counts:

| aspect | agile reference tasks (30) | this generator (90) |
|---|---|---|
| tasks with a goal type missing | 17 / 30 | 45 / 90 |
| tasks with all-prefix visibility | 0 / 30 | 0 / 90 |
| `visible_from` per objective, as a fraction of the waypoints | 0.396 | 0.399 |
| cameras whose calibration target is unreachable | 0 / 603 | 0 / 1820 |

**Deviations:** Upstream's lander-visibility repair takes the map by value and is lost; ours applies it, so rovers can always reach a waypoint visible from the lander (none of the 30 agile tasks is affected).
