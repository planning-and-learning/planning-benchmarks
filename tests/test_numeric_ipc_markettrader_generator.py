import re
from collections import deque
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.markettrader import generator
from pypddl_datasets.generators.numeric.ipc.markettrader.generator import (  # pylint: disable=protected-access
    _profitable,  # pyright: ignore[reportPrivateUsage]  # the test applies the generator's filter to the references
    main,
    make_problem,
)

Roads = dict[tuple[str, str], float]
OnSale = dict[str, dict[str, int]]

REFERENCE = Path(__file__).resolve().parents[1] / "data/numeric/ipc2023/markettrader"


def parse(text: str) -> tuple[list[str], Roads, Roads, OnSale]:
    markets = text.split("(:objects")[1].split("- market")[0].split()
    roads = {(a, b): float(c) for a, b, c in re.findall(r"drive-cost\s+(\S+)\s+(\S+)\s*\)\s*([\d.]+)", text)}
    prices = {(g, m): float(p) for g, m, p in re.findall(r"\(price (\S+) (\S+)\)\s+([\d.]+)", text)}
    on_sale: OnSale = {}
    for g, m, p in re.findall(r"\(on-sale (\S+) (\S+)\)\s+(\d+)", text):  # on-sale amounts are integers
        on_sale.setdefault(g, {})[m] = int(p)
    return markets, roads, prices, on_sale


@pytest.mark.parametrize("num_markets", [2, 3, 5, 8])
@pytest.mark.parametrize("seed", range(3))
def test_road_map_is_connected_symmetric_and_profitable(num_markets: int, seed: int) -> None:
    problem = make_problem(num_markets, seed)
    assert problem == make_problem(num_markets, seed)
    markets, roads, prices, on_sale = parse(problem)
    assert len(markets) == num_markets and all(roads[b, a] == c and 0.8 <= c <= 7.0 for (a, b), c in roads.items())
    assert set(re.findall(r"\(can-drive (\S+) (\S+)\)", problem)) == set(roads)
    reached, frontier = {markets[0]}, deque([markets[0]])
    while frontier:
        here = frontier.popleft()
        for a, b in roads:
            if a == here and b not in reached:
                reached.add(b)
                frontier.append(b)
    assert reached == set(markets)
    assert _profitable(roads, prices, on_sale)
    assert f"(at camel0 {markets[-1]})" in problem and "(>= (cash) 1000)" in problem


def test_reference_tasks_pass_the_profitability_filter() -> None:
    for path in REFERENCE.glob("pfile*.pddl"):
        _, roads, prices, on_sale = parse(path.read_text())
        assert _profitable(roads, prices, on_sale)


def test_parses_strictly_and_cli(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (tmp_path / "p.pddl").write_text(make_problem(4, 2))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")
    assert main(["-m", "4", "-s", "2"]) == 0
    assert capsys.readouterr().out == make_problem(4, 2)
    with pytest.raises(ValueError, match="num_markets"):
        make_problem(1)
