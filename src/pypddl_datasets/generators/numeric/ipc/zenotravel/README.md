# zenotravel (numeric/ipc)

Planes with fuel, burn rates and passenger limits fly people between cities.

## Source

- **Domain:** Zenotravel, IPC 2002 numeric track (the domain file says "Author unknown"); IPC 2023 encoding with `located` and domain name `zenotravel`
- **Generator:** port of `pddl-generators/zenotravel/zenogenerator.cc` in numeric mode (`ztravel -n <seed> <cities> <planes> <people> <distance>`), the generator of the IPC 2002 numeric tasks; Python port in `generator.py`
- **Reference tasks:** `data/numeric/ipc2023/zenotravel`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cities` | cities | 3–35 |
| `num_planes` | planes | 1–5 |
| `num_people` | people | 3–40 |
| `distance` | distance bound | 1000 (tasks 1–17), 50 (tasks 18–20) |
| `metric` | `weighted` (`w2·total-time + w1·total-fuel-used`) or `fuel` | 18 weighted, 2 fuel |

## Distribution

### Objects
`plane1..`, `person1..`, `city0..`.

### Initial state
- Distances between distinct cities uniform in `[distance/2, distance)`, symmetric; distance 0 to the city itself.
- Each plane at a uniform city, slow burn 1..5, fuel uniform below `slow_burn·distance`, capacity `(2.1+u)·slow_burn·distance`, fast burn `(2+2u)·slow_burn`, zoom limit 1..10, onboard 0 (u uniform in [0,1)).
- Each person at a uniform city; `total-fuel-used` 0 (and `total-time` 0 with the weighted metric).

### Goal
Planes keep a destination goal with probability 0.3, people with probability 0.97; destinations are uniform and may equal the start. A task can end up with no goals.

### Other
Weighted metric with `w1, w2` uniform in 1..5 (as upstream); no action increases `total-time`. Name `ztravel-<cities>-<planes>-<people>`.

## Comparison with reference tasks

All 20 tasks regenerated at their sizes and distance bound, 10 seeds each:

| aspect | reference tasks | this generator |
|---|---|---|
| plane goal rate | 0.29 | 0.34 |
| person goal rate | 0.97 | 0.97 |
| fast burn / slow burn | 2.69 | 2.77 |
| capacity / (slow burn · max distance) | 2.71 | 2.67 |
| fuel / (slow burn · max distance) | 0.51 | 0.50 |
| zoom limit | 5.4 | 5.4 |

**Deviations:** IPC task names encode planes and people but, in hand-edited tasks such as pfile1, not always the actual counts.
