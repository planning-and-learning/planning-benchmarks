"""Fresh training tasks for pypddl-datasets' classical Beluga 2025 domain.

This is a standalone training distribution, not the competition's generator.
It uses the five challenge jig types, flights of capacity 40, two-sided racks,
ordered unloading/loading, and ordered production lines. Solvability is not
guaranteed: limited rack space and ordering constraints can cause deadlocks.
"""

import argparse
import random


# (name, empty size, loaded size), as in the Beluga 2025 benchmark.
JIG_TYPES = (
    ("typeA", 4, 4),
    ("typeB", 8, 11),
    ("typeC", 9, 18),
    ("typeD", 18, 25),
    ("typeE", 32, 32),
)


def make_problem(
    num_flights: int = 3,
    jigs_per_flight: int = 2,
    num_racks: int = 2,
    min_rack_size: int = 20,
    max_rack_size: int = 40,
    initial_occupancy: float = 0.3,
    num_trailers: int = 1,
    num_hangars: int = 1,
    num_production_lines: int = 1,
    max_delivery_delay: int = 1,
    jig_type_distribution: int = 0,
    seed: int = 0,
) -> str:
    """Return deterministic PDDL for scalar parameters and a nonnegative seed.

    Counts must be positive; max_delivery_delay may be zero. Rack capacities
    are sampled independently between min_rack_size and max_rack_size (>= 4).
    initial_occupancy is a target fraction in [0, 1] of total rack capacity.
    Fill until reaching that target or no jig fits; the last jig may overshoot.
    Initial jigs are equally likely to be loaded or empty. num_trailers counts
    trailers on EACH side. Type sampling is uniform (0), or chooses the smaller
    (1) or larger (2) of two independent uniform candidate draws.

    Incoming flights carry one type, up to jigs_per_flight jigs, subject to
    aircraft capacity 40 and a packing check against the inventory still on site.
    Loaded jigs enter production after 1..max_delivery_delay flights (immediately
    when zero); remaining production is completed during the last flight.
    Initial loaded jigs wait 0..max_delivery_delay flights. Production orders
    shuffle jobs due together across balanced lines. Returns batch one type
    from initially empty jigs or those produced on PREVIOUS flights, within
    capacity 40. Every loaded jig must visit a hangar; empty jigs without a
    return flight remain on site. Flights can have empty incoming/outgoing loads.
    Start small with num_flights=2, jigs_per_flight=1, initial_occupancy=0,
    min_rack_size=4, max_rack_size=8, max_delivery_delay=0.
    """
    values = {
        "num_flights": num_flights,
        "jigs_per_flight": jigs_per_flight,
        "num_racks": num_racks,
        "min_rack_size": min_rack_size,
        "max_rack_size": max_rack_size,
        "num_trailers": num_trailers,
        "num_hangars": num_hangars,
        "num_production_lines": num_production_lines,
        "max_delivery_delay": max_delivery_delay,
        "jig_type_distribution": jig_type_distribution,
        "seed": seed,
    }
    for name, value in values.items():
        minimum = 0 if name in {"max_delivery_delay", "jig_type_distribution", "seed"} else 1
        if type(value) is not int or value < minimum:  # pylint: disable=unidiomatic-typecheck
            raise ValueError(f"{name} must be an integer >= {minimum}")
    if not 4 <= min_rack_size <= max_rack_size:
        raise ValueError("rack sizes must satisfy 4 <= min_rack_size <= max_rack_size")
    if jig_type_distribution not in (0, 1, 2):
        raise ValueError("jig_type_distribution must be 0, 1, or 2")
    # Exact types reject bool as well as nonnumeric caller input.
    # pylint: disable-next=unidiomatic-typecheck
    if type(initial_occupancy) not in (int, float) or not 0 <= initial_occupancy <= 1:
        raise ValueError("initial_occupancy must be a number in [0, 1]")

    rng = random.Random(seed)

    def choose_type(candidates: list[int]) -> int:
        first = rng.choice(candidates)
        if jig_type_distribution == 0:
            return first
        second = rng.choice(candidates)
        return min(first, second) if jig_type_distribution == 1 else max(first, second)

    capacities = [rng.randint(min_rack_size, max_rack_size) for _ in range(num_racks)]
    # Each jig is (type index, initially empty, arrival flight); -1 means on site.
    jigs: list[tuple[int, bool, int]] = []
    racks: list[list[int]] = [[] for _ in range(num_racks)]
    free_space = capacities.copy()
    production_times: list[int] = []
    incoming: list[list[int]] = [[] for _ in range(num_flights)]
    while sum(capacities) - sum(free_space) < initial_occupancy * sum(capacities):
        empty = rng.choice((False, True))
        candidates = [i for i, (_, small, large) in enumerate(JIG_TYPES)
                      if large <= max(capacities) and (small if empty else large) <= max(free_space)]
        if not candidates:
            break
        kind = choose_type(candidates)
        _, small, large = JIG_TYPES[kind]
        size = small if empty else large
        rack = rng.choice([i for i, space in enumerate(free_space) if space >= size])
        # Empty jigs face the aircraft; loaded jigs face the factory.
        if empty:
            racks[rack].insert(0, len(jigs))
        else:
            racks[rack].append(len(jigs))
        free_space[rack] -= size
        jigs.append((kind, empty, -1))
        production_times.append(-1 if empty else min(num_flights - 1, rng.randint(0, max_delivery_delay)))

    on_site = list(range(len(jigs)))
    produced: set[int] = set()
    outgoing: list[list[int]] = [[] for _ in range(num_flights)]
    production: list[list[int]] = [[] for _ in range(num_production_lines)]
    for flight in range(num_flights):
        # ponytail: greedy packing ignores rack access; the planner checks ordering deadlocks.
        space = capacities.copy()
        site_sizes: list[int] = []
        for jig in on_site:
            kind, empty, _ = jigs[jig]
            _, small, large = JIG_TYPES[kind]
            site_sizes.append(small if empty or jig in produced else large)
        for size in sorted(site_sizes, reverse=True):
            fitting = [(remaining, rack) for rack, remaining in enumerate(space) if remaining >= size]
            if not fitting:
                space = []
                break
            _, rack = min(fitting)
            space[rack] -= size
        batch_limits = {kind: min(jigs_per_flight, 40 // size, sum(remaining // size for remaining in space))
                        for kind, (_, _, size) in enumerate(JIG_TYPES)}
        candidates = [kind for kind, count in batch_limits.items() if count]
        if candidates:
            kind = choose_type(candidates)
            for _ in range(batch_limits[kind]):
                jig = len(jigs)
                incoming[flight].append(jig)
                on_site.append(jig)
                jigs.append((kind, False, flight))
                delay = rng.randint(1, max_delivery_delay) if max_delivery_delay else 0
                production_times.append(min(num_flights - 1, flight + delay))
            rng.shuffle(incoming[flight])

        batch = [jig for jig in on_site if not jigs[jig][1] and jig not in produced
                 and production_times[jig] <= flight]
        rng.shuffle(batch)
        for jig in batch:
            shortest = min(map(len, production))
            line = rng.choice([i for i, jobs in enumerate(production) if len(jobs) == shortest])
            production[line].append(jig)
            produced.add(jig)

        ready: list[list[int]] = [[] for _ in JIG_TYPES]
        for jig in on_site:
            if production_times[jig] < flight:
                ready[jigs[jig][0]].append(jig)
        candidates = [kind for kind, jobs in enumerate(ready) if jobs]
        if candidates:
            kind = rng.choice(candidates)
            outgoing[flight] = ready[kind][:40 // JIG_TYPES[kind][1]]
            departing = set(outgoing[flight])
            on_site = [jig for jig in on_site if jig not in departing]

    objects = [f"{' '.join(f'n{i}' for i in range(max(32, *capacities) + 1))} - num",
               f"{' '.join(kind[0] for kind in JIG_TYPES)} - type",
               f"{' '.join(f'jig{i}' for i in range(len(jigs)))} - jig",
               f"{' '.join(f'rack{i}' for i in range(num_racks))} - rack",
               f"{' '.join(f'flight{i}' for i in range(num_flights))} - beluga",
               f"{' '.join(f'hangar{i}' for i in range(num_hangars))} - hangar",
               f"{' '.join(f'line{i}' for i in range(num_production_lines))} - production-line"]
    num_slots = max(map(len, outgoing))
    if num_slots:
        objects.append(f"{' '.join(f'slot{i}' for i in range(num_slots))} - slot")
    init = ["(= (total-cost) 0)", "(processed-flight flight0)"]
    goals: list[str] = []
    for side in ("bside", "fside"):
        for i in range(num_trailers):
            trailer = f"trailer_{side}{i}"
            objects.append(f"{trailer} - trailer")
            init.extend((f"(empty {trailer})", f"(at-side {trailer} {side})"))
    init.extend(f"(empty hangar{i})" for i in range(num_hangars))
    for jig, (kind, empty, arrival) in enumerate(jigs):
        name, small, large = JIG_TYPES[kind]
        init.extend((f"(is_type jig{jig} {name})", f"(size jig{jig} n{small if empty else large})",
                     f"(empty-size jig{jig} n{small})"))
        if empty:
            init.append(f"(empty jig{jig})")
        else:
            goals.append(f"(empty jig{jig})")
        if arrival >= 0:
            init.append(f"(in jig{jig} flight{arrival})")
    sizes = sorted({size for _, small, large in JIG_TYPES for size in (small, large)})
    for rack, contents in enumerate(racks):
        init.extend((f"(at-side rack{rack} bside)", f"(at-side rack{rack} fside)",
                     f"(free-space rack{rack} n{free_space[rack]})"))
        for size in sizes:
            init.extend(f"(fit n{space - size} n{size} n{space} rack{rack})"
                        for space in range(size, capacities[rack] + 1))
        if not contents:
            init.append(f"(empty rack{rack})")
        else:
            init.extend(f"(in jig{jig} rack{rack})" for jig in contents)
            init.extend((f"(clear jig{contents[0]} bside)", f"(clear jig{contents[-1]} fside)"))
            for left, right in zip(contents, contents[1:]):
                init.extend((f"(next-to jig{left} jig{right} bside)",
                             f"(next-to jig{right} jig{left} fside)"))
    for flight, (arrivals, departures) in enumerate(zip(incoming, outgoing)):
        unload = [f"jig{jig}" for jig in arrivals] + ["dummy-jig"]
        init.append(f"(to_unload {unload[0]} flight{flight})")
        init.extend(f"(next_unload {left} {right})" for left, right in zip(unload, unload[1:]))
        loads = [JIG_TYPES[jigs[jig][0]][0] for jig in departures] + ["dummy-type"]
        slots = [f"slot{i}" for i in range(len(departures))] + ["dummy-slot"]
        init.append(f"(to_load {loads[0]} {slots[0]} flight{flight})")
        init.extend(f"(next_load {loads[i + 1]} {slots[i]} {slots[i + 1]} flight{flight})"
                    for i in range(len(departures)))
        if flight + 1 < num_flights:
            init.append(f"(next-flight-to-process flight{flight} flight{flight + 1})")
        goals.extend((f"(to_unload dummy-jig flight{flight})",
                      f"(to_load dummy-type dummy-slot flight{flight})"))
    for line, jobs in enumerate(production):
        if jobs:
            deliveries = [f"jig{jig}" for jig in jobs] + ["dummy-jig"]
            init.append(f"(to_deliver {deliveries[0]} line{line})")
            init.extend(f"(next_deliver {left} {right})" for left, right in zip(deliveries, deliveries[1:]))
    return (f"(define (problem beluga-training-s{seed})\n (:domain beluga)\n (:objects\n  "
            + "\n  ".join(objects) + "\n )\n (:init\n  " + "\n  ".join(init)
            + "\n )\n (:goal (and\n  " + "\n  ".join(goals)
            + "\n ))\n (:metric minimize (total-cost))\n)\n")


def main(argv: list[str] | None = None) -> int:
    """Write a generated problem to stdout."""
    parser = argparse.ArgumentParser(
        description="Generate a Beluga 2025 deterministic training problem.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--num-flights", type=int, default=3, help="number of flights")
    parser.add_argument("--jigs-per-flight", type=int, default=2, help="maximum incoming jigs per flight")
    parser.add_argument("--num-racks", type=int, default=2, help="number of two-sided racks")
    parser.add_argument("--min-rack-size", type=int, default=20, help="minimum rack capacity (at least 4)")
    parser.add_argument("--max-rack-size", type=int, default=40, help="maximum rack capacity")
    parser.add_argument("--initial-occupancy", type=float, default=0.3, help="target initial rack occupancy in [0, 1]")
    parser.add_argument("--num-trailers", type=int, default=1, help="trailers on each side")
    parser.add_argument("--num-hangars", type=int, default=1, help="number of hangars")
    parser.add_argument("--num-production-lines", type=int, default=1, help="number of ordered production lines")
    parser.add_argument("--max-delivery-delay", type=int, default=1, help="maximum arrival-to-production delay")
    parser.add_argument("--jig-type-distribution", type=int, choices=(0, 1, 2), default=0,
                        help="0: uniform, 1: prefer small jigs, 2: prefer large jigs")
    parser.add_argument("--seed", type=int, default=0, help="nonnegative random seed")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
