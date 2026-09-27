#!/usr/bin/env python3
# Factory Robot (IPC 2026 numeric, domain by Joan Espasa Arxer). The IPC tasks name
# their call (`generate.py --robots R --stations S --workload W --max-temp T --seed 42`)
# but the script was not published; this reconstructs it from the 20 tasks.

from __future__ import annotations

import argparse
import random
import sys

CAPACITIES = (80, 100, 120, 150)
WORK_COSTS = (8, 10, 12, 15)
COOLING_POWERS = (4, 6)


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(
    num_robots: int = 2,
    num_stations: int | None = None,
    workload: int = 40,
    max_temp: int = 20,
    seed: int | None = None,
) -> str:
    """Generate a Factory Robot task.

    Stations ``charging``, ``cooling`` and ``assembly0..`` form a complete graph
    (``num_stations`` defaults to ``num_robots + 3``); only ``cooling`` cools (power
    4 or 6) and calibrates, only ``charging`` charges. Robots start calibrated on
    distinct random stations with energy capacity - U(0..20); capacity, work cost,
    max temperature (``max_temp`` + U(0..5)) and efficiency U(2..4) are drawn per
    robot. Every robot must reach workload ``workload`` + U(-2..2); robot r0 must
    also end at temperature <= ``max_temp``.
    """
    num_stations = num_robots + 3 if num_stations is None else num_stations
    for name, value, minimum in (("num_robots", num_robots, 1), ("num_stations", num_stations, 3),
                                 ("workload", workload, 3), ("max_temp", max_temp, 0)):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_stations < num_robots + 2:
        raise ValueError("num_stations must be at least num_robots + 2 (robots need free stations to move)")

    rng = random.Random(seed)
    stations = ["charging", "cooling", *(f"assembly{i}" for i in range(num_stations - 2))]
    robots = [f"r{i}" for i in range(num_robots)]
    starts = rng.sample(stations, num_robots)
    cooling_power = rng.choice(COOLING_POWERS)
    specs: list[dict[str, int]] = []
    for _ in robots:
        capacity = rng.choice(CAPACITIES)
        specs.append({  # drawn in key order
            "capacity": capacity,
            "energy": capacity - rng.randint(0, 20),
            "work_cost": rng.choice(WORK_COSTS),
            "max_temp": max_temp + rng.randint(0, 5),
            "efficiency": rng.randint(2, 4),
        })
    targets = [workload + rng.randint(-2, 2) for _ in robots]

    init = [f"(at {r} {s})" for r, s in zip(robots, starts)]
    init += [f"(connected {a} {b})" for a in stations for b in stations if a != b]
    init += ["(has-charger charging)", "(has-calibrator cooling)"]
    init += [f"(free {s})" for s in stations if s not in starts]
    init += [f"(calibrated {r})" for r in robots]
    init.append("")
    for fluent, key in (("energy", "energy"), ("workload", None), ("temperature", None), ("production", None)):
        init += [f"(= ({fluent} {r}) {spec[key] if key else 0})" for r, spec in zip(robots, specs)]
    init.append("")
    for fluent, key in (
        ("capacity", "capacity"), ("work-cost", "work_cost"), ("max-temp", "max_temp"), ("efficiency", "efficiency")
    ):
        init += [f"(= ({fluent} {r}) {spec[key]})" for r, spec in zip(robots, specs)]
    init += [f"(= (cooling-power {s}) {cooling_power if s == 'cooling' else 0})" for s in stations]
    goal = [f"(>= (workload {r}) {t})" for r, t in zip(robots, targets)] + [f"(<= (temperature r0) {max_temp})"]

    return (f"""(define (problem factory-{num_robots}r-{num_stations}s)
  (:domain factory-robot)

  (:objects
    {' '.join(robots)} - robot
    {' '.join(stations)} - station
  )

  (:init
{chr(10).join(("    " + fact) if fact else "" for fact in init)}
  )

  (:goal (and
{chr(10).join("    " + g for g in goal)}
  ))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Factory Robot PDDL problem.")
    parser.add_argument("--robots", dest="num_robots", type=int, default=2)
    parser.add_argument("--stations", dest="num_stations", type=int)
    parser.add_argument("--workload", type=int, default=40)
    parser.add_argument("--max-temp", type=int, default=20)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
