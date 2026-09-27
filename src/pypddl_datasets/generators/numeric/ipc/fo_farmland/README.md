# fo_farmland (numeric/ipc)

Farmland with hireable cars that move several workers at once, where the reward bound is penalised by the transport cost.

## Source

- **Domain:** FO-Farmland (`farmland_ln`) by Enrico Scala and Dongxu Li (Li, Scala, Haslum and Bogomolov, IJCAI 2018); IPC 2023 numeric track
- **Generator:** `numeric/ipc/farmland` (port of `farmland/farmlandgenerator.py`, Enrico Scala) with the IPC tasks' `(= (num-of-cars) 0)` and cost-penalised bound; Python generator in `generator.py`
- **Reference tasks:** `data/numeric/ipc2023/fo-farmland`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_farms` | farms (even) | 2–10 |
| `num_units` | workers on the source farm | 100–1000 |
| `seed` | RNG seed | 1229 |

## Distribution

### Objects
`farm0..farm{n-1}` of type `farm`.

### Initial state
As `numeric/ipc/farmland` (ladder `adj`, source with `num_units`, others 0/1, `(= (cost) 0)`), plus `(= (num-of-cars) 0)`.

### Goal
- `(>= (x f) 1)` for every farm.
- `Σ w_f · x_f − cost ≥ 1.4 · num_units`, weights as in `farmland`.

### Other
No metric; the cost enters the goal. Problem name `instance_<n>_<units>_<seed>_ladder`.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| ladder `adj` facts, fluents, source size, 0/1 others | 20 tasks | identical structure in 20/20 |
| goal form | `(>= (- reward (cost)) bound)` | same |

**Deviations:** as in `farmland`, the random draws (source, 0/1 allocations, weights) differ from the Python 2 reference draws.
