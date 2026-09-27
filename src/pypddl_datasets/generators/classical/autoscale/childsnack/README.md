# childsnack (autoscale)

Make sandwiches, taking gluten allergies into account, and serve them on trays to children waiting at tables.

## Source

- **Domain:** Raquel Fuentetaja and Tomás de la Rosa, IPC 2014
- **Generator:** `childsnack/child-snack-generator.py` (Raquel Fuentetaja and Tomás de la Rosa, MIT license) from [Autoscale's pddl-generators](https://github.com/AI-Planning/autoscale/tree/main/pddl-generators), called as `child-snack-generator.py pool {seed} {num_children} {num_trays} {gluten_factor} {const_ratio}`. Same as `ipc/childsnack`: `generator.py` re-exports it and only `domain.pddl` is Autoscale's.
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/childsnack`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/childsnack`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_children` | children (also bread and content portions) | Autoscale: start 2–12, slope 1–3; agile tasks 5–34 |
| `num_trays` | trays | Autoscale: {2, 3, 4}; agile tasks 4 or 2 |
| `gluten_factor` | share of allergic children | Autoscale: {0.4, 0.6, 0.8}; agile tasks 0.8 or 0.6 |
| `const_ratio` | sandwich objects per child | Autoscale: {1, 1.3, 2}; agile tasks 1.0 or 2.0 |
| `seed` | random seed | – |

## Distribution

### Objects
Same as `ipc/childsnack`: `child1..c`, `bread1..c`, `content1..c`, `ceil(c * const_ratio)` sandwiches, trays, and `table1..table3`.

### Initial state
Same as `ipc/childsnack`. Everything starts in the kitchen; `int(c * gluten_factor)` gluten-free breads and contents and allergic children are drawn uniformly without replacement; each child waits at a uniformly random table; all sandwiches are `notexist`.

### Goal
`served` for every child.

### Other
No action costs. Problem name `childsnack-c<c>-t<t>`. Solvable whenever `const_ratio >= 1`.

## Comparison with reference tasks

30 agile tasks; 30 samples per task at the parameters recorded in its header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| sandwiches = ceil(c · ratio), allergic = gluten-free breads = int(c · gluten) | 30/30 | always |
| distinct tables with waiting children | 2.93 | 2.97 |
| share of children at the busiest table | 0.464 | 0.452 |
| problem name | `prob-snack` | `childsnack-c…-t…` |

**Deviations:** none in the distribution; only the problem name and the missing header comment.
