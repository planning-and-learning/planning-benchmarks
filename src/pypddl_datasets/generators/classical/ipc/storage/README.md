# storage (ipc)

Hoists move crates from containers into grid-shaped depots.

## Source

- **Domain:** Alfonso Gerevini and Alessandro Saetti, IPC 2006 (Storage-Propositional)
- **Generator:** `storage/main.cpp` by Alfonso Gerevini and Alessandro Saetti, Storage-Propositional square-depot path only; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/storage`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_crates` | crates | 1–20 |
| `num_hoists` | hoists | 1–5 |
| `num_store_areas` | store areas over all depots | 1–40 (2 × crates from task 4 on) |
| `num_depots` | depots | 1–5 |
| `num_containers` | containers; the default is ⌈crates/4⌉ | 1–5 |

## Distribution

### Objects
- Store areas `depotD-R-C`, split roughly evenly over depots (±10% deviation).
- Each depot is a near-square grid with its door on the last row.
- Container areas `container-K-J`, containers, depots, `loadarea`, and transit areas.

### Initial state
- Grid adjacency inside depots. Each depot door connects to `loadarea`.
- Adjacent depots are joined by a transit area with probability ½ each.
- Hoists start on distinct random store areas of random depots; the other areas are `clear`.
- Crates start in containers, 4 per container, with the last container taking the rest.

### Goal
- Every crate must be `in` a depot.
- They are spread with at least one crate per depot while crates remain, over two passes with halving.

### Other
- No action costs.
- The problem is named `storage-c<C>-h<H>-s<S>-d<D>-o<K>`.
- Upstream's ASCII depot map comment is dropped.
- Always solvable: every depot is reachable through `loadarea`.

## Comparison with reference tasks

All 30 IPC tasks, regenerated at their own crate, hoist, area, depot and container counts:

| aspect | reference tasks | this generator |
|---|---|---|
| object counts per type, goals, hoist placement, clear facts | — | equal in all 30 |
| transit areas, D=1 (12 tasks) | 1 | 1 |
| transit areas, D ≥ 2 (18 tasks) | always 2 (load area plus one transit area) | 1 + Binomial(D−1, ½): mean 1.47 (D=2), 1.94 (D=3), 2.48 (D=4), 2.99 (D=5) |
| depot shapes and area split | for example [6, 6, 8] areas | 3 of 30 tasks differ (random ±10% split) |
| names | `storage-N` | `storage-c…-h…-s…-d…-o…` |

**Deviations:**
- With 2 or more depots, the IPC 2006 tasks always contain exactly one transit area between depots. Ours joins each adjacent pair independently with probability ½. That changes the `connected` facts, for example 34 against 32 in task 15.
- Autoscale's storage tasks do follow the ½ rule: 21 depots give 12 transit areas in both.
- Naming differs.
