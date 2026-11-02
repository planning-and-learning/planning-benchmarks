"""A reused finite draw must still honor each caller's output constraints."""
from __future__ import annotations

from fractions import Fraction
from importlib.resources import files
import random
from typing import Any

import pytest

from test_problog_acceleration import sample_distribution

from pypddl_datasets.generators._problog import choices
from pypddl_datasets.generators._problog.engine import sample_source

LIBRARY = files("pypddl_datasets.generators").joinpath("_problog/library.pl").read_text()


@pytest.mark.parametrize("selector,arguments", [
    ("uniform_choice", "k,[a,b,c]"),
    ("weighted_choice", "k,[1,2,0],[a,b,c]"),
])
def test_failed_bound_output_does_not_replace_the_cached_draw(selector: str, arguments: str) -> None:
    source = LIBRARY + f"""
        wrong :- {selector}({arguments},missing,_).
        selected(X,R) :- {selector}({arguments},X,R).
        query(wrong). query(selected(_,_)).
    """
    for seed in (2, 5):
        actual = sample_source(source, random.Random(seed))
        reference = sample_source(source, random.Random(seed), accelerated=False)
        assert actual == reference
        assert len([term for term, present in actual.items() if present]) == 1


@pytest.mark.parametrize("selector,arguments,helper", [
    ("uniform_choice", "k,[a,b,c]", "_uniform_selection"),
    ("weighted_choice", "k,[1,2,0],[a,b,c]", "_weighted_selection"),
])
def test_nested_queries_reuse_draw_but_recheck_output_unification(
    selector: str, arguments: str, helper: str, monkeypatch: pytest.MonkeyPatch,
) -> None:
    original = getattr(choices, helper)
    calls = 0

    def count_selection(*args: Any, **kwargs: Any) -> Any:
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(choices, helper, count_selection)
    source = LIBRARY + f"""
        first(L) :- findall(X,{selector}({arguments},X,_),L).
        second(L) :- findall(X,{selector}({arguments},X,_),L).
        mismatch(L) :- findall(X,{selector}({arguments},X,[missing]),L).
        bound(L) :- findall(X,({selector}({arguments},X,R),{selector}({arguments},X,R)),L).
        query(first(_)). query(second(_)). query(mismatch(_)). query(bound(_)).
    """
    actual = sample_source(source, random.Random(2))
    assert calls == 1
    assert actual == sample_source(source, random.Random(2), accelerated=False)
    assert {str(term) for term, present in actual.items() if present and str(term.functor) == "mismatch"} == {"mismatch([])"}
    assert sample_source(source, random.Random(2)) == actual
    assert calls == 2, "the memoized draw must belong to one world"


@pytest.mark.parametrize("call", ["uniform_choice(k,[],_,_)", "weighted_choice(k,[0,0],[a,b],_,_)"])
def test_empty_choice_remains_failure_when_repeated_in_nested_queries(call: str) -> None:
    source = LIBRARY + f"""
        first(L) :- findall(yes,{call},L).
        second(L) :- findall(yes,{call},L).
        query(first(_)). query(second(_)).
    """
    world = sample_source(source, random.Random(2))
    assert {str(term) for term, present in world.items() if present} == {"first([])", "second([])"}
    assert world == sample_source(source, random.Random(2), accelerated=False)


@pytest.mark.parametrize("selector,arguments,first_mass", [
    ("uniform_choice", "k,[a,b]", Fraction(1, 2)),
    ("weighted_choice", "k,[1,2],[a,b]", Fraction(1, 3)),
])
def test_failed_selected_remaining_alias_preserves_full_draw_law(
    selector: str, arguments: str, first_mass: Fraction,
) -> None:
    source = LIBRARY + f"""
        wrong :- {selector}({arguments},X,[X]).
        selected(X,R) :- {selector}({arguments},X,R).
        query(wrong). query(selected(_,_)).
    """
    expected = {"selected(a,[b])": first_mass, "selected(b,[a])": 1 - first_mass}
    assert sample_distribution(source, accelerated=False) == expected
    assert sample_distribution(source) == expected
