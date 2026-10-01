# pathwaysmetric (numeric/ipc)

Biochemical pathways: combine molecule quantities through reactions until enough of the goal molecules exist.

## Source

- **Domain:** Pathways (IPC 2006) by Yannis Dimopoulos, Alfonso Gerevini and Alessandro Saetti, in the atemporal metric version of Coles, Fox and Long (JAIR 2013) used by the IPC 2023 numeric track
- **Generator:** port of `pddl-generators/pathways/main.c` in numeric mode (`-N` with random constants and disjunctive goals); reaction selection and goal sampling are implemented in `generator.py`, with the upstream reaction database shipped beside it as `reactions.txt` and `simple_substances.txt`
- **Reference tasks:** `data/numeric/ipc2023/pathwaysmetric`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `min_reactions` | minimal number of reactions in the network (`-R`) | 12–324 |
| `num_goals` | goal pairs (`-G`) | 1–27 |

## Distribution

### Objects
Used simple and complex molecules from the upstream reaction database.

### Initial state
- Every used simple molecule `possible`, every molecule `available` 0, `num-subs` 0.
- Each selected reaction with need and produce quantities uniform in 1..4; a catalysed association of a molecule with itself becomes a self-association needing the sum of both quantities.
- Durations per reaction: association `1 + (0.2 − f/10)`, catalysed `2 + (0.4 − f/5)`, synthesis `4 + (0.8 − f/2.5)`, f = upstream `fnum_rand` (one decimal).

### Goal
Goal `i`: `(>= (+ (available a) (available b)) k)` for a pair drawn from late reachability levels, `k` the sum of two draws in 1..4.

### Other
No metric. Upstream warns tasks may be unsolvable; no filter.

## Comparison with reference tasks

21 generated tasks (IPC sizes, seeds from the IPC 2006 command lines) vs the 20 reference tasks:

| aspect | reference tasks | this generator |
|---|---|---|
| need/produce 1 / 2 / 3 / 4 | 0.25 / 0.25 / 0.25 / 0.25 | 0.25 / 0.26 / 0.24 / 0.25 |
| mean goal threshold | 5.12 | 5.14 |
| duration ranges (assoc / catalysed / synthesis) | 0.8–1.1 / 1.6–2.3 / 3.2–4.6 | 0.8–1.1 / 1.6–2.3 / 3.2–4.6 |
| self-association facts | 10 | 7 |

**Deviations:** tasks are not byte-identical to the IPC ones (Python RNG instead of glibc).
