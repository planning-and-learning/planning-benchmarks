import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.flashfill.generator import FAMILIES, _Example, _task, main, make_task

DATA = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks/flashfill-sat18-adl"
FACT = r"\((?:assignment|hiindex|loindex|size|next|input-assignment) [^()?]*\)"


def reference_examples(i):
    domain = (DATA / f"domain-p{i:02d}.pddl").read_text().lower()
    problem = (DATA / f"p{i:02d}.pddl").read_text().lower()
    inits = [re.findall(FACT, problem.split("(:init")[1].split("(test-0)")[0])]
    goals = []
    for k in range(10):
        m = re.search(rf"\(:action repeat-end-main-{k}-1\n(.*?)\n\)\n", domain, re.S)
        if not m:
            break
        pre, eff = m.group(1).split(":effect")
        goals.append(re.findall(r"\((?:assignment|size) res [^()]*\)", pre))
        if "(done-programming)" not in eff:
            inits.append(re.findall(FACT, eff))
    name = re.search(r"problem (\S+)\)", problem).group(1)
    return name, [_Example(i, g) for i, g in zip(inits, goals)]


@pytest.mark.parametrize("i", range(1, 21))
def test_ipc_task_is_rebuilt_exactly_from_its_examples(i):
    name, examples = reference_examples(i)
    family = next(f for f in FAMILIES if name.startswith(f + "-"))
    domain, problem = _task(family, examples, name)
    assert domain == (DATA / f"domain-p{i:02d}.pddl").read_text().lower()
    assert problem.rstrip("\n") == (DATA / f"p{i:02d}.pddl").read_text().lower()


@pytest.mark.parametrize("family", sorted(FAMILIES))
def test_generated_tasks_parse_and_have_one_test_per_example(family, tmp_path):
    domain, problem = make_task(family, 3, seed=5)
    assert (domain, problem) == make_task(family, 3, seed=5) and domain == domain.lower()
    assert re.findall(r"^    \(test-(\d+)\)$", domain, re.M) == ["0", "1", "2"]
    lines = FAMILIES[family][1]
    assert len(re.findall(r"\(:action repeat-end-main-", domain)) == 3 * (lines - 1)
    assert domain.count("(done-programming)\n    )") == lines - 1
    (tmp_path / "domain.pddl").write_text(domain)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(tmp_path / "domain.pddl", options).parse_task(tmp_path / "p.pddl")


def test_cli_writes_both_files(tmp_path):
    args = ["initials", "2", "-s", "4", "--domain", str(tmp_path / "d.pddl"), "--problem", str(tmp_path / "p.pddl")]
    assert main(args) == 0
    assert ((tmp_path / "d.pddl").read_text(), (tmp_path / "p.pddl").read_text()) == make_task("initials", 2, seed=4)
    with pytest.raises(ValueError, match="family"):
        make_task("reverse", 2)
