"""Rejected grounding-table optimizations, with reproducible semantic counterexamples.

These prototypes must remain experimental: even sharing only complete, ground
Boolean answers changes programs whose predicates inspect variable bindings.
"""
from __future__ import annotations

from contextvars import ContextVar
import json
from random import Random
from time import perf_counter

from problog.engine_stack import DefineCache
from problog.logic import is_ground
from pypddl_datasets.generators import model_source
from pypddl_datasets.generators._problog import engine as backend
from pypddl_datasets.generators._problog.prepared import clear_prepared_cache, prepared_program

ORIGINAL = backend.SampleFormula
CACHE = ContextVar('pypddl_probe_world_cache', default=None)
QUERIES = '\n'.join(f'query({term}).' for term in (
    'object(_,_)', 'initial(_)', 'goal(_)', 'domain(_)', 'problem_name(_)', 'failure(_)'))


class BooleanCache(DefineCache):
    """Assert the node-portability premise instead of silently accepting it."""
    def __setitem__(self, goal, results):
        assert all(node in (0, None) for _, node in results.items()), (goal, results)
        return super().__setitem__(goal, results)


class ExactCache(DefineCache):
    """Also rejected: exact calls do not replay transitive local cache effects."""
    def __init__(self, shared, dont_cache):
        super().__init__(dont_cache)
        self.shared = shared

    def key(self, goal):
        if self.is_dont_cache(goal) or getattr(goal[1], 'state', None):
            return None
        functor, arguments = self._reindex_vars(goal)
        return functor, tuple(arguments)

    def __setitem__(self, goal, results):
        super().__setitem__(goal, results)
        key, rows = self.key(goal), list(results.items())
        if key is not None and all(node in (0, None) and is_ground(*args)
                                   and not getattr(args, 'state', None) for args, node in rows):
            self.shared[key] = rows

    def get(self, goal, default=None):
        result = super().get(goal)
        if result is not None:
            return result
        result = self.shared.get(self.key(goal))
        if result is not None:
            super().__setitem__(goal, dict(result))
            return result
        return default


class SharedFormula(ORIGINAL):
    def __init__(self, **options):
        super().__init__(**options)
        shared = CACHE.get()
        if shared is None:
            shared = BooleanCache(set())
            CACHE.set(shared)
        self._cache = ExactCache(*shared) if isinstance(shared, tuple) else shared


def run(source, seed, shared):
    backend.SampleFormula = SharedFormula if shared else ORIGINAL
    with prepared_program(source) as prepared:
        shared_table = (({}, prepared.database.dont_cache) if shared == "exact"
                        else BooleanCache(prepared.database.dont_cache))
    token = CACHE.set(shared_table)
    try:
        return backend.sample_source(source, Random(seed))
    finally:
        CACHE.reset(token)
        backend.SampleFormula = ORIGINAL


def checks():
    probes = [
        'out(L):-findall(X,member(X,[a,a,b]),L). query(out(_)).',
        'p(a). p(b). out(L):-findall(X,p(X),L). nested(L):-findall(X,out(X),L). query(out(_)). query(nested(_)).',
        'edge(a,b). edge(b,a). edge(b,c). reach(A,B):-edge(A,B). reach(A,B):-edge(A,C),reach(C,B). out(L):-findall(X,reach(a,X),L). query(reach(a,_)). query(out(_)).',
        '0.5::coin. p(a):-coin. p(b):-\\+coin. out(L):-findall(X,p(X),L). query(p(_)). query(out(_)).',
    ]
    for source in probes:
        source = ':- use_module(library(lists)).\n' + source
        for seed in range(3):
            clear_prepared_cache()
            expected = run(source, seed, False)
            assert run(source, seed, True) == expected


def counterexamples():
    cases = (
        ('ground_promotion', True,
         'p(X):-var(X),X=a. a(L):-findall(X,p(X),L). '
         'b(L):-findall(X,(p(a),X=a),L). query(a(_)). query(b(_)).'),
        ('transitive_local_cache', 'exact',
         'q(X):-var(X),X=a. p(X):-q(X). a(L):-findall(X,p(X),L). '
         'b(L):-findall(X,(p(X),q(a)),L). query(a(_)). query(b(_)).'),
    )
    for name, shared, source in cases:
        expected, actual = run(source, 0, False), run(source, 0, shared)
        assert actual != expected, 'this experiment must expose its known limitation'
        print(json.dumps({'counterexample': name, 'cache': shared, 'source': source,
                          'reference': {str(term): value for term, value in expected.items()},
                          'cached': {str(term): value for term, value in actual.items()}}), flush=True)


def main():
    counterexamples()
    checks()
    results = []
    for domain, parameters in (
        ('ferry', {'num_cars': 17, 'num_locations': 12}),
        ('delivery', {'grid_size': 13, 'num_packages': 12}),
        ('rovers', {'num_rovers': 4, 'num_waypoints': 10, 'num_objectives': 4,
                    'num_cameras': 5, 'num_goals': 8}),
        ('rovers', {'num_rovers': 10, 'num_waypoints': 25, 'num_objectives': 6,
                    'num_cameras': 10, 'num_goals': 10}),
    ):
        source = model_source(domain, parameters) + '\n' + QUERIES
        run(source, 0, False)  # Prepare both comparisons before starting their timers.
        expected = None
        for shared in (False, True):
            start = perf_counter()
            actual = run(source, 0, shared)
            elapsed = perf_counter() - start
            if expected is None:
                expected = actual
            assert actual == expected, domain
            row = {'domain': domain, 'parameters': parameters,
                   'shared': shared, 'seconds': elapsed, 'queries': len(actual)}
            results.append(row)
            print(json.dumps(row), flush=True)
    return results


if __name__ == '__main__':
    main()
