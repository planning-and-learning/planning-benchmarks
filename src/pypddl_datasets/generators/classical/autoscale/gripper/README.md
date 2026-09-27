# gripper (autoscale)

A robot with two grippers carries balls from room A to room B.

## Source

- **Domain:** Jana Koehler, AIPS-1998 competition (same domain file as the IPC)
- **Generator:** `gripper/gripper.c` ((C) 2001 Albert Ludwigs University Freiburg), called by Autoscale as `gripper -n {n}`; `generator.py` re-exports `../../ipc/gripper`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/gripper`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/gripper`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_balls` (`-n`) | number of balls | agile: 20-165 (Autoscale: linear, base 8-20) |

## Distribution

### Objects
The same as `ipc/gripper`: `rooma`, `roomb`, `left`, `right`, and `ball1..ball{n}`.

### Initial state
The same as `ipc/gripper`: fixed. All balls and the robot are in `rooma`, and both grippers are free.

### Goal
Every ball is in `roomb`.

### Other
No action costs. Problem name `gripper-{n}`, as in Autoscale. Deterministic and always solvable.

## Comparison with reference tasks

| aspect | reference tasks (30 agile) | this generator |
|---|---|---|
| objects | 2895 | 2895 |
| init facts per predicate (`at`, `ball`, `free`, `gripper`, `room`, `at-robby`) | 2775, 2775, 60, 60, 60, 30 | identical |
| goal `at` | 2775 | 2775 |
| problem names | `gripper-{n}` | identical |

**Deviations:** none found.
