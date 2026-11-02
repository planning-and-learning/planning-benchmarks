"""Independent tiny laws and support checks for the experimental graph models."""
from __future__ import annotations

from collections.abc import Callable
from fractions import Fraction
from importlib.resources import files
from itertools import combinations
from pathlib import Path
import random
from runpy import run_path
from typing import cast

import pytest
from test_problog_acceleration import sample_distribution

from pypddl_datasets.generators._problog.engine import evaluate_source, sample_source
from pypddl_datasets.generators.probabilistic import model_source

# Experiments are checkout scripts, not an installed Python package.
source = cast(Callable[[str, dict[str, int | float]], str], run_path(str(
    Path(__file__).parents[1] / "experiments/problog/graph_models.py"))["source"])

LIBRARY = files("pypddl_datasets.generators").joinpath("_problog/library.pl").read_text()
SAMPLERS = Path(__file__).parents[1].joinpath("experiments/problog/graph_samplers.pl").read_text(encoding="utf-8")
PARAMETERS: dict[str, int | float] = {
    "num_rovers": 2, "num_waypoints": 3, "num_objectives": 1,
    "num_cameras": 1, "num_goals": 1,
}


def positive(source_text: str) -> dict[str, Fraction]:
    return {key: value for key, value in evaluate_source(source_text).items() if value}


@pytest.mark.parametrize("low,high", [(0, 0), (2, 5), (0, 6)])
def test_graph_integer_is_uniform_without_a_materialized_range(low: int, high: int) -> None:
    query = f"answer(V) :- graph_integer(k,{low},{high},V). query(answer(_))."
    program = LIBRARY + SAMPLERS + query
    expected = {f"answer({i})": Fraction(1, high-low+1) for i in range(low, high+1)}
    assert positive(program) == expected
    assert sample_distribution(program) == expected


@pytest.mark.parametrize("count", [0, 1, 2, 4])
def test_fixed_size_subsets_are_uniform(count: int) -> None:
    query = f"answer(V) :- graph_subset(k,{count},4,[a,b,c,d],V). query(answer(_))."
    values = list(combinations("abcd", count))
    expected = {f"answer([{', '.join(items)}])": Fraction(1, len(values)) for items in values}
    program = LIBRARY + SAMPLERS + query
    assert positive(program) == expected
    assert sample_distribution(program) == expected


def test_growing_tree_is_not_uniform_over_labeled_trees() -> None:
    query = """
    star :- growing_tree(k,[0,1,2,3],T),between(0,3,V),graph_incidence_count(T,[V],3).
    query(star).
    """
    # A growing tree on four randomly ordered labels is a star with probability
    # 1/3. A uniform labeled tree would instead have probability 4/16 = 1/4.
    assert positive(LIBRARY + SAMPLERS + query) == {"star": Fraction(1, 3)}


def test_ipc2023_three_vertex_joint_law_retains_the_shared_backbone() -> None:
    query = """
    joint(T,S,A,B) :- backbone(T),visibility(V),sort(V,S),
        movement(0,X),sort(X,A),movement(1,Y),sort(Y,B).
    query(joint(_,_,_,_)).
    """
    triangle = "[e(0,1), e(0,2), e(1,2)]"
    trees = ("[e(0,1), e(0,2)]", "[e(0,1), e(1,2)]", "[e(0,2), e(1,2)]")
    expected: dict[str, Fraction] = {}
    for tree in trees:
        expected[f"joint({tree},{tree},{tree},{tree})"] = Fraction(1, 6)
        for left, right, mass in ((tree, tree, Fraction(49, 600)),
                                  (tree, triangle, Fraction(7, 200)),
                                  (triangle, tree, Fraction(7, 200)),
                                  (triangle, triangle, Fraction(3, 200))):
            expected[f"joint({tree},{triangle},{left},{right})"] = mass
    program = source("ipc2023", PARAMETERS) + query
    assert positive(program) == expected
    # Exhaust the actual accelerated sampler's random histories as well as
    # checking inference. This also catches stochastic findall/cache mistakes.
    assert sample_distribution(program) == expected


@pytest.mark.parametrize("variant", ["sparse", "ipc2023"])
@pytest.mark.parametrize("count", [1, 2, 8])
def test_graph_models_preserve_connected_support_and_sampling_scope(variant: str, count: int) -> None:
    parameters = {**PARAMETERS, "num_waypoints": count}
    query = r"""
    valid :- graphs(V,Gs),backbone(T),num_waypoints(N),length(T,L),L=:=N-1,
        connected_graph(N,T),connected_graph(N,V),sort(V,Sorted),length(V,Size),length(Sorted,Size),
        \+ (ground_member(e(A,B),V),A>=B),
        \+ (ground_member(r(_,G),Gs),\+ connected_graph(N,G)),
        \+ (ground_member(r(_,G),Gs),ground_member(E,G),\+ ground_member(E,V)),
        \+ (ground_member(r(_,G),Gs),ground_member(E,T),\+ ground_member(E,G)).
    query(valid).
    """
    program = source(variant, parameters) + query
    for seed in range(3):
        assert {str(term): value for term, value in sample_source(program, random.Random(seed)).items()} == {"valid": True}


def test_experiment_retains_the_public_current_source() -> None:
    assert source("current", PARAMETERS) == model_source("rovers", PARAMETERS)
    with pytest.raises(ValueError, match="unknown graph variant"):
        source("grid", PARAMETERS)
