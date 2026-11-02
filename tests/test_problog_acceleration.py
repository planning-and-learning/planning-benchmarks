"""Joint laws for accelerated probabilistic primitives, independent of their code.

Overlapping calls can share individual Bernoulli heads without sharing a whole
categorical draw. These cases detect changes hidden by correct single-call marginals.
"""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from fractions import Fraction
from importlib.resources import files
from pathlib import Path
import random

import pytest
from problog.logic import Constant, Term
from typing_extensions import override

from reference_generators.tracing import NextChoice, TaskKey, Trace
from pypddl_datasets.generators._problog.engine import evaluate_source, sample_source
from pypddl_datasets.generators.runtime import Atom

REFERENCE = Path(__file__).with_name("reference_generators").joinpath("choices.pl").read_text(encoding="utf-8")


@dataclass(frozen=True)
class ChoiceCase:
    name: str
    body: str
    expected: dict[str, Fraction]


def _joint(weights: dict[tuple[str, str], Fraction]) -> dict[str, Fraction]:
    return {f"pair({left},{right})": mass for (left, right), mass in weights.items()}


CASES = (
    ChoiceCase("repeated_id", "uniform_choice(k,[a,b,c],X,_),uniform_choice(k,[a,b,c],Y,_)",
               _joint({(value, value): Fraction(1, 3) for value in "abc"})),
    ChoiceCase("independent_ids", "uniform_choice(k,[a,b],X,_),uniform_choice(other,[a,b],Y,_)",
               _joint({(left, right): Fraction(1, 4) for left in "ab" for right in "ab"})),
    ChoiceCase("shared_suffix", "uniform_choice(k,[a,b,c],X,_),uniform_choice(k,[b,c],Y,_)",
               _joint({("a", "b"): Fraction(1, 6), ("a", "c"): Fraction(1, 6),
                       ("b", "b"): Fraction(1, 3), ("c", "c"): Fraction(1, 3)})),
    ChoiceCase("shared_suffix_reverse", "uniform_choice(k,[b,c],Y,_),uniform_choice(k,[a,b,c],X,_)",
               _joint({("a", "b"): Fraction(1, 6), ("a", "c"): Fraction(1, 6),
                       ("b", "b"): Fraction(1, 3), ("c", "c"): Fraction(1, 3)})),
    ChoiceCase("permuted_lists", "uniform_choice(k,[a,b,c],X,_),uniform_choice(k,[b,a,c],Y,_)",
               _joint({(left, right): Fraction(1, 9) for left in "abc" for right in "abc"})),
    ChoiceCase("duplicate_values", "uniform_choice(k,[a,a,b],X,_),uniform_choice(k,[a,b],Y,_)",
               _joint({("a", "a"): Fraction(1, 2), ("a", "b"): Fraction(1, 6),
                       ("b", "b"): Fraction(1, 3)})),
    ChoiceCase("bound_outputs", "(uniform_choice(k,[a,b,c],b,[a,c]),X=yes;\\+uniform_choice(k,[a,b,c],b,[a,c]),X=no),uniform_choice(k,[a,b,c],Y,_)",
               _joint({("yes", "b"): Fraction(1, 3), ("no", "a"): Fraction(1, 3),
                       ("no", "c"): Fraction(1, 3)})),
    ChoiceCase("nested_values", "uniform_choice(k,[[a],[b]],X,_),uniform_choice(k,[[b]],Y,_)",
               _joint({("[a]", "[b]"): Fraction(1, 2), ("[b]", "[b]"): Fraction(1, 2)})),
    ChoiceCase("remaining_order", "uniform_choice(k,[a,b,a],X,Y)",
               _joint({("a", "[b, a]"): Fraction(1, 3), ("b", "[a, a]"): Fraction(1, 3),
                       ("a", "[a, b]"): Fraction(1, 3)})),
    ChoiceCase("direct_head", "uniform_choice(k,[a,b,c],X,_),(uniform_head(k,2,b,[c]),Y=yes;\\+uniform_head(k,2,b,[c]),Y=no)",
               _joint({("a", "yes"): Fraction(1, 6), ("a", "no"): Fraction(1, 6),
                       ("b", "yes"): Fraction(1, 3), ("c", "no"): Fraction(1, 3)})),
    ChoiceCase("floating_weights", "weighted_choice(k,[0.5,1.5],[a,b],X,_),weighted_choice(k,[0.5,1.5],[a,b],Y,_)",
               _joint({("a", "a"): Fraction(1, 4), ("b", "b"): Fraction(3, 4)})),
    ChoiceCase("weighted_shared_suffix", "weighted_choice(k,[1,2,3],[a,b,c],X,_),weighted_choice(k,[2,3],[b,c],Y,_)",
               _joint({("a", "b"): Fraction(1, 15), ("a", "c"): Fraction(1, 10),
                       ("b", "b"): Fraction(1, 3), ("c", "c"): Fraction(1, 2)})),
    ChoiceCase("weighted_shared_head", "weighted_choice(k,[1,1,2],[a,b,c],X,_),weighted_choice(k,[1,2,1],[a,b,c],Y,_)",
               _joint({("a", "a"): Fraction(1, 4), ("b", "b"): Fraction(1, 6),
                       ("b", "c"): Fraction(1, 12), ("c", "b"): Fraction(1, 3),
                       ("c", "c"): Fraction(1, 6)})),
    ChoiceCase("weighted_unreduced_identity", "weighted_choice(k,[1,1],[a,b],X,_),weighted_choice(k,[2,2],[a,b],Y,_)",
               _joint({(left, right): Fraction(1, 4) for left in "ab" for right in "ab"})),
    ChoiceCase("separate_selector_namespaces", "uniform_choice(k,[a,b],X,_),weighted_choice(k,[1,1],[a,b],Y,_)",
               _joint({(left, right): Fraction(1, 4) for left in "ab" for right in "ab"})),
)


def _interpreted(source: str) -> str:
    """Rename only selector predicates so native dispatch cannot intercept them."""
    return source.replace("uniform_choice", "logical_uniform_choice").replace(
        "weighted_choice", "logical_weighted_choice")


def sample_distribution(source: str, *, accelerated: bool = True, coins: bool = False) -> dict[str, Fraction]:
    pending: list[tuple[tuple[int, ...], Fraction]] = [((), Fraction(1))]
    weights: defaultdict[str, Fraction] = defaultdict(Fraction)
    visited = 0
    while pending:
        prefix, mass = pending.pop()
        visited += 1
        assert visited < 10_000, "primitive reference exceeded its finite trace budget"
        try:
            rng = CoinTrace(prefix) if coins else Trace(prefix)
            result = sample_source(source, rng, accelerated=accelerated)
        except NextChoice as choice:
            pending.extend(((*prefix, index), mass / choice.count) for index in range(choice.count))
        else:
            selected = [str(term) for term, present in result.items() if present]
            assert len(selected) == 1, selected
            weights[selected[0]] += mass
    assert sum(weights.values(), Fraction()) == 1
    return dict(weights)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.name)
def test_accelerated_selectors_preserve_full_joint_laws(case: ChoiceCase) -> None:
    query = f"\npair(X,Y) :- {case.body}.\nquery(pair(_,_))."
    interpreted = _interpreted(REFERENCE + query)
    exact = evaluate_source(interpreted)
    assert {key: value for key, value in exact.items() if value} == case.expected
    assert sample_distribution(REFERENCE + query, accelerated=False) == case.expected
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    assert sample_distribution(library + query) == case.expected


def _term_list(values: Sequence[Term]) -> Term:
    result = Term("[]")
    for value in reversed(values):
        result = Term(".", value, result)
    return result


@pytest.mark.parametrize("count,edges,expected", [
    (1, (), True), (2, (), False), (3, ((0, 1), (1, 2)), True),
    (3, ((0, 1), (1, 0)), False),
    (2, ((0, 0), (0, 1), (0, 1)), True),
])
def test_native_connectivity_preserves_undirected_graph_semantics(
    count: int, edges: tuple[tuple[int, int], ...], expected: bool,
) -> None:
    from pypddl_datasets.generators._problog.primitives import connected_graph
    graph = _term_list([Term("e", Constant(left), Constant(right)) for left, right in edges])
    assert bool(connected_graph(Constant(count), graph)) is expected


@pytest.mark.parametrize("edges,vertices,expected", [
    ("[e(a,b)]", "[a,b]", 2),
    ("[e(a,b)]", "[a,a,b,b]", 2),
    ("[e(a,a)]", "[a]", 2),
    ("[e(a,b),e(a,b)]", "[a,b]", 4),
    ("[e(a,b),e(b,c)]", "[a,c]", 2),
    ("[]", "[a]", 0),
])
def test_incidence_kernel_counts_endpoint_occurrences(
    edges: str, vertices: str, expected: int,
) -> None:
    # Once wired into the common library, this checks native and interpreted
    # sampling against the same arithmetic contract, including duplicate edges.
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    source = library + f"\ncount(C) :- graph_incidence_count({edges},{vertices},C). query(count(_))."
    assert evaluate_source(source) == {f"count({expected})": Fraction(1)}
    assert sample_distribution(source) == {f"count({expected})": Fraction(1)}
    assert sample_distribution(source, accelerated=False) == {f"count({expected})": Fraction(1)}


def test_native_choices_keep_nested_world_and_concurrent_rng_isolation() -> None:
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    source = library + """
        first(X) :- uniform_choice(k,[a,b,c],X,_).
        second(Y) :- uniform_choice(k,[b,c],Y,_).
        nested(L) :- findall(pair(X,Y),(first(X),second(Y)),L).
        query(first(_)). query(second(_)). query(nested(_)).
    """
    def sampled(seed: int, accelerated: bool = True) -> dict[str, bool]:
        return {str(term): value for term, value in sample_source(
            source, random.Random(seed), accelerated=accelerated).items()}

    before = random.getstate()
    expected = [sampled(seed, False) for seed in range(16)]
    assert [sampled(seed) for seed in range(16)] == expected
    with ThreadPoolExecutor(max_workers=4) as pool:
        assert list(pool.map(sampled, range(16))) == expected
    assert random.getstate() == before


@pytest.mark.parametrize("predicate", ["uniform_choice", "'uniform_choice'"])
def test_selector_extension_falls_back_without_losing_user_clauses(predicate: str) -> None:
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    source = library + f"""
        {predicate}(extension,[base],extra,[]).
        selected(X) :- uniform_choice(extension,[base],X,_).
        query(selected(_)).
    """
    expected = {"selected(base)": True, "selected(extra)": True}
    assert evaluate_source(source) == {term: Fraction(1) for term in expected}
    for accelerated in (False, True):
        sampled = sample_source(source, random.Random(0), accelerated=accelerated)
        assert {str(term): present for term, present in sampled.items()} == expected


class NextUniformHead(Exception):
    def __init__(self, probability: Fraction) -> None:
        super().__init__(probability)
        self.probability = probability


class UniformHeads(random.Random):
    """Collapse equivalent integers in an actual uniform-head randrange(N)<1 draw.

    These bounded cases have no weighted selectors or nontrivial graph draws.
    Primitive tests above separately check integer-level native choice behavior.
    """
    def __init__(self, prefix: tuple[bool, ...]) -> None:
        super().__init__(0)
        self.prefix = prefix
        self.index = 0

    @override
    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
        assert stop is None and step == 1 and start >= 2
        if self.index == len(self.prefix):
            raise NextUniformHead(Fraction(1, start))
        present = self.prefix[self.index]
        self.index += 1
        return 0 if present else 1

    @override
    def random(self) -> float:
        raise AssertionError("tiny uniform-only case unexpectedly requested a float draw")


@pytest.mark.parametrize("case_index", range(9))
def test_native_complete_tiny_task_laws_against_frozen_samplers(case_index: int) -> None:
    from test_problog_distributions import cases
    from reference_generators.tracing import distribution, signature
    from pypddl_datasets.generators.probabilistic import sample_model

    case = cases()[case_index]
    expected, _ = distribution(case.sample)
    pending: list[tuple[tuple[bool, ...], Fraction]] = [((), Fraction(1))]
    actual: defaultdict[TaskKey, Fraction] = defaultdict(Fraction)
    explored = 0
    while pending:
        prefix, mass = pending.pop()
        explored += 1
        assert explored < 10_000
        try:
            problem = sample_model(case.domain, case.parameters, UniformHeads(prefix))
        except NextUniformHead as choice:
            pending.extend(((*prefix, outcome), mass * probability)
                           for outcome, probability in ((True, choice.probability),
                                                        (False, 1 - choice.probability)))
        else:
            actual[signature(problem)] += mass
    assert dict(actual) == expected
    assert sum(actual.values(), Fraction()) == 1


def _initial_atoms(world: dict[Term, bool]) -> set[Atom]:
    return {Atom(str(term.args[0].functor), tuple(str(value) for value in term.args[0].args))
            for term, present in world.items() if present and str(term.functor) == "initial"}


def _legacy_image_tickets(facts: set[Atom]) -> dict[tuple[str, str], int]:
    carriers = {fact.arguments[1] for fact in facts if fact.predicate == "on_board"}
    visible = {fact.arguments for fact in facts if fact.predicate == "visible_from"}
    traversals = {fact.arguments for fact in facts if fact.predicate == "can_traverse"}
    result: defaultdict[tuple[str, str], int] = defaultdict(int)
    for rover in carriers:
        for objective, waypoint in visible:
            for carrier, left, right in traversals:
                if carrier == rover and waypoint in (left, right):
                    result[(objective, rover)] += 1
    return dict(result)


@pytest.mark.parametrize("accelerated", [False, True])
def test_sampled_rovers_image_tickets_match_the_same_worlds_initial_facts(accelerated: bool) -> None:
    from problog.logic import term2list
    from pypddl_datasets.generators.classical.rovers.parameters import Parameters
    from pypddl_datasets.generators.probabilistic import model_source

    source = model_source("rovers", Parameters(2, 3, 2, 2, 1, edge_probability=1)) + """
        tickets(W,P,T) :- graphs(_,Graphs),image_distribution(Graphs,W,P,T).
        query(initial(_)). query(tickets(_,_,_)).
    """
    observed_weights: set[int] = set()
    for seed in range(6):
        world = sample_source(source, random.Random(seed), accelerated=accelerated)
        expected = _legacy_image_tickets(_initial_atoms(world))
        tickets = next(term for term, present in world.items() if present and str(term.functor) == "tickets")
        weights = term2list(tickets.args[0], deep=False)
        pairs = term2list(tickets.args[1], deep=False)
        actual = {(f"objective{pair.args[0]}", f"rover{pair.args[1]}"): weight.value
                  for pair, weight in zip(pairs, weights)}
        assert len(pairs) == len(actual), "duplicate pairs would reweight image targets"
        assert actual == expected
        assert tickets.args[2].value == sum(expected.values())
        observed_weights.update(expected.values())
    assert len(observed_weights) > 1, "the scenarios must exercise unequal multiplicities"


class CoinTrace(Trace):
    """Exhaustive ideal Bernoulli(1/2) draws for the graph/subset cases below."""
    @override
    def random(self) -> float:
        if self.index == len(self.prefix):
            raise NextChoice(2)
        value = self.prefix[self.index]
        self.index += 1
        return 0.25 if value == 0 else 0.75

    @override
    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
        raise AssertionError("a float Bernoulli must not become a discrete RNG call")


def test_bernoulli_subset_duplicate_items_share_the_same_coin() -> None:
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    source = library + "\nselected(L) :- bernoulli_subset(k,0.5,[a,a,b],L). query(selected(_))."
    expected = {f"selected({values})": Fraction(1, 4) for values in ("[]", "[b]", "[a, a]", "[a, a, b]")}
    assert {key: value for key, value in evaluate_source(source).items() if value} == expected
    assert sample_distribution(source, coins=True, accelerated=False) == expected
    assert sample_distribution(source, coins=True) == expected


def test_bernoulli_subset_overlapping_lists_share_only_common_coins() -> None:
    from itertools import product
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    source = library + """
        pair(X,Y) :- bernoulli_subset(k,0.5,[a,b],X),bernoulli_subset(k,0.5,[b,c],Y).
        query(pair(_,_)).
    """
    expected: dict[str, Fraction] = {}
    for first, shared, last in product((False, True), repeat=3):
        left = "[" + ", ".join(value for value, present in (("a", first), ("b", shared)) if present) + "]"
        right = "[" + ", ".join(value for value, present in (("b", shared), ("c", last)) if present) + "]"
        expected[f"pair({left},{right})"] = Fraction(1, 8)
    assert {key: value for key, value in evaluate_source(source).items() if value} == expected
    assert sample_distribution(source, coins=True, accelerated=False) == expected
    assert sample_distribution(source, coins=True) == expected


@pytest.mark.parametrize("at_threshold", [False, True])
def test_native_bernoulli_subset_keeps_rare_binary64_threshold(at_threshold: bool) -> None:
    import math
    probability = 5e-9
    draw = probability if at_threshold else math.nextafter(probability, 0.0)
    class BoundaryDraw(CoinTrace):
        @override
        def random(self) -> float:
            return draw
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    source = library + f"\nselected(L) :- bernoulli_subset(k,{probability},[a,a],L). query(selected(_))."
    expected = "selected([])" if at_threshold else "selected([a, a])"
    for accelerated in (False, True):
        assert {str(term): value for term, value in sample_source(
            source, BoundaryDraw(()), accelerated=accelerated).items() if value} == {expected: True}


@pytest.mark.parametrize("probability,expected", [(0, "[]"), (1, "[a, a, b]")])
def test_bernoulli_subset_endpoints_need_no_randomness(probability: int, expected: str) -> None:
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    source = library + f"\nselected(L) :- bernoulli_subset(k,{probability},[a,a,b],L). query(selected(_))."
    for accelerated in (False, True):
        world = sample_source(source, CoinTrace(()), accelerated=accelerated)
        assert {str(term): present for term, present in world.items() if present} == {
            f"selected({expected})": True}


def test_bernoulli_subset_and_direct_predicates_share_the_same_coin() -> None:
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    source = library + """
        state(L,yes) :- bernoulli_subset(k,0.5,[a,a],L),bernoulli_member(k,0.5,a),bernoulli_draw(k,0.5,a).
        state(L,no) :- bernoulli_subset(k,0.5,[a,a],L),\\+bernoulli_member(k,0.5,a),\\+bernoulli_draw(k,0.5,a).
        query(state(_,_)).
    """
    expected = {"state([a, a],yes)": Fraction(1, 2), "state([],no)": Fraction(1, 2)}
    assert {key: value for key, value in evaluate_source(source).items() if value} == expected
    for accelerated in (False, True):
        assert sample_distribution(source, accelerated=accelerated, coins=True) == expected


def _reference_graph_law(budget: int) -> dict[str, Fraction]:
    from reference_generators.graphs import connected_edges
    from pypddl_datasets.generators.runtime import GenerationExhausted

    def prolog_graph(edges: set[tuple[int, int]]) -> str:
        return "[" + ", ".join(f"e({left},{right})" for left, right in sorted(edges)) + "]"

    pending: list[tuple[tuple[int, ...], Fraction]] = [((), Fraction(1))]
    weights: defaultdict[str, Fraction] = defaultdict(Fraction)
    while pending:
        prefix, mass = pending.pop()
        rng = CoinTrace(prefix)
        try:
            visibility = connected_edges(3, rng, max_attempts=budget)
            movement = connected_edges(3, rng, allowed_edges=visibility, max_attempts=budget)
        except NextChoice:
            pending.extend(((*prefix, value), mass / 2) for value in (0, 1))
        except GenerationExhausted:
            weights["failed"] += mass
        else:
            weights[f"state({prolog_graph(visibility)},{prolog_graph(movement)})"] += mass
    assert len(weights) == 8
    assert sum(weights.values(), Fraction()) == 1
    return dict(weights)


@pytest.mark.parametrize("budget", [1, 2])
def test_native_graph_sampling_complete_joint_law_matches_frozen_rejection(budget: int) -> None:
    from dataclasses import asdict
    from pypddl_datasets.generators.classical.rovers.parameters import Parameters
    from pypddl_datasets.generators.probabilistic import model_source

    parameters = {**asdict(Parameters(1, 3, 1, 0, 1)), "graph_budget": budget}
    source = model_source("rovers", parameters) + """
        state(V,M) :- graphs(V,[r(0,M)]).
        failed :- failure(graph_exhausted).
        query(state(_,_)). query(failed).
    """
    expected = _reference_graph_law(budget)
    assert {key: value for key, value in evaluate_source(source).items() if value} == expected
    assert sample_distribution(source, coins=True) == expected
