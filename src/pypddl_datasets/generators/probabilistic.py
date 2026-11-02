"""Public declarative ProbLog sampling and finite probability-reference API."""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import fields, is_dataclass
from fractions import Fraction
from importlib import import_module
from importlib.resources import files
import math
import re
from typing import cast

from .runtime import Problem, RandomSource

MODEL_DOMAINS = ("delivery", "ferry", "rovers")
_OUTPUT_QUERIES = "\n".join(f"query({value})." for value in (
    "object(_,_)", "initial(_)", "goal(_)", "domain(_)", "problem_name(_)", "failure(_)",
))


def _parameter_values(parameters: object) -> dict[str, int | float]:
    values: dict[object, object]
    if is_dataclass(parameters) and not isinstance(parameters, type):
        values = {item.name: getattr(parameters, item.name) for item in fields(parameters)}
    elif isinstance(parameters, Mapping):
        values = dict(cast(Mapping[object, object], parameters))
    else:
        raise TypeError("parameters must be a dataclass instance or mapping")
    result: dict[str, int | float] = {}
    for name, value in values.items():
        if not isinstance(name, str) or not re.fullmatch(r"[a-z][a-z_0-9]*", name):
            raise ValueError("parameter names must be lowercase identifiers")
        if isinstance(value, bool) or not isinstance(value, (int, float)) or (isinstance(value, float) and not math.isfinite(value)):
            raise ValueError(f"parameter {name!r} must be a finite number")
        result[name] = value
    return result


def _validated_parameters(domain: str, parameters: object) -> dict[str, int | float]:
    values = _parameter_values(parameters)
    budget = values.pop("graph_budget", None) if domain == "rovers" else None
    parameter_type = getattr(import_module(f".classical.{domain}.parameters", __package__), "Parameters")
    values = _parameter_values(parameter_type(**values))
    if budget is not None:
        if not isinstance(budget, int) or budget < 0:
            raise ValueError("graph_budget must be a nonnegative integer")
        values["graph_budget"] = budget
    return values


def model_source(domain: str, parameters: object) -> str:
    """Return the complete public model, shared choices and parameter facts."""
    if domain not in MODEL_DOMAINS:
        raise ValueError(f"no ProbLog model for {domain!r}")
    root = files("pypddl_datasets.generators")
    common = root.joinpath("_problog").joinpath("library.pl").read_text()
    model = root.joinpath("classical").joinpath(domain).joinpath("distribution.pl").read_text()
    facts = "\n".join(f"{name}({value!r})." for name, value in _validated_parameters(domain, parameters).items())
    return "\n".join((common, model, facts, "failure(_) :- fail."))


def sample_model(domain: str, parameters: object, rng: RandomSource) -> Problem:
    """Draw a labeled task, retaining explicit model failure outcomes."""
    from ._problog.engine import sample_source
    from ._problog.output import decode_world
    return decode_world(sample_source(model_source(domain, parameters) + "\n" + _OUTPUT_QUERIES, rng))


def evaluate_model(domain: str, parameters: object, query_source: str) -> Mapping[str, Fraction]:
    """Evaluate finite queries exactly, without floating-point probability cutoffs."""
    from ._problog.engine import evaluate_source
    return evaluate_source(model_source(domain, parameters) + "\n" + query_source)
