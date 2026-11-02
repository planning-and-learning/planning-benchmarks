# Generator distributions and migration

Distribution revision **2** implements the approved migration of all 23 classical
generators and all 17 learning split recipes. Seeded output changes are intentional;
the regenerated corpus and its manifests are the new reproducibility baseline.
Previously published data releases remain immutable.

## Public contract

Every domain has three public files beside its `domain.pddl`:

- `parameters.py`: a frozen `Parameters` dataclass validating the supported inputs.
- `generator.py`: `sample(parameters, rng) -> Problem`, `render(problem) -> str`,
  and the historical `make_problem` and command-line entry points.
- `distribution.spec`: a complete declarative contract, with parameters, metadata,
  declarations, and named rules grouped as `initial`, `goal`, and `joint`.

The public `pypddl_datasets.generators` discovery API lists the domains, parameter
names, distribution revision, probability law, solvability policy, evidence scope,
and raw specification text through `get_specification(domain).source`. Discovery,
source inspection, and generation work with the base installation, including Lark.
`load_specification(domain, parameters, *, max_groundings=None)` accepts a dataclass
or mapping and compiles the contract without importing generator construction code. `pypddl-datasets[specs]` adds Z3 and the existing PDDL parser for
executable membership and enumeration. Specifications are shipped public API;
tests consume those same specifications.

```python
from random import Random
from pypddl_datasets.generators import get_specification, load_specification
from pypddl_datasets.generators.classical.blocks_4.generator import Parameters, sample, render

print(get_specification("blocks_4").source)
parameters = Parameters(num_blocks=3)
problem = sample(parameters, Random(7))
spec = load_specification("blocks_4", parameters)
result = spec.check_pddl(render(problem))
assert result.is_member, result
for constraint in spec.initial:
    print(constraint.name, constraint.source, constraint.formula)
reference = spec.enumerate(limit=200, timeout_ms=10_000)
assert reference.complete
assert len(reference.situations) == 169
```

## Logical language and semantic identity

Specifications use quantified finite relational logic in one self-contained
`distribution.spec` per domain. A shared Lark grammar and generic compiler ground
these files into the Z3 checking engine. For fixed parameters the declarations
define a finite typed object universe, Boolean relations, and bounded integers.
Cardinality, ranking, and finite dynamic programming express the rules explicitly.
Related domains repeat their constraints locally; there are no domain imports,
templates, Python callbacks, or shared domain constraint builders. The
[language reference](specification-language.md) describes the syntax and semantics.

The optional `max_groundings` budget stops construction with a source-located
`SpecificationError`; it never returns a partially constrained specification.
Ground numeric expressions follow Python integer and binary64 arithmetic, including
operation order and conversions. Symbolic arithmetic is Boolean/integer affine.
Probability laws and evidence remain readable metadata, separate from support.

A task's support is the set of labeled interpretations satisfying all three groups.
Object presence, static facts, initialized fluents, goal membership, and the metric
belong to the interpretation. Labels are significant. Task names, whitespace, fact
order, random seeds, and auxiliary witnesses do not define different semantic tasks.
Acyclicity ranks, latent goal attributes, and optimal-cost witnesses are projected
out during model enumeration.

A goal variable states whether a positive atom occurs in the goal conjunction.
An absent goal atom imposes no requirement on the final planning state. It does
not mean that atom must be false. Membership nevertheless binds that goal-membership
variable to false when absent. All absent initial atoms are also bound to false;
the solver cannot complete a malformed initial state by inventing facts. Numeric
initializations must be present. Unexpected vocabulary, objects, unsupported goal
syntax, and mismatched metrics are rejected.

`check_pddl` decodes through `pypddl` in strict mode without synthetic action costs.
It returns `member`, `nonmember`, `unknown`, or `timeout`, with named violations where
available. Enumeration returns `complete` only after the remaining projected model
space is proved empty. `limit`, `unknown`, and `timeout` are inconclusive results.
The optional solver can be expensive for large finite universes; bounded examples
are the intended exhaustive-check workload.

## What the evidence establishes

These obligations remain separate:

| Obligation | Evidence |
| --- | --- |
| Parameter validity | Explicit dataclass checks and boundary tests. |
| Soundness | Independent parsing and membership tests on generated tasks; malformed-task tests exercise the oracle. |
| Support completeness | Exact specification enumeration compared with sampler choice enumeration for tractable finite cases. |
| Weighting | Exact rational probability mass for selected finite choice trees and declared graph proposals. |
| Solvability | Domain-specific constructive conditions or independent tiny planning checks; no universal solvability requirement. |
| Reproducibility | Manifest replay, semantic hashes, byte comparisons, runtime and revision provenance. |

Three-block Blocksworld has 13 labeled arrangements and 169 independent initial/goal
pairs. Exhaustive choice tests check their uniform weights. Tiny graph checks cover
all 64 edge subsets on four vertices, identify the 38 connected graphs independently
by cuts, and verify the Bernoulli proposal mass. Grid shape tests cover all six
surjections from three keys onto two shapes. Further domain-specific checks cover
support witnesses, parameter boundaries, numeric resource relationships, topology,
and goal selection. Public descriptions report the scope actually checked.

A finite seed sweep cannot prove that a generator has full support. Tiny exhaustive
tests also do not prove arbitrary-size completeness. Logic describes permitted
situations; it does not assign their probabilities. Repairs, projection, and
rejection change weights and are documented in the probability law. General proofs
and exact weights for every domain and size remain outside the verified evidence.

## Approved distribution changes

| Family | Revision 2 behavior |
| --- | --- |
| Driverlog | Independent simple undirected connected road and path graphs; both directions emitted. |
| Nomystery | Connected weighted graph with positive costs; exact minimum travel fuel determines the fuel budget. |
| Rovers | Connected visibility sampled first; each rover gets a connected traversal subset of that visibility. |
| Barman | Uniform goal-shot subset, preserving the recipe and beverage laws. |
| Satellite | Uniform instrument ownership and calibration; supported modes are the set of two independent uniform draws; observation selection retains instrument-then-mode weighting. |
| Grid | Uniform surjective key/lock shape assignments without distinguished-label anchors; constructive reachable key placement; diagonal lock layouts are allowed. |
| Floortile | Uniform assignment of the existing balanced white/black robot color counts; distinct robot columns retained. |
| Logistics | Uniform airport in each city and uniform truck-label/city bijection, one truck per city. |
| Visitall | Every grid cell can be selected as unavailable; grid adjacency and the original quantized goal-inclusion law remain. |

For freely generated movement graphs, each candidate edge is independently selected
with probability `p`, then the proposal is accepted only if connected. The typed
APIs default to `p = 0.5`. At that value the accepted graph is uniform over connected
labeled graphs in the candidate universe. Other probabilities give the conditional
Bernoulli law. Rovers samples each traversal within its already sampled visibility;
unioning independently sampled traversal graphs would change visibility's law.
Nomystery retains `int(constrainedness * optimum)` with Python floating-point
multiplication. At very large integer costs this can round below the optimum even
when constrainedness is 1; solvability requires the resulting budget to cover the
optimum. Nomystery's historical `edge_factor` alias resolves to
`min(1, 2 * edge_factor / (num_locations - 1))`; an explicit edge probability wins.

Geometric grids and fixed directed routes retain their family structure. In
particular, Visitall does not promise that removing cells leaves a connected grid.
Driverlog, Logistics, and Grid retain their nonempty-goal singleton repair laws.
These differ from Bernoulli selection conditioned on a nonempty set. TPP retains
independent stock draws that can be insufficient. Schedule retains partial and
possibly empty goals. Solvability is stated per domain in public descriptions.

## Shared implementation and operational behavior

`runtime.py` supplies immutable semantic objects, atoms, assignments, metrics and
problems, a `RandomSource` protocol, canonical rendering, semantic hashing, and the
conditional connected-graph sampler. Shared Blocksworld and Hiking helpers factor
common construction. Each generator keeps domain-specific algorithms and named
parameters. There is no common mutable superclass or positional parameter tuple API.

Invalid typed parameters raise `ValueError`. Legacy wrappers retain their established
calling conventions and invalid-result behavior where feasible. `Rejected(reason)`
is an explicit unsuccessful proposal; `GenerationExhausted` is an operational
failure, distinct from invalid parameters and nonmembership. Graph sampling has a
proposal budget. Exhaustion propagates instead of silently restarting an already
partially sampled hierarchy, which could bias its parent distribution. Even with propagation, conditioning on a
whole task completing can reweight earlier choices when later failure probabilities
depend on them. The ideal hierarchical law and the explicit failure outcome must
therefore be distinguished from weights among completed tasks. Goldminer's
retained soft-path walk terminates almost surely but has no finite deterministic
step bound.

## Learning split policy and provenance

The 17 `generate_instances.py` entry points declare finite typed structural spaces.
Invalid parameter combinations are removed before assigning quotas. Spaces must
be disjoint across train/validation/test. Complete shuffled cycles plus an unbiased
partial last cycle keep each configuration's count within floor/ceiling of its
quota. Configurations outside an old lexicographic prefix now receive support.
A rejected proposal retries the same assigned configuration; it never transfers
that configuration's quota to an easier one.

SHA-256-derived streams separate scheduling and each task's attempts by master seed,
domain, split, task index, and attempt index. The fixed corpus uses master seed 0.
All families retain 100 tasks per split, except Gripper's deterministic 5/5/10.
This gives 4,820 tasks and 51 manifests. Parameter diversity does not establish
semantic uniqueness or increasing planning difficulty; duplicates remain legal.

Each manifest records the distribution revision, package/Python versions, domain
hash, parameter policy, configuration count, retry budget, task parameters,
accepted seed, all attempt seeds, rejection counts/reasons, and byte and semantic
hashes. The semantic hash preserves object labels and ignores serialization order.
The runner stages all three splits before replacing managed task files, so a
sampling failure leaves an existing domain's splits intact.

```sh
python -m pypddl_datasets.generators.classical.grid.generate_instances \
  --master-seed 0 --output-root data/classical/generated
```

Exact reproduction is tied to recorded versions and the supported runtime. A
historical seed is not a promise of historical output after a distribution revision.

## Checks and release migration

Pyright checks all source and tests strictly with the Python 3.10 language target;
there is no generator exclusion. Pylint checks generator correctness, duplication,
and complexity: 12 branches, 50 statements, 15 locals, five nested blocks, and five
arguments. Compatibility signatures have narrowly scoped exceptions. CI tests
Python 3.10 and 3.13 with base and optional-specification installs.

```sh
pip install -e '.[dev,specs]'
pyright
pylint src/pypddl_datasets/generators tests/test_generator*.py tests/test_specification*.py
python -m pypddl_datasets.scripts.large_files unpack
pytest tests
python -m pypddl_datasets.validation --root data --strict
python -m pypddl_datasets.scripts.extract_requirements --data-root data
python -m pypddl_datasets.validation.requirements --root data
python -m pypddl_datasets.scripts.package_data --output dist/data.tar.gz
python -m build
```

The existing data-and-package release workflow publishes the new immutable data
archive and updates the package's data pin. This implementation prepares the corpus,
metadata, documentation, and checks; it does not publish a release or change the
pin to an unpublished asset. A checkout can use its regenerated corpus immediately
through `PYPDDL_DATASETS_DATA`.

## Declarative specification migration

The declarative switch preserves distribution revision 2, all sampler and parameter
implementations, split recipes, and every generated task/domain/manifest byte.
The 23 preliminary Python specification modules and two domain constraint helper
files were removed. There is one complete contract per domain and one generic
parser/compiler.

Before removal, a separate copy of the Python implementation served as a migration
reference. Eleven bounded projected support sets matched exactly across Gripper,
Blocks 3/4, Ferry, Grid, Rovers, and Nomystery. Woodworking resource projections
matched for factors 1 and 2. Another 1,194 single-atom membership mutations agreed
across the 20 simpler domains. Existing independent sampler/support tests remain
in the suite; the saved implementation is not a runtime or test dependency. These
checks establish bounded migration evidence, not arbitrary-size equivalence.

The footprint below includes the public facade/metadata loader, checking framework,
parser/compiler/grammar, and domain specifications. It excludes tests, documentation,
and unchanged generator code. Line counts include comments and blank lines.

| Specification source | Before | After |
| --- | ---: | ---: |
| Total files | 31 | 32 |
| Total lines (Python + DSL + grammar) | 1,958 | 3,023 |
| Python lines | 1,958 | 1,388 |

The domain contracts are now local and declarative, and there is less Python.
Total source is larger because the language adds parsing, finite grounding, and
validation infrastructure. This migration does not claim an overall code-size
reduction.
