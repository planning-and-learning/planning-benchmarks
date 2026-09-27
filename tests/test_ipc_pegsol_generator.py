import re

import pytest

from pypddl_datasets.generators.classical.ipc.pegsol.generator import LINES, main, make_problem


def _solves_to_centre(pegs: frozenset[tuple[int, int]]) -> bool:
    dead: set[frozenset[tuple[int, int]]] = set()

    def search(state: frozenset[tuple[int, int]]) -> bool:
        if len(state) == 1:
            return state == {(3, 3)}
        if state in dead:
            return False
        for frm, over, to in LINES:
            if frm in state and over in state and to not in state and search((state - {frm, over}) | {to}):
                return True
        dead.add(state)
        return False

    return search(pegs)


@pytest.mark.parametrize("num_pegs,seed", [(1, 0), (5, 1), (9, 2), (12, 3)])
def test_pegsol_positions_are_solvable_end_games(num_pegs, seed):
    problem = make_problem(num_pegs, seed=seed)
    assert problem == make_problem(num_pegs, seed=seed) and problem == problem.lower()
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    assert len(re.findall(r" - location", problem)) == 33
    assert len(re.findall(r"\(in-line ", init)) == 76
    occupied = frozenset((int(r), int(c)) for r, c in re.findall(r"\(occupied pos-(\d)-(\d)\)", init))
    free = re.findall(r"\(free pos-\d-\d\)", init)
    assert len(occupied) == num_pegs and len(free) == 33 - num_pegs
    assert "(= (total-cost) 0)" in init and "(move-ended)" in init
    assert re.findall(r"\(occupied (\S+)\)", goal) == ["pos-3-3"] and len(re.findall(r"\(free ", goal)) == 32
    assert _solves_to_centre(occupied)


def test_pegsol_full_board_holes_and_large_counts():
    holes = set()
    for seed in range(30):
        init = make_problem(32, seed=seed).split("(:init", 1)[1].split("(:goal", 1)[0]
        holes |= set(re.findall(r"\(free (pos-\d-\d)\)", init))
    assert holes == {"pos-0-3", "pos-3-0", "pos-3-3", "pos-3-6", "pos-6-3"}
    assert len(re.findall(r"\(occupied ", make_problem(28, seed=4).split("(:goal")[0])) == 28


def test_pegsol_cli_and_validation(capsys):
    assert main(["-n", "7", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(7, seed=3)
    for value in (0, 33, 2.5, True):
        with pytest.raises(ValueError, match="num_pegs"):
            make_problem(value)
