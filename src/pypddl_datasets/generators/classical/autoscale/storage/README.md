# storage (autoscale)

Hoists move crates from containers into grid-shaped depots.

## Source

- **Domain:** Alfonso Gerevini and Alessandro Saetti, IPC 2006 (Storage-Propositional)
- **Generator:** `storage/main.cpp` by Alfonso Gerevini and Alessandro Saetti, called as `storage -p 01 -o {containers} -e {seed} -c {crates} -n {hoists} -s {store_areas} -d {depots}`; re-exports `ipc/storage` (same distribution, Autoscale's domain file)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/storage` (also `21.11-optimal-strips/storage`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_crates` | crates | 4–27 |
| `num_hoists` | hoists | 6–50 |
| `num_store_areas` | store areas; Autoscale adds max(depots, hoists, crates) | 15–156 |
| `num_depots` | depots (Autoscale caps at 36) | 2–21 |
| `num_containers` | containers; the default is ⌈crates/4⌉ | ⌈crates/4⌉ |

## Distribution

### Objects
Near-square depots of store areas, container areas, containers, `loadarea`, and transit areas. See `ipc/storage`.

### Initial state
- Depot grids connected to `loadarea`.
- Each adjacent depot pair is joined by a transit area with probability ½.
- Hoists on distinct random depot areas; crates in containers (4 per container).

### Goal
All crates in depots, spread with at least one per depot while crates remain.

### Other
- No action costs.
- The problem is named `storage-c<C>-h<H>-s<S>-d<D>-o<K>`, where the agile tasks all use `storage-1`.
- Always solvable.

## Comparison with reference tasks

All 30 agile tasks, regenerated at their own counts:

| aspect | reference tasks | this generator |
|---|---|---|
| transit areas (by depot count) | 1 + Binomial(D−1, ½), for example D=21: 12 and D=4: 1–4 | same rule, for example D=21: 12 and D=4: 2 |
| object counts, crate placement, goals | — | same structure |

**Deviations:**
- None in distribution.
- Naming differs.
