# settlers_snp (numeric/ipc)

Settlers resource management: gather and process resources, build vehicles, houses, industries and rails.

## Source

- **Domain:** Enrico Scala and Miquel Ramirez's encoding of Patrik Haslum's IPC 2002 Settlers (IPC 2026 `settlers-snp`); `domain.pddl` is the IPC file
- **Generator:** reconstruction from the reference tasks (no generator was published; pddl-generators' settlers is Marcel Steinmetz's discretized variant with another encoding); `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/settlers-snp`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | locations | 5–15 |
| `num_vehicles` | potential vehicles (default `min(n, 10)`) | 5–10 |
| `num_goals` | goal facts (default uniform in `[n−2, 1.6n]`) | 3–25 |
| `land_density` | fraction of location pairs with roads (default 0.8 − 0.025n) | 2.45 roads per location |

## Distribution

### Objects
`location0..`, `vehicle0..` (declared in reverse order, as the references).

### Initial state
All counters 0 (labour, pollution, resource-use, housing, every `available`, `space-in`). Each location is independently woodland (0.74), mountain (0.44), by-coast (0.52), metalliferous (0.29), each property present somewhere. Roads: random spanning tree plus random pairs up to `land_density`, both directions. Sea links: random coastal pairs (0 to #coastal). Every vehicle `potential`.

### Goal
Draws from housing ≥ 1 or 2, `has-coal-stack`, `has-sawmill`, `has-ironworks` at uniform locations, and rail links as walks of 1–5 roads (rails can only be built along roads), without duplicates.

### Other
`(:metric minimize (+ (+ (* 1 (pollution)) (* 1 (resource-use))) (* 1 (labour))))`, as all references.

## Comparison with reference tasks

All 20 reference tasks regenerated at their locations, vehicles and goal counts (5 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| woodland / mountain / by-coast / metalliferous | 0.74 / 0.44 / 0.52 / 0.29 | 0.69 / 0.48 / 0.48 / 0.25 |
| roads per location | 2.45 | 2.29 |
| sea links per task | 2.15 | 2.21 |
| goal kinds rail / housing / ironworks / sawmill / coal | 0.44 / 0.19 / 0.13 / 0.13 / 0.11 | 0.42 / 0.17 / 0.15 / 0.16 / 0.10 |

**Deviations:** 4 of the 106 reference rail goals lie on pairs without a road, which makes those tasks unsolvable; the generator only asks for buildable rails.
