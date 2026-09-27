#!/usr/bin/env python3
# Reconstructed from the IPC 2026 rainbowttles tasks (data/numeric/ipc2026/rainbowttles-{opt,sat});
# their generator (generate_rainbowttles_NO_constants.py) was not published. Domain by Alba Gragera.

from __future__ import annotations

import argparse
import random
import sys
from collections.abc import Iterator
from dataclasses import dataclass

COLOURS = ("red", "green", "blue", "yellow", "purple", "orange", "cyan", "magenta", "lime", "teal")


@dataclass
class Block:
    """``segments`` contiguous segments of one colour inside a bottle."""

    colour: str
    segments: int


Bottle = list[Block]  # bottom first


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _wrap(names: list[str], type_name: str) -> list[str]:
    return [f"    {' '.join(names[i:i + 8])} - {type_name}" for i in range(0, len(names), 8)]


def _reverse_moves(bottles: list[Bottle], capacity: int) -> Iterator[tuple[int, int, int]]:
    """Legal reversed pours: take k segments of b1's top block onto bottle b.

    A forward pour moves a whole top block, so the reverse either splits a top
    block (k < size, forward: merge onto the same colour) or moves the only block
    of a bottle entirely (forward: pour into an empty bottle).
    """
    for i, source in enumerate(bottles):
        if not source:
            continue
        colour, size = source[-1].colour, source[-1].segments
        for k in range(1, size + 1):
            if k == size and len(source) > 1:
                continue
            for j, target in enumerate(bottles):
                if j == i or any(block.colour == colour for block in target):
                    continue
                if sum(block.segments for block in target) + k <= capacity:
                    yield i, j, k


def make_problem(
    num_colours: int,
    num_spare: int = 2,
    bottles_per_colour: int = 1,
    capacity: int = 4,
    scramble_steps: int = 10,
    seed: int | None = None,
    name: str = "rainbowttles-constant-free",
) -> str:
    """Generate a solvable Rainbowttles task by scrambling a solved state.

    The solved state has ``bottles_per_colour`` full bottles per colour plus
    ``num_spare`` empty bottles; ``scramble_steps`` random reversed pours keep
    each colour at most one contiguous block per bottle, so replaying them
    forwards (then closing every bottle) solves the task.
    """
    for label, value, minimum, maximum in (
        ("num_colours", num_colours, 1, len(COLOURS)),
        ("num_spare", num_spare, 1, 99),
        ("bottles_per_colour", bottles_per_colour, 1, 99),
        ("capacity", capacity, 1, 99),
        ("scramble_steps", scramble_steps, 0, 10**6),
    ):
        if not _is_int(value) or not minimum <= value <= maximum:
            raise ValueError(f"{label} must be an integer in [{minimum}, {maximum}]")

    rng = random.Random(seed)
    colours = list(COLOURS[:num_colours])
    bottles: list[Bottle] = [[Block(c, capacity)] for c in colours for _ in range(bottles_per_colour)]
    bottles += [[] for _ in range(num_spare)]
    rng.shuffle(bottles)
    for _ in range(scramble_steps):
        moves = list(_reverse_moves(bottles, capacity))
        if not moves:
            break
        i, j, k = rng.choice(moves)
        colour = bottles[i][-1].colour
        bottles[i][-1].segments -= k
        if bottles[i][-1].segments == 0:
            bottles[i].pop()
        bottles[j].append(Block(colour, k))

    names = [f"bottle{i:02d}" for i in range(1, len(bottles) + 1)]
    init = [f"  (real-colour {c})" for c in colours] + ["  (empty-colour empty)", ""]
    init += [f"  (= (bottle-capacity {b}) {capacity})" for b in names] + [""]
    for b, stack in zip(names, bottles):
        amounts = {block.colour: block.segments for block in stack}
        init += [f"  (= (colour-segments {b} {c}) {amounts.get(c, 0)})" for c in colours]
        init += [f"  (= (colour-segments {b} empty) 0)", f"  (= (segments-filled {b}) {sum(amounts.values())})"]
        chain = [block.colour for block in reversed(stack)] + ["empty"]
        init.append(f"  (upper-colour {b} {chain[0]})")
        init += [f"  (colour-below {b} {a} {below})" for a, below in zip(chain, chain[1:])]
        init.append("")
    nl = "\n"
    return (f"""(define (problem {name})
 (:domain rainbowttles-constant-free)
 (:objects
{nl.join(_wrap(names, "bottle") + _wrap(colours + ["empty"], "colour"))}
 )
 (:init
{nl.join(init)}
 )

 (:goal (and
{nl.join(f"  (closed {b})" for b in names)}
 ))

)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Rainbowttles PDDL problem.")
    parser.add_argument("-c", "--num-colours", type=int, required=True)
    parser.add_argument("-e", "--num-spare", type=int, default=2, help="empty bottles in the solved state (default: 2)")
    parser.add_argument("-b", "--bottles-per-colour", type=int, default=1)
    parser.add_argument("--capacity", type=int, default=4)
    parser.add_argument("-k", "--scramble-steps", type=int, default=10)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--name", default="rainbowttles-constant-free")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
