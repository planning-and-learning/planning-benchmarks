"""Semantic, graph and fuel tests for generators without committed splits."""
from __future__ import annotations
from collections.abc import Callable, Iterator, Sequence
from itertools import permutations, product
from pathlib import Path
import random
from typing import TypeVar

import pytest

from pypddl_datasets.generators.classical.nomystery import generator as nomystery
from pypddl_datasets.generators.classical.rovers import generator as rovers
from pypddl_datasets.generators.classical.schedule import generator as schedule
from pypddl_datasets.generators.classical.spanner import generator as spanner
from pypddl_datasets.generators.classical.visitall import generator as visitall
from pypddl_datasets.generators.classical.woodworking import generator as woodworking
from pypddl_datasets.generators.runtime import Atom, Problem, render_problem

T = TypeVar("T")
ROOT = Path(__file__).resolve().parents[1] / "src/pypddl_datasets/generators/classical"


def facts(problem: Problem, predicate: str) -> frozenset[tuple[str, ...]]:
    return frozenset(fact.arguments for fact in problem.initial
                     if isinstance(fact, Atom) and fact.predicate == predicate)


@pytest.mark.parametrize(("domain", "generate"), [
    ("nomystery", lambda: nomystery.sample(nomystery.Parameters(3, 2), random.Random(0))),
    ("rovers", lambda: rovers.sample(rovers.Parameters(2, 3, 2, 0, 2), random.Random(0))),
    ("schedule", lambda: schedule.sample(schedule.Parameters(2), random.Random(0))),
    ("spanner", lambda: spanner.sample(spanner.Parameters(2, 1, 2), random.Random(0))),
    ("visitall", lambda: visitall.sample(visitall.Parameters(2), random.Random(0))),
    ("woodworking", lambda: woodworking.sample(woodworking.Parameters(4, 2), random.Random(0))),
])
def test_complex_rendering_parses(domain: str, generate: Callable[[], Problem]) -> None:
    pytest.importorskip("pypddl")
    from pypddl.formalism import Parser, ParserOptions
    options = ParserOptions()
    options.strict = True
    options.add_action_costs = False
    parser = Parser(ROOT / domain / "domain.pddl", options)
    parser.parse_task(render_problem(generate()))


def test_spanner_exact_tiny_support(monkeypatch: pytest.MonkeyPatch) -> None:
    reached: set[tuple[str, str]] = set()
    for decisions in product(range(2), repeat=2):
        choices = iter(decisions)
        def choose(sequence: Sequence[T], decisions: Iterator[int] = choices) -> T:
            return sequence[next(decisions)]
        rng = random.Random(0)
        monkeypatch.setattr(rng, "choice", choose)
        generated = spanner.sample(spanner.Parameters(2, 1, 2), rng)
        positions = {args[0]: args[1] for args in facts(generated, "at")}
        reached.add((positions["spanner1"], positions["spanner2"]))
    assert reached == set(product(("location1", "location2"), repeat=2))


def _event_route_cost(distances: list[list[int]], truck: int,
                      starts: tuple[int, ...], goals: tuple[int, ...]) -> int:
    """Independent oracle: enumerate all precedence-respecting event orders."""
    events = tuple((package, stage) for package in range(len(starts)) for stage in range(2))
    costs: list[int] = []
    for order in permutations(events):
        if any(order.index((package, 0)) > order.index((package, 1))
               for package in range(len(starts))):
            continue
        route = [truck, *((starts if stage == 0 else goals)[package] for package, stage in order)]
        costs.append(sum(distances[left][right] for left, right in zip(route, route[1:])))
    return min(costs)


def test_nomystery_minimum_fuel_against_event_enumeration() -> None:
    from pypddl_datasets.generators.classical.nomystery.generator import minimum_fuel
    distances = [[0, 2, 5], [2, 0, 3], [5, 3, 0]]
    pairs = [(start, goal) for start in range(3) for goal in range(3) if start != goal]
    for truck, first, second in product(range(3), pairs, pairs):
        starts, goals = (first[0], second[0]), (first[1], second[1])
        assert minimum_fuel(distances, truck, list(starts), list(goals)) == _event_route_cost(
            distances, truck, starts, goals)


def test_nomystery_large_costs_have_no_arbitrary_infinity() -> None:
    from pypddl_datasets.generators.classical.nomystery.generator import shortest_paths
    cost = 10**20
    assert shortest_paths([[None, cost, None], [cost, None, cost], [None, cost, None]])[0][2] == 2 * cost


def test_nomystery_probability_alias_and_full_graph() -> None:
    assert nomystery.Parameters().probability == 0.5
    assert nomystery.Parameters(7, edge_factor=1.5, edge_probability=None).probability == 0.5
    assert nomystery.Parameters(6, edge_factor=1.5, edge_probability=None).probability == 0.6
    assert nomystery.Parameters(3, edge_factor=100, edge_probability=0.25).probability == 0.25
    task = nomystery.sample(nomystery.Parameters(3, 2, edge_probability=1), random.Random(1))
    assert facts(task, "connected") == frozenset((f"l{i}", f"l{j}")
                                               for i in range(3) for j in range(3) if i != j)
    origins = {args[0]: args[1] for args in facts(task, "at")}
    assert all(origins[goal.arguments[0]] != goal.arguments[1] for goal in task.goal)


def test_rovers_support_cyclic_movement_and_calibration() -> None:
    task = rovers.sample(rovers.Parameters(2, 3, 2, 0, 3, edge_probability=1), random.Random(2))
    visibility = facts(task, "visible")
    assert len(visibility) == 6
    for rover in ("rover0", "rover1"):
        traversals = {(left, right) for carrier, left, right in facts(task, "can_traverse") if carrier == rover}
        assert traversals == visibility
    camera_carriers = {args[0]: args[1] for args in facts(task, "on_board")}
    assert {args[0] for args in facts(task, "equipped_for_imaging")} == set(camera_carriers.values())
    assert all(any(camera == supported[0] for supported in facts(task, "supports"))
               for camera in camera_carriers)
    assert facts(task, "store_of") == frozenset({("rover0store", "rover0"), ("rover1store", "rover1")})


def test_rovers_single_waypoint_keeps_empty_goal_boundary() -> None:
    task = rovers.sample(rovers.Parameters(1, 1, 1, 0, 5, edge_probability=0), random.Random(0))
    assert not facts(task, "visible")
    assert not facts(task, "can_traverse")
    assert not task.goal


def test_schedule_probability_endpoints() -> None:
    absent = schedule.Parameters(1, cylindrical_goal_probability=0, initial_colour_probability=0,
                                 goal_colour_probability=0, initial_hole_probability=0,
                                 goal_hole_probability=0, goal_surface_probability=0)
    task = schedule.sample(absent, random.Random(0))
    assert not task.goal and not facts(task, "painted") and not facts(task, "has-hole")
    present = schedule.Parameters(1, cylindrical_goal_probability=100, initial_colour_probability=100,
                                  goal_colour_probability=100, initial_hole_probability=100,
                                  goal_hole_probability=100, goal_surface_probability=100)
    task = schedule.sample(present, random.Random(0))
    assert len(task.goal) == 4
    assert len(facts(task, "painted")) == len(facts(task, "has-hole")) == 1


@pytest.mark.parametrize("width,height", [(1, 1), (1, 3), (3, 1), (2, 2)])
def test_visitall_geometry_and_zero_goal_ratio(width: int, height: int) -> None:
    task = visitall.sample(visitall.Parameters(width, height, goal_ratio=0), random.Random(0))
    assert len(task.objects) == width * height
    assert len(task.goal) == 1
    assert task.goal[0].arguments in facts(task, "visited")
    assert len(facts(task, "connected")) == 2 * ((width - 1) * height + (height - 1) * width)


def test_visitall_every_cell_can_be_unavailable(monkeypatch: pytest.MonkeyPatch) -> None:
    reached: set[str] = set()
    for missing in range(4):
        rng = random.Random(0)
        def remove_cell(population: Sequence[T], k: int, index: int = missing) -> list[T]:
            assert k == 1
            return [population[index]]
        monkeypatch.setattr(rng, "sample", remove_cell)
        task = visitall.sample(visitall.Parameters(2, 2, num_unavailable=1), rng)
        all_names = {f"loc-x{x}-y{y}" for x in range(2) for y in range(2)}
        reached.update(all_names - {item.name for item in task.objects})
    assert len(reached) == 4


@pytest.mark.parametrize("factor", [1.0, 2.0])
def test_woodworking_capacity_and_initial_goal_relationship(factor: float) -> None:
    for seed in range(20):
        task = woodworking.sample(woodworking.Parameters(5, 2, factor), random.Random(seed))
        sizes = {"small": 1, "medium": 2, "large": 3}
        part_sizes = {name: sizes[size] for name, size in facts(task, "goalsize")}
        required = sum(part_sizes[name] for (name,) in facts(task, "unused"))
        capacity = sum(int(size[1:]) for _, size in facts(task, "boardsize"))
        assert capacity == factor * required
        initial = {fact for fact in task.initial if isinstance(fact, Atom)}
        for part in (item.name for item in task.objects if item.type_name == "part"):
            goals = {goal for goal in task.goal if goal.arguments[0] == part}
            assert 3 <= len(goals) <= 5
            assert not goals.issubset(initial)
        assert sum(item.type_name in woodworking.MACHINES for item in task.objects) == 14


@pytest.mark.parametrize("invalid", [
    lambda: nomystery.Parameters(1), lambda: nomystery.Parameters(edge_probability=0),
    lambda: rovers.Parameters(1, 2, 1, 0, 1, 0), lambda: schedule.Parameters(1, num_shapes=3),
    lambda: spanner.Parameters(1, 2, 1), lambda: visitall.Parameters(1, num_unavailable=1),
    lambda: woodworking.Parameters(1, 1, float("nan")),
    lambda: nomystery.Parameters(num_packages=0), lambda: nomystery.Parameters(max_edge_cost=0),
    lambda: nomystery.Parameters(constrainedness=0.5),
    lambda: nomystery.Parameters(edge_factor=float("inf")),
    lambda: nomystery.Parameters(edge_probability=float("nan")),
    lambda: rovers.Parameters(0, 2, 1, 0, 1), lambda: rovers.Parameters(1, 2, 1, -1, 1),
    lambda: rovers.Parameters(1, 2, 1, 0, 1, 1.1),
    lambda: schedule.Parameters(0), lambda: schedule.Parameters(1, num_colours=0),
    lambda: schedule.Parameters(1, goal_hole_probability=101),
    lambda: spanner.Parameters(0, 1, 1), lambda: spanner.Parameters(1, 1, 0),
    lambda: visitall.Parameters(1, height=0), lambda: visitall.Parameters(1, goal_ratio=float("nan")),
    lambda: woodworking.Parameters(0, 1), lambda: woodworking.Parameters(1, 0),
    lambda: woodworking.Parameters(1, 1, 0.5),
])
def test_invalid_complex_parameters(invalid: Callable[[], object]) -> None:
    with pytest.raises(ValueError):
        invalid()
