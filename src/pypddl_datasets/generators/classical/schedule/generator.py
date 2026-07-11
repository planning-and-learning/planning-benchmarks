#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time

shapes = ("cylindrical", "circular", "oblong")
colours = ("blue", "yellow", "red", "black")
widths = ("one", "two", "three")
orientations = ("front", "back")
surfaces = ("polished", "rough", "smooth")


def make_problem(
    num_parts: int,
    num_shapes: int = 0,
    num_colours: int = 2,
    num_widths: int = 2,
    num_orientations: int = 2,
    cylindrical_goal_probability: int = 80,
    initial_colour_probability: int = 50,
    goal_colour_probability: int = 80,
    initial_hole_probability: int = 50,
    goal_hole_probability: int = 80,
    goal_surface_probability: int = 50,
    seed: int | None = None,
) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    initial_states = []
    for _ in range(num_parts):
        shape = shapes[rng.randrange(num_shapes + 1)]
        surface = surfaces[rng.randrange(len(surfaces))]
        colour = (
            colours[rng.randrange(num_colours)]
            if rng.randrange(100) < initial_colour_probability
            else None
        )
        hole = (
            (
                widths[rng.randrange(num_widths)],
                orientations[rng.randrange(num_orientations)],
            )
            if rng.randrange(100) < initial_hole_probability
            else None
        )
        initial_states.append((shape, surface, colour, hole))

    goal_states = []
    for _ in range(num_parts):
        shape = (
            "cylindrical"
            if rng.randrange(100) < cylindrical_goal_probability
            else None
        )
        surface = (
            surfaces[rng.randrange(len(surfaces))]
            if rng.randrange(100) < goal_surface_probability
            else None
        )
        colour = (
            colours[rng.randrange(num_colours)]
            if rng.randrange(100) < goal_colour_probability
            else None
        )
        hole = (
            (
                widths[rng.randrange(num_widths)],
                orientations[rng.randrange(num_orientations)],
            )
            if rng.randrange(100) < goal_hole_probability
            else None
        )
        goal_states.append((shape, surface, colour, hole))

    part_names = " ".join(f"p{i}" for i in range(num_parts))
    object_lines = [f"{part_names} - part"]
    if num_shapes:
        shape_names = " ".join(shapes[1 : num_shapes + 1])
        object_lines.append(f"{shape_names} - ashape")
    colour_names = " ".join(colours[:num_colours])
    width_names = " ".join(widths[:num_widths])
    orientation_names = " ".join(orientations[:num_orientations])
    object_lines.extend(
        (
            f"{colour_names} - colour",
            f"{width_names} - width",
            f"{orientation_names} - anorient",
        )
    )

    init_facts = []
    for colour in colours[:num_colours]:
        init_facts.append(f"(has-paint immersion-painter {colour})")
        init_facts.append(f"(has-paint spray-painter {colour})")
    for orientation in orientations[:num_orientations]:
        init_facts.append(f"(can-orient drill-press {orientation})")
        init_facts.append(f"(can-orient punch {orientation})")
    for width in widths[:num_widths]:
        init_facts.append(f"(has-bit drill-press {width})")
        init_facts.append(f"(has-bit punch {width})")

    for i, (shape, surface, colour, hole) in enumerate(initial_states):
        part = f"p{i}"
        init_facts.append(f"(shape {part} {shape})")
        init_facts.append(f"(surface-condition {part} {surface})")
        if colour is not None:
            init_facts.append(f"(painted {part} {colour})")
        if hole is not None:
            init_facts.append(f"(has-hole {part} {hole[0]} {hole[1]})")
        init_facts.append(f"(temperature {part} cold)")

    goal_facts = []
    for i, (shape, surface, colour, hole) in enumerate(goal_states):
        part = f"p{i}"
        if shape is not None:
            goal_facts.append(f"(shape {part} {shape})")
        if surface is not None:
            goal_facts.append(f"(surface-condition {part} {surface})")
        if colour is not None:
            goal_facts.append(f"(painted {part} {colour})")
        if hole is not None:
            goal_facts.append(f"(has-hole {part} {hole[0]} {hole[1]})")

    problem_name = (
        f"schedule-p{num_parts}-s{num_shapes}-c{num_colours}"
        f"-w{num_widths}-o{num_orientations}"
    )
    objects = "\n        ".join(object_lines)
    init = "\n        ".join(init_facts)
    goals = "\n            ".join(goal_facts)

    return f"""(define (problem {problem_name})
    (:domain schedule)
    (:objects
        {objects}
    )
    (:init
        {init}
    )
    (:goal
        (and
            {goals}
        )
    )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="generate a schedule planning problem")
    parser.add_argument("-p", "--num-parts", type=int, required=True)
    parser.add_argument(
        "-s",
        "--num-shapes",
        type=int,
        default=0,
        help="number of non-cylindrical shapes (default: 0)",
    )
    parser.add_argument("-c", "--num-colours", type=int, default=2)
    parser.add_argument("-w", "--num-widths", type=int, default=2)
    parser.add_argument("-o", "--num-orientations", type=int, default=2)
    parser.add_argument(
        "--cylindrical-goal-probability",
        type=int,
        default=80,
    )
    parser.add_argument("--initial-colour-probability", type=int, default=50)
    parser.add_argument("--goal-colour-probability", type=int, default=80)
    parser.add_argument("--initial-hole-probability", type=int, default=50)
    parser.add_argument("--goal-hole-probability", type=int, default=80)
    parser.add_argument("--goal-surface-probability", type=int, default=50)
    parser.add_argument("-r", "--seed", type=int)
    args = parser.parse_args(argv)

    if args.num_parts < 1:
        parser.error("--num-parts must be at least 1")
    if not 0 <= args.num_shapes <= 2:
        parser.error("--num-shapes must be between 0 and 2")
    if not 1 <= args.num_colours <= len(colours):
        parser.error(f"--num-colours must be between 1 and {len(colours)}")
    if not 1 <= args.num_widths <= len(widths):
        parser.error(f"--num-widths must be between 1 and {len(widths)}")
    if not 1 <= args.num_orientations <= len(orientations):
        parser.error(
            f"--num-orientations must be between 1 and {len(orientations)}"
        )

    probabilities = (
        "cylindrical_goal_probability",
        "initial_colour_probability",
        "goal_colour_probability",
        "initial_hole_probability",
        "goal_hole_probability",
        "goal_surface_probability",
    )
    for option in probabilities:
        if not 0 <= getattr(args, option) <= 100:
            parser.error(
                f"--{option.replace('_', '-')} must be between 0 and 100"
            )

    print(
        make_problem(
            num_parts=args.num_parts,
            num_shapes=args.num_shapes,
            num_colours=args.num_colours,
            num_widths=args.num_widths,
            num_orientations=args.num_orientations,
            cylindrical_goal_probability=args.cylindrical_goal_probability,
            initial_colour_probability=args.initial_colour_probability,
            goal_colour_probability=args.goal_colour_probability,
            initial_hole_probability=args.initial_hole_probability,
            goal_hole_probability=args.goal_hole_probability,
            goal_surface_probability=args.goal_surface_probability,
            seed=args.seed,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
