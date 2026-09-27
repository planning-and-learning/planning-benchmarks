#!/usr/bin/env python3
# Reconstructed from the IPC 2023 numeric delivery tasks (Shleyfman and Kuroiwa; hand-made maps,
# no generator was published). Map families: undirected (tree plus extra doors) as in delivery-x-1..11,
# directed (a cycle through all rooms plus chords) as in delivery-x-12..19.

from __future__ import annotations

import argparse
import random
import string
import sys

ARM_NAMES = {1: ["arm"], 2: ["left", "right"], 3: ["left", "mid", "right"]}


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(
    num_rooms: int,
    num_items: int,
    num_bots: int = 2,
    num_arms: int = 2,
    max_weight: int = 2,
    load_limit: int | None = None,
    directed: bool = False,
    extra_doors: int = 0,
    spread: float = 0.2,
    stay_probability: float = 0.02,
    seed: int | None = None,
) -> str:
    """Generate a Delivery task.

    Rooms ``rooma, roomb, ...`` are connected by doors: undirected maps are a
    random spanning tree plus ``extra_doors`` further two-way doors; directed maps
    are a one-way cycle through all rooms in random order plus ``extra_doors``
    one-way chords, so every map is strongly connected. All bots start in rooma.
    Items weigh uniformly 1..``max_weight``, start in rooma or, with probability
    ``spread``, in a uniform room, and must reach a uniform other room (their
    start with probability ``stay_probability``, as in a few IPC tasks).
    ``load_limit`` defaults to ``2 * num_arms * max_weight``; it must be at
    least ``max_weight`` so every item can be carried.
    """
    for name, value, minimum in (
        ("num_rooms", num_rooms, 1),
        ("num_items", num_items, 1),
        ("num_bots", num_bots, 1),
        ("num_arms", num_arms, 1),
        ("max_weight", max_weight, 1),
        ("extra_doors", extra_doors, 0),
    ):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_rooms > len(string.ascii_lowercase):
        raise ValueError(f"num_rooms must be at most {len(string.ascii_lowercase)}")
    if load_limit is None:
        load_limit = 2 * num_arms * max_weight
    if not _is_int(load_limit) or load_limit < max_weight:
        raise ValueError("load_limit must be an integer at least max_weight")
    for name, value in (("spread", spread), ("stay_probability", stay_probability)):
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"{name} must be in [0, 1]")

    rng = random.Random(seed)
    rooms = [f"room{c}" for c in string.ascii_lowercase[:num_rooms]]
    doors: list[tuple[int, int]] = []
    if directed:
        order = [0] + rng.sample(range(1, num_rooms), num_rooms - 1)
        doors = [(order[i], order[(i + 1) % num_rooms]) for i in range(num_rooms)] if num_rooms > 1 else []
        candidates = [(a, b) for a in range(num_rooms) for b in range(num_rooms) if a != b and (a, b) not in doors]
    else:
        for room in range(1, num_rooms):
            other = rng.randrange(room)
            doors += [(other, room), (room, other)]
        candidates = [(a, b) for a in range(num_rooms) for b in range(a + 1, num_rooms) if (a, b) not in doors]
    if extra_doors > len(candidates):
        raise ValueError(f"extra_doors must be at most {len(candidates)}")
    for a, b in rng.sample(candidates, extra_doors):
        doors += [(a, b)] if directed else [(a, b), (b, a)]

    items = [f"item{i}" for i in range(num_items, 0, -1)]
    bots = [f"bot{b}" for b in range(1, num_bots + 1)]
    arm_names = ARM_NAMES.get(num_arms, [f"arm{j}-" for j in range(1, num_arms + 1)])
    arms = {bot: [f"{name}{b}" for name in arm_names] for b, bot in enumerate(bots, start=1)}
    weight = {item: rng.randint(1, max_weight) for item in items}
    start = {item: rng.randrange(num_rooms) if rng.random() < spread else 0 for item in items}
    goal = {}
    for item in items:
        others = [r for r in range(num_rooms) if r != start[item]]
        goal[item] = start[item] if not others or rng.random() < stay_probability else rng.choice(others)

    init = [f"(= (weight {item}) {weight[item]})" for item in items]
    init += [f"(at-bot {bot} rooma)" for bot in bots]
    init += [f"(free {arm})" for bot in bots for arm in arms[bot]]
    init += [f"(mount {arm} {bot})" for bot in bots for arm in arms[bot]]
    init += [f"(at {item} {rooms[start[item]]})" for item in items]
    init += [f"(door {rooms[a]} {rooms[b]})" for a, b in doors]
    for bot in bots:
        init += [f"(= (current_load {bot}) 0)", f"(= (load_limit {bot}) {load_limit})"]
    init.append("(= (cost) 0)")
    goals = [f"(at {item} {rooms[goal[item]]})" for item in items]
    name = f"delivery-r{num_rooms}-i{num_items}-b{num_bots}-a{num_arms}-{'d' if directed else 'u'}{extra_doors}-{seed}"

    return (f"""(define (problem {name})
   (:domain delivery)
   (:objects {" ".join(rooms)} - room
             {" ".join(items)} - item
             {" ".join(bots)} - bot
             {" ".join(arm for bot in bots for arm in arms[bot])} - arm)
   (:init {(chr(10) + " " * 10).join(init)})
   (:goal (and {(chr(10) + " " * 15).join(goals)}))
   (:metric minimize (cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Delivery PDDL problem.")
    parser.add_argument("num_rooms", type=int)
    parser.add_argument("num_items", type=int)
    parser.add_argument("-b", "--num-bots", type=int, default=2)
    parser.add_argument("-a", "--num-arms", type=int, default=2, help="arms per bot")
    parser.add_argument("-w", "--max-weight", type=int, default=2)
    parser.add_argument("-l", "--load-limit", type=int, help="default: 2 * num_arms * max_weight")
    parser.add_argument("--directed", action="store_true", help="one-way cycle plus chords instead of two-way doors")
    parser.add_argument("-e", "--extra-doors", type=int, default=0)
    parser.add_argument("--spread", type=float, default=0.2, help="probability an item starts outside rooma")
    parser.add_argument("--stay-probability", type=float, default=0.02, help="probability an item's goal is its start")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
