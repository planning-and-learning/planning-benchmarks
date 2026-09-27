import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.mprime.generator import make_problem as make_strips
from pypddl_datasets.generators.numeric.ipc.mprime import generator
from pypddl_datasets.generators.numeric.ipc.mprime.generator import main, make_problem


@pytest.mark.parametrize("args", [(4, 2, 2, 6, 4, 1), (10, 3, 6, 6, 3, 3), (18, 6, 12, 8, 4, 3)])
def test_numeric_mprime_translates_the_strips_levels(args: tuple[int, int, int, int, int, int], tmp_path: Path) -> None:
    problem = make_problem(*args, seed=6)
    strips = make_strips(*args, seed=6)
    init = strips.split("(:init", 1)[1]

    def chain(relation: str, kind: str) -> dict[str, int]:
        successor = dict(re.findall(rf"\({relation} ([^\s()]+) ([^\s()]+)\)", init))
        current = next(x for x in re.findall(rf"\({kind} ([^\s()]+)\)", init) if x not in successor.values())
        order: dict[str, int] = {}
        while current:
            order[current] = len(order)
            current = successor.get(current)
        return order

    fuel, space = chain("attacks", "province"), chain("orbits", "planet")
    locale = {f: int(v) for f, v in re.findall(r"\(= \(locale ([^\s()]+)\) (\d+)\)", problem)}
    harmony = {v: int(n) for v, n in re.findall(r"\(= \(harmony ([^\s()]+)\) (\d+)\)", problem)}
    assert locale == {f: fuel[p] for f, p in re.findall(r"\(locale ([^\s()]+) ([^\s()]+)\)", init)}
    assert harmony == {v: space[p] for v, p in re.findall(r"\(harmony ([^\s()]+) ([^\s()]+)\)", init)}
    for relation in ("eats", "craves"):
        assert re.findall(rf"\({relation} [^\s()]+ [^\s()]+\)", problem) == re.findall(
            rf"\({relation} [^\s()]+ [^\s()]+\)", strips
        )
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cli(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-l", "5", "-v", "2", "-c", "3", "-f", "5", "-p", "3", "-g", "2", "-s", "1"]) == 0
    assert capsys.readouterr().out == make_problem(5, 2, 3, 5, 3, 2, seed=1)
