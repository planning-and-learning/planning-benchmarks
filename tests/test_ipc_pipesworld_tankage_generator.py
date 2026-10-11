import collections
import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.pipesworld_tankage import generator
from pypddl_datasets.generators.classical.ipc.pipesworld_tankage.generator import NETWORKS, main, make_problem


def _facts(text: str) -> collections.defaultdict[str, list[tuple[str, ...]]]:
    by: collections.defaultdict[str, list[tuple[str, ...]]] = collections.defaultdict(list)
    for fact in re.findall(r"\(([a-z][a-z0-9 -]*)\)", text):
        predicate, *arguments = fact.split()
        by[predicate].append(tuple(arguments))
    return by


@pytest.mark.parametrize("network", sorted(NETWORKS))
@pytest.mark.parametrize("tankage", [20, 50, 90])
def test_pipesworld_tankage_structure(network: int, tankage: int, tmp_path: Path) -> None:
    capacity = sum(n for *_, n in NETWORKS[network])
    num_batches, num_goals = capacity + 8, 4
    problem = make_problem(network, num_batches, num_goals, tankage=tankage, seed=network)
    assert problem == make_problem(network, num_batches, num_goals, tankage=tankage, seed=network) == problem.lower()
    init_text, goal_text = problem.split("(:init", 1)[1].split("(:goal", 1)
    init, goal = _facts(init_text), _facts(goal_text)
    product = {f[0]: f[1] for f in init["is-product"]}
    assert len(product) == num_batches

    # Pipes are full chains of their IPC length; every other batch is at exactly one area.
    first, last = {p: b for b, p in init["first"]}, {p: b for b, p in init["last"]}
    follow = {previous: following for following, previous in init["follow"]}
    in_pipes: set[str] = set()
    for (a, b, length), (frm, to, pipe) in zip(NETWORKS[network], init["connect"]):
        assert (frm, to) == (f"a{a}", f"a{b}")
        chain = [first[pipe]]
        while chain[-1] in follow:
            chain.append(follow[chain[-1]])
        assert len(chain) == length and chain[-1] == last[pipe]
        assert ((pipe,) in init["unitary"]) == (length == 1)
        in_pipes |= set(chain)
    location = {f[0]: f[1] for f in init["on"]}
    assert len(in_pipes) == capacity and set(location) == set(product) - in_pipes

    # Tank slots: round(tankage% of the product's batches) per area, at least the batches held there.
    slots = collections.Counter((a, p) for _, p, a in init["tank-slot-product-location"])
    held = collections.Counter((a, product[b]) for b, a in location.items())
    for p in set(product.values()):
        for a in {x for x, _, _ in init["connect"]} | {x for _, x, _ in init["connect"]}:
            assert slots[a, p] == max((2 * list(product.values()).count(p) * tankage + 100) // 200, held[a, p])
    assert len(init["occupied"]) == len(location) and len(init["occupied"]) + len(init["not-occupied"]) == sum(
        slots.values()
    )

    # Goals move distinct batches to new areas and restore every pipe to normal.
    goals = {f[0]: f[1] for f in goal["on"]}
    assert len(goals) == num_goals and all(location.get(b) != a for b, a in goals.items())
    assert sorted(goal["normal"]) == sorted(init["normal"]) == sorted((p,) for _, _, p in init["connect"])

    path = tmp_path / "p.pddl"
    path.write_text(problem, encoding="utf-8")
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(path)


def test_pipesworld_tankage_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-n", "3", "-b", "12", "-g", "3", "-t", "60", "--seed", "4"]) == 0
    assert capsys.readouterr().out == make_problem(3, 12, 3, tankage=60, seed=4)
    for arguments, message in (
        ((6, 12, 2, 50), "network"),
        ((2, 4, 1, 50), "num_batches"),
        ((2, 10, 7, 50), "num_goals"),
        ((2, 10, 0, 50), "num_goals"),
        ((2, 10, 2, 0), "tankage"),
        ((2, 10, 2, 101), "tankage"),
    ):
        network, num_batches, num_goals, tankage = arguments
        with pytest.raises(ValueError, match=message):
            make_problem(network, num_batches, num_goals, tankage=tankage)
