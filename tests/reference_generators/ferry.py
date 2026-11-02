"""Semantic sampling and PDDL compatibility entry points for ferry."""

from __future__ import annotations

from pypddl_datasets.generators.runtime import Problem, RandomSource, atom, objects
from pypddl_datasets.generators.classical.ferry.parameters import Parameters


def sample(parameters: Parameters, rng: RandomSource) -> Problem:
    """Sample independent car origins, destinations and ferry location."""
    cars = [f"c{i}" for i in range(parameters.num_cars)]
    locations = [f"l{i}" for i in range(parameters.num_locations)]
    origins = [rng.choice(locations) for _ in cars]
    destinations = [rng.choice(locations) for _ in cars]
    initial = [atom("location", location) for location in locations]
    initial.extend(atom("car", car) for car in cars)
    initial.extend(atom("not-eq", left, right)
                   for left in locations for right in locations if left != right)
    initial.append(atom("empty-ferry"))
    initial.extend(atom("at", car, origin) for car, origin in zip(cars, origins))
    initial.append(atom("at-ferry", rng.choice(locations)))
    return Problem(
        f"ferry-l{parameters.num_locations}-c{parameters.num_cars}", "ferry",
        objects([*locations, *cars]), tuple(initial),
        tuple(atom("at", car, destination) for car, destination in zip(cars, destinations)),
    )
