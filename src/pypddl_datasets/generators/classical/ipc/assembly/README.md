# assembly (ipc)

Assemble one goal item from a part-of tree, with resources, assemble and remove orders, and transient parts that are put in and taken out again.

## Source

- **Domain:** Drew McDermott, AIPS-1998 (ADL track)
- **Generator:** reconstruction from the IPC tasks; McDermott's generator is not public, and pddl-generators' `assembly.c` does not produce these tasks (different names, requires rate and order patterns), so no code is taken from it
- **Reference tasks:** `data/classical/downward-benchmarks/assembly` (30 tasks, `ipc-optimal-adl`, `ipc-satisficing-adl`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_parts` | parts of the goal assembly | 3–13 |
| `num_resources` | resources | 1–3 |
| `depth` | levels below the goal | 3 (one task 2) |
| `max_sons` | parts of a level-1 assembly (deeper: up to `max_sons // 2`) | 1–8 |
| `internal_probability`, `deep_internal_probability` | a level-1 / deeper part is itself assembled | 0.94 / 0.11 |
| `requires_probability` | a non-goal assembly requires a random resource | 0.84 |
| `order_probability` | assemble order per pair of siblings | 0.18 |
| `transient_probability` | transient relation per candidate (part, whole one level up) pair | 0.009 |
| `tool_probability` | one extra free tool used as a transient part | 1/30 |

## Distribution

### Objects
Assemblies named from IPC's word pool (`bracket`, `frob`, `widget`, …; `-<n>` suffixes beyond the pool) and resources from IPC's tool pool (`charger`, `pliers`, …).

### Initial state
- `part-of` tree: the goal has `num_parts` parts; level-1 parts are assembled with 0.94 (1..`max_sons` parts), deeper ones with 0.11; level `depth` holds base parts.
- `available` for every base part, the tool (if any) and every resource; `requires` for non-goal assemblies with 0.84.
- `assemble-order` between siblings with 0.18 per pair, consistent with one random order per whole.
- Transient part `t` of a whole `W` one level above `t` (not `t`'s own whole `P`): `(transient-part t W)`, `(assemble-order t x W)` and `(remove-order x t W)` for a random part `x` of `W`, `(assemble-order t x P)`, with 0.37 a second `x` and with 0.35 a part of `W` ordered before `t` — the patterns of the IPC tasks.

### Goal
`(complete <goal>)`.

### Other
No costs. Every whole's order graph is acyclic: a transient whose orders would close a cycle (possible when two transients cross) is dropped, so every task is solvable (checked by a breadth-first search over the domain semantics in the test).

## Comparison with reference tasks

All 30 IPC tasks, each regenerated at its own `num_parts`, `num_resources` and depth (20 seeds):

| aspect | reference tasks | this generator |
|---|---|---|
| assemblies | 45.9 | 42.6 |
| assembled (non-base) items | 12.1 | 11.7 |
| parts per assembled item | 3.68 | 3.57 |
| requires rate (non-goal assemblies) | 0.84 | 0.84 |
| transient parts | 2.30 | 1.90 |
| remove orders | 2.40 | 1.90 |
| sibling order density | 0.176 | 0.186 |
| assemble orders | 23.0 | 20.6 |
| tools | 0.03 | 0.04 |

**Deviations:**
- 17 of about 800 order facts in the IPC tasks follow none of the patterns above (e.g. orders between parts of different wholes); they are not generated.
- Slightly fewer transient parts (1.90 vs 2.30), partly from dropping cycle-closing transients.
