# miconic_simpleadl (ipc)

An elevator serves passengers; stopping at a floor boards and drops everyone there by conditional effects.

## Source

- **Domain:** Jana Koehler, AIPS-2000 (simple ADL track)
- **Generator:** the AIPS-2000 generator with all passenger kinds off, which is the typed `ipc/miconic` distribution; this package re-exports `ipc/miconic` with `typed=True` (no own code)
- **Reference tasks:** `data/classical/downward-benchmarks/miconic-simpleadl` (150 tasks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_floors` | floors | 2–60 (= 2 × passengers) |
| `num_passengers` | passengers | 1–30 |

## Distribution

### Objects
`p0..` passengers and `f0..` floors, typed.

### Initial state
`above` for every floor pair; per passenger a uniform origin and a uniform destination different from it; lift at `f0`.

### Goal
`(served p)` for every passenger.

### Other
No costs. Always solvable.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| floors = 2 × passengers | 150 / 150 | parameter |
| destination equals origin | 0 | 0 |
| lift at `f0` | 150 / 150 | always |
| init and goal predicates | `above`, `origin`, `destin`, `lift-at` / `served` | same |

**Deviations:** none found; problem names encode the parameters.
