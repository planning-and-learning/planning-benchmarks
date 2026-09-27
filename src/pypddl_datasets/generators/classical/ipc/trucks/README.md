# trucks (ipc)

Trucks with ordered storage areas deliver packages, some of them by a deadline on a discrete time line.

## Source

- **Domain:** Yannis Dimopoulos, Alfonso Gerevini, Alessandro Saetti (IPC 2006, "Trucks Propositional"), lifted ADL version with universal and disjunctive preconditions
- **Generator:** port of `pddl-generators/trucks/trucks.c` (gen-Trucks, same authors), propositional mode; the STRIPS grounding `trucks-strips.sh` is not applied
- **Reference tasks:** `data/classical/downward-benchmarks/trucks` (30 tasks, `ipc-optimal-adl`, `ipc-satisficing-adl`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_trucks` | trucks | 1 |
| `num_locations` | locations | 3–7 |
| `num_packages` | packages | 3–20 |
| `num_areas` | storage areas per truck | 2–6 (always `num_locations - 1`) |
| `name` | problem number, names the task `truck-<n>` like upstream `-n` | 1–30 |

## Distribution

### Objects
`truck<i>`, `package<i>`, `l<i>`, times `t0 … t<T-1>` with T = num_locations · ⌈num_packages / num_areas⌉ + 1, areas `a<i>`.

### Initial state
- Each truck at a uniform location, all its areas `free`; `(closer a_i a_j)` for i < j.
- Packages in groups of `num_areas` at a uniform location per group.
- All locations pairwise `connected`; `(time-now t0)`, `next` chain and the `le` relation over t1 … t<T-1>.

### Goal
Every package at a uniform location different from its start. With probability 1 − 1/num_areas the goal is `(delivered p l t)` with deadline t = w · num_locations (if num_locations ≤ num_areas) or w · (num_areas + 1), w = package index div num_areas + 1; otherwise `(at-destination p l)`.

### Other
No action costs. Every deadline respects the time line upstream checks (w · … ≤ T − 1).

## Comparison with reference tasks

All 30 IPC tasks regenerated at the parameters of the upstream README's IPC call list:

| aspect | reference tasks | this generator |
|---|---|---|
| objects, `free`/`closer`/`connected`/`le`/`next` facts | — | identical in 30/30 |
| goal count, deadline time per deadline package | — | identical in 30/30 |
| goals with a deadline | 0.748 | 0.768 |

**Deviations:** only the random draws (truck and package locations, destinations, which goals have deadlines) differ, since upstream used C `random()`.
