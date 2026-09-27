import re
from collections import deque
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.rainbowttles import generator
from pypddl_datasets.generators.numeric.ipc.rainbowttles.generator import main, make_problem


def _bottles(problem):
    init = problem.split("(:init")[1].split("(:goal")[0]
    names = sorted(set(re.findall(r"bottle\d+", init)))
    stacks = []
    for b in names:
        below = dict(re.findall(rf"\(colour-below {b} (\S+) (\S+)\)", init))
        top = re.search(rf"\(upper-colour {b} (\S+)\)", init).group(1)
        chain = []
        while top != "empty":
            chain.append((top, int(re.search(rf"\(= \(colour-segments {b} {top}\) (\d+)\)", init).group(1))))
            top = below[top]
        stacks.append(tuple(reversed(chain)))  # bottom first
    return stacks


def _solvable(stacks, capacity):
    """BFS over the domain's pour / pour-to-empty; solved when every bottle is empty or one full colour."""
    def done(state):
        return all(not s or (len(s) == 1 and s[0][1] == capacity) for s in state)
    start = tuple(stacks)
    seen, queue = {start}, deque([start])
    while queue:
        state = queue.popleft()
        if done(state):
            return True
        for i, src in enumerate(state):
            if not src:
                continue
            colour, k = src[-1]
            for j, dst in enumerate(state):
                if i == j or sum(n for _, n in dst) + k > capacity:
                    continue
                if dst and dst[-1][0] != colour:
                    continue
                new_dst = dst[:-1] + ((colour, dst[-1][1] + k),) if dst else ((colour, k),)
                nxt = list(state)
                nxt[i], nxt[j] = src[:-1], new_dst
                nxt = tuple(nxt)
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
    return False


@pytest.mark.parametrize("seed", range(8))
def test_scramble_keeps_invariants_and_stays_solvable(seed):
    problem = make_problem(3, num_spare=2, scramble_steps=6, seed=seed)
    assert problem == make_problem(3, num_spare=2, scramble_steps=6, seed=seed)
    stacks = _bottles(problem)
    totals = {}
    for stack in stacks:
        colours = [c for c, _ in stack]
        assert len(colours) == len(set(colours)) and sum(n for _, n in stack) <= 4
        for c, n in stack:
            totals[c] = totals.get(c, 0) + n
    assert totals == {"red": 4, "green": 4, "blue": 4}
    assert _solvable(stacks, 4)


def test_two_bottles_per_colour_and_goal():
    problem = make_problem(8, num_spare=3, bottles_per_colour=2, scramble_steps=30, seed=1)
    stacks = _bottles(problem)
    assert len(stacks) == 19 and sum(n for s in stacks for _, n in s) == 64
    assert len(re.findall(r"\(closed bottle\d+\)", problem.split("(:goal")[1])) == 19


def test_parses_strictly(tmp_path):
    (tmp_path / "p.pddl").write_text(make_problem(10, num_spare=4, bottles_per_colour=2, scramble_steps=41, seed=2))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cli_and_validation(capsys):
    assert main(["-c", "4", "-k", "7", "-s", "5"]) == 0
    assert capsys.readouterr().out == make_problem(4, scramble_steps=7, seed=5)
    for kwargs in (dict(num_colours=0), dict(num_colours=11), dict(num_colours=3, num_spare=0)):
        with pytest.raises(ValueError):
            make_problem(**kwargs)
