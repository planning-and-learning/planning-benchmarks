"""Verify isolated ProbLog graph hierarchy, retry and repair models.

Run with Python from a temporary environment containing problog==2.3.0.
This checks probabilities against independent rational formulas, not seeds.
The ProbLog evaluator itself uses floating point.
"""

from __future__ import annotations

import json
import math
import random
from fractions import Fraction
from pathlib import Path
from time import perf_counter

from problog import get_evaluatable
from problog.logic import Term, term2list
from problog.program import PrologString
from problog.tasks.sample import sample

HERE = Path(__file__).resolve().parent
SOURCE = (HERE / "conditioning.pl").read_text()


def evaluate(source: str) -> tuple[dict[Term, float], float]:
    start = perf_counter()
    result = get_evaluatable().create_from(PrologString(source)).evaluate()
    return result, perf_counter() - start


def close(actual: float, expected: Fraction) -> None:
    assert math.isclose(actual, float(expected), rel_tol=1e-11, abs_tol=1e-12), (
        actual, expected
    )


def finite_probabilities(budget: int) -> tuple[Fraction, Fraction]:
    """Independent derivation: four equally likely connected visibility graphs.

    A path has proposal success 1/4; a triangle has proposal success 1/2.
    Visibility itself succeeds with 1-(1/2)^budget. The child retry holds the
    sampled visibility fixed, so its success probability depends on that graph.
    """
    visibility_success = 1 - Fraction(1, 2) ** budget
    path_success = 1 - Fraction(3, 4) ** budget
    success = visibility_success * (3 * path_success + visibility_success) / 4
    complete_success = visibility_success**2 / 4
    return success, complete_success


def main() -> None:
    report: dict[str, object] = {}
    local, elapsed = evaluate(SOURCE + "\nquery(local(V,T)).")
    assert len(local) == 7
    for term, probability in local.items():
        visible = term2list(term.args[0])
        expected = Fraction(1, 16) if len(visible) == 3 else Fraction(1, 4)
        close(probability, expected)
    close(sum(local.values()), Fraction(1))
    report["local"] = {"outcomes": len(local), "seconds": elapsed,
                       "complete_visibility_probability": "1/4"}

    global_result, elapsed = evaluate(
        SOURCE + "\nquery(raw_pair(V,T)). evidence(global_accept)."
    )
    supported_global = {q: p for q, p in global_result.items() if p > 0}
    assert len(supported_global) == 7
    for term, probability in supported_global.items():
        expected = Fraction(1, 10) if len(term2list(term.args[0])) == 3 else Fraction(1, 5)
        close(probability, expected)
    close(sum(global_result.values()), Fraction(1))
    report["global_evidence"] = {"outcomes": len(supported_global), "seconds": elapsed,
                                 "complete_visibility_probability": "2/5"}

    for budget in (1, 2, 3):
        expected_success, expected_complete = finite_probabilities(budget)
        for method, predicate in (("explicit", "finite"), ("collapsed", "collapsed_pair")):
            result, elapsed = evaluate(SOURCE + f"\nquery({predicate}({budget},V,T)).")
            supported = {q: p for q, p in result.items() if p > 0}
            assert len(supported) == 12
            visibility_success = 1 - Fraction(1, 2) ** budget
            observed_success = observed_complete = 0.0
            for term, probability in supported.items():
                visible, traversal = term.args[1:]
                if str(visible) == "failure":
                    expected = 1 - visibility_success
                else:
                    complete = len(term2list(visible)) == 3
                    child_failure = (Fraction(1, 2) if complete else Fraction(3, 4)) ** budget
                    child = child_failure if str(traversal) == "failure" else (1 - child_failure) / (4 if complete else 1)
                    expected = visibility_success * child / 4
                    if str(traversal) != "failure":
                        observed_success += probability
                        if complete:
                            observed_complete += probability
                close(probability, expected)
            close(sum(supported.values()), Fraction(1))
            close(observed_success, expected_success)
            close(observed_complete, expected_complete)
            report[f"{method}_budget_{budget}"] = {
                "seconds": elapsed,
                "success": str(expected_success),
                "failure": str(1 - expected_success),
                "complete_visibility_given_success": str(expected_complete / expected_success),
            }

    repair, elapsed = evaluate((HERE / "repair.pl").read_text())
    by_name = {str(q): p for q, p in repair.items()}
    close(by_name["only_a"], Fraction(3, 8))
    close(by_name["only_b"], Fraction(3, 8))
    close(by_name["both"], Fraction(1, 4))
    report["repair"] = {"seconds": elapsed, "only_a": "3/8", "only_b": "3/8", "both": "1/4"}

    # Querying the joint term verifies that each sampled world emits one pair.
    # It also avoids confusing per-edge marginals with an entire sampled graph.
    for query, count, label in (
        ("query(local(V,T)).", 5, "sample_local"),
        ("query(finite(10000,V,T)).", 50, "sample_explicit_budget_10000"),
    ):
        random.seed(20260916)
        start = perf_counter()
        for world in sample(PrologString(SOURCE + "\n" + query), n=count, format="dict"):
            selected = [term for term, value in world.items() if value]
            assert len(selected) == 1, world
            term = selected[0]
            graph_arguments = term.args if label == "sample_local" else term.args[1:]
            assert all(str(graph) != "failure" for graph in graph_arguments)
            assert all(len(term2list(graph)) >= 2 for graph in graph_arguments)
        report[label] = {"count": count, "seconds": perf_counter() - start}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
