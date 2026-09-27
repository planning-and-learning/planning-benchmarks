# sugar (numeric/ipc)

Mills turn raw cane into sugar brands, trucks and cranes move it to depots, to fill the requested storage.

## Source

- **Domain:** supply-chain domain from Amanda Coles, Maria Fox and Derek Long, "A hybrid LP-RPG heuristic for modelling numeric resource flows in planning", JAIR 46 (2013); IPC 2023 numeric track
- **Generator:** reconstruction from the reference tasks, which are hand-written from one template (no generator was published, and none was found elsewhere)
- **Reference tasks:** `data/numeric/ipc2023/sugar`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_mills` | mills (2 or 3) | 2 (1 task), 3 (19 tasks) |
| `num_goals` | in-storage goals | 1–5 |
| `seed` | random seed | — |

## Distribution

### Objects
Brands 1–4, `sugar-cane`, trucks 1–2, depots 1–3, mills 1–2 or 1–3, cranes 1–3 (crane3 has no location with 2 mills, as in the reference task).

### Initial state
- The reference template: production sets and current brands per mill, declared `in-storage` fluents per mill (mill2 declares brand1 instead of brand4, so it cannot produce brand4), all `change-process` pairs, complete road map, trucks at depot1/depot2 with capacities 10/6, crane capacities 5 (3/5 with 2 mills), service times 10/15/10, cost-process 1/3/6, max-produce 5/8/10, max-changing 2.
- Raw cane per mill drawn from the reference values {0, 3, 4, 5, 7, 8, 10, 15, 20, 25, 30}; `unharvest-field` uniform in 3..4.
- With 3 mills, mill3 starts with 2 units of brand4 with probability 0.85 (16 of 18 reference tasks); `labour-cost` 0 is initialised with probability 0.6.

### Goal
`num_goals` distinct `(>= (in-storage L B) A)`: B a brand some mill can produce; L a depot, or with probability 0.15 a mill declaring that fluent; A drawn from the reference amounts (1, 2, 3, 4, 5, 7, 10 with their observed frequencies).

### Other
No metric. Draws repeat until the total goal amount fits the cane (stock plus 5 per harvest), which with the complete road map and manual loading makes the task solvable. Problem name `sugar-m<num_mills>-g<num_goals>`.

## Comparison with reference tasks

Five seeds per reference task at its mill and goal count:

| aspect | reference tasks | this generator |
|---|---|---|
| goals per task | 2.9 | 2.9 |
| mean goal amount | 3.17 | 3.77 |
| share of goals at mills | 0.09 | 0.10 |
| structure (objects, static facts) | one template | same template |

**Deviations:**
- The reference template has small hand-edit variations the generator does not reproduce (a duplicated `current-process` fact in 2 tasks, missing `service-time crane3` in 1, other production sets in 2).
- Raw cane is drawn independently per mill; the references often repeat values across mills.
