#!/usr/bin/env python3
"""Satellite with one satellite carrying one instrument that supports every mode.

The instrument must be switched on and calibrated (pointing at its calibration
target) before any image, and stays calibrated. Optimal cost: switch_on + calibrate
+ one take_image per goal + one turn to the calibration target unless already
pointing there + one turn per other direction with an image goal.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_directions: int, num_modes: int, num_images: int, seed: int | None = None) -> str:
    if num_directions < 1 or num_modes < 1:
        raise ValueError("num_directions and num_modes must be at least 1")
    if not 1 <= num_images <= num_directions * num_modes:
        raise ValueError("num_images must be between 1 and num_directions * num_modes")
    rng = random.Random(seed if seed is not None else int(time.time()))
    directions = [f"direction{i}" for i in range(num_directions)]
    modes = [f"mode{i}" for i in range(num_modes)]
    images = rng.sample([(d, m) for d in directions for m in modes], num_images)
    pointing, target = rng.choice(directions), rng.choice(directions)
    cost = 2 + num_images + (pointing != target) + len({d for d, _ in images} - {target})
    init = [
        "(satellite satellite0)",
        "(instrument instrument0)",
        "(on_board instrument0 satellite0)",
        "(power_avail satellite0)",
        f"(pointing satellite0 {pointing})",
        f"(calibration_target instrument0 {target})",
        *(f"(mode {mode})\n    (supports instrument0 {mode})" for mode in modes),
        *(f"(direction {direction})" for direction in directions),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem satellite-single-instrument-d{num_directions}-m{num_modes}-i{num_images})
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
    parser = argparse.ArgumentParser(description="Generate a single-instrument Satellite task.")
    parser.add_argument("-d", "--num-directions", type=int, required=True)
    parser.add_argument("-m", "--num-modes", type=int, required=True)
    parser.add_argument("-i", "--num-images", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_directions, args.num_modes, args.num_images, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
