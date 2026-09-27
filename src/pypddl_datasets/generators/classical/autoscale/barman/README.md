# barman (autoscale)

A two-handed robot barman fills shots with ingredients and shaken cocktails.

## Source

- **Domain:** Sergio Jiménez Celorrio, IPC 2011; Autoscale's version adds a `(used ?d ?b)` effect to `pour-shaker-to-shot`
- **Generator:** `barman/barman-generator.py` from [Autoscale's pddl-generators](https://github.com/AI-Planning/autoscale/tree/main/pddl-generators) (no author stated), called as `barman-generator.py {num_cocktails} {num_ingredients} {num_shots} {seed}`. `generator.py` re-exports `../../ipc/barman` with `action_costs=True`.
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/barman`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/barman`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cocktails` | cocktails, each mixed from two distinct ingredients | Autoscale: start 1–10, slope ≥ 0.33; agile tasks 6–70 |
| `num_ingredients` | ingredients (one dispenser each) | Autoscale: {2,…,6}; agile tasks 2–6 |
| `num_shots` | shots, at least `num_cocktails + 1` | Autoscale: `num_cocktails` + (1–5, optional slope); agile tasks 11–78 |
| `seed` | random seed | – |

## Distribution

### Objects
Same as `ipc/barman`: `shaker1`, hands `left`/`right`, `shot1..`, `ingredient1..`, `cocktail1..`, `dispenser1..`, levels `l0 l1 l2`.

### Initial state
Same as `ipc/barman`, plus `(= (total-cost) 0)`.

### Goal
Same as `ipc/barman`: shots `1..c` get a random permutation of all cocktails; each shot `c+1..s-1` gets a random cocktail or ingredient with probability 1/2 each; the last shot stays free.

### Other
Action costs with `(:metric minimize (total-cost))`. Problem name `barman-c<c>-i<i>-s<s>`. Solvable: every cocktail can be made with the shaker and the free shot.

## Comparison with reference tasks

30 agile tasks, each compared with 50 generated tasks at its `(c, i, s)`.

| aspect | reference tasks | this generator |
|---|---|---|
| every cocktail served exactly once in shots 1..c | 30/30 | always |
| goals = shots − 1 | 30/30 | always |
| ingredient goals among shots beyond `c` | 0.55 | 0.51 (expected 0.50) |
| extra goal shots per task | 3.43 | 3.43 |
| metric | yes | yes |
| problem name | `prob` | `barman-c…-i…-s…` |

**Deviations:** none in the distribution; only the problem name.
