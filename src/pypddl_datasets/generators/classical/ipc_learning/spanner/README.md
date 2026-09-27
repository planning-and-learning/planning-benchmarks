# spanner (ipc_learning)

A man picks up spanners along a corridor and tightens nuts at the gate.

## Source

- **Domain:** Amanda Coles, Andrew Coles, Maria Fox, Derek Long (IPC 2011); learning-track spelling `usable`
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/spanner`), learning-track domain file; `usable` instead of `useable`
- **Reference tasks:** `data/classical/ipc2023-learning/spanner_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `spanner/spanner.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_spanners` | spanners | 1–487 |
| `num_nuts` | nuts | 1–244 |
| `num_locations` | corridor locations | 4–99 |

## Distribution

### Objects
Man, spanners, nuts, shed, corridor locations, gate.

### Initial state
Link chain shed → corridor → gate; spanners uniform on the corridor, all usable; nuts loose at the gate.

### Goal
Every nut tightened.

### Other
No action costs. Solvable iff spanners ≥ nuts (not enforced).

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| links per location | 1.098 | 1.098 |
| spanner placement | corridor | corridor |

**Deviations:**
- None found.
