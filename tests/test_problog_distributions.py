"""Independent legacy laws and declarative support for the ProbLog pilot.

Every queried task binds all declared semantic variables, including absent atoms
and optional objects. Enumerating sampled seeds is not used to establish support.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from fractions import Fraction
import random
import re

import pytest

from reference_generators import delivery, ferry, rovers
from reference_generators.tracing import TaskKey, Trace, distribution, signature
from pypddl_datasets.generators import load_specification
from pypddl_datasets.generators.probabilistic import evaluate_model, sample_model
from pypddl_datasets.generators.runtime import Atom, Problem, render_problem

pytest.importorskip("z3")
pytest.importorskip("pypddl")

from pypddl_datasets.generators._specifications.core import SemanticKey, Situation, Specification  # pylint: disable=wrong-import-position

Parameters = ferry.Parameters | delivery.Parameters | rovers.Parameters


@dataclass(frozen=True)
class Case:
    domain: str
    parameters: Parameters
    sample: Callable[[Trace], Problem]
    weights: dict[Fraction, int]


def cases() -> tuple[Case, ...]:
    results: list[Case] = []
    for cars, locations in ((0, 1), (0, 2), (1, 1), (1, 2), (2, 2)):
        parameters = ferry.Parameters(cars, locations)
        count = locations ** (2 * cars + 1)
        results.append(Case("ferry", parameters, lambda rng, params=parameters: ferry.sample(params, rng),
                            {Fraction(1, count): count}))
    for packages in (1, 2):
        parameters_delivery = delivery.Parameters(2, packages)
        weights = {Fraction(1, 48): 48} if packages == 1 else {Fraction(1, 192): 48, Fraction(1, 256): 192}
        results.append(Case("delivery", parameters_delivery,
                            lambda rng, params=parameters_delivery: delivery.sample(params, rng), weights))
    for cameras in (0, 1):
        parameters_rovers = rovers.Parameters(1, 1, 1, cameras, 1)
        weights = {Fraction(1, 49): 28, Fraction(1, 7): 3} if cameras == 0 else {Fraction(2, 49): 21, Fraction(1, 49): 7}
        results.append(Case("rovers", parameters_rovers,
                            lambda rng, params=parameters_rovers: rovers.sample(params, rng), weights))
    return tuple(results)


def interpretation(specification: Specification, problem: Problem) -> Situation:
    """Bind the entire independent contract, including all omitted output facts."""
    names = {item.name for item in problem.objects}
    initial, goal = set(problem.initial), set(problem.goal)
    values: list[tuple[SemanticKey, bool | int]] = []
    for key in specification.semantic_variables:
        if key.kind == "object":
            value = key.predicate in names
        else:
            assert key.kind == "atom"
            value = Atom(key.predicate, key.arguments) in (initial if key.group == "initial" else goal)
        values.append((key, value))
    return Situation(tuple(values))


def quoted(value: str) -> str:
    if re.fullmatch(r"[a-z][a-zA-Z0-9_]*", value):
        return value
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


def binding_query(index: int, situation: Situation) -> str:
    """Conjunction of positive and negative facts for one whole labeled task."""
    literals: list[str] = []
    for key, value in situation.values:
        if key.kind == "object":
            type_name = "untyped" if key.arguments[0] == "object" else key.arguments[0]
            term = f"object({quoted(key.predicate)},{quoted(type_name)})"
        else:
            assert key.kind == "atom"
            atom = quoted(key.predicate)
            if key.arguments:
                atom += "(" + ",".join(map(quoted, key.arguments)) + ")"
            term = f"{key.group}({atom})"
        literals.append(term if value else "\\+ " + term)
    return f"outcome({index}) :- " + ", ".join(literals) + f".\nquery(outcome({index}))."


def compare_probabilities(domain: str, parameters: Parameters,
                          weights: dict[TaskKey, Fraction], problems: dict[TaskKey, Problem]) -> None:
    """Compare every legacy task, with total mass ruling out missing alternatives."""
    specification = load_specification(domain, parameters)
    keys = list(weights)
    source = "\n".join(binding_query(index, interpretation(specification, problems[key]))
                       for index, key in enumerate(keys))
    actual = evaluate_model(domain, parameters, source)
    expected = {f"outcome({index})": weights[key] for index, key in enumerate(keys)}
    assert actual.keys() == expected.keys()
    assert all(value > 0 for value in actual.values())
    # Tiny finite categorical laws are exact rationals, independently of seeds.
    assert actual == expected
    assert sum(actual.values(), Fraction()) == sum(expected.values(), Fraction())


@pytest.mark.parametrize("case", cases(), ids=lambda case: f"{case.domain}-{case.parameters}")
def test_complete_pilot_task_probabilities_and_support(case: Case) -> None:
    weights, problems = distribution(case.sample)
    assert Counter(weights.values()) == case.weights
    specification = load_specification(case.domain, case.parameters)
    permitted = specification.enumerate(limit=len(weights), timeout_ms=30_000)
    assert permitted.complete
    assert {interpretation(specification, problem).identity for problem in problems.values()} == {
        situation.identity for situation in permitted.situations}
    compare_probabilities(case.domain, case.parameters, weights, problems)
    for seed in range(3):
        problem = sample_model(case.domain, case.parameters, random.Random(seed))
        assert signature(problem) in weights
        assert specification.check_pddl(render_problem(problem)).is_member


@pytest.mark.parametrize("budget", [1, 2, 3])
def test_rovers_local_graph_retries_preserve_complete_joint_law(budget: int) -> None:
    """All seven connected graph pairs plus failure, with finite local retries."""
    from dataclasses import asdict
    from itertools import combinations

    edges = ((0, 1), (0, 2), (1, 2))
    graphs = [*combinations(edges, 2), edges]
    queries: list[str] = []
    expected: dict[str, Fraction] = {}
    visibility_mass = (1 - Fraction(1, 2) ** budget) / 4
    for visibility in graphs:
        for movement in graphs:
            if not set(movement).issubset(visibility):
                continue
            def prolog_graph(values: tuple[tuple[int, int], ...]) -> str:
                return "[" + ",".join(f"e({a},{b})" for a, b in values) + "]"
            index = len(expected)
            queries.append(f"pair({index}) :- visibility({prolog_graph(visibility)}),"
                           f"movement(0,{prolog_graph(movement)}).\nquery(pair({index})).")
            movement_mass = 1 - Fraction(3, 4) ** budget if len(visibility) == 2 else visibility_mass
            expected[f"pair({index})"] = visibility_mass * movement_mass
    expected["failure(graph_exhausted)"] = 1 - sum(expected.values(), Fraction())
    queries.append("query(failure(graph_exhausted)).")
    parameters = {**asdict(rovers.Parameters(1, 3, 1, 0, 1)), "graph_budget": budget}
    assert evaluate_model("rovers", parameters, "\n".join(queries)) == expected


def test_rovers_camera_repair_preserves_owner_and_append_order() -> None:
    """Requested ownership and all four repair subsets for each of three owners."""
    from itertools import combinations

    expected: dict[str, Fraction] = {}
    queries: list[str] = []
    for owner in range(3):
        remaining = [rover for rover in range(3) if rover != owner]
        for size in range(3):
            for repaired in combinations(remaining, size):
                index = len(expected)
                literals = [f"camera_owner(0,{owner})"]
                literals.extend(f"camera_owner({camera},{rover})"
                                for camera, rover in enumerate(repaired, start=1))
                literals.append(f"\\+ camera_owner({size + 1},_)")
                queries.append(f"owners({index}) :- " + ",".join(literals) + f".\nquery(owners({index})).")
                expected[f"owners({index})"] = Fraction(1, 3) * Fraction(4, 7) ** size * Fraction(3, 7) ** (2 - size)
    actual = evaluate_model("rovers", rovers.Parameters(3, 1, 1, 1, 1), "\n".join(queries))
    assert actual == expected
    assert sum(actual.values(), Fraction()) == 1


def _image_goal_weights(supported: tuple[str, ...], visible_count: int) -> dict[frozenset[str], Fraction]:
    from itertools import product
    weights: defaultdict[frozenset[str], Fraction] = defaultdict(Fraction)
    for count in (2, 3, 4):
        attempts = min(count, 2 * visible_count)
        for draws in product(supported, repeat=attempts):
            weights[frozenset(draws)] += Fraction(1, 3 * len(supported) ** attempts)
    return dict(weights)


def _image_query(index: int, visible: tuple[int, ...], supported: tuple[str, ...],
                 requested: frozenset[str]) -> str:
    literals: list[str] = []
    for site in range(2):
        term = f"objective_visible(0,{site})"
        literals.append(term if site in visible else "\\+ " + term)
    for mode in ("colour", "high_res", "low_res"):
        term = f"camera_mode(0,{mode})"
        literals.append(term if mode in supported else "\\+ " + term)
        term = f"goal(communicated_image_data(objective0,{mode}))"
        literals.append(term if mode in requested else "\\+ " + term)
    return f"images({index}) :- " + ",".join(literals) + f".\nquery(images({index}))."


def test_rovers_replacement_visibility_and_image_goal_deduplication() -> None:
    """Complete joint marginal over visible sites, camera modes and image goals."""
    from itertools import combinations

    modes = ("colour", "high_res", "low_res")
    expected: dict[str, Fraction] = {}
    queries: list[str] = []
    visibility_laws = {(0,): Fraction(3, 8), (1,): Fraction(3, 8), (0, 1): Fraction(1, 4)}
    for visible, visibility_mass in visibility_laws.items():
        for size in range(1, 4):
            for supported in combinations(modes, size):
                for requested, goal_mass in _image_goal_weights(supported, len(visible)).items():
                    index = len(expected)
                    queries.append(_image_query(index, visible, supported, requested))
                    expected[f"images({index})"] = visibility_mass * Fraction(1, 7) * goal_mass
    actual = evaluate_model("rovers", rovers.Parameters(1, 2, 1, 1, 3, edge_probability=1), "\n".join(queries))
    assert actual == expected
    assert sum(actual.values(), Fraction()) == 1


@pytest.mark.parametrize("at_threshold", [False, True])
def test_rovers_rare_edge_draw_keeps_the_legacy_float_threshold(
    at_threshold: bool, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Force a rare legal edge and its strict boundary; never rely on observing it."""
    from dataclasses import asdict
    import math
    from pypddl_datasets.generators.runtime import GenerationExhausted
    from reference_generators.graphs import connected_edges

    probability = 5e-9
    draw = probability if at_threshold else math.nextafter(probability, 0.0)
    rng = random.Random(0)
    monkeypatch.setattr(rng, "random", lambda: draw)

    def last(start: int, stop: int | None = None, step: int = 1) -> int:
        return (range(start) if stop is None else range(start, stop, step))[-1]

    # The categorical path deliberately disagrees with the real-valued draw.
    # Bernoulli edges must use the same threshold operation as the old sampler.
    monkeypatch.setattr(rng, "randrange", last)
    parameters = {**asdict(rovers.Parameters(1, 2, 1, 0, 1, probability)), "graph_budget": 1}
    if at_threshold:
        with pytest.raises(GenerationExhausted):
            connected_edges(2, rng, probability, max_attempts=1)
        with pytest.raises(GenerationExhausted):
            sample_model("rovers", parameters, rng)
    else:
        assert connected_edges(2, rng, probability, max_attempts=1) == {(0, 1)}
        problem = sample_model("rovers", parameters, rng)
        visible = {fact.arguments for fact in problem.initial
                   if isinstance(fact, Atom) and fact.predicate == "visible"}
        assert visible == {("waypoint0", "waypoint1"), ("waypoint1", "waypoint0")}


def test_rovers_image_targets_keep_visibility_multiplicity_weights() -> None:
    """A twice-visible objective has twice the incidence weight, before drawing."""
    parameters = rovers.Parameters(1, 2, 2, 1, 1, edge_probability=1)
    source = """
    sites :- objective_visible(0,0), \\+ objective_visible(0,1),
             objective_visible(1,0), objective_visible(1,1).
    weights :- sites, graphs(_,Gs),image_weight(Gs,0,0,2),image_weight(Gs,1,0,4).
    wrong :- sites, graphs(_,Gs),image_weight(Gs,0,0,4).
    query(sites). query(weights). query(wrong).
    """
    assert evaluate_model("rovers", parameters, source) == {
        "sites": Fraction(3, 32), "weights": Fraction(3, 32), "wrong": Fraction()}


def test_rovers_default_graph_budget_preserves_failure_and_draw_count() -> None:
    from typing_extensions import override
    from pypddl_datasets.generators.runtime import GenerationExhausted

    class RejectingEdges(random.Random):
        def __init__(self) -> None:
            super().__init__(0)
            self.draws = 0

        @override
        def random(self) -> float:
            self.draws += 1
            return 0.9999999999999999

    parameters = rovers.Parameters(1, 2, 1, 0, 1)
    legacy_rng = RejectingEdges()
    with pytest.raises(GenerationExhausted):
        rovers.sample(parameters, legacy_rng)
    assert legacy_rng.draws == 10_000
    migrated_rng = RejectingEdges()
    with pytest.raises(GenerationExhausted):
        sample_model("rovers", parameters, migrated_rng)
    assert migrated_rng.draws == legacy_rng.draws
