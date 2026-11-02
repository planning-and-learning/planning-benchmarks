"""Compare a declarative tiny Grid model with exhaustive legacy RNG histories."""
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from random import Random, seed
from time import perf_counter

from problog import get_evaluatable
from problog.logic import term2list
from problog.program import PrologFile
from problog.tasks.sample import sample as problog_sample

from pypddl_datasets.generators import load_specification
from pypddl_datasets.generators.classical.grid.generator import Parameters, sample
from pypddl_datasets.generators.runtime import render_problem


class Branch(Exception):
    def __init__(self, size):
        self.size = size


class ChoiceTrace:
    """Enumerate intended uniform integer choices, independently of ProbLog."""
    def __init__(self, prefix):
        self.prefix = iter(prefix)

    def randrange(self, start, stop=None, step=1):
        values = range(start) if stop is None else range(start, stop, step)
        try:
            index = next(self.prefix)
        except StopIteration:
            raise Branch(len(values)) from None
        return values[index]

    def choice(self, values):
        return values[self.randrange(len(values))]

    def sample(self, values, count):
        remaining = list(values)
        return [remaining.pop(self.randrange(len(remaining))) for _ in range(count)]

    def random(self):
        return 0.0  # This fixture has goal_probability=1.


def cell(name):
    x, y = map(int, name.removeprefix("pos").split("-"))
    return x * 2 + y


def legacy_outcome(problem):
    locks = tuple(sorted(cell(a.arguments[0]) for a in problem.initial if a.predicate == "locked"))
    robot = next(cell(a.arguments[0]) for a in problem.initial if a.predicate == "at-robot")
    key = next(cell(a.arguments[1]) for a in problem.initial if a.predicate == "at")
    return locks, robot, key, cell(problem.goal[0].arguments[1])


def logic_outcome(term):
    locks, robot, key, goal = term.args
    return tuple(int(x) for x in term2list(locks)), int(robot), int(key), int(goal)


def main():
    parameters = Parameters(2, 2, 1, 1, 2)
    spec = load_specification("grid", parameters)
    expected = defaultdict(Fraction)
    queue = [((), Fraction(1))]
    while queue:
        prefix, mass = queue.pop()
        try:
            problem = sample(parameters, ChoiceTrace(prefix))
        except Branch as branch:
            queue.extend(((*prefix, index), mass / branch.size) for index in range(branch.size))
        else:
            assert spec.check_pddl(render_problem(problem)).is_member
            expected[legacy_outcome(problem)] += mass
    enumeration = spec.enumerate(limit=100)
    assert enumeration.complete and len(enumeration.situations) == len(expected) == 60
    assert sum(expected.values()) == 1

    path = Path(__file__).with_name("grid_tiny.pl")
    start = perf_counter()
    probabilities = get_evaluatable().create_from(PrologFile(str(path))).evaluate()
    inference_seconds = perf_counter() - start
    observed = {logic_outcome(term): value for term, value in probabilities.items() if value > 0}
    assert observed.keys() == expected.keys()
    error = max(abs(observed[key] - float(value)) for key, value in expected.items())
    assert error < 1e-12

    seed(17)  # ProbLog 2.3.0 uses the process-global Python RNG.
    iterator = problog_sample(PrologFile(str(path)), n=101, format="dict")
    start = perf_counter()
    next(iterator)
    first_seconds = perf_counter() - start
    start = perf_counter()
    for world in iterator:
        outcomes = [term for term, truth in world.items() if truth and term.functor == "outcome"]
        assert len(outcomes) == 1 and logic_outcome(outcomes[0]) in expected
    sample_seconds = perf_counter() - start
    rng = Random(17)
    start = perf_counter()
    for _ in range(100):
        sample(parameters, rng)
    python_seconds = perf_counter() - start
    print({"tasks": len(expected), "oracle_masses": dict(Counter(map(str, expected.values()))),
           "max_absolute_probability_error": error, "inference_seconds": inference_seconds,
           "first_sample_seconds": first_seconds, "next_100_samples_seconds": sample_seconds,
           "legacy_100_samples_seconds": python_seconds})


if __name__ == "__main__":
    main()
