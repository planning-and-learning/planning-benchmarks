# pipesworld_notankage (ipc)

Batches of oil derivatives move through a fixed pipeline network: pushing a batch into a full pipe pushes the batch at its other end out. Some products may not touch inside a pipe; areas store any number of batches.

## Source

- **Domain:** Frederico Liporace and Jörg Hoffmann, IPC 2004 (credited on the [IPC-4 domain page](https://ipc04.icaps-conference.org/deterministic/domains.html); the domain file names no author); split STRIPS version, lowercased
- **Generator:** the IPC generator is not public; re-exports the reconstruction in `../pipesworld_tankage` with `tankage=None`
- **Reference tasks:** `data/classical/downward-benchmarks/pipesworld-notankage` (50 tasks, parameters in the names `pNN-netN-bB-gG`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `network` | one of the five IPC networks | 1–5 |
| `num_batches` | batches; must exceed the pipe capacity of the network | net1 6–14, net2 10–18, net3 12–20, net4 14–22, net5 22–30 |
| `num_goals` | batches with a goal area; at most `num_batches` − pipe capacity | 2–8 |

## Distribution

### Objects
As in `../pipesworld_tankage`, without tank slots.

### Initial state
As in `../pipesworld_tankage` (networks, `may-interface`, uniform products, uniform pipe filling and area placement), without tank slots.

### Goal
`num_goals` batches at the areas a random walk of 50 push/pop moves per batch takes them to (never their start). No `normal` goals, as in the IPC tasks.

### Other
No action costs. Problem name `pipesworld-net<N>-b<B>-g<G>`. Every task is solvable.

## Comparison with reference tasks

All 50 IPC tasks regenerated at the parameters in their names (5 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| networks, pipe lengths, unitary pipes, `may-interface` | identical | identical |
| distinct products per task | 4.74 | 4.80 |
| incompatible adjacent pairs in pipes | 0.12 | 0.16 |
| goal batches initially in a pipe | 0.34 | 0.42 |
| mean hops from start area to goal area | 1.42 | 1.41 |
| goal at the start area | 0 | 0 |
| solved by LAMA-first (Fast Downward) | — | 17/17 small tasks tried |

**Deviations:** as in `../pipesworld_tankage`: random-walk goals favour batches that start in a pipe (0.42 vs 0.34); only the five IPC networks; batch names in index order.
