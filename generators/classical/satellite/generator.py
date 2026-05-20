#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time

MODE_NAMES = ["infrared", "image", "spectrograph", "thermograph"]


def make_problem(
    num_satellites: int,
    num_instruments: int,
    num_modes: int,
    num_targets: int,
    num_observations: int,
    seed: int | None = None,
) -> str | None:
    if min(num_satellites, num_instruments, num_modes, num_targets, num_observations) < 1:
        return None

    rng = random.Random(seed if seed is not None else int(time.time()))
    satellites = [f"satellite{i}" for i in range(num_satellites)]
    instruments = [f"instrument{i}" for i in range(num_instruments)]
    modes = [f"{MODE_NAMES[i % len(MODE_NAMES)]}{i}" for i in range(num_modes)]
    targets = [f"target{i}" for i in range(num_targets)]
    observations = [f"observation{i}" for i in range(num_observations)]
    directions = targets + observations

    init_facts = []
    for satellite in satellites:
        init_facts.append(f"    (power_avail {satellite})")
        init_facts.append(f"    (pointing {satellite} {rng.choice(directions)})")

    instrument_modes: dict[str, list[str]] = {}
    for index, instrument in enumerate(instruments):
        satellite = satellites[index % len(satellites)]
        calibration_target = targets[index % len(targets)]
        init_facts.append(f"    (on_board {instrument} {satellite})")
        init_facts.append(f"    (calibration_target {instrument} {calibration_target})")
        supported = {modes[index % len(modes)], rng.choice(modes)}
        instrument_modes[instrument] = sorted(supported)
        init_facts.extend(f"    (supports {instrument} {mode})" for mode in instrument_modes[instrument])

    goals = []
    for index, observation in enumerate(observations):
        instrument = instruments[index % len(instruments)]
        mode = rng.choice(instrument_modes[instrument])
        goals.append(f"      (have_image {observation} {mode})")

    return f'''(define (problem satellite-s{num_satellites}-i{num_instruments}-m{num_modes}-t{num_targets}-o{num_observations})
  (:domain satellite)
  (:objects
    {' '.join(satellites)} - satellite
    {' '.join(instruments)} - instrument
    {' '.join(modes)} - mode
    {' '.join(directions)} - direction
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{chr(10).join(goals)}
    )
  )
)
'''


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Satellite PDDL problem.")
    parser.add_argument("num_satellites", type=int)
    parser.add_argument("num_instruments", type=int)
    parser.add_argument("num_modes", type=int)
    parser.add_argument("num_targets", type=int)
    parser.add_argument("num_observations", type=int)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)

    problem = make_problem(args.num_satellites, args.num_instruments, args.num_modes, args.num_targets, args.num_observations, args.seed)
    if problem is None:
        parser.error("all dimensions must be at least 1")
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
