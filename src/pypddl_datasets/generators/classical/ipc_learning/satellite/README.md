# satellite (ipc_learning)

Satellites turn, calibrate instruments and take images.

## Source

- **Domain:** Maria Fox, Derek Long (IPC 2002); learning-track encoding with negative preconditions
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/satellite`), learning-track domain file; unchanged
- **Reference tasks:** `data/classical/ipc2023-learning/satellite_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `satellite/satellite.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_satellites` | satellites | 3–99 |
| `num_instruments` | instruments | 3–195 |
| `num_modes` | modes | 1–10 |
| `num_targets` | calibration targets | — |
| `num_observations` | observations | — |
| `pointing_goal_probability` | pointing goal per satellite | ~0.5 |
| `pointing_goal_may_hold` | pointing goal drawn over all directions incl. the current one (default, learning track); off: a different direction | on |

## Distribution

### Objects
Satellites, instruments, modes, directions (targets and observations).

### Initial state
Round-robin instruments over satellites, modes per instrument, calibration targets, random pointing.

### Goal
`have_image` goals, plus pointing goals with `pointing_goal_probability`, drawn over all directions (so a goal may already hold).

### Other
No action costs.

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| instruments per satellite | 1.664 | 1.664 |
| modes per instrument | 2.103 | 1.552 |
| pointing goals per satellite | 0.509 | 0.506 |
| tasks with a pointing goal already true | 0.383 | 0.333 (default) / 0.000 (option off) |

**Deviations:**
- Fewer modes per instrument (1.55 vs 2.10).
