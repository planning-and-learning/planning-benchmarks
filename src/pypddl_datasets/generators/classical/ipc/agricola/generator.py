#!/usr/bin/env python3
# Port of pddl-generators agricola/GenAgricola.py (Tomas de la Rosa, IPC 2018):
# `GenAgricola.py <last_stage> <seed> --num_workers <w> [--must_create_workers]`.
# Like the IPC tasks (and unlike upstream), the init sets (= (total-cost) 0).

from __future__ import annotations

import argparse
import random
import sys

NORMAL_ROUNDS = [1, 2, 3, 5, 6, 8, 10, 12]
HARVEST_ROUNDS = [r for r in range(1, 21) if r not in NORMAL_ROUNDS]
MAX_STAGE = len(HARVEST_ROUNDS)  # 12: round 21 is the last one upstream can name
OPEN_CARDS = [
    "act_labor", "act_wood", "act_clay", "act_reed", "act_build", "act_plow", "act_grain", "act_stone",
]
ROUND_CARDS = [
    "act_fences", "act_sheep", "act_sow", "act_family", "act_improve", "act_carrot", "act_boar", "act_cattle",
]


def make_problem(
    last_stage: int,
    num_workers: int = 5,
    must_create_workers: bool = False,
    seed: int | None = None,
    num_ints: int = 16,
) -> str:
    """Generate an Agricola task that must reach the harvest end of ``last_stage``.

    Stage ``s`` ends with the harvest in round ``h_s`` (4, 7, 9, 11, 13, 14, ...),
    so there are ``h_last + 1`` rounds and ``last_stage + 1`` stages. The only
    random choices are the order of the four stage-1 round cards (rounds 1-4,
    the first one open from the start), the order of the four stage-2 cards
    (rounds 5-8) and the initial food in 0..3. With ``must_create_workers`` the
    goal also demands growing the family to ``num_workers`` workers.
    """
    checks: list[tuple[str, object, int]] = [
        ("last_stage", last_stage, 1), ("num_workers", num_workers, 2), ("num_ints", num_ints, 1)
    ]
    for name, value, minimum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if last_stage > MAX_STAGE:
        raise ValueError(f"last_stage must be at most {MAX_STAGE}")

    rng = random.Random(seed)
    num_ints = max(num_ints, 2 + 2 * num_workers)
    num_rounds = HARVEST_ROUNDS[last_stage - 1] + 1

    def names(prefix: str, count: int) -> str:
        return " ".join(f"{prefix}{i}" for i in range(1, count + 1))

    init = [f"(next_num num{i} num{i + 1})" for i in range(num_ints)]
    init += [f"(num_substract num{i} num{j} num{i - j})" for i in range(1, num_ints + 1) for j in range(1, i + 1)]
    init += [f"(next2_num num{i} num{i + 2})" for i in range(num_ints - 1)]
    init += [f"(next_stage stage{i} stage{i + 1})" for i in range(1, last_stage + 1)]
    init += [f"(next_round round{i} round{i + 1})" for i in range(1, num_rounds)]
    init += [f"(next_worker worker{i} worker{i - 1})" for i in range(num_workers, 1, -1)]
    init.append("(next_worker worker1 noworker)")
    init += [
        f"(category_round round{j} {'tnormal' if j in NORMAL_ROUNDS else 'tharvest'})" for j in range(1, num_rounds + 1)
    ]
    init += [f"(open_action {card})" for card in OPEN_CARDS]
    stage1, stage2 = ROUND_CARDS[:4], ROUND_CARDS[4:]
    rng.shuffle(stage1)
    init.append(f"(open_action {stage1[0]})")
    init += [f"(drawcard_round {stage1[k]} round{k + 1})" for k in range(min(4, num_rounds))]
    rng.shuffle(stage2)
    init += [f"(drawcard_round {stage2[k]} round{k + 5})" for k in range(min(4, num_rounds - 4))]
    init += [f"(drawcard_round void round{k})" for k in range(9, num_rounds + 1)]
    init += [f"(available_action {card})" for card in OPEN_CARDS + ROUND_CARDS]
    for k in range(2, num_workers + 1):
        init += [f"(food_required worker{k} num{2 * k})", f"(food_required worker{k} num{2 * k + 1})"]
    init += [
        "(current_worker worker2)",
        "(max_worker worker2)",
        "(current_round round1)",
        "(current_stage stage1)",
        "(harvest_phase stage1 harvest_init)",
        f"(num_food num{rng.randint(0, 3)})",
    ]
    init += [f"(supply_resource act_{resource} {resource})" for resource in ("wood", "clay", "reed", "stone")]
    init += ["(built_rooms room1 worker1)", "(built_rooms room2 worker2)"]
    init += [f"(space_rooms room{k})" for k in range(3, num_workers + 1)]
    costs = [4, 6, 15, 30, 60]
    while len(costs) < num_workers - 1:
        costs.append(costs[-1] + 30)
    init += [f"(= (group_worker_cost worker{w}) {c})" for w, c in zip(range(2, num_workers + 1), costs[::-1])]
    init.append("(= (total-cost) 0)")

    goal = [f"(harvest_phase stage{last_stage} harvest_end)"]
    if must_create_workers:
        goal.append(f"(max_worker worker{num_workers})")

    nl = "\n    "
    return (f"""(define (problem agricola-{'allworkers-' if must_create_workers else ''}{last_stage}-{num_workers})
(:domain agricola)
(:objects
    {names("num", num_ints)} - num
    {names("stage", last_stage + 1)} - stage
    {names("round", num_rounds)} - round
    {names("worker", num_workers)} - worker
    {names("room", num_workers)} - room
)
(:init
    {nl.join(init)}
)
(:goal
(and
    {nl.join(goal)}
)
)
(:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an Agricola (IPC 2018) PDDL problem.")
    parser.add_argument("last_stage", type=int, help=f"stage whose harvest must end, 1..{MAX_STAGE}")
    parser.add_argument("-w", "--num-workers", type=int, default=5)
    parser.add_argument("--must-create-workers", action="store_true", help="goal also requires num_workers workers")
    parser.add_argument("--num-ints", type=int, default=16, help="minimum number of integer objects (default: 16)")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.last_stage, args.num_workers, args.must_create_workers, args.seed, args.num_ints)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
