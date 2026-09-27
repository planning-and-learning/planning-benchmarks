# settlersnumeric (numeric/ipc)

Settlers: gather and refine resources, build infrastructure, vehicles and houses on a land and sea map.

## Source

- **Domain:** Settlers, IPC 2002 numeric track (domain file: introduced by Maria Fox and Derek Long in IPC-3; pddl-generators credits Patrik Haslum)
- **Generator:** reconstruction from the reference tasks; the IPC tasks were written by hand and `pddl-generators/settlers` is a discretised STRIPS variant (needs CPLEX)
- **Reference tasks:** `data/numeric/ipc2023/settlersnumeric`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | places | 4–15 |
| `num_vehicles` | potential vehicles | 5–15 |
| `num_goals` | goals | 1–30 |
| `num_islands` | land-connected islands | 1–3 |

## Distribution

### Objects
`location<i>` places, `vehicle<i>` vehicles.

### Initial state
- Islands: random spanning tree plus extra roads per island, mean degree `2.4 + 0.25·size`; `connected-by-land` symmetric.
- Each place coastal with probability 0.55; islands chained by sea between coastal places, extra sea routes between coastal places with probability 0.1.
- Woodland 0.68, mountain 0.38, metalliferous 0.26 per place; island 0 has at least one of each.
- All numeric fluents 0 (resource use, labour, pollution, housing, carts, resources per place); every vehicle `potential`.

### Goal
`num_goals` distinct goals drawn by kind with the IPC frequencies: rail along a road (0.45), housing ≥ 1 (p 0.7) or ≥ 2 (0.18), sawmill (0.13), ironworks (0.11), coal stack (0.11), timber at a place (0.01), a ship (0.01).

### Other
Metric `(+ (+ (* a (pollution)) (* b (resource-use))) (* c (labour)))`, weights uniform in 0..3. Solvable by construction: island 0 can produce every resource, carts and ships reach every place, rail goals are roads.

## Comparison with reference tasks

60 generated tasks at IPC-like sizes vs the 20 reference tasks:

| aspect | reference tasks | this generator |
|---|---|---|
| coastal places | 0.56 | 0.53 |
| woodland / mountain / metalliferous per place | 0.70 / 0.40 / 0.28 | 0.67 / 0.37 / 0.28 |
| goal kinds rail / housing / sawmill / ironworks / coal stack | 0.45 / 0.20 / 0.13 / 0.12 / 0.10 | 0.48 / 0.17 / 0.12 / 0.13 / 0.10 |
| directed roads per place (4–6 / 7–9 / 10–15 places) | 3.2 / 4.4 / 5.0 | 3.6 / 4.1 / 5.1 |

**Deviations:**
- One IPC task (pfile7) has a rail goal between places without a road, and one (pfile14) a sea route between non-coastal places; both are left out (the first is unsolvable).
