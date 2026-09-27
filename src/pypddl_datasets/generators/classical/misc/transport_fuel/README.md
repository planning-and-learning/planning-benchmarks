# transport_fuel (misc)

Transport with consumable per-truck fuel and no refuelling. Our own variant; no reference tasks exist.

## Source

- **Domain:** our variant of IPC 2008 Transport (domain `transport-fuel`, no action costs)
- **Generator:** own generator, `generator.py`
- **Reference tasks:** none

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations` | locations | – |
| `num_trucks` | trucks | – |
| `num_packages` | packages | – |
| `capacity` | capacity of every truck | – |
| `extra_edges` | undirected roads beyond a spanning tree | – |
| `fuel` | initial fuel of every truck | default: constructive bound |

## Distribution

### Objects
As `ipc/transport`, plus fuel levels `fuel0..fuel<fuel>` (type `fuellevel`). Name `transport-fuel-l<L>-t<T>-p<P>-c<C>-e<E>-f<F>`.

### Initial state
As `ipc/transport` (random spanning tree plus `extra_edges`, uniform truck and package locations, equal capacities), plus a `fuel-predecessor` chain and every truck starting at `fuel`. Each drive consumes one unit.

### Goal
Every package at a uniform location different from its start.

### Other
No costs or metric. With `fuel=None` the budget is enough for the first truck to deliver the packages one at a time along shortest paths, so tasks are solvable; smaller explicit budgets may be unsolvable.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| – | no reference tasks | – |

**Deviations:** none found (no reference).
