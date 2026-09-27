#!/usr/bin/env python3

# Port of pddl-generators/satellite/satgen.cc (STRIPS): `satgen <seed> <#satellites>
# <max instruments> <#modes> <#targets> <#observations>`. The default is the IPC 2002
# distribution and untyped encoding. Autoscale 21.11 uses the typed encoding and two
# 2021 patches (`patched`): every observation is interesting and every mode is
# supported by some instrument.

from __future__ import annotations

import argparse
import random
import sys
from typing import cast

MODE_TYPES = ("infrared", "image", "spectrograph", "thermograph")


def make_problem(
    num_satellites: int,
    max_instruments: int,
    num_modes: int,
    num_targets: int,
    num_observations: int,
    seed: int | None = None,
    typed: bool = False,
    patched: bool = False,
) -> str:
    for name, value in (
        ("num_satellites", num_satellites),
        ("max_instruments", max_instruments),
        ("num_modes", num_modes),
        ("num_targets", num_targets),
        ("num_observations", num_observations),
    ):
        checked = cast(object, value)  # runtime check: callers may pass any type
        if not isinstance(checked, int) or isinstance(checked, bool) or checked < 1:
            raise ValueError(f"{name} must be an integer at least 1")

    rng = random.Random(seed)

    def rnd(limit: int) -> int:
        # satgen's rnd(): uniform in [0, limit), and 0 for limit 0.
        return int(limit * rng.random())

    modes = [f"{rng.choice(MODE_TYPES)}{i}" for i in range(num_modes)]
    targets = [f"{rng.choice(('Star', 'GroundStation'))}{i}" for i in range(num_targets)]
    observations: list[str] = []
    images: list[list[str]] = []
    for i in range(num_targets, num_targets + num_observations):
        observations.append(f"{rng.choice(('Star', 'Phenomenon', 'Planet'))}{i}")
        interesting = patched or rnd(10) < 9  # unpatched satgen: 9 in 10 observations get goals
        chosen = rng.sample(modes, 1 + rnd(num_modes // 3))
        images.append(chosen if interesting else [])
    directions = targets + observations

    # (start, end, interesting, instruments); instrument = (modes, calibration targets)
    satellites: list[tuple[str, str, bool, list[tuple[list[str], list[str]]]]] = []
    supported: set[str] = set()
    for _ in range(num_satellites):
        start, end = rng.choice(directions), rng.choice(directions)
        interesting = rnd(5) < 2
        instruments: list[tuple[list[str], list[str]]] = []
        for _ in range(1 + rnd(max_instruments)):
            instrument_modes = rng.sample(modes, min(1 + rnd(3), num_modes))
            supported.update(instrument_modes)
            instruments.append((instrument_modes, rng.sample(targets, 1 + rnd(num_targets // 3))))
        satellites.append((start, end, interesting, instruments))
    # ponytail: upstream walks the modes in random order; each unsupported mode
    # draws its host independently, so a fixed order gives the same distribution.
    for mode in modes if patched else []:
        if mode not in supported:
            instruments = satellites[rnd(num_satellites)][3]
            instruments[rnd(len(instruments))][0].append(mode)

    objects: list[str] = []
    init_facts: list[str] = []
    goals: list[str] = []
    instrument_id = 0

    def declare(name: str, type_name: str) -> str:
        return f"{name} - {type_name}" if typed else name

    def kind(fact: str) -> list[str]:
        return [] if typed else [f"({fact})"]

    for satellite_id, (start, end, interesting, instruments) in enumerate(satellites):
        satellite = f"satellite{satellite_id}"
        objects.append(declare(satellite, "satellite"))
        init_facts += kind(f"satellite {satellite}")
        on_board: list[str] = []
        for instrument_modes, calibration_targets in instruments:
            instrument = f"instrument{instrument_id}"
            instrument_id += 1
            objects.append(declare(instrument, "instrument"))
            init_facts += kind(f"instrument {instrument}")
            init_facts.extend(f"(supports {instrument} {mode})" for mode in instrument_modes)
            init_facts.extend(f"(calibration_target {instrument} {target})" for target in calibration_targets)
            on_board.append(f"(on_board {instrument} {satellite})")
        init_facts += on_board
        init_facts.extend((f"(power_avail {satellite})", f"(pointing {satellite} {start})"))
        if interesting:
            goals.append(f"(pointing {satellite} {end})")
    objects.extend(declare(mode, "mode") for mode in modes)
    objects.extend(declare(direction, "direction") for direction in directions)
    for mode in modes:
        init_facts += kind(f"mode {mode}")
    for direction in directions:
        init_facts += kind(f"direction {direction}")
    for observation, observation_modes in zip(observations, images):
        goals.extend(f"(have_image {observation} {mode})" for mode in observation_modes)

    name = f"satellite-s{num_satellites}-i{max_instruments}-m{num_modes}-t{num_targets}-o{num_observations}"
    return (f"""(define (problem {name})
  (:domain satellite)
  (:objects
{chr(10).join(f"    {line}" for line in objects)}
  )
  (:init
{chr(10).join(f"    {fact}" for fact in init_facts)}
  )
  (:goal
    (and
{chr(10).join(f"      {goal}" for goal in goals)}
    )
  )
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Satellite PDDL problem (satgen distribution).")
    parser.add_argument("--num-satellites", type=int, required=True)
    parser.add_argument(
        "--max-instruments", type=int, default=3, help="maximum instruments per satellite (Autoscale: 3)"
    )
    parser.add_argument("--num-modes", type=int, required=True)
    parser.add_argument("--num-targets", type=int, required=True)
    parser.add_argument("--num-observations", type=int, required=True)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--typed", action="store_true", help="typed encoding instead of type predicates")
    parser.add_argument(
        "--patched",
        action="store_true",
        help="Autoscale 2021 patches: all observations interesting, all modes supported",
    )
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
