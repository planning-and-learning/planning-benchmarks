# openstacks (ipc)

Orders are started and shipped once all their products are made, minimizing the number of simultaneously open stacks.

## Source

- **Domain:** Patrik Haslum (IPC 2006 "Openstacks Propositional", strips forced sequential version, `domain_openstacks06.pddl`) and its IPC 2008 ADL version with action costs (`domain.pddl`); instances of IPC 2006 from the 2005 Constraint Modelling Challenge (Barbara Smith, Ian Gent)
- **Generator:** port of `pddl-generators/openstacks/generator.py` (matrix sampling after Ioannis Refanidis's `generate_problems`), written for the lifted ADL encodings; the per-task grounded domain upstream writes is not produced
- **Reference tasks:** `data/classical/downward-benchmarks/openstacks-{opt,sat}08-adl` (identical domain file, `style="08"`) and `data/classical/downward-benchmarks/openstacks` (`style="06"`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_products`, `num_orders` | matrix size | 5–80 (square) |
| `density` | upstream density parameter (`clustered`) or percentage of ones (`uniform`) | 2008: ≈ 5–30 (clustered); 2006: 7–68 % (uniform) |
| `style` | `08` (IPC 2008 ADL, cost metric) or `06` (IPC 2006, `machine-available`, no metric) | — |
| `model` | `clustered` (upstream) or `uniform` (iid, reaches dense Challenge matrices) | — |
| `shuffle` | permute orders and products (the IPC matrices are shuffled) | — |

## Distribution

### Objects
Counts `n0 … n<max(orders, products)>`, orders `o<i>`, products `p<i>`.

### Initial state
- `next-count` chain, `(stacks-avail n0)`, every order `waiting`; `style="06"` adds `(machine-available)`, `style="08"` adds `(= (total-cost) 0)`.
- `includes`: `clustered` includes pair (o, p) with upstream's normal-density weight around the diagonal (every pair has probability ≥ 1/100, so every matrix is possible); `uniform` includes each pair with probability density/100. Empty orders get a uniform product and unused products a uniform order; then orders and products are permuted.

### Goal
Every order `shipped`.

### Other
`style="08"`: `(:metric minimize (total-cost))`, opening a stack costs 1. Always solvable.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| 2008: density at n = 5 / 30 / 80 | 0.280 / 0.056 / 0.032 | 0.268 / 0.056 / 0.033 (density 5 / 23 / 29) |
| 2008: mean \|o − p\| at n = 30 / 80 | 7.9 / 23.7 | 10.1 / 26.8 |
| 2006: density (all 30 tasks, `uniform` at each task's density) | 0.276 | 0.282 |
| 2006: mean \|o − p\| | 10.95 | 10.97 |
| init and goal predicates, objects per type | — | identical kinds and counts |

**Deviations:**
- The 2008 matrices are shuffled only in the orders (Ioannis's program), so they stay closer to the diagonal than a full shuffle (7.9 vs 10.1 at n = 30); `shuffle=False` gives the unshuffled extreme.
- The 2006 Challenge matrices are hand-made families (`small`, `wbo`, `wbop`, `wbp`, `shaw`, `sp`); `uniform` matches their densities, not their specific structure.
