# ProbLog feasibility experiments

These models assess ProbLog 2.3.0 as a possible declarative generator language.
The original `.pl` prototypes remain isolated experiments. Production Ferry,
Delivery and Rovers now use packaged `distribution.pl` models through the shared
backend; the original experiments continue to test stock ProbLog behavior.
See [the feasibility report](../../docs/problog-feasibility.md) for the decision,
limitations and measurements.

From the repository root, with `uv` available:

```bash
uv venv --python 3.13 /tmp/planning-problog-feasibility
uv pip install --python /tmp/planning-problog-feasibility/bin/python 'problog==2.3.0' -e '.[specs]'
/tmp/planning-problog-feasibility/bin/python experiments/problog/verify_simple.py
/tmp/planning-problog-feasibility/bin/python experiments/problog/verify_grid.py
/tmp/planning-problog-feasibility/bin/python experiments/problog/verify_conditioning.py
/tmp/planning-problog-feasibility/bin/python experiments/problog/verify_semantics.py
```

`verify_simple.py` checks complete tiny Ferry/Delivery distributions against exact
rational choice histories from the existing Python samplers and independently
checks support against `distribution.spec`. It also demonstrates one shared
ProbLog-output-to-`Problem` decoder and reports unoptimized sampling timings.
The same `.pl` domain models support generation and probability queries.

`verify_grid.py` checks the 60 outcomes of Grid(2,2,1,1,2), including their unequal
weights. `grid_tiny.pl` only models this subfamily; it is not general Grid.

`verify_conditioning.py` checks the three-node graph component of Rovers, local
versus global conditioning, finite retry failures and singleton goal repair.
It does not implement complete Rovers tasks.

`verify_semantics.py` reproduces version-specific choice identity, recursion,
aggregation and numerical behavior. Several assertions deliberately document
upstream behavior incompatible with strict probability/support preservation:
passing the script means those limitations were reproduced, not fixed. This
script was also run successfully on Python 3.10.21.

ProbLog's inference backend uses floating-point arithmetic. Probability-table
comparisons use explicit tolerances against exact `Fraction` reference weights;
“exact inference” does not mean exact rational numeric results. Timing observations
are local measurements, not optimized performance guarantees. ProbLog uses the
process-global Python RNG; the experiment scripts run as separate processes.

## Production pilot performance

Run the bounded measurement harness against the installed current generators:

```bash
python experiments/problog/benchmark.py --list
python experiments/problog/benchmark.py --samples 3 --timeout 60 \
  --memory-mib 2048 --output /tmp/problog-benchmark.json
```

Use repeatable `--case NAME` arguments to select configurations. Each case runs in
a fresh child process. The report includes cold import/setup time, individual
`sample` plus PDDL-rendering times, successes and failures, subprocess timeouts,
peak resident memory, Python/ProbLog versions, model/backend source hashes and the
repository source for every parameter selection. Output is checkpointed after
each case. The default 60-second/2-GiB bounds are exploratory safety limits, not
claims about what every user should consider practical.

Ferry and Delivery cases cover the largest configuration in each committed
train/validation/test recipe. Rovers has no generated split recipe: its cases use
object counts and goal counts extracted from named checked-in PDDL tasks, with the
current default edge probability. The old tasks do not record their exact original
generator parameters or sampling law. HTG cases deliberately test the large end
of the repository; timeout or memory failure is an operating-range finding.

## Declarative Rovers graph comparison

`compare_graph_models.py` compares the current graph law, a sparse shared-tree
structural proxy, and the IPC 2023 graph construction. The new sampling rules live
in `graph_samplers.pl` and `rovers_graphs.pl`; production models remain unchanged.
See [the graph-scaling report](../../docs/problog-graph-scaling.md) for the exact
scope, reproducible commands, distribution checks, timeouts, and measurements.
