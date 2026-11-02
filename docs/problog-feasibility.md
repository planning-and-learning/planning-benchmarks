# ProbLog feasibility for declarative task generation

This is the historical stock-ProbLog assessment. The subsequent
[production pilot](problog-pilot.md) addresses its runtime blockers; see the
[performance report](problog-pilot-performance.md) for current measurements.

Assessed 2026-09-16 against ProbLog **2.3.0**, using isolated Python environments.
The question is whether it can replace per-domain Python generation while keeping
current probability laws and `make_problem` signatures, and reducing authoring
complexity. Production generators, distribution specs and project dependencies
were not changed. Runnable models and checks are in
[experiments/problog](../experiments/problog/README.md).

**Verdict:** ProbLog is a credible declarative authoring language and a useful
probability reference tool. Working models demonstrate the relevant semantics.
Stock ProbLog 2.3.0 is not yet suitable as our probability-preserving production
runtime: verified numerical cutoffs can remove possible outcomes, its RNG interface
does not match ours, and straightforward sampling is substantially slower. These
are concrete engineering obstacles, not evidence that the language cannot express
our distributions.

## What was actually built and verified

| Prototype | Result |
| --- | --- |
| [Ferry](../experiments/problog/ferry.pl) | A 25-line parameterized model defines objects, initial facts, goals and names. Three complete tiny distributions matched the existing sampler and independent support spec: 1, 8 and 32 tasks. |
| [Delivery](../experiments/problog/delivery.pl) | A 31-line parameterized model preserves local destination normalization. The 48-task one-package case and 240-task two-package case matched; the latter retains 48 tasks at `1/192` and 192 at `1/256`. |
| [Tiny Grid](../experiments/problog/grid_tiny.pl) | The `(2,2,1,1,2)` subfamily matched all 60 tasks: 48 at `1/72`, 12 at `1/36`. Reachability is ordinary recursive logic. This is not general Grid. |
| [Rovers graph component](../experiments/problog/conditioning.pl) | Local hierarchical sampling gives complete visibility probability `1/4`; global evidence gives `2/5`. All seven joint connected graph outcomes matched independent formulas. This is not complete Rovers. |
| Local finite retries | Explicit attempt-indexed choices preserve the failure event. Exact-mode checks passed for budgets 1, 2 and 3. Demand sampling also ran with budget 10,000 without grounding every possible attempt. |
| [Goal repair](../experiments/problog/repair.pl) | The singleton-repair distribution is `3/8, 3/8, 1/4`, as required, rather than uniform nonempty subsets. |
| [Semantics checks](../experiments/problog/verify_semantics.py) | Confirmed random-choice identity, duplicate list values, sampling of unbounded recursion, a per-world minimum, and the numerical counterexamples below. Passed on Python 3.10.21 and 3.13.2. |

The model line counts exclude shared adapters, parameter validation and public
metadata; they are not a like-for-like total-code reduction claim.

Ferry/Delivery compare every fully bound task, including absent atoms, against
exact rational weights obtained by enumerating the actual Python generator's
choices. Their support also equals complete enumeration of the current
`distribution.spec`. Another 100 sampled tasks were decoded with one generic
adapter, rendered by the existing renderer, and accepted by the independent
PDDL membership checker. Grid also compares against exhaustive legacy choice
histories and complete specification enumeration.

The largest absolute probability error in these six finite domain cases was
below `7e-17`. This is agreement within floating-point tolerance, not a claim of
rational arithmetic inside ProbLog. These are bounded feasibility checks, not
all-domain implementations or arbitrary-size equivalence proofs.

## Why the language fits

ProbLog already combines probabilistic facts and categorical alternatives with
logical derivation. Its Python API supports both probability queries and joint
sampled worlds. We do not need to write a parser or a new probabilistic logic
interpreter. [Language documentation](https://problog.readthedocs.io/en/latest/modeling_basic.html),
[Python API](https://problog.readthedocs.io/en/latest/python.html).

For example, the Ferry model uses:

```prolog
origin(C,L) :- car(C), locations(Ls), select_uniform(origin(C),Ls,L,_).
destination(C,L) :- car(C), locations(Ls), select_uniform(destination(C),Ls,L,_).
initial(at(C,L)) :- origin(C,L).
goal(at(C,L)) :- destination(C,L).
```

Each object supplies a random-choice identifier. The initial and goal atoms follow
from those choices. Ordinary derived predicates do not create extra random
outcomes merely because they have several proofs. The standard library provides
`select_uniform/4` and weighted selection.
[Official selection example](https://dtai.cs.kuleuven.be/problog/tutorial/sampling/02_arithmeticexpressions.html).

Delivery chooses its starts first and then samples from the corresponding legal
destination list. That expresses its intended conditional law directly. It does
not globally condition an independently proposed whole task.

For graphs, recursive reachability replaces rank-witness encodings. For finite
lists, deterministic operations can express ordered token grouping, projection,
repair and deduplication. Each independent draw still needs a distinct identity:
repeating the same probabilistic atom reuses its result. A variable appearing only
in a probabilistic rule's body can create additional independent choices; the
semantics checks demonstrate a resulting `3/4` probability where an incautious
translation might expect `1/2`.

There is also no fundamental sampling-language obstacle to Goldminer's unbounded
trace. ProbLog can sample recursive generative models without enumerating all
possible traces. Its documentation explicitly distinguishes this from standard
inference over infinite support.
[Official inference tutorial](https://dtai.cs.kuleuven.be/problog/tutorial/advanced/00_inference.html).

A generative ProbLog model still describes how random choices combine. It does not
automatically synthesize an efficient sampler from arbitrary initial/goal
constraints. Blocks' uniform tower distribution, for example, still needs a suitable
construction or a potentially expensive conditional model.

## Local conditioning is feasible, with execution tradeoffs

We tested two approaches:

1. **Explicit local retries:** index every proposal by stage and attempt; keep
   parent values fixed; produce `failure` when the budget reaches zero. This
   preserves the operational law without enumerating all possible graphs during
   ordinary sampling.
2. **Nested inference plus categorical selection:** `subquery/3` computes a locally
   conditioned distribution, and `select_weighted` samples from it. This worked for
   all seven three-node graph pairs, but computes candidate outcome weights and
   is expensive. Independently sampling the returned marginal probabilities would
   be wrong; the whole graph must be selected categorically.

For the explicit retry model, independent rational success probabilities are
`5/32`, `99/256`, and `1169/2048` at budgets 1, 2 and 3. Their complements are
failure mass. The visibility graph among successful tasks is consequently
budget-dependent, as in the current generator.

After simplifying reachability to recursive closure, the three-node retry model
sampled 50 graph pairs with budget 10,000 in about 2.2 seconds. This measures
only the graph component, not complete Rovers tasks.

The model also contains an analytic elimination of retries using `1-(1-c)^B`.
Although mathematically valid, ordinary floating-point evaluation can round this
to one and erase a small failure probability. It should not replace the explicit
process under a strict preservation contract.

The official `subquery` facility provides nested probability evaluation, not an
automatic locally conditioned sampler. The stock sampling API's evidence handling
uses rejection; indiscriminately making all validity conditions evidence would
reweight earlier choices.
[Nested-inference example](https://dtai-static.cs.kuleuven.be/problog/tutorial/various/05_numberguessing.html),
[sampling documentation](https://problog.readthedocs.io/en/latest/cli.html#sampling-sample).

## Confirmed runtime blockers

### Positive-probability outcomes can be lost

This model has exactly two possible outcomes:

```prolog
0.999999995::common; 0.000000005::rare.
query(common).
query(rare).
```

The stock sampler skips an annotated-disjunction alternative if its remaining
probability is below `1e-8`. Forcing the legal random draw `0.9999999999` produces
both `common=false` and `rare=false`: an impossible third outcome, instead of the
rare branch. This is a deterministic regression check, not a failure to observe a
rare outcome in random trials.

The installed source is `problog/tasks/sample.py`, `SampledFormula.add_atom`.
The reproduction is in [verify_semantics.py](../experiments/problog/verify_semantics.py).
Using the standard library's `select_weighted` avoids this particular annotated-
disjunction cutoff in the tested example, but does not fix all numerical issues.

Default log-space inference also maps a primitive probability of `1e-10` to zero.
Explicit `SemiringProbability` retains it in that example, but ordinary probability
space can underflow on long products. A computed zero must therefore not be used
as a proof that a task is outside the distribution without a suitable arithmetic
backend. The relevant implementation is `SemiringLogProbability` in
[the evaluator source](https://problog.readthedocs.io/en/latest/_modules/problog/evaluator.html).

### Default arithmetic changes boundary behavior

ProbLog's `Constant.FLOAT_PRECISION` defaults to 15 decimal places. Under that
setting, `truncate(1.9999999999999998)` gives `2`; Python's corresponding truncation
gives `1`. A literal probability of `1e-16` becomes zero even when the ordinary
probability semiring is selected.

Setting `Constant.FLOAT_PRECISION = None` fixes those two reproductions, but it is
a package-global setting and does not remove the other sampler/evaluator cutoffs.
The implementation is in [the Constant source](https://problog.readthedocs.io/en/latest/_modules/problog/logic.html).
Nomystery and Woodworking already have observable numeric boundary behavior, so a
migration needs an explicit arithmetic policy and compatibility tests.

### RNG isolation needs an adapter

The sampled-world implementation uses Python's process-global `random` module.
Its public sampling function does not expose the injected `RandomSource` interface
used by our generators. Preserving isolated seeded streams and concurrent calls
requires generic integration work or a library change. Saving/restoring global
state is insufficient for concurrent threads.

### Performance needs a representative acceptance gate

Local observations for the straightforward, unoptimized models:

| Case | Prepare + first sample | Subsequent sample | Current Python sample |
| --- | ---: | ---: | ---: |
| Ferry: 10 cars, 5 locations | 112 ms | 102 ms | 0.037 ms |
| Delivery: 5×5 grid, 5 packages | 482 ms | 355 ms | 0.100 ms |
| Tiny Grid subfamily | 45 ms | 27 ms | 0.055 ms |

Ferry/Delivery subsequent times include decoding into `Problem`; both sides omit
PDDL rendering. Each averages 10 ProbLog samples versus 1,000 Python samples.
Grid averages 100 samples and returns only a compact outcome term on the ProbLog
side, so its numbers are less directly comparable. These are small local runs,
not optimized backend limits. They nevertheless establish that interpreter
integration is not a performance-neutral substitution.

Exact inference and forward sampling must be assessed separately. Exact retry
inference already grew expensive at small budgets, whereas sampling with a
10,000-attempt cap completed quickly on ordinary paths. Exact enumeration should
remain a bounded reference tool, not the production generation strategy.

## Remaining all-domain questions

| Requirement | Assessment |
| --- | --- |
| Ordinary finite categorical/subset generators | Good language fit; Ferry and Delivery demonstrate the shared API. Uniform subset/permutation laws still need correct declarations. |
| Connected graph generators | Expressible without Python graph callbacks. The Rovers graph experiment demonstrates local retries and recursive closure. |
| General Grid | Tiny conditional-reachability case works. Multiple shapes, uniform onto maps and opening histories remain to be implemented and measured. |
| Goldminer | Recursive sampling is supported; the complete carving model and output law remain unverified. Exact general trace inference is a different problem. |
| Nomystery | A per-world minimum is expressible and was tested on a tiny model. Scalable shortest pickup/delivery cost, binary64 scaling and large emitted fuel tables remain unresolved. Decision-theoretic optimization is not automatically this per-instance computation. |
| Woodworking | Lists and latent choices fit the recipe, but the full model, retries, numeric boundaries and practical scale have not been verified. |
| Public checking API | ProbLog does not automatically reproduce current named-rule violations, initial/goal/joint group selection and typing diagnostics. These need deliberate adapters or retained support checking. |
| Development tooling | Pyright can still check Python adapters; it cannot check `.pl` files. Grounding errors, explicit schema validation and model tests would need to supply the relevant checks. |

The package installed without extra Python dependencies in the isolated environment;
small inference used its bundled DDNNF backend. The semantics checks passed on
our minimum Python 3.10 and on 3.13. Other platforms/backends were not assessed.
Package details are available from [the official PyPI release](https://pypi.org/project/problog/2.3.0/).
Some online docs still describe version 2.2; installed 2.3.0 behavior was checked
directly. For example, its `findall` preserves repeated values in our deterministic
and probabilistic tests, despite an older documentation statement about deduplication.

## Recommended decision

Continue evaluating ProbLog as a candidate language, rather than extending our
custom language with a complete probabilistic interpreter immediately. The working
models provide evidence that this could reduce domain authoring code.

Do not migrate all generators onto the stock runtime yet. The next acceptance gate
should be a generic integration that addresses numeric support preservation and
RNG isolation, followed by representative-size measurements and one complete hard
domain. Avoid solving the hard domains through domain-specific Python callbacks;
that would retain the original duplication behind a different file format.

A possible integration is one public `distribution.pl` per domain, generic parameter
fact binding, joint-world sampling, and one typed decoder into the existing
`Problem`/renderer. Existing `make_problem` signatures can remain adapters. The
current prototype decoder only covers Boolean atoms and object types; numeric
initializations, metrics, validation and error reporting remain work.

Retain independent support specifications during a pilot. A model cannot reveal
its own missing intended outcomes by generating and checking against itself.
Exhaustive legacy probability tables, boundary tests and independent logical
contracts remain the migration evidence. No adoption or distribution change was
made by this feasibility investigation.
