# mprime (ipc)

Mystery with an extra action that passes fuel between locations.

## Source

- **Domain:** Drew McDermott, AIPS-1998 competition
- **Generator:** same distribution as `../mystery` (`generator.py` wraps it with `prime=True`); pddl-generators `mprime/mprime.c` is a typed adaptation the IPC tasks do not follow
- **Reference tasks:** `data/classical/downward-benchmarks/mprime`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | locations (`food`) | 4–22 |
| `num_vehicles` | vehicles (`pleasure`), at most `num_locations` | 1–16 |
| `num_cargos` | cargos (`pain`) | 2–46 |
| `num_fuel_levels` | fuel levels (`province`) | 3–13 |
| `num_space_levels` | space levels (`planet`) | 2–4 |
| `num_goals` | cargos with a goal | 1–3 |

## Distribution

### Objects
As `../mystery`.

### Initial state
As `../mystery`.

### Goal
As `../mystery`.

### Other
No action costs. Domain `mystery-prime-strips` (requires `:equality :negative-preconditions`). Problem name `strips-mprime-l<L>-v<V>-c<C>-f<F>-s<S>-g<G>` (IPC: `strips-mprime-x-<i>` and `strips-mprime-y-<i>`). Solvability is not checked.

## Comparison with reference tasks

prob01–30 are the mystery tasks under the mprime domain, so the measurements in `../mystery/README.md` (taken over all 35 mprime tasks) apply unchanged.

| aspect | reference tasks | this generator |
|---|---|---|
| roads per location | 1.268 | 1.288 |
| vehicles at distinct locations | 35/35 | always |
| goals per task | 1–3 | `num_goals` |

**Deviations:** as `../mystery`.
