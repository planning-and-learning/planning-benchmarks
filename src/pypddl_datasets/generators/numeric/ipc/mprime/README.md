# mprime (numeric/ipc)

Mystery-prime with fuel and space as numeric fluents: vehicles carry cargo along roads, fuel can be passed between locations.

## Source

- **Domain:** Mystery-prime by Drew McDermott, IPC 1998; numeric encoding `mystery-prime-typed` of the IPC 2023 numeric track
- **Generator:** translation of `classical/ipc/mprime` (fitted to the IPC 1998 tasks; McDermott's generator is not public). The IPC 2023 tasks are exact translations of IPC 1998 mprime tasks: a location's fuel is the index of its fuel level along the `attacks` chain, a vehicle's space the index of its space level along `orbits`
- **Reference tasks:** `data/numeric/ipc2023/mprime`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | foods (locations) | 4–25 |
| `num_vehicles` | pleasures (vehicles) | 1–6 |
| `num_cargos` | pains (cargos) | 2–15 |
| `num_fuel_levels` | fuel levels | 5–10 |
| `num_space_levels` | space levels | 3–5 |
| `num_goals` | goals | 1–3 |

## Distribution

### Objects
Typed `food`, `pleasure`, `pain` with IPC's obfuscated names.

### Initial state
As `classical/ipc/mprime` (roads `eats`, positions `craves`), with `(= (locale food) k)` and `(= (harmony pleasure) k)` instead of level facts.

### Goal
`craves` goals of cargos, as `classical/ipc/mprime`.

### Other
No metric. No solvability filter (the IPC set contains unsolvable tasks).

## Comparison with reference tasks

40 generated tasks at IPC-like sizes vs the 20 reference tasks:

| aspect | reference tasks | this generator |
|---|---|---|
| mean locale | 2.87 | 2.95 |
| mean harmony | 1.97 | 1.86 |
| roads per food | 2.52 | 2.49 |
| goals per task | 1.5 | 2.25 (parameter) |

**Deviations:** as `classical/ipc/mprime`; the translation itself is exact.
