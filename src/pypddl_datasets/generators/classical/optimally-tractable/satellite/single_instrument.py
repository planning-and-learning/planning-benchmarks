#!/usr/bin/env python3
"""Satellite as generated for the IPC with one satellite, one instrument supporting every mode, and image goals only.

Directions, calibration targets, the initial pointing and the image goals are drawn
as by the IPC generator (ipc/satellite, satgen): num_targets calibration-target
directions and num_observations observation directions; the instrument calibrates at
1 + rnd(num_targets / 3) random targets; the satellite points at a random direction;
nine in ten observations are interesting and want 1 + rnd(num_modes / 3) random modes
(a draw without any image goal is repeated). The restriction drops the IPC's pointing
goal (two in five satellites) and lets the one instrument support every mode instead
of one to three.

The instrument must be switched on and calibrated (pointing at one of its targets)
before any image, and stays calibrated; image directions are never targets. Optimal
cost: switch_on + calibrate + one take_image per goal + one turn to a target unless
already pointing at one + one turn per direction with an image goal.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_targets: int, num_observations: int, num_modes: int, seed: int | None = None) -> str:
    for name, value in (("num_targets", num_targets), ("num_observations", num_observations), ("num_modes", num_modes)):
        if value < 1:
            raise ValueError(f"{name} must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))

    def rnd(limit: int) -> int:
        # satgen's rnd(): uniform in [0, limit), and 0 for limit 0.
        return int(limit * rng.random())

    modes = [f"mode{i}" for i in range(num_modes)]
    targets = [f"target{i}" for i in range(num_targets)]
    observations = [f"observation{i}" for i in range(num_observations)]
    images: list[tuple[str, str]] = []
    while not images:  # the IPC leaves a task without goals with probability 0.1^observations; redraw those
        for observation in observations:
            interesting = rnd(10) < 9
            chosen = rng.sample(modes, 1 + rnd(num_modes // 3))
            images.extend((observation, mode) for mode in chosen if interesting)
    directions = targets + observations
    pointing = rng.choice(directions)
    calibration_targets = rng.sample(targets, 1 + rnd(num_targets // 3))
    cost = 2 + len(images) + (pointing not in calibration_targets) + len({direction for direction, _ in images})
    init = [
        "(satellite satellite0)",
        "(instrument instrument0)",
        "(on_board instrument0 satellite0)",
        "(power_avail satellite0)",
        f"(pointing satellite0 {pointing})",
        *(f"(calibration_target instrument0 {target})" for target in calibration_targets),
        *(f"(mode {mode})\n    (supports instrument0 {mode})" for mode in modes),
        *(f"(direction {direction})" for direction in directions),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem satellite-single-instrument-t{num_targets}-o{num_observations}-m{num_modes})
  (:domain satellite)
  (:objects satellite0 instrument0 {' '.join([*modes, *directions])})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (have_image {direction} {mode})' for direction, mode in images)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Satellite task with one instrument supporting every mode.")
    parser.add_argument("-t", "--num-targets", type=int, required=True, help="calibration-target directions")
    parser.add_argument("-o", "--num-observations", type=int, required=True, help="observation directions")
    parser.add_argument("-m", "--num-modes", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_targets, args.num_observations, args.num_modes, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
