# blocksworld (autoscale)

Blocksworld with a robot arm (4 operators): rearrange uniformly random towers into another random configuration.

## Source

- **Domain:** Blocksworld goes back to Terry Winograd (1972); 4-operator encoding with `on-table`/`arm-empty` from the pddl-generators `blocksworld/4ops` directory
- **Generator:** `blocksworld/bwstates.1` (John Slaney and Sylvie Thiébaux) + `blocksworld/4ops/2pddl` (Albert Ludwigs University Freiburg) from [Autoscale's pddl-generators](https://github.com/AI-Planning/autoscale/tree/main/pddl-generators), called as `blocksworld 4 {n} {seed}`; Python port in `generator.py` (reuses the uniform state sampler of `ipc/blocks_4`)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/blocksworld`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/blocksworld`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_blocks` | blocks | Autoscale: start 5–10, slope 1–5; agile tasks 9–151 |
| `seed` | random seed | – |

## Distribution

### Objects
Blocks `b1..bn`.

### Initial state
A state drawn uniformly at random from all blocksworld states with n blocks (exact counting, as bwstates): `on`, `on-table`, `clear`, `arm-empty`.

### Goal
A second, independently drawn uniform random state, given only by its `on` facts. Tower bottoms and tops are left unconstrained, and blocks alone on the table get no goal fact.

### Other
No action costs. Problem name `bw-rand-<n>` (as upstream). Always solvable.

## Comparison with reference tasks

30 agile tasks, each compared with 20 generated tasks with the same number of blocks. Values are per block.

| aspect | reference tasks | this generator |
|---|---|---|
| initial towers per block | 0.118 | 0.131 |
| initial highest tower / n | 0.345 | 0.346 |
| goal `on` facts per block | 0.870 | 0.870 |
| goal `on-table` / `clear` facts | 0 / 0 | 0 / 0 |
| goal towers per block (towers with ≥ 2 blocks) | 0.127 | 0.111 |
| goal highest tower / n | 0.328 | 0.353 |
| problem name | `bw-rand-<n>` | same |

**Deviations:** none found.
