"""Independent small-state and boundary checks for migrated classical samplers."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, Hashable, MutableSequence, Sequence
from dataclasses import FrozenInstanceError
from fractions import Fraction
from itertools import permutations, product
import random
from typing import TypeVar

import pytest
from typing_extensions import override

from pypddl_datasets.generators.classical.barman import generator as barman
from pypddl_datasets.generators.classical.blocks_4 import generator as blocks
from pypddl_datasets.generators.classical.blocks_3 import generator as blocks_three
from pypddl_datasets.generators.classical.driverlog import generator as driverlog
from pypddl_datasets.generators.classical.grid import generator as grid
from pypddl_datasets.generators.classical.floortile import generator as floortile
from pypddl_datasets.generators.classical.logistics import generator as logistics
from pypddl_datasets.generators.classical.miconic import generator as miconic
from pypddl_datasets.generators.classical.satellite import generator as satellite
from pypddl_datasets.generators.classical.tpp import generator as tpp
from pypddl_datasets.generators.runtime import Atom, Problem, atom, is_connected

T = TypeVar("T")
Outcome = TypeVar("Outcome", bound=Hashable)


class NextChoice(Exception):
    """Suspend finite exploration at the next abstract uniform integer choice."""

    def __init__(self, values: tuple[int, ...]) -> None:
        super().__init__(values)
        self.values = values


class ChoiceTrace(random.Random):
    """Replay a finite prefix of ideal randrange draws, independently of seeds."""

    def __init__(self, prefix: tuple[int, ...]) -> None:
        super().__init__(0)
        self.prefix = prefix
        self.index = 0

    @override
    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
        values = tuple(range(start) if stop is None else range(start, stop, step))
        if self.index == len(self.prefix):
            raise NextChoice(values)
        result = self.prefix[self.index]
        self.index += 1
        assert result in values
        return result


def enumerate_integer_choices(run: Callable[[ChoiceTrace], Outcome]) -> dict[Outcome, Fraction]:
    """Accumulate leaf mass, weighting each primitive draw rather than each trace."""
    pending: list[tuple[tuple[int, ...], Fraction]] = [((), Fraction(1))]
    outcomes: defaultdict[Outcome, Fraction] = defaultdict(Fraction)
    explored = 0
    while pending:
        prefix, mass = pending.pop()
        explored += 1
        assert explored < 100_000, "finite-case test exceeded its declared exploration budget"
        try:
            outcome = run(ChoiceTrace(prefix))
        except NextChoice as choice:
            pending.extend(((*prefix, value), mass / len(choice.values)) for value in choice.values)
        else:
            outcomes[outcome] += mass
    assert sum(outcomes.values(), Fraction()) == 1
    return dict(outcomes)


def legal_block_arrangements(count: int) -> set[frozenset[Atom]]:
    """Enumerate labeled tower partitions independently using cuts of permutations."""
    arrangements: set[frozenset[Atom]] = set()
    for order in permutations(f"b{i}" for i in range(1, count + 1)):
        for cuts in product((False, True), repeat=count - 1):
            facts = {atom("on-table", order[0]), atom("clear", order[-1])}
            for index, cut in enumerate(cuts):
                if cut:
                    facts.update((atom("clear", order[index]), atom("on-table", order[index + 1])))
                else:
                    facts.add(atom("on", order[index + 1], order[index]))
            arrangements.add(frozenset(facts))
    return arrangements


def test_blocksworld_three_block_exact_joint_support_and_weights() -> None:
    def outcome(rng: ChoiceTrace) -> tuple[frozenset[Atom], frozenset[Atom]]:
        problem = blocks.sample(blocks.Parameters(3), rng)
        initial = frozenset(fact for fact in problem.initial
                            if isinstance(fact, Atom) and fact.predicate != "arm-empty")
        return initial, frozenset(problem.goal)

    reference = legal_block_arrangements(3)
    assert len(reference) == 13
    actual = enumerate_integer_choices(outcome)
    assert set(actual) == set(product(reference, repeat=2))
    assert set(actual.values()) == {Fraction(1, 169)}


def test_grid_uniform_shape_surjections_have_no_fixed_label_anchors() -> None:
    # The independent reference is every tuple containing both shapes.
    reference = {assignment for assignment in product(range(2), repeat=3) if len(set(assignment)) == 2}
    actual = enumerate_integer_choices(lambda rng: tuple(grid.uniform_surjection(3, 2, rng)))
    assert set(actual) == reference
    assert set(actual.values()) == {Fraction(1, 6)}


class EndpointRandom:
    """Select explicit labels while delegating unrelated random operations."""

    def __init__(self, seed: int) -> None:
        self.rng = random.Random(seed)

    def random(self) -> float:
        return self.rng.random()

    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
        return self.rng.randrange(start, stop, step)

    def randint(self, a: int, b: int) -> int:
        return self.rng.randint(a, b)

    def sample(self, population: Sequence[T], k: int) -> list[T]:
        if k == 2:
            return [population[0], population[-1]]
        return self.rng.sample(population, k)

    def choice(self, seq: Sequence[T]) -> T:
        return seq[-1]

    def shuffle(self, x: MutableSequence[T]) -> None:
        x.reverse()


def initial_atoms(problem: Problem, predicate: str) -> set[tuple[str, ...]]:
    return {fact.arguments for fact in problem.initial if isinstance(fact, Atom) and fact.predicate == predicate}


def test_grid_diagonal_locks_complete_reachability_without_rejection() -> None:
    problem = grid.sample(grid.Parameters(2, 2, 1, 1, 2), EndpointRandom(4))
    assert initial_atoms(problem, "locked") == {("pos0-0",), ("pos1-1",)}
    robot = next(iter(initial_atoms(problem, "at-robot")))[0]
    assert initial_atoms(problem, "at") == {("key0", robot)}
    assert len(problem.goal) == 1
    assert problem.goal[0].arguments[1] != robot


def test_barman_goal_shots_are_not_restricted_to_a_label_prefix() -> None:
    parameter = barman.Parameters(1, 2, 3, num_goals=2)
    problem = barman.sample(parameter, EndpointRandom(4))
    assert {fact.arguments[0] for fact in problem.goal} == {"shot1", "shot3"}


def test_satellite_ownership_calibration_and_modes_are_not_indexed() -> None:
    problem = satellite.sample(satellite.Parameters(2, 2, 2, 2, 1), EndpointRandom(4))
    assert initial_atoms(problem, "on_board") == {("instrument0", "satellite1"), ("instrument1", "satellite1")}
    assert initial_atoms(problem, "calibration_target") == {("instrument0", "target1"), ("instrument1", "target1")}
    assert initial_atoms(problem, "supports") == {("instrument0", "image1"), ("instrument1", "image1")}
    assert problem.goal == (atom("have_image", "observation0", "image1"),)


def test_driverlog_graphs_are_symmetric_connected_and_can_omit_old_chain() -> None:
    seen_without_chain = False
    for seed in range(20):
        problem = driverlog.sample(driverlog.Parameters(4, 1, 1, 1), random.Random(seed))
        for predicate in ("link", "path"):
            edges = initial_atoms(problem, predicate)
            assert all((right, left) in edges and left != right for left, right in edges)
            assert is_connected(4, ((int(left[1:]), int(right[1:])) for left, right in edges))
            seen_without_chain |= ("s0", "s1") not in edges
    assert seen_without_chain


def test_boundary_goal_and_supply_conventions() -> None:
    one_floor = miconic.sample(miconic.Parameters(1, 1), random.Random(1))
    assert initial_atoms(one_floor, "origin") == {("p0", "f0")}
    assert initial_atoms(one_floor, "destin") == {("p0", "f0")}
    assert one_floor.goal == (atom("served", "p0"),)
    empty_goal = logistics.sample(logistics.Parameters(1, 2, 2, 1, 0), random.Random(1))
    assert not empty_goal.goal
    scarce = tpp.sample(tpp.Parameters(1, 1, 1, 1, 2), random.Random(1))
    assert initial_atoms(scarce, "on-sale") == {("goods0", "market0", "level1")}
    assert scarce.goal == (atom("stored", "goods0", "level2"),)


def test_parameters_are_frozen_and_validate_before_sampling() -> None:
    parameters = grid.Parameters(2, 2, 1, 1, 2)
    with pytest.raises(FrozenInstanceError):
        setattr(parameters, "width", 0)
    with pytest.raises(ValueError, match="at least one position"):
        grid.Parameters(2, 2, 1, 1, 4)
    with pytest.raises(ValueError, match="finite"):
        logistics.Parameters(1, 2, 1, 1, float("nan"))
    assert grid.make_problem(1, 2) is None


def test_floortile_and_logistics_roles_are_not_anchored_to_labels() -> None:
    floor = floortile.sample(floortile.Parameters(1, 2, 2), EndpointRandom(3))
    assert initial_atoms(floor, "robot-has") == {("robot1", "black"), ("robot2", "white")}
    transport = logistics.sample(logistics.Parameters(2, 2, 1, 1), EndpointRandom(3))
    assert initial_atoms(transport, "AIRPORT") == {("l0-1",), ("l1-1",)}
    positions = dict((fact[0], fact[1]) for fact in initial_atoms(transport, "at"))
    assert positions["t0"].startswith("l1-")
    assert positions["t1"].startswith("l0-")
    assert positions["a0"] == "l1-1"


def test_driverlog_edge_probability_boundary_is_explicit() -> None:
    problem = driverlog.sample(driverlog.Parameters(3, 1, 1, 1, edge_probability=1), random.Random(0))
    expected = {(f"s{left}", f"s{right}") for left in range(3) for right in range(3) if left != right}
    assert initial_atoms(problem, "link") == expected
    assert initial_atoms(problem, "path") == expected
    with pytest.raises(ValueError, match="positive"):
        driverlog.Parameters(3, 1, 1, 1, edge_probability=0)


def test_blocksworld_encodings_keep_their_distinct_vocabularies(capsys: pytest.CaptureFixture[str]) -> None:
    problem = blocks_three.sample(blocks_three.Parameters(2), random.Random(5))
    assert problem.domain == "blocksworld-3ops"
    assert not initial_atoms(problem, "arm-empty")
    assert blocks_three.main(["-b", "2", "-s", "5"]) == 0
    assert capsys.readouterr().out == blocks_three.make_problem(2, 5)
    assert blocks.main(["-b", "2", "-s", "5"]) == 0
    assert capsys.readouterr().out == blocks.make_problem(2, 5)
