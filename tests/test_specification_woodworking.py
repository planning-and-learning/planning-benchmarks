"""Independent Woodworking support witnesses and semantic counterexamples."""
from __future__ import annotations
from dataclasses import replace
import random

import pytest

from pypddl_datasets.generators.classical.woodworking.generator import sample
from pypddl_datasets.generators.classical.woodworking.parameters import Parameters
from pypddl_datasets.generators.runtime import Assignment, Atom, Metric, Object, Problem, atom, render_problem

from pypddl_datasets.generators import load_specification

pytest.importorskip("z3")
pytest.importorskip("pypddl")


@pytest.mark.parametrize("parts,machines,factor", [(1, 1, 1.0), (3, 1, 1.0), (4, 2, 1.5), (5, 2, 2.0)])
def test_woodworking_specification_accepts_generated_tasks(parts: int, machines: int, factor: float) -> None:
    parameters = Parameters(parts, machines, factor)
    specification = load_specification("woodworking", parameters)
    for seed in range(4):
        task = sample(parameters, random.Random(seed))
        result = specification.check_pddl(render_problem(task), timeout_ms=10_000)
        assert result.is_member, (parts, seed, result)


def _existing_part() -> Problem:
    """A hand-built one-part task, independent of the generation algorithm."""
    kinds = ("highspeed-saw", "glazer", "grinder", "immersion-varnisher", "planer", "saw", "spray-varnisher")
    declarations = (*(Object(f"{kind}0", kind) for kind in kinds),
                    Object("black", "acolour"), Object("white", "acolour"),
                    Object("oak", "awood"), Object("pine", "awood"),
                    Object("p0", "part"), Object("s0", "aboardsize"))
    initial = (
        atom("grind-treatment-change", "varnished", "colourfragments"),
        *(atom("grind-treatment-change", old, "untreated") for old in ("glazed", "untreated", "colourfragments")),
        atom("is-smooth", "smooth"), atom("is-smooth", "verysmooth"),
        Assignment(atom("total-cost"), 0), atom("empty", "highspeed-saw0"),
        *(atom("has-colour", f"{kind}0", "black") for kind in ("glazer", "spray-varnisher", "immersion-varnisher")),
        atom("available", "p0"), atom("treatment", "p0", "varnished"),
        atom("surface-condition", "p0", "rough"), atom("colour", "p0", "white"),
        atom("wood", "p0", "oak"), atom("goalsize", "p0", "small"),
        *(Assignment(atom(function, "p0"), value) for function, value in
          (("spray-varnish-cost", 5), ("glaze-cost", 10), ("grind-cost", 15), ("plane-cost", 10))),
    )
    return Problem("independent", "woodworking", declarations, initial,
                   (atom("available", "p0"), atom("colour", "p0", "black"), atom("wood", "p0", "oak")),
                   Metric(atom("total-cost")))


def test_independent_existing_part_needs_no_boards() -> None:
    specification = load_specification("woodworking", Parameters(1, 1))
    result = specification.check_pddl(render_problem(_existing_part()))
    assert result.is_member, result
    assert specification.auxiliary_variables
    assert all(key.kind in {"atom", "object", "number"} for key in specification.semantic_variables)


@pytest.mark.parametrize("mutation", ["same_initial_color", "wrong_cost", "missing_size", "missing_machine_color", "wrong_metric"])
def test_woodworking_specification_rejects_semantic_mutations(mutation: str) -> None:
    task = _existing_part()
    if mutation == "same_initial_color":
        initial = tuple(atom("colour", "p0", "black") if value == atom("colour", "p0", "white") else value
                        for value in task.initial)
        task = replace(task, initial=initial)
    elif mutation == "wrong_cost":
        initial = tuple(Assignment(value.function, 6)
                        if isinstance(value, Assignment) and value.function.predicate == "spray-varnish-cost"
                        else value for value in task.initial)
        task = replace(task, initial=initial)
    elif mutation == "missing_size":
        task = replace(task, initial=tuple(value for value in task.initial if value != atom("goalsize", "p0", "small")))
    elif mutation == "missing_machine_color":
        task = replace(task, initial=tuple(value for value in task.initial if value != atom("has-colour", "glazer0", "black")))
    else:
        task = replace(task, metric=Metric(atom("total-cost"), "maximize"))
    result = load_specification("woodworking", Parameters(1, 1)).check_pddl(render_problem(task))
    assert result.status == "nonmember", result
    assert result.violations != ("pddl.syntax_or_semantics",), result


def _unused_part() -> Problem:
    task = _existing_part()
    properties = {"available", "treatment", "surface-condition", "colour", "wood"}
    initial = tuple(value for value in task.initial
                    if not (isinstance(value, Atom) and value.predicate in properties and value.arguments[0] == "p0"))
    initial += (atom("unused", "p0"), atom("available", "b0"), atom("wood", "b0", "oak"),
                atom("surface-condition", "b0", "rough"), atom("boardsize", "b0", "s1"),
                atom("boardsize-successor", "s0", "s1"))
    return replace(task, initial=initial, objects=(*task.objects, Object("b0", "board"), Object("s1", "aboardsize")))


def test_independent_resource_packing_and_excess_capacity() -> None:
    task = _unused_part()
    specification = load_specification("woodworking", Parameters(1, 1))
    assert specification.check_pddl(render_problem(task)).is_member
    initial = tuple(atom("boardsize", "b0", "s2") if value == atom("boardsize", "b0", "s1") else value
                    for value in task.initial)
    too_much = replace(task, objects=(*task.objects, Object("s2", "aboardsize")),
                       initial=(*initial, atom("boardsize-successor", "s1", "s2")))
    result = specification.check_pddl(render_problem(too_much))
    assert result.status == "nonmember", result
    assert result.violations != ("pddl.syntax_or_semantics",), result


def test_resource_factor_changes_the_permitted_capacity() -> None:
    task = _unused_part()
    initial = tuple(atom("boardsize", "b0", "s2") if value == atom("boardsize", "b0", "s1") else value
                    for value in task.initial)
    doubled = replace(task, objects=(*task.objects, Object("s2", "aboardsize")),
                      initial=(*initial, atom("boardsize-successor", "s1", "s2")))
    assert load_specification("woodworking", Parameters(1, 1, 2)).check_pddl(render_problem(doubled)).is_member


def _rename(task: Problem, renaming: dict[str, str]) -> Problem:
    def renamed(value: Atom) -> Atom:
        return replace(value, arguments=tuple(renaming.get(argument, argument) for argument in value.arguments))
    initial = tuple(renamed(value) if isinstance(value, Atom) else replace(value, function=renamed(value.function))
                    for value in task.initial)
    return replace(task, initial=initial, goal=tuple(renamed(value) for value in task.goal),
                   objects=tuple(replace(item, name=renaming.get(item.name, item.name)) for item in task.objects))


def _two_wood_groups() -> Problem:
    first = _unused_part()
    second = _rename(first, {"p0": "p1", "b0": "b1", "oak": "pine", "pine": "oak"})
    added = tuple(value for value in second.initial
                  if ((isinstance(value, Atom) and any(arg in {"p1", "b1"} for arg in value.arguments))
                      or (isinstance(value, Assignment) and "p1" in value.function.arguments)))
    return replace(first, objects=(*first.objects, Object("p1", "part"), Object("b1", "board")),
                   initial=(*first.initial, *added), goal=(*first.goal, *second.goal))


def test_board_labels_follow_first_unused_wood_group() -> None:
    task = _two_wood_groups()
    specification = load_specification("woodworking", Parameters(2, 1))
    assert specification.check_pddl(render_problem(task)).is_member
    permuted = _rename(task, {"b0": "b1", "b1": "b0"})
    result = specification.check_pddl(render_problem(permuted))
    assert result.status == "nonmember", result
    assert result.violations != ("pddl.syntax_or_semantics",), result
    # Reordering both the parts and their wood groups satisfies the legacy law.
    reordered = _rename(task, {"p0": "p1", "p1": "p0", "b0": "b1", "b1": "b0"})
    assert specification.check_pddl(render_problem(reordered)).is_member


def _four_large_parts() -> Problem:
    base = _existing_part()
    initial = tuple(value for value in base.initial
                    if ((isinstance(value, Atom) and "p0" not in value.arguments)
                        or (isinstance(value, Assignment) and "p0" not in value.function.arguments)))
    for index in range(4):
        name = f"p{index}"
        initial += (atom("unused", name), atom("goalsize", name, "large"),
                    *(Assignment(atom(function, name), value) for function, value in
                      (("spray-varnish-cost", 15), ("glaze-cost", 20), ("grind-cost", 45), ("plane-cost", 30))))
    for index, size in enumerate((9, 3)):
        initial += (atom("available", f"b{index}"), atom("wood", f"b{index}", "oak"),
                    atom("surface-condition", f"b{index}", "rough"), atom("boardsize", f"b{index}", f"s{size}"))
    initial += tuple(atom("boardsize-successor", f"s{i - 1}", f"s{i}") for i in range(1, 10))
    declarations = (*base.objects, Object("red", "acolour"),
                    *(Object(f"p{i}", "part") for i in range(1, 4)),
                    *(Object(f"b{i}", "board") for i in range(2)),
                    *(Object(f"s{i}", "aboardsize") for i in range(1, 10)))
    goals = tuple(goal for i in range(4) for goal in
                  (atom("available", f"p{i}"), atom("colour", f"p{i}", "black"), atom("wood", f"p{i}", "oak")))
    return replace(base, initial=initial, objects=declarations, goal=goals)


@pytest.mark.parametrize("mutation", ["partial_board_first", "board_prefix_gap", "size_prefix_extra"])
def test_ordered_group_packing_and_object_prefixes(mutation: str) -> None:
    task = _four_large_parts()
    specification = load_specification("woodworking", Parameters(4, 1))
    assert specification.check_pddl(render_problem(task)).is_member
    if mutation == "partial_board_first":
        task = _rename(task, {"b0": "b1", "b1": "b0"})
    elif mutation == "board_prefix_gap":
        task = _rename(task, {"b1": "b2"})
    else:
        task = replace(task, objects=(*task.objects, Object("s10", "aboardsize")))
    result = specification.check_pddl(render_problem(task))
    assert result.status == "nonmember", result
    assert result.violations != ("pddl.syntax_or_semantics",), result
