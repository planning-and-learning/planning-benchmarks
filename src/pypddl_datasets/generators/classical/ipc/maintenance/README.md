# maintenance (ipc)

Mechanics are scheduled day by day at airports so that every plane gets maintained during one of its visits.

## Source

- **Domain:** Jussi Rintanen, IPC 2014
- **Generator:** `pddl-generators/maintenance/maintenance.c` (Jussi Rintanen); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/maintenance-opt14-adl`, `data/classical/downward-benchmarks/maintenance-sat14-adl` (one shared domain file)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_days` | days in the schedule | 10–200 |
| `num_planes` | planes | 10–900 |
| `num_visits` | visits per plane | 2–8 |

## Distribution

### Objects
Days `d1..d<days+1>` (one more than there are `today` facts, as upstream), airports `fra ber ham`, planes `ap1..ap<planes>`.

### Initial state
- `(today d<i>)` for every day but the extra one.
- Each plane makes `num_visits` visits, each on a uniform day at a uniform one of the three airports. Repeated (plane, day, airport) draws are printed twice, as upstream.

### Goal
`(done ap<i>)` for every plane.

### Other
No action costs. Upstream's `<mechanics>` and `<cities>` arguments are dropped: the IPC tasks always use 1 and 3, visits are always spread over three airports, and mechanics never appear in the task. Name `maintenance-scheduling-1-3-<days>-<planes>-<visits>-<seed>`. Solvability isn't guaranteed (a day can have visits at two airports), as upstream.

## Comparison with reference tasks

All 25 IPC tasks regenerated at their days, planes, visits and index as seed:

| aspect | reference tasks | this generator |
|---|---|---|
| `today`, `at`, `done` fact counts | — | identical in 25/25 |
| duplicated `at` facts (total) | 341 | 324 |
| airports | fra, ber, ham | fra, ber, ham |

**Deviations:** none found; the random visits themselves differ (C `rand()` vs Python `random`).
