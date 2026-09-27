import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.rovers.generator import make_problem as make_strips
from pypddl_datasets.generators.numeric.ipc.rover import generator
from pypddl_datasets.generators.numeric.ipc.rover.generator import main, make_problem


@pytest.mark.parametrize("args", [(1, 4, 2, 2, 3), (4, 10, 5, 4, 8), (8, 25, 8, 6, 20)])
def test_numeric_rover_extends_the_strips_task(args, tmp_path):
    problem = make_problem(*args, seed=3)
    assert problem == make_problem(*args, seed=3)
    strips = make_strips(*args, seed=3)
    assert re.sub(r"\(in (rover\d+) ", r"(at \1 ", problem.split("(:goal")[0]).count("(at rover") == strips.count("(at rover")
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    sunny = set(re.findall(r"\(in_sun (\w+)\)", init))
    sources: dict[str, set[str]] = {}
    for rover, source in re.findall(r"\(can_traverse (\w+) (\w+) \w+\)", init):
        sources.setdefault(rover, set()).add(source)
    assert all(sources[r] & sunny for r in sources)  # makeChargeable
    assert set(re.findall(r"\(= \(energy (\w+)\) (\d+)\)", init)) == {(f"rover{i}", "50") for i in range(args[0])}
    assert "(= (recharges) 0)" in init and problem.rstrip().endswith("(:metric minimize (recharges))\n)")
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_and_validation(capsys):
    assert main(["-r", "2", "-w", "6", "-o", "3", "-c", "2", "-g", "4", "-s", "7"]) == 0
    assert capsys.readouterr().out == make_problem(2, 6, 3, 2, 4, seed=7)
    with pytest.raises(ValueError, match="num_waypoints"):
        make_problem(1, 1, 1, 1, 1)
