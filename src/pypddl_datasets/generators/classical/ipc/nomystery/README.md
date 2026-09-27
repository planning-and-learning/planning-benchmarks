# nomystery (ipc)

One truck delivers packages over a weighted road graph with a tight, non-replenishable fuel budget.

## Source

- **Domain:** Nomystery, designed to study resource-constrained planning (Hoffmann et al.), IPC 2011
- **Generator:** pddl-generators `nomystery/src` (C++ generator with a domain-specific optimal solver); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/nomystery-opt11-strips`, `data/classical/downward-benchmarks/nomystery-sat11-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | graph nodes | opt11: 4–13, sat11: 6–15 |
| `num_packages` | packages | opt11: 3–12 (locations − 1), sat11: 6–15 (= locations) |
| `edge_factor` | edges = int(factor × locations) | 1.5 |
| `max_edge_cost` | edge weights uniform in 1..max | 25 |
| `constrainedness` | initial fuel = int(C × optimal fuel) | 1.1 and 1.5 (10 tasks each per track) |
| `seed` | random seed | 1 |
| `full_sum_table` | `sum` for every level pair (IPC) instead of only edge-cost deltas (Autoscale) | `True` |

## Distribution

### Objects
`t0` (one truck), `l0..` locations, `p0..` packages, `level0..level{F}` fuel levels with `F = max(initial fuel, max_edge_cost)`.

### Initial state
A random spanning tree (random connected node to a random unconnected node) plus random extra edges up to `int(edge_factor × n)` edges, each undirected with a uniform weight 1..`max_edge_cost`, written as `connected` and `fuelcost` in both directions. Truck at a uniform location; each package at a uniform location. `(fuel t0 level{int(C × M)})` where `M` is the exact minimum fuel. `(sum level{a} level{d} level{a+d})` for all levels `a` and `d` with `a + d <= F`, including `d = 0`, as in IPC; with `full_sum_table=False` only for the distinct edge costs `d`. `(= (total-cost) 0)`.

### Goal
Every package at a uniform location different from its start.

### Other
`(:metric minimize (total-cost))`. Problem name `transport-l{n}-t1-p{k}---int100n{100·factor}-m{max}---int100c{100·C}---s{seed}---e0`, identical to the IPC names. Solvable for `C >= 1` by construction.

## Comparison with reference tasks

| aspect | reference tasks (40, regenerated with their encoded parameters) | this generator |
|---|---|---|
| objects, edges, goals | edges = int(1.5 n), 1 truck, k goals | identical |
| goal equals start | 0 / 360 | never |
| mean edge cost | 8.8–16.3 | 7.1–13.8 |
| fuel levels (p01 opt, c = 1.5) | 37 | 65 |
| `sum` facts | all level pairs incl. delta 0: L(L+1)/2 for L levels (p01: 703 at 37 levels), 40/40 | all level pairs incl. delta 0: L(L+1)/2 |
| metric, `(= (total-cost) 0)` | yes | yes |

**Deviations:**
- The initial fuel (and so the level count) differs per task because the RNG differs; ranges overlap.
