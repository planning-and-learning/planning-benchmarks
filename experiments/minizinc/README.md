# MiniZinc Rovers scaling pilot

This experiment compares graph construction in the current ProbLog model with
constraint solving in MiniZinc. It does not migrate production generators.

`rovers.mzn` describes symmetric, loop-free visibility and per-rover movement
graphs over all waypoints. Every graph is connected; movement is a subset of
visibility. Its optional soil fragment adds locations, soil samples, capabilities,
and a fixed number of eligible soil goals. It is not a complete Rovers model:
cameras, image goals, rock goals and PDDL emission are outside this pilot.

MiniZinc uses randomized Boolean polarities and solver search. This preserves the
set of feasible graph assignments, but **does not preserve the ProbLog probability
law**. Locations are deterministic. Matching edge densities is only a diagnostic,
not a distribution proof. ProbLog retains its current Bernoulli probabilities,
local retry scopes, and explicit failure outcome.

## Run

Use the official MiniZinc command-line bundle with Chuffed; no Python MiniZinc
package is required. The recorded experiment uses MiniZinc 2.10.1, Chuffed 0.14.0,
and Gecode 6.4.0, installed only under `/tmp/minizinc-scaling-2.10.1`.

Official Linux bundle:
https://github.com/MiniZinc/libminizinc/releases/download/2.10.1/MiniZinc-2.10.1-x86_64-linux-gnu.tar.gz

Downloaded archive SHA256:
`ef7b97d7ce9bf848d2f7b5e412d4affb8f52167cb6fd0540c7c0a81a02940d1b`

```sh
.venv/bin/python experiments/minizinc/benchmark.py \
  --minizinc /path/to/minizinc \
  --case 10,4 --case 25,10 --case 50,10 --case 100,14 \
  --backend chuffed --backend problog \
  --samples 3 --timeout 45 \
  --output /tmp/minizinc-scaling.json
```

For the additional soil fragment, use `--soil --backend chuffed`. The harness
chooses `max(1, floor(n/4))` soil goals. For the larger graph probes, use
`--case 197,30 --case 500,1 --case 1000,1 --samples 1`.

Direct model invocation:

```sh
minizinc --solver chuffed --statistics --random-seed 1 \
  -D 'n=25; nr=10; num_goals=6; graph_only=false; search_mode=1;' \
  experiments/minizinc/rovers.mzn
```

## Measurement scope

Each MiniZinc sample uses a fresh process. Its wall time includes startup,
flattening, solver initialization/search and JSON output. `flatTime` and
`solveTime` are the compiler/solver's own statistics. The randomness in this
pilot is selected during flattening, so these timings deliberately include
flattening on every draw.

ProbLog runs each configuration in a fresh process and requests all its samples
there: the first sampler call is cold and later calls can reuse preparation.
Per-sample times include model assembly, sampling and full graph decoding, while
imports, output validation, hashing and JSON serialization are outside that
internal timer. Whole-process wall time is also recorded. The query materializes
`graphs/2` directly; it does not compute the older graph-count query with its
nested `findall`, or generate a complete PDDL task.

MiniZinc receives a timeout per sample. The ProbLog batch receives that budget
multiplied by the sample count. Every process has a 2 GiB address-space limit;
it is not a combined process-tree RSS limit. The harness samples summed process
and descendant RSS every 50 ms, which can miss brief peaks and double-count
shared pages. ProbLog additionally records its own resident high-water mark.
Timeouts kill tracked descendants as well as the process group and retain
completed results. PID start times guard against killing a reused PID.

Every emitted graph is checked for endpoint bounds, duplicates, connectivity and
movement containment. MiniZinc output additionally passes exact array-shape,
Boolean-type, placement and soil-goal checks. Results retain seeds, density,
output hashes, source hashes, versions and host-load observations. Repeated
seeds establish reproducibility, not distribution correctness.

## Results (2026-09-17)

**This MiniZinc/Chuffed formulation scales worse than the current ProbLog graph sampler.**

The small matrix uses three seeds (1, 2, 3); the large probes use seed 1.
Both backends materialize visibility and every movement graph. These are graph
fragments, not full Rovers tasks, and the two backends have different sampling laws.
All reported cases use every undirected waypoint pair as a candidate edge.

| Waypoints | Rovers | MiniZinc wall / sample | ProbLog wall / sample | MiniZinc peak tree RSS | ProbLog peak tree RSS |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 4 | 0.133 s | 0.152 s | 16.9 MiB | 37.2 MiB |
| 25 | 10 | 0.313 s | 0.244 s | 36.1 MiB | 38.9 MiB |
| 50 | 10 | 1.209 s | 0.597 s | 77.5 MiB | 42.9 MiB |
| 100 | 14 | 23.859 s | 2.568 s | 336.3 MiB | 56.9 MiB |
| 197 | 30 | No result in 45 s | 18.234 s | 2519.1 MiB | 135.7 MiB |
| 500 | 1 | No result in 45 s | 28.845 s | 959.2 MiB | 202.3 MiB |
| 1000 | 1 | Allocation failure at 19.6 s | No result in 45 s | 1855.9 MiB | 477.6 MiB |

MiniZinc values are means of fresh process wall times. ProbLog values divide
the batch process wall time by its completed samples, amortizing imports and
preparation across three draws in the small matrix. MiniZinc validation in the
parent process is outside its timer; ProbLog validation and summary serialization
are inside its batch timer. These are the measured operating modes, not identical
startup policies or estimates of tail latency.

Measurements ran sequentially on a shared Linux host with an AMD Ryzen 7 PRO
4750U and approximately 31 GiB physical RAM. An initial timeout-cleanup defect
left detached solver processes running during earlier measurements. Those
processes were stopped, the harness was fixed and regression-tested, and **all
reported measurements were rerun**. No solver descendants remained after the
clean queue. Source hashes match the current model, harness and ProbLog files.
Earlier measurements are archived separately and excluded from this table.

At 100 waypoints, MiniZinc averages 2.13 s flattening and **20.10 s solver
search**, with approximately 39,000 nodes and zero reported failures per draw.
ProbLog averages 2.47 s inside its graph sampler. Removing MiniZinc compilation
cost would therefore leave a substantial gap. Zero failures argues against
backtracking explosion in these completed cases; more detailed solver profiling
would be needed to attribute search time among graph propagation and branching.

The 100-waypoint visibility graphs have 2,447–2,474 edges for MiniZinc and
2,464–2,523 for ProbLog, out of 4,950 candidates. Comparable density rules out
a trivial sparse-versus-dense explanation, but it does not prove equal laws.
Each backend produced three distinct graph hashes at every small configuration.

At 197 waypoints, the approximately 2.5 GiB MiniZinc figure sums compiler and
solver RSS. The 2 GiB address-space limit applies to each process, not the sum.
At 1,000 waypoints MiniZinc reports `std::bad_alloc` under that cap; ProbLog
instead hits the time limit. Neither has demonstrated useful performance there
under this measurement budget. The 500- and 1,000-waypoint probes use only one
rover and should not be read as a continuation at a fixed rover count.

## Solver and search checks

- Gecode failed to produce the 8-waypoint, 2-rover graph within 10 seconds;
  Chuffed completed it in 0.117 seconds. This smoke comparison uses deterministic
  search (`--search-mode 0`). In the installed bundle, Gecode uses a reachability
  decomposition of connectivity; Chuffed supplies a native connectivity
  constraint. This result should not be generalized to every Gecode encoding.
- Chuffed does not support `indomain_random`. The pilot instead randomizes
  Boolean polarities at compile time, then searches with `indomain_min`.
- The reported model uses `input_order`; an exploratory `first_fail` version
  was also tried. Its pre-cleanup timings are not used for performance claims.
- The initial diagnostic sweep used seeds 0, 1, 2; seeds 0 and 1 produced
  duplicate MiniZinc graphs. The reported final sweep uses 1, 2, 3 and verified
  distinct outputs. This is a smoke check of diversity, not a statistical claim.

## Additional soil fragment

The same model with soil samples, capable rovers, and exact eligible goal counts
also executed successfully. These are one-seed measurements of the reduced
example, not a comparison against full Rovers task generation.

| Waypoints / rovers | Soil goals | MiniZinc wall |
| --- | ---: | ---: |
| 25 / 10 | 6 | 0.305 s |
| 100 / 14 | 25 | 25.920 s |

## Artifacts and checks

- [Final small matrix](results/scaling-input-order.json)
- [Large probes](results/scaling-large.json)
- [Additional soil fragment](results/soil-fragment.json)
- [Solver smoke comparison](results/solver-smoke.json)
- [Discarded pre-cleanup measurements](results/pre-cleanup/)

All 31 targeted tests passed, including invalid-graph/schema rejection, tiny
ProbLog deterministic/failure/isolation cases and detached-child timeout cleanup.
The test module passes Pyright and Pylint. Production generator/model files are
unchanged. Source-distribution packaging includes this experiment so the new
tests can import its validator.

This pilot provides no reason to replace the current probabilistic generator
with this MiniZinc formulation for speed. Other encodings, solvers, sparse
candidate topologies or specialized samplers would require separate measurements.
