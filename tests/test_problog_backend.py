"""Regressions for the generic ProbLog adapter, independent of domain rules."""
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from importlib.resources import files
import random

import pytest
from problog.logic import Constant, Term
from typing_extensions import override

from pypddl_datasets.generators._problog.engine import evaluate_source, sample_source
from pypddl_datasets.generators._problog.numbers import rational, unrounded_constant
from pypddl_datasets.generators._problog.output import decode_world
from pypddl_datasets.generators.probabilistic import model_source, sample_model
from pypddl_datasets.generators.runtime import GenerationExhausted


class LastDraw(random.Random):
    """Choose the last discrete outcome; do not approximate a rare event."""
    @override
    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
        values = range(start) if stop is None else range(start, stop, step)
        return values[-1]

    @override
    def random(self) -> float:
        return 0.9999999999


@pytest.mark.parametrize("probabilities", [
    "0.999999995::common; 0.000000005::rare.",
    "(199999999/200000000)::common; (1/200000000)::rare.",
])
def test_rare_annotated_disjunction_keeps_exhaustive_support(probabilities: str) -> None:
    source = probabilities + " query(common). query(rare)."
    result = sample_source(source, LastDraw())
    assert {str(term): value for term, value in result.items()} == {"common": False, "rare": True}
    assert evaluate_source(source) == {"common": Fraction(199999999, 200000000),
                                       "rare": Fraction(1, 200000000)}


def test_reference_inference_has_no_epsilon_or_underflow_cutoff() -> None:
    result = evaluate_source("1e-16::a. 1e-16::b. both :- a,b. query(a). query(both).")
    assert result == {"a": Fraction(1, 10**16), "both": Fraction(1, 10**32)}
    assert rational(Term("/", Constant(1), Constant(7))) == Fraction(1, 7)


def test_numeric_factory_preserves_binary64_and_builtin_term_identity() -> None:
    precision = Constant.FLOAT_PRECISION
    result = evaluate_source("""
        below(V) :- X is 1.9999999999999998, V is truncate(X).
        negative(V) :- X is -1.9999999999999998, V is truncate(X).
        difference(V) :- V is 0.3-0.2.
        0.5::edge(X) :- between(0,1,X).
        a :- edge(0).
        b :- between(0,0,X), edge(X).
        joint :- a,b.
        query(below(_)). query(negative(_)). query(difference(_)). query(joint).
    """)
    assert result == {"below(1)": Fraction(1), "negative(-1)": Fraction(1),
                      "difference(0.09999999999999998)": Fraction(1), "joint": Fraction(1, 2)}
    assert type(unrounded_constant(1)) is Constant  # pylint: disable=unidiomatic-typecheck
    assert Term("edge", unrounded_constant(1)) == Term("edge", Constant(1))
    assert Constant.FLOAT_PRECISION == precision
    assert Constant(1.9999999999999998).value == 2.0


def test_float_bernoulli_uses_existing_binary64_threshold() -> None:
    # At the exact boundary the legacy comparison is strict, with no rounding.
    class BoundaryDraw(random.Random):
        @override
        def random(self) -> float:
            return 0.9999999999999999
    sampled = sample_source("0.9999999999999999::a. query(a).", BoundaryDraw())
    assert not sampled[Term("a")]


def test_float_bernoulli_rule_keeps_threshold_when_problog_compiles_it_as_a_group() -> None:
    class BoundaryDraw(random.Random):
        @override
        def random(self) -> float:
            return 0.9999999999999999

        @override
        def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
            raise AssertionError("a float Bernoulli must use random(), including a non-ground rule")
    source = "p(0.9999999999999999). P::a(X) :- p(P), between(0,0,X). query(a(0))."
    assert sample_source(source, BoundaryDraw()) == {Term("a", Constant(0)): False}


def test_nested_findall_reuses_the_same_world_choices() -> None:
    source = """
        0.5::a.
        inner(L) :- findall(x,a,L).
        outer(L) :- findall(X,inner(X),L).
        query(a). query(inner(_)). query(outer(_)).
    """
    for seed in range(12):
        result = {str(term): present for term, present in sample_source(source, random.Random(seed)).items()}
        expected = "[x]" if result["a"] else "[]"
        assert result[f"inner({expected})"]
        assert result[f"outer([{expected}])"]


def test_rng_isolation_across_calls_threads_and_global_state() -> None:
    source = "0.5::a. 0.75::b. query(a). query(b)."
    def sample(seed: int) -> dict[Term, bool]:
        return sample_source(source, random.Random(seed))
    before = random.getstate()
    expected = [sample(seed) for seed in range(16)]
    with ThreadPoolExecutor(max_workers=4) as pool:
        assert list(pool.map(sample, range(16))) == expected
    assert random.getstate() == before


def test_threaded_models_keep_external_library_registration_local() -> None:
    parameters = {"num_rovers": 1, "num_waypoints": 2, "num_objectives": 1,
                  "num_cameras": 0, "num_goals": 1, "edge_probability": 1}
    def sample(seed: int) -> str:
        return repr(sample_model("rovers", parameters, random.Random(seed)))
    expected = [sample(seed) for seed in range(8)]
    with ThreadPoolExecutor(max_workers=4) as pool:
        assert list(pool.map(sample, range(8))) == expected


def test_uniform_and_weighted_choices_are_exact_including_zero_weights() -> None:
    library = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    result = evaluate_source(library + """
        u(X) :- uniform_choice(u,[a,b,c,d,e,f,g],X,_).
        w(X) :- weighted_choice(w,[0,2,1,0],[a,b,c,d],X,_).
        query(u(_)). query(w(_)).
    """)
    assert {key: value for key, value in result.items() if key.startswith("u(")} == {
        f"u({letter})": Fraction(1, 7) for letter in "abcdefg"}
    assert {key: value for key, value in result.items() if key.startswith("w(") and value} == {
        "w(b)": Fraction(2, 3), "w(c)": Fraction(1, 3)}


def test_failure_and_invalid_input_are_explicit() -> None:
    with pytest.raises(GenerationExhausted, match="graph_exhausted"):
        decode_world({Term("failure", Term("graph_exhausted")): True})
    with pytest.raises(ValueError, match="global evidence"):
        sample_source("0.5::a. evidence(a). query(a).", random.Random(0))
    with pytest.raises(ValueError, match="outside"):
        sample_source("1.1::a. query(a).", random.Random(0))
    for invalid in ({"bad-name": 1}, {"n": float("nan")}, {"n": True}, {"n": "1"}):
        with pytest.raises(ValueError):
            model_source("ferry", invalid)
    assert "edge_probability(0.5)." in model_source("rovers", {"num_rovers": 1, "num_waypoints": 1, "num_objectives": 1, "num_cameras": 0, "num_goals": 1})
    with pytest.raises(ValueError):
        model_source("ferry", {"num_cars": 0, "num_locations": 0})
    # A failed call cannot leak its per-world cache into the next call.
    assert sample_source("1::a. query(a).", random.Random(0)) == {Term("a"): True}



def test_propagated_evidence_preserves_conditional_probability_normalization() -> None:
    source = "(1/3)::a. (1/4)::b. joint :- a,b."
    joint = evaluate_source(source + " query(joint). query(a).")
    conditioned = evaluate_source(source + " evidence(a). query(joint). query(a). query(b).")
    assert joint == {"joint": Fraction(1, 12), "a": Fraction(1, 3)}
    assert conditioned == {"joint": Fraction(1, 4), "a": Fraction(1), "b": Fraction(1, 4)}
    assert conditioned["joint"] * joint["a"] == joint["joint"]


def test_nested_conditioning_retains_annotated_disjunction_normalization() -> None:
    result = evaluate_source("""
        0.2::a; 0.3::b; 0.5::c.
        evidence(a,false).
        selected(a) :- a. selected(b) :- b. selected(c) :- c.
        values(L) :- findall(X,selected(X),L).
        query(a). query(b). query(c). query(values(_)).
    """)
    assert {query: weight for query, weight in result.items() if weight} == {
        "b": Fraction(3, 8), "c": Fraction(5, 8),
        "values([b])": Fraction(3, 8), "values([c])": Fraction(5, 8)}
    # No evidence choices escape into later independent evaluations.
    assert evaluate_source("0.2::a. query(a).") == {"a": Fraction(1, 5)}
