# driverlog (ipc)

Drivers walk along paths and drive trucks along roads to deliver packages, and drivers and trucks may also have goal locations.

## Source

- **Domain:** Derek Long and Maria Fox, IPC 2002 (untyped STRIPS encoding with type predicates)
- **Generator:** `driverlog/generator.cc` (dlgen, IPC 2002), STRIPS mode without distances; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/driverlog`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | road junctions `s*` | 3–20 |
| `num_drivers` | drivers | 2–8 |
| `num_packages` | packages | 2–25 |
| `num_trucks` | trucks | 2–6 |
| `typed` | Autoscale's typed encoding instead of type predicates | IPC: off |

## Distribution

### Objects
Junctions `s*`, one path location `p{a}-{b}` per directed foot-path edge, `driver*`, `truck*` and `package*`. Untyped: kinds are given by `driver`, `truck`, `obj` and `location` facts.

### Initial state
- Foot paths and roads are two random directed graphs, drawn interleaved per junction with two path attempts and four road attempts; each graph is then connected by chaining unreached junctions.
- Every foot-path edge runs through its own path location; as upstream, the unused `p{b}-{a}` of a two-way pair is also declared.
- Drivers, trucks and packages start at uniformly random junctions; trucks are `empty`.
- Fact order as in the IPC tasks: each object's `at` fact followed by its type fact (trucks also `empty`), then all `location` facts, then `path` and `link`.

### Goal
Every driver, truck and package draws a uniformly random destination, which may equal its start. Drivers and trucks keep it as a goal with probability 0.7, packages with probability 0.95.

### Other
No action costs. Problem name `dlog-l{junctions}-{drivers}-{trucks}-{packages}`. Both graphs are connected, so every task is solvable.

## Comparison with reference tasks

All 20 IPC tasks, each regenerated at its own junctions, drivers, packages and trucks (10 seeds):

| aspect | reference tasks | this generator |
|---|---|---|
| `link` facts per junction | 4.06 | 3.91 |
| path locations per junction | 1.45 | 1.47 |
| goal rate drivers / trucks / packages | 0.67 / 0.72 / 0.96 | 0.74 / 0.65 / 0.94 |
| goals equal to the start | 0.18 | 0.16 |

**Deviations:**
- Problem names encode the parameters (IPC: `DLOG-{drivers}-{trucks}-{packages}`).
- Driver and truck goal rates differ by about 0.07 in opposite directions; the IPC set has only 61 drivers and 60 trucks, so this is within seed noise.
