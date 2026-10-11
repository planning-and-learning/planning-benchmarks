import re
from typing import Any

import pytest

from pypddl_datasets.generators.classical.ipc.thoughtful.generator import main, make_problem


def _chain(init: str, bottom: str, link: str) -> list[str]:
    above = {lower: upper for upper, lower in re.findall(rf"\({link} (\S+) (\S+)\)", init)}
    chain = [bottom]
    while chain[-1] in above:
        chain.append(above[chain[-1]])
    return chain


@pytest.mark.parametrize("num_cards,num_columns", [(1, 1), (5, 4), (11, 6), (13, 7)])
def test_thoughtful_deals_every_card_once(num_cards: int, num_columns: int) -> None:
    problem = make_problem(num_cards, num_columns, seed=3)
    assert problem == make_problem(num_cards, num_columns, seed=3)
    assert problem == problem.lower()
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    columns = [_chain(init, bottom, "on") for bottom in re.findall(r"\(bottomcol (\S+)\)", init)]
    talon = _chain(init, re.findall(r"\(bottomtalon (\S+)\)", init)[0], "ontalon")
    assert sorted(map(len, columns)) == list(range(1, num_columns + 1))
    assert set(re.findall(r"\(clear (\S+)\)", init)) == {column[-1] for column in columns}
    assert set(re.findall(r"\(faceup (\S+)\)", init)) == {column[-1] for column in columns}
    assert re.findall(r"\(toptalon (\S+)\)", init) == [talon[-1]]
    assert re.findall(r"\(talonplayable (\S+)\)", init) == [talon[2]]
    dealt = [card for column in columns for card in column] + talon
    cards = {card for card, value in re.findall(r"\(value (\S+) n(\d+)\)", init) if value != "0"}
    assert len(dealt) == len(set(dealt)) == 4 * num_cards and set(dealt) == cards
    assert len(re.findall(r"\(home \S+\)", problem.split("(:goal", 1)[1])) == 4


def test_thoughtful_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-n", "11", "-c", "6", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(11, 6, seed=9)


@pytest.mark.parametrize(
    "parameter,value", [("num_cards", 0), ("num_cards", 14), ("num_columns", 0), ("num_columns", 6)]
)
def test_thoughtful_rejects_invalid_parameters(parameter: str, value: int) -> None:
    parameters: dict[str, Any] = {"num_cards": 5, "num_columns": 4}
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
