#!/usr/bin/env python3
# Reconstruction of the IPC 2026 numeric Coins (minimum coins) tasks (no generator was
# published): all reference tasks use the denominations 1, 2, 3, 5, 7 with penalty 1
# and differ only in the target value (29 up to 3000, growing by about 27% per task).

from __future__ import annotations

import argparse
import sys

DENOMINATIONS = (1, 2, 3, 5, 7)


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(target: int, denominations: tuple[int, ...] = DENOMINATIONS) -> str:
    """Generate a Coins task: reach ``target`` with the fewest coins.

    Deterministic, like the reference tasks. ``denominations`` must contain 1 so that
    every target is reachable.
    """
    if not _is_int(target) or target < 1:
        raise ValueError("target must be an integer at least 1")
    if (
        not denominations
        or any(not _is_int(d) or d < 1 for d in denominations)
        or len(set(denominations)) != len(denominations)
        or 1 not in denominations
    ):
        raise ValueError("denominations must be distinct positive integers including 1")
    coins = [f"c{i + 1}" for i in range(len(denominations))]
    init = [f"        (= (denomination {c}) {d})" for c, d in zip(coins, denominations)]
    init.append("")
    init += [f"        (= (denomination-penalty {c}) 1)" for c in coins]
    init.append("")
    init += [f"        (no-coin-update {c})" for c in coins]
    init += ["", "        (= (current-value) 0)", "        (= (coin-count) 0)", "        (= (penalty) 0)"]
    return (f"""(define (problem coins-{target})
    (:domain coins)

    (:objects
        {' '.join(coins)} - coin
    )

    (:init
{chr(10).join(init)}
    )

    (:goal
        (and
            (= (current-value) {target})
            (= (penalty) 0)
        )
    )

    (:metric minimize (coin-count))

)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Coins PDDL problem.")
    parser.add_argument("-t", "--target", type=int, required=True)
    parser.add_argument(
        "-d", "--denominations", type=int, nargs="+", default=list(DENOMINATIONS),
        help="coin denominations, must include 1 (default: 1 2 3 5 7)",
    )
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.target, tuple(args.denominations))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
