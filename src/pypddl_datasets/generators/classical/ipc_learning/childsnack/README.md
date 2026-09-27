# childsnack (ipc_learning)

Sandwiches are made and served to children, some allergic to gluten.

## Source

- **Domain:** Raquel Fuentetaja, Tomás de la Rosa (IPC 2014); learning-track encoding
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/childsnack`), learning-track domain file; problem declares `(:domain childsnack)` instead of `child-snack`
- **Reference tasks:** `data/classical/ipc2023-learning/childsnack_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `childsnack/childsnack.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_children` | children | 4–292 |
| `num_trays` | trays | 1–10 |
| `gluten_factor` | allergic share | 0–0.56 |
| `const_ratio` | sandwiches per child | 1.0–1.5 |

## Distribution

### Objects
Children, trays, bread and content portions (one each per child), sandwiches (`const_ratio`·children), tables.

### Initial state
Allergic children and gluten-free portions by `gluten_factor`; trays in the kitchen; children waiting at random tables.

### Goal
Every child served.

### Other
No action costs. Solvable by construction (enough gluten-free portions).

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| allergic share | 0.562 | 0.562 |
| sandwiches per child | 1.325 | 1.326 |
| gluten-free bread per child | 0.562 | 0.562 |

**Deviations:**
- None found; `gluten_factor=1.0` gives the all-allergic tasks (3/90).
