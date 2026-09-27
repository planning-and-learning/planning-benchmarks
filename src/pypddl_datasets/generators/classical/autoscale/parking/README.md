# parking (autoscale)

Rearrange cars on a street of curbs where cars may be double- but not triple-parked.

## Source

- **Domain:** Parking, IPC 2011/2014; Autoscale's copy (adds `:negative-preconditions`, `:equality` and `(not (= ...))` guards), lowercased
- **Generator:** Autoscale's `pddl-generators/parking/parking-generator.pl`, called as `parking-generator.pl prob {curbs} {cars} seq` with `cars = 2·(curbs − 1) + cars_diff`, `cars_diff ∈ {0, −1, −2}`; re-exports `../../ipc/parking` (same distribution)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/parking`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/parking`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_curbs` | curb locations | agile: 9–43, optimal: 3–17 |
| `num_cars` | cars, `2·(curbs − 1) + cars_diff` | agile: 16–84 (diff 0), optimal: 4–30 (diff −2..0) |

## Distribution

### Objects
`car_{i}`, `curb_{i}`, zero-padded to the widest index.

### Initial state
Shuffled cars; a uniform number between `ceil(cars/2)` and `min(curbs, cars)` stand at the first curbs, the rest behind them; `curb-clear` for free curbs; `(= (total-cost) 0)`.

### Goal
Canonical layout: `car_i` at `curb_i`, the remaining cars behind cars 0, 1, ….

### Other
Unit action costs, `(:metric minimize (total-cost))`. Problem name `parking-c{curbs}-n{cars}` (Autoscale: `parking`). See `../../ipc/parking`.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| `cars − 2·(curbs − 1)` | agile {0}, optimal {−2, −1, 0} | any `cars <= 2·(curbs − 1)` |
| object naming | `car_00`, `curb_0` (padded to width) | same |
| goal layout | canonical | canonical |
| problem name | `parking` | `parking-c{curbs}-n{cars}` |

**Deviations:** none found in the distribution; only the problem name differs.
