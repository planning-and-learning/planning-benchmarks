# ProbLog pilot performance

The shared runtime now generates the tested 25-waypoint Rovers task in **1.52
seconds**, compared with **73.47 seconds** for the same corrected model under
interpreted ProbLog. The 100-waypoint configuration completes in **17–19 seconds**
per task. The frozen imperative generators remain substantially faster: about
**8.23 milliseconds** and **0.69 seconds**, respectively. These improvements make
larger offline runs possible; they do not close the performance gap with Python.

## Current measurements

The [final optimized matrix](../experiments/problog/performance/runtime-comparison.json)
and [four-mode baseline](../experiments/problog/performance/runtime-stage1.json)
were recorded on 2026-09-16 with Python 3.13.2, ProbLog 2.3.0 and Linux x86-64
(glibc 2.39), on a shared host reporting 16 CPUs. The baseline ran alongside the
independent single-core distribution proof and occasional development probes.
The final optimized measurements started after those checks finished. Host load
is recorded; these are approximate shared-machine observations.

The interpreted baseline uses the **current corrected declarative models** with
native specialization disabled. After that baseline, the final sampler added
whole-selector memoization and avoided recomputing probabilities for cached
primitive heads. The models, Prolog library and exact-inference implementation
did not change. Each artifact retains its own complete source hashes. Every
measured case had unchanged sources during execution, and every overlapping
ProbLog seed produced the same PDDL fingerprint across both optimization stages
and both preparation policies.

After measurements, one fallback-only correction normalized quoted predicate
names in the primitive-extension guard. No bundled domain extends a primitive.
A [separate validation](../experiments/problog/performance/post-measurement-validation.json)
checks that all 16 measured model sources retain the same specialization decision
and identifies the sole changed backend file and its before/after hashes. The
original timing artifacts are unchanged; the large probes were not repeated for
this guard correction.

| Configuration | Imperative mean (ms) | Interpreted first task (s) | Optimized fresh first task (s) | Optimized cached warm tasks (s) | Cached peak RSS (MiB) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Ferry `(17,12)` | 0.206 | 0.304 | 0.067 | 0.034–0.035 | 38.1 |
| Delivery `(13,12)` | 1.108 | 2.397 | 0.403 | 0.402–0.404 | 44.6 |
| Rovers: 10 waypoints | 0.648 | 3.547 | 0.388 | 0.273–0.355 | 42.1 |
| Rovers: 15 waypoints | 1.855 | 12.552 | 0.585 | 0.554–0.676 | 46.2 |
| Rovers: 25 waypoints | 8.231 | 73.470 | 1.524 | 1.436–1.796 | 51.8 |
| Rovers: 100 waypoints | 693.036 | No task in 75 s | 17.104 | 18.195–19.008 | 231.3 |

Imperative means cover 100 seeds. The interpreted baseline requests seed 0; the
optimized modes request seeds 0, 1 and 2. Fresh comparisons therefore use the same
seed, while the warm range is only seeds 1 and 2, not an estimate of tail latency.
All **36 final optimized tasks** completed without a generation exception. At 100
waypoints, the interpreted worker produced no task within its 75-second total
budget and reached **1,458.6 MiB** RSS. The final optimized cached worker completed
all three tasks within 56 seconds total wall time, peaking at **231.3 MiB**.

For the five configurations with completed interpreted observations, the
same-seed first-task speedups are approximately **4.5×, 6.0×, 9.1×, 21.5× and
48.2×**, in table order. Cached warm means are still roughly **170–480×** the
imperative means for the smaller configurations and **27×** at 100 waypoints.
Startup/import setup adds about 0.07 seconds to optimized workers and 0.05 seconds
to imperative workers; those values are reported separately from task time.

The [remaining size-survey cases](../experiments/problog/performance/current-range.json)
use the final runtime, one cold seed-0 task per process, the same 75-second total
budget and a 2 GiB address-space cap:

| Configuration | Outcome | Peak RSS (MiB) |
| --- | --- | ---: |
| `ferry-train-max` | 0.045 s | 37.2 |
| `ferry-valid-max` | 0.052 s | 36.9 |
| `delivery-train-max` | 0.098 s | 37.8 |
| `delivery-valid-max` | 0.180 s | 37.5 |
| `rovers-test` | 0.120 s | 38.8 |
| `rovers-downward-small` | 0.145 s | 38.3 |
| `rovers-ipc-medium` | 9.039 s | 131.5 |
| `rovers-ipc-large` | No task in 75 s (timeout) | 555.5 |
| `rovers-htg-small` | No task in 75 s (timeout) | 671.8 |
| `rovers-htg-large` | No task in 75 s (timeout) | 890.1 |

Timeouts and resource failures establish limits of this measured budget, not a
proof that a configuration can never finish. A model-declared graph-retry
exhaustion is reported separately from those resource outcomes. Small samples
cannot estimate rare failure probabilities; the independent correctness checks
cover the finite retry law and rare numeric outcomes.

## Practical range and migration decision

Ferry and Delivery complete at all committed split extrema. The selected Rovers
settings through the Downward 100-waypoint case and the IPC medium case complete
within the measurement budget. The larger IPC and HTG settings remain outside
the demonstrated useful range under this budget; their observations above must
be considered before expanding the migration. These statements apply to the
listed parameter tuples, not every task with the same waypoint count.

At the observed warm rates, 1,000 serial 25-waypoint tasks would take roughly
27 minutes, and 1,000 serial 100-waypoint tasks roughly five hours. These are
simple throughput extrapolations, not measured thousand-task batches. Whether
that is acceptable depends on the intended dataset volume.

**Keep broad migration on hold.** Continue with the three-domain pilot and its
independent distribution checks. The optimized shared operations substantially
improve generation, but the large imperative gap and the remaining large-case
limits do not justify converting every generator yet. Further substantial gains
would require reducing repeated logical evaluation or compiling a larger portion
of deterministic model execution. Compact domain files do not mean the runtime
as a whole has become simpler.

## Why time and memory grow

Generation samples **one world**. It does not enumerate all possible tasks; the
exhaustive distribution verifier is a separate inference workload. Sampling still
runs through ProbLog's general-purpose query engine, which constructs logical
terms, unifies arguments, stores intermediate query answers and handles nested
`findall` calls before the PDDL problem can be decoded.

An archived [development profile](../experiments/problog/performance/rovers-25-stage1-profile.txt)
recorded about **10.1 million Python function calls** for one warm 25-waypoint
world, after native list membership but before the final selector-cache change.
The profile includes 54 calls through `findall`, including nested evaluations,
and substantial term equality,
unification, result propagation and table-lookup work. Its instrumented time is
not a normal generation-time measurement. Native operations remove expensive
pieces of this evaluation, but the surrounding interpreter work remains.

Rovers also has inherent size growth: a complete undirected candidate graph has
`N*(N-1)/2` edges, rising from **300 at 25 waypoints to 4,950 at 100**. Each rover
adds movement relations, and objectives, cameras and goal attempts add more
queries and intermediate collections. The final 100-waypoint samples contain
about **40,000 initial facts**. ProbLog's term and table representations cost more
than the direct lists and sets used by the imperative sampler. Process RSS also
includes the interpreter, imports and cached preparation; it is not simply the
size of the emitted PDDL.

## Parameter provenance

Ferry and Delivery cases use the maximum of each parameter in their committed
split recipes:

| Domain | Train | Validation | Test |
| --- | --- | --- | --- |
| Ferry `(cars, locations)` | `(7,5)` | `(11,8)` | `(17,12)` |
| Delivery `(grid side, packages)` | `(5,4)` | `(8,7)` | `(13,12)` |

Rovers has no generated split recipe. Its configurations use object and goal
counts from named checked-in tasks, with the current default edge probability
0.5. For example, Downward `p14.pddl` supplies `(4,10,4,5,8)` and `p25.pddl`
supplies `(10,25,6,10,10)` in `(rovers, waypoints, objectives, cameras, goals)`
order. Every tuple and source path appears in the artifacts and
`benchmark.py --list`. These are valid current generator requests at repository
scales; they do not recover the original parameters, graph density or probability
law of the old task files. In particular, the default dense graph law makes the
1,000- and 5,500-waypoint HTG probes demanding even before interpreter overhead.

## Reproduce

Use a Linux checkout with the package installed. The
[comparison harness](../experiments/problog/compare_preparation.py) supports four
modes, each run in a separate bounded process:

| Mode | Implementation | Preparation policy |
| --- | --- | --- |
| `imperative` | Frozen pre-migration algorithm in `tests/reference_generators` | Ordinary Python construction |
| `interpreted` | Corrected declarative source, `accelerated=False` | New preparation for every task |
| `optimized-fresh` | Shared native operations and selector memoization | New preparation for every task |
| `optimized-cached` | Production runtime | Cold first task, then reused preparation |

```sh
python experiments/problog/benchmark.py --list
python experiments/problog/compare_preparation.py \
  --samples 3 --interpreted-samples 1 --imperative-samples 100 \
  --timeout 75 --memory-mib 2048 \
  --output /tmp/problog-runtime-comparison.json
```

The default comparison covers the six configurations in the first table. Repeat
`--case NAME` and `--mode MODE` to select configurations or execution modes. For
example, reproduce a large final-runtime probe with:

```sh
python experiments/problog/compare_preparation.py \
  --case rovers-ipc-large --mode optimized-cached --samples 1 \
  --timeout 75 --memory-mib 2048 --output /tmp/problog-large-probe.json
```

Each task timer includes model assembly and parameter validation where the
production ProbLog API performs them, sampling, decoding and PDDL rendering.
The imperative sampler receives its validated parameters once during setup,
matching its former `sample` interface. Imports are timed separately. Preparation
component probes run after the task measurements to leave the first task cold.
Peak RSS covers the whole process, including those probes; the address-space cap
is not an RSS cap. A supervisor records memory while a worker runs, retaining an
observation if it is killed, although a brief final peak can be missed.

Each case/mode has an aggregate time limit, not a per-task deadline. Completed
seeds are emitted immediately and retained after a later timeout. Artifacts
separate timeouts, crashes and generation exceptions, retain output hashes and
object/fact/goal counts, and hash sources before and after every case. The source
coverage includes backend Python and Prolog files, domain models, wrappers,
parameters, renderer, frozen reference algorithms and measurement scripts.
Preparation caching reuses exclusively borrowed programs within a thread; each
task gets fresh choices and grounding state. Exact inference retains ordinary
Prolog definitions. Correctness evidence is in the [pilot report](problog-pilot.md).

## Historical observations

The original [size survey](../experiments/problog/performance/benchmark.json),
[10/15-waypoint follow-up](../experiments/problog/performance/rovers-midpoints.json)
and [25-waypoint run](../experiments/problog/performance/rovers-25.json) predate
both runtime acceleration and the correction to Rovers image-incidence counting.
The earlier 25-waypoint tasks took 47–52 seconds and about 178 MiB. Those numbers
are historical context, not the fair before/after comparison above.

The [earlier 100-waypoint measurement](../experiments/problog/performance/rovers-100-cancelled.json)
was stopped at the user's request after 258.73 seconds without a completed task,
peaking at 256.2 MiB. That was a cancellation before its 300-second limit, not a
model-declared failure. The user subsequently chose continued optimization.
The [stage-one runtime matrix](../experiments/problog/performance/runtime-stage1.json)
already produced 100-waypoint tasks in about 26 seconds; its three-task optimized
cases hit their aggregate 75-second limit during the third task. The final matrix
completes all three and establishes the current operating range above.
