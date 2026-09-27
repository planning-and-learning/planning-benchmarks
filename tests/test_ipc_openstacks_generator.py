import re
import statistics
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.openstacks import generator
from pypddl_datasets.generators.classical.ipc.openstacks.generator import main, make_problem

HERE = Path(generator.__file__).parent


def includes(problem):
    return [(int(o), int(p)) for o, p in re.findall(r"\(includes o(\d+) p(\d+)\)", problem)]


@pytest.mark.parametrize("model", ["clustered", "uniform"])
@pytest.mark.parametrize("seed", range(4))
def test_every_order_and_product_is_used_once_at_least(model, seed):
    problem = make_problem(12, 9, 30, seed=seed, model=model)
    assert problem == make_problem(12, 9, 30, seed=seed, model=model)
    pairs = includes(problem)
    assert {o for o, _ in pairs} == set(range(1, 10)) and {p for _, p in pairs} == set(range(1, 13))
    assert re.findall(r"\(shipped o(\d+)\)", problem) == [str(i) for i in range(1, 10)]
    assert len(re.findall(r"\(next-count ", problem)) == 12 and "(stacks-avail n0)" in problem


def test_shuffle_breaks_the_diagonal_clustering():
    distance = lambda **kw: statistics.mean(abs(o - p) for s in range(10) for o, p in includes(make_problem(60, 60, 20, seed=s, **kw)))
    assert distance(shuffle=False) < 16 < 18 < distance()  # shuffled: about n/3 = 20


def test_uniform_model_density_is_the_percentage():
    density = statistics.mean(len(includes(make_problem(40, 40, 54, seed=s, model="uniform"))) / 1600 for s in range(5))
    assert 0.5 < density < 0.58


@pytest.mark.parametrize("style,domain", [("08", "domain.pddl"), ("06", "domain_openstacks06.pddl")])
def test_output_parses_strictly(style, domain, tmp_path):
    problem = make_problem(8, 7, 25, seed=2, style=style)
    assert ("(machine-available)" in problem) == (style == "06") and ("total-cost" in problem) == (style == "08")
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(HERE / domain, options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_matches_make_problem(capsys):
    assert main(["6", "5", "40", "-s", "3", "--style", "06", "--model", "uniform"]) == 0
    assert capsys.readouterr().out == make_problem(6, 5, 40, seed=3, style="06", model="uniform")


@pytest.mark.parametrize("parameter,value", [("num_products", 0), ("num_orders", 0), ("density", 101), ("style", "11"), ("model", "x")])
def test_rejects_invalid_parameters(parameter, value):
    parameters = dict(num_products=3, num_orders=3, density=20)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
