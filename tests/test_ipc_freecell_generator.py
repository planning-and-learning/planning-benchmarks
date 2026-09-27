import re

import pytest

from pypddl_datasets.generators.classical.ipc.freecell.generator import main, make_problem


def _columns(problem):
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    above = {lower: upper for upper, lower in re.findall(r"\(on (\S+) (\S+)\)", init)}
    columns = []
    for bottom in re.findall(r"\(bottomcol (\S+)\)", init):
        column = [bottom]
        while column[-1] in above:
            column.append(above[column[-1]])
        columns.append(column)
    return init, columns


@pytest.mark.parametrize(
    "num_cards,num_cells,num_columns,style",
    [(1, 4, 8, "ipc2000"), (5, 4, 8, "ipc2000"), (13, 4, 8, "ipc2000"), (2, 2, 4, "ipc2002"), (9, 4, 7, "ipc2002")],
)
def test_freecell_deals_every_card_once(num_cards, num_cells, num_columns, style):
    problem = make_problem(num_cards, num_cells, num_columns, seed=3, style=style)
    assert problem == make_problem(num_cards, num_cells, num_columns, seed=3, style=style)
    assert problem == problem.lower()
    init, columns = _columns(problem)
    dealt = [card for column in columns for card in column]
    cards = {card for card, value in re.findall(r"\(value (\S+) n(\d+)\)", init) if value != "0"}
    assert len(dealt) == len(set(dealt)) == 4 * num_cards and set(dealt) == cards
    assert set(re.findall(r"\(clear (\S+)\)", init)) == {column[-1] for column in columns}
    assert re.findall(r"\(cellspace n(\d+)\)", init) == [str(num_cells)]
    assert re.findall(r"\(colspace n(\d+)\)", init) == [str(num_columns - len(columns))]
    heights = sorted(map(len, columns))
    if style == "ipc2002":
        assert heights[-1] - heights[0] <= 1
    goal = problem.split("(:goal", 1)[1]
    assert len(re.findall(r"\(home \S+\)", goal)) == 4


def test_freecell_canstack_links_opposite_colours_one_rank_up():
    init, _ = _columns(make_problem(3, seed=0))
    assert set(re.findall(r"\(canstack (\S+) (\S+)\)", init)) == {
        (f"{low}{rank}", f"{high}{next_rank}")
        for rank, next_rank in (("a", "2"), ("2", "3"))
        for low, high in [("c", "d"), ("c", "h"), ("s", "d"), ("s", "h"), ("d", "c"), ("d", "s"), ("h", "c"), ("h", "s")]
    }


def test_freecell_cli_matches_make_problem(capsys):
    assert main(["-n", "4", "-f", "2", "-c", "5", "-s", "9", "--style", "ipc2002"]) == 0
    assert capsys.readouterr().out == make_problem(4, 2, 5, seed=9, style="ipc2002")


@pytest.mark.parametrize(
    "parameter,value", [("num_cards", 0), ("num_cards", 14), ("num_cells", -1), ("num_columns", 0), ("style", "ipc2004")]
)
def test_freecell_rejects_invalid_parameters(parameter, value):
    parameters = dict(num_cards=3, num_cells=4, num_columns=8, style="ipc2000")
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
