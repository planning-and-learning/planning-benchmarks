# sailing (numeric/ipc)

Sailing boats move on an unbounded plane, with wind-dependent speeds, to rescue people.

## Source

- **Domain:** Sailing by Enrico Scala and Miquel Ramirez (Scala, Haslum, Thiébaux and Ramirez, JAIR 2020); IPC 2023 numeric track
- **Generator:** port of `sailing/generate_saving.py` (Enrico Scala) from [hstairs/planning-numeric-domains-generators](https://github.com/hstairs/planning-numeric-domains-generators); the reference tasks use upstream's commented-out signed distance line; Python port in `generator.py`
- **Reference tasks:** `data/numeric/ipc2023/sailing`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_boats` | boats | 1–4 |
| `num_people` | people to rescue | 1–10 |
| `max_distance` | bound on \|d\| | 500 |
| `nonnegative_distances` | draw `d` from `0..max_distance` | not used |
| `seed` | RNG seed | 1229 |

## Distribution

### Objects
`b0..` of type `boat`, `p0..` of type `person`.

### Initial state
- People first: `(d p)` uniform in `-max_distance..max_distance` (negative values occur, see `data/numeric/ipc2023/README.md`).
- Then boats: `(x b)` uniform in `-10..10`, `(y b) = 0`.

### Goal
`(saved p)` for every person.

### Other
No action costs or metric. Always solvable (the plane is unbounded). Problem name `instance_<boats>_<people>_<seed>`, like upstream.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| init and goal facts at the name's parameters and seed | 20 tasks | identical in 20/20 |
| `d` range | −394..483 | −500..500 |

**Deviations:** none found.
