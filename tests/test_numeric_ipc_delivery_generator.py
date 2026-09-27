import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.delivery import generator
from pypddl_datasets.generators.numeric.ipc.delivery.generator import main, make_problem


def reachable(doors: list[tuple[str, str]], source: str) -> set[str]:
    seen, frontier = {source}, [source]
    while frontier:
        current = frontier.pop()
        for a, b in doors:
            if a == current and b not in seen:
                seen.add(b)
                frontier.append(b)
    return seen


@pytest.mark.parametrize("directed", [False, True])
@pytest.mark.parametrize("rooms,extra", [(1, 0), (3, 1), (6, 2)])
def test_delivery_maps_are_strongly_connected(rooms: int, extra: int, directed: bool) -> None:
    problem = make_problem(rooms, 8, 2, 3, 3, directed=directed, extra_doors=extra, seed=4)
    assert problem == make_problem(rooms, 8, 2, 3, 3, directed=directed, extra_doors=extra, seed=4)
    init, goal = problem.split("(:goal", 1)
    doors = re.findall(r"\(door (\S+) (\S+)\)", init)
    names = {f"room{c}" for c in "abcdef"[:rooms]}
    assert all(reachable(doors, r) == names for r in names)
    assert directed or all((b, a) in doors for a, b in doors)
    weights = [int(w) for w in re.findall(r"\(= \(weight \S+\) (\d+)\)", init)]
    limits = {int(v) for v in re.findall(r"\(= \(load_limit \S+\) (\d+)\)", init)}
    assert len(weights) == 8 and max(weights) <= min(limits)  # every item can be carried
    assert set(re.findall(r"\(at-bot \S+ (\S+)\)", init)) == {"rooma"}
    assert len(re.findall(r"\(mount ", init)) == 6 and len(re.findall(r"\(at (item\S+) \S+\)", goal)) == 8


def test_delivery_parses_strictly(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    for k, (directed, extra_doors) in enumerate([(False, 0), (True, 2)]):
        (tmp_path / f"p{k}.pddl").write_text(make_problem(5, 10, seed=k, directed=directed, extra_doors=extra_doors))
        Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / f"p{k}.pddl")


def test_delivery_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["4", "6", "--directed", "-e", "1", "-s", "2"]) == 0
    assert capsys.readouterr().out == make_problem(4, 6, directed=True, extra_doors=1, seed=2)
    with pytest.raises(ValueError, match="load_limit"):
        make_problem(3, 3, max_weight=4, load_limit=3)
    with pytest.raises(ValueError, match="extra_doors"):
        make_problem(2, 3, extra_doors=1)
