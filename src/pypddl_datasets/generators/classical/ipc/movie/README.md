# movie (ipc)

Get one snack of each of five kinds, rewind the movie and reset the counter.

## Source

- **Domain:** Corin Anderson, AIPS-1998 competition
- **Generator:** pddl-generators `movie/movie.c` (FF domain collection, Jörg Hoffmann); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/movie`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_snacks` | objects per snack kind (chips, dip, pop, cheese, crackers) | 5–34 (`probNN` uses NN + 4) |

## Distribution

### Objects
`5 * num_snacks` untyped objects: `c1..cN` (chips), `d1..dN` (dip), `p1..pN` (pop), `z1..zN` (cheese), `k1..kN` (crackers), listed per kind in descending order as in the IPC tasks.

### Initial state
Fixed: one kind fact per object (`(chips c1)`, ...) and `(counter-at-other-than-two-hours)`. No randomness.

### Goal
Fixed: `movie-rewound`, `counter-at-zero` and `have-<kind>` for all five kinds.

### Other
No action costs. Problem name `strips-movie-<num_snacks>` (IPC: `strips-movie-x-<index>`). Every task is solvable (7-step plan).

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| init and goal fact sets, prob01–prob30 | — | identical for all 30 with `num_snacks = index + 4` |
| objects | 5 × (index + 4) | 5 × `num_snacks` |

**Deviations:**
- Problem name encodes `num_snacks` instead of the IPC index.
