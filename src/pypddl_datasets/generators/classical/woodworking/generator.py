#!/usr/bin/env python

from __future__ import annotations

import argparse
import random
import sys
import time
from io import StringIO
from math import ceil

_colours = ["black", "white", "red", "green", "blue", "mauve"]
_woods = ["oak", "pine", "cherry", "teak", "mahogany", "beech", "walnut"]
_machines = [
    "highspeed-saw",
    "glazer",
    "grinder",
    "immersion-varnisher",
    "planer",
    "saw",
    "spray-varnisher",
]
_boardsize_prefix = "s"


def default_machines(num_machines):
    return {machine: num_machines for machine in _machines}


class Part:
    def __init__(self, index, woods, colours, rng, problemtype=None):
        self.name = "p%d" % index
        self.rng = rng
        self.problemtype = problemtype
        self.generate_random_goal(woods, colours)
        self.generate_random_init(woods, colours)

    def generate_random_goal(self, woods, colours):
        self.goalprops = dict()
        self.goalprops["treatment"] = self.rng.choice(["varnished", "glazed"])
        self.goalprops["surface-condition"] = self.rng.choice(["smooth", "verysmooth"])

        if self.problemtype != "painting":
            colours = colours + ["natural"]

        self.goalprops["colour"] = self.rng.choice(colours)
        self.goalprops["wood"] = self.rng.choice(woods)
        self.generate_goal_selection()

    def generate_goal_selection(self, nr_goals=None):
        if nr_goals is None:
            nr_goals = self.rng.choice([2, 2, 2, 3, 4])
        self.goalselection = set(self.rng.sample(list(self.goalprops), nr_goals))

    def generate_random_init(self, woods, colours):
        def gen_preprocessing_status():
            self.initprops["treatment"] = self.rng.choice(
                ["varnished", "glazed", "colourfragments"]
            )
            self.initprops["surface-condition"] = self.rng.choice(
                ["rough", "smooth", "verysmooth"]
            )
            self.initprops["wood"] = self.goalprops["wood"]

            poss_colours = set(colours + ["natural"]) - {self.goalprops["colour"]}
            self.initprops["colour"] = self.rng.choice(sorted(poss_colours))

        self.initprops = dict()

        status = self.rng.choice(["unused"] * 4 + ["available"])
        if status != "unused":
            while True:
                gen_preprocessing_status()
                goal_initially_satisfied = True
                for prop in self.goalselection:
                    if self.initprops[prop] != self.goalprops[prop]:
                        goal_initially_satisfied = False
                        break

                if not goal_initially_satisfied:
                    break

                self.generate_goal_selection(len(self.goalselection))

        self.size = self.rng.randint(1, 3)

    def dump_init(self, indent="", out=None):
        if self.initprops:
            print(f"{indent}(available {self.name})", file=out)

            for prop, val in self.initprops.items():
                print(f"{indent}({prop} {self.name} {val})", file=out)
        else:
            print(f"{indent}(unused {self.name})", file=out)

        print(
            "%s(goalsize %s %s)"
            % (indent, self.name, ["small", "medium", "large"][self.size - 1]),
            file=out,
        )
        print(
            f"{indent}(= (spray-varnish-cost {self.name}) {self.size * 5})",
            file=out,
        )
        print(
            "%s(= (glaze-cost %s) %d)" % (indent, self.name, self.size * 5 + 5),
            file=out,
        )
        print(
            "%s(= (grind-cost %s) %d)" % (indent, self.name, self.size * 15), file=out
        )
        print(
            "%s(= (plane-cost %s) %d)" % (indent, self.name, self.size * 10), file=out
        )

    def dump_goal(self, indent="", out=None):
        print(f"{indent}(available {self.name})", file=out)

        for choice in sorted(self.goalselection):
            print(
                f"{indent}({choice} {self.name} {self.goalprops[choice]})",
                file=out,
            )


class Board:
    def __init__(self, index, wood, size, rng):
        self.wood = wood
        self.name = "b%d" % index
        self.size = size
        self.surface = rng.choice(["rough", "rough", "rough", "smooth"])

    def dump_init(self, indent="", out=None):
        print(
            "%s(boardsize %s %s%d)" % (indent, self.name, _boardsize_prefix, self.size),
            file=out,
        )
        print(f"{indent}(wood {self.name} {self.wood})", file=out)
        print(
            f"{indent}(surface-condition {self.name} {self.surface})", file=out
        )
        print(f"{indent}(available {self.name})", file=out)


class Machine:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.colours = set()

    def dump_init(self, indent, out=None):
        if self.type == "highspeed-saw":
            print(f"{indent}(empty {self.name})", file=out)

        for colour in sorted(self.colours):
            print(f"{indent}(has-colour {self.name} {colour})", file=out)


class Task:
    def __init__(
        self,
        nr_parts,
        nr_machines,
        rng,
        wood_factor=1.0,
        problemtype=None,
        **additional_machines
    ):
        self.problemtype = problemtype
        self.wood_factor = wood_factor
        self.rng = rng

        nr_colours = max(int(round(0.7 * nr_parts)), 2)
        self.colours = self.rng.sample(_colours, min(nr_colours, len(_colours)))

        nr_woods = max(int(round(0.25 * nr_parts)), 2)
        self.woods = self.rng.sample(_woods, min(nr_woods, len(_woods)))

        self.parts = [
            Part(nr, self.woods, self.colours, self.rng, problemtype)
            for nr in range(nr_parts)
        ]

        self.max_board_size = self._generate_boards()

        self._generate_machines(nr_machines, **additional_machines)
        self._assign_colours_to_machines()

    def _generate_boards(self):
        quantities = dict()

        for part in [p for p in self.parts if not p.initprops]:
            wood = part.goalprops["wood"]
            quantities.setdefault(wood, []).append(part.size)

        self.boards = []
        counter = 0
        maxsize = 0
        for wood, quantity in quantities.items():
            if not quantity:
                self.woods.remove("wood")
            else:
                additional_wood = int(ceil(sum(quantity) * (self.wood_factor - 1)))

                while additional_wood > 3:
                    rand = self.rng.randint(1, 3)
                    quantity.append(rand)
                    additional_wood -= rand

                quantity.append(additional_wood)
                self.rng.shuffle(quantity)
                for amounts in zip(
                    quantity[::4],
                    quantity[1::4] + [0],
                    quantity[2::4] + [0],
                    quantity[3::4] + [0],
                ):
                    size = sum(amounts)
                    maxsize = max(maxsize, size)
                    self.boards.append(Board(counter, wood, size, self.rng))
                    counter += 1

        return maxsize

    def _generate_machines(self, nr_machines, **changes):
        machines = dict(default_machines(nr_machines))
        machines.update(changes)

        self.machines = dict()
        for type, number in machines.items():
            if number:
                m = [Machine(f"{type}{nr}", type) for nr in range(number)]
                self.machines[type] = m

    def _assign_colours_to_machines(self):
        necessary = self._determine_necessary_colours()

        spray_varnishers = self.machines.get("spray-varnisher", [])
        immersion_varnishers = self.machines.get("immersion-varnisher", [])
        glazers = self.machines.get("glazer", [])

        for colour in sorted(necessary["varnished"]):
            machines = self.rng.sample(
                spray_varnishers, int(ceil(0.6 * len(spray_varnishers)))
            )
            machines += self.rng.sample(
                immersion_varnishers, int(ceil(0.6 * len(immersion_varnishers)))
            )

            for m in machines:
                m.colours.add(colour)

        for colour in sorted(necessary["glazed"]):
            for m in self.rng.sample(glazers, int(ceil(0.6 * len(glazers)))):
                m.colours.add(colour)

        for colour in sorted(necessary["unspecified"]):
            machines = self.rng.sample(
                spray_varnishers, int(ceil(0.3 * len(spray_varnishers)))
            )
            machines += self.rng.sample(
                immersion_varnishers, int(ceil(0.3 * len(immersion_varnishers)))
            )
            machines += self.rng.sample(glazers, int(ceil(0.3 * len(glazers))))

            for m in machines:
                m.colours.add(colour)

        for type in ["spray-varnisher", "immersion-varnisher", "glazer"]:
            for m in self.machines.get(type, []):
                if not m.colours:
                    m.colours.add(self.rng.choice(self.colours))

    def _determine_necessary_colours(self):
        used_colours = dict()
        used_colours["varnished"] = set()
        used_colours["glazed"] = set()
        used_colours["unspecified"] = set()

        for part in self.parts:
            if "colour" in part.goalselection:
                colour = part.goalprops["colour"]

                if "treatment" in part.goalselection:
                    used_colours[part.goalprops["treatment"]].add(colour)
                else:
                    used_colours["unspecified"].add(colour)

        return used_colours

    def dump(self, out=None):
        self._dump_header(out)
        self._dump_objects("  ", out)
        self._dump_init("  ", out)
        self._dump_goal("  ", out)
        self._dump_metric("  ", out)

        print(")", file=out)

    def _dump_header(self, out=None):
        print(
            "; woodworking task with %s parts and %d%% wood"
            % (len(self.parts), self.wood_factor * 100),
            file=out,
        )
        print("; machines:", file=out)

        for type, machines in self.machines.items():
            print(";   %d %s" % (len(machines), type), file=out)

        print("", file=out)
        print("(define (problem wood-prob)", file=out)
        print("  (:domain woodworking)", file=out)

    def _dump_objects(self, indent="", out=None):
        print(indent + "(:objects", file=out)

        for type, machines in self.machines.items():
            print(
                "{}  {} - {}".format(indent, " ".join([m.name for m in machines]), type),
                file=out,
            )

        print("{}  {} - acolour".format(indent, " ".join(self.colours)), file=out)
        print("{}  {} - awood".format(indent, " ".join(self.woods)), file=out)
        print(
            "{}  {} - part".format(indent, " ".join([p.name for p in self.parts])), file=out
        )
        if self.boards:
            print(
                "{}  {} - board".format(
                    indent, " ".join([b.name for b in self.boards])
                ),
                file=out,
            )

        boardsizes = [
            "%s%d" % (_boardsize_prefix, size)
            for size in range(self.max_board_size + 1)
        ]

        print("{}  {} - aboardsize".format(indent, " ".join(boardsizes)), file=out)
        print(indent + ")", file=out)

    def _dump_init(self, indent="", out=None):
        print(indent + "(:init", file=out)
        print(indent + "  (grind-treatment-change varnished colourfragments)", file=out)
        print(indent + "  (grind-treatment-change glazed untreated)", file=out)
        print(indent + "  (grind-treatment-change untreated untreated)", file=out)
        print(indent + "  (grind-treatment-change colourfragments untreated)", file=out)
        print(indent + "  (is-smooth smooth)", file=out)
        print(indent + "  (is-smooth verysmooth)", file=out)
        print(indent + "  (= (total-cost) 0)", file=out)

        for size in range(self.max_board_size):
            print(
                "%s  (boardsize-successor %s%d %s%d)"
                % (indent, _boardsize_prefix, size, _boardsize_prefix, size + 1),
                file=out,
            )

        for type in self.machines:
            for m in self.machines[type]:
                m.dump_init(indent + "  ", out)

        for part in self.parts:
            part.dump_init(indent + "  ", out)

        for board in self.boards:
            board.dump_init(indent + "  ", out)

        print(indent + ")", file=out)

    def _dump_goal(self, indent="", out=None):
        print(indent + "(:goal", file=out)
        print(indent + "  (and", file=out)

        for part in self.parts:
            part.dump_goal(indent + "  ", out)

        print(indent + "  )", file=out)
        print(indent + ")", file=out)

    def _dump_metric(self, indent="", out=None):
        print(indent + "(:metric minimize (total-cost))", file=out)


def make_problem(
    num_parts: int,
    num_machines: int,
    wood_factor: float = 1.0,
    seed: int | None = None,
) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))
    instance = Task(num_parts, num_machines, rng, wood_factor)
    output = StringIO()
    instance.dump(out=output)
    return output.getvalue()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="generate a woodworking pddl problem."
    )
    parser.add_argument("wood_factor", type=float, help="available wood factor")
    parser.add_argument("num_parts", type=int, help="number of parts")
    parser.add_argument("num_machines", type=int, help="machines of each type")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    args = parser.parse_args(argv)

    if args.wood_factor < 1.0:
        parser.error("wood_factor must be at least 1")
    if args.num_parts < 1:
        parser.error("num_parts must be at least 1")
    if args.num_machines < 1:
        parser.error("num_machines must be at least 1")

    print(
        make_problem(
            args.num_parts,
            args.num_machines,
            args.wood_factor,
            args.seed,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())