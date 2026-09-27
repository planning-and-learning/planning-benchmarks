# barman (ipc)

A two-handed robot barman fills shots with ingredients and shaken cocktails.

## Source

- **Domain:** Sergio Jiménez Celorrio, IPC 2011 (not stated in the generator files); `domain.pddl` is the IPC 2014 file (no action costs)
- **Generator:** `barman/barman-generator.py` from [pddl-generators](https://github.com/AI-Planning/pddl-generators) (no author stated), the generator of the IPC 2011/2014 tasks; Python port in `generator.py`. `../../autoscale/barman` re-exports it with `action_costs=True`.
- **Reference tasks:** `data/classical/downward-benchmarks/barman-opt11-strips`, `data/classical/downward-benchmarks/barman-opt14-strips`, `data/classical/downward-benchmarks/barman-sat11-strips`, `data/classical/downward-benchmarks/barman-sat14-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cocktails` | cocktails, each mixed from two distinct ingredients | 3–11 |
| `num_ingredients` | ingredients (one dispenser each) | 3–5 |
| `num_shots` | shots, at least `num_cocktails + 1` | `num_cocktails + 1` … `num_cocktails + 6` |
| `seed` | random seed | – |
| `action_costs` | IPC 2011 encoding: `(= (total-cost) 0)` and the metric (default off, IPC 2014) | 2011 tasks: on; 2014 tasks: off |

## Distribution

### Objects
`shaker1`, hands `left`/`right`, `shot1..`, `ingredient1..`, `cocktail1..`, `dispenser1..` (one per ingredient), levels `l0 l1 l2`.

### Initial state
Everything is on the table, clean and empty; both hands are empty; the shaker is at level `l0`; `next l0 l1`, `next l1 l2`; dispenser i dispenses ingredient i. Each cocktail's parts are an ordered pair of distinct ingredients drawn uniformly. With `action_costs`, also `(= (total-cost) 0)`.

### Goal
Shots `1..c` contain a uniformly random permutation of all cocktails. Each shot `c+1..s-1` contains, with probability 1/2 each, a uniformly random cocktail or a uniformly random ingredient. The last shot is left free.

### Other
No action costs by default (IPC 2014); `action_costs=True` adds `(:metric minimize (total-cost))` for the IPC 2011 domain. Problem name `barman-c<c>-i<i>-s<s>`. Solvable: every cocktail can be made with the shaker and the free shot.

## Comparison with reference tasks

All 74 IPC tasks, each compared with 100 generated tasks at its `(c, i, s)`.

| aspect | reference tasks | this generator |
|---|---|---|
| every cocktail served exactly once in shots 1..c | 74/74 | always |
| goals = shots − 1 | 74/74 | always |
| init predicates | clean, cocktail-part1/2, dispenses, empty, handempty, next, ontable, shaker-empty-level, shaker-level | same |
| ingredient goals among shots beyond `c` (sat11 / opt11 / sat14 / opt14) | 0.58 / 0.38 / 0.42 / 0.67 | 0.54 / 0.56 / 0.52 / 0.56 (expected 0.50) |
| extra goal shots per task (sat11 / opt11 / sat14 / opt14) | 1.80 / 0.40 / 3.20 / 0.43 | same (fixed by parameters) |
| `total-cost` | 2011: yes, 2014: no | `action_costs` selects |
| problem name | `prob` | `barman-c…-i…-s…` |

**Deviations:**
- The IPC ingredient shares scatter around 1/2 because the tracks have only 6–64 extra goal shots in total; the generator draws 1/2.
- The IPC 2011 tasks need `action_costs=True` together with the 2011 domain file (the Autoscale file adds one `used` effect to it).
- Problem name only otherwise.
