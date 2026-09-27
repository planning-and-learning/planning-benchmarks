# zenotravel (ipc)

Planes with discrete fuel levels fly people between cities.

## Source

- **Domain:** IPC 2002 (organised by Derek Long and Maria Fox), STRIPS untyped version
- **Generator:** port of `pddl-generators/zenotravel/zenogenerator.cc` (IPC 2002 generator), STRIPS mode; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/zenotravel`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cities` | cities | 3–22 |
| `num_planes` | planes | 1–5 |
| `num_people` | people | 2–25 |
| `distance` | distance bound; positive values randomise initial fuel | positive (fuel is random in all IPC tasks) |
| `typed` | typed encoding (Autoscale) instead of type predicates | false |

## Distribution

### Objects
`plane1..`, `person1..`, `city0..`, fuel levels `fl0..fl6`.

### Initial state
- Every plane and person at a uniform city; type predicates (`aircraft`, `person`, `city`, `flevel`) unless `typed`.
- Fuel: `fl0` for every plane with `distance=0`; otherwise `fl(rnd(b·distance) mod 7)` with burn rate `b` uniform in 1..5, i.e. about uniform over the 7 levels.
- `next` chain `fl0 → … → fl6`.

### Goal
Each plane with probability 0.3 and each person with probability 0.97 must be at a uniform city (possibly its start).

### Other
No costs or metric. Name `ztravel-c<C>-<P>-<Q>`. Always solvable (refuel works everywhere).

## Comparison with reference tasks

All 20 IPC tasks, 20 distinct seeds each, `distance=1000`.

| aspect | reference tasks | this generator |
|---|---|---|
| initial fuel levels fl0..fl6 | 10, 9, 10, 9, 6, 10, 11 of 65 planes (≈ uniform) | 0.12–0.16 each (uniform) |
| plane goal rate | 0.31 | 0.29 |
| person goal rate | 0.97 | 0.97 |
| goal equals start | 30/219 = 0.14 | 0.12 |
| encoding | untyped, type predicates | untyped, type predicates |
| problem name | `ztravel-<planes>-<people>` | `ztravel-c<cities>-<planes>-<people>` |

**Deviations:**
- The default `distance=0` puts every plane at `fl0`; reproducing the IPC tasks needs `distance > 0`.
- Problem name also encodes the number of cities.
