# nomystery (autoscale)

One truck delivers packages over a weighted road graph with a tight, non-replenishable fuel budget.

## Source

- **Domain:** Nomystery (Hoffmann et al.), IPC 2011; Autoscale's copy, lowercased
- **Generator:** Autoscale's `pddl-generators/nomystery` (C++ generator with optimal solver), called as `nomystery -l L -p P -n 1.5 -m 25 -c C -s seed -e 0`; `../../ipc/nomystery` with `full_sum_table=False`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/nomystery`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/nomystery`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | graph nodes | agile: 14–28, optimal: 7–12 |
| `num_packages` | packages | agile: 9–86, optimal: 3–40 |
| `edge_factor` | edges = int(factor × locations) | 1.5 |
| `max_edge_cost` | edge weights uniform in 1..max | 25 |
| `constrainedness` | initial fuel = int(C × optimal fuel) | agile: 1.5, 2.0; optimal: 1.5 |
| `seed` | random seed | encoded in the task name |

## Distribution

### Objects
`t0`, `l0..`, `p0..`, `level0..level{F}` with `F = max(initial fuel, 25)`.

### Initial state
Random spanning tree plus extra edges up to `int(1.5 n)`, uniform weights 1..25, truck and packages at uniform locations, fuel `int(C × M)` with `M` the exact minimum fuel, `sum` facts for every level and every edge-cost delta only (unlike the IPC tasks, which list every level pair), `(= (total-cost) 0)`.

### Goal
Every package at a uniform location different from its start.

### Other
`(:metric minimize (total-cost))`; problem name identical to the Autoscale names (parameters and seed encoded). See `../../ipc/nomystery`.

## Comparison with reference tasks

| aspect | reference tasks | this generator (parameters and seed from the task name) |
|---|---|---|
| problem name | e.g. `transport-l14-t1-p9---int100n150-m25---int100c200---s2019---e0` | identical |
| `sum` facts / fuel levels, optimal p01, p02 | 474/83, 712/103 | 1153/160, 861/122 |
| `sum` facts / fuel levels, agile p01, p02 | 5085/313, 6815/391 | 4091/353, 4361/325 |

**Deviations:** none structural (the `sum` table is restricted to edge-cost deltas, as in the Autoscale tasks); fuel budgets differ per task because the RNG differs.
