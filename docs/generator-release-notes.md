# Unreleased: generator distribution revision 2

All 23 classical generators now provide validated frozen parameters, injected random
sources, semantic problem values, and shared rendering. Public specifications ship
as self-contained `distribution.spec` files beside the generators, with named
initial, goal, and joint constraints. Lark is a base dependency; Z3 stays optional. The base
package supports discovery and generation; install `pypddl-datasets[specs]` for
independent PDDL membership and bounded logical enumeration.

The switch from Python specification builders to declarative files preserves
revision 2 support, samplers, and existing task/manifest bytes. Use
`get_specification(domain).source` to inspect a contract and
`load_specification(domain, parameters)` to execute it. The preliminary per-domain
`build_specification` modules have been removed.

The earlier revision 2 generator migration intentionally changes seeded output. Connected movement graphs and
interchangeable label choices follow the approved revision 2 laws described in the
[design and migration document](generator-design.md). Woodworking preserves its
legacy board-group ordering. Historical module entry points and `make_problem`
wrappers remain available.

All 17 learning recipes now use balanced shuffled configuration cycles, fixed
configuration retries, and digest-derived seed streams. The 4,820 committed tasks
have been regenerated into 51 splits using master seed 0. Their manifests include
parameters, attempt seeds, rejection counts, distribution/runtime provenance, and
byte and semantic fingerprints. A second full regeneration reproduced every task
and manifest exactly.

Verification covers exact small-domain support and weights, invalid situations,
probability boundaries, larger committed examples, and public import behavior with
and without optional dependencies. These are bounded results, not arbitrary-size
completeness proofs. Descriptions expose the evidence and solvability scope for each
family. Nomystery's retained floating-point scaling and finite hierarchical sampling
budgets have explicit qualifications.

Strict Pyright includes all generators, specifications, and tests. Pylint enforces
correctness, duplication, and complexity limits. CI exercises Python 3.10 and 3.13
with base and specification dependencies. The metadata parser cache is bounded to
avoid retaining native syntax trees for the entire dataset during freshness checks.

The complete dataset passed strict validation: 16,550 tasks and 2,744 domain files,
with zero errors. Requirements metadata was regenerated and remained identical.
The prepared archive contains 19,363 verified files in 474 domain directories,
including all 51 manifests:

- File: `dist/data.tar.gz`
- Size: 186,432,704 bytes
- SHA-256: `bbe93899177b7269f3121344ef2ecfc42d39c30846782a54caa3daab7b1207bb`

Wheel and source distributions are prepared locally. The wheel includes all 23
specifications and generator domain files, and excludes benchmark data and
repository-only tooling. The source distribution includes the design, tests, and
focused typing stubs.

Publishing uses the existing **data-and-package** release workflow, which creates
an immutable data release and updates the package's data pin. Until that release,
use `PYPDDL_DATASETS_DATA` pointing at this checkout's `data/` directory to select
the regenerated corpus. The local build retains the current package version;
version and release tags are assigned by the release workflow.
