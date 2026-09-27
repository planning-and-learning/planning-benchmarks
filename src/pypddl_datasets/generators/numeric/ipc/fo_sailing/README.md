# fo_sailing (numeric/ipc)

Sailing with a controllable speed per boat: boats accelerate to move farther and must slow down to rescue.

## Source

- **Domain:** FO-Sailing (`sailing_ln`) by Enrico Scala and Dongxu Li (Li, Scala, Haslum and Bogomolov, IJCAI 2018); IPC 2023 numeric track
- **Generator:** `numeric/ipc/sailing` (port of `sailing/generate_saving.py`, Enrico Scala) with `(= (v b) 1)` per boat; Python generator in `generator.py`
- **Reference tasks:** `data/numeric/ipc2023/fo-sailing`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_boats` | boats | 1–5 |
| `num_people` | people to rescue | 1–4 |
| `max_distance` | bound on \|d\| | 500 |
| `nonnegative_distances` | draw `d` from `0..max_distance` (upstream's active line) | the 4 five-boat tasks |
| `seed` | RNG seed | 1229 |

## Distribution

### Objects
`b0..` of type `boat`, `p0..` of type `person`.

### Initial state
As `numeric/ipc/sailing`, plus `(= (v b) 1)` for every boat.

### Goal
`(saved p)` for every person.

### Other
No action costs or metric. Always solvable. Problem name `instance_<boats>_<people>_<seed>`.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| init and goal facts (signed distances) | 16 tasks | identical in 16/16 |
| 5-boat tasks: `d` range | 26–140 (all ≥ 0) | 0..500 with `nonnegative_distances` |

**Deviations:** the 4 five-boat reference tasks draw nonnegative distances from a stream we cannot reproduce (not upstream seed 1229); their structure is covered by `nonnegative_distances=True`.
