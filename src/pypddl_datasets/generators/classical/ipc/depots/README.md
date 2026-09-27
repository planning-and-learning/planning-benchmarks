# depots (ipc)

Trucks move crates between depots and distributors, and hoists stack the crates onto pallets and other crates.

## Source

- **Domain:** Derek Long and Maria Fox, IPC 2002 (untyped STRIPS encoding `depot`)
- **Generator:** `depots/depots.cc` (IPC 2002 generator, pddl-generators); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/depot`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_depots` (`-e`) | depots | 1-6 |
| `num_distributors` (`-i`) | distributors | 2-6 |
| `num_trucks` (`-t`) | trucks | 2-6 |
| `num_pallets` (`-p`) | pallets, raised to at least one per place | 3-20 |
| `num_hoists` (`-u`) | hoists, raised to at least one per place | 3-15 |
| `num_crates` (`-c`) | crates | 2-20 |
| `typed` (`--typed`) | typed encoding (Autoscale) instead of type predicates | IPC: untyped |

## Distribution

### Objects
Places `depot0..` then `distributor0..`, plus `truck*`, `pallet*`, `crate*` and `hoist*`. They are untyped, and type predicates (`place`, `truck`, `hoist`, `pallet`, `crate`, `surface`) are in the initial state. With `typed`, objects are typed and there are no type predicates.

### Initial state
- The first `#places` pallets and hoists sit one per place, in order. The rest are at uniformly random places.
- Trucks are at uniformly random places.
- Each crate is stacked on the current top of a uniformly random pallet's tower, at that pallet's place.
- `clear` is set on every tower top, and `available` on every hoist.

### Goal
- There are `2 * num_crates` draws of a uniformly random crate. A crate drawn for the first time is put on top of a uniformly random pallet's goal tower. Repeat draws are ignored, so some crates stay goal-free.
- A goal can equal the crate's current position.

### Other
- No action costs.
- Problem name `depot-{depots}-{distributors}-{trucks}-{pallets}-{hoists}-{crates}`; the domain is `depot`, or `depots` when typed.
- Always solvable, since any crate can be moved anywhere.

## Comparison with reference tasks

22 IPC tasks, each generated at its own object counts (10 seeds per task, mean totals):

| aspect | reference tasks | this generator |
|---|---|---|
| object counts (depots/distributors/trucks/pallets/hoists/crates) | 53 / 62 / 62 / 168 / 133 / 222 | identical |
| `pallet0` at `depot0`, every place has a pallet and a hoist | 22 / 22 | always |
| goal `on` facts | 189 | 190.4 |
| goal `on` a pallet | 113 | 107.9 |
| goal equals initial position | 10 | 13.2 |
| sum of max tower heights | 71 | 74.0 |
| type predicates / untyped objects | yes | yes |

**Deviations:**
- Problem names are `depot-...` instead of `depotprob{seed}`.
