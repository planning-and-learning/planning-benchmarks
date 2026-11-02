# Declarative generation audit

Audit date: 2026-09-16. Scope: all 23 classical generators, their parameters,
`distribution.spec` files, shared samplers, language/compiler, and relevant tests.
This is an assessment, not a generator migration. Production code and distributions
were not changed.

All 23 have finite semantic task spaces for fixed supported parameters. We found
no concrete support mismatch, but this is not an arbitrary-size completeness proof.
The main missing capability is an executable probability measure. The current
language describes allowed tasks; its probability metadata is prose.

Eleven domains are uniform over permitted **labeled semantic initial/goal pairs**.
Six more have relatively direct finite conditional probability models. Driverlog
adds conditioned graph sampling. Grid, Goldminer, Nomystery, Rovers, and Woodworking
need more substantial treatment. None is mathematically impossible to describe
with finite weighted outcomes. Efficient generation and a compact, understandable
specification are separate requirements.

## All-domain findings

Links lead to the inspected samplers; each directory also contains the inspected
`distribution.spec` and `parameters.py`. “Uniform” refers to semantic tasks after
projecting out logical witnesses, not arbitrary solver models or construction traces.

| Domain | Existing law and migration obstacle | Useful simplification |
| --- | --- | --- |
| [blocks_3](../src/pypddl_datasets/generators/classical/blocks_3/generator.py) | Independent uniform initial/goal tower arrangements. Requires exact projected uniform sampling; full-model witness counting biases it. | Generic acyclicity and derived clear/top facts; omit self-edges with existing sparse declarations. |
| [blocks_4](../src/pypddl_datasets/generators/classical/blocks_4/generator.py) | Same uniform tower law, with fixed initial empty arm. | Same; keep each domain's constraints explicit. |
| [childsnack](../src/pypddl_datasets/generators/classical/childsnack/generator.py) | Uniform fixed-size allergy/resource subsets and independent table choices. | Fixed facts, subset cardinality and categorical fields. |
| [delivery](../src/pypddl_datasets/generators/classical/delivery/generator.py) | Uniform starts, then uniform eligible common destination. The number of eligible destinations depends on starts, so whole tasks are generally nonuniform. | One destination field; local conditional weight; fixed adjacency facts. |
| [ferry](../src/pypddl_datasets/generators/classical/ferry/generator.py) | Independent uniform positions and goals. | Total position functions and fixed type/inequality facts. |
| [floortile](../src/pypddl_datasets/generators/classical/floortile/generator.py) | Uniform robot-column injection, rows and fixed-count color assignments; uniform semantic tasks. | Functions, all-different columns, color cardinality, derived occupancy complement. |
| [gripper](../src/pypddl_datasets/generators/classical/gripper/generator.py) | Deterministic task. Only generic materialization is needed. | Fixed fact comprehensions. |
| [hiking](../src/pypddl_datasets/generators/classical/hiking/generator.py) | Independent fair tent states; everything else fixed. | Sparse fixed partner/route tuples already expressible today. |
| [hiking_binary](../src/pypddl_datasets/generators/classical/hiking_binary/generator.py) | Same fair tent law, with stronger car-count precondition. | Same sparse/fixed-fact improvements. |
| [miconic](../src/pypddl_datasets/generators/classical/miconic/generator.py) | Uniform endpoints with different destination, except the one-floor fallback. Eligible destination count is constant, so tasks are uniform. | Origin/destination functions, fixed ordering facts. |
| [spanner](../src/pypddl_datasets/generators/classical/spanner/generator.py) | Independent uniform spanner placements. | Separate random positions from fixed bob/nut positions and chain. |
| [tpp](../src/pypddl_datasets/generators/classical/tpp/generator.py) | Uniform truck placements and stock quantities. Insufficient stock remains permitted. | Integer/enum quantity fields; sparse level chain and fixed facts. |
| [barman](../src/pypddl_datasets/generators/classical/barman/generator.py) | Uniform distinct recipe pairs and goal-shot subset; ingredient/cocktail mixture gives category-dependent weights. | Functions, partial goal function, categorical mixture. |
| [logistics](../src/pypddl_datasets/generators/classical/logistics/generator.py) | Uniform truck-city permutation and dependent placements; Bernoulli goal selection with singleton repair. | Bijections/functions; explicit repaired-subset factor. |
| [satellite](../src/pypddl_datasets/generators/classical/satellite/generator.py) | Two replacement mode draws become a set; hidden instrument choice weights image modes. Duplicate histories must be summed. | Small set-valued fields and explicit output factors. |
| [schedule](../src/pypddl_datasets/generators/classical/schedule/generator.py) | Independent attribute choices and integer-percent inclusion. Empty/already-satisfied goals remain possible. | Optional functions and tuple-valued attributes. |
| [visitall](../src/pypddl_datasets/generators/classical/visitall/generator.py) | Uniform unavailable subset/start; quantized independent goal selection, with start forced into goal. | Selected object set and derived adjacency; remove redundant presence rules. |
| [driverlog](../src/pypddl_datasets/generators/classical/driverlog/generator.py) | Two independently conditioned Bernoulli connected graphs, each with 10,000-proposal failure; repaired goal subsets. | Generic connected/undirected graphs and partial position functions. |
| [grid](../src/pypddl_datasets/generators/classical/grid/generator.py) | Uniform onto shape maps, then sequential frontier-lock selection and reachable key placement. Opening histories contribute unequal task weights. | Functions, derived reachability, bounded state transitions; plain connectedness is insufficient. |
| [goldminer](../src/pypddl_datasets/generators/classical/goldminer/generator.py) | Fair initial rocks overwritten by a random carving walk. Many rock/walk histories yield each output; walk traces are unbounded. | Exact finite segment transition kernel can eliminate boundary loops; retain the two-column west-step restriction. |
| [nomystery](../src/pypddl_datasets/generators/classical/nomystery/generator.py) | Connected Bernoulli graph, uniform edge costs/endpoints, deterministic optimal fuel. Edge-count-dependent cost multiplicity prevents uniform tasks. | Declarative least-cost derivation, numeric fields, dependent object prefixes; current full grounding is expensive. |
| [rovers](../src/pypddl_datasets/generators/classical/rovers/generator.py) | Hierarchically conditioned graphs, equipment/camera repairs, replacement draws and deduplicated goals. Local retry exhaustion depends on prior choices. | Functions/sets and local probability scopes; soil/rock site selection simplifies to uniform without replacement, but image multiplicities do not. |
| [woodworking](../src/pypddl_datasets/generators/classical/woodworking/generator.py) | Hidden full goals, weighted projections, scoped preprocessing rejection, chunk-token shuffles, ordered grouping and capability unions. | Records, sequences/multisets, derived fields; remove four redundant palette rules. |

## Why support alone is insufficient

These examples distinguish the actual laws from plausible but incorrect replacements.

- **Delivery:** for grid size 2 and two packages, the 240 permitted tasks split into
  48 tasks of probability `1/192` and 192 of probability `1/256`. Colocated package
  starts have three eligible destinations; separated starts have four. Uniform
  sampling of permitted tasks changes the probability of colocated starts from
  `1/4` to `1/5`. A semantic weight proportional to `1 / eligible_destinations`
  suffices here; a general stochastic process is unnecessary.
- **Blocks:** with two blocks, the separate-block arrangement admits four height
  witnesses and either tower admits one. Uniform full-model sampling would give
  the separate-block arrangement probability `2/3`, instead of `1/3`.
- **Singleton repair:** Logistics, Driverlog and Grid select a Bernoulli subset,
  then replace an empty selection with a uniform singleton when the probability
  is positive. With two items and probability `1/2`, subset masses are
  `3/8, 3/8, 1/4`; conditioning on nonemptiness gives `1/3` each.
- **Satellite:** two independent draws from two modes give singleton support sets
  probability `1/4` each and the pair probability `1/2`. Given instrument mode
  sets `{A}` and `{A,B}`, selecting an instrument then one of its modes produces
  `A` with probability `3/4`, not `1/2`.
- **Grid:** parameters `(2,2,1,1,2)` with default goals have exactly 60 tasks:
  48 at probability `1/72`, 12 at `1/36`. The reachable placement region depends
  on the previously sampled lock layout. More generally, a shape's selection
  weight is its number of frontier locks, not one vote per shape.
- **Rovers:** ignoring retry-budget exhaustion, three waypoints and one rover at
  edge probability `1/2` give complete visibility probability `1/4` under the
  hierarchy, but `2/5` under globally conditioned raw graph draws. Traversal
  acceptance differs between visibility graphs, so exact finite-budget failure
  also matters, even when its probability is very small.
- **Goldminer:** with two rows, three columns and gold row fixed to zero, there are
  five rock patterns. Four have probability `1/6`; the all-soft pattern has
  probability `1/3`. Existence of a permitted carving path does not determine its
  probability.
- **Woodworking:** for an available part with two selected goal properties, an iid
  preprocessing proposal is accepted with probability `47/54`. After acceptance,
  each color-containing pair has probability `9/47`, wood+treatment and wood+surface
  each `6/47`, and treatment+surface `8/47`. The full hidden goal and selected
  property count stay fixed during retries.

## Missing semantics versus optional language conveniences

The essential additions for preserving probabilities are:

1. **An executable measure over labeled semantic tasks.** Explicit uniform
   semantics suffice for eleven domains. Other domains need normalized factors
   or a generative model. A solver's first model, randomized search order, or
   incomplete enumeration prefix does not provide this measure.
2. **Three distinct kinds of values:** random latent choices, deterministic
   derived values, and existential proof witnesses. Random histories leading to
   the same task have their masses added. Proof witnesses contribute no weight.
3. **Dependent distributions and local normalization.** A condition must say which
   choices it resamples and which earlier choices remain fixed. Replacing all
   constraints by one global observation is incorrect for several domains.
4. **Explicit failure semantics.** Existing graph/preprocessing budgets can raise
   failure. A local proposal with acceptance probability `c` and budget `B` has
   failure mass `(1-c)^B`. Dropping that event, retrying the whole task, and
   conditioning on eventual success are different contracts.
5. **Defined numeric semantics.** Schedule uses integer percentages; Visitall
   uses `ceil(binary64(goal_ratio * area))/area`; Nomystery and Woodworking use
   observable Python floating-point evaluation, truncation, ceiling and rounding.
   Ideal Bernoulli laws, finite random-number thresholds, and identical
   seed-to-task mappings must not be conflated.

Uniform subsets, permutations, functions, sets, multisets, records, graph
operators and optimal-value expressions improve readability and execution. They
are not all fundamental additions to expressive power: the current bounded
Boolean/integer language already encodes many of them, laboriously.

A finite weighted-output table could express every fixed parameter instance, but
is not a practical authoring format. Conversely, a universal probabilistic
programming language can encode the algorithms, but does not automatically make
them simpler or more declarative in the constraint-modeling sense.

Unrestricted stochastic loops are **not established as necessary** for these 23
domains. Grid's opening steps and Woodworking's chunking are parameter-bounded.
Goldminer's vertical motion is monotone until a west step; boundary self-loops can
be eliminated using an exact finite kernel. From row `r > 0`, an upward segment's
first movement reaches row zero with probability `2/(r+1)` and each intermediate
row with probability `1/(r+1)`, then either stops with probability `1/2` or
continues upward. At the boundary it eventually exits with probability one.
The downward case is symmetric. This yields a finite triangular recurrence,
though it still needs independent verification before replacing the sampler.

Nomystery's optimal fuel is a deterministic computation **within each sampled
instance**. Minimizing over possible tasks would change the distribution. A
generic least-cost operator could accept declarative transitions/costs; a hidden
`nomystery_optimum` callback would defeat the proposed architecture.

## Are the specifications as simple as possible?

No. Most are already fairly short (roughly 32–65 lines including metadata), but
Rovers has 160 lines and Woodworking 288. Several expose implementation details
of constraint encoding rather than just the domain's mathematical structure.

Improvements available without adding a language feature:

- Use existing sparse declarations for fixed tuples. Hiking currently declares
  `4*C^3` partner Boolean slots to represent only `C` fixed partner triples. Its
  fixed route can likewise use `P-1` tuples rather than a dense `P*P` family.
- Remove redundant constraints selectively. Four Woodworking palette rules and
  Visitall's start/goal availability rules repeat the compiler's automatic
  `atom -> present(optional argument)` declaration constraints. Rovers also has
  a literal `true` goal rule.
- Simplify equivalent probability descriptions where justified: Rovers' soil/rock
  site candidate multiplicities are constant within a generated world. This does
  not apply to image goals or Grid frontier shapes.

Small, generic authoring improvements worth evaluating:

- **Fixed/derived fact comprehensions:** combine a relation declaration and its
  defining equality. A ground `let` already exists; symbolic derived definitions
  do not have comparable shorthand.
- **Function and optional-function declarations:** replace a Boolean relation plus
  repeated “exactly one”/“at most one” constraints. Multiplicity sugar can compile
  to today's representation without immediately implementing first-class symbolic
  object values.
- **Set, sequence and multiset operations:** express cardinality, union, projection
  and ordering directly. Preserve their distinctions: deduplication and token
  permutation induce different weights.
- **Generic connectedness, acyclicity and least-fixed-point reachability:** hide
  rank witnesses. Grid unlocking needs dependent reachability, not just a connected
  static graph. Goldminer additionally constrains allowed segment shapes.

These do not require domain templates, imported domain constraints or Python
callbacks. Each domain can remain explicit in its own public file.

There is an API caveat: narrowing a declared vocabulary changes checking behavior
when a rule group is disabled, and may turn a named-rule violation into an
undeclared-atom error. Folding a rule into a declaration can also change diagnostic
names. Full-task support equivalence alone does not guarantee equivalence of the
public partial-group checker. Any cleanup should preserve or explicitly address
that distinction.

Compact source does not remove computational costs. Local measurements during
this audit, **before sampling**, found:

| Specification parameters | Compilation result |
| --- | --- |
| Nomystery: 3 locations, 2 packages, cost bound 2 | About 0.19 s; 114 semantic and 44 auxiliary variables. |
| Nomystery: defaults | Exceeded 1,000,000 grounding operations after about 10 s. |
| Rovers: `(2,3,2,1,2)` | About 0.11 s; 112 semantic and 17 auxiliary variables. |
| Woodworking: 6 parts, 2 machines, factor 2 | About 4.8 s; 1,167 semantic and 613 auxiliary variables. |

These are single local observations, not benchmarks. Nomystery's `N*3^P` Bellman
states, fuel universe and scaling lookup are clear reasons a solver wrapper alone
will not be an efficient production generator. A generic materializer also needs
PDDL domain identifiers, object types, numeric initializations and metrics. Existing
`make_problem` signatures can remain thin compatibility adapters.

## Existing languages worth comparing

The capability descriptions below come from primary project documentation; the
fit judgments are this audit's assessment. None was integrated or benchmarked here.

| Language/tool | Existing capabilities relevant here | Fit and remaining issue |
| --- | --- | --- |
| [Essence / Conjure](https://conjure.readthedocs.io/en/latest/essence.html) | High-level finite sets, multisets, functions, sequences, relations, records and cardinality/function attributes. | Strong candidate for simpler support specifications. Probability measures and faithful sampling remain a separate layer. |
| [MiniZinc](https://docs.minizinc.dev/en/latest/lib-globals-graph.html) | Established constraint modeling with connectedness, reachability, DAG and tree constraints. | Useful modeling/backend comparison. Finding a valid or optimal solution does not supply our required task probabilities. Its [random-number builtins](https://docs.minizinc.dev/en/latest/lib-stdlib-random.html) return samples of primitive distributions; they are not a declaration of uniform sampling over satisfying tasks. |
| [Alloy](https://alloy.readthedocs.io/en/latest/language/sets-and-relations.html) | Relational/set modeling with composition and transitive closure; concise graph invariants. | Useful support-language comparison. A probability-preserving generation layer would still be needed. |
| [ProbLog](https://problog.readthedocs.io/en/latest/modeling_basic.html) | Probabilistic facts, categorical annotated disjunctions, logical derivation and evidence. Also has [sampling](https://problog.readthedocs.io/en/latest/cli.html#sampling-sample). | Especially relevant to finite relational probabilities. Retry scopes, failures and deterministic numeric/optimization behavior still need explicit modeling; evidence is not automatically our local retry semantics. |
| [Dice](https://github.com/SHoltzen/dice) | Discrete probabilistic programming, observation and exact inference through weighted model counting. | Relevant to finite probability reference models. Current documented language lacks recursion; the author repository describes it as research code. Not an automatic solution for unbounded traces or large instances. |
| [Scenic](https://docs.scenic-lang.org/en/latest/tutorials/fundamentals.html) | Probabilistic scenario descriptions combining object properties, distributions and requirements. | Closest application concept, but focused on spatial scenarios. Static control flow cannot depend on random values; PDDL output and our stateful constructions need adaptation. Its [requirements](https://docs.scenic-lang.org/en/latest/reference/statements.html#require-boolean) are observations, so their scope must be checked carefully. |
| [WebPPL](https://docs.webppl.org/en/master/language.html) | Sampling, conditioning, recursive and higher-order functions; [inference](https://docs.webppl.org/en/master/inference/index.html) over stochastic return values. | General enough to express the constructions in principle. This moves us toward probabilistic programs, not automatically smaller logical specifications; inference may be approximate or intractable. |
| [PRISM](https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction) | State-based guarded probabilistic transitions. | Useful reference formalism for Goldminer and explicit retry/failure processes. Less direct as the main authoring language for relational PDDL task pairs. |

Conjure's [representation symmetry handling](https://conjure.readthedocs.io/en/latest/features.html)
also addresses a problem we must handle: one abstract set can have many low-level
representations. Regardless of backend, sampling must operate on the intended
labeled task projection. Logical equisatisfiability alone does not establish
probability preservation.

## Evidence and recommended next step

New exact discrete-choice exploration compared the current samplers with complete
projected specification enumeration for these twelve cases:

| Domain and parameters | Number of semantic tasks | Exact task masses |
| --- | ---: | --- |
| blocks_3 `(3,)` | 169 | All `1/169` |
| blocks_4 `(3,)` | 169 | All `1/169` |
| childsnack `(2,1,0.5)` | 72 | All `1/72` |
| delivery `(2,2)` | 240 | 48 at `1/192`; 192 at `1/256` |
| ferry `(1,2)` | 8 | All `1/8` |
| floortile `(1,2,2)` | 16 | All `1/16` |
| gripper `(2,)` | 1 | `1` |
| hiking `(2,1,2)` | 4 | All `1/4` |
| hiking_binary `(2,3,2)` | 4 | All `1/4` |
| miconic `(2,2)` | 4 | All `1/4` |
| spanner `(2,1,2)` | 4 | All `1/4` |
| tpp `(1,1,2,2,2)` | 8 | All `1/8` |

All compared supports matched. The additional Grid case above also matched all
60 outcomes with exact Fraction masses. Goldminer's five-pattern analytic check
matched projected enumeration. Rovers' singleton case with no requested cameras
has 31 tasks: three at `1/7` and 28 at `1/49`. Woodworking's four palette
redundancies were checked by asserting each negated rule against declaration
constraints; each was unsatisfiable in the one-part instance, and the compiler's
general presence implication explains the redundancy for every size.

The probability calculations treat primitive discrete choices by their intended
probabilities; they do not enumerate PRNG seeds. Sampling checks and tiny complete
cases do not prove arbitrary-size support equality. In particular, ordinary random
testing cannot rule out a rare missing output.

Recommended sequence:

1. Record these exact probability counterexamples as independent migration gates,
   alongside boundary/support tests. Retain an independent oracle after migration;
   checking a spec-generated task with the same spec cannot establish that the
   spec itself captures the intended distribution.
2. Compare small models in our DSL, Essence and a probabilistic language such as
   ProbLog before committing to a larger custom interpreter. Use Ferry for simple
   structure, Delivery for local normalization, and Grid for latent histories;
   then test feasibility against Rovers, Nomystery and Woodworking.
3. Evaluate source size, explanation clarity, installation/runtime cost, projection
   semantics and exact tiny probability tables. Assess constraint compactness and
   generative expressiveness separately.
4. If keeping the DSL, first exploit current sparse syntax and evaluate small
   fact/function conveniences. Introduce an explicit uniform/weighted measure
   before adding a broad stochastic-process language. Treat exact enumeration
   as a bounded reference backend, not a scalable general sampler.
5. Migrate only after each family preserves support, probabilities, failure policy,
   numeric boundaries and practical runtime. Preserve existing public signatures.

The earlier [generic generator design](generic-generator-design.md) describes one
possible generative-programming architecture. This audit narrows its minimality
claims: most domains do not need a process language, and even Goldminer's unbounded
walk has a possible finite reduction. The decision should follow a representative
prototype rather than an assumption that another custom language will reduce code.

Follow-up: [ProbLog feasibility experiments](problog-feasibility.md) test executable
models, local conditioning, performance and numeric compatibility.
