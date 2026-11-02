"""Complete two-waypoint Rovers law, partitioned for tractable exact inference.

Run after installing .[dev,specs]. All 12,444 full tasks are checked. The 31
partitions fix equipment and camera modes; their masses are evaluated separately,
then multiply each conditional task probability. This is a complete joint-law
comparison, not a collection of marginal checks.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from contextlib import contextmanager
from dataclasses import asdict
from fractions import Fraction
import hashlib
import json
from importlib.metadata import version
from pathlib import Path
import resource
import signal
import sys
from time import perf_counter

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests"))

from reference_generators import rovers  # pylint: disable=wrong-import-position
from reference_generators.tracing import distribution  # pylint: disable=wrong-import-position
from test_problog_distributions import binding_query, interpretation  # pylint: disable=wrong-import-position
from pypddl_datasets.generators import load_specification  # pylint: disable=wrong-import-position
from pypddl_datasets.generators.probabilistic import evaluate_model, model_source  # pylint: disable=wrong-import-position
from pypddl_datasets.generators.runtime import Atom  # pylint: disable=wrong-import-position


def partition(problem):
    facts = {fact for fact in problem.initial if isinstance(fact, Atom)}
    equipment = tuple(Atom(f'equipped_for_{kind}', ('rover0',)) in facts
                      for kind in ('soil_analysis', 'rock_analysis', 'imaging'))
    modes = tuple(Atom('supports', ('camera0', mode)) in facts for mode in rovers.MODES)
    return equipment, modes


def partition_clause(index, label):
    equipment, modes = label
    flags = ','.join(str(flag).lower() for flag in equipment)
    body = f'base_equipment(0,{flags})'
    if equipment[2]:
        body += ',camera_flags(0,' + ','.join(str(flag).lower() for flag in modes) + ')'
    return f'partition({index}) :- {body}.'


def source_hashes():
    paths = [*sorted((ROOT / 'src/pypddl_datasets/generators/_problog').glob('*.py')),
             ROOT / 'tests/reference_generators/rovers.py',
             ROOT / 'tests/reference_generators/graphs.py',
             ROOT / 'tests/reference_generators/tracing.py',
             Path(__file__).resolve()]
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}


@contextmanager
def partition_budget(seconds):
    """Bound a reference-inference partition on this Unix verification runner."""
    def expired(_signum, _frame):
        raise TimeoutError(f'partition exceeded {seconds:g} seconds')
    previous = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def write_report(path, report):
    report['peak_rss_mib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    path.write_text(json.dumps(report, indent=2) + '\n')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('/tmp/problog-rovers-complete.json'))
    parser.add_argument('--partition-timeout', type=float, default=300,
                        help='maximum seconds for one conditional partition (default: 300)')
    parser.add_argument('--memory-mib', type=int, default=2048,
                        help='process virtual-memory limit in MiB (default: 2048)')
    args = parser.parse_args()
    if args.partition_timeout <= 0 or args.memory_mib <= 0:
        parser.error('resource limits must be positive')
    resource.setrlimit(resource.RLIMIT_AS, (args.memory_mib * 1024**2, args.memory_mib * 1024**2))
    parameters = rovers.Parameters(1, 2, 1, 0, 1, edge_probability=1)
    started = perf_counter()
    weights, problems = distribution(lambda rng: rovers.sample(parameters, rng))
    assert len(weights) == 12_444 and sum(weights.values(), Fraction()) == 1
    specification = load_specification('rovers', parameters)
    partitions = defaultdict(list)
    for key, problem in problems.items():
        partitions[partition(problem)].append(key)
    assert len(partitions) == 31
    labels = list(partitions)
    clauses = '\n'.join(partition_clause(index, label) for index, label in enumerate(labels))
    masses = {f'partition({index})': sum((weights[key] for key in partitions[label]), Fraction())
              for index, label in enumerate(labels)}
    assert evaluate_model('rovers', parameters, clauses + '\n' + '\n'.join(
        f'query(partition({index})).' for index in range(len(labels)))) == masses
    assert sum(masses.values(), Fraction()) == 1
    report = {
        'domain': 'rovers', 'parameters': asdict(parameters),
        'python': sys.version, 'problog': version('problog'),
        'source_sha256': source_hashes(),
        'partition_timeout_seconds': args.partition_timeout, 'memory_limit_mib': args.memory_mib,
        'model_sha256': hashlib.sha256(model_source('rovers', parameters).encode()).hexdigest(),
        'oracle': 'Frozen revision-2 Python sampler, complete exact rational choice histories',
        'reference_tasks': len(weights), 'reference_seconds': perf_counter() - started,
        'comparison': 'All full task probabilities = verified partition mass times exact conditional probability',
        'partitions': [], 'checked_tasks': 0, 'checked_mass': '0', 'complete': False,
    }
    write_report(args.output, report)
    print(json.dumps(report), flush=True)
    checked = set()
    total_mass = Fraction()
    for index, label in enumerate(labels):
        assert hashlib.sha256(model_source('rovers', parameters).encode()).hexdigest() == report['model_sha256'], 'model changed during verification'
        assert source_hashes() == report['source_sha256'], 'backend, oracle or verifier changed during verification'
        partition_started = perf_counter()
        keys = partitions[label]
        source = clauses + f'\nevidence(partition({index})).\n' + '\n'.join(
            binding_query(outcome, interpretation(specification, problems[key]))
            for outcome, key in enumerate(keys))
        try:
            with partition_budget(args.partition_timeout):
                actual = evaluate_model('rovers', parameters, source)
        except (TimeoutError, MemoryError) as error:
            report.update(status='resource_limit', failed_partition=index,
                          error=f'{type(error).__name__}: {error}',
                          elapsed_seconds=perf_counter() - started)
            write_report(args.output, report)
            raise
        mass = masses[f'partition({index})']
        expected = {f'outcome({outcome})': weights[key] / mass for outcome, key in enumerate(keys)}
        assert actual == expected
        assert sum(actual.values(), Fraction()) == 1
        assert not checked.intersection(keys)
        checked.update(keys)
        total_mass += mass
        report['partitions'].append({'index': index, 'tasks': len(keys), 'mass': str(mass),
                                     'seconds': perf_counter() - partition_started})
        report.update(checked_tasks=len(checked), checked_mass=str(total_mass),
                      elapsed_seconds=perf_counter() - started)
        write_report(args.output, report)
        print(f'Verified {index + 1}/31 partitions, {len(checked)}/{len(weights)} full tasks; mass {total_mass}', flush=True)
    assert total_mass == 1 and checked == set(weights)
    report.update(complete=True, status='complete')
    write_report(args.output, report)
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
