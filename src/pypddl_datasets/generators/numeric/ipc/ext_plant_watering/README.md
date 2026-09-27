# ext_plant_watering (numeric/ipc)

Agents carry water from taps to plants on a grid, with a bounded water reserve and bucket size.

## Source

- **Domain:** Joan Espasa Arxer, based on Plant Watering by Guillem Francès and Hector Geffner as adapted to numeric planning by Enrico Scala and Miquel Ramirez (IPC 2023 numeric track)
- **Generator:** reconstruction from the reference tasks (no generator was published)
- **Reference tasks:** `data/numeric/ipc2023/ext-plant-watering`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `size` | grid side (coordinates 1..size) | 10–15 |
| `num_plants` | plants | 5–19 |
| `num_agents`, `num_taps` | agents, taps | 2, 1 |
| `max_carry` | bucket size per agent | 5 |
| `max_poured` | largest demand per plant | 10 |

## Distribution

### Objects
`plant1 ..`, `tap1 ..`, `agent1 ..`.

### Initial state
- Plants, taps and agents on distinct uniformly random cells.
- `carrying`, `poured`, `total_poured`, `total_loaded` are 0; `max_carry` per agent.
- `water_reserve` = total demand + floor(total demand / 10).

### Goal
`(= (poured p) d)` with `d` uniform in 1..`max_poured` for every plant, and `(= (total_poured) (total_loaded))`.

### Other
No metric. Problem name `instance_<size>_<plants>_<agents>_<seed>`, as in the reference tasks. Always solvable (reserve covers the demand).

## Comparison with reference tasks

Every reference task regenerated at the parameters in its name (10 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| reserve = demand + floor(demand / 10) | 20 of 20 | always |
| demand per plant (mean) | 5.62 | 5.49 |
| reserve slack (mean) | 6.85 | 6.69 |
| distinct cells for all things | 20 of 20 | always |
| mean x coordinate | 6.45 | 6.47 |

**Deviations:** none found.
