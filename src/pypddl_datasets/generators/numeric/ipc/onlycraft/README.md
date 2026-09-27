# onlycraft (numeric/ipc)

A Minecraft-like agent breaks trees, crafts planks, sticks and tree taps, and crafts pogo sticks.

## Source

- **Domain:** IPC 2026 numeric track (`PolyCraft`), inspired by Benyamin, Mordoch, Shperberg, Piotrowski and Stern, "Crafting a Pogo Stick in Minecraft with Heuristic Search (Extended Abstract)"
- **Generator:** reconstruction from the 40 opt and sat IPC tasks (no generator was published); Python in `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/onlycraft-opt`, `data/numeric/ipc2026/onlycraft-sat` (same domain file; they differ only in their parameter sequences)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_pogo_sticks` | pogo sticks to craft | opt 1–20, sat 1–200 |
| `num_trees` | tree cells (default ceil(3.5 × sticks)) | 4–700 |
| `grid_size` | n for n² cells (default floor(√trees) + 1) | 3–27 |

## Distribution

### Objects
Cells `cell0..cell<n²−1>`.

### Initial state
- `position` and `crafting_table_cell` on uniformly random cells (the table may share a tree cell).
- `num_trees` random cells are `tree_cell`, the rest `air_cell`; no low or dead trees, no `connected` facts.
- All inventory counts and `toxicity` 0.

### Goal
`(>= (count_pogo_stick) k)`.

### Other
No metric; name `onlycraft-p<k>-t<trees>-g<n>`.

## Comparison with reference tasks

Regenerated at each IPC task's goal count:

| aspect | reference tasks | this generator (defaults) |
|---|---|---|
| tree cells | ceil(3.5 k) | identical in 40/40 |
| grid size | — | identical in 38/40 |

**Deviations:** two opt tasks use a larger grid (49 cells for 35 trees, 81 for 63); pass `grid_size` for those.
