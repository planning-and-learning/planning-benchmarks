# forestfire (numeric/ipc)

Bots fetch water from ponds to put out fires on a grid, chopping trees and squeezing through bushes on the way.

## Source

- **Domain:** Alexander Shleyfman (shleyfman.alexander@gmail.com), IPC 2026 numeric track
- **Generator:** reconstruction from the 20 IPC tasks (no generator was published); Python in `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/forestfire`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `width`, `height` | grid size (width odd) | 3–9 × 3–8 |
| `num_bots`, `num_axes` | bots and axes on row 1 | 1–3, 1–3 |
| `water_capacity` | water per bot | 3–12 |
| `axe_durability` | chops per axe | 2–4 |
| `gate_tree` | trees on the middle cell of row 2 | 3, 6 |
| `fire_rows`, `fire_probability`, `max_fire` | burning top rows, per-cell fire chance, fire units | 1–2, subsets to all cells, 1–13 |
| `extra_trees`, `max_tree` | trees between gate and fire rows | 0–5, 2–6 |

## Distribution

### Objects
`bot<i>`, `axe<i>`, `grass<x>_<y>` for every cell except row 2, where all cells but the middle one are `bushes<x>_<y>`.

### Initial state
- All 4-neighbours `connected` (both directions); `max-water` 1 on every bush, so bots cross bushes with at most one unit of water.
- `tree` 0 everywhere except the gate (`gate_tree`) and `extra_trees` random cells between gate and fire rows (1..`max_tree`).
- `fire` on a random subset (at least one) of the top `fire_rows` rows, 1..`max_fire` units each; 0 elsewhere.
- Bots on `grass1_1`, `grass2_1`, …, empty (`has-water` 0) with `water-capacity`; axes on `grass1_1`, `grass2_1`, … with `durability`; ponds `grass1_1` and `grass<width>_1`; `(= (cost) 0)`.

### Goal
`(= (fire c) 0)` for every burning cell.

### Other
`(:metric minimize (cost))`. A draw is kept only if the fire rows can be reached by chopping at most the total axe durability (entering a tree cell forces chopping it), so tasks are solvable; name `forestfire-w<W>-h<H>-b<bots>-a<axes>`.

## Comparison with reference tasks

Regenerated at each IPC task's width, height, bots and axes:

| aspect | reference tasks | this generator |
|---|---|---|
| objects, connections, ponds, start cells, `max-water` | — | identical in 19/20 |
| gate tree, water capacity, durability, fire amounts | per task | parameters |

**Deviations:**
- `prob12` declares `axe3` but never places it (its `(at axe2 grass2_1)` is duplicated); here every axe is placed.
- Axe durabilities are one value per task (IPC `prob15` mixes 3/4/2); extra trees are random cells, not whole rows.
