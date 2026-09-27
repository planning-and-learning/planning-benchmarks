#!/usr/bin/env python3
# Reconstruction of Drew McDermott's AIPS-1998 Assembly tasks
# (data/classical/downward-benchmarks/assembly); the IPC tasks were not made by
# pddl-generators' assembly.c, so its code is not used here.

from __future__ import annotations

import argparse
import random
import sys

NAMES = (
    "bracket", "coil", "connector", "contraption", "device", "doodad", "fastener", "foobar", "frob",
    "gimcrack", "hack", "hoozawhatsie", "kludge", "mount", "plug", "socket", "sprocket", "thingumbob",
    "tube", "unit", "valve", "whatsis", "widget", "wire",
)
RESOURCES = (
    "charger", "clamp", "file", "hammer", "hammock", "pliers", "scaffold", "scalpel", "scope", "tweezers",
    "voltmeter",
)


def make_problem(
    num_parts: int,
    num_resources: int = 2,
    seed: int | None = None,
    depth: int = 3,
    max_sons: int = 6,
    internal_probability: float = 0.94,
    deep_internal_probability: float = 0.11,
    requires_probability: float = 0.84,
    order_probability: float = 0.18,
    transient_probability: float = 0.009,
    tool_probability: float = 0.03,
) -> str:
    """Generate an Assembly task: build the root from a part-of tree.

    The root has ``num_parts`` parts; a part on level 1 is itself assembled
    (has 1..``max_sons`` parts) with ``internal_probability``, deeper ones with
    ``deep_internal_probability`` (1..``max_sons // 2`` parts); level ``depth``
    holds base parts only. Every non-root assembly requires a random resource
    with ``requires_probability``; siblings get an assemble order with
    ``order_probability`` per pair, consistent with one random order per whole.
    A part ``t`` becomes a transient part of another whole ``W`` one level up
    with ``transient_probability`` per pair; like in the IPC tasks it then gets
    ``(assemble-order t x W)``, ``(remove-order x t W)`` and
    ``(assemble-order t x P)`` for a random part ``x`` of ``W`` and its own
    whole ``P``, sometimes a second such ``x`` and a part of ``W`` ordered before
    it. With ``tool_probability`` an extra free assembly (a tool, part of
    nothing) is a transient part of a random whole. Base parts, tools and
    resources are available.
    """
    checks: list[tuple[str, object, int]] = [
        ("num_parts", num_parts, 1), ("num_resources", num_resources, 1),
        ("depth", depth, 1), ("max_sons", max_sons, 1),
    ]
    for name, value, minimum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    probabilities = (
        ("internal_probability", internal_probability), ("deep_internal_probability", deep_internal_probability),
        ("requires_probability", requires_probability), ("order_probability", order_probability),
        ("transient_probability", transient_probability), ("tool_probability", tool_probability),
    )
    for name, value in probabilities:
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"{name} must be in [0, 1]")

    rng = random.Random(seed)
    # nodes are ints; level[n], parent[n], sons[n]
    level: list[int] = [0]
    parent: list[int] = [-1]
    sons: list[list[int]] = [[]]
    frontier = [0]
    while frontier:
        node = frontier.pop(0)
        d = level[node]
        if d == depth:
            continue
        if d == 0:
            count = num_parts
        elif rng.random() < (internal_probability if d == 1 else deep_internal_probability):
            count = rng.randint(1, max_sons if d == 1 else max(1, max_sons // 2))
        else:
            continue
        for _ in range(count):
            level.append(d + 1)
            parent.append(node)
            sons.append([])
            sons[node].append(len(level) - 1)
            frontier.append(len(level) - 1)
    num_nodes = len(level)

    orders: list[tuple[int, int, int]] = []  # (prev, part, whole)
    removes: list[tuple[int, int, int]] = []  # (prev, transient, whole)
    transients: list[tuple[int, int]] = []
    rank: dict[int, int] = {}
    for whole in range(num_nodes):
        order = sons[whole][:]
        rng.shuffle(order)
        for i, x in enumerate(order):
            rank[x] = i
            orders.extend((x, y, whole) for y in order[i + 1:] if rng.random() < order_probability)

    def acyclic(edges: list[tuple[int, int, int]]) -> bool:
        succ: dict[tuple[int, int], list[int]] = {}
        for a, b, w in edges:
            succ.setdefault((w, a), []).append(b)
        state: dict[tuple[int, int], int] = {}

        def visit(node: tuple[int, int]) -> bool:
            state[node] = 1
            for b in succ.get(node, []):
                nxt = (node[0], b)
                if state.get(nxt) == 1 or (nxt not in state and not visit(nxt)):
                    return False
            state[node] = 2
            return True

        return all(state.get(node) == 2 or visit(node) for node in list(succ))

    def add_transient(t: int, whole: int) -> None:
        parts = sons[whole]
        x = rng.choice(parts)
        # t goes in right before x in whole's order, so whole's own orders stay acyclic
        later = [y for y in parts if rank[y] >= rank[x]]
        firsts = [x] + ([rng.choice(later)] if len(later) > 1 and rng.random() < 0.37 else [])
        new: list[tuple[int, int, int]] = []
        for y in dict.fromkeys(firsts):
            new.append((t, y, whole))
            if parent[t] >= 0:
                new.append((t, y, parent[t]))
        earlier = [y for y in parts if rank[y] < rank[x]]
        if earlier and rng.random() < 0.35:
            new.append((rng.choice(earlier), t, whole))
        # ponytail: a cross order (t, y, P) binds when y is itself transient in P; drop a
        # transient whose orders would close a cycle, which would make the task unsolvable
        if not acyclic(orders + new):
            return
        transients.append((t, whole))
        orders.extend(new)
        removes.append((x, t, whole))

    for t in range(num_nodes):
        if level[t] < 2:
            continue
        for whole in range(num_nodes):
            if (
                sons[whole] and level[whole] == level[t] - 1 and whole != parent[t]
                and rng.random() < transient_probability
            ):
                add_transient(t, whole)
    tools: list[int] = []
    wholes = [w for w in range(num_nodes) if sons[w] and w != 0]
    if wholes and rng.random() < tool_probability:
        level.append(-1)
        parent.append(-1)
        sons.append([])
        tools.append(len(level) - 1)
        add_transient(tools[0], rng.choice(wholes))
        num_nodes += 1

    names = [
        NAMES[i % len(NAMES)] + (f"-{i}" if i >= len(NAMES) else "")
        for i in rng.sample(range(num_nodes + len(NAMES)), num_nodes)
    ]
    picked: list[int] = rng.sample(range(max(num_resources, len(RESOURCES))), num_resources)
    resources = [RESOURCES[i] if i < len(RESOURCES) else f"resource-{i}" for i in picked]
    requires = [
        (n, rng.choice(resources)) for n in range(1, num_nodes) if sons[n] and rng.random() < requires_probability
    ]

    facts = [f"(available {names[n]})" for n in range(num_nodes) if not sons[n]]
    facts += [f"(available {r})" for r in resources]
    facts += [f"(requires {names[n]} {r})" for n, r in requires]
    facts += [f"(part-of {names[n]} {names[parent[n]]})" for n in range(1, num_nodes) if parent[n] >= 0]
    facts += [f"(transient-part {names[t]} {names[w]})" for t, w in transients]
    facts += [f"(assemble-order {names[a]} {names[b]} {names[w]})" for a, b, w in dict.fromkeys(orders)]
    facts += [f"(remove-order {names[a]} {names[b]} {names[w]})" for a, b, w in removes]

    return (f"""(define (problem assembly-p{num_parts}-r{num_resources}-d{depth}-m{max_sons}-s{seed})
   (:domain assembly)
   (:objects {' '.join(names)} - assembly
             {' '.join(resources)} - resource)
   (:init
          {(chr(10) + '          ').join(facts)})
   (:goal (complete {names[0]})))
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an ADL Assembly PDDL problem.")
    parser.add_argument("-p", "--num-parts", type=int, required=True, help="parts of the goal assembly (IPC: 3-13)")
    parser.add_argument("-r", "--num-resources", type=int, default=2, help="resources (IPC: 1-3)")
    parser.add_argument("-d", "--depth", type=int, default=3)
    parser.add_argument("-m", "--max-sons", type=int, default=6)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_parts, args.num_resources, args.seed, depth=args.depth, max_sons=args.max_sons)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
