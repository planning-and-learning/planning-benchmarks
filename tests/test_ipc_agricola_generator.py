import re
from pathlib import Path

import pytest

from pypddl_datasets.generators.classical.ipc.agricola.generator import ROUND_CARDS, main, make_problem

IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


def _deterministic_facts(problem: str) -> tuple[list[str], list[str], list[str]]:
    problem = problem.lower()
    objects = problem.split("(:objects")[1].split("(:init")[0].split()
    init = re.findall(r"\((?:= \([^)]*\) \d+|[^()]*)\)", problem.split("(:init")[1].split("(:goal")[0])
    goal = re.findall(r"\([^()]*\)", problem.split("(:goal")[1].split("(:metric")[0])
    random_facts = ("(drawcard_round act", "(num_food", *(f"(open_action {card})" for card in ROUND_CARDS[:4]))
    return sorted(objects), sorted(f for f in init if not f.startswith(random_facts)), sorted(goal)


@pytest.mark.parametrize(
    "path,last_stage,workers,must",
    [("agricola-opt18-strips/p01.pddl", 3, 4, False), ("agricola-sat18-strips/p10.pddl", 12, 10, False),
     ("agricola-sat18-strips/p17.pddl", 9, 7, True)],
)
def test_agricola_reproduces_ipc_tasks_up_to_random_draws(path, last_stage, workers, must):
    problem = make_problem(last_stage, workers, must, seed=0)
    assert problem == make_problem(last_stage, workers, must, seed=0) and problem == problem.lower()
    assert _deterministic_facts(problem) == _deterministic_facts((IPC / path).read_text())


def test_agricola_random_draws():
    foods, first_cards = set(), set()
    for seed in range(40):
        init = make_problem(5, 6, seed=seed).split("(:init", 1)[1]
        draws = dict((int(r), c) for c, r in re.findall(r"\(drawcard_round (\S+) round(\d+)\)", init))
        assert sorted(draws[r] for r in range(1, 5)) == sorted(ROUND_CARDS[:4])
        assert sorted(draws[r] for r in range(5, 9)) == sorted(ROUND_CARDS[4:])
        assert f"(open_action {draws[1]})" in init
        foods |= set(re.findall(r"\(num_food num(\d)\)", init))
        first_cards.add(draws[1])
    assert foods == {"0", "1", "2", "3"} and first_cards == set(ROUND_CARDS[:4])


def test_agricola_cli_and_validation(capsys):
    assert main(["4", "-w", "6", "--must-create-workers", "-s", "2"]) == 0
    assert capsys.readouterr().out == make_problem(4, 6, True, seed=2)
    for parameters, name in (((0,), "last_stage"), ((13,), "last_stage"), ((3, 1), "num_workers")):
        with pytest.raises(ValueError, match=name):
            make_problem(*parameters)
