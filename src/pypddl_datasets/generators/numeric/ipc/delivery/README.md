# delivery (numeric/ipc)

Robots with several arms and a tray deliver weighted items between rooms under a load limit.

## Source

- **Domain:** Alexander Shleyfman and Ryo Kuroiwa (IPC 2023 numeric track)
- **Generator:** reconstruction from the reference tasks, whose maps are hand-made (no generator was published)
- **Reference tasks:** `data/numeric/ipc2023/delivery`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rooms` | rooms `rooma ..` | 2–6 |
| `num_items` | items | 4–42 |
| `num_bots`, `num_arms` | bots, arms per bot | 1–3, 2–8 |
| `max_weight` | item weights 1..max_weight | 1–4 |
| `load_limit` | per-bot load limit (default `2 * num_arms * max_weight`) | 4–20 |
| `directed`, `extra_doors` | one-way cycle plus chords, or two-way tree plus extra doors | both families |
| `spread` | probability an item starts outside rooma | 0–0.47 per task |
| `stay_probability` | probability an item's goal is its start | 0–0.27 per task |

## Distribution

### Objects
Rooms, items, bots `bot<b>`, arms `left<b> right<b>` (`left mid right` for three arms, `arm<j>-<b>` otherwise).

### Initial state
- Doors: undirected maps are a random spanning tree plus extra two-way doors (reference: star, square, path shapes); directed maps are a one-way cycle through all rooms in random order plus one-way chords (reference: 5- and 6-room cycles with chords). Every map is strongly connected.
- All bots in rooma with free arms and `current_load = 0`; items weigh uniformly 1..`max_weight` and start in rooma or, with probability `spread`, in a uniform room.
- `(= (cost) 0)`.

### Goal
Every item in a uniform room different from its start (its start with probability `stay_probability`).

### Other
`(:metric minimize (cost))` (moves 3, arm actions 2, tray actions 1). Always solvable: every item fits the load limit and the map is strongly connected.

## Comparison with reference tasks

Generated at reference-like parameters (3/6/6 rooms, 8/26/36 items, 10 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| items starting outside rooma | 0.148 | 0.168 |
| goal equals start | 0.017 | 0.021 |
| mean item weight | 1.41 | 1.78 |
| bots start in rooma | always | always |

**Deviations:**
- The reference maps are six hand-made layouts; the generator samples random maps of the same two families.
- Reference weights lean towards 1 (many tasks use only weight 1); set `max_weight=1` for those.
