#!/usr/bin/env python3
# Port of Autoscale's pddl-generators settlers/generator.py (Marcel Steinmetz), the generator
# of the IPC 2018 Settlers tasks, with the IPC problem encoding (independent conditional
# effects, independent resource levels). The tasks were made under Python 2, so draws use
# Python 2's randint/sample/shuffle; the seed in an IPC task header reproduces its map and
# goals. Upstream computes the minimal ship transport for island maps with a CPLEX MIP; this
# port uses a feasible solution of the same MIP (round trips from each sea's wharf), an upper
# bound, so resource levels are never below upstream's and tasks stay solvable.

from __future__ import annotations

import argparse
import math
import random
import sys
from collections import defaultdict

RESOURCES = ["stone", "timber", "ore", "wood", "coal", "iron"]
NUM_BUILDINGS = 3  # coal stack, sawmill, ironworks (docks/wharf unsupported upstream)
SHIP_CAPACITY = 8
TRIP_FUEL = 2
TRACKS = {  # (constrainedness, constraint increment, vehicles, vehicle increment), generate-instances.py
    "opt": (1.2, 4, 1.2, 2),
    "sat": (1.5, 5, 1.5, 3),
}
MAPS = {"tiny": (3, 2, 0), "small": (5, 5, 1), "large": (8, 9, 1), "huge": (16, 18, 2)}  # locations, edges, seas


class _Py2Random(random.Random):
    """Python 2's randint/sample(k=1)/shuffle on top of the (unchanged) Mersenne Twister."""

    def rnd_int(self, n: int) -> int:  # randint(0, n - 1)
        return int(self.random() * n)

    def rnd_sample(self, x) -> int:  # sample(sorted(x), 1)[0]
        pool = sorted(x)
        return pool[int(self.random() * len(pool))]

    def rnd_shuffle(self, x: list[int]) -> list[int]:
        y = list(x)
        for i in reversed(range(1, len(y))):
            j = int(self.random() * (i + 1))
            y[i], y[j] = y[j], y[i]
        return y


class _Map:
    def __init__(self, rng: _Py2Random, locations: int, edges: int, seas: int, prob_coast: int):
        if edges > locations * (locations - 1) // 2 or seas > locations:
            raise ValueError("too many edges or seas for the number of locations")
        self.landmap: list[set[int]] = [set() for _ in range(locations)]
        self.location_to_sea: list[int | None] = [None] * locations
        self.sea_to_locations: list[list[int]] = [[] for _ in range(seas)]
        self.woodland = 0
        self.mountain = rng.rnd_int(locations // 2)
        self.metalliferous = rng.rnd_int(locations // 2)
        if seas > 0 and prob_coast > 0:
            next_free_sea = 0
            for x in range(1, locations):  # woodland is never at the coast
                if next_free_sea < seas or rng.rnd_int(prob_coast) == 0:
                    sea = rng.rnd_int(seas) if next_free_sea >= seas else next_free_sea
                    self.location_to_sea[x] = sea
                    self.sea_to_locations[sea].append(x)
                    next_free_sea += 1
        # make the map connected (by land or through a shared sea)
        sea0 = self.location_to_sea[0]
        connected = sorted({0, *(self.sea_to_locations[sea0] if sea0 is not None else [])})
        for t in rng.rnd_shuffle([x for x in range(locations) if x not in connected]):
            if t in connected:
                continue
            s = rng.rnd_sample(connected)
            self._link(s, t)
            connected.append(t)
            edges -= 1
            if self.location_to_sea[t] is not None:
                connected += [t2 for t2 in self.sea_to_locations[self.location_to_sea[t]] if t2 not in connected]
        available = [x for x in range(locations) if len(self.landmap[x]) < locations - 1]
        while edges > 2:  # keep two edges for the resource connectivity below
            edges -= self._random_edge(rng, available, locations)
        # woodland, metalliferous and mountain must be connected by land
        reachable = self.reachability()
        connected_set = set(reachable[self.woodland])
        for t in rng.rnd_shuffle([x for x in [self.metalliferous, self.mountain] if x not in connected_set]):
            if t in connected_set:
                continue
            s = rng.rnd_sample(connected_set)
            self._link(s, t)
            connected_set |= reachable[t]
            if len(self.landmap[s]) == locations - 1:
                available.remove(s)
            if len(self.landmap[t]) == locations - 1:
                available.remove(t)
            edges -= 1
        while edges > 0:
            edges -= self._random_edge(rng, available, locations)
        if edges < 0:
            raise ValueError("not enough edges to connect the map")

    def _link(self, s: int, t: int) -> None:
        self.landmap[s].add(t)
        self.landmap[t].add(s)

    def _random_edge(self, rng: _Py2Random, available: list[int], locations: int) -> int:
        i = rng.rnd_int(len(available))
        s = available[i]
        t = rng.rnd_sample(set(range(locations)) - self.landmap[s] - {s})
        self._link(s, t)
        if len(self.landmap[s]) == locations - 1:
            del available[i]
        if len(self.landmap[t]) == locations - 1:
            available.remove(t)
        return 1

    def reachability(self) -> list[set[int]]:
        """Land-reachable locations per location (the land graph is undirected)."""
        result: list[set[int]] = [set() for _ in self.landmap]
        for x in range(len(self.landmap)):
            if result[x]:
                continue
            component, stack = {x}, [x]
            while stack:
                for y in self.landmap[stack.pop()]:
                    if y not in component:
                        component.add(y)
                        stack.append(y)
            for y in component:
                result[y] = component
        return result


# goal = (kind, location, extra); resource needs per kind: (stone, timber, ore, processed, iron, coal, wood)
_NEEDS = {
    "rail": (0, 3, 1, 2, True, True, False),
    "coal-stack": (0, 1, 0, 1, False, False, False),
    "sawmill": (0, 2, 0, 2, False, False, False),
    "ironworks": (2, 2, 0, 4, False, False, True),
}


def _needs(goal: tuple[str, int, int]) -> tuple[int, int, int, int, bool, bool, bool]:
    kind, _, n = goal
    if kind == "house":
        return n, n, 0, 2 * n, False, False, True
    return _NEEDS[kind]


def _goal_fact(goal: tuple[str, int, int]) -> str:
    kind, x, y = goal
    return {
        "rail": f"(connected-by-rail p{x} p{y})",
        "house": f"(housing p{x} hl{y})",
        "coal-stack": f"(has-coal-stack p{x})",
        "sawmill": f"(has-sawmill p{x})",
        "ironworks": f"(has-ironworks p{x})",
    }[kind]


def _goals(rng: _Py2Random, m: _Map, locations: int, num_goals: int, ph: int, pb: int, pr: int) -> list[tuple[str, int, int]]:
    goals: list[tuple[str, int, int]] = []
    psum = ph + pb + pr
    locb = list(range(locations))
    buildings: dict[int, set[int]] = defaultdict(set)
    for x in range(locations):
        if m.location_to_sea[x] is None:
            buildings[x] = {3, 4}
    locr = [x for x in range(locations) if m.landmap[x]]
    rail_links: dict[int, set[int]] = defaultdict(set)
    houses: dict[int, int] = defaultdict(int)
    if not locr:
        p = int((pb / psum) * pr)
        pb, ph, pr = pb + p, ph + pr - p, 0
    for _ in range(num_goals):
        what = 1 + int(rng.random() * psum)  # randint(1, psum)
        if what <= ph:
            houses[rng.rnd_int(locations)] += 1
        elif what <= ph + pb:
            i = rng.rnd_int(len(locb))
            x = locb[i]
            t = rng.rnd_sample(set(range(NUM_BUILDINGS)) - buildings[x])
            goals.append((("coal-stack", "sawmill", "ironworks")[t], x, 0))
            buildings[x].add(t)
            if len(buildings[x]) == NUM_BUILDINGS:
                del locb[i]
                if not locb:
                    p = int((pr / psum) * pb)
                    pr, ph, pb = pr + p, ph + pb - p, 0
        else:
            i = rng.rnd_int(len(locr))
            x = locr[i]
            y = rng.rnd_sample(m.landmap[x] - rail_links[x])
            goals.append(("rail", x, y))
            rail_links[x].add(y)
            if len(rail_links[x]) == len(m.landmap[x]):
                del locr[i]
                if not locr:
                    p = int((pb / psum) * pr)
                    pb, ph, pr = pb + p, ph + pr - p, 0
    goals += [("house", loc, n) for loc, n in sorted(houses.items())]
    return goals


def _transport(nodes: list[dict], num_seas: int) -> int:
    """Trips of a feasible solution to upstream's ship-transport MIP (an upper bound on its optimum).

    Each sea's single distributor (the node holding its wharf) serves the nodes discovered
    through that sea with round trips of at most SHIP_CAPACITY units; its last trip does not
    return. Every departing trip costs TRIP_FUEL units at its origin, so a served node's
    delivery includes the fuel of its return trips and everything it distributes onward.
    """
    served: dict[int, list[int]] = defaultdict(list)  # sea -> nodes discovered through it
    for node in nodes[1:]:
        served[node["via"]].append(node["iid"])
    demand = {node["iid"]: node["required"] for node in nodes}
    trips_total = 0
    # nodes are in BFS order, so children follow parents: settle leaves first
    for node in reversed(nodes):
        for sea in sorted(node["distributor"]):
            children = [iid for iid in served.get(sea, []) if iid != node["iid"] and demand[iid] > 0]
            if not children:
                continue
            last = children[-1]
            for child in children:
                base, trips = demand[child], 0
                while True:  # fixed point: returns cost fuel at the child
                    returns = trips - 1 if child == last else trips
                    needed = base + TRIP_FUEL * max(returns, 0)
                    new_trips = math.ceil(needed / SHIP_CAPACITY) if needed > 0 else 0
                    if new_trips == trips:
                        break
                    trips = new_trips
                returns = max(trips - 1 if child == last else trips, 0)
                demand[node["iid"]] += needed + TRIP_FUEL * trips
                trips_total += trips + returns
    return trips_total


def _min_resources(m: _Map, goals: list[tuple[str, int, int]]) -> tuple[int, int, int, int]:
    """Upstream's minimal (stone, timber, ore, vehicles) to reach the goals (CPLEX replaced)."""
    reachable = m.reachability()
    locations = len(m.landmap)
    abstract: dict[int, int] = {}
    reverse_map: list[set[int]] = []
    for x in range(locations):
        if x == min(reachable[x]):
            abstract[x] = len(reverse_map)
            reverse_map.append(reachable[x])
    abstract_of = [abstract[min(reachable[x])] for x in range(locations)]
    abstr_start = abstract_of[min(m.woodland, m.mountain, m.metalliferous)]
    num_seas = len(m.sea_to_locations)
    loc_to_seas: list[set[int]] = [set() for _ in reverse_map]
    sea_to_locs: list[set[int]] = [set() for _ in range(num_seas)]
    for x, a in abstract.items():
        for y in reachable[x]:
            sea = m.location_to_sea[y]
            if sea is not None:
                loc_to_seas[a].add(sea)
                sea_to_locs[sea].add(a)

    stone = timber = ore = vehicles = 0
    processed = [0] * len(reverse_map)
    num_required = [0] * locations
    required = [False] * locations
    locs_req_res: set[int] = set()
    iron = coal = wood = False
    has = set()
    base = {m.woodland, m.mountain, m.metalliferous}
    for goal in goals:
        s, t, o, p, needs_iron, needs_coal, needs_wood = _needs(goal)
        loc = goal[1]
        a = abstract_of[loc]
        locs_req_res.add(a)
        required[loc] = (loc not in base) or (loc != m.woodland and t > 0) or (loc != m.mountain and s > 0) \
            or (loc != m.metalliferous and o > 0)
        stone, timber, ore = stone + s, timber + t, ore + o
        num_required[loc] += p
        processed[a] += p
        iron, coal, wood = iron or needs_iron, coal or needs_coal, wood or needs_wood
        if a == abstr_start and goal[0] in ("sawmill", "coal-stack", "ironworks"):
            has.add(goal[0])
    wharf_required = len(locs_req_res) > 1 or abstr_start not in locs_req_res
    iron = iron or wharf_required
    coal, wood = coal or iron, wood or iron
    required[m.metalliferous] = required[m.metalliferous] or (
        iron and (m.metalliferous != m.woodland or m.metalliferous != m.mountain))
    if required[m.metalliferous]:
        locs_req_res.add(abstr_start)
    for needed, building in ((iron, "ironworks"), (coal, "coal-stack"), (wood, "sawmill")):
        if needed and building not in has:
            s, t, o = _NEEDS[building][:3]
            stone, timber, ore = stone + s, timber + t, ore + o
    if wharf_required or any(required[loc] for loc in reverse_map[abstr_start]):
        timber, vehicles = timber + 1, vehicles + 1
    if not wharf_required:
        return stone, timber, ore, vehicles

    for num_wharfs in range(num_seas + 1):
        best: tuple[int, int, int] | None = None  # (vehicles, timber, ore)
        for root_sea in sorted(loc_to_seas[abstr_start]):
            if num_wharfs == 0:
                continue  # goals never contain wharfs
            # choose which seas get a wharf (depth-first, as upstream), then where
            for seas_choice in _sea_selections(root_sea, abstr_start, sea_to_locs, locs_req_res, num_wharfs):
                for wharfs in _wharf_placements(seas_choice, root_sea, abstr_start):
                    result = _transport_cost(m, wharfs, abstr_start, abstract_of, reverse_map, reachable,
                                             loc_to_seas, locs_req_res, required, processed, num_required, num_seas)
                    if best is None or result[0] < best[0] or (result[0] == best[0] and result[1] < best[1]):
                        best = result
        if best is not None:
            return stone + num_wharfs * 4, timber + best[1], ore + best[2], vehicles + best[0]
    raise ValueError("no wharf placement connects all goal locations")


def _sea_selections(root_sea, abstr_start, sea_to_locs, locs_req_res, num_wharfs):
    """Sets of covered seas (with candidate wharf locations) reaching all required locations."""
    num_seas = len(sea_to_locs)
    results = []

    def extend(covered: dict[int, set[int]], reached: set[int], start: int) -> None:
        if locs_req_res <= reached:
            results.append(dict(covered))
            return
        for sea in range(start, num_seas):
            if sea in covered or len(covered) >= num_wharfs:
                continue
            candidates = sea_to_locs[sea] & reached
            if candidates and not sea_to_locs[sea] <= reached:
                covered[sea] = candidates
                extend(covered, reached | sea_to_locs[sea], 0)
                del covered[sea]

    extend({root_sea: {abstr_start}}, set(sea_to_locs[root_sea]), 0)
    return results


def _wharf_placements(covered: dict[int, set[int]], root_sea: int, abstr_start: int):
    """One wharf location per covered sea (the root sea's wharf is at the start island)."""
    seas = sorted(covered)
    placements: list[dict[int, int]] = [{}]
    for sea in seas:
        options = [abstr_start] if sea == root_sea else sorted(covered[sea])
        placements = [{**p, sea: loc} for p in placements for loc in options]
    return placements


def _transport_cost(m, wharfs, abstr_start, abstract_of, reverse_map, reachable, loc_to_seas, locs_req_res,
                    required, processed, num_required, num_seas):
    covered = set(wharfs)
    wharf_at: dict[int, set[int]] = defaultdict(set)
    for sea, loc in wharfs.items():
        wharf_at[loc].add(sea)
    needs_cart = [False] * len(reverse_map)
    needs_cart[abstr_start] = True
    for x in range(len(reverse_map)):
        if x == abstr_start:
            continue
        if wharf_at[x]:
            needs_cart[x] = True
        elif x in locs_req_res:
            needs_cart[x] = any(required[loc] and (m.location_to_sea[loc] is None or m.location_to_sea[loc] not in covered)
                                for loc in reverse_map[x])
    # flow graph: abstract islands with carts, concrete coastal locations without
    nodes = [{"iid": 0, "ref": abstr_start, "abstract": True, "required": 12 * len(wharf_at[abstr_start]),
              "distributor": set(wharf_at[abstr_start]), "via": None}]
    lookup: dict[int, int] = {loc: 0 for loc in reverse_map[abstr_start]}
    i = 0
    while i < len(nodes):
        node = nodes[i]
        if node["abstract"]:
            succ = [(sea, loc) for sea in sorted(loc_to_seas[node["ref"]]) for loc in m.sea_to_locations[sea]]
        else:
            sea = m.location_to_sea[node["ref"]]
            succ = [(sea, loc) for loc in m.sea_to_locations[sea]] if sea is not None else []
        for sea, loc in succ:
            if loc in lookup or sea not in covered:
                continue
            a = abstract_of[loc]
            iid = len(nodes)
            if needs_cart[a]:
                nodes.append({"iid": iid, "ref": a, "abstract": True, "required": processed[a] + 1 + 12 * len(wharf_at[a]),
                              "distributor": set(wharf_at[a]), "via": sea})
                for loc2 in reachable[loc]:
                    lookup[loc2] = iid
            else:
                nodes.append({"iid": iid, "ref": loc, "abstract": False, "required": num_required[loc],
                              "distributor": set(), "via": sea})
                lookup[loc] = iid
        i += 1
    timber = TRIP_FUEL * _transport(nodes, num_seas)
    vehicles = ore = 0
    for x in range(len(reverse_map)):
        if x != abstr_start and needs_cart[x]:
            timber += 1
            vehicles += 1
    for _sea in wharfs:
        timber += 2 + 4 + 8  # docks + wharf + ship
        ore += 2 + 4  # wharf + ship
        vehicles += 1  # ship
    return vehicles, timber, ore


def make_problem(
    num_locations: int,
    num_edges: int,
    num_seas: int,
    num_goals: int,
    seed: int = 0,
    track: str = "sat",
    prob_coast: int = 2,
    prob_goal_house: int = 3,
    prob_goal_building: int = 3,
    prob_goal_raillink: int = 4,
) -> str:
    """Generate a Settlers task.

    A random connected map of land roads (islands joined by seas; location 0 is the
    woodland, mountain and metalliferous locations lie in the first half) and goals drawn
    as houses, buildings (coal stack, sawmill, ironworks) and rail links with weights
    3/3/4. Resources at the woodland/mountain/metalliferous locations and potential
    vehicles are the minimal amounts needed for the goals, scaled by the track's
    constrainedness plus an increment (`opt`: 1.2/+4 resources, 1.2/+2 vehicles;
    `sat`: 1.5/+5, 1.5/+3).
    """
    for name, value, minimum in (("num_locations", num_locations, 2), ("num_edges", num_edges, 1),
                                 ("num_seas", num_seas, 0), ("num_goals", num_goals, 1)):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if track not in TRACKS:
        raise ValueError(f"track must be one of {', '.join(TRACKS)}")
    constrainedness, increment, vehicle_factor, vehicle_increment = TRACKS[track]

    rng = _Py2Random(seed)
    m = _Map(rng, num_locations, num_edges, num_seas, prob_coast)
    goals = _goals(rng, m, num_locations, num_goals, prob_goal_house, prob_goal_building, prob_goal_raillink)
    stone, timber, ore, vehicles_needed = _min_resources(m, goals)

    num = {
        "stone": int(constrainedness * stone), "timber": int(constrainedness * timber),
        "ore": int(constrainedness * ore), "wood": int(constrainedness * timber),
        "coal": int(constrainedness * timber), "iron": int(constrainedness * ore),
        "housing": int(constrainedness * min(timber, stone)),
    }
    num = {k: v + increment for k, v in num.items()}
    vehicles = int(vehicle_factor * vehicles_needed) + vehicle_increment
    base = {"stone": m.mountain, "timber": m.woodland, "ore": m.metalliferous}

    objects = ["    " + " ".join(f"p{i}" for i in range(num_locations)) + " - place"]
    if vehicles > 0:
        objects.append("    " + " ".join(f"v{i}" for i in range(vehicles)) + " - vehicle")
    for k, v in num.items():  # levels up to 10 are domain constants
        if v > 10:
            objects.append("    " + " ".join(f"{k[0]}l{i}" for i in range(11, v + 1)) + f" - {k}_level")

    init = [f"    (connected-by-land p{i} p{j})" for i in range(num_locations) for j in sorted(m.landmap[i])]
    for sea_locations in m.sea_to_locations:
        init += [f"    (connected-by-sea p{j} p{k})" for j in sea_locations for k in sea_locations if j != k]
    init += [f"    (by-coast p{i})" for i in range(num_locations) if m.location_to_sea[i] is not None]
    init += [f"    (housing p{i} hl0)" for i in range(num_locations)]
    for i in range(num_locations):
        for r in RESOURCES:
            v = num[r] if base.get(r) == i else 0
            init.append(f"    (available-{r} p{i} {r[0]}l{v})")
            init += [f"    (available-atleast-{r} p{i} {r[0]}l{d})" for d in (1, 2, 4) if v >= d]
    for i in range(vehicles):
        init.append(f"    (potential v{i})")
        init += [f"    (available-{r} v{i} {r[0]}l0)" for r in RESOURCES]
    for d in (1, 2):
        init += [f"    (diff-space spl{i + d} spl{d} spl{i})" for i in range(11 - d)]
    init += [f"    (diff-housing hl{i + 1} hl1 hl{i})" for i in range(num["housing"])]
    for r in RESOURCES:
        for d in (1, 2, 4):
            init += [f"    (diff-{r} {r[0]}l{i + d} {r[0]}l{d} {r[0]}l{i})" for i in range(num[r] + 1 - d)]
    for r in RESOURCES:
        for al in (1, 2, 4):
            for consumed in (1, 2, 4):
                for old in range(8):
                    if old - consumed < al <= old:
                        init.append(f"    (del-atleast-{r} {r[0]}l{old} {r[0]}l{consumed} {r[0]}l{al})")
                    if old < al <= old + consumed:
                        init.append(f"    (add-atleast-{r} {r[0]}l{old} {r[0]}l{consumed} {r[0]}l{al})")
    init.append("    (= (total-cost) 0)")
    goal_facts = "\n".join(f"    {_goal_fact(g)}" for g in goals)
    return (f""";; Generator input: seed={seed}, locations={num_locations}, edges={num_edges}, seas={num_seas}, goals={num_goals}, track={track}
(define (problem settlers-{num_locations}-{num_seas}-{num_goals}-{track}-{seed})
(:domain settlers)
(:objects
{chr(10).join(objects)}
)
(:init
{chr(10).join(init)}
)
(:goal
(and
{goal_facts}
)
)
(:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an IPC 2018 Settlers PDDL problem.")
    parser.add_argument("--map", choices=MAPS, help="IPC map preset (sets locations, edges and seas)")
    parser.add_argument("-l", "--num-locations", type=int)
    parser.add_argument("-e", "--num-edges", type=int)
    parser.add_argument("--num-seas", type=int)
    parser.add_argument("-g", "--num-goals", type=int, required=True)
    parser.add_argument("-t", "--track", choices=TRACKS, default="sat")
    parser.add_argument("-s", "--seed", type=int, default=0)
    args = parser.parse_args(argv)
    locations, edges, seas = MAPS[args.map] if args.map else (args.num_locations, args.num_edges, args.num_seas)
    if None in (locations, edges, seas):
        parser.error("give --map or all of --num-locations, --num-edges and --num-seas")
    try:
        problem = make_problem(locations, edges, seas, args.num_goals, args.seed, args.track)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
