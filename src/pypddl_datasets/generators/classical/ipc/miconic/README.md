# miconic (ipc)

An elevator picks up passengers at their origin floor and drops them at their destination.

## Source

- **Domain:** Jana Koehler, AIPS-2000 (Miconic-STRIPS); `domain.pddl` is the IPC file (untyped, type predicates, `board` keeps `origin`)
- **Generator:** pddl-generators `miconic/miconic.c` (the AIPS-2000 competition generator, (C) 2001 Albert Ludwigs University Freiburg); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/miconic`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_floors` | floors | 2–60 (always 2 × passengers) |
| `num_passengers` | passengers | 1–30 (5 tasks per size) |
| `seed` | random seed | – |
| `typed` | typed encoding (Autoscale's domain) instead of type predicates | `false` |

## Distribution

### Objects
`p0..` passengers, `f0..` floors; untyped, with `(passenger p)` and `(floor f)` facts (`typed=True`: typed objects, no type facts).

### Initial state
`(above f{i} f{j})` for all `i < j`; per passenger a uniform origin floor and a uniform destination floor different from the origin; `(lift-at f0)`.

### Goal
`(served p)` for every passenger.

### Other
No action costs. Problem name `mixed-f{floors}-p{passengers}-u0-v0-d0-a0-n0-a0-b0-n0-f0`. `num_floors >= 2` is required (upstream loops forever with one floor); always solvable.

## Comparison with reference tasks

| aspect | reference tasks (150) | this generator |
|---|---|---|
| floors / passengers | floors = 2 × passengers, passengers 1–30 | any |
| origin == destination | 0 / 2325 | never |
| lift start | `f0` in 150 / 150 | `f0` |
| goals | `served` for all passengers | same |
| encoding | untyped, `(passenger p)`/`(floor f)` type facts; `board` keeps `origin` | the same IPC domain file and encoding |
| problem name | `mixed-f6-p3-u0-v0-g0-a0-n0-a0-b0-n0-f0-r0` | `mixed-f6-p3-u0-v0-d0-a0-n0-a0-b0-n0-f0` |

**Deviations:**
- None in the distribution; only the problem name suffix differs (`d0`, no `r0`).
