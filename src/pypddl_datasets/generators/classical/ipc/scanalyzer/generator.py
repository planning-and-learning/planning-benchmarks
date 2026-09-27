#!/usr/bin/env python3
# Port of autoscale/pddl-generators/scanalyzer/generator.py (non-"simple"
# problem types, as called by Autoscale 21.11). The upstream generator is
# deterministic: its --seed is never used, so it is not offered here.

from __future__ import annotations

import argparse
import sys

SEGMENT_TYPES = ("empty", "ab")
INOUT_TYPES = ("none", "in", "both")


def make_problem(size: int, segment_type: str = "empty", inout: str = "in") -> str:
    """Generate a Scanalyzer3D task with ``size`` in and ``size`` out segments.

    ``segment_type`` "ab" splits every segment into halves a/b (4-cycles and a
    permuted goal), "empty" keeps whole segments (2-cycles). ``inout`` selects
    which segments are connected to the analysis station: only segment 1 on
    each side ("none"), all in-segments ("in"), or all segments ("both").
    """
    if not isinstance(size, int) or isinstance(size, bool) or size < 1:
        raise ValueError("size must be an integer at least 1")
    if segment_type not in SEGMENT_TYPES:
        raise ValueError(f"segment_type must be one of {SEGMENT_TYPES}")
    if inout not in INOUT_TYPES:
        raise ValueError(f"inout must be one of {INOUT_TYPES}")

    halves = ["a", "b"] if segment_type == "ab" else [""]
    num_in, num_out = {"none": (1, 1), "in": (size, 1), "both": (size, size)}[inout]
    perm = [0, *range(size - 1, 0, -1)]
    opposite = {"in": "out", "out": "in"}

    objects: list[str] = []
    init: list[str] = []
    goal: list[str] = []
    for seg in range(1, size + 1):
        for direction in ("in", "out"):
            for half in halves:
                objects.append(f"seg-{direction}-{seg}{half} - segment")
                objects.append(f"car-{direction}-{seg}{half} - car")
                init.append(f"(on car-{direction}-{seg}{half} seg-{direction}-{seg}{half})")
                goal.append(f"(analyzed car-{direction}-{seg}{half})")
            if len(halves) == 1:
                goal.append(f"(on car-{direction}-{seg} seg-{direction}-{seg})")
            else:
                goal.append(f"(on car-{direction}-{seg}b seg-{direction}-{seg}a)")
                goal.append(f"(on car-{direction}-{seg}a seg-{opposite[direction]}-{perm[seg - 1] + 1}b)")
        for seg2 in range(1, size + 1):
            if len(halves) == 1:
                init.append(f"(CYCLE-2 seg-in-{seg} seg-out-{seg2})")
            else:
                init.append(f"(CYCLE-4 seg-in-{seg}a seg-in-{seg}b seg-out-{seg2}a seg-out-{seg2}b)")
    for in_seg in range(1, num_in + 1):
        for out_seg in range(1, num_out + 1):
            if len(halves) == 1:
                init.append(f"(CYCLE-2-WITH-ANALYSIS seg-in-{in_seg} seg-out-{out_seg})")
            else:
                init.append(
                    f"(CYCLE-4-WITH-ANALYSIS seg-in-{in_seg}a seg-in-{in_seg}b seg-out-{out_seg}a seg-out-{out_seg}b)"
                )
    init.append("(= (total-cost) 0)")

    return (f"""(define (problem scanalyzer3d-{size}-{segment_type}-{inout})
  (:domain scanalyzer3d)
  (:objects
{chr(10).join(f"    {line}" for line in sorted(objects))}
  )
  (:init
{chr(10).join(f"    {line}" for line in sorted(init))}
  )
  (:goal
    (and
{chr(10).join(f"      {line}" for line in sorted(goal))}
    )
  )
  (:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Scanalyzer3D PDDL problem.")
    parser.add_argument("size", type=int)
    parser.add_argument("segment_type", choices=SEGMENT_TYPES)
    parser.add_argument("inout", choices=INOUT_TYPES)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
