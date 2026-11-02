"""Reproduce ProbLog 2.3.0 semantics relevant to a generator migration.

Run in the isolated feasibility environment. These checks deliberately document
upstream numerical limitations; they do not modify the production generators.
"""

from __future__ import annotations

import json
from importlib.metadata import version
from math import isclose
from unittest.mock import patch

from problog import get_evaluatable
from problog.evaluator import SemiringProbability
from problog.logic import Constant
from problog.program import PrologString
from problog.tasks.sample import sample


def infer(source: str, *, normal_probability: bool = False) -> dict[str, float]:
    """Evaluate a small model, optionally avoiding default log-space cutoffs."""
    compiled = get_evaluatable().create_from(PrologString(source))
    options = {"semiring": SemiringProbability()} if normal_probability else {}
    return {str(key): value for key, value in compiled.evaluate(**options).items()}


def forced_sample(source: str, draws: list[float]) -> dict[str, bool]:
    """Use legal deterministic RNG outputs to exercise otherwise rare branches."""
    with patch("problog.tasks.sample.random.random", side_effect=draws):
        result = next(sample(PrologString(source), format="dict"))
    return {str(key): value for key, value in result.items()}


def main() -> None:
    """Check expected identities, recursion, aggregation and numerical boundaries."""
    results: dict[str, object] = {"problog_version": version("problog")}
    assert results["problog_version"] == "2.3.0", "Reassess these observations on upgrades"

    same = infer("0.5::heads(k). both :- heads(k), heads(k). query(both).")
    fresh = infer(
        "0.5::heads(K) :- between(1,2,K). "
        "both :- heads(1), heads(2). query(both)."
    )
    body = infer("tag(a). tag(b). 0.5::selected :- tag(X). query(selected).")
    assert same == {"both": 0.5}
    assert fresh == {"both": 0.25}
    assert body == {"selected": 0.75}
    results["choice_identity"] = {"same_atom": same, "fresh_ids": fresh, "body_variables": body}

    duplicates = infer(
        "value(1,a). value(2,a). "
        "result(L) :- findall(X,value(_,X),L). query(result(_))."
    )
    assert duplicates == {"result([a, a])": 1.0}
    results["findall_preserves_repeated_values"] = duplicates
    repeated = infer(
        "0.5::value(1,a). 0.5::value(2,a). "
        "result(L) :- findall(X,value(_,X),L). query(result(_))."
    )
    assert repeated == {"result([])": 0.25, "result([a])": 0.5, "result([a, a])": 0.25}
    results["probabilistic_repeated_values"] = repeated

    recursive = forced_sample(
        "0.5::stop(T). "
        "walk(T,T) :- stop(T). "
        "walk(T,N) :- \\+ stop(T), U is T+1, walk(U,N). "
        "result(N) :- walk(0,N). query(result(_)).",
        [0.9, 0.9, 0.1],
    )
    assert recursive == {"result(2)": True}
    results["unbounded_recursion_sample"] = recursive

    optimum = infer(
        ":- use_module(library(lists)). "
        "0.5::cheap. cost(a,1) :- cheap. cost(a,5) :- \\+ cheap. cost(b,3). "
        "optimum(M) :- findall(C,cost(_,C),L), min_list(L,M). query(optimum(_))."
    )
    assert optimum == {"optimum(1)": 0.5, "optimum(3)": 0.5}
    results["per_world_minimum"] = optimum

    categorical = "0.999999995::common; 0.000000005::rare. query(common). query(rare)."
    categorical_mass = infer(categorical)
    categorical_sample = forced_sample(categorical, [0.9999999999])
    assert isclose(categorical_mass["rare"], 5e-9, rel_tol=1e-12)
    assert categorical_sample == {"common": False, "rare": False}
    results["annotated_disjunction_tail"] = {
        "inference": categorical_mass,
        "forced_tail_sample": categorical_sample,
        "finding": "Sampler drops a positive tail and returns an impossible null outcome",
    }

    weighted_tail = forced_sample(
        ":- use_module(library(lists)). "
        "outcome(X) :- select_weighted(test,[0.999999995,0.000000005],"
        "[common,rare],X,_). query(outcome(_)).",
        [0.9999999999],
    )
    assert weighted_tail == {"outcome(rare)": True}
    results["weighted_selector_avoids_ad_cutoff"] = weighted_tail

    tiny = "(1/10000000000)::rare. query(rare)."
    default_tiny = infer(tiny)
    normal_tiny = infer(tiny, normal_probability=True)
    assert default_tiny == {"rare": 0.0}
    assert normal_tiny == {"rare": 1e-10}
    results["default_inference_cutoff"] = {"default": default_tiny, "normal_space": normal_tiny}

    boundary = "result(V) :- V is truncate(1.9999999999999998). query(result(_))."
    rounded = infer(boundary)
    literal = "0.0000000000000001::rare. query(rare)."
    rounded_literal = infer(literal, normal_probability=True)
    precision = Constant.FLOAT_PRECISION
    try:
        Constant.FLOAT_PRECISION = None
        unrounded = infer(boundary)
        unrounded_literal = infer(literal, normal_probability=True)
    finally:
        Constant.FLOAT_PRECISION = precision
    assert rounded == {"result(2)": 1.0}
    assert unrounded == {"result(1)": 1.0}
    assert rounded_literal == {"rare": 0.0}
    assert unrounded_literal == {"rare": 1e-16}
    results["float_constant_rounding"] = {
        "default_precision": precision,
        "default_boundary": rounded,
        "rounding_disabled_boundary": unrounded,
        "default_tiny_literal": rounded_literal,
        "rounding_disabled_tiny_literal": unrounded_literal,
    }
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
