# gear_car (numeric/ipc)

A car accelerates, shifts through a linear gearbox and must stop in first gear after an exact distance, trading time against fuel.

## Source

- **Domain:** IPC 2026 numeric track (`car_linear_gears_numeric`; authors not named in the files)
- **Generator:** reconstruction from the 20 IPC tasks (no generator was published); Python in `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/gear-car`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_gears` | gears | 2–5 |
| `distance` | target distance D (goal D ≤ d ≤ D+2) | 50–2160 |

## Distribution

### Objects
Gears `g1..g<n>`.

### Initial state
- `(current_gear g1)`, `gear_next` chain; d = v = a = 0, acceleration bounds −1..2, `acc_step` 1, `max_speed` 2n.
- Gear i: speed band 2(i−1)..2i, acceleration −1..(2 for g1, 1 for middle gears, 0 for the top gear), fuel per drive aligned 11 (g1) / 11−i, under 18 / 17, over 15+n for g1 and 12+n−2(i−2) above — exactly the IPC tables.
- `fuel` = ceil(1.2 F) + 10 for the minimum fuel F of any plan (computed by search); `beta` ≈ ceil(1.2 T) + 5n − 6 for the minimum number of drive steps T; `alpha` = beta · (fuel + 1).

### Goal
D ≤ d ≤ D+2, `(current_gear g1)`, v = 0, a = 0, fuel ≥ 0, fuel_used > 0.

### Other
`(:metric minimize (cost))`, where each drive costs alpha + beta · fuel. Deterministic (no seed): the task is a function of `num_gears` and `distance`. Solvable by construction (the fuel budget exceeds a feasible plan's).

## Comparison with reference tasks

Regenerated at each IPC task's gears and distance:

| aspect | reference tasks | this generator |
|---|---|---|
| gear tables, bounds, speeds, goal | — | identical in 19/19 |
| `fuel` | — | identical in 19/19 |
| `beta` (and so `alpha`) | — | within 2 in 19/19 (exact in 10) |

**Deviations:**
- `beta`'s exact IPC formula is unknown; the fit is within 2. It only changes the metric weights.
- `p000` is a hand-edited copy of `p01` (distance 50, fuel 200, p01's alpha/beta); the generator gives fuel 126 there.
