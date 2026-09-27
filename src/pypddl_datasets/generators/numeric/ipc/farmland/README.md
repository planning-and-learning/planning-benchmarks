# farmland (numeric/ipc)

Workers are moved between adjacent farms until every farm is staffed and a weighted reward bound is reached.

## Source

- **Domain:** Farmland by Enrico Scala and Miquel Ramirez (Scala, Haslum, Thiébaux and Ramirez, JAIR 2020); IPC 2023 numeric track
- **Generator:** port of `farmland/farmlandgenerator.py` (Enrico Scala) from [hstairs/planning-numeric-domains-generators](https://github.com/hstairs/planning-numeric-domains-generators), ladder-graph mode, plus the IPC tasks' `(= (cost) 0)`; networkx replaced by the explicit ladder edges; Python port in `generator.py`
- **Reference tasks:** `data/numeric/ipc2023/farmland`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_farms` | farms (even) | 2–10 |
| `num_units` | workers on the source farm | 100–900 |
| `seed` | RNG seed | 1229 |

## Distribution

### Objects
`farm0..farm{n-1}` of type `farm`.

### Initial state
- A ladder graph over the farms (`networkx.ladder_graph(n/2)`: two paths plus rungs), `adj` in both directions.
- A uniformly chosen source farm has `num_units` workers; every other farm 0 or 1 (uniform).
- `(= (cost) 0)`.

### Goal
- `(>= (x f) 1)` for every farm.
- Weighted reward `Σ w_f · x_f ≥ 1.4 · num_units`, with weight 1.0 for the source and uniform 1.0–2.0 (one decimal) for the others.

### Other
No metric. Solvable: move-slow keeps the worker total, and moving workers to weights > 1 raises the reward. Problem name `instance_<n>_<units>_<seed>_ladder`, like upstream.

## Comparison with reference tasks

Every reference task regenerated at the farms, units and seed in its name:

| aspect | reference tasks | this generator |
|---|---|---|
| ladder `adj` facts, fluents, source size, 0/1 others | 20 tasks | identical structure in 20/20 |
| non-source weight, mean (range) | 1.44 (1.1–1.9) | 1.49 (1.1–2.0) |
| reward bound | 1.4 · units | same |

**Deviations:** the source farm, the 0/1 allocations and the weights differ from the reference draws: upstream ran under Python 2, whose `randint` draws differently.
