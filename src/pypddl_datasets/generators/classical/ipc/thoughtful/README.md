# thoughtful (ipc)

Thoughtful Solitaire: Klondike with every card position known. Move all cards of four suits home in ascending order, using the tableau columns (alternating colours, descending; kings into empty columns) and a talon that is cycled one card at a time.

## Source

- **Domain:** IPC 2008 learning track (organisers Alan Fern, Roni Khardon, Prasad Tadepalli; rules after Bjarnason, Tadepalli, Fern, "Searching Solitaire in Real Time", ICGA Journal 2007); the domain file names no author. This is the IPC 2014 version `thoughtful-typed` (already lowercase; copied verbatim)
- **Generator:** no original generator is public (the IPC 2008 domain page links none). The deal is reconstructed from the reference tasks; Python implementation in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/thoughtful-{sat,mco}14-strips` (40 tasks: 5 `bootstrap-typed-*`, 35 `p<s>_<t>_<k>-typed` / `target-typed-*`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cards` | cards per suit, ace upwards (4 suits always); rank `num_cards` is the "king" | 5 (bootstrap), 11, 13 |
| `num_columns` | tableau columns; column i holds i cards | 4 (bootstrap), 6, 7 |
| `seed` | random seed | – |

The IPC sizes are `(5, 4)`, `(11, 6)` and `(13, 7)` (problem names `thoughtful-s<num_cards>-t<num_columns>`). The talon must keep at least 3 cards.

## Distribution

### Objects
Per suit `c d h s` the cards `0, a, 2, …, 9, t, j, q, k` up to `num_cards` (card `0` is the empty home placeholder); `coln0 … coln<num_columns>` (colnum); `n0 … n<num_cards>` (num); the suits `c d h s` (suittype).

### Initial state
- Static: `value` of every card, `suit` of every card, `successor` chain on the numbers, `colsuccessor` chain on the colnums, `king` for the rank-`num_cards` cards, `canstack c1 c2` for every c1 of rank r ≥ 2 onto c2 of rank r + 1 in the opposite colour (aces never stack). No `ace` facts.
- Deal: one uniform shuffle of the 4 · `num_cards` cards; the first 1 + 2 + … + `num_columns` cards fill columns of heights 1, 2, …, `num_columns` (`bottomcol`, `on` bottom to top, `clear` and `faceup` on the top card only); the rest is the talon (`bottomtalon`, `ontalon` bottom to top, `toptalon`) with `talonplayable` on its third card from the bottom.
- `colspace coln0` (no empty column); `home` holds the four placeholders.

### Goal
`home` of the top card of each suit; nothing else.

### Other
No action costs. Problem name `thoughtful-s<num_cards>-t<num_columns>`, as in the IPC tasks (no seed). Solvability is not checked. The IPC 2008 page says the competition tasks were all proven solvable with the Bjarnason et al. solver, and the gaps in the IPC task numbers (`p11_6_53`, `_59`, `_62`, …) suggest a filtered pool; Fast Downward solved 20/20 generated `(5, 4)` tasks, while for `(11, 6)` and `(13, 7)` neither the IPC tasks nor generated tasks finish within 4 minutes with `lama-first`, so solvability of large generated tasks is unknown. All output is lowercase.

## Comparison with reference tasks

Every one of the 151 reference files (IPC 2014, Autoscale 21.11 agile and optimal, Autoscale's IPC 2008 learning-track pool) is reproduced line for line (up to case, whitespace, and the pool's `:requirements` line) when its own deal is fed in place of the shuffle. Deal statistics over the 65 distinct reference deals vs. 2000 seeds per size:

| aspect (mean per task) | reference (5,4) / (11,6) / (13,7) | this generator |
|---|---|---|
| distinct deals | 5 / 23 / 37 | – |
| aces on top of a column | 1.60 / 0.39 / 0.41 | 0.79 / 0.56 / 0.54 |
| aces in the talon | 1.60 / 2.09 / 2.03 | 2.04 / 2.12 / 1.85 |
| kings at a column bottom | 0.80 / 0.61 / 0.73 | 0.77 / 0.55 / 0.53 |
| ace or 2 initially talon-playable | 0.40 / 0.13 / 0.11 | 0.39 / 0.18 / 0.15 |

The differences are mostly within sampling noise of the small reference sets (standard error about 0.12–0.15 for the large sizes, 0.35 for the 5 bootstrap tasks); the bootstrap tasks having more aces on top may reflect the IPC solvability filter.

**Deviations:**
- No solvability filter (the IPC tasks were filtered with a solver that is not public).
- Which shuffled positions go to which column is a convention; any fixed mapping gives the same uniform deal distribution.
