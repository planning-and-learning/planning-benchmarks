# Declarative Rovers graph experiment

This experiment asks whether changing the graph construction makes the existing
ProbLog backend scale better. It does not establish feasibility for all domains,
and it does not add a new native graph sampler or change a production generator.

The models use the installed ProbLog 2.3.0 parser and engine, plus the repository's
existing sampling integration and accelerated generic choice/list operations.
Every new sampling rule is written in ProbLog. Python only composes the source,
runs isolated measurements, decodes outputs, and renders PDDL.

## Compared graph laws

- **Current:** independent visibility edges at probability 0.5, rejecting
  disconnected graphs; each rover independently samples a connected subgraph at
  the same probability, with the production local retry budgets.
- **Sparse:** grow a tree with a uniformly shuffled vertex order and a uniform
  earlier parent for each new vertex. Make four random endpoint-pair attempts per
  waypoint, discard loops/duplicates, and add their edges to the tree. Each rover
  retains that shared tree and independently takes each extra edge with
  probability 3/10. Visibility has at most `5n - 1` undirected edges. This is a
  sparse structural proxy, not the classic IPC probability law: classic IPC uses
  connectivity repair and different exploration trees covering reachable subsets.
- **IPC 2023 graphs:** grow the same kind of randomly relabeled recursive tree;
  choose the total number of visibility edges uniformly from `n-1` through
  `n(n-1)/2`; choose the additional edges uniformly without replacement. Each rover
  retains the shared tree and independently takes each extra edge with probability
  3/10. This matches the graph construction in the
  [official graph utility](https://github.com/ipc2023-learning/benchmarks/blob/main/benchmarking_utils.py)
  and [Rovers model](https://github.com/ipc2023-learning/benchmarks/blob/main/rovers/rovers.py),
  not the remaining equipment, placement, and goal laws of that generator.

All three variants span every waypoint. This preserves the full-reachability
assumption used by the repository's sample-goal rules. All nongraph rules are
inherited from the production model; graph-dependent image-goal probabilities
naturally change with the graph. Equal seeds do not imply equal tasks across laws.

The reusable declarations are in
[`graph_samplers.pl`](../experiments/problog/graph_samplers.pl) (54 lines), with a
17-line [Rovers composition](../experiments/problog/rovers_graphs.pl).
Uniform integer draws use binary interval splitting, and fixed-cardinality
subsets use an exact `K/N` inclusion probability while scanning candidates.
These avoid huge integer lists and repeated selection/removal of graph edges.
The implementation still represents graphs as Prolog edge lists.

## Measurement policy

The harness is [`compare_graph_models.py`](../experiments/problog/compare_graph_models.py).
Each configuration runs in a fresh subprocess with a 2 GiB address-space limit.
Full-task timing includes source assembly, sampling, decoding, and PDDL rendering;
imports are reported separately. The first draw prepares the model and later
seeds reuse the prepared program. RSS is the worker's high-water mark, including
imports and caches, not graph storage alone. Graph diagnostics and hashes are
computed after full-task timing. Completed seeds are retained if a later seed
hits the total worker deadline. A timeout is a censored measurement.

Cases inherit parameters from the existing benchmark: 25 waypoints/10 rovers,
100 waypoints/14 rovers, 197 waypoints/30 rovers, and 1,000 waypoints/1 rover.
Their remaining object and goal parameters are recorded in the JSON artifacts.
The IPC-shaped cases are complete tasks under the experiment's hybrid laws;
object counts matching an IPC instance do not reproduce that instance.

Small exact-law checks overlapped with parts of the initial run. The extended
100-waypoint IPC run and larger sparse survey ran without other generation
benchmarks. Load averages and source hashes are recorded for each case. The small
seed counts support a feasibility check, not stable latency quantiles.

## Results

Full-task results, three seeds per row:

| Waypoints | Graph law | Mean time | Individual times, range | Peak RSS |
|---:|---|---:|---:|---:|
| 25 | current | 1.61 s | 1.42–1.81 s | 51.6 MiB |
| 25 | sparse | 2.38 s | 2.32–2.44 s | 53.6 MiB |
| 25 | ipc2023 | 1.65 s | 1.41–2.04 s | 56.7 MiB |
| 100 | current | 18.85 s | 17.53–19.92 s | 245.7 MiB |
| 100 | sparse | 15.31 s | 14.88–15.92 s | 151.8 MiB |
| 100 | ipc2023 | 44.37 s | 38.76–49.70 s | 297.7 MiB |

The sparse construction was slower at 25 waypoints. At 100 it reduced mean task
time by about 19% and peak RSS by about 38%, while reducing visibility edges from
roughly 2,450 to 470. This is a useful memory improvement but a modest latency
improvement for such a large reduction in edge count.

IPC 2023 samples have much higher edge-count variance than the current Bernoulli
law. The three 100-waypoint draws contained 4,195, 2,486, and 4,461 visibility
edges. These few draws are not an estimate of its typical density or latency.
Even the middle draw, with an edge count close to the current model, took 38.76 s.
The initial 75-second total worker budget retained only the first of three tasks;
the extended 180-second run completed all three, in 134.57 s including setup and
per-task diagnostics. No successful sample was discarded from the raw reports.

Graph-only measurements use seed 0 and produce compact counts instead of PDDL:

| Waypoints | Graph law | Graph-only time | Peak RSS |
|---:|---|---:|---:|
| 100 | current | 2.70 s | 52.9 MiB |
| 100 | sparse | 7.79 s | 72.6 MiB |
| 100 | ipc2023 | 25.23 s | 108.5 MiB |
| 197 | current | 20.41 s | 140.0 MiB |
| 197 | sparse | 19.02 s | 123.0 MiB |
| 197 | ipc2023 | No result within 75 s | 98.1 MiB |

Smaller graphs do not automatically make these declarative constructions faster.
The current graph law already uses accelerated bulk Bernoulli subset draws;
the tree growth, fixed-cardinality scan, and sparse edge-attempt composition are
new interpreted rules. They still create, traverse, and match Prolog edge lists.
These timings assess this implementation, not the achievable performance of
future native implementations of the same graph primitives. Graph-only queries
have different evaluation behavior from full tasks, so their times should not
be subtracted as an exact profile of nongraph work.

Larger complete-task attempts, one seed each:

| Waypoints | Rovers | Graph law | Outcome | Peak RSS at timeout |
|---:|---:|---|---|---:|
| 197 | 30 | sparse | No task within 75 s | 1573.6 MiB |
| 1000 | 1 | sparse | No task within 75 s | 592.2 MiB |

For the 197-waypoint case, sparse graphs alone completed in 19.02 s and 123 MiB,
but producing the complete task exceeded 75 s and reached approximately 1.54 GiB.
Full-task evaluation, including repeated graph queries and graph-dependent goal
construction, remains a substantial cost. The 1,000-waypoint sparse case also
exceeded the bound. There is no evidence here that all generators would become
practical after introducing graph abstractions.

The next bounded investigation would be a native implementation of one shared
graph operation while keeping these declarative definitions as its reference.
It should be validated against the tiny joint laws and measured on complete tasks.
The experiment does not justify a wider migration or a replacement interpreter.

Raw artifacts:

- [Initial full-task matrix](../experiments/problog/performance/graph-models-initial.json)
- [Completed IPC 2023 100-waypoint run](../experiments/problog/performance/graph-models-ipc2023-100.json)
- [Graph-only comparison](../experiments/problog/performance/graph-models-graphs.json)
- [Larger sparse task attempts](../experiments/problog/performance/graph-models-large-sparse.json)

## Validation

All 16 targeted tests passed. They check exact integer and fixed-size subset laws,
the growing-tree star probability on four vertices (1/3, versus 1/4 for a uniform
labeled tree), and all 15 positive joint outcomes for three vertices and two
rovers. The latter checks both exact inference and an exhaustive enumeration of
the accelerated sampler's random histories, including the shared-backbone
correlation and independent 3/10 extra-edge decisions. Boundary/support checks
cover one, two, and eight waypoints, connectivity, no loops/duplicates, movement
containment, and backbone inclusion. The production model source is unchanged.

The experiment loader and test module pass Pyright and Pylint.

```sh
.venv/bin/python -m pytest tests/test_problog_graph_models.py -q
.venv/bin/python experiments/problog/compare_graph_models.py \
  --case rovers-downward-medium --case rovers-downward-large \
  --samples 3 --timeout 75 --output /tmp/graph-models.json
.venv/bin/python experiments/problog/compare_graph_models.py \
  --case rovers-downward-large --case rovers-ipc-large --graph-only \
  --samples 1 --timeout 75 --output /tmp/graph-only.json
```
