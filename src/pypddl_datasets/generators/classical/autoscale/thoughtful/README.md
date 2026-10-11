# thoughtful (autoscale)

Thoughtful Solitaire: Klondike with every card position known. Move all cards of four suits home in ascending order, using the tableau columns and a talon that is cycled one card at a time.

## Source

- **Domain:** IPC 2008 learning track / IPC 2014 `thoughtful-typed` (no author named in the file); Autoscale's copy, identical to the IPC 2014 file (already lowercase)
- **Generator:** Autoscale has no generator for this domain (its tasks come from the IPC 2014 and IPC 2008 learning-track pools); re-exports `../../ipc/thoughtful`, whose deal is reconstructed from those tasks
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/thoughtful`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/thoughtful`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cards` | cards per suit, ace upwards (4 suits always) | agile: 11, 13; optimal: 5, 11, 13 |
| `num_columns` | tableau columns; column i holds i cards | agile: 6, 7; optimal: 4, 6, 7 |
| `seed` | random seed | – |

Sizes: agile 13 × `(11, 6)`, 17 × `(13, 7)`; optimal 5 × `(5, 4)`, 15 × `(11, 6)`, 10 × `(13, 7)`.

## Distribution

Same as [`../../ipc/thoughtful`](../../ipc/thoughtful/README.md): uniform shuffle, columns of heights 1 … `num_columns` with only the top card face up, the rest as talon with its third card from the bottom playable; goal all four top cards home.

## Comparison with reference tasks

All 60 Autoscale tasks (42 byte-identical to IPC 2014 tasks, the rest from the IPC 2008 learning-track pool) are reproduced line for line when their own deal is fed in place of the shuffle; deal statistics are in the IPC README.

**Deviations:** no solvability filter (the IPC tasks were proven solvable with a solver that is not public).
