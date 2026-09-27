# freecell (ipc)

FreeCell solitaire: move all cards of four suits home in ascending order, using free cells and empty columns as temporary storage.

## Source

- **Domain:** Fahiem Bacchus, AIPS-2000 competition (STRIPS adaptation of a TLPLAN domain by Nolan Andres and Robert HillHouse); reused in IPC 2002
- **Generator:** the original IPC generator is not public. The deal is reconstructed from the reference tasks; pddl-generators' `freecell/freecell.c` (Jörg Hoffmann, FF domain collection) uses a different, typed encoding and was only a reference. Python implementation in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/freecell` (60 IPC 2000 tasks `probfreecell-N-k.pddl`, 20 IPC 2002 tasks `pNN.pddl`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cards` | cards per suit, ace upwards (4 suits always) | 2–13 (IPC 2000: 5 tasks per value; IPC 2002: 1–2 per value) |
| `num_cells` | free cells | IPC 2000: 4; IPC 2002: 2–4 |
| `num_columns` | tableau columns | IPC 2000: 8; IPC 2002: 4–8 |
| `style` | `ipc2000` or `ipc2002`: deal, number range and naming | both |
| `seed` | random seed | – |

## Distribution

### Objects
Four suit objects (`c d h s` for `ipc2000`, `club diamond heart spade` for `ipc2002`), and per suit the cards `0, a, 2, …, 10, j, q, k` up to `num_cards` (card `0` is the empty home placeholder), e.g. `c0 ca c2` or `club0 clubA club2`. Numbers `n0 … nM` with M = 13 for `ipc2000` and M = max(num_cards, num_cells, num_columns) for `ipc2002`.

### Initial state
- Static: `value` of every card (placeholder n0, ace n1, …), `suit` of every card, `successor` chain on the numbers, `canstack c1 c2` for every card c1 of rank r ≥ 1 and card c2 of rank r + 1 in the opposite colour (clubs/spades black, diamonds/hearts red).
- `home` holds the four placeholders; `cellspace n<num_cells>` (all cells empty), `colspace n<num_columns − non-empty columns>`.
- Tableau (uniform shuffle, dealt round-robin to the columns): `ipc2000` deals a full 52-card deck onto the columns and then removes every card above `num_cards`, so columns are uneven and may end up empty; `ipc2002` shuffles and deals only the 4 · `num_cards` cards, so column heights differ by at most one. Each column contributes `bottomcol`, `on` facts bottom to top and `clear` on its top card.

### Goal
`home` of the top card (rank `num_cards`) of each of the four suits; nothing else.

### Other
No action costs, no metric. Problem name `freecell-<num_cards>[-<seed>]` (`ipc2000`) or `freecell<num_cards>-4` (`ipc2002`). Solvability is neither guaranteed nor checked (random deals are almost always solvable with 4 cells; tasks with few cells and columns can be dead ends). All output is lowercase.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| objects, static facts and goal given each task's parameters | – | identical in 80/80 tasks |
| cards in free cells initially | 0 in 80/80 | always 0 |
| `ipc2000` non-empty columns, mean (N = 2 / 3 / 4 / 6 / 8+) | 5.80 / 7.00 / 7.40 / 7.80 / 8.00 | 5.50 / 6.74 / 7.43 / 7.91 / ≥7.99 |
| `ipc2000` highest column, mean (N = 2 / 6 / 10 / 13) | 2.40 / 4.60 / 6.40 / 7.00 | 2.42 / 4.80 / 6.46 / 7.00 |
| `ipc2002` column heights | equal to round-robin heights in 20/20 (spread ≤ 1) | round-robin, spread ≤ 1 |

(IPC: 5 tasks per N; generator: 400 seeds per N.)

**Deviations:**
- Problem names differ (the IPC 2000 names count instances 1–5 instead of seeds; the IPC 2002 set repeats names like `FreeCell9-4` for different tasks).
- Which physical column receives the extra cards and the fact order differ; neither affects the task.
