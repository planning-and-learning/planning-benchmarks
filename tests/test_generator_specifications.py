"""Independent logical support checks, projected completeness, and counterexamples."""
from __future__ import annotations

# Optional dependencies must be skipped before executable specification imports.
# pylint: disable=wrong-import-position

from collections.abc import MutableSequence, Sequence
from fractions import Fraction
from importlib import import_module
from pathlib import Path
from typing import Protocol, TypeVar, cast
import random

import pytest
pytest.importorskip("z3")
pytest.importorskip("pypddl")

import z3
from test_generator_simple import ChoiceTrace, enumerate_integer_choices
from reference_generators import ferry as ferry_reference, rovers as rovers_reference

from pypddl_datasets.generators import load_specification
from pypddl_datasets.generators._specifications import core
from pypddl_datasets.generators._specifications.core import Group, SemanticKey, Situation, Specification
from pypddl_datasets.generators._specifications.decoding import decode_pddl
from pypddl_datasets.generators.classical.blocks_3 import parameters as blocks_three
from pypddl_datasets.generators.classical.blocks_4 import parameters as blocks_four
from pypddl_datasets.generators.classical.ferry import parameters as ferry
from pypddl_datasets.generators.classical.gripper import parameters as gripper
from pypddl_datasets.generators.classical.grid import parameters as grid
from pypddl_datasets.generators.classical.goldminer import parameters as goldminer
from pypddl_datasets.generators.classical.rovers import parameters as rovers
from pypddl_datasets.generators.runtime import Problem, RandomSource, render_problem


T = TypeVar("T")


class CategoricalTrace:
    """Finite ideal draws; fractional Bernoulli laws are outside this test helper.

    The tested parameter cases use only Bernoulli endpoints. A fixed real draw
    therefore preserves their support and mass without tracing random PRNG bits.
    """
    def __init__(self, prefix: tuple[int, ...]) -> None:
        self.trace = ChoiceTrace(prefix)

    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
        return self.trace.randrange(start, stop, step)

    def randint(self, a: int, b: int) -> int:
        return self.randrange(a, b + 1)

    def random(self) -> float:
        return 0.5

    def choice(self, seq: Sequence[T]) -> T:
        return seq[self.randrange(len(seq))]

    def sample(self, population: Sequence[T], k: int) -> list[T]:
        remaining = list(population)
        return [remaining.pop(self.randrange(len(remaining))) for _ in range(k)]

    def shuffle(self, x: MutableSequence[T]) -> None:
        for index in range(len(x) - 1, 0, -1):
            other = self.randrange(index + 1)
            x[index], x[other] = x[other], x[index]


class GeneratorModule(Protocol):
    """Boundary for parametrized domain tests; concrete APIs remain typed."""
    def sample(self, parameters: object, rng: RandomSource) -> Problem: ...


def _situation(spec: Specification, problem: Problem) -> Situation:
    domain = Path(__file__).parents[1] / "src/pypddl_datasets/generators/classical" / spec.domain / "domain.pddl"
    situation, _ = decode_pddl(domain, render_problem(problem))
    supplied = dict(situation.values)
    return Situation(tuple((key, supplied.get(key, False)) for key in spec.semantic_variables))


def _changed(situation: Situation, group: str, predicate: str, arguments: tuple[str, ...], value: bool) -> Situation:
    values = dict(situation.values)
    values[SemanticKey(group, "atom", predicate, arguments)] = value
    return Situation(tuple(values.items()))


@pytest.mark.parametrize("variant", [3, 4])
def test_blocks_exact_specification_and_sampler_support(variant: int) -> None:
    spec = load_specification("blocks_3", blocks_three.Parameters(3)) if variant == 3 else load_specification("blocks_4", blocks_four.Parameters(3))
    generator = cast(GeneratorModule, import_module(f"pypddl_datasets.generators.classical.blocks_{variant}.generator"))
    parameters = blocks_three.Parameters(3) if variant == 3 else blocks_four.Parameters(3)

    def outcome(rng: ChoiceTrace) -> frozenset[tuple[SemanticKey, bool | int]]:
        return _situation(spec, generator.sample(parameters, rng)).identity

    generated = enumerate_integer_choices(outcome)
    permitted = spec.enumerate(limit=169)
    assert permitted.complete
    assert len(permitted.situations) == 169
    assert {situation.identity for situation in permitted.situations} == set(generated)
    assert set(generated.values()) == {Fraction(1, 169)}


@pytest.mark.parametrize("count,expected", [(1, 1), (2, 3), (3, 13), (4, 73)])
def test_block_arrangement_reference_counts(count: int, expected: int) -> None:
    spec = load_specification("blocks_4", blocks_four.Parameters(count))
    projection = [key for key in spec.semantic_variables if key.group == "initial"]
    result = spec.enumerate(limit=expected, projection=projection, groups=("initial",))
    assert result.complete
    assert len(result.situations) == expected


def test_block_cycles_duplicate_support_and_false_clear_are_rejected() -> None:
    spec = load_specification("blocks_4", blocks_four.Parameters(3))
    situation = spec.enumerate(limit=1).situations[0]
    cyclic = situation
    for key, _ in situation.values:
        if key.group == "initial" and key.predicate == "on":
            cyclic = _changed(cyclic, "initial", "on", key.arguments, False)
    for upper, lower in (("b1", "b2"), ("b2", "b3"), ("b3", "b1")):
        cyclic = _changed(cyclic, "initial", "on", (upper, lower), True)
        cyclic = _changed(cyclic, "initial", "on-table", (upper,), False)
        cyclic = _changed(cyclic, "initial", "clear", (upper,), False)
    result = spec.check(cyclic)
    assert not result.is_member
    assert any("acyclic" in violation for violation in result.violations)
    key = next(key for key, value in situation.values if key.predicate == "clear" and key.group == "initial" and value)
    assert not spec.check(_changed(situation, "initial", "clear", key.arguments, False)).is_member
    assert not spec.check(_changed(situation, "initial", "holding", ("b1",), True)).is_member


@pytest.mark.parametrize("cars,locations", [(0, 1), (0, 2), (1, 1), (1, 2), (2, 2)])
def test_ferry_exact_joint_support(cars: int, locations: int) -> None:
    spec = load_specification("ferry", ferry.Parameters(cars, locations))
    generator = ferry_reference
    parameters = ferry.Parameters(cars, locations)
    generated = enumerate_integer_choices(lambda rng: _situation(spec, generator.sample(parameters, CategoricalTrace(rng.prefix))).identity)
    count = locations ** (2 * cars + 1)
    permitted = spec.enumerate(limit=count)
    assert permitted.complete
    assert len(permitted.situations) == count
    assert {situation.identity for situation in permitted.situations} == set(generated)
    assert set(generated.values()) == {Fraction(1, count)}


@pytest.mark.parametrize("balls", [1, 2, 5])
def test_gripper_point_mass(balls: int) -> None:
    spec = load_specification("gripper", gripper.Parameters(balls))
    generator = cast(GeneratorModule, import_module("pypddl_datasets.generators.classical.gripper.generator"))
    problem = generator.sample(gripper.Parameters(balls), random.Random(17))
    permitted = spec.enumerate(limit=1)
    assert permitted.complete
    assert permitted.situations[0].identity == _situation(spec, problem).identity
    assert spec.check_pddl(render_problem(problem)).is_member


def test_absent_goal_atom_is_membership_not_false_world_fact() -> None:
    from pypddl_datasets.generators.classical.driverlog import generator
    parameters = generator.Parameters(2, 1, 1, 1, package_goal_probability=0)
    spec = load_specification("driverlog", parameters)
    problem = generator.sample(parameters, random.Random(0))
    assert not problem.goal
    assert spec.check_pddl(render_problem(problem)).is_member
    changed = _changed(_situation(spec, problem), "goal", "at", ("package1", "s0"), True)
    assert not spec.check(changed).is_member


def test_initial_and_goal_groups_are_readable_and_independent() -> None:
    spec = load_specification("blocks_4", blocks_four.Parameters(2))
    assert all(rule.name.startswith("initial.") and rule.description for rule in spec.initial)
    assert all(rule.name.startswith("goal.") and rule.description for rule in spec.goal)
    assert spec.auxiliary_variables
    with pytest.raises(TypeError):
        spec.object_universe["intruder"] = "object"  # type: ignore[index]


def test_projection_blocks_auxiliary_witnesses_and_unselected_variables() -> None:
    spec = Specification("test")
    atom = spec.atom("initial", "selected")
    witness = spec.witness("arbitrary_rank")
    spec.add("initial", "witness_bounds", z3.And(witness >= 0, witness < 20))
    spec.add("initial", "selected", atom)
    spec.atom("goal", "optional")
    result = spec.enumerate(limit=1, projection=[SemanticKey("initial", "atom", "selected")])
    assert result.complete
    assert len(result.situations) == 1
    assert spec.enumerate(limit=2, projection=[]).complete


def test_enumeration_limit_and_invalid_budgets() -> None:
    spec = load_specification("ferry", ferry.Parameters(1, 2))
    assert spec.enumerate(limit=0).status == "limit"
    assert spec.enumerate(limit=7).status == "limit"
    assert spec.enumerate(limit=8).complete
    with pytest.raises(ValueError):
        spec.enumerate(limit=-1)
    with pytest.raises(ValueError):
        spec.enumerate(timeout_ms=0)
    with pytest.raises(ValueError):
        spec.enumerate(projection=[SemanticKey("initial", "atom", "unknown")])


def test_timeout_and_solver_unknown_are_explicit(monkeypatch: pytest.MonkeyPatch) -> None:
    spec = load_specification("gripper", gripper.Parameters(1))
    times = iter((0.0, 1.0))
    monkeypatch.setattr(core, "monotonic", lambda: next(times))
    assert spec.enumerate(timeout_ms=1).status == "timeout"
    solver = z3.Solver()
    monkeypatch.setattr(solver, "check", lambda: z3.unknown)
    monkeypatch.setattr(solver, "reason_unknown", lambda: "incomplete theory")

    def unknown_solver(groups: Sequence[Group] = ("initial", "goal", "joint")) -> z3.Solver:
        assert groups
        return solver

    monkeypatch.setattr(spec, "solver", unknown_solver)
    assert spec.enumerate().status == "unknown"
    assert spec.check(Situation(())).status == "unknown"


@pytest.mark.parametrize("parameters", [grid.Parameters(2, 2, 1, 1, 1), grid.Parameters(3, 2, 2, 3, 2)])
def test_grid_samples_and_lock_deadlock_counterexample(parameters: grid.Parameters) -> None:
    from pypddl_datasets.generators.classical.grid import generator
    spec = load_specification("grid", parameters)
    problem = generator.sample(parameters, random.Random(0))
    for seed in range(5):
        problem = generator.sample(parameters, random.Random(seed))
        assert spec.check_pddl(render_problem(problem)).is_member
    if parameters.num_keys == 1:
        situation = _situation(spec, problem)
        lock = next(key.arguments[0] for key, value in situation.values if key.predicate == "locked" and value)
        modified = situation
        for key, _ in situation.values:
            if key.group == "initial" and key.predicate == "at":
                modified = _changed(modified, "initial", "at", key.arguments, key.arguments[-1] == lock)
        result = spec.check(modified)
        assert not result.is_member
        assert any("unlockable" in name for name in result.violations)


def test_goldminer_rejects_a_sealed_gold_cell() -> None:
    from pypddl_datasets.generators.classical.goldminer import generator
    parameters = goldminer.Parameters(2, 3)
    spec = load_specification("goldminer", parameters)
    problem = generator.sample(parameters, random.Random(0))
    assert spec.check_pddl(render_problem(problem)).is_member
    situation = _situation(spec, problem)
    for row in range(2):
        situation = _changed(situation, "initial", "soft-rock-at", (f"f{row}-1f",), False)
        situation = _changed(situation, "initial", "hard-rock-at", (f"f{row}-1f",), True)
    result = spec.check(situation)
    assert not result.is_member
    assert any("soft_path" in violation for violation in result.violations)


@pytest.mark.parametrize("parameters", [rovers.Parameters(1, 1, 1, 0, 1), rovers.Parameters(2, 3, 2, 1, 2)])
def test_rovers_variable_cameras_and_full_semantic_membership(parameters: rovers.Parameters) -> None:
    from pypddl_datasets.generators.classical.rovers import generator
    spec = load_specification("rovers", parameters)
    problem = generator.sample(parameters, random.Random(0))
    for seed in range(8):
        problem = generator.sample(parameters, random.Random(seed))
        assert spec.check_pddl(render_problem(problem)).is_member
    situation = _situation(spec, problem)
    assert not spec.check(_changed(situation, "initial", "available", ("rover0",), False)).is_member
    assert not spec.check(_changed(situation, "goal", "communicated_image_data", ("objective0", "impossible-mode"), True)).is_member
    if parameters.num_waypoints > 1:
        for key, _ in situation.values:
            if key.predicate == "can_traverse" and key.arguments[0] == "rover0":
                situation = _changed(situation, "initial", key.predicate, key.arguments, False)
        result = spec.check(situation)
        assert not result.is_member
        assert any("connected_can_traverse" in violation for violation in result.violations)


def test_pddl_rejects_extra_objects_facts_numbers_and_wrong_metric() -> None:
    from pypddl_datasets.generators.classical.barman import generator
    parameters = generator.Parameters(1, 2, 2)
    source = render_problem(generator.sample(parameters, random.Random(0)))
    spec = load_specification("barman", parameters)
    assert spec.check_pddl(source).is_member
    for mutated in (source.replace("(:objects", "(:objects extra - shot", 1),
                    source.replace("(:init", "(:init (contains shot1 ingredient1)", 1),
                    source.replace("(= (total-cost) 0)", "(= (total-cost) 1)"),
                    source.replace("minimize", "maximize")):
        assert not spec.check_pddl(mutated).is_member


def test_interpretation_rejects_coercions_and_conflicting_duplicates() -> None:
    spec = load_specification("gripper", gripper.Parameters(1))
    situation = spec.enumerate(limit=1).situations[0]
    key = situation.values[0][0]
    assert not spec.check(Situation((*situation.values, (key, False)))).is_member
    invalid = dict(situation.values)
    invalid[key] = 2
    assert not spec.check(Situation(tuple(invalid.items()))).is_member
    assert spec.check(Situation((*situation.values, situation.values[0]))).is_member


def test_missing_goal_and_malformed_pddl_are_nonmembers() -> None:
    spec = load_specification("gripper", gripper.Parameters(1))
    assert not spec.check_pddl("(define (problem malformed)").is_member
    assert not spec.check_pddl("(define (problem empty) (:domain gripper-strips) (:objects left right ball1) (:init))").is_member


@pytest.mark.parametrize("domain,parameters,count", [
    ("grid", grid.Parameters(2, 2, 1, 1, 1), 108),
    ("rovers", rovers.Parameters(1, 1, 1, 0, 1), 31),
])
def test_hard_family_tiny_whole_task_support(domain: str, parameters: object, count: int) -> None:
    # The legacy choice tree remains independent of the ProbLog execution order.
    # Complete migrated probability tables are checked in test_problog_distributions.
    generator = cast(GeneratorModule, rovers_reference if domain == "rovers" else
                     import_module(f"pypddl_datasets.generators.classical.{domain}.generator"))
    spec = load_specification(domain, parameters)
    generated = enumerate_integer_choices(lambda rng: _situation(spec, generator.sample(parameters, CategoricalTrace(rng.prefix))).identity)
    permitted = spec.enumerate(limit=count)
    assert permitted.complete
    assert len(permitted.situations) == count
    assert {situation.identity for situation in permitted.situations} == set(generated)


class ParameterModule(Protocol):
    """Typed interface used to check the same semantic contract across domains."""
    def Parameters(self, *args: object, **kwargs: object) -> object: ...  # pylint: disable=invalid-name


MEMBERSHIP_CASES: tuple[tuple[str, tuple[int | float, ...]], ...] = (
    ("barman", (1, 2, 2)), ("blocks_3", (2,)), ("blocks_4", (2,)),
    ("childsnack", (2, 1, 0.5)), ("delivery", (2, 1)), ("driverlog", (3, 1, 1, 1)),
    ("ferry", (0, 1)), ("floortile", (1, 2, 2)), ("goldminer", (2, 3)),
    ("grid", (2, 2, 1, 1, 1)), ("gripper", (1,)), ("hiking", (1, 1, 2)),
    ("hiking_binary", (1, 2, 2)), ("logistics", (1, 2, 1, 1)), ("miconic", (1, 1)),
    ("nomystery", (2, 1, 1.5, 1)), ("rovers", (1, 1, 1, 0, 1)),
    ("satellite", (1, 1, 1, 1, 1)), ("schedule", (1,)), ("spanner", (1, 1, 1)),
    ("tpp", (1, 1, 1, 1, 2)), ("visitall", (1,)), ("woodworking", (1, 1)),
)


@pytest.mark.parametrize("domain,arguments", MEMBERSHIP_CASES)
def test_all_domains_have_independent_executable_membership(domain: str, arguments: tuple[int | float, ...]) -> None:
    module = cast(ParameterModule, import_module(f"pypddl_datasets.generators.classical.{domain}.parameters"))
    generator = cast(GeneratorModule, import_module(f"pypddl_datasets.generators.classical.{domain}.generator"))
    parameters = module.Parameters(*arguments)
    spec = load_specification(domain, parameters)
    for seed in range(3):
        result = spec.check_pddl(render_problem(generator.sample(parameters, random.Random(seed))), timeout_ms=10000)
        assert result.is_member, result


@pytest.mark.parametrize("probability", [0.0, 0.000001, 0.999999, 1.0])
@pytest.mark.parametrize("domain,arguments,field", [
    ("barman", (1, 2, 3), "ingredient_goal_probability"),
    ("driverlog", (2, 1, 1, 1), "package_goal_probability"),
    ("logistics", (1, 2, 2, 1), "goal_package_probability"),
    ("satellite", (1, 1, 2, 1, 1), "pointing_goal_probability"),
    ("visitall", (2,), "goal_ratio"),
])
def test_probability_support_boundaries(domain: str, arguments: tuple[int, ...], field: str, probability: float) -> None:
    module = cast(ParameterModule, import_module(f"pypddl_datasets.generators.classical.{domain}.parameters"))
    generator = cast(GeneratorModule, import_module(f"pypddl_datasets.generators.classical.{domain}.generator"))
    parameters = module.Parameters(*arguments, **{field: probability})
    spec = load_specification(domain, parameters)
    for seed in range(2):
        result = spec.check_pddl(render_problem(generator.sample(parameters, random.Random(seed))))
        assert result.is_member, result


@pytest.mark.parametrize("probability", [0, 1, 99, 100])
def test_integer_probability_support_boundaries(probability: int) -> None:
    from pypddl_datasets.generators.classical.schedule import generator
    parameters = generator.Parameters(1, cylindrical_goal_probability=probability,
                                      initial_colour_probability=probability, goal_colour_probability=probability,
                                      initial_hole_probability=probability, goal_hole_probability=probability,
                                      goal_surface_probability=probability)
    spec = load_specification("schedule", parameters)
    for seed in range(3):
        result = spec.check_pddl(render_problem(generator.sample(parameters, random.Random(seed))))
        assert result.is_member, result
