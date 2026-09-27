import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.fo_counters import generator
from pypddl_datasets.generators.numeric.ipc.fo_counters.generator import main, make_problem

IPC = Path(__file__).resolve().parents[1] / "data/numeric/ipc2023/fo-counters"


def facts(text):
    text = re.sub(r";[^\n]*", "", text).lower()
    return sorted(re.findall(r"\(= \([^()]*\) -?[\d.]+\)", text)), re.sub(r"\s+", "", text.split("(:goal", 1)[1])


@pytest.mark.parametrize("index", range(1, 21))
def test_fo_counters_reproduce_every_ipc_task(index):
    ipc = (IPC / f"pfile{index}.pddl").read_text()
    n = len(re.findall(r"\(value c\d+\)", ipc.split("(:goal")[0]))
    assert facts(make_problem(n)) == facts(ipc)


def test_fo_counters_strict_parse_and_cli(tmp_path, capsys):
    (tmp_path / "p.pddl").write_text(make_problem(5))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]
    assert main(["-n", "3"]) == 0 and capsys.readouterr().out == make_problem(3)
    with pytest.raises(ValueError, match="num_counters"):
        make_problem(1)
