# blocks_3 (ipc)

Blocksworld without a robot arm (3 move operators): rearrange uniformly random towers into a goal configuration.

## Source

- **Domain:** Blocksworld goes back to Terry Winograd (1972); the 3-operator encoding (`move-b-to-b`, `move-b-to-t`, `move-t-to-b`) comes from the IPP domain collection via [pddl-generators](https://github.com/AI-Planning/pddl-generators) `blocksworld/3ops`. It was not used at an IPC.
- **Generator:** our own variant of `blocksworld/bwstates.1` (John Slaney and Sylvie Thiébaux) + `blocksworld/3ops/2pddl` (Albert Ludwigs University Freiburg); `generator.py` samples states uniformly like bwstates and adds a full goal state
- **Reference tasks:** none with this encoding; closest are `data/classical/downward-benchmarks/blocks` (4 operators)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_blocks` | blocks | 4–17 (IPC `blocks`) |
| `seed` | random seed (default: current time) | – |

## Distribution

### Objects
Blocks `b1..bn`.

### Initial state
A state drawn uniformly at random from all blocksworld states with n blocks (exact counting, as bwstates): `on`, `on-table`, `clear`.

### Goal
A second, independently drawn uniform random state, given in full: every `on` fact, `on-table` for each tower bottom, and `clear` for each tower top.

### Other
No action costs. `domain.pddl` requires `:equality` and `:negative-preconditions`. Problem name `blocks-3-<n>`. Always solvable.

## Comparison with reference tasks

Against the 4-operator IPC `blocks` tasks (35 tasks, 20 samples each); per block. The state sampler is the one used by `blocks_4`.

| aspect | reference tasks | this generator |
|---|---|---|
| initial towers per block | 0.323 | 0.336 |
| initial highest tower / n | 0.690 | 0.598 |
| goal `on` facts per block | 0.876 | 0.668 |
| goal `on-table` / `clear` facts per block | 0 / 0 | 0.332 / 0.332 |
| goal highest tower / n | 1.000 (single tower) | 0.587 |

**Deviations:**
- Deliberate variant: 3-operator encoding (no arm) and full goal state; there is no IPC reference for this encoding.
- Relative to the IPC blocks tasks, the goal differs as for `blocks_4`: IPC always asks for one tower of all blocks.
