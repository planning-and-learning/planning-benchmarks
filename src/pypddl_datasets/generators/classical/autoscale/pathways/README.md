# pathways (autoscale)

Biochemical pathways: choose initial substances and apply reactions until one of two target molecules is available for every goal.

## Source

- **Domain:** Yannis Dimopoulos, Alfonso Gerevini and Alessandro Saetti, IPC 2006; one domain file per task (`make_task`)
- **Generator:** re-export of `ipc/pathways` (port of pddl-generators `pathways/main.c`, plus `pathways/wrapper.py` via `strips_wrapper=True`)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/pathways` are the 30 IPC tasks (byte-identical to `downward-benchmarks/pathways`); `21.11-optimal-strips/pathways` come from Autoscale's pool of `wrapper.py` runs (`tasks-of-domains-without-usable-generator/pathways-exhaustive`), which use the STRIPS encoding of `strips_wrapper=True`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `min_reactions` | stop adding substances once this many reactions are reachable | reaction facts 1–625 |
| `num_goals` | disjunctive goals (declared goal predicates) | goals used 1–48 |
| `num_substances` | choosable initial substances (levels `l0..lL`) | 3–50 |
| `strips_wrapper` | `wrapper.py` encoding | agile: false; optimal: true |

## Distribution

### Objects
IPC style: the molecules of reachable reactions (goal molecules as domain constants) and the levels. `strips_wrapper`: all molecules are domain constants, the problem declares only levels.

### Initial state
As `ipc/pathways`: `possible` for the drawn simple substances, the reachable reactions, `(num-subs l0)` and the `next` chain.

### Goal
`goal1..goal<k>`. IPC style: each goal action has an `or` of two `available` preconditions. `strips_wrapper`: two single-precondition `dummy-strips-action-<i>` per goal; `num_goals` goal predicates are declared, but only the reachable goals are asked for.

### Other
No action costs. `make_task` returns `(domain, problem)`. Tasks can be unsolvable, as upstream.

## Comparison with reference tasks

Each task regenerated with R = its reaction-fact count, G = its declared goals, L = its levels − 1 (5 seeds):

| aspect | reference tasks | this generator |
|---|---|---|
| agile: goals used / reaction facts / `possible` (30 tasks) | 20.43 / 301.9 / 47.0 | 20.43 / 363.2 / 51.5 |
| optimal (`strips_wrapper`): goals used / reaction facts / `possible` (30 tasks) | 7.77 / 73.1 / 20.3 | 7.74 / 84.3 / 24.5 |
| optimal: declared goal predicates ≥ goals used | 30/30 | always |

**Deviations:**
- Reaction counts are higher because the reference count is passed as the minimum; the IPC seeds are selected draws (see `ipc/pathways`).
