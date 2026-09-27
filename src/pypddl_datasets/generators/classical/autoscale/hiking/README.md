# hiking (autoscale)

Couples walk a linear route leg by leg; cars move tents and people so that a pitched tent waits at the end of every leg.

## Source

- **Domain:** Lee McCluskey (University of Huddersfield, produced with GIPO), IPC 2014; Autoscale's copy, lowercased
- **Generator:** Autoscale's `pddl-generators/hiking/generator.py` by Lee McCluskey, called as `generator.py {n_couples} {n_cars} {n_places} {seed}`; re-exports `../../ipc/hiking` (same distribution)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/hiking`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/hiking`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_couples` | couples (= tents) | agile: 1–2, optimal: 1–2 |
| `num_cars` | cars (Autoscale: couples + 1..5 + slope) | agile: 4–13, optimal: 3–12 |
| `num_places` | places on the route | agile: 9–25, optimal: 2–28 |

## Distribution

### Objects
`car0..`, `tent0..`/`couple0..`, `place0..`, `guy{i}`/`girl{i}` per couple.

### Initial state
Everything at `place0`, `(walked couple place0)`, `partners` facts, the `next` chain; each tent `up` or `down` with probability 1/2.

### Goal
`(walked couple{i} place{n-1})` for every couple.

### Other
No action costs. Problem name `hiking-{couples}-{cars}-{places}`, as in the Autoscale tasks. See `../../ipc/hiking`.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| all objects, persons, tents and cars at `place0` | 60/60 | always |
| tents initially up | agile 25/44 (57 %), optimal 27/45 (60 %) | 47 % (200 samples) |
| problem name | `hiking-1-4-10` | same scheme |

**Deviations:** none beyond sampling noise in the up/down share.
