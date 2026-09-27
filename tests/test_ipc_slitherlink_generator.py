import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.slitherlink import generator
from pypddl_datasets.generators.classical.ipc.slitherlink.generator import (  # pylint: disable=protected-access
    _Grid,  # pyright: ignore[reportPrivateUsage]  # the tests call the solver directly
    main,
    make_problem,
    make_puzzle,
    to_pddl,
)

REFERENCE = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks/slitherlink-opt23-adl"


def _match(pattern: str, text: str, flags: int = 0) -> re.Match[str]:
    match = re.search(pattern, text, flags)
    assert match is not None, pattern
    return match


@pytest.mark.parametrize("rows,cols", [(1, 2), (3, 3), (3, 4), (5, 6)])
@pytest.mark.parametrize("seed", range(3))
def test_puzzles_have_a_unique_solution(rows: int, cols: int, seed: int) -> None:
    clues = make_puzzle(rows, cols, seed=seed)
    assert clues == make_puzzle(rows, cols, seed=seed)
    assert all(0 <= v <= 4 for v in clues.values())
    assert _Grid(rows, cols).count_solutions(clues, limit=3) == 1


def test_grid_without_unique_region_is_rejected() -> None:
    # on 2x2 the growth rule always yields the ambiguous L-tromino
    with pytest.raises(ValueError, match="2x2"):
        make_puzzle(2, 2, seed=0)


def test_solver_counts_both_loops_of_an_ambiguous_puzzle() -> None:
    # the L-tromino and its complement satisfy the same clues
    assert _Grid(2, 2).count_solutions({(0, 0): 2, (0, 1): 3, (1, 0): 3, (1, 1): 2}, limit=5) == 2


def test_writer_reproduces_an_ipc_task() -> None:
    text = (REFERENCE / "p01.pddl").read_text()
    rows, cols = map(int, _match(r"gen (\d+) (\d+) ", text).groups())
    lines = [line[4:] for line in text.splitlines()[2 : 2 + rows]]
    clues = {(r, c): int(ch) for r, line in enumerate(lines) for c, ch in enumerate(line[:cols]) if ch.isdigit()}

    def facts(t: str) -> list[str]:
        t = re.sub(r";[^\n]*", "", t).lower()
        return sorted(re.findall(r"\([^()]+\)", t.split("(:init", 1)[1]))

    assert facts(to_pddl(rows, cols, clues, "x")) == facts(text)


def test_output_parses_strictly(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    for rows, cols in ((2, 3), (4, 5)):
        (tmp_path / "p.pddl").write_text(make_problem(rows, cols, seed=2))
        Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["3", "4", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(3, 4, seed=9)


@pytest.mark.parametrize("parameter,value", [("rows", 0), ("cols", 0), ("rows", 2.5), ("cols", True)])
def test_rejects_invalid_parameters(parameter: str, value: bool | float) -> None:
    parameters: dict[str, Any] = {"rows": 3, "cols": 3}
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
