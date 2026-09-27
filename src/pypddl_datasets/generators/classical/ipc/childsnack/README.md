# childsnack (ipc)

Make sandwiches, taking gluten allergies into account, and serve them on trays to children waiting at tables.

## Source

- **Domain:** Raquel Fuentetaja and Tomás de la Rosa, IPC 2014
- **Generator:** `childsnack/child-snack-generator.py` in `pool` mode (Raquel Fuentetaja and Tomás de la Rosa, MIT license) from [pddl-generators](https://github.com/AI-Planning/pddl-generators); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/childsnack-opt14-strips`, `data/classical/downward-benchmarks/childsnack-sat14-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_children` | children (also bread and content portions) | 6–15 (opt14), 10–24 (sat14) |
| `num_trays` | trays | 2–3 (opt14), 3–4 (sat14) |
| `gluten_factor` | share of allergic children | 0.4 |
| `const_ratio` | sandwich objects per child | 1.3 |
| `seed` | random seed (default: current time) | – |

## Distribution

### Objects
`child1..c`, `bread1..c`, `content1..c`, `ceil(c * const_ratio)` sandwiches, trays, and places `table1..table3` (plus the domain constant `kitchen`).

### Initial state
All trays, breads and contents are in the kitchen. `int(c * gluten_factor)` breads, contents and children are drawn uniformly without replacement as gluten-free or allergic; the rest are `not_allergic_gluten`. Each child waits at a uniformly random table. Every sandwich is `notexist`.

### Goal
`served` for every child.

### Other
No action costs. Problem name `childsnack-c<c>-t<t>`. Solvable whenever `const_ratio >= 1`.

## Comparison with reference tasks

40 IPC tasks; the generator is compared with 30 samples per IPC task at the parameters recorded in its header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| sandwiches = ceil(c · 1.3), allergic = gluten-free breads = contents = int(0.4 c), 3 tables, goals = c | 40/40 | always |
| distinct tables with waiting children | 2.95 | 2.98 |
| share of children at the busiest table | 0.461 | 0.481 |
| problem name | `prob-snack` | `childsnack-c…-t…` |
| header comment with parameters | yes | no |

**Deviations:** none in the distribution; only the problem name and the missing header comment.
