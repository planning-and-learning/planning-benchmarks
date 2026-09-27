# block_grouping (numeric/ipc)

Coloured blocks on a grid must be grouped: blocks share a cell exactly when they share a colour.

## Source

- **Domain:** Enrico Scala and Miquel Ramirez (Scala et al., JAIR 2020; IPC 2023 numeric track)
- **Generator:** reconstruction from the reference tasks (no generator was published)
- **Reference tasks:** `data/numeric/ipc2023/block-grouping`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `size` | grid side (coordinates 1..size) | 5–100 |
| `num_blocks` | blocks | 5–40 |
| `num_colours` | colours | 2–10 |

## Distribution

### Objects
Blocks `b1 .. b<n>`.

### Initial state
- Every block at a uniformly random cell `x, y` in 1..size (blocks may share a cell).
- Bounds `min_x = min_y = 1`, `max_x = max_y = size`.

### Goal
Every block gets a uniformly random colour (a colour may stay unused). For every block pair (in name order): `(= (x a) (x b))` and `(= (y a) (y b))` if they share a colour, otherwise `(or (not (= (x a) (x b))) (not (= (y a) (y b))))`.

### Other
The problem declares `:disjunctive-preconditions :negative-preconditions` whenever the goal has a disjunction (strict PDDL rejects them otherwise). No metric. Problem name `instance_<size>_<blocks>_<colours>_<seed>`, as in the reference tasks. Solvable whenever `num_colours <= size * size`.

## Comparison with reference tasks

Every reference task regenerated at the parameters in its name (10 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| blocks sharing a start cell (mean) | 1.55 | 1.57 |
| same-colour pairs (mean) | 45.3 | 43.9 |
| different-colour pairs (mean) | 252.0 | 253.3 |

**Deviations:** none found.
