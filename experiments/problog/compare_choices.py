"""Isolated balanced-choice experiment; never changes the production model files.

Run each timing in a fresh process, for example:
    python experiments/problog/compare_choices.py check balanced
    python experiments/problog/compare_choices.py delivery linear
    python experiments/problog/compare_choices.py delivery balanced

The seed fixes each implementation independently. Different choice trees consume
random integers differently, so equal seeds do not imply equal Rovers tasks.
"""
from __future__ import annotations

import argparse
import hashlib
from importlib.resources import files
import json
import random
import resource
from time import perf_counter

from pypddl_datasets.generators._problog.engine import evaluate_source, sample_source
from pypddl_datasets.generators._problog.output import decode_world
from pypddl_datasets.generators.classical.delivery.parameters import Parameters as Delivery
from pypddl_datasets.generators.classical.rovers.parameters import Parameters as Rovers
from pypddl_datasets.generators.probabilistic import model_source
from pypddl_datasets.generators.runtime import render_problem

BALANCED = r"""
(Half/N)::uniform_left(Id,Values,Half,N).
uniform_split(0,Values,[],Values).
uniform_split(N,[X|Xs],[X|Left],Right) :- N>0,Next is N-1,
    uniform_split(Next,Xs,Left,Right).
uniform_halves(Values,Left,Right,Half,N) :- length(Values,N),N>1,
    Half is N//2,uniform_split(Half,Values,Left,Right).
uniform_choice(_,[X],X,[]).
uniform_choice(Id,Values,V,Rest) :- uniform_halves(Values,Left,Right,Half,N),
    uniform_left(Id,Values,Half,N),uniform_choice(Id,Left,V,Remaining),
    append(Remaining,Right,Rest).
uniform_choice(Id,Values,V,Rest) :- uniform_halves(Values,Left,Right,Half,N),
    \+ uniform_left(Id,Values,Half,N),uniform_choice(Id,Right,V,Remaining),
    append(Left,Remaining,Rest).
"""
QUERIES = "\n".join(f"query({value})." for value in (
    "object(_,_)", "initial(_)", "goal(_)", "domain(_)", "problem_name(_)", "failure(_)",
))


def alternatives() -> tuple[str, str]:
    """Replace only the uniform primitive in an in-memory model copy."""
    root = files("pypddl_datasets.generators").joinpath("_problog")
    library = root.joinpath("library.pl").read_text()
    start = library.index("(1/N)::uniform_head")
    end = library.index("uniform_int(", start)
    return library, library[:start] + BALANCED + library[end:]


def check(linear: str, balanced: str) -> dict[str, str]:
    queries = """
        u(X) :- uniform_choice(u,[a,b,c,d,e,f,g],X,_).
        d(X,R) :- uniform_choice(d,[a,b,a],X,R).
        same :- uniform_choice(s,[a,b,c],X,_),uniform_choice(s,[a,b,c],X,_).
        query(u(_)). query(d(_,_)). query(same).
    """
    actual = evaluate_source(balanced + queries)
    assert actual == evaluate_source(linear + queries)
    return {key: str(value) for key, value in actual.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=("check", "delivery", "rovers10", "rovers20"))
    parser.add_argument("variant", choices=("linear", "balanced"))
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()
    linear, balanced = alternatives()
    if args.case == "check":
        print(json.dumps(check(linear, balanced), indent=2))
        return
    if args.case == "delivery":
        domain, parameters = "delivery", Delivery(13, 12)
    elif args.case == "rovers10":
        domain, parameters = "rovers", Rovers(4, 10, 4, 5, 8)
    else:
        domain, parameters = "rovers", Rovers(4, 20, 10, 4, 10)
    source = model_source(domain, parameters)
    production_hash = hashlib.sha256(source.encode()).hexdigest()
    if args.variant == "balanced":
        source = source.replace(linear, balanced, 1)
    source += "\n" + QUERIES
    started = perf_counter()
    problem = decode_world(sample_source(source, random.Random(args.seed)))
    rendered = render_problem(problem)
    print(json.dumps({
        "case": args.case, "parameters": repr(parameters), "variant": args.variant,
        "seed": args.seed, "seconds": perf_counter() - started,
        "peak_mib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024,
        "objects": len(problem.objects), "initial": len(problem.initial),
        "goals": len(problem.goal), "production_model_sha256": production_hash,
        "experiment_source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "pddl_sha256": hashlib.sha256(rendered.encode()).hexdigest(),
    }, indent=2))


if __name__ == "__main__":
    main()
