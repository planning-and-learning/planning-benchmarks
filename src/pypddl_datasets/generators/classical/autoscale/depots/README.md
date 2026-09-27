# depots (autoscale)

Trucks move crates between depots and distributors, and hoists stack the crates onto pallets and other crates.

## Source

- **Domain:** Derek Long and Maria Fox, IPC 2002, typed STRIPS encoding `depots` (IPC uses the untyped `depot` encoding)
- **Generator:** `depots/depots.cc`, called by Autoscale as `depots -e .. -i .. -t .. -p .. -h .. -c .. -s {seed}`; `generator.py` calls `../../ipc/depots` with `typed=True`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/depots`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/depots`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_depots` | depots | agile: 9-142 |
| `num_distributors` | distributors | agile: 2 |
| `num_trucks` | trucks | agile: 2 |
| `num_pallets` | pallets (raised to at least one per place) | agile: 16-144 |
| `num_hoists` | hoists (raised to at least one per place) | agile: 11-144 |
| `num_crates` | crates | agile: 3-43 |

## Distribution

### Objects
The same as `ipc/depots`, but typed: `depot`, `distributor`, `truck`, `pallet`, `crate`, `hoist`. There are no type predicates.

### Initial state
The same as `ipc/depots`: one pallet and one hoist per place, extras at random places, and crates stacked on random pallets.

### Goal
There are `2 * num_crates` random crate draws. A crate drawn for the first time goes on a random pallet's goal tower, and repeat draws are skipped.

### Other
No action costs. Problem name `depot-{depots}-{distributors}-{trucks}-{pallets}-{hoists}-{crates}`, the same scheme as Autoscale. Always solvable.

## Comparison with reference tasks

30 agile tasks, each generated at its own parameters (1 seed):

| aspect | reference tasks | this generator |
|---|---|---|
| typed objects (depot/distributor/truck/pallet/hoist/crate) | 2256 / 60 / 60 / 2323 / 2316 / 684 | identical |
| init `at` / `available` / `clear` / `on` | 5383 / 2316 / 2323 / 684 | identical |
| goal `on` | 592 | 582 |

**Deviations:** none found. The goal count depends on the random draws and is within noise.
