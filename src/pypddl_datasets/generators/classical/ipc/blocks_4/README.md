# blocks_4 (ipc)

Blocksworld with a robot arm (4 operators): rearrange uniformly random towers into a goal configuration.

## Source

- **Domain:** Blocksworld goes back to Terry Winograd (1972); `domain.pddl` is the IPC 2000 4-operator `BLOCKS` domain (predicates `ontable`, `handempty`, actions `pick-up`, `put-down`, `stack`, `unstack`)
- **Generator:** our own variant of `blocksworld/bwstates.1` (John Slaney and Sylvie Thiébaux) + `blocksworld/4ops/2pddl` (Albert Ludwigs University Freiburg) from [pddl-generators](https://github.com/AI-Planning/pddl-generators); `generator.py` samples initial states uniformly like bwstates; the goal follows the IPC tasks
- **Reference tasks:** `data/classical/downward-benchmarks/blocks`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_blocks` | blocks | 4–17 |
| `seed` | random seed (default: current time) | – |
| `goal` | `tower` (IPC, default) or `full` (our variant) | `tower` |

## Distribution

### Objects
Blocks `b1..bn`.

### Initial state
A state drawn uniformly at random from all blocksworld states with n blocks (exact counting, as bwstates): `on`, `ontable`, `clear`, and `handempty`.

### Goal
- `goal="tower"` (default, as every IPC task): one tower of all n blocks in a uniformly random order, given as its n−1 `on` facts only; the bottom block's position and `clear` are left unconstrained.
- `goal="full"` (our variant): a second, independently drawn uniform random state, given in full: every `on` fact, `ontable` for each tower bottom, and `clear` for each tower top.

### Other
No action costs. Problem name `blocks-4-<n>`. Always solvable.

## Comparison with reference tasks

35 IPC tasks, each compared with 20 generated tasks with the same number of blocks. Values are per block.

| aspect | reference tasks | this generator |
|---|---|---|
| initial towers per block | 0.323 | 0.336 |
| initial highest tower / n | 0.690 | 0.598 |
| IPC initial state under uniform sampling | mean percentile 0.45 (towers), 0.60 (height) | – |
| goal `on` facts per block | 0.876 (= (n−1)/n) | 0.876 (`full`: 0.668) |
| goal `ontable` / `clear` facts per block | 0 / 0 | 0 / 0 (`full`: 0.332 / 0.332) |
| goal towers per block | 0.124 (always one tower) | 0.124 (`full`: 0.237) |
| goal highest tower / n | 1.000 | 1.000 (`full`: 0.587) |
| block names | `a`, `b`, … | `b1`, `b2`, … |
| domain | IPC `BLOCKS` | the same file |

**Deviations:**
- None in the goal with the default `goal="tower"`. `goal="full"` is our deliberate variant with a unique goal state.
- Initial states are consistent with uniform sampling (percentiles near 0.5 over 35 tasks); the IPC towers are slightly taller (0.69 vs 0.60).
- Block names (`b1`, … vs `a`, …) and problem names differ.
