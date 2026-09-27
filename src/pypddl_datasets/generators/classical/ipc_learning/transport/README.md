# transport (ipc_learning)

Vehicles with capacities deliver packages over roads.

## Source

- **Domain:** IPC 2008; learning-track cost-free encoding (`size` type)
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/transport`), learning-track domain file; unchanged
- **Reference tasks:** `data/classical/ipc2023-learning/transport_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `transport/transport.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | locations | 5–99 |
| `num_trucks` | vehicles | 3–50 |
| `num_packages` | packages | 1–194 |
| `capacity` | maximum vehicle capacity | 2–10 |
| `extra_edges` | roads beyond a spanning tree; default `None` draws the edge count uniformly between a tree and the complete graph (learning track's `random_connected_graph`) | — |
| `random_capacities` | each vehicle's capacity uniform in 1..`capacity` (default, learning track); off: all at `capacity` | on |

## Distribution

### Objects
`l0..`, `t0..`, `p0..`, sizes `capacity0..`.

### Initial state
Random spanning tree plus extra roads (both directions): by default a uniform number between none and the complete graph. Vehicles at uniform locations, capacity uniform in 1..max.

### Goal
Every package at another location.

### Other
No action costs. Always solvable.

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| roads per location | 9.93 | 10.05 (default) / 1.85 (`extra_edges=0`) |
| vehicle capacity / max | 0.697 | 0.685 (default) / 1.000 (`random_capacities=False`) |
| goal equals start | 0.000 | 0.000 |

**Deviations:**
- None found.
