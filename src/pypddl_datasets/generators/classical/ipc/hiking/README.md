# hiking (ipc)

Couples walk a linear route leg by leg; cars move tents and people so that a pitched tent waits at the end of every leg.

## Source

- **Domain:** Lee McCluskey (University of Huddersfield, produced with GIPO), IPC 2014
- **Generator:** pddl-generators `hiking/generator.py` by Lee McCluskey; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/hiking-opt14-strips`, `data/classical/downward-benchmarks/hiking-sat14-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_couples` | couples (= tents, 2 persons each) | opt14: 1–2, sat14: 1–3 |
| `num_cars` | cars | opt14: 2–4, sat14: 2–4 |
| `num_places` | places on the route | opt14: 3–8, sat14: 5–8 |

## Distribution

### Objects
`car0..`, `tent0..`/`couple0..` (one tent per couple), `place0..place{n-1}`, `guy{i}`/`girl{i}` per couple.

### Initial state
Everything starts at `place0`: every person, tent and car; `(walked couple{i} place0)`; `(partners couple{i} guy{i} girl{i})`. The route is the chain `(next place{i} place{i+1})`. Each tent is independently `up` or `down` with probability 1/2 — the only random choice.

### Goal
`(walked couple{i} place{n-1})` for every couple.

### Other
No action costs. Problem name `hiking-{couples}-{cars}-{places}`. Solvable when `num_cars >= num_couples + 1` (upstream's note); the CLI enforces that bound, `make_problem` does not.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| object counts per type, init/goal predicate counts (all 40 tasks, same parameters) | — | identical in all 40 |
| init facts other than up/down (ptesting-3-4-8) | — | identical set |
| tents initially up | 40/81 (49 %) | 50 % |
| problem name | `Hiking-3-4` | `hiking-3-4-8` |

**Deviations:**
- The CLI rejects `num_cars < num_couples + 1`, but 13 of the 40 IPC tasks (2-2-*, 3-3-*) have `num_cars == num_couples`; use `make_problem` for those.
- Problem names carry the place count and are lowercase.
