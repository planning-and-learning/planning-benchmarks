# fo_counters (numeric/ipc)

Counters with controllable increment rates must be brought into strictly increasing order at minimal cost.

## Source

- **Domain:** FO-Counters by Enrico Scala and Dongxu Li (Li, Scala, Haslum and Bogomolov, IJCAI 2018); IPC 2023 numeric track
- **Generator:** reconstruction from the reference tasks (no generator published); every reference task starts all values and rates at 0, so the task is determined by the number of counters; Python generator in `generator.py`
- **Reference tasks:** `data/numeric/ipc2023/fo-counters`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_counters` | counters `c0..c{n-1}` | 2–21 |

## Distribution

### Objects
`c0..c{n-1}` of type `counter`.

### Initial state
`(= (max_int) 2n)`, `(value c_i) = 0`, `(rate_value c_i) = 0`, `(= (total-cost) 0)`.

### Goal
`(<= (+ (value c_i) 1) (value c_{i+1}))` for every `i < n-1`.

### Other
`(:metric minimize (total-cost))`; every action costs 1. Deterministic. Problem name `instance_<n>`.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| init and goal facts | 20 tasks | identical in 20/20 |
| metric | minimize total-cost | same |

**Deviations:** none found.
