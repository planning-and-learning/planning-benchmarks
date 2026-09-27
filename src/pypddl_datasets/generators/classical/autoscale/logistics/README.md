# logistics (autoscale)

Packages move between locations with trucks inside cities and airplanes between city airports.

## Source

- **Domain:** Manuela Veloso (first version); AIPS-1998 version by Bart Selman and Henry Kautz; Autoscale's copy (logistics98 encoding), lowercased
- **Generator:** Autoscale's `pddl-generators/logistics/logistics.c` (FF domain collection, (C) 2001 Albert Ludwigs University Freiburg), called as `logistics -r {seed} -a {airplanes} -c {cities} -s {city_size} -p {packages} -t {cities}`; own Python port in `generator.py` (differs from `../../ipc/logistics`)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/logistics`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/logistics`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cities` | cities (one airport each) | agile: 8–66, optimal: 2–6 |
| `city_size` | locations per city | agile: 15–32, optimal: 2–16 |
| `num_packages` | packages | agile: 3–98, optimal: 1–14 |
| `num_airplanes` | airplanes | agile: 5–34, optimal: 2–8 |
| `num_trucks` | trucks, default one per city | = cities in all 60 tasks |

## Distribution

### Objects
`a{i}`, `c{i}`, `t{i}`, `l{c}-{k}`, `p{i}`; untyped with type predicates.

### Initial state
Type facts, `in-city`, airport `l{c}-0` per city. Truck `i < num_cities` at a uniform location of city `i`, further trucks at uniform locations anywhere; packages at uniform locations; airplanes at uniform airports.

### Goal
`(at p l)` for every package, `l` uniform over all locations (may equal the start, as upstream).

### Other
No action costs. Problem name `logistics-c{cities}-s{size}-p{packages}-a{airplanes}-t{trucks}`. Always solvable.

## Comparison with reference tasks

| aspect | reference tasks | this generator (same sizes) |
|---|---|---|
| goals per package | 1.00 (agile 1511/1511, optimal 203/203) | 1.00 |
| goal equals start | agile 0/1511, optimal 12/203 | agile 1/1511, optimal 12/203 |
| trucks at an airport | agile 34/1110, optimal 15/75 | agile 50/1110, optimal 10/75 |
| packages at an airport | agile 64, optimal 25 | agile 66, optimal 28 |
| problem name | `logistics-c8-s15-p3-a5` | `logistics-c8-s15-p3-a5-t8` |

**Deviations:** none in the distribution; problem names carry the truck count.
