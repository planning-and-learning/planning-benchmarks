# ProbLog generator pilot

The pilot moves Ferry, Delivery and full Rovers generation into public per-domain
[`distribution.pl` files](../src/pypddl_datasets/generators/classical). Existing
`make_problem` signatures, names and parameter conventions remain compatibility
wrappers. The intended probability laws remain revision 2; identical old
seed-to-task mappings and PDDL ordering are not promised.

This follows the [feasibility investigation](problog-feasibility.md) and
[all-domain audit](declarative-generation-audit.md). Absolute generation time,
memory, workload provenance and practical limits are reported separately in
[the performance report](problog-pilot-performance.md).

## Architecture and API

Each domain model declares random choices, deterministic relations and the common
output vocabulary: `object(Name,Type)`, `initial(Atom)`, `goal(Atom)`, `domain(Name)`,
`problem_name(Name)` and optional `failure(Reason)`. Objects and PDDL atoms are
materialized by one shared adapter. `failure` raises `GenerationExhausted`.
There are no domain-specific Python generation callbacks.

The public module is `pypddl_datasets.generators.probabilistic`:

```python
from random import Random
from pypddl_datasets.generators.classical.ferry.parameters import Parameters
from pypddl_datasets.generators.probabilistic import (
    evaluate_model, model_source, sample_model,
)

parameters = Parameters(num_cars=1, num_locations=2)
problem = sample_model("ferry", parameters, Random(7))
source = model_source("ferry", parameters)
probabilities = evaluate_model("ferry", parameters, "query(origin(c0,l0)).")
# probabilities["origin(c0,l0)"] == Fraction(1, 2)
```

The API accepts domain parameter dataclasses or mappings and validates them using
the existing domain parameter contract. `model_source` returns the complete model,
shared choice definitions and concrete parameters. `evaluate_model` returns exact
`Fraction` weights for finite queries. It is a reference tool: large exact
inference can be much more expensive than drawing a task. Rovers additionally
accepts a nonnegative integer `graph_budget` diagnostic override through a mapping;
normal wrappers retain the original 10,000 attempts.

The independent `distribution.spec` files and their public checking API remain.
They describe allowed tasks independently of the executable sampling model. This
separation lets tests detect a model that omits intended outcomes; a model checking
its own samples cannot establish that property.

## Runtime acceleration

Sampling recognizes the exact bundled shared library and executes its finite
choices, Bernoulli subsets, ground-list traversal, connectivity and incidence
counting as generic native primitives. The per-domain model still determines random identities, retry scope,
repairs, initial facts and goals. `model_source` includes complete Prolog
implementations, and exact inference continues to use those definitions.

Optimization preserves primitive identities, including correlations between
choices over overlapping list suffixes. Extending a primitive with user clauses
disables replacement rather than discarding those clauses. The internal
`sample_source(..., accelerated=False)` path supports independent comparisons.

A bounded thread-local cache reuses prepared clauses and query declarations.
Each draw gets fresh stochastic caches and formula tables. Within that draw, finite
selectors reuse their completed value/rest pair before checking each caller's output
constraints; overlapping calls still share the original primitive decisions. An executing engine is
never shared by concurrent or reentrant calls, and an exception evicts it. Program
preparation still uses the registration lock described below.

The optimization checks compare complete sampled task laws with the frozen
imperative samplers, in addition to inference and support checks. This distinction
caught an image-weight error: sampled `findall` collapsed two true disjunction
branches. Incidence now explicitly counts both endpoints, and full-world tests
reconstruct the expected weights from independently read initial facts.

## Complexity tradeoff

The models are compact: Ferry has 25 lines, Delivery 32 and Rovers 159, including
comments and blank lines. Those counts do not include the shared runtime, public
API, validation, type stubs or independent tests. The backend is substantially more
complex than calling the imperative samplers: it owns numeric compatibility,
world-local choice identities, canonical primitive specialization and safe program
reuse. This pilot simplifies authoring additional domains; it is not evidence of
less total code or a simpler system overall.

Keep domain construction in the models and native operations generic. Further
runtime changes should earn their maintenance cost through measured improvements
and independent probability checks. Broader grounding-table reuse was rejected after counterexamples changed answers
for predicates that inspect variable bindings; those experiments remain separate.

## Probability and numeric semantics

The small shared ProbLog library provides exact finite uniform and integer-weighted
choices. Keep ratios such as `1/N` in probability annotations, rather than first
computing a floating-point approximation with `is`. Repeated draws need distinct
identities; repeated references to the same draw and choice context share its
outcome. Duplicate values in a choice list are distinct tickets. Ordinary logical
proof witnesses carry no additional sampling weight.

The runtime integration is pinned to ProbLog 2.3.0 and addresses four observed
issues without changing installed library files or process-global configuration:

- Exact rational reference evaluation avoids epsilon cutoffs and floating-point
  underflow in probability products.
- Categorical sampling retains small positive remaining masses; rational choices
  use the supplied RNG's integer operations.
- Model-local numeric constants and arithmetic retain Python binary64 values.
  Direct float Bernoulli choices use the legacy strict `rng.random() < p`
  comparison. Float annotations in reference inference denote their decimal
  representation after parsing to a Python float; this is an ideal probability
  law, not an enumeration of Python's finite random-number grid or arbitrary
  precision preservation of the original decimal literal.
- Nested `findall` targets share one sampled-world choice cache. A context-local
  RNG and cache isolate calls and threads, including nested aggregation. Model
  preparation is serialized because ProbLog uses global external-predicate
  registration; independent world sampling can then proceed concurrently.

Use the public API to execute these models. Stock ProbLog sampling alone does not
include these compatibility corrections. The low-level sampler rejects global
`evidence`: the pilot's locally scoped retries are explicit model relations.
Exact inference may use evidence, but it must not silently replace a generator's
local normalization or failure policy.

## What the three models exercise

| Domain | Preserved construction |
| --- | --- |
| Ferry | Independent uniform car starts, destinations and ferry position. |
| Delivery | Uniform starts, then a destination chosen from the eligible set determined by those starts. Two-package tasks are generally nonuniform. |
| Rovers | Bernoulli visibility followed by each movement graph conditional on that visibility; finite failure; nonempty equipment subsets; requested camera ownership and ordered repairs; replacement objective visibility draws; parity-based sample flags; bounded sample goals and weighted image requests with final deduplication. |

Rovers keeps prior graph choices fixed while retrying a movement graph. It does not
condition an independently proposed whole task on every graph being connected.
Its image-pair list is aggregated into integer incidence weights; camera and mode
selection remain subsequent conditional draws. Soil and rock site multiplicities
cancel because every eligible rover has a connected movement graph. Probability
zero and one edges are deterministic, so exact grounding can discard impossible
retry branches.

## Verification and its limits

[`tests/test_problog_distributions.py`](../tests/test_problog_distributions.py)
compares full tiny task distributions against frozen revision-2 Python samplers
under [`tests/reference_generators`](../tests/reference_generators). The oracle
traces every finite choice with rational weights. Task queries bind absent atoms
and optional objects as well as present facts. Independent support enumeration
checks the same tiny task sets. These checks go beyond observing generated seeds.

The regular cases include five Ferry parameterizations, both 2x2 Delivery cases,
and two one-waypoint Rovers cases. Focused Rovers checks cover all seven three-node
graph pairs and failure for retry budgets 1, 2 and 3; ordered multi-rover camera
repair; and the joint image visibility/mode/goal law. Rare-edge tests force both a
legal tiny-probability outcome and its strict threshold boundary.

[`experiments/problog/verify_pilot.py`](../experiments/problog/verify_pilot.py)
provides the separate complete two-waypoint Rovers check over 12,444 labeled tasks.
Its JSON report records checked probability mass, source hash and a `complete`
flag. A partially written report is not evidence of completion. Run the ordinary
suite and this extended verifier when changing model or backend probability
semantics; use the final checkpointed report as the authoritative extended result.

The [completed two-waypoint report](../experiments/problog/verification/rovers-two-waypoints.json)
verified all **12,444 tasks**, all 31 disjoint partitions and total probability mass
one. It took 20.13 minutes and peaked at 624 MiB. The subsequent finite-choice
memoization changes sampling only; the [dependency validation](../experiments/problog/verification/rovers-two-waypoints-inference-validation.json)
confirms that the model and exact-inference execution path are unchanged. Native
sampling has separate exhaustive tiny-table and cache regressions.

These are bounded distribution equalities and targeted semantic checks, not an
arbitrary-size equivalence proof. Large-instance sampling performance and bounded
exact-inference performance are separate acceptance criteria.

## Expansion beyond the pilot

ProbLog supplies the needed language mechanisms for many remaining generators,
but new models still need independent laws and realistic workload measurements.
The all-domain audit remains the detailed reference. The remaining twenty domains
fall into these groups:

| Domains | Remaining work before migration |
| --- | --- |
| Gripper, Hiking, Hiking Binary, Spanner, Childsnack, Miconic, Floortile, TPP | Fixed facts and finite choices; exact subset/injection laws where needed. Confirm output size and runtime at repository sizes. |
| Blocks 3, Blocks 4 | Preserve uniform labeled tower arrangements through an exact construction or correct counting. Uniform choices among solver witnesses or naive partitions are biased. |
| Barman, Logistics, Satellite, Schedule, Visitall | Explicit mixture weights, repaired subsets, hidden replacement histories and integer/float probability thresholds. The pilot mechanisms appear sufficient, but no full migration is verified. |
| Driverlog | Reuse the established graph/retry semantics in an explicit domain model; verify repaired goal selection and practical graph scale. |
| Grid | Declarative sequential unlocking and reachable key placement. Frontier multiplicities and construction-history weights matter; the earlier tiny Grid prototype does not establish the general model. |
| Goldminer | Preserve the carving-walk distribution and overwritten initial rocks. Recursive sampling or a verified finite transition reduction is needed; exact inference over unbounded traces is a separate issue. |
| Nomystery | Derive an optimum within each already sampled task, preserve fuel rounding, and avoid exhaustive exponential grounding. Also extend generic output to numeric assignments and metrics. A domain-specific optimum callback would defeat the architecture. |
| Woodworking | Hidden full goals, fixed-parent retry scopes, weighted projections, chunk-token permutations, grouping and numeric boundaries. Add generic numeric assignment/metric output and measure list-heavy construction costs. |

Current output materialization covers the positive propositional pilot. Numeric
initializations and metrics are not implemented there. Nor does the pilot establish
a universal efficient constraint-to-sampler compiler: authors still declare how
random choices combine, and carefully distinguish lists, sets and proof results.

Hold a broad migration until the runtime is adequate for the intended workloads.
The pilot establishes compatible distributions and a measured operating range,
while generation remains substantially slower than the imperative samplers. Any
next authoring pilot should start with simple finite models and retain independent
specs and exact tiny laws. Driverlog would test reuse of the graph machinery;
Satellite would test further hidden choices. General Grid and numeric/resource
domains need separate bounded pilots. Large Rovers configurations remain an
execution limit; the performance report identifies which requests finished within
the measured bounds.
