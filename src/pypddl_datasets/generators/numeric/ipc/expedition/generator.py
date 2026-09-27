#!/usr/bin/env python3
# Reconstructed from the IPC 2023/2026 numeric expedition tasks (no generator was published).

from __future__ import annotations

import argparse
import string
import sys


def make_problem(
    num_waypoints: int,
    num_sleds: int = 2,
    separate_tracks: bool = False,
    capacity: int = 4,
    initial_supplies: int = 1,
    depot_supplies: int = 1000,
) -> str:
    """Generate an Expedition task.

    Sleds start at the first waypoint of a chain of ``num_waypoints`` waypoints
    (``wa0 .. wa<n-1>``) and must all reach its last waypoint. Only the first
    waypoint holds supplies (``depot_supplies``). With ``separate_tracks`` every
    sled gets its own chain (``wa``, ``wb``, ...) and depot. Every sled starts with
    ``initial_supplies`` and holds at most ``capacity``.
    """
    for name, value, minimum in (
        ("num_waypoints", num_waypoints, 2),
        ("num_sleds", num_sleds, 1),
        ("capacity", capacity, 1),
        ("initial_supplies", initial_supplies, 0),
        ("depot_supplies", depot_supplies, 0),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if initial_supplies > capacity:
        raise ValueError("initial_supplies must not exceed capacity")
    if separate_tracks and num_sleds > len(string.ascii_lowercase):
        raise ValueError(f"num_sleds must be at most {len(string.ascii_lowercase)} with separate tracks")

    num_tracks = num_sleds if separate_tracks else 1
    tracks = [[f"w{string.ascii_lowercase[t]}{i}" for i in range(num_waypoints)] for t in range(num_tracks)]
    sleds = [f"s{i}" for i in range(num_sleds)]

    init = []
    for i, sled in enumerate(sleds):
        track = tracks[i % num_tracks]
        init += [f"(at {sled} {track[0]})", f"(= (sled_capacity {sled}) {capacity})", f"(= (sled_supplies {sled}) {initial_supplies})"]
        if i < num_tracks:  # each chain is listed once, after its first sled
            init += [f"(= (waypoint_supplies {w}) {depot_supplies if j == 0 else 0})" for j, w in enumerate(track)]
            init += [f"(is_next {a} {b})" for a, b in zip(track, track[1:])]
    goals = [f"(at {sled} {tracks[i % num_tracks][-1]})" for i, sled in enumerate(sleds)]
    waypoints = " ".join(w for track in tracks for w in track)

    return (f"""(define (problem instance_{num_sleds}_sled_{num_waypoints - 5})

	(:domain expedition)

	(:objects
		{" ".join(sleds)} - sled
		{waypoints} - waypoint
	)

  (:init
{chr(10).join(chr(9) * 2 + fact for fact in init)}
	)

	(:goal
		(and
{chr(10).join(chr(9) * 3 + goal for goal in goals)}
		)
	)
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Expedition PDDL problem.")
    parser.add_argument("num_waypoints", type=int, help="waypoints per chain")
    parser.add_argument("-s", "--num-sleds", type=int, default=2)
    parser.add_argument("--separate-tracks", action="store_true", help="one chain and depot per sled")
    parser.add_argument("--capacity", type=int, default=4)
    parser.add_argument("--initial-supplies", type=int, default=1)
    parser.add_argument("--depot-supplies", type=int, default=1000)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
