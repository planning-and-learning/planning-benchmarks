#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time
from collections import deque
from typing import TypedDict


class Rover(TypedDict):
    location: int
    soil: bool
    rock: bool
    image: bool
    traversals: list[tuple[int, int]]
    reachable: set[int]
    cameras: list[int]


class Camera(TypedDict):
    target: int
    onboard: int
    modes: list[str]


class Objective(TypedDict):
    visible_from: set[int]
    requests: set[tuple[int, str]]


class Waypoint(TypedDict):
    soil: bool
    rock: bool
    sunny: bool


def make_problem(
    num_rovers: int,
    num_waypoints: int,
    num_objectives: int,
    num_cameras: int,
    num_goals: int,
    seed: int | None = None,
    learning_graphs: bool = True,
    learning_goals: bool = True,
) -> str:
    """rovgen-style task; the two options (default on) follow the IPC 2023 learning track.

    ``learning_graphs``: the visibility graph gets a random number of edges uniform between a
    spanning tree and the complete graph, and every rover may also traverse each visible edge
    between waypoints it reaches with probability 0.3. ``learning_goals``: each goal type's count
    is uniform in 0..available (so a type can be missing), with at least one goal overall;
    ``num_goals`` is then ignored.
    """
    seed = seed if seed is not None else int(time.time())
    rng = random.Random(seed)

    def random_flags() -> tuple[bool, bool, bool]:
        value = rng.randrange(7)
        flags: list[bool] = []
        for _ in range(3):
            flags.append(value % 2 == 0)
            value //= 2
        return flags[0], flags[1], flags[2]

    paths: list[set[int]] = [set() for _ in range(num_waypoints)]
    for _ in range(num_waypoints):
        for _ in range(5):
            source = rng.randrange(num_waypoints)
            target = rng.randrange(num_waypoints)
            if source != target and source not in paths[target]:
                paths[source].add(target)

    reached: set[int] = set()
    start = rng.randrange(num_waypoints)
    pending = deque([start])
    while pending:
        waypoint = pending.popleft()
        if waypoint in reached:
            continue
        reached.add(waypoint)
        pending.extend(paths[waypoint] - reached)

    while len(reached) < num_waypoints:
        target = next(i for i in range(num_waypoints) if i not in reached)
        paths[start].add(target)
        start = target
        pending.append(start)
        while pending:
            waypoint = pending.popleft()
            if waypoint in reached:
                continue
            reached.add(waypoint)
            pending.extend(paths[waypoint] - reached)

    if learning_graphs:
        pairs = {frozenset((a, b)) for a in range(num_waypoints) for b in paths[a] if a != b}
        target_edges = rng.randint(num_waypoints - 1, num_waypoints * (num_waypoints - 1) // 2)
        missing = [
            (a, b) for a in range(num_waypoints) for b in range(a + 1, num_waypoints) if frozenset((a, b)) not in pairs
        ]
        for a, b in rng.sample(missing, max(0, min(len(missing), target_edges - len(pairs)))):
            paths[a].add(b)

    lander_waypoint = rng.randrange(num_waypoints)
    rovers: list[Rover] = []
    for _ in range(num_rovers):
        location = rng.randrange(num_waypoints)
        soil, rock, image = random_flags()
        traversals: list[tuple[int, int]] = []
        reachable = {location}
        pending = deque([location])
        radius = num_waypoints // 3 + rng.randrange(num_waypoints)

        while radius and pending:
            source = pending.popleft()
            for target in range(num_waypoints):
                if target not in paths[source] and source not in paths[target]:
                    continue
                if any(destination == target for _, destination in traversals):
                    continue
                include = rng.randrange(10) > 2
                if include or not traversals:
                    traversals.extend(((source, target), (target, source)))
                    pending.append(target)
                    reachable.add(target)
            radius -= 1

        if learning_graphs:
            have = {frozenset(t) for t in traversals}
            for a in sorted(reachable):
                for b in sorted(paths[a]):
                    if b in reachable and a != b and frozenset((a, b)) not in have and rng.random() < 0.3:
                        have.add(frozenset((a, b)))
                        traversals.extend(((a, b), (b, a)))

        rovers.append(
            {
                "location": location,
                "soil": soil,
                "rock": rock,
                "image": image,
                "traversals": traversals,
                "reachable": reachable,
                "cameras": [],
            }
        )

    for rover in rovers:
        locations = {
            waypoint
            for traversal in rover["traversals"]
            for waypoint in traversal
        }
        if locations and not any(
            waypoint != lander_waypoint
            and (
                lander_waypoint in paths[waypoint]
                or waypoint in paths[lander_waypoint]
            )
            for waypoint in locations
        ):
            waypoint = rng.choice(sorted(locations - {lander_waypoint}))
            paths[lander_waypoint].add(waypoint)

    cameras: list[Camera] = []

    def add_camera(onboard: int | None = None) -> None:
        target = rng.randrange(num_objectives)
        onboard = rng.randrange(num_rovers) if onboard is None else onboard
        colour, high_res, low_res = random_flags()
        modes = [
            mode
            for mode, supported in (
                ("colour", colour),
                ("high_res", high_res),
                ("low_res", low_res),
            )
            if supported
        ]
        cameras.append(
            {
                "target": target,
                "onboard": onboard,
                "modes": modes,
            }
        )
        rovers[onboard]["image"] = True

    for _ in range(num_cameras):
        add_camera()

    for rover_id, rover in enumerate(rovers):
        rover["cameras"] = [
            camera_id
            for camera_id, camera in enumerate(cameras)
            if camera["onboard"] == rover_id
        ]
        if rover["image"] and not rover["cameras"]:
            add_camera(rover_id)
            rover["cameras"].append(len(cameras) - 1)

    objectives: list[Objective] = []
    for _ in range(num_objectives):
        visible_from = {
            rng.randrange(num_waypoints)
            for _ in range(rng.randrange(1, num_waypoints + 1))
        }
        objectives.append({"visible_from": visible_from, "requests": set()})

    waypoints: list[Waypoint] = []
    for _ in range(num_waypoints):
        waypoints.append(
            {
                "soil": rng.randrange(num_waypoints) % 2 == 0,
                "rock": rng.randrange(num_waypoints) % 2 == 0,
                "sunny": rng.randrange(10) < 3,
            }
        )

    for rover in rovers:
        traversals = rover["traversals"]
        if traversals and not any(
            waypoints[source]["sunny"] for source, _ in traversals
        ):
            source = rng.choice(traversals)[0]
            waypoints[source]["sunny"] = True

    soil_goal_count = rng.randrange(1, num_goals + 1) + num_goals // 3
    rock_goal_count = rng.randrange(1, num_goals + 1) + num_goals // 3
    image_goal_count = rng.randrange(1, num_goals + 1) + num_goals // 3

    soil_sites: list[int] = []
    rock_sites: list[int] = []
    for rover in rovers:
        reachable = {
            waypoint
            for traversal in rover["traversals"]
            for waypoint in traversal
        }
        if rover["soil"]:
            soil_sites.extend(
                waypoint
                for waypoint in range(num_waypoints)
                if waypoint in reachable and waypoints[waypoint]["soil"]
            )
        if rover["rock"]:
            rock_sites.extend(
                waypoint
                for waypoint in range(num_waypoints)
                if waypoint in reachable and waypoints[waypoint]["rock"]
            )

    goals: list[str] = []

    def add_sample_goals(kind: str, sites: list[int], count: int) -> None:
        selected: set[int] = set()
        count = min(count, len(set(sites)))
        while len(selected) < count:
            waypoint = rng.choice(sites)
            if waypoint not in selected:
                selected.add(waypoint)
                goals.append(f"(communicated_{kind}_data waypoint{waypoint})")

    if learning_goals:
        soil_goal_count = rng.randint(0, len(set(soil_sites)))
        rock_goal_count = rng.randint(0, len(set(rock_sites)))
    if soil_sites:
        add_sample_goals("soil", soil_sites, soil_goal_count)
    if rock_sites:
        add_sample_goals("rock", rock_sites, rock_goal_count)

    for camera in cameras:
        objective = objectives[camera["target"]]
        reachable = rovers[camera["onboard"]]["reachable"]
        if objective["visible_from"].isdisjoint(reachable):
            objective["visible_from"].add(rng.choice(sorted(reachable)))

    suitable: list[tuple[int, int]] = []
    for rover_id, rover in enumerate(rovers):
        if not rover["cameras"]:
            continue
        for objective_id, objective in enumerate(objectives):
            for waypoint in sorted(objective["visible_from"]):
                for left, right in rover["traversals"]:
                    if waypoint in (left, right):
                        suitable.append((objective_id, rover_id))

    if learning_goals:
        image_goal_count = rng.randint(0, len(suitable))
        if not goals and not image_goal_count:
            if soil_sites or rock_sites:
                kind, sites = ("soil", soil_sites) if soil_sites else ("rock", rock_sites)
                add_sample_goals(kind, sites, 1)
            else:
                image_goal_count = 1
    for _ in range(min(image_goal_count, len(suitable))):
        objective_id, rover_id = rng.choice(suitable)
        camera_id = rng.choice(rovers[rover_id]["cameras"])
        mode = rng.choice(cameras[camera_id]["modes"])
        request = (objective_id, mode)
        if request not in objectives[objective_id]["requests"]:
            objectives[objective_id]["requests"].add(request)
            goals.append(
                f"(communicated_image_data objective{objective_id} {mode})"
            )

    rover_names = " ".join(f"rover{i}" for i in range(num_rovers))
    store_names = " ".join(f"rover{i}store" for i in range(num_rovers))
    waypoint_names = " ".join(
        f"waypoint{i}" for i in range(num_waypoints)
    )
    objective_names = " ".join(
        f"objective{i}" for i in range(num_objectives)
    )
    object_lines = [
        "general - lander",
        "colour high_res low_res - mode",
        f"{rover_names} - rover",
        f"{store_names} - store",
        f"{waypoint_names} - waypoint",
    ]
    if cameras:
        camera_names = " ".join(f"camera{i}" for i in range(len(cameras)))
        object_lines.append(f"{camera_names} - camera")
    object_lines.append(f"{objective_names} - objective")

    init_facts: list[str] = []
    written_edges: set[frozenset[int]] = set()
    for left, targets in enumerate(paths):
        for right in sorted(targets):
            edge = frozenset((left, right))
            if left == right or edge in written_edges:
                continue
            written_edges.add(edge)
            init_facts.append(f"(visible waypoint{left} waypoint{right})")
            init_facts.append(f"(visible waypoint{right} waypoint{left})")

    for waypoint, properties in enumerate(waypoints):
        if properties["soil"]:
            init_facts.append(f"(at_soil_sample waypoint{waypoint})")
        if properties["rock"]:
            init_facts.append(f"(at_rock_sample waypoint{waypoint})")

    # learning domain has no channel_free/available predicates
    init_facts.append(f"(at_lander general waypoint{lander_waypoint})")

    for rover_id, rover in enumerate(rovers):
        init_facts.extend(
            (
                f"(at rover{rover_id} waypoint{rover['location']})",
                f"(store_of rover{rover_id}store rover{rover_id})",
                f"(empty rover{rover_id}store)",
            )
        )
        if rover["soil"]:
            init_facts.append(f"(equipped_for_soil_analysis rover{rover_id})")
        if rover["rock"]:
            init_facts.append(f"(equipped_for_rock_analysis rover{rover_id})")
        if rover["image"]:
            init_facts.append(f"(equipped_for_imaging rover{rover_id})")
        init_facts.extend(
            f"(can_traverse rover{rover_id} waypoint{left} waypoint{right})"
            for left, right in rover["traversals"]
        )

    for camera_id, camera in enumerate(cameras):
        init_facts.append(
            f"(on_board camera{camera_id} rover{camera['onboard']})"
        )
        init_facts.append(
            f"(calibration_target camera{camera_id} "
            f"objective{camera['target']})"
        )
        init_facts.extend(
            f"(supports camera{camera_id} {mode})" for mode in camera["modes"]
        )

    for objective_id, objective in enumerate(objectives):
        init_facts.extend(
            f"(visible_from objective{objective_id} waypoint{waypoint})"
            for waypoint in sorted(objective["visible_from"])
        )

    objects = "\n".join(f"    {line}" for line in object_lines)
    init = "\n".join(f"    {fact}" for fact in init_facts)
    goal = "\n".join(f"      {fact}" for fact in goals)

    return f"""(define (problem roverprob{seed})
  (:domain rover)
  (:objects
{objects}
  )
  (:init
{init}
  )
  (:goal
    (and
{goal}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="generate a rovers pddl problem.")
    parser.add_argument("num_rovers", type=int, help="number of rovers")
    parser.add_argument("num_waypoints", type=int, help="number of waypoints")
    parser.add_argument("num_objectives", type=int, help="number of objectives")
    parser.add_argument("num_cameras", type=int, help="number of cameras")
    parser.add_argument("num_goals", type=int, help="goal-density parameter")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    parser.add_argument(
        "--sparse-graphs", dest="learning_graphs", action="store_false", help="original rovgen graph density"
    )
    parser.add_argument(
        "--rovgen-goals", dest="learning_goals", action="store_false", help="original rovgen goal counts"
    )
    args = parser.parse_args(argv)

    if args.num_rovers < 1:
        parser.error("num_rovers must be at least 1")
    if args.num_waypoints < 1:
        parser.error("num_waypoints must be at least 1")
    if args.num_objectives < 1:
        parser.error("num_objectives must be at least 1")
    if args.num_cameras < 0:
        parser.error("num_cameras must be non-negative")
    if args.num_goals < 1:
        parser.error("num_goals must be at least 1")

    print(
        make_problem(
            args.num_rovers,
            args.num_waypoints,
            args.num_objectives,
            args.num_cameras,
            args.num_goals,
            args.seed,
            args.learning_graphs,
            args.learning_goals,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
