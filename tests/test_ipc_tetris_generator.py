import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.tetris import generator
from pypddl_datasets.generators.classical.ipc.tetris.generator import main, make_problem


@pytest.mark.parametrize("num_rows,seed", [(4, 0), (8, 9), (14, 5)])
def test_tetris_pieces_are_disjoint_in_the_upper_half(num_rows: int, seed: int) -> None:
    problem = make_problem(num_rows, seed)
    assert problem == make_problem(num_rows, seed) == problem.lower()
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    cells = [tuple(map(int, cell)) for cell in re.findall(r"f(\d+)-(\d+)f", problem.split("(:init")[0])]
    assert len(cells) == 4 * num_rows
    occupied = [
        (int(r), int(c))
        for fact in re.findall(r"\(at_(?:square|two|right_l) [^)]*\)", init)
        for r, c in re.findall(r"f(\d+)-(\d+)f", fact)
    ]
    clear = {(int(r), int(c)) for r, c in re.findall(r"\(clear f(\d+)-(\d+)f\)", init)}
    assert len(occupied) == len(set(occupied)) and not clear & set(occupied)
    assert clear | set(occupied) == set(cells)
    # Pieces sit in rows 0..num_rows/2 and never in column 3 (L-pieces may reach it).
    assert all(r <= num_rows // 2 for r, _ in occupied)
    assert all(
        int(c) < 3
        for fact in re.findall(r"\(at_(?:square|two) [^)]*\)", init)
        for _, c in re.findall(r"f(\d+)-(\d+)f", fact)
    )
    assert re.findall(r"\(at_right_l ", init)
    assert "(= (total-cost) 0)" in init and "(:metric minimize (total-cost))" in goal
    goal_cells = {(int(r), int(c)) for r, c in re.findall(r"\(clear f(\d+)-(\d+)f\)", goal)}
    assert goal_cells == {(r, c) for r in range(num_rows // 2) for c in range(4)}


def test_tetris_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-r", "6", "-s", "1"]) == 0
    assert capsys.readouterr().out == make_problem(6, 1)
    for rows in (2, 5):
        with pytest.raises(ValueError, match="num_rows"):
            make_problem(rows)


@pytest.mark.parametrize("block_type,piece", [(1, "at_square"), (2, "at_two"), (3, "at_right_l")])
@pytest.mark.parametrize("num_rows", [4, 10, 24])
def test_tetris_single_block_types(block_type: int, piece: str, num_rows: int, tmp_path: Path) -> None:
    for seed in range(5):
        problem = make_problem(num_rows, seed, block_type)
        init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
        pieces = re.findall(r"\((at_square|at_two|at_right_l) ", init)
        assert pieces and set(pieces) == {piece}
        occupied = [
            (int(r), int(c)) for f in re.findall(r"\(at_\w+ [^)]*\)", init) for r, c in re.findall(r"f(\d+)-(\d+)f", f)
        ]
        assert len(occupied) == len(set(occupied))
        # upstream's inclusive row bound: 1x1 and 2x1 pieces may reach row num_rows/2 (+1 for a downward 2x1)
        assert all(r <= num_rows // 2 + (block_type == 2) for r, _ in occupied)
        assert f"(problem tetris-{num_rows}-{block_type}-" in problem
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(make_problem(num_rows, 1, block_type))
    here = Path(generator.__file__).parent
    for domain in (here / "domain.pddl", here.parents[1] / "autoscale/tetris/domain.pddl"):
        Parser(domain, options).parse_task(tmp_path / "p.pddl")


def test_tetris_block_type_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-r", "8", "-s", "3", "-b", "2"]) == 0
    assert capsys.readouterr().out == make_problem(8, 3, 2)
    with pytest.raises(ValueError, match="block_type"):
        make_problem(8, 1, 5)
