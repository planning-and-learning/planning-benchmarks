# parking (ipc)

Rearrange cars on a street of curbs where cars may be double- but not triple-parked.

## Source

- **Domain:** Parking (isomorphic to a bounded-table Blocksworld with towers of height ≤ 2), IPC 2011 and IPC 2014
- **Generator:** pddl-generators `parking/parking-generator.pl` (seq mode); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/parking-opt11-strips`, `data/classical/downward-benchmarks/parking-sat11-strips`, `data/classical/downward-benchmarks/parking-opt14-strips`, `data/classical/downward-benchmarks/parking-sat14-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_curbs` | curb locations | opt11: 7–12, sat11: 12–17, opt14: 7–11, sat14: 15–21 |
| `num_cars` | cars, at most `2·(curbs − 1)` | always `2·(curbs − 1)` |

## Distribution

### Objects
`car_{i}` and `curb_{i}`, zero-padded to the width of the largest index.

### Initial state
Cars in uniformly shuffled order; a uniform number between `ceil(cars/2)` and `min(curbs, cars)` of them stand directly at the first curbs, the rest double-park behind them in order. Facts: `at-curb`, `at-curb-num`, `behind-car`, `car-clear`, `curb-clear` for free curbs, `(= (total-cost) 0)`.

### Goal
The canonical layout: `car_i` at `curb_i` for the first `min(curbs, cars)` cars, the remaining cars behind cars 0, 1, … (`at-curb-num` and `behind-car` goals).

### Other
Unit action costs, `(:metric minimize (total-cost))`. Problem name `parking-c{curbs}-n{cars}`. Solvable for `cars <= 2·(curbs − 1)` (one free curb space).

## Comparison with reference tasks

| aspect | reference tasks (80) | this generator (`cars = 2·(curbs − 1)`) |
|---|---|---|
| cars | 2·(curbs − 1) in 80/80 | same |
| goal facts | curbs `at-curb-num` + (curbs − 2) `behind-car`, canonical in 80/80 | same |
| tasks with one free curb initially | 42/80 | 39/80 |
| cost facts and metric | yes | yes |
| object names | `car_00`, `curb_00` (padded) | same |
| problem name | `parking` | `parking-c{curbs}-n{cars}` |

**Deviations:** none found in the distribution. The domain file is the IPC 2014 one; the IPC 2011 domain is identical apart from whitespace.
