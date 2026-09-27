# mprime (autoscale)

Logistics variant: trucks move cargo over a map, moves consume fuel at the origin, and fuel can be passed between locations.

## Source

- **Domain:** Drew McDermott (AIPS-1998), typed pddl-generators version with speaking predicate names (`mprime/domain.pddl`)
- **Generator:** port of `pddl-generators/mprime/mprime.c` (FF domain collection; Freiburg notice, see `LICENSES/LicenseRef-Freiburg.txt`); Python port in `generator.py`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-{agile,optimal}-strips/mprime` (60 tasks, parameters in the task names)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | locations | 3–25 |
| `max_fuel` | maximal fuel per location | 3–15 |
| `max_space` | maximal vehicle capacity | 1–4 |
| `num_vehicles` | vehicles | 1–16 |
| `num_cargos` | cargos | 2–50 |

## Distribution

### Objects
`f0..fF` (fuel), `s0..sS` (space), `l0..`, `v0..`, `c0..`.

### Initial state
- Locations form a ring (`conn` both ways); `not-equal` for every location pair; `fuel-neighbor` and `space-neighbor` chains.
- Fuel per location uniform in 0..`max_fuel`; space per vehicle uniform in 1..`max_space`.
- Vehicles and cargos at uniform locations.

### Goal
Every cargo at a uniform location (possibly its start).

### Other
No action costs. Problem name `strips-mprime-l<l>-f<f>-s<s>-v<v>-c<c>`, as upstream. Solvability is not checked (neither upstream).

## Comparison with reference tasks

All 60 Autoscale tasks regenerated at the parameters in their names (5 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| objects, static facts, goal count | — | identical in 60/60 |
| mean fuel / `max_fuel` | 0.563 | 0.514 |
| mean space / `max_space` | 0.743 | 0.749 |
| goals already true | 0.125 | 0.126 |

**Deviations:** the reference tasks carry slightly more fuel, likely because Autoscale kept only solvable draws; this generator does not filter.
