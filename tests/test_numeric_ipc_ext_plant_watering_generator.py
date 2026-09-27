import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.ext_plant_watering import generator
from pypddl_datasets.generators.numeric.ipc.ext_plant_watering.generator import main, make_problem


@pytest.mark.parametrize("size,plants,agents,taps", [(3, 2, 2, 1), (10, 5, 2, 1), (15, 19, 3, 2)])
def test_plant_watering_reserve_covers_demand(size, plants, agents, taps):
    problem = make_problem(size, plants, agents, taps, seed=5)
    assert problem == make_problem(size, plants, agents, taps, seed=5)
    init, goal = problem.split("(:goal", 1)
    demand = [int(v) for v in re.findall(r"\(= \(poured \S+\) (\d+)\)", goal)]
    assert len(demand) == plants and all(1 <= d <= 10 for d in demand)
    reserve = int(re.search(r"\(= \(water_reserve\) (\d+)\)", init).group(1))
    assert reserve == sum(demand) + sum(demand) // 10
    cells = list(zip(re.findall(r"\(= \(x \S+\) (\d+)\)", init), re.findall(r"\(= \(y \S+\) (\d+)\)", init)))
    assert len(cells) == plants + agents + taps == len(set(cells))
    assert "(= (total_poured) (total_loaded))" in goal


def test_plant_watering_parses_strictly(tmp_path):
    (tmp_path / "p.pddl").write_text(make_problem(8, 6, seed=2))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_plant_watering_cli_and_validation(capsys):
    assert main(["6", "4", "-s", "1"]) == 0
    assert capsys.readouterr().out == make_problem(6, 4, seed=1)
    with pytest.raises(ValueError, match="size is too small"):
        make_problem(1, 1)
    with pytest.raises(ValueError, match="num_plants"):
        make_problem(5, 0)
