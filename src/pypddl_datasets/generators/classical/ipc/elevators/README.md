# elevators (ipc)

Fast and slow elevators with limited capacity and floor-dependent travel costs carry passengers between floors of a building divided into areas.

## Source

- **Domain:** IPC 2008, sequenced STRIPS encoding with action costs (also used in IPC 2011)
- **Generator:** `elevators/generate.py` from pddl-generators (author unknown, per its README); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/elevators-opt08-strips`, `data/classical/downward-benchmarks/elevators-sat08-strips`, `data/classical/downward-benchmarks/elevators-opt11-strips`, `data/classical/downward-benchmarks/elevators-sat11-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_areas` | areas; floors = `num_areas * area_size + 1` | 2-4 |
| `area_size` | floors per area | 4-10 |
| `num_passengers` | passengers | 3-60 |
| `num_fast_elevators` | fast elevators | 1-4 |
| `num_slow_elevators` | slow elevators per area | 1 |
| `fast_capacity` / `slow_capacity` | elevator capacities | 3/2, 4/3 or 6/4 (default 3/2) |
| `fast_cost`, `stop_fast_cost` / `slow_cost`, `stop_slow_cost` | travel cost = stop + distance * cost | 3, 1 / 1, 5 (defaults) |

## Distribution

### Objects
Counts `n0..` (floors and capacities), passengers `p*`, `fast*` and `slow{area}-{i}` elevators.

### Initial state
- `next` and `above` define the floor order.
- Fast elevators reach every `area_size // 2`-th floor of the building.
- Slow elevators of area a reach the floors of area a plus the first floor of the next area.
- Each elevator starts at a uniformly random reachable floor, holding 0 passengers, with `can-hold` up to its capacity.
- Passengers start on uniformly random floors.
- `travel-fast` and `travel-slow` costs are `stop + |i - j| * cost` for every pair of floors the elevator reaches.

### Goal
Every passenger has a goal on a uniformly random floor different from its start.

### Other
- Action costs, with `(:metric minimize (total-cost))`.
- Problem name `elevators-a{areas}-s{size}-p{passengers}-f{fast}-l{slow}`.
- Every floor is reachable by a slow elevator, so tasks are solvable.

## Comparison with reference tasks

100 IPC tasks, each generated at its recovered areas, area size, passengers, elevators and capacities (1 seed):

| aspect | reference tasks | this generator |
|---|---|---|
| floors, elevators, passengers, reachable floors, fast-stop step, capacities, goals | per task | identical in all 100 tasks |
| init `above` / `next` / `reachable-floor` / `can-hold` | 16014 / 1548 / 3054 / 1547 | identical |
| `travel-fast` / `travel-slow` facts | 1623 / 6026 | identical; same cost formula (fast 1 + 3d, slow 5 + d) |
| lift starts on a reachable floor | 448 of 448 | 448 of 448 |
| goals equal to the start floor | 0 | 0 |

**Deviations:**
- Problem names are `elevators-a..` instead of `elevators-sequencedstrips-p{floors}_{passengers}_{seed}`.
- Capacities are parameters with default 3/2. The larger IPC tasks need 4/3 or 6/4 passed explicitly.
