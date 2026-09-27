#!/usr/bin/env python3
# Flashfill (IPC 2018, Javier Segovia-Aguas): Excel flash fill as planning programs. Upstream's
# pipeline (Autoscale's pddl-generators/flashfill) draws random string examples with
# domains/excel_variables/gen0{1,2,4,5}.py and compiles them with the C++ planning-programs
# compiler (`bin/compile PLPR ...`) into one domain and problem per task. The compiled domain
# only depends on the examples through its constants, one `(test-k)` predicate per example and
# the `repeat-end*-k-*` actions that check example k's output and load example k+1; everything
# else is fixed per task family. This generator therefore ports the example generators and
# fills a per-family skeleton taken from the IPC tasks (skeleton-*.pddl.gz: an IPC domain with
# those parts cut out).
# ponytail: program-line counts are fixed per family (the IPC ones); other line counts need a
# port of the planning-programs compiler (src/compile.cpp).

from __future__ import annotations

import argparse
import gzip
import random
import string
import sys
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).parent
FAMILIES = {  # family -> (skeleton, program lines)
    "add-paren": ("one-input-7-lines", 7),
    "extract-minutes": ("one-input-7-lines", 7),
    "first-last-initial": ("two-inputs-8-lines", 8),
    "initials": ("two-inputs-6-lines", 6),
}
LIMITERS = ("space", "hyph", "colon", "dot", "lpar", "rpar")
EXTRACT_MINUTES_SIZE = 6  # the IPC extract-minutes examples: 7 characters, hiindex i6


@dataclass
class _Example:
    init: list[str] = field(default_factory=list[str])
    goal: list[str] = field(default_factory=list[str])


def _letters(rng: random.Random, n: int) -> list[str]:
    return [rng.choice(string.ascii_lowercase) for _ in range(n)]


def _single_input(size: int) -> list[str]:
    return [f"(hiindex str i{size})", "(loindex str i0)", f"(size str i{size})", "(size res i0)",
            "(input-assignment str-var str row-0)", *(f"(next i{i} i{i + 1})" for i in range(size + 1))]


def _two_inputs(name_size: int, surname_size: int) -> list[str]:
    return [f"(hiindex str i{name_size})", "(loindex str i0)", f"(hiindex str2 i{surname_size})",
            "(loindex str2 i0)", f"(size str i{name_size})", f"(size str2 i{surname_size})", "(size res i0)",
            "(input-assignment str-var str row-0)", "(input-assignment str2-var str2 row-0)",
            *(f"(next i{i} i{i + 1})" for i in range(name_size + surname_size + 1))]


def _example(family: str, rng: random.Random, size: int) -> _Example:
    """One input/output example, as gen01/gen02/gen04/gen05.py draw it."""
    if family == "add-paren":  # gen01: "(" + size-1 letters -> "(" + letters + ")"
        letters = _letters(rng, size - 1)
        chars = ["lpar", *letters]
        init = [*_single_input(size), *(f"(assignment str i{i} {c})" for i, c in enumerate(chars))]
        goal = [*(f"(assignment res i{i} {c})" for i, c in enumerate(chars)), f"(assignment res i{size} rpar)"]
    elif family == "extract-minutes":  # gen02: "h:mm.ss" -> "mm" (keeps upstream's extra lpar at i0)
        hour, minutes, seconds = rng.randint(0, 9), rng.randint(0, 59), rng.randint(0, 59)
        digits = [
            f"n{hour}", "colon", f"n{minutes // 10}", f"n{minutes % 10}", "dot", f"n{seconds // 10}", f"n{seconds % 10}"
        ]
        init = [
            *_single_input(size),
            "(assignment str i0 lpar)",
            *(f"(assignment str i{i} {c})" for i, c in enumerate(digits)),
        ]
        goal = [f"(assignment res i0 n{minutes // 10})", f"(assignment res i1 n{minutes % 10})"]
    else:  # gen04 "Name Surname" -> "Name S", gen05 -> "N S"
        name, surname = _letters(rng, size), _letters(rng, size)
        init = [*_two_inputs(size, size), *(f"(assignment str i{i} {c})" for i, c in enumerate(name)),
                *(f"(assignment str2 i{i} {c})" for i, c in enumerate(surname))]
        kept = name if family == "first-last-initial" else name[:1]
        goal = [*(f"(assignment res i{i} {c})" for i, c in enumerate(kept)), f"(assignment res i{len(kept)} space)",
                f"(assignment res i{len(kept) + 1} {surname[0]})", f"(size res i{len(kept) + 2})"]
    return _Example(init, goal)


_RESETS = """        (forall (?string1 - string ?index2 - index ?char3 - char)
            (when
                (and
                    (assignment ?string1 ?index2 ?char3)
                )
                (not (assignment ?string1 ?index2 ?char3))
            )
        )
        (forall (?input1 - input ?index2 - index)
            (when
                (and
                    (loindex ?input1 ?index2)
                )
                (not (loindex ?input1 ?index2))
            )
        )
        (forall (?input1 - input ?index2 - index)
            (when
                (and
                    (hiindex ?input1 ?index2)
                )
                (not (hiindex ?input1 ?index2))
            )
        )
        (forall (?string1 - string ?index2 - index)
            (when
                (and
                    (size ?string1 ?index2)
                )
                (not (size ?string1 ?index2))
            )
        )
        (forall (?input-variable1 - input-variable)
            (when
                (and
                    (empty ?input-variable1)
                )
                (not (empty ?input-variable1))
            )
        )
        (forall (?index1 - index ?index2 - index)
            (when
                (and
                    (next ?index1 ?index2)
                )
                (not (next ?index1 ?index2))
            )
        )
        (forall (?input-variable1 - input-variable ?input2 - input ?stackrow3 - stackrow)
            (when
                (and
                    (input-assignment ?input-variable1 ?input2 ?stackrow3)
                )
                (not (input-assignment ?input-variable1 ?input2 ?stackrow3))
            )
        )"""


def _test_actions(examples: list[_Example], lines: int) -> str:
    def indent(facts: list[str]) -> str:
        return "".join(f"        {f}\n" for f in facts)

    actions: list[str] = []
    for k, example in enumerate(examples):
        for line in range(1, lines):
            if k + 1 < len(examples):
                effect = (f"        (not (test-{k}))\n        (test-{k + 1})\n"
                          f"        (not (stack-line-{line} ?stackrow0))\n"
                          f"        (stack-line-0 ?stackrow0)\n{indent(examples[k + 1].init)}{_RESETS}\n")
            else:
                effect = "        (done-programming)\n"
            actions.append(f"""(:action repeat-end-main-{k}-{line}
    :parameters (?stackrow0 - stackrow)
    :precondition
    (and
        (top-stack ?stackrow0)
        (top-stack row-0)
        (stack-main row-0)
        (stack-line-{line} row-0)
        (ins-end-{line})
        (test-{k})
{indent(example.goal)}    )
    :effect
    (and
{effect}    )
)
""")
    for k in range(len(examples)):
        for line in range(1, lines):
            actions.append(f"""(:action repeat-end-0-{k}-{line}
    :parameters (?stackrow0 - stackrow ?stackrow1 - stackrow)
    :precondition
    (and
        (ins-end-{line})
        (test-{k})
        (next-stack-row ?stackrow0 ?stackrow1)
        (top-stack ?stackrow1)
        (stack-main ?stackrow1)
        (stack-line-{line} ?stackrow1)
    )
    :effect
    (and
        (not (top-stack ?stackrow1))
        (top-stack ?stackrow0)
        (not (stack-main ?stackrow1))
        (not (stack-line-{line} ?stackrow1))
        (forall (?input-variable2 - input-variable ?input3 - input)
            (and
                (not (input-assignment ?input-variable2 ?input3 ?stackrow1))
            )
        )
        (increase (total-cost) 1)
    )
)
""")
    return "\n".join(actions)


def _constants(examples: list[_Example], two_inputs: bool) -> str:
    symbols = {f.split()[-1].rstrip(")") for e in examples for f in [*e.init, *e.goal] if f.startswith("(assignment")}
    indices = {
        tok.rstrip(")") for e in examples for f in [*e.init, *e.goal] for tok in f.split()[1:]
        if tok.rstrip(")")[:1] == "i" and tok.rstrip(")")[1:].isdigit()
    }
    inputs, variables = ("str str2", "str-var str2-var") if two_inputs else ("str", "str-var")
    return "\n".join([
        f"    {' '.join(sorted(symbols - set(LIMITERS)))} - char",
        f"    {' '.join(sorted(symbols & set(LIMITERS)))} - limiter",
        f"    {inputs} - input",
        "    res - output",
        f"    {' '.join(sorted(indices))} - index",
        f"    {variables} - input-variable",
        "    row-0 row-1 - stackrow",
    ])


def _task(family: str, examples: list[_Example], name: str) -> tuple[str, str]:
    skeleton, lines = FAMILIES[family]
    domain = gzip.decompress((HERE / f"skeleton-{skeleton}.pddl.gz").read_bytes()).decode()
    domain = domain.replace("@@constants@@", _constants(examples, skeleton.startswith("two")))
    domain = domain.replace("@@test-predicates@@", "\n".join(f"    (test-{k})" for k in range(len(examples))))
    domain = domain.replace("@@test-actions@@", _test_actions(examples, lines))
    init = "\n".join(f"    {f}" for f in examples[0].init)
    empties = "\n".join(f"    (empty-{line})" for line in range(lines))
    problem = f"""(define (problem {name})
(:domain flashfill)
(:objects
)
(:init
    (= (total-cost) 0)
{init}
    (test-0)
    (next-stack-row row-0 row-1)
    (stack-main row-0)
    (stack-line-0 row-0)
    (top-stack row-0)
{empties}
)
(:goal
(and
    (done-programming)
)
)
(:metric minimize (total-cost))
)
"""
    return domain.lower(), problem.lower()


def make_task(
    family: str, num_tests: int, min_size: int = 3, max_size: int = 7, seed: int | None = None
) -> tuple[str, str]:
    """Generate a Flashfill task as (domain, problem).

    `num_tests` examples of the family's string transformation; each example's string
    length is uniform in [min_size, max_size] (extract-minutes always uses 7 characters).
    A plan is a program of the family's fixed number of lines that maps every example
    input to its output.
    """
    if family not in FAMILIES:
        raise ValueError(f"family must be one of {', '.join(FAMILIES)}")
    checks: list[tuple[str, object, int]] = [
        ("num_tests", num_tests, 1), ("min_size", min_size, 2), ("max_size", max_size, 2),
    ]
    for name, value, minimum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if max_size < min_size:
        raise ValueError("max_size must be at least min_size")
    rng = random.Random(seed)
    sizes = [
        EXTRACT_MINUTES_SIZE if family == "extract-minutes" else rng.randint(min_size, max_size)
        for _ in range(num_tests)
    ]
    examples = [_example(family, rng, size) for size in sizes]
    return _task(family, examples, f"{family}-{num_tests}-{max(sizes)}-{seed}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an IPC 2018 Flashfill domain and problem.")
    parser.add_argument("family", choices=FAMILIES)
    parser.add_argument("num_tests", type=int)
    parser.add_argument("--min-size", type=int, default=3)
    parser.add_argument("--max-size", type=int, default=7)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--domain", default="domain.pddl", help="domain output file (default: domain.pddl)")
    parser.add_argument("--problem", default="problem.pddl", help="problem output file (default: problem.pddl)")
    args = parser.parse_args(argv)
    try:
        domain, problem = make_task(args.family, args.num_tests, args.min_size, args.max_size, args.seed)
    except ValueError as error:
        parser.error(str(error))
    Path(args.domain).write_text(domain, encoding="utf-8")
    Path(args.problem).write_text(problem, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
