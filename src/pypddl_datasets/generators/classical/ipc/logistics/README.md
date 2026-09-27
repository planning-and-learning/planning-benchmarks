# logistics (ipc)

Packages move between locations with trucks inside cities and airplanes between city airports.

## Source

- **Domain:** Manuela Veloso (first version); AIPS-1998 version by Bart Selman and Henry Kautz; used in AIPS-1998 and AIPS-2000
- **Generator:** pddl-generators `logistics/logistics.c` (FF domain collection, (C) 2001 Albert Ludwigs University Freiburg); Python port in `generator.py`, extended to the structure of the IPC tasks
- **Reference tasks:** `data/classical/downward-benchmarks/logistics98` (`style="98"`, `domain.pddl`), `data/classical/downward-benchmarks/logistics00` (`style="00"`, `domain_logistics00.pddl`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cities` | cities (one airport each) | 98: 3–47, 00: 2–5 |
| `city_size` | locations per city | 98: 2–17, 00: 2 (required) |
| `num_packages` | packages | 98: 3–57, 00: 3 per city |
| `num_airplanes` | airplanes | 98: 1–15, 00: 1–2 |
| `num_trucks` | trucks, at least one per city (default: one per city) | 98: 5–106 (1–13 per city), 00: one per city (required) |
| `num_goals` | packages with a goal (default: all) | 98: 3–45 (coverage 0.25–1.0), 00: 4–15 (coverage 0.67–1.0) |
| `style` | `"98"` or `"00"`: IPC structure and encoding | |

## Distribution

### Objects
- `"98"`: `package{i}`, `city{c}`, `truck{t}`, `plane{a}`, locations `city{c}-{k}` (k = 1..`city_size`); untyped, type predicate `obj`.
- `"00"`: `obj{c}{k}`, `cit{c}`, `tru{c}`, `apn{a}`, locations `pos{c}` and `apt{c}`; untyped, type predicate `package`.

### Initial state
- Type predicates and `(in-city loc city)`; the airport of a city is its last location (`city{c}-{city_size}` / `apt{c}`).
- `"98"`: truck `i` < `num_cities` starts in city `i`, further trucks in uniformly random cities; every truck at a uniform location of its city. Packages start at uniform locations over all cities.
- `"00"`: one truck per city at its `pos`; packages are assigned to cities round-robin and start at their city's `pos`.
- Airplanes start at uniformly random airports (several may share one).

### Goal
`num_goals` distinct packages, drawn uniformly, get `(at package location)` with the location uniform over all locations, so a goal may already hold.

### Other
- No action costs.
- Problem name `logistics{style}-c{cities}-s{size}-p{packages}-a{airplanes}-t{trucks}-g{goals}`.
- Solvable by construction: every city has an airport and a truck, every airport is reachable by airplane.

## Comparison with reference tasks

Each IPC task regenerated at its own cities, city size, packages, airplanes, trucks and goals (10 seeds each), per-task means:

| aspect | logistics98 | this generator (`"98"`) | logistics00 | this generator (`"00"`) |
|---|---|---|---|---|
| trucks per city (1 / 2 / 3 / 4 / 5) | 267 / 99 / 64 / 40 / 23 cities | 259 / 96 / 75 / 43 / 22 | always 1 | always 1 |
| goal coverage | 0.828 | 0.828 | 0.890 | 0.890 |
| goal already holds | 0.036 | 0.039 | 0.189 | 0.182 |
| goal at an airport | 0.357 | 0.312 | 0.500 | 0.492 |
| goal in the start city | 0.107 | 0.120 | 0.399 | 0.370 |
| packages starting at an airport | 0.283 | 0.316 | 0 | 0 |
| trucks starting at an airport | 0.139 | 0.304 | 0 | 0 |
| domain encoding | `obj` | `obj` (`domain.pddl`) | `package` | `package` (`domain_logistics00.pddl`) |

Before this revision the generator had one truck per city, never generated a goal that already holds, gave every package a goal by default and started logistics00-sized tasks at airports about 50% of the time.

**Deviations:**
- logistics98 trucks start at airports about half as often as a uniform draw gives (0.14 vs 0.30); the IPC mechanism is unknown, and uniform placement covers it.
- Problem and object names follow the IPC pattern but not the IPC object order.
