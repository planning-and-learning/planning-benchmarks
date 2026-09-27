import random
import re
from pathlib import Path
from typing import cast

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.pathways import generator
from pypddl_datasets.generators.classical.ipc.pathways.generator import main, make_task


def _search(pattern: str, text: str, flags: int = 0) -> re.Match[str]:
    match = re.search(pattern, text, flags)
    assert match is not None, pattern
    return match


IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks/pathways"


class GlibcRand:
    """glibc rand() (TYPE_3), to replay the IPC 2006 seeds through the port."""

    def __init__(self, seed: int) -> None:
        r = [seed or 1]
        for _ in range(30):
            hi, lo = divmod(r[-1], 127773)
            r.append((16807 * lo - 2836 * hi) % 2147483647)
        r += r[:3]
        for i in range(34, 344):
            r.append((r[i - 31] + r[i - 3]) & 0xFFFFFFFF)
        self.r = r

    def randrange(self, n: int) -> int:
        self.r.append((self.r[-31] + self.r[-3]) & 0xFFFFFFFF)
        return (self.r[-1] >> 1) % n


@pytest.mark.parametrize("task,seed,reactions,goals", [(1, 2004, 12, 1), (5, 387462, 72, 6)])
def test_pathways_replays_ipc_tasks_with_the_original_rng(task: int, seed: int, reactions: int, goals: int) -> None:
    # replaying the IPC tasks needs the private builder driven by the original RNG
    rng = cast(random.Random, GlibcRand(seed))  # duck-typed: _build only calls randrange
    applied, used, picked = generator._build(  # pyright: ignore[reportPrivateUsage]  # pylint: disable=protected-access
        rng, reactions, goals
    )
    ipc_init = (IPC / f"p{task:02d}.pddl").read_text()
    ipc_domain = (IPC / f"domain_p{task:02d}.pddl").read_text()
    assert set(re.findall(r"\(possible (\S+)\)", ipc_init)) == {s for s in generator.SIMPLE if s in used and s != "_"}
    assert len(re.findall(r"-reaction ", ipc_init)) == len(applied)
    ipc_pairs = re.findall(r"\(or \(available (\S+)\)\s*\(available (\S+)\)\)", ipc_domain)
    assert [tuple(picked[i : i + 2]) for i in range(0, len(picked), 2)] == ipc_pairs


@pytest.mark.parametrize("reactions,goals,substances,seed", [(12, 1, 3, 1), (72, 6, 7, 2), (240, 20, 22, 3)])
def test_pathways_goals_are_relaxed_reachable(reactions: int, goals: int, substances: int, seed: int) -> None:
    domain, problem = make_task(reactions, goals, substances, seed=seed)
    assert (domain, problem) == make_task(reactions, goals, substances, seed=seed)
    assert domain == domain.lower() and problem == problem.lower()
    init = problem.split("(:init", 1)[1]
    facts = re.findall(r"\((association-reaction|catalyzed-association-reaction|synthesis-reaction) ([^)]*)\)", init)
    assert len(facts) >= reactions
    reachable = set(re.findall(r"\(possible (\S+)\)", init))
    changed = True
    while changed:
        changed = False
        for kind, args in facts:
            *inputs, product = args.split()
            needed = inputs[:1] if kind == "synthesis-reaction" else inputs
            if set(needed) <= reachable and product not in reachable:
                reachable.add(product)
                changed = True
    pairs = re.findall(r"\(or \(available (\S+)\)\s*\(available (\S+)\)\)", domain)
    assert len(pairs) == goals and all(a in reachable and b in reachable for a, b in pairs)
    constants = _search(r"\(:constants(.*?)\)", domain, re.S).group(1).split()
    assert {c for c in constants if c not in ("-", "simple", "complex")} == {m for pair in pairs for m in pair}
    assert len(re.findall(r" - level", problem)) == substances + 1
    assert len(re.findall(r"\(goal\d+\)", problem.split("(:goal")[1])) == goals


def test_pathways_cli_and_validation(tmp_path: Path) -> None:
    domain, problem = tmp_path / "d.pddl", tmp_path / "p.pddl"
    assert main(["-R", "24", "-G", "2", "-L", "3", "-s", "5", "--domain", str(domain), "--problem", str(problem)]) == 0
    assert (domain.read_text(), problem.read_text()) == make_task(24, 2, 3, seed=5)
    for parameters, name in (((0, 1, 1), "min_reactions"), ((5, 0, 1), "num_goals"), ((5, 1, 0), "num_substances")):
        with pytest.raises(ValueError, match=name):
            make_task(*parameters)


@pytest.mark.parametrize("reactions,goals,substances,seed", [(10, 2, 3, 1), (20, 25, 22, 4), (60, 8, 10, 2)])
def test_pathways_strips_wrapper_encoding(
    reactions: int, goals: int, substances: int, seed: int, tmp_path: Path
) -> None:
    domain, problem = make_task(reactions, goals, substances, seed, strips_wrapper=True)
    assert domain == domain.lower() and problem == problem.lower()
    used = len(re.findall(r"\(goal\d+\)", problem.split("(:goal", 1)[1]))
    predicates = domain.split("(:predicates", 1)[1].split("(:action", 1)[0]
    assert len(re.findall(r"\(goal\d+\)", predicates)) == goals >= used >= 1
    dummies = re.findall(
        r"\(:action dummy-strips-action-(\d+)\n :parameters \(\)\n"
        r" :precondition \(available (\S+)\)\n :effect \(and \(goal(\d+)\)\)\)",
        domain,
    )
    assert [int(i) for i, _, _ in dummies] == list(range(2 * used))
    assert [int(g) for _, _, g in dummies] == [i // 2 + 1 for i in range(2 * used)]
    # molecules live in the domain; the problem declares only levels
    objects = problem.split("(:objects", 1)[1].split("(:init", 1)[0]
    assert set(re.findall(r" - (\w+)", objects)) == {"level"}
    constants = domain.split("(:constants", 1)[1].split("(:predicates", 1)[0]
    assert {m for _, m, _ in dummies} <= set(constants.split())
    (tmp_path / "domain.pddl").write_text(domain)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(tmp_path / "domain.pddl", options).parse_task(tmp_path / "p.pddl")
