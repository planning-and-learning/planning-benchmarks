# pipesworld_tankage (ipc)

Batches of oil derivatives move through a fixed pipeline network: pushing a batch into a full pipe pushes the batch at its other end out. Some products may not touch inside a pipe, and every area stores each product in a limited number of tank slots.

## Source

- **Domain:** Frederico Liporace and Jörg Hoffmann, IPC 2004 (credited on the [IPC-4 domain page](https://ipc04.icaps-conference.org/deterministic/domains.html); the domain file names no author); `domain.pddl` is the split (push/pop start/end) STRIPS version used by the IPC tasks, lowercased. `domain-nosplit.pddl` is not included.
- **Generator:** the IPC generator is not public; `generator.py` is a reconstruction from the IPC tasks
- **Reference tasks:** `data/classical/downward-benchmarks/pipesworld-tankage` (50 tasks, parameters in the names `pNN-netN-bB-gG-tT`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `network` | one of the five IPC networks (below) | 1–5 |
| `num_batches` | batches; must exceed the pipe capacity of the network | net1 6–14, net2 10–18, net3 12–20, net4 14–22, net5 22–30 |
| `num_goals` | batches with a goal area; at most `num_batches` − pipe capacity | 2–8 |
| `tankage` | tank slots in percent (1–100; default 50); `None` emits a notankage task, see `../pipesworld_notankage` | 20–90 |

## Distribution

### Objects
`b0..` (batch-atom), `a1..aA` (area), pipes `s<from><to>`, tank slots `ta<area>-<k>-<product>`. Products are the domain constants `lco gasoleo rat-a oca1 oc1b`.

### Initial state
- Networks (pipe: batches it holds), as in the IPC tasks: net1 `s12:1 s13:1`; net2 `s12:2 s13:2`; net3 net2 + `s34:1`; net4 net3 + `s23:3`; net5 net4 + `s15:4`. Pipes of length 1 are `unitary`, all others `not-unitary`; every pipe is `normal`.
- `may-interface` for all product pairs except rat-a with oca1 or oc1b (both orders), as in every IPC task.
- Every batch gets a uniform product. A uniform shuffle fills the pipes (`first`/`follow`/`last`); the remaining batches are `on` uniform areas. Adjacent batches in a pipe may be incompatible, as in the IPC tasks.
- Tank slots: each area gets, for each product present in the task, max(round-half-up(`tankage`% × batches of that product), batches of that product it holds initially) slots; held slots are `occupied`, the rest `not-occupied`. This rule reproduces all 50 IPC tasks exactly.

### Goal
A random walk of complete push/pop moves (respecting `may-interface` and free tank slots) runs 50 moves per batch, longer if fewer than `num_goals` batches have left their start. `num_goals` uniform batches among those that end at an area other than their start get `(on b a)` for that area; plus `(normal s)` for every pipe, as in the IPC tasks.

### Other
No action costs. Problem name `pipesworld-net<N>-b<B>-g<G>-t<T>`. Every task is solvable (the walk is a plan). A start whose walk gets stuck is redrawn; after 100 redraws `make_problem` raises `ValueError` (only for very tight tankage with many goals, e.g. net1, 14 batches, 12 goals, 20 %).

## Comparison with reference tasks

All 50 IPC tasks regenerated at the parameters in their names (5 seeds each, 250 tasks):

| aspect | reference tasks | this generator |
|---|---|---|
| networks, pipe lengths, unitary pipes | identical | identical |
| `may-interface` facts | 21, same set | same |
| tank-slot rule | 50/50 | by construction |
| tank slots per task | 41.6 | 41.3 |
| occupied share of tank slots | 0.255 | 0.256 |
| distinct products per task | 4.74 | 4.80 |
| incompatible adjacent pairs in pipes | 0.12 | 0.16 |
| goal batches initially in a pipe | 0.34 | 0.44 |
| mean hops from start area to goal area | 1.42 | 1.39 |
| goal at the start area | 0 | 0 |
| solved by LAMA-first (Fast Downward) | — | 18/18 small tasks tried |

**Deviations:**
- Goals come from a random walk (guaranteed solvable) rather than the IPC procedure; the IPC goals look like uniform batches sent to uniform other areas. The walk favours batches that start in a pipe (0.44 vs 0.34), because batches starting at an area are ineligible when they return home.
- Only the five IPC networks; larger tasks grow by batches and goals only.
- The IPC tankage and notankage tasks share initial states and goals; here they share the start (same seed) but the goals differ, since the walk respects tank slots.
- Batch names are listed in index order; IPC lists them shuffled. Problem names encode the parameters.
