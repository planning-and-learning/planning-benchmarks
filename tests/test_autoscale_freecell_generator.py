import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.autoscale.freecell import generator
from pypddl_datasets.generators.classical.autoscale.freecell.generator import main, make_problem

AGILE = Path(__file__).resolve().parents[1] / "data/classical/autoscale-benchmarks-main/21.11-agile-strips/freecell"


@pytest.mark.parametrize("cells,cols,stacks,size", [(0, 1, 1, 1), (2, 6, 4, 4), (4, 8, 8, 13)])
def test_freecell_deals_every_card_once(cells: int, cols: int, stacks: int, size: int, tmp_path: Path) -> None:
    problem = make_problem(cells, cols, stacks, size, seed=3)
    assert problem == make_problem(cells, cols, stacks, size, seed=3) == problem.lower()
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    bottoms = re.findall(r"\(bottomcol (\S+)\)", init)
    uppers = [upper for upper, _ in re.findall(r"\(on (\S+) (\S+)\)", init)]
    assert sorted(bottoms + uppers) == sorted(f"{s}{'a' if j == 0 else j + 1}" for s in "chsd" for j in range(size))
    assert len(re.findall(r"\(clear ", init)) == len(bottoms) <= stacks
    assert f"(colspace coln{cols - stacks})" in init and f"(cellspace celln{cells})" in init
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_freecell_static_facts_and_goal_match_agile_task() -> None:
    reference = (AGILE / "p01.pddl").read_text().lower()  # freecell-f3-c5-s4-i2, 3 cards per suit
    problem = make_problem(3, 5, 2, 3, seed=0)

    def static(text: str) -> list[str]:
        init = text.split("(:init", 1)[1]
        return sorted(
            f for f in re.findall(r"\([a-z]+ [^()]*\)", init) if not f.startswith(("(bottomcol", "(on ", "(clear"))
        )

    assert static(problem) == static(reference)


def test_freecell_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-f", "2", "-c", "6", "-i", "4", "-n", "5", "-r", "9"]) == 0
    assert capsys.readouterr().out == make_problem(2, 6, 4, 5, seed=9)
    with pytest.raises(ValueError, match="num_stacks"):
        make_problem(2, 3, 4, 5)
