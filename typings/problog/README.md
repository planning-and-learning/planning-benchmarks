These partial stubs describe the ProbLog 2.3.0 interfaces used by the generator
backend. They are not a complete typing distribution for ProbLog. Dynamic term,
engine context and database internals retain `Any`; project parameter, task and
probability APIs have concrete types. Check these signatures against the pinned
upstream implementation when upgrading it, and rerun the numerical, aggregation,
conditioning and concurrent-sampling regressions.
