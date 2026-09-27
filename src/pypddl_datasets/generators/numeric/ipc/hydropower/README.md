# hydropower (numeric/ipc)

A reservoir operator pumps water up when electricity is cheap and generates when it is expensive, to raise funds to a target.

## Source

- **Domain:** Amanda Coles, Maria Fox and Derek Long, "A hybrid LP-RPG heuristic for modelling numeric resource flows in planning", JAIR 46 (2013); IPC 2023 numeric track
- **Generator:** reconstruction from the reference tasks (no generator was published with the IPC 2023 dataset, and none was found elsewhere)
- **Reference tasks:** `data/numeric/ipc2023/hydropower`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `capacity` | reservoir capacity (`stored_capacity`) | 1–53 |
| `seed` | random seed (only used for capacities below 10) | — |

## Distribution

### Objects
27 turn values `n0..n26` and 51 half-hourly time points `t0000..t2500`, identical in every task.

### Initial state
- `(= (value nI) I)` for every turn value and the fixed demand curve of the reference tasks (price level per time point, low at night, peaking at 26 at t1700).
- `(timenow t0000)` and a `before` chain t0000 → … → t2400 (t2430 and t2500 exist but are unreachable, as in the tasks).
- `stored_units` 0, `stored_capacity` = `capacity`, `funds` 1000.

### Goal
`(>= (funds) 1000 + profit)` with profit 50·⌊20·capacity/50⌋ for capacity ≥ 10, else 10·u with u uniform in {2·capacity − 1, 2·capacity}.

### Other
No metric. Always solvable: the optimal profit is 22.95 per unit of capacity (buy at 3 before t0400, sell at 26 at t1700) and the goal profit is at most 20 per unit. Problem name `power<capacity>`.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| objects and initial facts | one fixed template, capacity varies | identical for the task's capacity |
| goal profit rule | 50·⌊20C/50⌋ (C ≥ 10), 10·{2C−1, 2C} (C < 10) | same rule |
| tasks reproduced exactly (init and goal) | 20 | 20 of 20 for some seed |

**Deviations:** only the problem name (`power<capacity>` instead of the task index).
