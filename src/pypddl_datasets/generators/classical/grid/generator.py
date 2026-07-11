#!/usr/bin/env python3

from __future__ import annotations

import argparse
from collections import defaultdict
import random
import sys
import time


def pos_name(pos: tuple[int, int]) -> str:
    return f"pos{pos[0]}-{pos[1]}"


def adjacent_positions(pos: tuple[int, int], positions: set[tuple[int, int]]) -> list[tuple[int, int]]:
    x, y = pos
    return [candidate for candidate in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)) if candidate in positions]


def join_facts(facts: list[str]) -> str:
    return "\n".join(f"       {fact}" for fact in facts)

def make_problem(
    width: int,
    height: int,
    num_shapes: int = 2,
    num_keys: int = 2,
    num_locks: int = 2,
    goal_probability: float = 1.0,
    seed: int | None = None,
) -> str | None:
    if width < 2 or height < 2:
        return None
    positions = [(x, y) for x in range(width) for y in range(height)]
    if num_shapes < 1 or num_keys < num_shapes or num_locks < num_shapes or num_locks >= len(positions):
        return None
    if not 0.0 < goal_probability <= 1.0:
        return None

    rng = random.Random(seed if seed is not None else int(time.time()))
    position_set = set(positions)
    locked_positions = rng.sample(positions, k=num_locks)
    open_positions = [pos for pos in positions if pos not in locked_positions]
    robot_pos = rng.choice(open_positions)

    keys = [f"key{k}" for k in range(num_keys)]
    shapes = [f"shape{k}" for k in range(num_shapes)]
    key_shapes = [shapes[k] if k < num_shapes else rng.choice(shapes) for k in range(num_keys)]
    lock_shapes = [shapes[k] if k < num_shapes else rng.choice(shapes) for k in range(num_locks)]
    locked_pos_to_shape = dict(zip(locked_positions, lock_shapes))

    shape_to_keys: dict[str, list[str]] = defaultdict(list)
    for key, shape in zip(keys, key_shapes):
        shape_to_keys[shape].append(key)

    key_positions: dict[str, tuple[int, int]] = {}
    reachable_locked: set[tuple[int, int]] = set()
    reachable_locations = [robot_pos]
    unlocked_positions = list(open_positions)
    index = 0
    while len(reachable_locations) < len(positions):
        while index < len(reachable_locations):
            loc = reachable_locations[index]
            for pos in adjacent_positions(loc, position_set):
                if pos in reachable_locations:
                    continue
                if pos in unlocked_positions:
                    reachable_locations.append(pos)
                else:
                    reachable_locked.add(pos)
            index += 1

        if not reachable_locked:
            return None

        pos = rng.choice(sorted(reachable_locked))
        shape = locked_pos_to_shape[pos]
        shape_keys = shape_to_keys[shape]
        sure_key = rng.choice(shape_keys)
        for key in shape_keys:
            if key not in key_positions:
                key_positions[key] = rng.choice(reachable_locations if key == sure_key else positions)

        for locked_pos, locked_shape in locked_pos_to_shape.items():
            if locked_shape == shape and locked_pos not in unlocked_positions:
                unlocked_positions.append(locked_pos)

        newly_reached = [locked_pos for locked_pos in sorted(reachable_locked) if locked_pos_to_shape[locked_pos] == shape]
        reachable_locations.extend(newly_reached)
        reachable_locked = {p for p in reachable_locked if locked_pos_to_shape[p] != shape}

    for key in keys:
        key_positions.setdefault(key, rng.choice(positions))

    nodes = [pos_name(pos) for pos in positions]
    conn_facts = [f"(conn {pos_name(p)} {pos_name(q)})" for p in positions for q in adjacent_positions(p, position_set)]
    locked_facts = [f"(locked {pos_name(pos)})" for pos in locked_positions]
    lock_shape_facts = [f"(lock-shape {pos_name(pos)} {locked_pos_to_shape[pos]})" for pos in locked_positions]
    open_facts = [f"(open {pos_name(pos)})" for pos in open_positions]
    key_shape_facts = [f"(key-shape {key} {shape})" for key, shape in zip(keys, key_shapes)]
    key_at_facts = [f"(at {key} {pos_name(key_positions[key])})" for key in keys]

    goal_facts = []
    for key in keys:
        if rng.random() < goal_probability:
            choices = [pos for pos in positions if pos != key_positions[key]]
            goal_facts.append(f"(at {key} {pos_name(rng.choice(choices))})")
    if not goal_facts:
        key = rng.choice(keys)
        choices = [pos for pos in positions if pos != key_positions[key]]
        goal_facts.append(f"(at {key} {pos_name(rng.choice(choices))})")

    init_facts = (["(arm-empty)"] + [f"(place {node})" for node in nodes] + [f"(shape {shape})" for shape in shapes]
                  + [f"(key {key})" for key in keys] + conn_facts + locked_facts + lock_shape_facts + open_facts
                  + key_shape_facts + key_at_facts + [f"(at-robot {pos_name(robot_pos)})"])
    problem_name = f"grid-{width}-{height}-{num_shapes}-{num_keys}-{num_locks}"

    return f'''(define (problem {problem_name})
  (:domain grid)
  (:objects
    {' '.join(nodes)}
    {' '.join(shapes)}
    {' '.join(keys)}
  )
  (:init
{join_facts(init_facts)}
  )
  (:goal
    (and
{join_facts(goal_facts)}
    )
  )
)
'''


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Grid PDDL problem.")
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    parser.add_argument("--shapes", type=int, default=2)
    parser.add_argument("--keys", type=int, default=2)
    parser.add_argument("--locks", type=int, default=2)
    parser.add_argument("--prob-goal", type=float, default=1.0)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)

    problem = make_problem(args.width, args.height, args.shapes, args.keys, args.locks, args.prob_goal, args.seed)
    if problem is None:
        parser.error("invalid or unsolvable grid configuration")
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
