# hiking_binary (misc)

Our variant of Hiking in which the ternary `partners` relation is split into two binary `partner_of` facts.

## Source

- **Domain:** our variant of the IPC 2014 Hiking domain by Lee McCluskey (University of Huddersfield); `walk_together` requires two distinct `partner_of` persons of the couple
- **Generator:** same draws as `../hiking` (pddl-generators `hiking/generator.py` by Lee McCluskey); Python code in `generator.py`
- **Reference tasks:** none (no IPC tasks use this encoding); compared with `data/classical/downward-benchmarks/hiking-opt14-strips`, `data/classical/downward-benchmarks/hiking-sat14-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_couples` | couples (= tents) | 1–3 (as hiking) |
| `num_cars` | cars, must be `>= num_couples + 1` | 2–4 (as hiking) |
| `num_places` | places on the route, `>= 2` | 3–8 (as hiking) |

## Distribution

### Objects
As `../hiking`: `car0..`, `tent0..`, `couple0..`, `place0..`, `guy{i}`/`girl{i}`.

### Initial state
As `../hiking`, with `(partner_of couple{i} guy{i})` and `(partner_of couple{i} girl{i})` instead of `(partners couple{i} guy{i} girl{i})`. Tents are `up`/`down` with probability 1/2 each.

### Goal
`(walked couple{i} place{n-1})` for every couple.

### Other
No action costs. Problem name `hiking-binary-{couples}-{cars}-{places}`. Parameters that upstream considers unsolvable (`num_cars < num_couples + 1`, `num_places < 2`) are rejected.

## Comparison with reference tasks

| aspect | reference tasks (hiking IPC 2014) | this generator |
|---|---|---|
| random choices | tent up/down | identical to `../hiking` (same RNG draws) |
| partner facts per couple | 1 ternary `partners` | 2 binary `partner_of` |
| tasks with `num_cars == num_couples` | 13 of 40 | not generated |

**Deviations:**
- Encoding differs by design (binary partner predicates).
