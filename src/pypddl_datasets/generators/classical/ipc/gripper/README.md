# gripper (ipc)

A robot with two grippers carries balls from room A to room B.

## Source

- **Domain:** Jana Koehler, AIPS-1998 competition (untyped STRIPS)
- **Generator:** `gripper/gripper.c` from the FF domain collection / pddl-generators, (C) 2001 Albert Ludwigs University Freiburg; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/gripper`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_balls` (`-n`) | number of balls | 4-42 (step 2, 20 tasks) |

## Distribution

### Objects
`rooma`, `roomb`, grippers `left` and `right`, balls `ball1`..`ball{num_balls}`, all untyped.

### Initial state
Fixed: `(room rooma)`, `(room roomb)`, `(gripper left)`, `(gripper right)`, `(ball b)` and `(at b rooma)` for every ball, `(free left)`, `(free right)`, `(at-robby rooma)`. No randomness.

### Goal
`(at b roomb)` for every ball.

### Other
No action costs, no metric. Problem name `gripper-{num_balls}`. Always solvable. Deterministic: there is no seed.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| init/goal fact sets at the same ball count | 20 tasks | identical in all 20 |
| objects per task | `num_balls + 4` | `num_balls + 4` |
| metric | none | none |

**Deviations:**
- Problem names are `gripper-N` instead of `strips-gripper-x-K`.
