import re

import pytest

from pypddl_datasets.generators.classical.ipc.spider.generator import main, make_problem


@pytest.mark.parametrize(
    "decks,suits,values,piles,deals", [(1, 4, 3, 3, 2), (2, 2, 9, 6, 2), (4, 1, 12, 8, 2), (1, 1, 4, 2, 0)]
)
def test_spider_places_every_card_once_and_movable_runs_are_on_top(decks, suits, values, piles, deals):
    problem = make_problem(decks, suits, values, piles, deals, seed=7)
    assert problem == make_problem(decks, suits, values, piles, deals, seed=7)
    assert problem == problem.lower()
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    on = re.findall(r"\(on (\S+) (\S+)\)", init)
    cards = {f"card-d{d}-s{s}-v{v}" for d in range(decks) for s in range(suits) for v in range(values)}
    assert sorted(upper for upper, _ in on) == sorted(cards)  # every card sits on exactly one thing
    in_play = set(re.findall(r"\(in-play (\S+)\)", init))
    assert len(in_play) == len(cards) - deals * piles
    assert len(re.findall(r"\(to-deal ", init)) == deals * piles
    heights = [len(re.findall(rf"\(part-of-tableau card-\S+ pile-{i}\)", init)) for i in range(piles)]
    assert max(heights) - min(heights) <= 1 and heights == sorted(heights, reverse=True)
    above = {lower: upper for upper, lower in on}
    for movable in re.findall(r"\(movable (\S+)\)", init):
        card = movable
        while card in above:  # movable cards form a same-suit run ending at the top
            (_, s1, v1), (_, s2, v2) = (re.findall(r"\d+", c) for c in (card, above[card]))
            assert s1 == s2 and int(v1) == int(v2) + 1
            card = above[card]
    assert len(re.findall(r"\(on \S+ discard\)", goal)) == len(cards)
    assert "(= (total-cost) 0)" in init and "(:metric minimize (total-cost))" in problem


def test_spider_cli_matches_make_problem(capsys):
    assert main(["-d", "2", "-u", "2", "-v", "5", "-p", "4", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(2, 2, 5, 4, seed=3)


@pytest.mark.parametrize(
    "parameter,value", [("num_decks", 0), ("num_suits", 0), ("num_values", 0), ("num_piles", 0), ("num_deals", -1), ("num_piles", 5)]
)
def test_spider_rejects_invalid_parameters(parameter, value):
    parameters = dict(num_decks=1, num_suits=4, num_values=3, num_piles=3, num_deals=2)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
