import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.recharging_robots import generator
from pypddl_datasets.generators.classical.ipc.recharging_robots.generator import main, make_problem

CASES = [
    dict(kind="covers", num_robots=2, num_obstacles=2, num_viewpoints=15, min_cover=2, num_areas=1),
    dict(kind="covers", num_robots=4, num_obstacles=5, num_viewpoints=15, min_cover=2, num_areas=3),
    dict(kind="single-source-move-to-locations", num_robots=3, num_obstacles=5, num_viewpoints=10),
    dict(kind="single-source-move-to-locations", num_robots=4, num_obstacles=5, num_viewpoints=15, move_from_source=True),
]


def _graph(problem):
    edges = re.findall(r"\(connected (\S+) (\S+)\)", problem)
    adj = {}
    for a, b in edges:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    return adj


def _dist(adj, source):
    dist, frontier = {source: 0}, [source]
    while frontier:
        nxt = []
        for u in frontier:
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    nxt.append(v)
        frontier = nxt
    return dist


@pytest.mark.parametrize("case", CASES)
@pytest.mark.parametrize("seed", range(3))
def test_tasks_are_connected_and_charged_enough(case, seed):
    problem = make_problem(**case, seed=seed)
    assert problem == make_problem(**case, seed=seed) and problem == problem.lower()
    objects = problem.split("(:objects", 1)[1].split("(:init", 1)[0]
    locations = objects.split(" - location", 1)[0].split()
    assert len(locations) == 4 * case["num_obstacles"] + case["num_viewpoints"]
    adj = _graph(problem)
    assert set(adj) == set(locations) and len(_dist(adj, locations[0])) == len(locations)

    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    at = dict(re.findall(r"\(at (robot-\d+) (\S+)\)", init))
    battery = {r: int(b) for r, b in re.findall(r"\(battery (robot-\d+) battery-(\d+)\)", init)}
    assert len(at) == len(battery) == case["num_robots"]
    levels = objects.split(" - robot", 1)[1].split(" - battery-level", 1)[0].split()
    assert len(levels) == sum(battery.values()) + 1
    if case["kind"] == "covers":
        configs = re.findall(r"\(config-fullfilled (config-\d+)\)", goal)
        assert len(configs) == case["num_areas"]
        guarded = re.findall(r"\(guard-config (config-\d+) (\S+)\)", init)
        assert {c for c, _ in guarded} == set(configs)
        assert not set(at.values()) & {loc for _, loc in guarded}  # robots start outside the areas
    else:
        targets = dict(re.findall(r"\(at (robot-\d+) (\S+)\)", goal))
        assert len(set(targets.values())) == case["num_robots"]
        # total charge covers moving every robot to its target
        needed = sum(_dist(adj, at[r])[t] for r, t in targets.items())
        assert sum(battery.values()) >= needed
    assert "(:metric minimize (total-cost))" in problem


def test_output_parses_strictly(tmp_path):
    options = ParserOptions()
    options.strict = True
    for i, case in enumerate(CASES):
        (tmp_path / f"p{i}.pddl").write_text(make_problem(**case, seed=1))
        Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / f"p{i}.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_matches_make_problem(capsys):
    assert main(["covers", "3", "2", "10", "--min-cover", "2", "--num-areas", "2", "-s", "5"]) == 0
    assert capsys.readouterr().out == make_problem("covers", 3, 2, 10, min_cover=2, num_areas=2, seed=5)


@pytest.mark.parametrize(
    "parameter,value",
    [("kind", "patrol"), ("num_robots", 0), ("num_obstacles", -1), ("min_cover", 0), ("num_areas", 0), ("charge_multiplier", 0.5)],
)
def test_rejects_invalid_parameters(parameter, value):
    parameters = dict(kind="covers", num_robots=2, num_obstacles=2, num_viewpoints=10)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
