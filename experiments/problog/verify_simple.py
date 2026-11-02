"""Historical stock-ProbLog feasibility checks against frozen Python samplers.

Run with an environment containing problog==2.3.0 and this project's [specs] extra:
    python experiments/problog/verify_simple.py

The engine uses floating probabilities. Exhaustive comparisons below use exact
Fraction trace weights as the oracle and an explicit numerical tolerance.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict
from fractions import Fraction
from importlib import import_module
import json
from pathlib import Path
import random
import sys
from time import perf_counter

from problog import get_evaluatable
from problog.logic import Constant, Term, make_safe, unquote
from problog.program import PrologString
from problog.tasks.sample import sample as problog_sample

from pypddl_datasets.generators import load_specification
from pypddl_datasets.generators._specifications.interpretation import Situation
from pypddl_datasets.generators.runtime import Atom, Object, Problem, render_problem

DIRECTORY = Path(__file__).resolve().parent
sys.path.insert(0, str(DIRECTORY.parents[1] / "tests"))
QUERIES = '\n'.join(f'query({query}).' for query in (
    'object(_,_)', 'initial(_)', 'goal(_)', 'domain(_)', 'problem_name(_)'))


def model_text(domain, parameters, *, queries=True):
    """Supply integer parameter facts, without generating domain rules in Python."""
    facts = '\n'.join(f'{name}({value}).' for name, value in parameters.items())
    return '\n'.join((DIRECTORY.joinpath(f'{domain}.pl').read_text(), facts,
                      QUERIES if queries else ''))


def decode_sample(world):
    """One domain-independent bridge from Boolean output terms to existing PDDL."""
    present = [term for term, value in world.items() if value is True]
    declarations = []
    initial, goal = [], []
    metadata = {}
    for term in present:
        kind = unquote(term.functor)
        if kind == 'object':
            name, type_name = (unquote(str(arg)) for arg in term.args)
            declarations.append(Object(name, None if type_name == 'untyped' else type_name))
        elif kind in ('initial', 'goal'):
            atom = term.args[0]
            value = Atom(unquote(atom.functor), tuple(unquote(str(arg)) for arg in atom.args))
            (initial if kind == 'initial' else goal).append(value)
        elif kind in ('domain', 'problem_name'):
            metadata[kind] = unquote(str(term.args[0]))
    return Problem(metadata['problem_name'], metadata['domain'], tuple(declarations),
                   tuple(initial), tuple(goal))


def signature(problem):
    """Ignore ordering, which is not part of a labeled semantic task."""
    return frozenset(problem.objects), frozenset(problem.initial), frozenset(problem.goal)


class NextChoice(Exception):
    def __init__(self, count):
        self.count = count


class ChoiceTrace:
    """Enumerate actual Python generator calls to choice, independently of ProbLog."""
    def __init__(self, prefix):
        self.prefix, self.index = prefix, 0

    def choice(self, values):
        if self.index == len(self.prefix):
            raise NextChoice(len(values))
        index = self.prefix[self.index]
        self.index += 1
        return values[index]


def trace_distribution(generator, parameters):
    pending = [((), Fraction(1))]
    weights, problems = defaultdict(Fraction), {}
    while pending:
        prefix, mass = pending.pop()
        try:
            problem = generator.sample(parameters, ChoiceTrace(prefix))
        except NextChoice as choice:
            pending.extend(((*prefix, index), mass / choice.count) for index in range(choice.count))
        else:
            key = signature(problem)
            weights[key] += mass
            problems[key] = problem
    assert sum(weights.values()) == 1
    return dict(weights), problems


def interpretation(spec, problem):
    initial, goal = set(problem.initial), set(problem.goal)
    names = {obj.name for obj in problem.objects}
    values = []
    for key in spec.semantic_variables:
        if key.kind == 'object':
            value = key.predicate in names
        else:
            assert key.kind == 'atom'
            value = Atom(key.predicate, key.arguments) in (initial if key.group == 'initial' else goal)
        values.append((key, value))
    return Situation(tuple(values))


def binding_query(index, situation):
    """Bind every declared semantic variable, including all absent atoms."""
    literals = []
    for key, value in situation.values:
        if key.kind == 'object':
            type_name = 'untyped' if key.arguments[0] == 'object' else key.arguments[0]
            term = Term('object', Term(key.predicate), Term(type_name))
        else:
            atom = Term(make_safe(key.predicate), *(Term(make_safe(arg)) for arg in key.arguments))
            term = Term(key.group, atom)
        literals.append(str(term) if value else '\\+ ' + str(term))
    return f'outcome({index}) :- ' + ', '.join(literals) + f'.\nquery(outcome({index})).'


def check_case(domain, values, expected_counts, samples=20):
    generator = import_module(f'reference_generators.{domain}')
    parameters = generator.Parameters(**values)
    oracle, problems = trace_distribution(generator, parameters)
    assert Counter(oracle.values()) == expected_counts
    spec = load_specification(domain, parameters)
    permitted = spec.enumerate(limit=len(oracle))
    assert permitted.complete
    situations = {key: interpretation(spec, problem) for key, problem in problems.items()}
    assert {s.identity for s in situations.values()} == {s.identity for s in permitted.situations}
    keys = list(oracle)
    queries = [binding_query(index, situations[key]) for index, key in enumerate(keys)]
    source = model_text(domain, values, queries=False) + '\n' + '\n'.join(queries)
    started = perf_counter()
    probabilities = get_evaluatable().create_from(PrologString(source)).evaluate()
    elapsed = perf_counter() - started
    errors = [abs(probabilities[Term('outcome', Constant(index))] - float(oracle[key]))
              for index, key in enumerate(keys)]
    assert max(errors) < 1e-12
    assert abs(sum(probabilities.values()) - 1) < 1e-12
    for world in problog_sample(PrologString(model_text(domain, values)), n=samples, format='dict'):
        problem = decode_sample(world)
        assert signature(problem) in oracle
        assert spec.check_pddl(render_problem(problem)).is_member
    return {'domain': domain, 'parameters': values, 'tasks': len(oracle),
            'weight_counts': {str(weight): count for weight, count in expected_counts.items()},
            'max_absolute_probability_error': max(errors),
            'inference_seconds': elapsed, 'rendered_samples_checked': samples}


def benchmark(domain, values, samples=10):
    generator = import_module(f'reference_generators.{domain}')
    parameters = generator.Parameters(**values)
    model = PrologString(model_text(domain, asdict(parameters)))
    started = perf_counter()
    stream = problog_sample(model, n=samples + 1, format='dict')
    first = decode_sample(next(stream))
    first_seconds = perf_counter() - started
    started = perf_counter()
    for world in stream:
        decode_sample(world)
    per_sample = (perf_counter() - started) / samples
    rng = random.Random(7)
    started = perf_counter()
    for _ in range(1000):
        generator.sample(parameters, rng)
    python_seconds = (perf_counter() - started) / 1000
    # Check a produced task against the independent support contract.
    spec = load_specification(domain, parameters)
    assert spec.check_pddl(render_problem(first)).is_member
    return {'domain': domain, 'parameters': values, 'subsequent_samples': samples,
            'prepare_and_first_sample_seconds': first_seconds,
            'subsequent_sample_and_decode_seconds': per_sample,
            'python_sample_seconds': python_seconds,
            'observed_slowdown': per_sample / python_seconds}


if __name__ == '__main__':
    random.seed(7)
    results = {
        'exact_mode_note': 'Exhaustive inference uses floating probabilities; compared with exact rational trace weights.',
        'cases': [
            check_case('ferry', {'num_cars': 1, 'num_locations': 2}, {Fraction(1, 8): 8}),
            check_case('ferry', {'num_cars': 0, 'num_locations': 1}, {Fraction(1): 1}),
            check_case('ferry', {'num_cars': 2, 'num_locations': 2}, {Fraction(1, 32): 32}),
            check_case('delivery', {'grid_size': 2, 'num_packages': 1}, {Fraction(1, 48): 48}),
            check_case('delivery', {'grid_size': 2, 'num_packages': 2}, {Fraction(1, 192): 48, Fraction(1, 256): 192}),
        ],
        'benchmarks': [
            benchmark('ferry', {'num_cars': 10, 'num_locations': 5}),
            benchmark('delivery', {'grid_size': 5, 'num_packages': 5}),
        ],
    }
    print(json.dumps(results, indent=2))
