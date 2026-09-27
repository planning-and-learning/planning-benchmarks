import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.autoscale.satellite.generator import main as main_autoscale
from pypddl_datasets.generators.classical.autoscale.satellite.generator import make_problem as make_autoscale
from pypddl_datasets.generators.classical.ipc.satellite import generator as ipc_generator
from pypddl_datasets.generators.classical.ipc.satellite.generator import main, make_problem


GENERATORS = Path(ipc_generator.__file__).parents[2]


def _parse(problem: str, domain_file: Path, tmp_path: Path) -> None:
    (tmp_path / "p.pddl").write_text(problem, encoding="utf-8")
    options = ParserOptions()
    options.strict = True
    Parser(domain_file, options).parse_task(tmp_path / "p.pddl")


@pytest.mark.parametrize("args", [(1, 1, 1, 1, 1), (2, 3, 3, 12, 5), (6, 3, 9, 20, 30)])
@pytest.mark.parametrize("seed", range(3))
def test_every_goal_is_achievable(args: tuple[int, int, int, int, int], seed: int) -> None:
    problem = make_autoscale(*args, seed=seed)
    assert problem == make_autoscale(*args, seed=seed)
    num_satellites, max_instruments, num_modes, num_targets, _ = args
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)

    on_board = re.findall(r"\(on_board (\w+) (\w+)\)", init)
    per_satellite: dict[str, int] = {}
    for _, satellite in on_board:
        per_satellite[satellite] = per_satellite.get(satellite, 0) + 1
    assert set(per_satellite) == {f"satellite{i}" for i in range(num_satellites)}
    assert all(1 <= count <= max_instruments for count in per_satellite.values())

    instruments = {instrument for instrument, _ in on_board}
    calibrated = {instrument for instrument, _ in re.findall(r"\(calibration_target (\w+) (\w+)\)", init)}
    assert calibrated == instruments
    supports = re.findall(r"\(supports (\w+) (\w+)\)", init)
    modes = set(re.findall(r"(\w+) - mode", problem))
    assert len(modes) == num_modes and {mode for _, mode in supports} == modes  # Autoscale patch

    # Satellites can turn anywhere, so a supported mode on a calibratable instrument suffices.
    images = re.findall(r"\(have_image (\w+) (\w+)\)", goal)
    assert {observation for observation, _ in images} == {
        name for name in re.findall(r"(\w+) - direction", problem) if int(re.sub(r"\D", "", name)) >= num_targets
    }
    assert {mode for _, mode in images} <= modes
    assert len(re.findall(r"\(pointing satellite\d+ \w+\)", init)) == num_satellites


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    argv = ["--num-satellites", "2", "--num-modes", "3", "--num-targets", "6", "--num-observations", "4", "--seed", "7"]
    assert main(argv) == 0
    assert capsys.readouterr().out == make_problem(2, 3, 3, 6, 4, seed=7)
    assert main_autoscale(argv) == 0
    assert capsys.readouterr().out == make_autoscale(2, 3, 3, 6, 4, seed=7)


@pytest.mark.parametrize(
    "parameter", ["num_satellites", "max_instruments", "num_modes", "num_targets", "num_observations"]
)
def test_rejects_invalid_parameters(parameter: str) -> None:
    parameters: dict[str, Any] = {
        "num_satellites": 1,
        "max_instruments": 1,
        "num_modes": 1,
        "num_targets": 1,
        "num_observations": 1,
    }
    parameters[parameter] = 0
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)


@pytest.mark.parametrize("seed", range(3))
def test_satellite_ipc_encoding_parses(seed: int, tmp_path: Path) -> None:
    untyped = make_problem(3, 3, 4, 8, 6, seed=seed)
    assert (
        " - " not in untyped
        and "(satellite satellite0)" in untyped
        and "(mode " in untyped
        and "(direction " in untyped
    )
    _parse(untyped, GENERATORS / "ipc/satellite/domain.pddl", tmp_path)
    _parse(make_autoscale(3, 3, 4, 8, 6, seed=seed), GENERATORS / "autoscale/satellite/domain.pddl", tmp_path)


def test_satellite_unpatched_observation_goal_rate_is_nine_in_ten() -> None:
    observations = goals = 0
    for seed in range(200):
        problem = make_problem(1, 3, 3, 3, 10, seed=seed)
        goals += len({o for o, _ in re.findall(r"\(have_image (\w+) (\w+)\)", problem.split("(:goal", 1)[1])})
        observations += 10
    assert 0.87 < goals / observations < 0.93
