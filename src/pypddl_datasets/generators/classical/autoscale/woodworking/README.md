# woodworking (autoscale)

Boards are cut into parts, which are planed, ground, varnished or glazed and coloured on machines.

## Source

- **Domain:** IPC 2008 Woodworking (authors not named in the files), Autoscale's domain file, whose `cut-board` actions also delete the old `boardsize` (the IPC files in `../../ipc/woodworking` keep it); generated problems parse against both
- **Generator:** `pddl-generators/woodworking/create_woodworking_instance.py` as called by Autoscale: `create_woodworking_instance.py <wood_factor> <size> <num_machines> <seed>`; same distribution as `ipc/woodworking`, which this package re-exports
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/woodworking` (also `21.11-optimal-strips/woodworking`)

## Parameters

| parameter | meaning | reference range (`domains.py`; agile tasks) |
|---|---|---|
| `num_parts` | parts | 2–30 + slope 1–10; 2–150 |
| `num_machines` | machines per kind | 1, 2, 3; 2 and 3 |
| `wood_factor` | wood relative to demand | 1.0, 1.25, 1.5, 2.0; 1.25 and 2.0 |

## Distribution

### Objects
See `ipc/woodworking`.

### Initial state
See `ipc/woodworking`.

### Goal
See `ipc/woodworking`.

### Other
Action costs, `(:metric minimize (total-cost))`, name `wood-prob`.

## Comparison with reference tasks

All 30 agile tasks, 3 seeds each at their parameters.

| aspect | reference tasks | this generator |
|---|---|---|
| colours | 5.87 | 5.87 |
| wood types | 6.53 | 6.53 |
| boards | 30.6 | 30.6 |
| parts initially available | 0.57 | 0.58 |
| colour / wood / surface / treatment goals per part | 0.67 / 0.64 / 0.65 / 0.67 | 0.66 / 0.65 / 0.64 / 0.66 |

**Deviations:** none found.
