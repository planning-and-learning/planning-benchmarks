# petri_net (numeric/ipc)

Fire Petri-net transitions (up to 4-place hyperedges) from a token source to reach target token counts.

## Source

- **Domain:** anonymous (IPC 2026); `domain.pddl` is the IPC file
- **Generator:** reconstruction from the reference tasks, which use three hand-made nets; no generator was published; `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/petri-net` (prob06–prob10, four goal variants each)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `net` | `mesh` (prob06/08), `pipeline` (prob07), `merge` (prob09/10) | all three |
| `chain_length` | length of each branch's leading chain (mesh, merge) | mesh 3, merge 2 |
| `goal` | goal variant: mesh `hubs`/`sum`, pipeline `drain`, merge `sum`/`empty` | all |
| `goal_tokens` | tokens required in `g` | mesh 2–3, pipeline 1–3, merge 2–5 |

## Distribution

### Objects
`s0`, the branch places (`a…`, `b…`, `c…`; pipeline `p…`, `q…`), `d1 d2` (merge) and `g`.

### Initial state
The net template's `source`, `sink` and transition facts (three branches for mesh/merge, two for pipeline, as the fixed hyperedge arities require); every place's `value` 0 and `(cost) = 0`.

### Goal
`(= tokens (value g))` plus the variant: mesh `hubs` (each branch hub = 1 or 2) or `sum` (the three outer petals sum ≥ 1–3); pipeline each `x5` = 1 or 2 and `x2 x3 x4` = 0; merge `sum` (the branch ends sum to 1) or `empty` (each branch end 0). Values are drawn uniformly from those ranges.

### Other
`(:metric minimize (cost))`. Every IPC value combination is reachable by the net's firings as in the references.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| objects and init facts (default chain lengths) | 3 nets | identical for all 20 tasks |
| goal of each task | 20 goals | each one produced by some seed (tested) |

**Deviations:** none within the templates; larger nets only via `chain_length` (the references have one size per net).
