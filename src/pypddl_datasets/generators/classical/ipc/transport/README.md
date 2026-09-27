# transport (ipc)

Trucks with limited capacity deliver packages over a road network.

## Source

- **Domain:** IPC 2008 Transport (authors not named in the domain or generator files). `domain.pddl` is the cost-free version (no `:action-costs`, `capacity` predicate); `domain_action_costs.pddl` is the IPC file with `road-length` costs
- **Generator:** port of `pddl-generators/transport/{city,two-cities,three-cities}-generator.py` and `euclidean_graph.py`, the generators behind the IPC 2008–2014 tasks; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/transport-{opt,sat}{08,11,14}-strips`

## Parameters

| parameter | meaning | reference range (IPC task names) |
|---|---|---|
| `kind` | `city`, `two-cities`, `three-cities` | all three |
| `num_nodes` | locations per city | 5–66 |
| `num_trucks` | trucks | 2–6 |
| `num_packages` | packages | 2–30 |
| `degree` | target average degree | 3–5 |
| `size`, `min_distance` | area side, minimum node distance | 1000, 100 |
| `action_costs` | emit `road-length`, `total-cost` and the metric (IPC encoding) | IPC: always |

## Distribution

### Objects
`city-loc-<i>` (`city-<c>-loc-<i>` for several cities), `truck-<i>`, `package-<i>`, `capacity-0..capacity-4`.

### Initial state
- Per city, nodes are placed uniformly in the area with `min_distance` (the area grows ×1.5 when placement fails); roads connect nodes within a degree-derived connect distance, increased until the graph is connected; cities are joined by single roads (upstream's three-cities `shortest_route` quirks kept).
- Trucks at uniform locations with a capacity uniform in 2..4; packages at uniform locations (two-cities: packages start in city 1, trucks in city 2).
- With `action_costs`: `road-length` = ceil(Euclidean distance / 10) per road and `(= (total-cost) 0)`.

### Goal
Every package at a uniform location different from its start (two-cities: in city 2).

### Other
Without `action_costs` the task has exactly the same roads, objects and goals, only without road lengths, total cost and metric; road lengths never constrain applicability, so both encodings have the same plans. With it, `(:metric minimize (total-cost))`, drive costs the road length, pick-up and drop cost 1. Name `transport-<kind>-sequential-<n>nodes-<size>size-<d>degree-<md>mindistance-<t>trucks-<p>packages-<seed>seed`, like upstream. Always solvable (connected roads).

## Comparison with reference tasks

Every IPC task regenerated at the parameters and seed in its name (`action_costs=True`):

| aspect | reference tasks | this generator |
|---|---|---|
| mean out-degree (2008 / 2011 / 2014) | 3.56 / 3.60 / 3.63 | 3.23 / 3.54 / 3.54 |
| mean road length (2008 / 2011 / 2014) | 33.3 / 26.2 / 20.8 | 34.5 / 26.8 / 21.5 |
| capacities 2 / 3 / 4 (all years) | 132 / 155 / 143 | 133 / 171 / 126 |
| domain file | identical to `domain_action_costs.pddl` | — |

**Deviations:**
- 2008 tasks have denser roads (out-degree 3.56 vs 3.23), which suggests an older generator version there.
- One 2008 task (`three-cities`, 1 node per city, degree 0) is outside the generator's parameter range.
