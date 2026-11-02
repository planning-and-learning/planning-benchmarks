# Independent sampler references

These are the revision-2 Python sampling algorithms captured on 2026-09-16,
before the ProbLog pilot changed the production generators. They are test-only
oracles. Do not update them to agree with a migrated generator: disagreements
must be investigated as possible changes to the distribution.

The source was copied from `/tmp/problog-pilot-baseline`, created from the
working tree before migration. SHA-256 hashes of the original complete files:

- `ferry/generator.py`: `5b37b92eceedec782764cd3de42c03a591d06931c9ebe35fed485630b4dfb1ca`
- `delivery/generator.py`: `7cc972eaf47473083d5967f4f888a18554abb7fb609d0a94b4c91aacf96f2427`
- `rovers/generator.py`: `039aed74b305cd1387bf1fc3764be268df4214b25dc54e9bd1d8bf309023e639`
- `runtime.py`: `c0600149202ad04ff88630e242b62513b701b073cca0d9b627b491b0551e463a`

Only CLI/rendering wrappers and their unused imports were removed. Parameter
imports now refer to the public validated dataclasses. Rovers imports its frozen
graph functions from `graphs.py`; record types (`Problem`, `Atom`, etc.) and
exceptions still come from the shared runtime. No sampling algorithm was changed.
The independent declarative `distribution.spec` files remain a separate oracle
for allowed labeled task support.
