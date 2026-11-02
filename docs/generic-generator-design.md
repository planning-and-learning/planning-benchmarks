# Generic generation with preserved probabilities

Status: proposed extension, not implemented. The current declarative support
language and its generic checker remain unchanged.

The [all-domain audit](declarative-generation-audit.md) compares this approach
with smaller measure-based models and existing languages. This document describes
one generative-programming option; its full feature set is not necessary for
every domain, and unrestricted stochastic loops are not established as necessary.

The objective is one generic generation engine reading each domain's
`distribution.spec`, with no domain-specific Python sampling algorithms or
callbacks. The user selected preservation of the existing probability laws.
The contract must therefore describe both permitted semantic tasks and the
probability measure over them. Logical support alone does not determine weights.

## One domain file, two independent descriptions

Keep the existing declarations and `initial`, `goal`, and `joint` constraints.
Add an executable `sampling` section, with a new language version. Probability
metadata remains readable documentation of that section.

The support constraints characterize admissibility independently of construction.
The sampling section declares random choices and how they determine a task. Both
are interpreted by shared infrastructure; neither imports domain helpers. Keeping
both descriptions makes it possible to test that generation realizes the intended
support, including missing outcomes in tiny exhaustive cases.

Illustrative syntax for the random part of Ferry, not currently accepted syntax:

```text
sampling {
    draw ferry_origin from uniform(Locations);
    draw car_origin[c in Cars] from uniform(Locations);
    draw car_destination[c in Cars] from uniform(Locations);

    bind initial.at_ferry(l) for l in Locations = ferry_origin == l;
    bind initial.at(c,l) for c in Cars, l in Locations = car_origin[c] == l;
    bind goal.at(c,l) for c in Cars, l in Locations = car_destination[c] == l;

    complete uniquely;
}
```

The final statement derives the remaining fixed semantic facts from the logical
constraints. It must prove that the remaining semantic projection is unique;
proof witnesses may still differ. Zero or multiple completions are specification
errors, never permission to select an arbitrary solver model or retry earlier
random choices. Explicit deterministic bindings can avoid solver completion when
all outputs are already defined.

## Minimal shared probability machinery

The required constructs are:

- Finite uniform choices and categorical choices with explicit weights.
- Bernoulli draws, finite indexed draws, permutations, and subsets, with explicit
  ordered/unordered and with/without-replacement semantics.
- Ground and dependent deterministic expressions, including the existing Python
  binary64 evaluation order and integer conversions.
- Scoped conditioning/retry blocks. Each names what is redrawn, what remains fixed,
  its acceptance condition, its attempt limit, and the failure outcome. Conditions
  may use local logical constraints with existential proof witnesses.
- Declarative stochastic transition processes: finite state for fixed parameters,
  explicit transition probabilities, initial state, stopping predicate, and any
  existing step budget. Traces may be unbounded. Finite state alone does not
  guarantee termination: establish absorption for a terminating process, or
  explicitly account for nontermination mass separately from budget exhaustion.

These are language constructs shared by all domains. Do not add operations named
for particular benchmark families, embed Python, or introduce imported domain
constraint libraries. If a domain cannot be expressed with these constructs,
review the missing general operation before extending the language.

Random latent values and logical `aux` witnesses must remain distinct. Several
random histories can lead to the same task; their probability masses add.
Existential proof witnesses establish admissibility and contribute no multiplicity
to task probability. For each fixed parameter setting, the engine must retain
explicit generation failure outcomes as well as successful outputs.

## Cases the design must preserve

| Case | Consequence for the engine |
| --- | --- |
| Blocks | Two blocks have three initial arrangements. The all-table arrangement has four height witnesses and each tower has one. Weighting full solver models would change the uniform arrangement law. |
| Grid goal repair | With two eligible keys and inclusion probability 1/2, the repaired goal subsets have probabilities 3/8, 3/8, and 1/4. Conditioning on nonemptiness or choosing a uniform subset gives different weights. |
| Rovers graph hierarchy | Sample visibility first. Condition each traversal graph locally on connectivity within that fixed visibility graph. One globally conditioned product distribution changes the parent weights. Retain existing retry exhaustion and propagation. |
| Woodworking | Preserve weighted goal sizes, hidden full goal properties, the exact preprocessing retry scope and 10,000-attempt limit, indexed chunk tokens including a final zero remainder, shuffle multiplicity, groups of four, and first-seen wood ordering. |
| Goldminer | The carving walk has an unbounded trace. A fixed-length draw array or new step cutoff changes its law. Use a stochastic transition process or an independently verified elimination of repeated transitions. |
| Nomystery | The Bellman constraints can determine the optimal resource value without choosing among task outputs. Preserve multiplication and truncation order when deriving fuel from that optimum. |
| Visitall and Schedule | Preserve the existing discrete threshold probabilities; a literal continuous Bernoulli parameter can differ from the current quantized law. |

Local conditioning is essential. Redrawing an entire task when a later stage fails
can reweight earlier choices. A repair explicitly transforms the proposal and may make additional random
draws, such as choosing a uniform singleton. Preserve those draws instead of
implicitly replacing the repair with conditional sampling.

## Execution and reference checking

Use a forward interpreter for generation. It executes the declared choices,
local retries, processes, and bindings with an injected random source and returns
the existing semantic `Problem` representation. Read the PDDL domain identifier
from `domain.pddl`: for example, the `blocks_4` family uses `blocksworld`. The shared
renderer and split runner consume the resulting problem.

Retain the existing generic support compiler and PDDL checker. Solver-dependent
conditioning and unique completion initially require the optional solver extra;
parsing and source inspection remain available in the base install. The prototype
must measure this cost before replacing production generators.

Provide a separate bounded probability interpreter for testing. For finite choice
trees it enumerates outcomes and sums exact masses over equal semantic tasks.
Rational arithmetic can represent finite primitive probabilities, with deliberate
conversion of evaluated floating-point thresholds. Retry limits must include the
exhaustion mass. Unbounded finite-state processes require absorption calculations
or a proved reduction, not truncated traces presented as exact results.

Every reference calculation reports completion or an explicit resource-limit
status. Large state spaces can make exact probability calculations impractical.
A generic execution interface does not imply efficient sampling or exact weight
calculation for every parameter size.

## Migration sequence and acceptance gates

1. Specify primitive probability, scoping, failure, and latent-variable semantics.
   Test them independently of benchmark domains, including unequal witness counts,
   duplicate histories, local normalization, and exhausted retries.
2. Add a generic API `sample(domain, parameters, rng)`, semantic rendering, and
   minimal unique semantic completion. Prototype Ferry/Gripper and Hiking using
   declarative random choices. Compare
   full tiny output probability tables against independently enumerated existing
   samplers. Measure source size and runtime before extending the kernel.
3. Migrate categorical/subset families, followed by repaired goal selection.
   Preserve exact singleton-repair, replacement, and quantization behavior.
4. Add scoped graph conditioning and exercise completion on dependent quantities,
   then migrate Driverlog,
   Rovers, and Nomystery. Test hierarchy probabilities and explicit failure mass,
   rather than only successful-task membership.
5. Add and validate stochastic processes, then migrate Goldminer, Woodworking,
   and any remaining stateful constructions. This step is a prerequisite for
   claiming all-domain probability preservation.
6. Remove per-domain Python samplers only after each domain passes support,
   probability, boundary, and practical runtime checks. Keep typed `Parameters`
   and historical entry points as compatibility adapters to the generic API.
   No probability calculations or domain construction belong in those adapters.

For each migration, compare independent tiny support and probability tables,
exercise malformed outcomes through PDDL decoding, and run larger sampled
membership checks. Reusing the same interpreter for both sides is not independent
evidence. These bounded checks do not establish an arbitrary-size equivalence
proof; public evidence must state the actual verification scope.

Preserving probability laws does not promise the same task for each seed. A new
implementation can consume random draws differently. Record sampler implementation
provenance separately from distribution revision, and retain existing generated
data. Any proposed change to the probability law or failure policy needs a
separate distribution decision.

The expected tradeoff is more explicit domain content and a larger interpreter.
The benefit is one execution engine and public executable probability contracts.
Do not claim this will reduce total code or reproduce efficient hand-written
algorithms automatically; evaluate those properties in the first prototype.
