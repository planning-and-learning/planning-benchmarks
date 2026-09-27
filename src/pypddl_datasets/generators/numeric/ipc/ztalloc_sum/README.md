# ztalloc_sum (numeric/ipc)

Reversed Collatz on several registers: starting from 1 each, double or apply (x−1)/3 until the registers sum to a target.

## Source

- **Domain:** Ztalloc by Christian Muise; IPC 2026 edit with several registers summing to a target (`domain.pddl` is the IPC file)
- **Generator:** reconstruction from the reference tasks (no generator was published); `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/ztalloc-sum`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_registers` | registers | 3–6 (5 tasks each) |
| `target` | required sum | 187–12347 |
| `min_target`, `max_target` | range for a drawn target when `target` is omitted | — |

## Distribution

### Objects
Registers `r1..rn`.

### Initial state
`(free)`; per register `(normal r)`, `(value r) = 1`, `(work-value r) = 0`; `(total-cost) = 0`.

### Goal
`(= (+ … (value r_i) …) target)`, `(free)`, and every register `normal` with `work-value` 0. `target` is given or uniform in `[min_target, max_target]`.

### Other
`(:metric minimize (total-cost))`. Solvable if the Collatz conjecture holds (as the domain notes).

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| tasks reproduced (registers and target from the task) | 20 | 20 identical (whitespace-normalized) |

**Deviations:** none; the reference targets grow with the register count, the generator draws them uniformly in a given range.
