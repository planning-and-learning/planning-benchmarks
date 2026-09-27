# agricola (autoscale)

A simplified Agricola: place workers on actions over the rounds, feed the family, build rooms.

## Source

- **Domain:** Tomás de la Rosa, IPC 2018; `domain.pddl` is Autoscale's version, whose `ag__finish_round_renew` differs from the IPC file in one action; generated problems parse against both
- **Generator:** re-export of `ipc/agricola` (port of `GenAgricola.py`)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-{agile,optimal}-strips/agricola`, from Autoscale's pool of upstream-generator runs (`tasks-of-domains-without-usable-generator/agricola`, names `p-empty-<stages>-<workers>-<seed>`); none is an IPC task

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `last_stage` | stage whose harvest must end (sets the number of rounds) | 9–12 (10–21 rounds) |
| `num_workers` | workers | 3–13 |
| `must_create_workers` | goal requires creating all workers | both |

## Distribution

### Objects
Numbers, stages, rounds, workers, rooms, as `ipc/agricola`.

### Initial state
As `ipc/agricola`: the round cards in random order, food and resource supply, initial rooms and workers, `(= (total-cost) 0)`.

### Goal
`(harvest_phase stage<last_stage> harvest_end)`, plus `(max_worker worker<num_workers>)` with `must_create_workers`.

### Other
Action costs and metric `minimize (total-cost)`. Tasks may be unsolvable (e.g. starvation at a harvest), as upstream.

## Comparison with reference tasks

All 60 tasks regenerated at the `last_stage`, workers and worker goal matching their round count (5 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| every init predicate count (22 predicates) | e.g. `category_round` 14.55, `food_required` 10.13, `num_substract` 164.6 | identical means |

**Deviations:** none found; only the random round-card order and initial food differ per seed.
