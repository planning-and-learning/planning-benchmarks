#!/usr/bin/env python3
# Reconstructed from the IPC 2023 numeric drone tasks (no generator was published):
# every point of an X x Y x Z grid is a location to visit, battery 2 * (X + Y + Z) + 1.

from __future__ import annotations

import argparse
import sys


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(size_x: int, size_y: int, size_z: int) -> str:
    """Generate a Drone task over all points of a ``size_x x size_y x size_z`` grid.

    The drone starts at the origin (the recharge point) with a full battery of
    ``2 * (size_x + size_y + size_z) + 1`` and must visit every grid point and
    return to the origin. The bounds are ``0 .. size`` per axis, as in the IPC
    tasks, so the drone may leave the grid by one step.
    """
    for name, value in (("size_x", size_x), ("size_y", size_y), ("size_z", size_z)):
        if not _is_int(value) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")

    points = [(x, y, z) for x in range(size_x) for y in range(size_y) for z in range(size_z)]
    names = [f"x{x}y{y}z{z}" for x, y, z in points]
    battery = 2 * (size_x + size_y + size_z) + 1
    coords = "\n".join(
        f"(= (xl {n}) {x})\n(= (yl {n}) {y})\n(= (zl {n}) {z})" for n, (x, y, z) in zip(names, points)
    )
    return (f""";;Instance with {size_x}x{size_y}x{size_z} points
(define (problem name) (:domain domain_name)
(:objects
{chr(10).join(f"{n} - location" for n in names)}
)
(:init (= (x) 0) (= (y) 0) (= (z) 0)
 (= (min_x) 0)  (= (max_x) {size_x})
 (= (min_y) 0)  (= (max_y) {size_y})
 (= (min_z) 0)  (= (max_z) {size_z})
{coords}
(= (battery-level) {battery})
(= (battery-level-full) {battery})
)
(:goal (and
{chr(10).join(f"(visited {n})" for n in names)}
(= (x) 0) (= (y) 0) (= (z) 0) ))
);; end of the problem instance
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Drone PDDL problem.")
    parser.add_argument("size_x", type=int)
    parser.add_argument("size_y", type=int)
    parser.add_argument("size_z", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.size_x, args.size_y, args.size_z)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
