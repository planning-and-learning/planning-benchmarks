# driverlog (autoscale)

Drivers walk along paths and drive trucks along roads to deliver packages, and drivers and trucks may also have goal locations.

## Source

- **Domain:** Derek Long and Maria Fox, IPC 2002, typed STRIPS encoding shipped with Autoscale
- **Generator:** `driverlog/generator.cc` (dlgen, IPC 2002), called by Autoscale as `dlgen {seed} {roadjunctions} {drivers} {packages} {trucks}` (typed, no distances). This package re-exports `../../ipc/driverlog` with `typed=True`.
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/driverlog`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/driverlog`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | road junctions `s*` | agile: 10–126 |
| `num_drivers` | drivers | agile: 4–6 |
| `num_packages` | packages | agile: 12–136 |
| `num_trucks` | trucks (Autoscale: `drivers + 0..1`) | agile: 4–6 |

## Distribution

### Objects
Same as `ipc/driverlog`, declared with types: `driver`, `truck`, `obj` (packages) and `location` (junctions and path locations).

### Initial state
Same distribution as `ipc/driverlog`, without the type facts.

### Goal
Same as `ipc/driverlog`: destinations uniform, possibly the start; kept with probability 0.7 for drivers and trucks, 0.95 for packages.

### Other
No action costs. Problem name `dlog-l{junctions}-{drivers}-{trucks}-{packages}` (Autoscale: `DLOG-{drivers}-{trucks}-{packages}`). Tasks are solvable.

## Comparison with reference tasks

30 agile tasks, each generated at its own junctions, drivers, trucks and packages (1 seed):

| aspect | reference tasks | this generator |
|---|---|---|
| drivers / trucks / packages | 148 / 148 / 2215 | identical |
| location objects (junctions + path locations) | 6276 | 6246 |
| init `link` / `path` | 15280 / 16916 | 15324 / 16772 |
| goal `at` | 2301 | 2332 |

**Deviations:**
- Problem names add the junction count (`dlog-l{junctions}-...`).
- Otherwise none found beyond seed noise.
