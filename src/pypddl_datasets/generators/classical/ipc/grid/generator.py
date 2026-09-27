#!/usr/bin/env python3
# Port of pddl-generators grid/generate.py. style="ipc" (default) follows the
# AIPS-1998 tasks in downward-benchmarks/grid: all locks share one shape and
# form a connected region, goals are uniform over all cells, IPC names.
# style="autoscale" is upstream generate.py as called by Autoscale 21.11.

from __future__ import annotations

import argparse
from collections import defaultdict
import random
import sys
import time


STYLES = ("ipc", "autoscale")
IPC_SHAPES = ("triangle", "diamond", "square", "circle")


def pos_name(pos: tuple[int, int], prefix: str = "pos") -> str:
    return f"{prefix}{pos[0]}-{pos[1]}"


def grow_region(positions: list[tuple[int, int]], size: int, rng: random.Random) -> list[tuple[int, int]]:
    """A connected set of ``size`` cells grown from a random cell."""
    position_set = set(positions)
    region = [rng.choice(positions)]
    while len(region) < size:
        frontier = sorted({q for p in region for q in adjacent_positions(p, position_set)} - set(region))
        region.append(rng.choice(frontier))
    return region


def adjacent_positions(pos: tuple[int, int], positions: set[tuple[int, int]]) -> list[tuple[int, int]]:
    x, y = pos
    return [candidate for candidate in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)) if candidate in positions]


def join_facts(facts: list[str]) -> str:
    return "\n".join(f"       {fact}" for fact in facts)

def make_problem(
    width: int,
    height: int,
    num_shapes: int | None = None,
    num_keys: int | None = None,
    num_locks: int | None = None,
    goal_probability: float | None = None,
    seed: int | None = None,
    style: str = "ipc",
) -> str | None:
    """Generate a Grid task, or None for invalid parameters.

    Defaults per style: "ipc" 4 shapes, max(width, height) + 4 keys,
    cells // 4 locks and goal probability 0.35 (the IPC tasks' averages);
    "autoscale" 2 shapes, 2 keys, 2 locks, goal probability 1.0 (upstream).
    """
    if style not in STYLES:
        raise ValueError(f"style must be one of {STYLES}")
    ipc = style == "ipc"
    if num_shapes is None:
        num_shapes = 4 if ipc else 2
    if num_keys is None:
        num_keys = max(width, height) + 4 if ipc else 2
    if num_locks is None:
        num_locks = width * height // 4 if ipc else 2
    if goal_probability is None:
        goal_probability = 0.35 if ipc else 1.0
    if width < 2 or height < 2:
        return None
    positions = [(x, y) for x in range(width) for y in range(height)]
    # IPC style: all locks share one shape, so one lock suffices.
    if num_shapes < 1 or num_keys < num_shapes or num_locks < (1 if ipc else num_shapes) or num_locks >= len(positions):
        return None
    if not 0.0 < goal_probability <= 1.0:
        return None

    rng = random.Random(seed if seed is not None else int(time.time()))
    position_set = set(positions)
    locked_positions = grow_region(positions, num_locks, rng) if ipc else rng.sample(positions, k=num_locks)
    open_positions = [pos for pos in positions if pos not in locked_positions]
    robot_pos = rng.choice(open_positions)

    keys = [f"key{k}" for k in range(num_keys)]
    shapes = [IPC_SHAPES[k] if ipc and k < len(IPC_SHAPES) else f"shape{k}" for k in range(num_shapes)]
    key_shapes = [shapes[k] if k < num_shapes else rng.choice(shapes) for k in range(num_keys)]
    if ipc:
        lock_shapes = [rng.choice(shapes)] * num_locks
    else:
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

        if not reachable_locked:  # walk reached every cell; upstream just ends the loop here
            break

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

        newly_reached = [
            locked_pos for locked_pos in sorted(reachable_locked) if locked_pos_to_shape[locked_pos] == shape
        ]
        reachable_locations.extend(newly_reached)
        reachable_locked = {p for p in reachable_locked if locked_pos_to_shape[p] != shape}

    for key in keys:
        key_positions.setdefault(key, rng.choice(positions))

    prefix = "node" if ipc else "pos"

    def name(pos: tuple[int, int]) -> str:
        return pos_name(pos, prefix)

    def destination(key: str) -> tuple[int, int]:
        # IPC goals may coincide with the key's start (1 of 19); upstream excludes it.
        return rng.choice(positions if ipc else [pos for pos in positions if pos != key_positions[key]])

    nodes = [name(pos) for pos in positions]
    conn_facts = [f"(conn {name(p)} {name(q)})" for p in positions for q in adjacent_positions(p, position_set)]
    locked_facts = [f"(locked {name(pos)})" for pos in locked_positions]
    lock_shape_facts = [f"(lock-shape {name(pos)} {locked_pos_to_shape[pos]})" for pos in locked_positions]
    open_facts = [f"(open {name(pos)})" for pos in open_positions]
    key_shape_facts = [f"(key-shape {key} {shape})" for key, shape in zip(keys, key_shapes)]
    key_at_facts = [f"(at {key} {name(key_positions[key])})" for key in keys]

    goal_facts = [f"(at {key} {name(destination(key))})" for key in keys if rng.random() < goal_probability]
    if not goal_facts:
        key = rng.choice(keys)
        goal_facts.append(f"(at {key} {name(destination(key))})")

    init_facts = (["(arm-empty)"] + [f"(place {node})" for node in nodes] + [f"(shape {shape})" for shape in shapes]
                  + [f"(key {key})" for key in keys] + conn_facts + locked_facts + lock_shape_facts + open_facts
                  + key_shape_facts + key_at_facts + [f"(at-robot {name(robot_pos)})"])
    problem_name = f"grid-{width}-{height}-{num_shapes}-{num_keys}-{num_locks}"

    return (f'''(define (problem {problem_name})
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
''').lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Grid PDDL problem.")
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    parser.add_argument("--shapes", type=int, help="default: 4 (ipc) / 2 (autoscale)")
    parser.add_argument("--keys", type=int, help="default: max(width, height) + 4 (ipc) / 2 (autoscale)")
    parser.add_argument("--locks", type=int, help="default: cells // 4 (ipc) / 2 (autoscale)")
    parser.add_argument("--prob-goal", type=float, help="default: 0.35 (ipc) / 1.0 (autoscale)")
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--style", choices=STYLES, default="ipc")
    args = parser.parse_args(argv)

    problem = make_problem(
        args.width, args.height, args.shapes, args.keys, args.locks, args.prob_goal, args.seed, args.style
    )
    if problem is None:
        parser.error("invalid or unsolvable grid configuration")
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
