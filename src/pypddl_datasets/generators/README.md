# Generators

A fully Python variant of [AI-planning/pddl-generators](https://github.com/AI-Planning/pddl-generators).

Every generator exposes `make_problem(...)` and ships a fixed `domain.pddl`.
Flashfill and classical Pathways are excluded because their domain changes per task.

## Beluga 2025

`classical.beluga2025.scalability_deterministic` generates fresh training tasks
for the fixed domain in `data/classical/beluga2025/scalability-deterministic`.
The domain is included in the package; generation does not download benchmark data.

```python
from pypddl_datasets.generators.classical.beluga2025.scalability_deterministic import make_problem

problem = make_problem(num_flights=3, jigs_per_flight=2, num_racks=3, seed=42)
```

```sh
python -m pypddl_datasets.generators.classical.beluga2025.scalability_deterministic.generator \
  --num-flights 3 --jigs-per-flight 2 --num-racks 3 --seed 42 > problem.pddl
```

This independent training distribution keeps the challenge's five jig types,
flight capacity 40, ordered loading/unloading, two-sided racks, and ordered
production lines. It targets similar storage and scheduling structure rather
than the competition's exact sampling probabilities:

- Each rack gets a capacity between `min_rack_size` and `max_rack_size`, allowing
  some jigs to fit only some racks. Set the bounds equal for identical racks.
- `initial_occupancy` sets a target fraction of occupied rack space. Initial jigs
  mix loaded and empty states. Discrete jig sizes can overshoot the target;
  filling also stops if no jig fits the remaining gaps.
- Each incoming flight carries one jig type. Batch sizes respect flight capacity
  and a greedy packing check against inventory still on site.
- Production follows arrivals with delays up to `max_delivery_delay`. Jobs due
  together are shuffled among balanced production lines. The final flight also
  completes outstanding production, including its own incoming jigs.
- Return flights batch one type from initially empty jigs or jigs produced on
  earlier flights. Returns release capacity for subsequent incoming batches;
  empty jigs without a return flight remain on site.

Type sampling defaults to uniform. `jig_type_distribution=1` prefers small jigs
by choosing the smaller of two uniform draws; `2` chooses the larger. There is
no fixed probability table. Both draws use the currently fitting candidates.
Flights may have empty incoming or outgoing loads when storage or production
limits what is available. Packing checks ignore rack access order, so ordering
deadlocks can still make a task unsolvable. All parameters are scalar and seeded.

The earlier `rack_size` and `initial_jigs` parameters have been replaced by the
rack-size bounds and occupancy target. For a small learning example:

```python
problem = make_problem(num_flights=2, jigs_per_flight=1, initial_occupancy=0,
                       min_rack_size=4, max_rack_size=8, max_delivery_delay=0, seed=42)
```

# Polynomially Recognizable Deadend Domains

- barman
- blocks_3
- childsnack
- hiking
- hiking_binary
- nomystery
- parcprinter
- rovers
- schedule
- tpp
- spanner
- woodworking
