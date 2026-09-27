# line_exchange_snp (numeric/ipc)

Robots on a line meet their neighbours at segment borders to exchange load units until all loads are equal.

## Source

- **Domain:** IPC 2026 numeric track (`line-exchange`, file `domain_snp.pddl`; authors not named in the files)
- **Generator:** reconstruction from the 20 IPC tasks, named `<robots>_<mean load>_<spread>_<segment>` (no generator was published); Python in `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/line-exchange-snp`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_robots` | robots | 3–5 |
| `mean_load` | mean load (total = robots × mean) | 5, 10, 15 |
| `spread` | percentage of units moved away from the balanced start | 25, 50, 90 |
| `segment` | segment length D (even) | 10, 50, 100 |

## Distribution

### Objects
Robots `r0..`.

### Initial state
- `D` = `segment`; robot i has index `i` and position x = D·i + D/2; `next` chain.
- Loads: start at `mean_load` each; each unit moves with probability `spread`% to a robot drawn by random weights Exp(1)^(0.8·spread/100); already balanced draws are redrawn.

### Goal
Every robot back at its start position and all loads equal (chain `(= (q r_i) (q r_i+1))`).

### Other
No metric. Solvable: the total load is divisible by the number of robots and neighbours can always meet at their shared border (D even); name `line-exchange-<N>-<A>-<B>-<D>`.

## Comparison with reference tasks

Regenerated at each IPC task's name parameters (20 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| positions, indices, D, goal | — | identical |
| mean max deviation from the mean load, spread 25 / 50 / 90 | 0.26 / 0.39 / 0.84 | 0.31 / 0.42 / 0.72 |

**Deviations:** the load model is fitted, not recovered; loads may reach 0 (IPC minimum is 1).
