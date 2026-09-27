# ferry (ipc)

A ferry carrying one car at a time moves cars between locations.

## Source

- **Domain:** origin unknown; taken from the IPP domain collection, sail restricted to distinct locations (not-eq facts); untyped STRIPS
- **Generator:** port of `pddl-generators/ferry/ferry.c` (© 2001 Albert Ludwigs University Freiburg); Python port in `generator.py`
- **Reference tasks:** `data/classical/ipc2023-learning/ferry_ipc2023_learning` (typed domain, same actions), `data/classical/tests/ferry`

## Parameters

| parameter | meaning | reference range (IPC 2023 learning) |
|---|---|---|
| `num_cars` | cars | 2–974 |
| `num_locations` | locations | 5–487 (about cars/2) |

## Distribution

### Objects
Untyped `l0..`, `c0..`.

### Initial state
- Type predicates `location`, `car`; `not-eq` for every ordered pair of distinct locations.
- `empty-ferry`; every car at a uniform location; ferry at a uniform location.

### Goal
Every car at a uniform location (may equal its start).

### Other
No costs or metric. Name `ferry-l<L>-c<C>`. Always solvable.

## Comparison with reference tasks

IPC 2023 learning track, 90 tasks.

| aspect | reference tasks | this generator |
|---|---|---|
| encoding | typed (`car`, `location`), negative preconditions | untyped, type predicates and `not-eq` facts |
| car start | uniform | uniform |
| ferry start | uniform (7/90 at `loc1`) | uniform |
| goal equals start | 0 of 19527 cars | probability 1/`num_locations` per car |
| names | `car1`, `loc1`; problem `ferry-01` | `c0`, `l0`; problem `ferry-l…` |

**Deviations:**
- Goals: the learning-track tasks never keep a car at its start; here a car's goal is its start with probability 1/L (20 % at L=5).
- Encoding differs (untyped IPP domain vs. the learning track's typed domain); `tests/ferry` uses the typed domain as well.
