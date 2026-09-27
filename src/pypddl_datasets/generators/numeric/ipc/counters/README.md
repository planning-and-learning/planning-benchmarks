# counters (numeric/ipc)

Integer counters, each incremented or decremented by one, must be brought into strictly increasing order.

## Source

- **Domain:** Counters by Guillem Francès and Hector Geffner (F-Strips, ICAPS 2015), numeric version by Enrico Scala and Miquel Ramirez (JAIR 2020); IPC 2023 numeric track
- **Generator:** reconstruction from the reference tasks. The only published helper, `counters/make_int_goals.py` in [hstairs/planning-numeric-domains-generators](https://github.com/hstairs/planning-numeric-domains-generators), rewrites goals and does not sample; Python generator in `generator.py`
- **Reference tasks:** `data/numeric/ipc2023/counters`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_counters` | counters `c0..c{n-1}` | 4–40 |
| `init` | `zero`, `reverse` or `random` initial values | 3 / 4 / 13 tasks |
| `seed` | RNG seed (`random` only) | — |

## Distribution

### Objects
`c0..c{n-1}` of type `counter`.

### Initial state
- `(= (max_int) 2n)`.
- `(value c_i)`: all 0 (`zero`), `2(n-1-i)` (`reverse`), or uniform in `0..2n-1` (`random`).

### Goal
`(<= (+ (value c_i) 1) (value c_{i+1}))` for every `i < n-1`: a numeric chain condition, no propositional goals.

### Other
No action costs or metric. Always solvable (`max_int = 2n` leaves room for `0, 1, ..., n-1`). Problem name `instance_<n>_<init>`.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| `zero` / `reverse` tasks | 3 / 4 | identical (all 7) |
| `random` value / max_int, mean | 0.498 | 0.495 |
| `random` value / max_int, max | 0.988 | 0.988 |
| `max_int` | 2n | 2n |

**Deviations:** none found; problem names differ (`instance_<n>_<k>` in IPC).
