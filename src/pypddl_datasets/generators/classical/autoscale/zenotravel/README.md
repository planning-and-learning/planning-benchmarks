# zenotravel (autoscale)

Planes with discrete fuel levels fly people between cities.

## Source

- **Domain:** IPC 2002 (organised by Derek Long and Maria Fox), STRIPS typed version
- **Generator:** `pddl-generators/zenotravel/zenogenerator.cc` as called by Autoscale: `ztravel <seed> <cities> <planes> <people>` (typed, no distance); `ipc/zenotravel` with `typed=True`, which this package wraps
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/zenotravel` (also `21.11-optimal-strips/zenotravel`)

## Parameters

| parameter | meaning | reference range (`domains.py`; agile tasks) |
|---|---|---|
| `num_cities` | cities | 3–30 + slope; 17–130 |
| `num_planes` | planes | 1–20 + slope ≤ 1; 6–32 |
| `num_people` | people | 5–20 + slope 1–10; 5–48 |
| `distance` | distance bound | 0 (not passed) |

## Distribution

### Objects
Typed `plane1.. - aircraft`, `person1.. - person`, `city0.. - city`, `fl0..fl6 - flevel`.

### Initial state
Planes and people at uniform cities; every plane at `fl0` (no distance); `next` chain. No type predicates.

### Goal
Each plane with probability 0.3, each person with probability 0.97, at a uniform city.

### Other
No costs. Name `ztravel-c<C>-<P>-<Q>`. Always solvable.

## Comparison with reference tasks

All 30 agile tasks.

| aspect | reference tasks | this generator |
|---|---|---|
| initial fuel | `fl0` for all 557 planes | `fl0` for all |
| plane goal rate | 0.31 | 0.30 |
| encoding | typed | typed |

**Deviations:** none found; the problem name also encodes the number of cities.
