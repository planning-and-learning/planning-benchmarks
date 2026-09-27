# ferry (ipc_learning)

A ferry carries cars one at a time between locations.

## Source

- **Domain:** unknown (IPP collection); IPC 2023 learning-track typed encoding
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/ferry`), learning-track domain file; typed objects (`- location`, `- car`) instead of `location`/`car`/`not-eq` facts (the learning `sail` uses a negative precondition)
- **Reference tasks:** `data/classical/ipc2023-learning/ferry_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `ferry/ferry.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cars` | cars | 2–974 |
| `num_locations` | locations | 5–487 |

## Distribution

### Objects
`l0..`, `c0..`, typed.

### Initial state
Cars and the ferry at uniform locations; `empty-ferry`.

### Goal
Every car at a uniform location, possibly its start.

### Other
No action costs. Always solvable.

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| goal equals start | 0.000 | 0.072 |

**Deviations:**
- Goals may equal the start (7%); the learning tasks never do. Superset, frequency difference only.
