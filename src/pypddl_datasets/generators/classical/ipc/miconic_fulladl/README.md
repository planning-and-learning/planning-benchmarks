# miconic_fulladl (ipc)

An elevator serves passengers with extra constraints: vips first, non-stop and direct travellers, attendants for passengers who must not travel alone, conflict groups that must not meet, and floors some passengers may not enter.

## Source

- **Domain:** Jana Koehler, AIPS-2000 (full ADL track)
- **Generator:** port of pddl-generators `miconic-fulladl/miconic.c`, the original AIPS-2000 generator (FF domain collection, Freiburg notice), printed like the IPC tasks
- **Reference tasks:** `data/classical/downward-benchmarks/miconic-fulladl` (150 tasks; `domain.pddl` and `orig-domain.pddl` are identical)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_floors`, `num_passengers` | floors, passengers | 2–60, 1–30 (floors = 2 × passengers) |
| `up_down`, `vip`, `going_nonstop`, `attendant`, `never_alone` | passenger-kind percentages | 20, 5, 5, 60, 10 (upstream defaults) |
| `conflict_a`, `conflict_b` | conflict group percentages | 20, 80 |
| `no_access`, `no_access_floors` | passengers with forbidden floors, floor percentage | 50, 5 |

## Distribution

### Objects
`p0..` passengers and `f0..` floors, all typed `passenger` / `floor`.

### Initial state
- Passenger kinds as unary facts (`going_up`/`going_down`, `vip`, `going_nonstop`, `attendant`, `never_alone`, `conflict_a`, `conflict_b`), each a random subset of `int(p · pct / 100)` passengers; attendants only when a never-alone passenger exists (at least one), conflict B only with a conflict A group and disjoint from it.
- `above` for every floor pair; origins and destinations uniform with upstream's heuristics (no A and B at one origin, conflict passengers away from vip floors, all up/down passengers in one direction, going-nonstop passengers share the first one's destination, no never-alone or conflict passenger waiting at a vip destination).
- `no-access` for 5% of the floors of half the passengers, never their own origin or destination, vip destinations near them, or never-alone origins for attendants; lift at `f0`.

### Goal
`(forall (?p - passenger) (served ?p))`.

### Other
No costs. Where upstream loops forever on a dead end (e.g. an up/down passenger on the top floor when all must go up) the journeys are redrawn. Solvability is not guaranteed (as upstream).

## Comparison with reference tasks

All 150 IPC tasks, regenerated at their floors and passengers (5 seeds), mean facts per task:

| aspect | reference tasks | this generator |
|---|---|---|
| going_up / going_down | 1.38 / 1.32 | 1.25 / 1.45 |
| vip / going_nonstop | 0.37 / 0.37 | 0.37 / 0.37 |
| attendant / never_alone | 8.13 / 1.10 | 8.13 / 1.10 |
| conflict_a / conflict_b | 2.70 / 11.80 | 2.70 / 11.80 |
| no-access | 12.9 | 15.4 |
| destination equals origin | 0 | 0 |

**Deviations:**
- About 20% more `no-access` facts than the IPC tasks (frequency only).
- Problem names encode the parameters and seed.
