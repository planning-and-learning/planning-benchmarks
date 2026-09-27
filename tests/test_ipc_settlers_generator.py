import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.settlers import generator
from pypddl_datasets.generators.classical.ipc.settlers.generator import MAPS, main, make_problem

DATA = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


def parts(text: str):
    text = re.sub(r";[^\n]*", "", text).lower()
    head, rest = text.split("(:init", 1)
    init, goal = rest.split("(:goal", 1)
    objects = set(head.split("(:objects", 1)[1].replace(")", " ").split()) - {"-"}
    return objects, set(re.findall(r"\([^()]+\)", init)), set(re.findall(r"\([^()]+\)", goal))


@pytest.mark.parametrize(
    "path", sorted(DATA.glob("settlers-*18-adl/p*.pddl")), ids=lambda p: f"{p.parent.name}/{p.name}"
)
def test_reproduces_ipc_task_from_its_header(path: Path) -> None:
    text = path.read_text()
    m = re.search(r"seed=(\d+), locations=(\d+), edges=(\d+), seas=(\d+).*goals=(\d+).*C=([\d.]+)", text)
    assert m is not None
    seed, locations, edges, seas, goals = (int(m[i]) for i in range(1, 6))
    track = "opt" if float(m[6]) < 1.3 else "sat"
    assert parts(make_problem(locations, edges, seas, goals, seed, track)) == parts(text)


@pytest.mark.parametrize("seed", range(20))
def test_island_maps_are_connected_and_stocked(seed: int) -> None:
    problem = make_problem(*MAPS["huge"], 8, seed=seed)
    assert problem == make_problem(*MAPS["huge"], 8, seed=seed) and problem == problem.lower()
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    edges = re.findall(r"\(connected-by-(?:land|sea) p(\d+) p(\d+)\)", init)
    reached, frontier = {"0"}, ["0"]
    while frontier:
        x = frontier.pop()
        for a, b in edges:
            if a == x and b not in reached:
                reached.add(b)
                frontier.append(b)
    assert reached == {str(i) for i in range(16)}
    stock = dict(re.findall(r"\(available-(stone|timber|ore) p\d+ \wl([1-9]\d*)\)", init))
    assert set(stock) == {"stone", "timber", "ore"}


def test_parses_strictly(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    for track in ("opt", "sat"):
        (tmp_path / f"{track}.pddl").write_text(make_problem(*MAPS["large"], 6, seed=4, track=track))
        Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / f"{track}.pddl")


def test_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--map", "small", "-g", "4", "-s", "3", "-t", "opt"]) == 0
    assert capsys.readouterr().out == make_problem(5, 5, 1, 4, 3, "opt")
    with pytest.raises(ValueError, match="track"):
        make_problem(3, 2, 0, 1, track="agile")
    with pytest.raises(ValueError, match="num_goals"):
        make_problem(3, 2, 0, 0)
