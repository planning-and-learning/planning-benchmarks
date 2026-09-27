# mystery (ipc)

Logistics with fuel stored at locations and limited vehicle space, with every predicate and object disguised by an unrelated name.

## Source

- **Domain:** Drew McDermott, AIPS-1998 competition
- **Generator:** McDermott's original generator is not public. pddl-generators `mystery/mystery.c` (FF domain collection, Jörg Hoffmann) is a typed, renamed adaptation with a ring road and a goal for every cargo, which the IPC tasks do not follow; `generator.py` implements the distribution measured on the IPC tasks
- **Reference tasks:** `data/classical/downward-benchmarks/mystery` (prob01–30; `mprime` prob01–30 are the same tasks)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | locations (`food`) | 4–22 |
| `num_vehicles` | vehicles (`pleasure`), at most `num_locations` | 1–16 |
| `num_cargos` | cargos (`pain`) | 2–46 |
| `num_fuel_levels` | fuel levels (`province`) | 3–13 |
| `num_space_levels` | space levels (`planet`) | 2–4 |
| `num_goals` | cargos with a goal | 1–3 |

## Distribution

### Objects
Untyped; names drawn without replacement from the name pools observed in the IPC tasks (53 foods, 17 pleasures, 14 pains, 13 provinces, 10 planets). A pool that runs out continues with `<name>-<k>`, k = 1, 2, ... (IPC does this for pains). Objects are listed food, pleasure, pain, province, planet.

### Initial state
- Kind facts `(food l)`, `(pleasure v)`, `(pain c)`, `(province f)`, `(planet s)` for every object.
- Roads `eats` (symmetric): every location links to one uniformly random other location; components are then joined by random edges, and remaining degree-1 locations get another random road until every location has degree ≥ 2 (for 3+ locations).
- Fuel chain `(attacks f_i f_i+1)` and space chain `(orbits s_i s_i+1)` over the listed order.
- `(locale l f)`: fuel at each location, uniform over all fuel levels.
- `(harmony v s)`: free space of each vehicle, uniform over all space levels except the lowest.
- `(craves v l)`: vehicles at pairwise distinct uniform locations; `(craves c l)`: cargos at uniform locations.
- Relation facts are shuffled, as in the IPC tasks.

### Goal
`num_goals` distinct uniform cargos, each `(craves c l)` for a uniform location (possibly its start, i.e. already satisfied). All other cargos are unconstrained.

### Other
No action costs. Problem name `strips-mysty-l<L>-v<V>-c<C>-f<F>-s<S>-g<G>` (IPC: `strips-mysty-x-<index>`). Solvability is not checked; the IPC set also contains unsolvable tasks.

## Comparison with reference tasks

Measured over the 35 IPC mprime tasks (prob01–30 equal mystery) and 20 generated tasks per IPC parameter tuple.

| aspect | reference tasks | this generator |
|---|---|---|
| roads per location | 1.268 | 1.288 |
| share of degree-2 locations | 0.579 | 0.595 |
| mean max degree | 3.83 | 4.17 |
| roads connected, min degree 2 | 35/35 | always |
| mean location fuel / (fuel levels − 1) | 0.483 | 0.496 |
| vehicle space 1/2/3 share (4 levels) | 0.32 / 0.32 / 0.36 | 0.35 / 0.33 / 0.32 |
| vehicles at distinct locations | 35/35 | always |
| cargos sharing a location with a vehicle | 0.439 | 0.430 |
| goals already satisfied initially | 0.080 | 0.090 |

**Deviations:**
- Max degree slightly higher (4.17 vs 3.83): the road model is calibrated, not McDermott's unknown procedure.
- Name suffixes are `-1..-k`; IPC suffixes skip numbers (e.g. `grief-7` with only 6 suffixed pains).
- Problem names encode the parameters instead of the IPC index.
