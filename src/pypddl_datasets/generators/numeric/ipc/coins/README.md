# coins (numeric/ipc)

Minimum coins: reach a target value by adding coins of given denominations, using as few coins as possible.

## Source

- **Domain:** Connor Little; IPC 2026 numeric track
- **Generator:** reconstruction from the reference tasks (no generator was published with the IPC 2026 dataset)
- **Reference tasks:** `data/numeric/ipc2026/coins`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `target` | value to reach | 29–3000 |
| `denominations` | coin values, must include 1 | always (1, 2, 3, 5, 7) |

## Distribution

### Objects
One coin `c<i>` per denomination.

### Initial state
`denomination` per coin, `denomination-penalty` 1 for every coin, `(no-coin-update c)` for every coin, `current-value`, `coin-count` and `penalty` 0.

### Goal
`(= (current-value) target)` and `(= (penalty) 0)`.

### Other
`(:metric minimize (coin-count))`. Deterministic; always solvable because denomination 1 is required. Problem name `coins-<target>`.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| denominations | (1, 2, 3, 5, 7) | (1, 2, 3, 5, 7) by default |
| initial state and goal | fixed template, target varies | identical for the task's target (20 of 20) |

**Deviations:** only the problem name (all reference tasks are named `p1`).
