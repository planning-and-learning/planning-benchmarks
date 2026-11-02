"""Native list traversal must preserve Prolog unification and sampled answers."""
from __future__ import annotations

from importlib.resources import files
import random

import pytest
from problog.logic import Constant, Term, list2term

from pypddl_datasets.generators._problog.engine import evaluate_source, sample_source
from pypddl_datasets.generators._problog.primitives import ground_member
from pypddl_datasets.generators.classical.rovers.parameters import Parameters
from pypddl_datasets.generators.probabilistic import model_source

LIBRARY = files("pypddl_datasets.generators").joinpath("_problog/library.pl").read_text()


@pytest.mark.parametrize("body,expected", [
    ("ground_member(X,[b,a,b,c,a])", "[b, a, c]"),
    ("ground_member(X,[[0],[0],[1]])", "[[0], [1]]"),
    ("ground_member(X,[])", "[]"),
    ("ground_member(f(X,X),[f(a,b),f(a,a),f(b,b),f(a,a)])", "[a, b]"),
    ("X=Y,ground_member(pair(X,Y),[pair(a,b),pair(a,a)])", "[a]"),
    ("ground_member(f(X,X),[f(a,b)])", "[]"),
    ("X=a,ground_member(X,[b,c])", "[]"),
    ("ground_member(X,[a,b,a]),ground_member(X,[a,c,a])", "[a]"),
    ("ground_member(X,[a,b]),\\+ground_member(X,[b,b])", "[a]"),
])
def test_ground_membership_matches_stock_answers(body: str, expected: str) -> None:
    query = f"\nanswer(Xs) :- findall(X,({body}),Xs). query(answer(_))."
    source = LIBRARY + query
    reference = LIBRARY + query.replace("ground_member", "member")
    expected_answers = {f"answer({expected})"}
    for candidate, accelerated in ((reference, True), (source, False), (source, True)):
        world = sample_source(candidate, random.Random(5), accelerated=accelerated)
        assert {str(term) for term, present in world.items() if present} == expected_answers
    # Exact inference retains the canonical Prolog definition, including its
    # treatment of proof multiplicities inside findall.
    assert evaluate_source(source) == evaluate_source(reference)


def test_membership_kernel_retains_occurrences_and_unifies_repeated_variables() -> None:
    values = list2term([Term("pair", Constant(0), Constant(1)),
                        Term("pair", Constant(0), Constant(0)),
                        Term("pair", Constant(0), Constant(0))])
    expected = Term("pair", Constant(0), Constant(0))
    assert ground_member(Term("pair", -1, -1), values) == [(expected, values), (expected, values)]
    assert not ground_member(Term("missing"), values)


def test_extended_membership_uses_interpreted_definition() -> None:
    source = LIBRARY + """
    ground_member(extra,[base]).
    answer(Xs) :- findall(X,ground_member(X,[base]),Xs).
    query(answer(_)).
    """
    native = sample_source(source, random.Random(5))
    reference = sample_source(source, random.Random(5), accelerated=False)
    assert native == reference
    assert {str(term) for term, present in native.items() if present} == {"answer([extra, base])"}


@pytest.mark.parametrize("seed", [8, 9])
def test_rovers_membership_preserves_complete_sampled_world(seed: int) -> None:
    source = model_source("rovers", Parameters(4, 10, 3, 4, 4))
    source += "\nquery(object(_,_)). query(initial(_)). query(goal(_)). query(failure(_))."
    reference = LIBRARY + source[len(LIBRARY):].replace("ground_member", "member")
    assert sample_source(source, random.Random(seed)) == sample_source(reference, random.Random(seed))
