#!/usr/bin/env python3
# Port of ipc2023-classical/domain-recharging-robots/generator.py (Daniel Gnad and
# Alvaro Torralba, IPC 2023; public domain), scenarios `covers` and
# `single-source-move-to-locations` as used by the IPC tasks. scipy's Delaunay,
# shapely geometry, networkx and the CPLEX covering ILPs are replaced by pure Python.

from __future__ import annotations

import argparse
import itertools
import math
import random
import sys
from collections import deque
from typing import cast

KINDS = ("covers", "single-source-move-to-locations")
MIN_SQUARE_WIDTH = 0.08
MIN_VIEWPOINT_VIEWPOINT_DISTANCE = 0.1
MIN_VIEWPOINT_OBSTACLE_DISTANCE = 0.05
MIN_OBSTACLE_OBSTACLE_DISTANCE = 0.05
MAX_ATTEMPTS = 10000

Point = tuple[float, float]
# robot starts, battery charges, goal locations, guard areas
Setup = tuple[list[int], list[int], list[int], list[list[int]]]


class _Redraw(Exception):
    """Upstream exits (or loops) on this draw; the caller draws a new map."""


def _square_distance(a: tuple[Point, float], b: tuple[Point, float]) -> float:
    (ax, ay), aw = a
    (bx, by), bw = b
    dx = max(0.0, abs(ax - bx) - (aw + bw) / 2)
    dy = max(0.0, abs(ay - by) - (aw + bw) / 2)
    return math.hypot(dx, dy)


def _point_square_distance(p: Point, s: tuple[Point, float]) -> float:
    (sx, sy), w = s
    return math.hypot(max(0.0, abs(p[0] - sx) - w / 2), max(0.0, abs(p[1] - sy) - w / 2))


def _delaunay_edges(points: list[Point]) -> set[tuple[int, int]]:
    """Bowyer-Watson; returns the undirected edges of the triangulation."""
    n = len(points)
    pts = list(points) + [(-1e5, -1e5), (1e5, -1e5), (0.0, 1e5)]
    triangles = [(n, n + 1, n + 2)]

    def in_circle(t: tuple[int, int, int], p: Point) -> bool:
        (ax, ay), (bx, by), (cx, cy) = (pts[i] for i in t)
        ax, ay, bx, by, cx, cy = ax - p[0], ay - p[1], bx - p[0], by - p[1], cx - p[0], cy - p[1]
        det = (ax * ax + ay * ay) * (bx * cy - cx * by) - (bx * bx + by * by) * (ax * cy - cx * ay) \
            + (cx * cx + cy * cy) * (ax * by - bx * ay)
        orient = (pts[t[1]][0] - pts[t[0]][0]) * (pts[t[2]][1] - pts[t[0]][1]) \
            - (pts[t[1]][1] - pts[t[0]][1]) * (pts[t[2]][0] - pts[t[0]][0])
        return det * orient > 1e-12

    for i, p in enumerate(points):
        bad = [t for t in triangles if in_circle(t, p)]
        boundary: dict[tuple[int, int], int] = {}
        for t in bad:
            for e in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
                key = (min(e), max(e))
                boundary[key] = boundary.get(key, 0) + 1
        triangles = [t for t in triangles if t not in bad]
        triangles += [(a, b, i) for (a, b), count in boundary.items() if count == 1]
    edges: set[tuple[int, int]] = set()
    for t in triangles:
        for a, b in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
            if a < n and b < n:
                edges.add((min(a, b), max(a, b)))
    return edges


class _Map:
    def __init__(self, rng: random.Random, num_obstacles: int, num_viewpoints: int,
                 max_distance: float, max_square_width: float):
        obstacles: list[tuple[Point, float]] = []
        for _ in range(MAX_ATTEMPTS):
            if len(obstacles) == num_obstacles:
                break
            w = rng.uniform(MIN_SQUARE_WIDTH, max_square_width)
            o = ((rng.uniform(w / 2, 1 - w / 2), rng.uniform(w / 2, 1 - w / 2)), w)
            if all(_square_distance(o, other) >= MIN_OBSTACLE_OBSTACLE_DISTANCE for other in obstacles):
                obstacles.append(o)
        viewpoints: list[Point] = []
        for _ in range(MAX_ATTEMPTS):
            if len(viewpoints) == num_viewpoints:
                break
            v = (rng.uniform(0.01, 0.99), rng.uniform(0.01, 0.99))
            if all(math.dist(v, w) >= MIN_VIEWPOINT_VIEWPOINT_DISTANCE for w in viewpoints) and all(
                _point_square_distance(v, o) >= MIN_VIEWPOINT_OBSTACLE_DISTANCE for o in obstacles
            ):
                viewpoints.append(v)
        if len(obstacles) < num_obstacles or len(viewpoints) < num_viewpoints:
            raise ValueError("num_obstacles/num_viewpoints do not fit into the unit square")

        self.locations = list(viewpoints)
        diagonals: set[tuple[int, int]] = set()
        for (x, y), w in obstacles:
            base = len(self.locations)
            h = w / 2
            self.locations += [(x - h, y - h), (x + h, y - h), (x + h, y + h), (x - h, y + h)]
            diagonals |= {(base, base + 2), (base + 1, base + 3)}
        # Upstream drops edges longer than max_distance and edges inside an obstacle
        # (shapely `contains`); corners of different obstacles and viewpoints never
        # lie inside one, so only square diagonals are dropped.
        self.connections = sorted(
            e for e in _delaunay_edges(self.locations)
            if math.dist(self.locations[e[0]], self.locations[e[1]]) <= max_distance and e not in diagonals
        )
        n = len(self.locations)
        self.neighbours: list[set[int]] = [set() for _ in range(n)]
        for a, b in self.connections:
            self.neighbours[a].add(b)
            self.neighbours[b].add(a)
        self.dist = [self._bfs(s) for s in range(n)]

    def _bfs(self, source: int) -> list[int]:
        dist = [-1] * len(self.locations)
        dist[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in self.neighbours[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        return dist

    def connected(self) -> bool:
        return min(self.dist[0]) >= 0

    def closed(self, y: int) -> set[int]:
        return self.neighbours[y] | {y}

    def dominates_within(self, targets: list[int], budget: int) -> bool:
        """Is there a set of at most `budget` locations guarding every target?"""
        def search(undominated: frozenset[int], budget: int) -> bool:
            if not undominated:
                return True
            if budget == 0:
                return False
            y = min(undominated, key=lambda t: (len(self.closed(t)), t))
            return any(search(undominated - self.closed(c), budget - 1) for c in sorted(self.closed(y)))
        return search(frozenset(targets), budget)

    def min_cost_cover(self, area: list[int], robots: list[int]) -> tuple[int, list[int]]:
        """Upstream's CPLEX model: send robots to distinct locations guarding the
        area, minimising the summed hop distance; unassigned robots stay put."""
        best: tuple[float, list[int]] = (math.inf, list(robots))
        seen: set[frozenset[int]] = set()

        def assignment(chosen: tuple[int, ...]) -> tuple[float, list[int]]:
            # dp over robots, mask of covered chosen locations
            k = len(chosen)
            dp: dict[int, tuple[float, list[int]]] = {0: (0, [])}
            for r in robots:
                nxt: dict[int, tuple[float, list[int]]] = {}
                for mask, (cost, picks) in dp.items():
                    options = [(cost, picks + [-1], mask)]
                    options += [(cost + self.dist[r][chosen[j]], picks + [j], mask | 1 << j)
                                for j in range(k) if not mask >> j & 1]
                    for c, p, m in options:
                        if m not in nxt or c < nxt[m][0]:
                            nxt[m] = (c, p)
                dp = nxt
            cost, picks = dp.get((1 << k) - 1, (math.inf, []))
            return cost, [robots[i] if j < 0 else chosen[j] for i, j in enumerate(picks)]

        def search(chosen: frozenset[int], undominated: frozenset[int]) -> None:
            nonlocal best
            if chosen in seen:
                return
            seen.add(chosen)
            cost, targets = assignment(tuple(sorted(chosen)))
            if cost >= best[0]:  # adding locations never lowers the cost
                return
            if not undominated:
                best = (cost, targets)
                return
            if len(chosen) == len(robots):
                return
            y = min(undominated, key=lambda t: (len(self.closed(t)), t))
            for c in sorted(self.closed(y)):
                search(chosen | {c}, undominated - self.closed(c))

        search(frozenset(), frozenset(area))
        if best[0] == math.inf:
            raise ValueError("not enough robots to guard an area")
        return int(best[0]), best[1]


def _gen_area(m: _Map, rng: random.Random, min_cover: int, centers: list[int]) -> list[int] | None:
    center = rng.choice(centers)
    order = sorted(range(len(m.locations)), key=lambda i: (m.dist[center][i], i))
    # Largest prefix guardable by min_cover robots (guard sets are monotone in the
    # prefix). Upstream loops forever if that prefix needs fewer; we redraw instead.
    lo, hi = 1, len(order)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if m.dominates_within(order[:mid], min_cover):
            lo = mid
        else:
            hi = mid - 1
    if min_cover > 1 and m.dominates_within(order[:lo], min_cover - 1):
        return None
    return sorted(order[:lo])


def _gen_areas(m: _Map, rng: random.Random, num_areas: int, min_cover: int) -> list[list[int]]:
    for _ in range(100):
        centers = set(range(len(m.locations)))
        areas: list[list[int]] = []
        while len(areas) < num_areas and centers:
            area = _gen_area(m, rng, min_cover, sorted(centers))
            if area is None:
                break
            centers -= set(area)
            areas.append(area)
        if len(areas) == num_areas:
            return areas
    raise _Redraw


def _covers(m: _Map, rng: random.Random, num_robots: int, min_cover: int, num_areas: int,
            charge_multiplier: float) -> Setup:
    areas = _gen_areas(m, rng, num_areas, min_cover)
    outside = sorted(set(range(len(m.locations))) - set(itertools.chain(*areas)))
    rng.shuffle(outside)
    start = outside[:num_robots]
    if len(start) != num_robots:
        raise _Redraw

    best: tuple[int, list[list[int]], list[list[int]]] | None = None
    for ordered in itertools.permutations(areas):
        # rendezvous: the location minimising the summed distance from the starts
        meet = min(range(len(m.locations)), key=lambda lid: (sum(m.dist[lid][s] for s in start), lid))
        cost = sum(m.dist[meet][s] for s in start)
        states = [list(start), [meet] * num_robots]
        for area in ordered:
            move, targets = m.min_cost_cover(area, states[-1])
            cost += move
            states.append(targets)
        best_cost = cost if best is None else best[0]
        if best is None or cost < best_cost:
            best = (cost, states, list(ordered))
    assert best is not None  # permutations() always yields at least one ordering
    cost, states, ordered = best
    min_charge = [m.dist[s][states[1][0]] for s in start]
    required = [sum(m.dist[a[r]][b[r]] for a, b in zip(states, states[1:])) for r in range(num_robots)]
    for _ in range(MAX_ATTEMPTS):
        charge = list(min_charge)
        remain = int(sum(required) * charge_multiplier) - sum(charge)
        while remain > 0:
            robot = rng.randint(0, num_robots - 1)
            c = rng.randint(0, remain)
            charge[robot] += c
            remain -= c
        if any(c < r for c, r in zip(charge, required)):
            break
    else:  # upstream loops forever when no robot ever needs a recharge
        raise _Redraw
    return start, charge, [], ordered


def _single_source(
    m: _Map, rng: random.Random, num_robots: int, charge_multiplier: float, move_from_source: bool
) -> Setup:
    n = len(m.locations)
    if n <= num_robots:
        raise ValueError("num_robots must be smaller than the number of locations")
    source = rng.choice(range(n))
    targets: list[int] = []
    while len(targets) != num_robots:
        t = rng.choice(range(n))
        if t != source and t not in targets:
            targets.append(t)
    charge_amount = math.ceil(sum(m.dist[source][t] for t in targets) * charge_multiplier)
    charge: list[int] = []
    remain = charge_amount
    for _ in targets:
        c = rng.choice(range(remain + 1))
        charge.append(c)
        remain -= c
    charge[-1] += charge_amount - sum(charge)
    sources = [source] * num_robots
    if move_from_source:
        for r, t in enumerate(targets):
            dt = m.dist[source][t]
            s = rng.choice([i for i in range(n) if m.dist[i][t] >= m.dist[i][source] + dt])
            sources[r] = s
            charge[r] += m.dist[s][source]
    return sources, charge, targets, []


def make_problem(
    kind: str,
    num_robots: int,
    num_obstacles: int,
    num_viewpoints: int,
    charge_multiplier: float = 1.0,
    min_cover: int = 1,
    num_areas: int = 1,
    move_from_source: bool = False,
    max_distance: float = 0.35,
    max_square_width: float = 0.3,
    seed: int | None = None,
) -> str:
    """Generate a Recharging Robots task.

    The map is a Delaunay triangulation of random viewpoints and the corners of
    random square obstacles (edges longer than ``max_distance`` and square
    diagonals removed). ``covers``: robots start outside ``num_areas`` areas, each
    the largest ball around a random centre that ``min_cover`` robots can guard,
    and must fulfil every area's guard configuration in turn. ``single-source-
    move-to-locations``: robots start at one location (optionally moved away with
    ``move_from_source``) and must reach distinct target locations. The total
    battery is the optimal movement cost times ``charge_multiplier``.
    """
    if kind not in KINDS:
        raise ValueError(f"kind must be one of {', '.join(KINDS)}")
    for name, value, minimum in (
        ("num_robots", num_robots, 1),
        ("num_obstacles", num_obstacles, 0),
        ("num_viewpoints", num_viewpoints, 0),
        ("min_cover", min_cover, 1),
        ("num_areas", num_areas, 1),
    ):
        checked = cast(object, value)  # runtime check: callers may pass any type
        if not isinstance(checked, int) or isinstance(checked, bool) or checked < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if not charge_multiplier >= 1.0:  # pylint: disable=unnecessary-negation  # also rejects NaN
        raise ValueError("charge_multiplier must be at least 1")
    if kind == "covers" and min_cover > num_robots:
        raise ValueError("min_cover must not exceed num_robots")
    if num_obstacles * 4 + num_viewpoints < 3:
        raise ValueError("need at least three locations (4 per obstacle, 1 per viewpoint)")

    rng = random.Random(seed)
    for _ in range(100):
        m = _Map(rng, num_obstacles, num_viewpoints, max_distance, max_square_width)
        if not m.connected():  # upstream asserts connectivity; we redraw
            continue
        try:
            if kind == "covers":
                setup = _covers(m, rng, num_robots, min_cover, num_areas, charge_multiplier)
            else:
                setup = _single_source(m, rng, num_robots, charge_multiplier, move_from_source)
        except _Redraw:
            continue
        break
    else:
        raise ValueError("no valid task in 100 maps; check num_robots, min_cover, num_areas and max_distance")
    starts, charge, goal_targets, areas = setup
    if kind == "covers":
        name = f"recharging-robots-cover-robots{num_robots}-areas{num_areas}-{seed}-{rng.randint(0, 10000)}"
    else:
        name = f"recharge-single-source-move-to-locations-{rng.randint(0, 10000)}"

    battery = sum(charge)
    lines = [f"(define (problem {name})", "(:domain recharging-robots)", "(:objects"]
    lines.append("  " + " ".join(f"location-{i:04d}" for i in range(len(m.locations))) + " - location")
    lines.append("  " + " ".join(f"robot-{i:02d}" for i in range(num_robots)) + " - robot")
    lines.append("  " + " ".join(f"battery-{i:04d}" for i in range(battery + 1)) + " - battery-level")
    if areas:
        lines.append("  " + " ".join(f"config-{i:02d}" for i in range(len(areas))) + " - config")
    lines += [")", "(:init", "  (= (move-cost) 1)", "  (= (recharge-cost) 1)", "  (= (total-cost) 0)"]
    lines += [f"  (connected location-{a:04d} location-{b:04d})" for a, b in m.connections]
    lines += [f"  (battery-predecessor battery-{i:04d} battery-{i + 1:04d})" for i in range(battery)]
    for r, (loc, c) in enumerate(zip(starts, charge)):
        lines += [f"  (at robot-{r:02d} location-{loc:04d})", f"  (battery robot-{r:02d} battery-{c:04d})"]
    for ci, area in enumerate(areas):
        lines += [f"  (guard-config config-{ci:02d} location-{loc:04d})" for loc in area]
    lines += [")", "(:goal", "  (and"]
    lines += [f"    (at robot-{r:02d} location-{t:04d})" for r, t in enumerate(goal_targets)]
    lines += [f"    (config-fullfilled config-{ci:02d})" for ci in range(len(areas))]
    lines += ["  )", ")", "(:metric minimize (total-cost))", ")"]
    return ("\n".join(lines) + "\n").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an IPC 2023 Recharging Robots PDDL problem.")
    parser.add_argument("kind", choices=KINDS)
    parser.add_argument("num_robots", type=int)
    parser.add_argument("num_obstacles", type=int)
    parser.add_argument("num_viewpoints", type=int)
    parser.add_argument("charge_multiplier", type=float, nargs="?", default=1.0)
    parser.add_argument("--min-cover", type=int, default=1, help="covers: robots needed to guard each area")
    parser.add_argument("--num-areas", type=int, default=1, help="covers: number of areas")
    parser.add_argument(
        "--move-from-source", action="store_true", help="single-source: move robots away from the source first"
    )
    parser.add_argument("--max-distance", type=float, default=0.35)
    parser.add_argument("--max-square-width", type=float, default=0.3)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
