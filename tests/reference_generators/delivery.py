"""Semantic sampling and PDDL compatibility entry points for delivery."""

from __future__ import annotations

from pypddl_datasets.generators.runtime import Atom, Problem, RandomSource, atom, objects
from pypddl_datasets.generators.classical.delivery.parameters import Parameters


def _adjacency(grid_size: int) -> tuple[Atom, ...]:
    return tuple(atom("adjacent", f"c_{x}_{y}", f"c_{a}_{b}")
                 for x in range(grid_size) for y in range(grid_size)
                 for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
                 if 0 <= a < grid_size and 0 <= b < grid_size)


def sample(parameters: Parameters, rng: RandomSource) -> Problem:
    """Sample package/truck placements and a common nontrivial destination."""
    cells = [f"c_{x}_{y}" for x in range(parameters.grid_size)
             for y in range(parameters.grid_size)]
    packages = [f"p{i}" for i in range(1, parameters.num_packages + 1)]
    locations = [rng.choice(cells) for _ in packages]
    initial = list(_adjacency(parameters.grid_size))
    initial.extend(atom("at", package, location) for package, location in zip(packages, locations))
    initial.extend((atom("at", "t1", rng.choice(cells)), atom("empty", "t1")))
    choices = [cell for cell in cells if len(set(locations)) != 1 or cell != locations[0]]
    destination = rng.choice(choices)
    return Problem(
        f"delivery-{parameters.grid_size}x{parameters.grid_size}-{parameters.num_packages}", "delivery",
        objects(cells, "cell") + objects(packages, "package") + objects(["t1"], "truck"),
        tuple(initial), tuple(atom("at", package, destination) for package in packages),
    )
