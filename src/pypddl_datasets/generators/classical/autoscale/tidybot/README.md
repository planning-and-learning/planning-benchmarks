# tidybot (autoscale)

A robot with a cart tidies objects from tables into cupboards.

## Source

- **Domain:** Bhaskara Marthi, IPC 2011; `domain.pddl` is Autoscale's copy, identical to `ipc/tidybot`'s
- **Generator:** re-export of `ipc/tidybot` (port of the Clojure generator `core.clj`)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-{agile,optimal}-strips/tidybot`, from Autoscale's pool (`tasks-of-domains-without-usable-generator/tidybot-exhaustive`, upstream-generator runs) plus 5 IPC 2011/2014 tasks

## Parameters

| parameter | meaning | reference range (task headers) |
|---|---|---|
| `world_size` | grid side | 6–15 |
| `num_tables` | requested tables | 0–10 |
| `num_cupboards` | cupboards | 1–3 |

## Distribution

### Objects
Robot `pr2`, the cart, objects, grid coordinates, as `ipc/tidybot`.

### Initial state
As `ipc/tidybot`: tables and cupboards placed on the grid (redrawn until every cupboard fits), objects on tables, robot and cart positions.

### Goal
`(object-done o)` for every object.

### Other
No action costs. Solvability is not guaranteed, as upstream.

## Comparison with reference tasks

The 55 tasks with a size header, regenerated at their size, tables and cupboards (5 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| objects = goals | 6.20 | 4.65 |
| `surface` cells | 17.6 | 11.4 |

**Deviations:**
- Generated tasks place fewer tables and objects than the headers' counts suggest (4.65 vs 6.20 objects); upstream drops tables that do not fit, and Autoscale's pool presumably favours runs where more fitted.
