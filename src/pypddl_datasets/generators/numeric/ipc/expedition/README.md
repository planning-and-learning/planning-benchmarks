# expedition (numeric/ipc)

Sleds follow chains of waypoints; moving costs one unit of supplies, and sleds can store and retrieve supplies at waypoints.

## Source

- **Domain:** Joan Espasa Arxer, based on the expedition domain by Ben Pathak (IPC 2023 numeric track; reused unchanged in IPC 2026)
- **Generator:** reconstruction from the reference tasks (no generator was published); the tasks are fully determined by chain length and layout, and this generator reproduces all of them
- **Reference tasks:** `data/numeric/ipc2023/expedition`, `data/numeric/ipc2026/expedition` (identical tasks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_waypoints` | waypoints per chain | 6–19 |
| `num_sleds` | sleds | 2 |
| `separate_tracks` | one chain and depot per sled instead of one shared chain | both |
| `capacity`, `initial_supplies`, `depot_supplies` | sled capacity, sled start supplies, supplies at each chain's first waypoint | 4, 1, 1000 |

## Distribution

### Objects
Sleds `s0, s1, ...`; waypoints `wa0 ..` (and `wb0 ..`, ... with separate tracks).

### Initial state
- Every sled at the first waypoint of its chain with `sled_capacity` and `sled_supplies`.
- `waypoint_supplies` is `depot_supplies` at each chain's first waypoint and 0 elsewhere; `is_next` links consecutive waypoints.

### Goal
Every sled at the last waypoint of its chain.

### Other
Deterministic, no metric. Problem name `instance_<sleds>_sled_<num_waypoints - 5>`, as in the reference tasks. Solvable by depot relays (supplies are plentiful at the depot).

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| tasks reproduced as init/goal fact sets (2023 / 2026) | 20 / 20 | 20 / 20 |

**Deviations:** none found (one reference task lists sled `s1`'s facts in a different order).
