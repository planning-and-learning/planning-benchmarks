# scanalyzer (autoscale)

Plants on conveyor belt segments must be analyzed by rotating them through cycles of segments, some of which pass an imaging station.

## Source

- **Domain:** Malte Helmert, IPC 2008
- **Generator:** `scanalyzer/generator.py` from pddl-generators, called as `generator.py {size} {segment_type} {inout}`; re-exports `ipc/scanalyzer` (same distribution, Autoscale's domain file)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/scanalyzer` (also `21.11-optimal-strips/scanalyzer`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `size` | segments per side | 4–33 |
| `segment_type` | `empty` or `ab` | `empty` |
| `inout` | `none`, `in` or `both` | `in` |

## Distribution

### Objects
See `ipc/scanalyzer`: a segment and a car per side and segment (halves with `ab`).

### Initial state
Cars on their own segments, all in×out cycles, and the analysis cycles given by `inout`. See `ipc/scanalyzer`.

### Goal
All cars analyzed and back on their segments (permuted halves with `ab`).

### Other
- Action costs.
- Deterministic.
- The problem is named `scanalyzer3d-<size>-<segment_type>-<inout>`, as in the agile tasks.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| init and goal fact sets (30 agile tasks) | — | identical in 30/30 |
| problem names | `scanalyzer3d-<size>-empty-in` | identical |

**Deviations:** none found.
