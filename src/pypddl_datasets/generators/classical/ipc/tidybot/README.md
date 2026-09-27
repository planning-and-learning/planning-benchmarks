# tidybot (ipc)

A household robot with a gripper and a cart moves objects on a 2D grid into U-shaped cupboards.

## Source

- **Domain:** Bhaskara Marthi, IPC 2011 (deterministic track)
- **Generator:** `tidybot/src/tidybot/core.clj` (Clojure, Bhaskara Marthi) from [pddl-generators](https://github.com/AI-Planning/pddl-generators); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/tidybot-opt11-strips`, `data/classical/downward-benchmarks/tidybot-opt14-strips`, `data/classical/downward-benchmarks/tidybot-sat11-strips` (opt14 reuses 10 opt11 and 10 sat11 tasks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `world_size` | side length of the square grid | 5–12 |
| `num_tables` | tables requested (placements that never fit are dropped) | 0–9 |
| `num_cupboards` | cupboards; each holds `(cupboard_size - 2)^2` objects | 1–3 |
| `min_table_size`, `max_table_size` | range of each table side length | 1–2 (measured) |
| `cupboard_size` | side length of a cupboard including its walls | 4 |
| `seed` | random seed | – |

## Distribution

### Objects
One robot `pr2`, one cart `cart`, `num_cupboards * (cupboard_size - 2)^2` objects `object0..`, coordinates `x0..x(w-1)`, `y0..y(w-1)`, and relative gripper offsets `xrel-1..xrel1`, `yrel-1..yrel1` (gripper radius 1).

### Initial state
- Static grid facts: `leftof`, `above`, `leftof-rel`, `above-rel`, `sum-x`, `sum-y`, `zerox-rel`, `zeroy-rel`.
- Cupboards are placed first, then tables. Each surface draws its side lengths uniformly from the size range and its lower-left corner uniformly in `1..w-size-2`. It is rejected if a corner falls within one cell of an existing surface, and retried up to 100 times before it is dropped. Cupboards get a uniformly random opening side (`u`, `d`, `l`, `r`). The whole world is redrawn (up to 1000 times) until every cupboard fits.
- Table cells: `base-obstacle` + `surface`. Cupboard walls: `base-obstacle` + `gripper-obstacle`. Cupboard interiors: `surface`.
- The robot is fixed at (0,0) (`parked`, `not-pushing`, `gripper-empty`, gripper at offset (0,0)), and the cart is fixed at (0,1) (`not-pushed`).
- Objects: one per cupboard interior cell. Each object starts on a distinct cell drawn uniformly from all table cells and cupboard interior cells (`object-pos` + `gripper-obstacle`).

### Goal
`object-done` for every object. The acceptable positions (`object-goal`, in the initial state) are the object's cupboard cell, plus with probability 1/2 one uniformly random table cell. There is no extra goal when no table was placed; upstream crashes in that case, and the IPC tasks are the runs that succeeded.

### Other
No action costs. The problem is always named `test`. Solvability is not guaranteed; the upstream README notes that some generated tasks are unsolvable or duplicates, and the IPC organisers selected among them.

## Comparison with reference tasks

Statistics over the IPC tasks with tables (27 tasks), comparing each IPC task with 200 generated tasks at the upstream README's parameters for that task (opt11 and sat11 tables).

| aspect | reference tasks | this generator |
|---|---|---|
| objects = 4 × cupboards | 40/40 tasks | always (world redrawn) |
| exact reproduction of opt11 p01 (5×5, 0 tables) | – | identical up to trailing whitespace (seed 38) |
| tables placed / requested | 0.652 | 0.738 |
| mean tables placed | 2.96 (never more than 4) | 3.43 (up to 9 at 11×11) |
| table sides of length 2 | 28.7% | 24.0% |
| extra table goals per object | 0.56 | 0.47 |
| robot, cart, gripper radius | fixed (0,0), (0,1), 1 | same |

**Deviations:**
- The IPC tasks have fewer tables per requested table (0.65 vs 0.74) and never more than 4 tables; at 10×10 with 9 requested tables, IPC has 4 and this generator 4.8 on average. The organisers' selection is not reproducible; pass a smaller `num_tables` (2–4) to match.
- At 9×9 this generator sometimes places 0 tables (the minimum over 200 seeds is 0); every IPC 9×9 task has at least 2.
- Whole-world redraw until all cupboards fit: upstream silently drops cupboards (154/200 samples at 12×12 with 3 cupboards), whereas all IPC tasks contain every requested cupboard.
