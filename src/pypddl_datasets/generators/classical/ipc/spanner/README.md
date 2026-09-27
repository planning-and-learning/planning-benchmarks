# spanner (ipc)

A man walks a one-way corridor from the shed to the gate, collecting single-use spanners to tighten nuts.

## Source

- **Domain:** Amanda Coles, Andrew Coles, Maria Fox and Derek Long, IPC 2011 learning track
- **Generator:** port of `pddl-generators/spanner/spanner-generator.py`; Python port in `generator.py`
- **Reference tasks:** `data/classical/ipc2023-learning/spanner_ipc2023_learning` (predicate `usable`), `data/classical/tests/spanner` (same domain file as ours)

## Parameters

| parameter | meaning | reference range (IPC 2023 learning) |
|---|---|---|
| `num_spanners` | spanners | 1–88 (1.0–2.0 × nuts, mostly 2×) |
| `num_nuts` | nuts | 1–49 |
| `num_locations` | corridor locations between shed and gate | 4–44 |

## Distribution

### Objects
`bob` (man), `spanner1..`, `nut1..`, `location1..`, `shed`, `gate`.

### Initial state
- `bob` at `shed`; every spanner at a uniform corridor location and `useable`; every nut `loose` at `gate`.
- `link` chain `shed → location1 → … → locationN → gate`.

### Goal
`tightened` for every nut.

### Other
No costs or metric. Name `prob` (configurable). Solvable iff `num_spanners ≥ num_nuts`, which the generator does not enforce.

## Comparison with reference tasks

IPC 2023 learning track, 90 tasks.

| aspect | reference tasks | this generator |
|---|---|---|
| spanner locations | uniform (5353 in first half, 5382 in second) | uniform |
| corridor | chain shed → locations → gate | same |
| spanners / nuts | 2.0 in 50 tasks, 1.0–1.9 in 40 | free parameter |
| predicate | `usable` | `useable` (IPC 2011 domain) |
| problem name | `spanner-01` | `prob` |

**Deviations:** none found in the distribution; only the predicate spelling (domain version) and naming differ.
