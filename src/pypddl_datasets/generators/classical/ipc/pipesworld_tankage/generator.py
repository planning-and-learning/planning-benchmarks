#!/usr/bin/env python3
# Generator for the IPC-2004 Pipesworld tasks (tankage and, with tankage=None, notankage).
# The IPC generator is not public; this reconstruction follows the IPC tasks (see README.md):
# the five IPC networks, uniform products and placement, and the IPC tank-slot rule. Goals
# come from a random walk of complete push/pop moves, so every task is solvable.

from __future__ import annotations

import argparse
import random
import sys
from collections import Counter

PRODUCTS = ("lco", "gasoleo", "rat-a", "oca1", "oc1b")
INCOMPATIBLE = {("rat-a", "oca1"), ("rat-a", "oc1b"), ("oca1", "rat-a"), ("oc1b", "rat-a")}
# Pipes (from-area, to-area, batches it holds) of the five IPC networks.
NETWORKS = {
    1: ((1, 2, 1), (1, 3, 1)),
    2: ((1, 2, 2), (1, 3, 2)),
    3: ((1, 2, 2), (1, 3, 2), (3, 4, 1)),
    4: ((1, 2, 2), (1, 3, 2), (2, 3, 3), (3, 4, 1)),
    5: ((1, 2, 2), (1, 3, 2), (1, 5, 4), (2, 3, 3), (3, 4, 1)),
}
WALK_STEPS = 50  # random-walk moves per batch before the goal is read off
MAX_STEPS = 100  # per batch, before the walk counts as stuck
REDRAWS = 100  # ponytail: fresh starts tried before giving up with a ValueError


def make_problem(
    network: int,
    num_batches: int,
    num_goals: int,
    tankage: int | None = 50,
    seed: int | None = None,
) -> str:
    """Generate a Pipesworld task on IPC network ``network`` (1-5).

    Every batch gets a uniform product; the pipes are filled with uniform batches and the rest
    sit at uniform areas. ``tankage`` (percent) gives each area round(tankage% of the batches
    of a product) tank slots for it, at least as many as it holds initially; ``None`` emits a
    notankage task. Goals put ``num_goals`` batches at areas they reach in a random walk.
    """
    checks: list[tuple[str, object]] = [("network", network), ("num_batches", num_batches), ("num_goals", num_goals)]
    for name, value in checks + ([] if tankage is None else [("tankage", tankage)]):
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError(f"{name} must be an integer")
    if network not in NETWORKS:
        raise ValueError("network must be 1, 2, 3, 4 or 5")
    pipes = NETWORKS[network]
    capacity = sum(length for _, _, length in pipes)
    if num_batches <= capacity:
        raise ValueError(f"num_batches must exceed the {capacity} batches the pipes of network {network} hold")
    if not 1 <= num_goals <= num_batches - capacity:
        raise ValueError(f"num_goals must be between 1 and num_batches - {capacity} (batches outside the pipes)")
    if tankage is not None and not 1 <= tankage <= 100:
        raise ValueError("tankage must be None or an integer percentage 1-100")

    rng = random.Random(seed)
    areas = range(1, 1 + max(max(a, b) for a, b, _ in pipes))
    for _ in range(REDRAWS):
        product = [rng.choice(PRODUCTS) for _ in range(num_batches)]
        shuffled = iter(rng.sample(range(num_batches), num_batches))
        contents = [[next(shuffled) for _ in range(n)] for *_, n in pipes]
        start: dict[int, int | None] = {b: None for batches in contents for b in batches}
        start.update((b, rng.choice(areas)) for b in shuffled)
        held = Counter((a, product[b]) for b, a in start.items() if a is not None)
        slots = {
            (a, p): max((2 * product.count(p) * tankage + 100) // 200, held[a, p])
            for p in sorted(set(product))
            for a in areas
            if tankage is not None
        }
        goals = _walk(rng, pipes, product, [list(c) for c in contents], dict(start), slots, num_goals)
        if goals is not None:
            break
    else:
        raise ValueError(f"num_goals: the random walk did not displace {num_goals} batches (tankage too tight?)")

    pipe_names = [f"s{a}{b}" for a, b, _ in pipes]
    slot_names = {key: [f"ta{key[0]}-{i}-{key[1]}" for i in range(1, n + 1)] for key, n in slots.items() if n}
    objects = [" ".join(f"b{b}" for b in range(num_batches)) + " - batch-atom"]
    objects += [" ".join(f"a{a}" for a in areas) + " - area", " ".join(pipe_names) + " - pipe"]
    init = [f"(normal {s})" for s in pipe_names]
    init += [f"(may-interface {p} {q})" for p in PRODUCTS for q in PRODUCTS if (p, q) not in INCOMPATIBLE]
    init += [f"(connect a{a} a{b} {s})" for (a, b, _), s in zip(pipes, pipe_names)]
    init += [f"(is-product b{b} {p})" for b, p in enumerate(product)]
    for b in sorted(b for b, a in start.items() if a is not None):
        init.append(f"(on b{b} a{start[b]})")
    if tankage is not None:
        objects += [" ".join(names) + " - tank-slot" for names in slot_names.values()]
        for (a, p), names in slot_names.items():
            init += [f"(tank-slot-product-location {t} {p} a{a})" for t in names]
            init += [f"({'occupied' if i < held[a, p] else 'not-occupied'} {t})" for i, t in enumerate(names)]
    for s, batches in zip(pipe_names, contents):
        init += [f"(first b{batches[0]} {s})", f"(last b{batches[-1]} {s})"]
        init += [f"(follow b{nxt} b{prev})" for prev, nxt in zip(batches, batches[1:])]
        init.append(f"({'unitary' if len(batches) == 1 else 'not-unitary'} {s})")
    goal = [f"(on b{b} a{a})" for b, a in goals]
    if tankage is not None:
        goal += [f"(normal {s})" for s in pipe_names]

    name = f"pipesworld-net{network}-b{num_batches}-g{num_goals}" + ("" if tankage is None else f"-t{tankage}")
    nl = "\n    "
    return f"""(define (problem {name})
  (:domain pipesworld_strips)
  (:objects
    {nl.join(objects)})
  (:init
    {nl.join(init)})
  (:goal (and
    {nl.join(goal)})))
""".lower()


def _walk(
    rng: random.Random,
    pipes: tuple[tuple[int, int, int], ...],
    product: list[str],
    contents: list[list[int]],
    location: dict[int, int | None],
    slots: dict[tuple[int, str], int],
    num_goals: int,
) -> list[tuple[int, int]] | None:
    """Random push/pop moves; ``num_goals`` displaced batches with their final areas, or None if stuck.

    Empty ``slots`` means no tankage; otherwise a batch only leaves a pipe into a free tank slot.
    """
    start = dict(location)
    held = Counter((a, product[b]) for b, a in location.items() if a is not None)
    steps = 0
    while True:
        displaced = sorted(b for b, a in location.items() if a is not None and a != start[b])
        if steps >= WALK_STEPS * len(product) and len(displaced) >= num_goals:
            return sorted((b, a) for b in rng.sample(displaced, num_goals) if (a := location[b]) is not None)
        if steps >= MAX_STEPS * len(product):
            return None
        moves: list[tuple[list[int], int, int, int, bool]] = []
        for (a, b, _), batches in zip(pipes, contents):
            for here, there, push in ((a, b, True), (b, a, False)):
                entry, leaving = (batches[0], batches[-1]) if push else (batches[-1], batches[0])
                if slots and held[there, product[leaving]] >= slots[there, product[leaving]]:
                    continue
                for x, at in location.items():
                    if at == here and (product[x], product[entry]) not in INCOMPATIBLE:
                        moves.append((batches, x, here, there, push))
        if not moves:
            return None
        batches, x, here, there, push = rng.choice(moves)
        if push:
            leaving = batches.pop()
            batches.insert(0, x)
        else:
            leaving = batches.pop(0)
            batches.append(x)
        held[here, product[x]] -= 1
        held[there, product[leaving]] += 1
        location[leaving], location[x] = there, None
        steps += 1


def main(argv: list[str] | None = None, tankage: bool = True) -> int:
    title = "Pipesworld (tankage)" if tankage else "Pipesworld (no tankage)"
    parser = argparse.ArgumentParser(description=f"Generate an IPC-2004 {title} PDDL problem.")
    parser.add_argument("-n", "--network", type=int, required=True, help="IPC network 1-5")
    parser.add_argument("-b", "--num-batches", type=int, required=True)
    parser.add_argument("-g", "--num-goals", type=int, required=True)
    if tankage:
        parser.add_argument("-t", "--tankage", type=int, default=50, help="tank slots in percent (default 50)")
    parser.add_argument("--seed", type=int)
    args = vars(parser.parse_args(argv))
    args.setdefault("tankage", None)
    try:
        problem = make_problem(**args)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
