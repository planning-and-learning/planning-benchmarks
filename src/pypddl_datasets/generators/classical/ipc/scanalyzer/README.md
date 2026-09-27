# scanalyzer (ipc)

Plants on conveyor belt segments must be analyzed by rotating them through cycles of segments, some of which pass an imaging station.

## Source

- **Domain:** Malte Helmert, IPC 2008 (based on the LemnaTec Scanalyzer 3D)
- **Generator:** `scanalyzer/generator.py` from pddl-generators (IPC 2008 organizers); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/scanalyzer-08-strips`, `scanalyzer-opt11-strips`, `scanalyzer-sat11-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `size` | segments per side (in and out) | 3–9 with `empty`, 1–3 with `ab` |
| `segment_type` | `empty`: whole segments with 2-cycles; `ab`: split into halves a/b with 4-cycles | both |
| `inout` | segments connected to the analysis station: `none` (1×1), `in` (size×1), `both` (size×size) | all three |

## Distribution

### Objects
- For each side and segment `k`, there is a segment `seg-<in|out>-<k>` and a car `car-<in|out>-<k>`.
- With `ab`, each of those is split into halves `…a` and `…b`.

### Initial state
- Each car starts on its own segment.
- For every pair of an in-segment and an out-segment there is a `cycle-2`, or a `cycle-4` with `ab`.
- The first `num_in × num_out` pairs are also `…-with-analysis`.
- `(= (total-cost) 0)`.

### Goal
- Every car is `analyzed`.
- With `empty`, every car returns to its own segment.
- With `ab`, halves are swapped, and the a-halves move to the opposite side under the fixed permutation `[0, size-1, …, 1]`.

### Other
- Action costs with `(:metric minimize (total-cost))`.
- Deterministic, with no seed.
- The problem is named `scanalyzer3d-<size>-<segment_type>-<inout>`.
- Upstream's `(1, size)` and `simple` problem types are not offered, because no IPC task uses them.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| init and goal fact sets (50 IPC tasks, 30 distinct) | — | identical for all 50 tasks |
| IPC numbering | `scanalyzer3d-<5·(size−1) + type + 50·[ab]>`, type 1/2/4 = none/in/both | `scanalyzer3d-<size>-<type>-<inout>` |
| duplicates | tasks 51, 52 and 54 are identical (size 1, `ab`, where `inout` has no effect) | same, since the output depends only on the parameters |

**Deviations:** none in content. Only the problem names differ.
