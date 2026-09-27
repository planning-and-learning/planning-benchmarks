# sailing_wind (numeric/ipc)

Sailing boats with wind-angle-dependent speed and inertia must reach and stop next to persons to save them.

## Source

- **Domain:** Luigi Bonassi and Carl Hentges (IPC 2026); `domain.pddl` is the IPC file (opt and sat identical)
- **Generator:** reconstruction from the reference tasks (no generator was published); `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/sailing-wind-opt`, `data/numeric/ipc2026/sailing-wind-sat`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_persons` | persons to save | opt 1, sat 1–2 |
| `num_boats` | boats | 1 |
| `min_distance`, `max_distance` | person distance from the origin | opt 16.3–26.3, sat 100 |
| `angle_step` | quantize person directions (degrees) | sat: 45 |
| `inertia` | boat `r` | opt 0.5, sat 0.9 |

## Distribution

### Objects
Boats `b0..`, persons `p0..`.

### Initial state
Every boat at (0, 0) at rest with sailing angle 0 and the fixed polar diagram of the references (`vmax_0` … `vmax_180`: 0, 0.17, 0.3, 0.45, 0.65, 1, 1.49, 1.44, 1.37, 1.26, 1.12, 0.96, 0.8). Every person at a uniform distance and direction (heading clockwise from +y), rounded to 0.1.

### Goal
Every person `saved`.

### Other
No metric (as the references). Solvable whenever a person lies outside the no-go zone; the boat can tack (headings 30° off the wind and beyond have positive speed).

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| boat fluents (polar, r, start) | identical in all 40 tasks | identical (`r` as a parameter) |
| person placement | opt: a diagonal sweep at distance 16.3–26.3; sat: distance 100 at multiples of 45° | uniform distance and direction; `angle_step=45` gives the sat pattern |

**Deviations:** the opt tasks move one person along a fixed diagonal line (x+0.4, y+0.4 per task); the generator draws positions at random instead. Sat coordinates are rounded to integers (71), ours to 0.1 (70.7).
