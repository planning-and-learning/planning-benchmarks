# miconic (ipc_learning)

An elevator transports passengers between floors.

## Source

- **Domain:** Jana Koehler (AIPS-2000); learning-track typed encoding
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/miconic`), learning-track domain file; unchanged
- **Reference tasks:** `data/classical/ipc2023-learning/miconic_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `miconic/miconic.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_floors` | floors | 4–196 |
| `num_passengers` | passengers | 1–485 |
| `lift_start` | `random` (default, learning track) or `bottom` (lift at `f0`, the original) | random |

## Distribution

### Objects
Floors `f0..`, passengers `p0..`, typed.

### Initial state
`above` chain, uniform origin and a different destination per passenger, lift on a uniform floor (`lift_start="bottom"`: at `f0`).

### Goal
Every passenger served.

### Other
No action costs. Always solvable.

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator (default / `lift_start="bottom"`) |
|---|---|---|
| origin equals destination | 0.000 | 0.000 / 0.000 |
| lift starts at the bottom floor | 0.067 | 0.100 / 1.000 |

**Deviations:**
- None found.
