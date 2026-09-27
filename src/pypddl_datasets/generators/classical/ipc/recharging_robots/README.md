# recharging_robots (ipc)

Guard robots with limited batteries move over a roadmap, share charge with each other, and either guard areas or reach target locations.

## Source

- **Domain:** Daniel Gnad and Álvaro Torralba (with Daniel Fišer), IPC 2023; dedicated to the public domain
- **Generator:** `generator.py` from [ipc2023-classical/domain-recharging-robots](https://github.com/ipc2023-classical/domain-recharging-robots) (same authors, public domain), scenarios `covers` and `single-source-move-to-locations`; Python port in `generator.py` (scipy Delaunay, shapely, networkx and the CPLEX covering models replaced by pure Python)
- **Reference tasks:** `data/classical/downward-benchmarks/recharging-robots-opt23-adl`, `data/classical/downward-benchmarks/recharging-robots-sat23-adl` (identical domain files)

## Parameters

| parameter | meaning | reference range (IPC task headers) |
|---|---|---|
| `kind` | `covers` or `single-source-move-to-locations` | 31 / 9 tasks |
| `num_robots` | robots | 2–6 |
| `num_obstacles` | square obstacles (4 locations each) | 5, 7, 8, 10 |
| `num_viewpoints` | additional random locations | 10–30 |
| `charge_multiplier` | total battery = optimal movement cost × this | 1 |
| `min_cover` | covers: robots needed to guard each area | 1–5 |
| `num_areas` | covers: areas to guard in turn | 1–3 |
| `move_from_source` | single-source: robots first moved away from the common source | 5 of 9 tasks |
| `max_distance`, `max_square_width` | longest road, largest obstacle side | 0.35, 0.3 (defaults) |

## Distribution

### Objects
`location-<i>` for the viewpoints and obstacle corners, `robot-<i>`, `battery-<0..total>`, and `config-<i>` per area (covers only).

### Initial state
- Obstacles: squares with side uniform in [0.08, `max_square_width`] in the unit square, at least 0.05 apart. Viewpoints uniform in [0.01, 0.99]², at least 0.1 from each other and 0.05 from obstacles.
- Roads (`connected`): the Delaunay triangulation of all locations without edges longer than `max_distance` and without square diagonals; the map is redrawn until connected.
- covers: areas are the largest distance balls around random centres (not in earlier areas) that `min_cover` robots can guard; robots start at distinct random locations outside all areas. The order of areas and the robot moves minimising total movement (rendezvous at the best meeting point, then optimal guarding assignments) fix the required charge; charge is the rendezvous distance per robot plus a random split of the rest, resampled until some robot must be recharged. `guard-config` lists each area.
- single-source: robots start at one random location (or, with `move_from_source`, at random locations from which the source is on a shortest path to their target, with the detour added to their charge); total charge = summed source–target distances × multiplier, split randomly.
- `(= (move-cost) 1)`, `(= (recharge-cost) 1)`, `(= (total-cost) 0)`, the battery predecessor chain.

### Goal
covers: `(config-fullfilled config-<i>)` for every area. single-source: every robot at its own distinct target location.

### Other
`(:metric minimize (total-cost))`. Solvable by construction (upstream's plan: rendezvous, redistribute charge, then move). Where upstream exits or loops (not enough locations outside the areas, no area of exactly `min_cover`, no charge split that needs a recharge) the port redraws the map. Names follow upstream (`recharging-robots-cover-robots<r>-areas<a>-<seed>-<rnd>`, `recharge-single-source-move-to-locations-<rnd>`).

## Comparison with reference tasks

All 40 IPC tasks regenerated at the parameters in their headers (3 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| covers: locations | 57.61 | 57.61 |
| covers: roads | 144.87 | 144.72 |
| covers: `guard-config` facts | 27.58 | 27.28 |
| covers: total battery | 24.23 | 24.85 |
| covers: guard configurations | 1.77 | 1.77 |
| single-source: locations | 37.89 | 37.89 |
| single-source: roads | 88.33 | 88.85 |
| single-source: total battery | 16.89 | 16.67 |
| single-source: robot goals | 4.22 | 4.22 |
| mean road degree (covers / single-source) | 4.99 / 4.64 | 4.98 / 4.66 |

**Deviations:**
- The triangulation of cocircular obstacle corners may pick another diagonal than qhull; diagonals are dropped anyway.
- Among equally cheap guarding assignments the port picks a different one than CPLEX may.
- The unused scenario `single-source-cover` is not ported.
