# transport (autoscale)

Trucks with limited capacity deliver packages over roads with lengths as costs.

## Source

- **Domain:** IPC 2008 Transport (authors not named in the domain or generator files), with `road-length` action costs
- **Generator:** `ipc/transport` with `action_costs=True`: the port of `pddl-generators/transport/{city,two-cities,three-cities}-generator.py` and `euclidean_graph.py` (the IPC 2008–2014 generators)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/transport` (also `21.11-optimal-strips/transport`); the same generators produced `data/classical/downward-benchmarks/transport-{opt,sat}{08,11,14}-strips`

## Parameters

| parameter | meaning | reference range (`domains.py`; agile tasks) |
|---|---|---|
| `kind` | `city`, `two-cities`, `three-cities` | all three; 10 / 8 / 12 tasks |
| `num_nodes` | locations per city | 2–60; 19–54 |
| `num_trucks` | trucks | 2–10 + slope; 2–96 |
| `num_packages` | packages | 2–10 + slope; 4–100 |
| `degree` | target average degree | 3, 4, 5; 3 and 5 |
| `size`, `min_distance` | area side, minimum node distance | 1000, 100 (fixed) |

## Distribution

### Objects
`city-loc-<i>` (and the other cities' locations), `truck-<i>`, `package-<i>`, `capacity-0..capacity-4`.

### Initial state
- Per city, nodes placed uniformly in the area with `min_distance` (area grows ×1.5 when placement fails); roads connect nodes within a degree-derived connect distance, increased until the graph is connected; cities are joined by single roads (upstream's three-cities `shortest_route` quirks kept).
- `road-length` = ceil(Euclidean distance / 10); `(= (total-cost) 0)`.
- Trucks at uniform locations with capacity uniform in 2..4; packages at uniform locations (two-cities: packages start in city 1, trucks and goals in city 2).

### Goal
Every package at a uniform location different from its start.

### Other
`(:metric minimize (total-cost))`. Name `transport-<kind>-sequential-<n>nodes-<size>size-<d>degree-<md>mindistance-<t>trucks-<p>packages-<seed>seed`, like upstream. Always solvable (connected roads).

## Comparison with reference tasks

All 30 agile tasks at their parameters and seeds.

| aspect | reference tasks | this generator |
|---|---|---|
| locations | 66.2 | 66.2 |
| mean out-degree | 4.28 | 4.28 |
| mean road length | 19.25 | 19.25 |
| capacities 2 / 3 / 4 | 355 / 317 / 364 | 346 / 330 / 360 |
| goal equals start | 0 | 0 |

**Deviations:** none found. Against the IPC 2008 tasks with `degree` 3 the mean out-degree is lower (e.g. 3.17 vs 4.4 for opt08 p05), suggesting an older generator version there; IPC 2011/2014 tasks match within ±0.4.
