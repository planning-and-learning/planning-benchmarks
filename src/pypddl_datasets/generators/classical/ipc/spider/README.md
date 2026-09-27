# spider (ipc)

Spider solitaire with all cards face up: build complete same-suit runs from king to ace and discard them, dealing one extra card to every pile from the deals when stuck.

## Source

- **Domain:** IPC 2018 (spider-opt18/sat18-strips); the domain authors are not recorded in the sources
- **Generator:** pddl-generators `spider/generate.py` (IPC 2018; authors not recorded). The IPC tasks were produced by `generate-and-solve.sh`, which re-ran the generator with seed + 1 until an external spider solver found a plan. Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/spider-opt18-strips`, `data/classical/downward-benchmarks/spider-sat18-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_decks` | decks | 1, 2, 4 (always num_decks · num_suits = 4) |
| `num_suits` | suits per deck | 4, 2, 1 |
| `num_values` | values per suit (ace … king) | opt: 3–9, sat: 6–12 |
| `num_piles` | tableau piles | 3–8 (values 3→3, 4→3, 5→4, 6→4, 7→5, 8→6, 9→6, 10→7, 11→8, 12→8) |
| `num_deals` | deals of one card per pile | 2 |
| `seed` | random seed | – |

## Distribution

### Objects
Cards `card-d<deck>-s<suit>-v<value>` for every deck, suit and value; piles `pile-0 … pile-<num_piles−1>` (type `tableau`); deals `deal-0 … deal-<num_deals>` (one more than dealt, as the "no deal left" marker); the constant `discard`.

### Initial state
- All cards are shuffled uniformly. The first `num_deals · num_piles` form the deals (card i of a deal goes to pile i); the rest are split evenly over the piles, the first piles receiving one extra card each.
- Per pile: `on` chain from the pile object upwards, `clear` on the top card, `part-of-tableau` for the pile and its cards, `in-play` for its cards, `movable` for the maximal same-suit descending run on top.
- Per deal: `on` chain onto `deal-i`, `clear` on the card for pile 0, `to-deal` facts linking each card to its pile and successor; `current-deal deal-0`, `next-deal` chain.
- Static: `can-continue-group` (same suit, value + 1, any decks), `can-be-placed-on` (any suits, value + 1), `is-ace`, `is-king`; `(= (total-cost) 0)`.

### Goal
Every card `on discard`, every pile and every deal (except the marker) `clear`.

### Other
Metric minimize `total-cost`: the domain charges 1 for starting a deal, moving a card or run, and starting to collect a completed run; all bookkeeping actions cost 0. Problem name `spider-<decks>-<suits>-<values>-<piles>-<deals>[-<seed>]`, as upstream. Solvability is not guaranteed: unlike the IPC tasks, no solver filter is applied. All output is lowercase.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| fact counts per predicate (except `movable`), each task's parameters | – | identical in 40/40 tasks |
| `movable` cards per task, mean | 5.73 | 5.80 (200 seeds per task) |
| output for the same seed as upstream `generate.py` | – | identical (same Python RNG calls) |
| tasks rejected as unsolvable before acceptance | ≥ 9 of 40 needed a seed retry (up to +48) | no filter |

**Deviations:**
- No solvability filter: the IPC seeds show that at least 9 of 40 accepted tasks needed retries, so a noticeable share of raw draws is unsolvable (or took the solver over 30 s).
- The IPC tasks themselves are not reproduced byte for byte even with their recorded seeds (their deals differ), presumably because of the retry history or a different Python RNG version.
