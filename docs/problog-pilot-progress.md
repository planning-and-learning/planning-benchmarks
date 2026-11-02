# ProbLog pilot progress

Objective: migrate Ferry, Delivery and full Rovers through a shared declarative
backend, preserve their task laws and public signatures, and establish the
practical operating range. Progress recorded on 2026-09-16.

## Implementation and optimization

- Added public per-domain `distribution.pl` models, a shared sampler and exact
  inference API, and generic output decoding. No domain-specific Python generation
  callbacks were added. Existing `make_problem` signatures remain.
- Retained independent `distribution.spec` contracts and froze the imperative
  algorithms as separate test oracles with provenance hashes.
- Corrected numeric cutoffs, binary64 rounding and RNG isolation, including
  nested aggregation and concurrent program preparation.
- Added generic native finite choices, Bernoulli subsets, graph operations and
  ground-list traversal, retaining pure Prolog reference definitions.
- Added bounded thread-local preparation reuse and per-world selector memoization.
  Shared primitive identities, duplicate tickets and output unification remain.
- Fixed image-incidence sampling after native-world checks exposed a discrepancy
  that inference-only checks missed. Both endpoints now contribute explicitly.
- Rejected broad and exact-call cross-formula caches after variable-binding
  counterexamples changed query answers. Those experiments remain separate.
- Fixed quoted primitive extensions so they also trigger interpreted fallback.
  This later guard correction leaves all measured bundled execution paths intact.

## Correctness and packaging

- All nine complete tiny inferred and native-sampled task laws match the frozen
  imperative oracles. Independent specifications enumerate the same tiny supports.
- The complete two-waypoint Rovers proof passed all 12,444 tasks, all 31 partitions
  and exact total mass one: 20.13 minutes, 624 MiB peak RSS. Its immutable artifact
  and validation of the unchanged inference dependencies are under
  `experiments/problog/verification/`.
- Regression checks cover local retry laws, 10,000-proposal exhaustion, rare float
  thresholds, camera repair, image multiplicities, shared choice identities,
  cache lifetime, failed output matches and concurrent RNG isolation.
- Full Python 3.13 suite passed 556 tests before the final sampling-only changes.
  Post-cache native checks passed 51 cases on both Python 3.10 and 3.13. Final
  quoted-fallback/backend/preparation checks passed 67 on 3.13 and 20 on 3.10;
  cache/API/runtime integration passed 115. Pyright and Pylint pass.
- Final wheel and source distribution contain every ProbLog resource; every
  packaged backend Python file matches the final source. Wheel-only checks without
  optional solvers passed 118 cases on each of Python 3.10 and 3.13.
- Final full-suite verification against all changes passed 578 tests on Python
  3.13 in 614.35 seconds, with one bundled pyparsing deprecation warning. Output:
  `/tmp/problog-release-full-suite.log`.

## Performance and recommendation

- Final representative matrix completed all 36 tasks; the additional size survey
  completed seven cases and recorded three 75-second timeouts, with no generation
  exceptions. Reports include source hashes, parameter provenance, setup, task
  timings, output hashes, memory and resource limits.
- Rovers25: corrected interpreted model 73.47 s versus optimized first task 1.52 s;
  cached peak RSS 51.8 MiB. Rovers100: 17–19 s/task, 231.3 MiB. Imperative means
  remain 8.23 ms and 0.69 s, respectively.
- IPC-large and the 1,000/5,500-waypoint HTG cases remain outside the demonstrated
  range under the measurement budget. Hold broad migration; keep the independent
  checks and assess further execution improvements against intended dataset volume.
- `docs/problog-pilot-performance.md` records reproduction commands, all outcomes,
  scaling causes and the post-measurement guard-fix validation. The pilot document
  lists remaining blockers for all twenty other domains and states the complexity
  tradeoff: compact domain authoring requires a more complex shared runtime.

Final checkpoint complete: full-suite verification passed all 578 tests.
