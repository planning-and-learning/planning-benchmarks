import re
from pathlib import Path

import pytest

from pypddl_datasets.generators.classical.transport_fuel import generator


@pytest.mark.parametrize("seed", range(5))
def test_default_fuel_covers_constructive_route(seed):
    problem = generator.make_problem(2, 2, 4, capacity=1, seed=seed)
    assert problem == generator.make_problem(2, 2, 4, capacity=1, seed=seed)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    starts = dict(re.findall(r"\(at (\w+) (\w+)\)", init))
    goals = re.findall(r"\(at (\w+) (\w+)\)", goal)
    current = starts["t0"]
    expected_fuel = 0
    for package, destination in goals:
        # On the two-location road, every change of location is exactly one drive.
        expected_fuel += int(current != starts[package]) + int(starts[package] != destination)
        current = destination
    assert set(re.findall(r"\(fuel (\w+) (\w+)\)", init)) == {
        ("t0", f"fuel{expected_fuel}"), ("t1", f"fuel{expected_fuel}")
    }
    assert problem == generator.make_problem(2, 2, 4, capacity=1, fuel=expected_fuel, seed=seed)


@pytest.mark.parametrize("fuel", [0, 1, 3])
def test_drive_consumes_one_fuel_and_cannot_refuel(fuel):
    domain = Path(generator.__file__).with_name("domain.pddl").read_text()
    drive = domain.split("(:action drive", 1)[1].split("(:action pick-up", 1)[0]
    preconditions, effects = drive.split(":precondition", 1)[1].split(":effect", 1)
    problem = generator.make_problem(2, 1, 1, fuel=fuel, seed=0)
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    state = set(re.findall(r"\([^()]+\)", init))
    start = re.search(r"\(at t0 (\w+)\)", init).group(1)
    target = "l1" if start == "l0" else "l0"
    successors = []
    # Ground the small STRIPS drive schema against the generated fuel chain.
    for before in range(fuel + 1):
        for after in range(fuel + 1):
            grounded_pre, grounded_eff = preconditions, effects
            for variable, value in {
                "?v": "t0", "?l1": start, "?l2": target,
                "?fuel-before": f"fuel{before}", "?fuel-after": f"fuel{after}",
            }.items():
                grounded_pre = grounded_pre.replace(variable, value)
                grounded_eff = grounded_eff.replace(variable, value)
            required = set(re.findall(r"\([^()]+\)", grounded_pre))
            if required <= state:
                deleted = set(re.findall(r"\(not\s+(\([^()]+\))\)", grounded_eff))
                additions = re.sub(r"\(not\s+\([^()]+\)\)", "", grounded_eff)
                successors.append((state - deleted) | set(re.findall(r"\([^()]+\)", additions)))
    assert len(successors) == int(fuel > 0)
    if fuel:
        assert {fact for fact in successors[0] if fact.startswith("(fuel ")} == {f"(fuel t0 fuel{fuel - 1})"}
        assert f"(at t0 {target})" in successors[0]
        assert f"(at t0 {start})" not in successors[0]
    assert re.findall(r"\(:action (\S+)", domain) == ["drive", "pick-up", "drop"]


def test_fuel_cli_matches_make_problem(capsys):
    assert generator.main(["-l", "4", "-t", "2", "-p", "3", "-c", "1", "-e", "1", "-f", "2", "-s", "7"]) == 0
    assert capsys.readouterr().out == generator.make_problem(4, 2, 3, capacity=1, extra_edges=1, fuel=2, seed=7)


@pytest.mark.parametrize("fuel", [-1, 1.5, True])
def test_invalid_fuel_is_rejected(fuel):
    with pytest.raises(ValueError, match="fuel"):
        generator.make_problem(2, 1, 1, fuel=fuel)
