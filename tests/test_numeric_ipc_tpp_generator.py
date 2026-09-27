import math
import re
from collections import Counter
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.tpp import generator
from pypddl_datasets.generators.numeric.ipc.tpp.generator import main, make_problem


@pytest.mark.parametrize("markets,goods,depots,trucks", [(1, 1, 1, 1), (5, 4, 1, 1), (40, 39, 1, 1), (6, 3, 2, 2)])
def test_tpp_supply_covers_every_request(markets, goods, depots, trucks, tmp_path):
    problem = make_problem(markets, goods, seed=2, num_depots=depots, num_trucks=trucks)
    assert problem == make_problem(markets, goods, seed=2, num_depots=depots, num_trucks=trucks)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    supply: Counter[str] = Counter()
    for g, m, q in re.findall(r"\(= \(on-sale (\w+) (\w+)\) (\d+)\)", init):
        supply[g] += int(q)
        assert int(q) == 0 or 1 <= int(re.search(rf"\(= \(price {g} {m}\) (\d+)\)", init).group(1)) <= 50
    requests = {g: int(r) for g, r in re.findall(r"\(= \(request (\w+)\) (\d+)\)", init)}
    assert len(requests) == goods and all(1 <= r <= supply[g] for g, r in requests.items())
    costs = {(a, b): float(c) for a, b, c in re.findall(r"\(= \(drive-cost (\w+) (\w+)\) ([\d.]+)\)", init)}
    places = markets + depots
    assert len(costs) == places * (places - 1) and all(costs[b, a] == c <= 1000 * math.sqrt(2) for (a, b), c in costs.items())
    assert len(re.findall(r"\(loc truck\d+ depot0\)", goal)) == trucks
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_and_validation(capsys):
    assert main(["-m", "5", "-g", "3", "-s", "4"]) == 0
    assert capsys.readouterr().out == make_problem(5, 3, seed=4)
    with pytest.raises(ValueError, match="num_goods"):
        make_problem(3, 0)
