# blocksworld (ipc_learning)

Blocks are stacked into towers by a 4-operator arm.

## Source

- **Domain:** Terry Winograd (1972); IPC 2023 learning-track encoding (untyped, 4 operators)
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/blocks_4`), learning-track domain file; unchanged
- **Reference tasks:** `data/classical/ipc2023-learning/blocksworld_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `blocksworld/blocksworld.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_blocks` | blocks | 5–488 |

## Distribution

### Objects
`b1..bn`, untyped.

### Initial state
A uniformly random blocksworld state (exact counting, as bwstates): `on`, `on-table`, `clear`, `arm-empty`.

### Goal
A second uniformly random state as a full goal: every `on`, `on-table` and `clear` fact.

### Other
No action costs. Always solvable.

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator |
|---|---|---|
| goal `on` per block | 0.859 | 0.814 |
| goal `on-table` / `clear` per block | 0.141 / 0.141 | 0.186 / 0.186 |
| initial towers per block | 0.147 | 0.174 |

**Deviations:**
- Objects are untyped; the learning tasks declare `- object` explicitly (same meaning). Fix if byte-level typing matters: emit `- object`.
