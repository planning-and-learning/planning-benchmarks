# elevators (autoscale)

Fast and slow elevators with limited capacity and floor-dependent travel costs carry passengers between floors of a building divided into areas.

## Source

- **Domain:** IPC 2008, sequenced STRIPS encoding with action costs (same domain file as the IPC)
- **Generator:** `elevators/generate.py` from Autoscale's pddl-generators (author unknown), called as `generate.py --seed .. {areas} {area_size} {passengers} {fast} {slow} --fast_cost 3 --stop_fast_cost 1 --fast_capacity 3 --slow_cost 1 --stop_slow_cost 5 --slow_capacity 2`; `generator.py` re-exports `../../ipc/elevators`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/elevators`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/elevators`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_areas` | areas (Autoscale enum 2-4) | agile: 3 |
| `area_size` | floors per area | agile: 6-35 |
| `num_passengers` | passengers | agile: 3-104 |
| `num_fast_elevators` | fast elevators (Autoscale enum 1-3) | agile: 1 |
| `num_slow_elevators` | slow elevators per area | 1 |
| capacities, costs | fast 3 / stop 1 / capacity 3, slow 1 / stop 5 / capacity 2 | constants (the defaults) |

## Distribution

### Objects
The same as `ipc/elevators`: counts `n*`, passengers `p*`, `fast*` and `slow{area}-{i}` elevators.

### Initial state
The same as `ipc/elevators`:
- Fast elevators reach every `area_size // 2`-th floor; slow elevators reach their area plus the first floor of the next one.
- Elevators start empty on a random reachable floor, and passengers start on random floors.
- Travel costs are `stop + distance * cost`.

### Goal
Every passenger has a goal on a random floor other than its start.

### Other
Action costs with a `total-cost` metric. Problem name `elevators-a..-s..-p..-f..-l..`. Every floor is reachable, so tasks are solvable.

## Comparison with reference tasks

30 agile tasks, each generated at its recovered parameters (1 seed):

| aspect | reference tasks | this generator |
|---|---|---|
| floors, elevators, passengers, reachable floors, capacities, goals | per task | identical in all 30 tasks |
| init `above` / `next` / `reachable-floor` / `can-hold` / `passenger-at` | 67770 / 1845 / 2146 / 270 / 1605 | identical |
| `travel-fast` / `travel-slow` facts | 637 / 23205 | identical |

**Deviations:**
- Problem names are `elevators-a..` instead of Autoscale's constant `elevators`.
