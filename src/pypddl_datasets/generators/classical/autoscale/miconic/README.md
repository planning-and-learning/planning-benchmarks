# miconic (autoscale)

An elevator picks up passengers at their origin floor and drops them at their destination.

## Source

- **Domain:** Jana Koehler, AIPS-2000 (Miconic-STRIPS); Autoscale's typed copy (declares unused `not-boarded`/`not-served`, `board` keeps `origin`), lowercased
- **Generator:** Autoscale's `pddl-generators/miconic/miconic.c` ((C) 2001 Albert Ludwigs University Freiburg), called as `miconic -f {floors} -p {passengers}`; `generator.py` re-exports `../../ipc/miconic` with `typed=True` (same distribution, Autoscale's typed domain)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/miconic`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/miconic`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_floors` | floors (`>= 2`) | agile: 11–124, optimal: 6–61 |
| `num_passengers` | passengers | agile: 19–155, optimal: 8–60 |

## Distribution

### Objects
`p0..` passengers, `f0..` floors (typed).

### Initial state
`(above f{i} f{j})` for all `i < j`; per passenger a uniform origin and a uniform destination different from it; `(lift-at f0)`.

### Goal
`(served p)` for every passenger.

### Other
No action costs. Problem name `mixed-f{floors}-p{passengers}-u0-v0-d0-a0-n0-a0-b0-n0-f0`, as in the Autoscale tasks. Always solvable.

## Comparison with reference tasks

| aspect | reference tasks (60) | this generator (same sizes) |
|---|---|---|
| init predicate counts (`above`, `origin`, `destin`, `lift-at`) | e.g. agile p01: 55/19/19/1 | identical |
| origin == destination | 0 | never |
| lift start | `f0` in 60/60 | `f0` |
| problem name | `mixed-f11-p19-u0-v0-d0-a0-n0-a0-b0-n0-f0` | identical |

**Deviations:** none found.
