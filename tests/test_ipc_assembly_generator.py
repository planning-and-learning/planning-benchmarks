import re
from collections import defaultdict, deque
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.assembly import generator
from pypddl_datasets.generators.classical.ipc.assembly.generator import main, make_problem

DOMAIN = Path(generator.__file__).with_name("domain.pddl")


def facts(problem, predicate):
    return [tuple(m.split()) for m in re.findall(rf"\({predicate} ([^()]*)\)", problem)]


def solvable(problem):
    """Breadth-first search over the Assembly domain's ADL semantics."""
    part_of = {(a, b) for a, b in facts(problem, "part-of")}
    transient = {(a, b) for a, b in facts(problem, "transient-part")}
    order = set(facts(problem, "assemble-order"))
    remove_order = set(facts(problem, "remove-order"))
    requires = defaultdict(set)
    for a, r in facts(problem, "requires"):
        requires[a].add(r)
    parts = defaultdict(set)
    for a, b in part_of:
        parts[b].add(a)
    transients = defaultdict(set)
    for a, b in transient:
        transients[b].add(a)
    goal = re.search(r"\(:goal \(complete ([^)]*)\)", problem).group(1)
    wholes = set(parts) | set(transients)
    start = (frozenset(a for (a,) in facts(problem, "available")), frozenset(), frozenset(), frozenset())
    seen, queue = {start}, deque([start])
    while queue:
        available, complete, inc, committed = queue.popleft()
        if goal in complete:
            return True
        successors = []
        resources = {r for rs in requires.values() for r in rs}
        for r in resources & available:
            for w in wholes:
                successors.append((available - {r}, complete, inc, committed | {(r, w)}))
        for r, w in committed:
            successors.append((available | {r}, complete, inc, committed - {(r, w)}))
        for w in wholes:
            if not all((r, w) in committed for r in requires[w]):
                continue
            for p in (parts[w] | transients[w]) & available:
                if all((prev, w) in inc for prev, part, whole in order if part == p and whole == w):
                    done = all(q == p or (q, w) in inc for q in parts[w]) and not any((t, w) in inc for t in transients[w])
                    successors.append((available - {p} | ({w} if done else set()), complete | ({w} if done else set()),
                                       inc | {(p, w)}, committed))
            for p, whole in inc:
                if whole != w:
                    continue
                if p in transients[w]:
                    ok = all((prev, w) in inc for prev, t, whole2 in remove_order if t == p and whole2 == w)
                else:
                    ok = not any((prev, w) in inc for prev, part, whole2 in order if part == p and whole2 == w)
                if ok:
                    done = all((q, w) in inc and q != p for q in parts[w]) and not any((t, w) in inc and t != p for t in transients[w])
                    successors.append((available | {p} | ({w} if done else set()), complete | ({w} if done else set()),
                                       inc - {(p, w)}, committed))
        for state in successors:
            if state not in seen:
                seen.add(state)
                queue.append(state)
    return False


@pytest.mark.parametrize("seed", range(6))
def test_small_tasks_with_transients_and_tools_are_solvable(seed):
    problem = make_problem(2, 1, seed=seed, depth=2, max_sons=2, order_probability=0.5,
                           transient_probability=0.5, tool_probability=0.5)
    assert solvable(problem)


@pytest.mark.parametrize("num_parts,num_resources,seed", [(3, 1, 0), (8, 2, 1), (13, 3, 2)])
def test_tree_and_transient_patterns(num_parts, num_resources, seed):
    problem = make_problem(num_parts, num_resources, seed=seed, transient_probability=0.05)
    assert problem == make_problem(num_parts, num_resources, seed=seed, transient_probability=0.05)
    parent = dict(facts(problem, "part-of"))
    kids = defaultdict(list)
    for c, w in parent.items():
        kids[w].append(c)
    root = re.search(r"\(complete ([^)]*)\)", problem).group(1)
    assert len(kids[root]) == num_parts and root not in parent
    available = {a for (a,) in facts(problem, "available")}
    resources = problem.split("- assembly", 1)[1].split("- resource", 1)[0].split()
    assert len(resources) == num_resources and set(resources) <= available
    assert all((x in available) == (not kids[x]) for x in parent)
    assert all(w in kids and w != root for w, _ in facts(problem, "requires"))
    orders = set(facts(problem, "assemble-order"))
    for t, w in facts(problem, "transient-part"):
        (x,) = [x for x, t2, w2 in facts(problem, "remove-order") if t2 == t and w2 == w]
        assert (t, x, w) in orders and parent[x] == w
        if t in parent:
            assert (t, x, parent[t]) in orders


def test_output_parses_strictly(tmp_path):
    options = ParserOptions()
    options.strict = True
    for i, problem in enumerate([make_problem(13, 3, seed=1), make_problem(5, 2, seed=2, depth=2, tool_probability=1.0)]):
        path = tmp_path / f"p{i}.pddl"
        path.write_text(problem)
        Parser(DOMAIN, options).parse_task(path)


def test_cli_matches_make_problem(capsys):
    assert main(["-p", "4", "-r", "2", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(4, 2, seed=3)


@pytest.mark.parametrize("parameter,value", [("num_parts", 0), ("num_resources", 0), ("depth", 0), ("order_probability", 1.5)])
def test_rejects_invalid_parameters(parameter, value):
    parameters = dict(num_parts=3)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
