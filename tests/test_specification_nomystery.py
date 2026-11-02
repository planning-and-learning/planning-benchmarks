"""Hand-built transport cases test the independent exact Nomystery specification."""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import product

import pytest

pytest.importorskip("z3")
pytest.importorskip("pypddl")

# These imports intentionally follow the optional-dependency checks.
# pylint: disable=wrong-import-position
from pypddl_datasets.generators.classical.nomystery.parameters import Parameters
from pypddl_datasets.generators.classical.nomystery.generator import fuel_budget
from pypddl_datasets.generators import load_specification
from pypddl_datasets.generators.runtime import Assignment, Atom, Metric, Object, Problem, atom, objects, render_problem
# pylint: enable=wrong-import-position


@dataclass(frozen=True)
class Route:
    """Explicit truck and package endpoints, without a route-finding algorithm."""

    truck: int
    starts: tuple[int, ...]
    goals: tuple[int, ...]


def problem_for(parameters: Parameters, roads: tuple[tuple[int, int, int], ...], route: Route, fuel: int) -> Problem:
    """Serialize a supplied finite instance; the caller supplies the claimed fuel."""
    maximum = max(fuel, parameters.max_edge_cost)
    initial: list[Atom | Assignment] = [Assignment(atom("total-cost"), 0)]
    for left, right, cost in roads:
        for source, target in ((left, right), (right, left)):
            initial.extend((atom("connected", f"l{source}", f"l{target}"),
                            atom("fuelcost", f"level{cost}", f"l{source}", f"l{target}")))
    initial.extend(atom("sum", f"level{after}", f"level{cost}", f"level{after + cost}")
                   for cost in sorted({road[2] for road in roads}) for after in range(maximum - cost + 1))
    initial.extend((atom("at", "t0", f"l{route.truck}"), atom("fuel", "t0", f"level{fuel}")))
    initial.extend(atom("at", f"p{index}", f"l{location}") for index, location in enumerate(route.starts))
    universe = objects((f"l{i}" for i in range(parameters.num_locations)), "location") + objects(["t0"], "truck")
    universe += objects((f"p{i}" for i in range(parameters.num_packages)), "package")
    universe += objects((f"level{i}" for i in range(maximum + 1)), "fuellevel")
    return Problem("hand-built", "transport-strips", universe, tuple(initial),
                   tuple(atom("at", f"p{index}", f"l{location}") for index, location in enumerate(route.goals)),
                   Metric(atom("total-cost")))


def test_two_location_exact_support_includes_both_truck_starts() -> None:
    parameters = Parameters(2, 1, max_edge_cost=1)
    specification = load_specification("nomystery", parameters)
    for truck, origin in product(range(2), repeat=2):
        # One unit if truck starts with the package; otherwise travel back first.
        fuel = 1 if truck == origin else 2
        problem = problem_for(parameters, ((0, 1, 1),), Route(truck, (origin,), (1 - origin,)), fuel)
        assert specification.check_pddl(render_problem(problem)).is_member
    result = specification.enumerate(limit=4, timeout_ms=5000)
    assert result.complete
    assert len(result.situations) == 4


def test_exact_optimum_uses_fuel_weights_instead_of_the_number_of_drives() -> None:
    parameters = Parameters(3, 1, max_edge_cost=5)
    specification = load_specification("nomystery", parameters)
    roads = ((0, 1, 1), (1, 2, 1), (0, 2, 5))
    route = Route(0, (0,), (2,))
    shortest_fuel = problem_for(parameters, roads, route, 2)
    shortest_steps = problem_for(parameters, roads, route, 5)
    assert specification.check_pddl(render_problem(shortest_fuel)).is_member
    assert not specification.check_pddl(render_problem(shortest_steps)).is_member


def test_pickup_precedence_and_multiple_packages_constrain_the_optimum() -> None:
    parameters = Parameters(3, 2, max_edge_cost=1)
    specification = load_specification("nomystery", parameters)
    roads = ((0, 1, 1), (1, 2, 1))
    route = Route(1, (0, 2), (2, 0))
    # Visiting all endpoints costs three; completing both opposing deliveries costs five.
    assert specification.check_pddl(render_problem(problem_for(parameters, roads, route, 5))).is_member
    assert not specification.check_pddl(render_problem(problem_for(parameters, roads, route, 3))).is_member


def test_fuel_scaling_preserves_the_float_product_rounding_boundary() -> None:
    parameters = Parameters(3, 1, max_edge_cost=3, constrainedness=1.2)
    specification = load_specification("nomystery", parameters)
    roads = ((0, 1, 2), (1, 2, 3))
    route = Route(0, (0,), (2,))
    # 1.2 is below 6/5 as an exact binary rational, but the Python product rounds to 6.0.
    assert int(1.2 * 5) == 6
    assert specification.check_pddl(render_problem(problem_for(parameters, roads, route, 6))).is_member
    assert not specification.check_pddl(render_problem(problem_for(parameters, roads, route, 5))).is_member
    assert not specification.check_pddl(render_problem(problem_for(parameters, roads, route, 7))).is_member


@pytest.mark.parametrize("removed", [atom("fuelcost", "level2", "l0", "l1"), atom("sum", "level0", "level2", "level2")])
def test_missing_weight_or_subtraction_fact_is_bound_false(removed: Atom) -> None:
    parameters = Parameters(2, 1, max_edge_cost=2)
    specification = load_specification("nomystery", parameters)
    problem = problem_for(parameters, ((0, 1, 2),), Route(0, (0,), (1,)), 2)
    assert removed in problem.initial
    changed = replace(problem, initial=tuple(fact for fact in problem.initial if fact != removed))
    assert not specification.check_pddl(render_problem(changed)).is_member


def test_numeric_metric_and_level_namespace_are_fully_bound() -> None:
    parameters = Parameters(2, 1, max_edge_cost=2)
    specification = load_specification("nomystery", parameters)
    problem = problem_for(parameters, ((0, 1, 2),), Route(0, (0,), (1,)), 2)
    nonzero = replace(problem, initial=(Assignment(atom("total-cost"), 1), *problem.initial[1:]))
    extra_level = replace(problem, objects=(*problem.objects, Object("level3", "fuellevel")))
    wrong_sum = replace(problem, initial=(*problem.initial, atom("sum", "level1", "level2", "level0")))
    missing_number = replace(problem, initial=problem.initial[1:])
    for changed in (nonzero, extra_level, wrong_sum, missing_number, replace(problem, metric=None)):
        assert not specification.check_pddl(render_problem(changed)).is_member


def test_connectivity_positive_weights_and_probability_one_are_constraints() -> None:
    parameters = Parameters(3, 1, max_edge_cost=2)
    route = Route(0, (0,), (1,))
    disconnected = problem_for(parameters, ((0, 1, 1),), route, 1)
    zero_weight = problem_for(parameters, ((0, 1, 0), (1, 2, 1)), route, 0)
    assert not load_specification("nomystery", parameters).check_pddl(render_problem(disconnected)).is_member
    assert not load_specification("nomystery", parameters).check_pddl(render_problem(zero_weight)).is_member
    chain = problem_for(parameters, ((0, 1, 1), (1, 2, 1)), route, 1)
    complete_only = load_specification("nomystery", replace(parameters, edge_probability=1))
    assert not complete_only.check_pddl(render_problem(chain)).is_member


def test_float_fuel_budget_can_round_below_large_integer_optimum() -> None:
    # Exercise the production scaling boundary without allocating its enormous PDDL level universe.
    optimum = 2**53 + 1
    assert fuel_budget(optimum, 1.0) == 2**53
    assert fuel_budget(optimum, 1.0) < optimum
    assert fuel_budget(5, 1.2) == 6
