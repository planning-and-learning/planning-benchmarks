# rovers (ipc_learning)

Rovers collect soil, rock and image data and send it to a lander.

## Source

- **Domain:** IPC 2002; learning-track encoding without `channel_free` and `available`
- **Generator:** generator as of 2026-09-27 (commit HEAD, `classical/rovers`), learning-track domain file; no `channel_free`/`available` facts (not in the learning domain)
- **Reference tasks:** `data/classical/ipc2023-learning/rovers_ipc2023_learning` (easy/medium/hard, 90 tasks); the learning track's own generator is `rovers/rovers.py` in [ipc2023-learning/benchmarks](https://github.com/ipc2023-learning/benchmarks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rovers` | rovers | 1–30 |
| `num_waypoints` | waypoints | 4–197 |
| `num_objectives` | objectives | 1–236 |
| `num_cameras` | cameras | 1–99 |
| `num_goals` | rovgen goal-density parameter (ignored with `learning_goals`) | 1–~400 |
| `learning_graphs` | visibility edge count uniform between a tree and the complete graph; each rover also traverses each visible edge between reached waypoints with probability 0.3 (default, learning track) | on |
| `learning_goals` | each goal type's count uniform in 0..available, at least one goal overall (default, learning track) | on |

## Distribution

### Objects
Rovers with stores, waypoints, cameras, modes colour/high_res/low_res, objectives, lander `general`.

### Initial state
Random connected visibility graph, by default densified to a uniform edge count between a tree and the complete graph; per-rover traversal subgraphs (plus 30% of the visible edges among reached waypoints by default); samples, equipment, cameras with calibration targets.

### Goal
Soil, rock and image communication goals; by default each type's count is uniform in 0..available, so a type can be missing.

### Other
No action costs.

## Comparison with reference tasks

Easy and medium learning test tasks regenerated at the parameters in their header comment.

| aspect | reference tasks | this generator (default / both options off) |
|---|---|---|
| soil / rock goals per waypoint | 0.243 / 0.280 | 0.226 / 0.258, 0.417 / 0.471 |
| image goals per objective | 1.684 | 2.454 / 1.183 |
| tasks without an image goal | 0.033 | 0.017 / 0.000 |
| `visible` per waypoint | 14.0 | 14.8 / 6.6 |
| `can_traverse` per rover-waypoint | 5.5 | 5.6 / 1.7 |

**Deviations:**
- More image goals per objective (2.45 vs 1.68): frequency difference only.
