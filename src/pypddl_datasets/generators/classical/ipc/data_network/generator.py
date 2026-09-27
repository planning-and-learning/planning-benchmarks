#!/usr/bin/env python3
# Port of pddl-generators/data-network/generator/generator.py (Manuel Heusner),
# including its tiny-, small- and ring-network definitions, as called by
# Autoscale: generator.py {items} {layers} {scripts} {network} {seed}.
# numpy's RNG is replaced by random.Random; the drawn distributions are unchanged.

from __future__ import annotations

import argparse
import random
import re
import sys

# network -> (servers as (capacity, io cost, processing mean, processing stddev), connections (a, b, send cost))
NETWORKS = {
    "tiny-network": (
        [(16, 5, 20, 4), (8, 1, 10, 2), (8, 1, 10, 2)],
        [(1, 2, 4), (1, 3, 6)],
    ),
    "small-network": (
        [(16, 5, 20, 4), (8, 1, 10, 2), (8, 1, 10, 2), (8, 1, 10, 2)],
        [(1, 2, 4), (1, 3, 6), (1, 4, 6), (2, 3, 2)],
    ),
    # A ring of small machines 2-7 with fast links between themselves and an
    # expensive link to a super computer in the middle.
    "ring-network": (
        [(16, 1, 10, 2)] + [(8, 2, 20, 4)] * 6,
        [(1, i, 20) for i in range(2, 8)] + [(i, i + 1 if i < 7 else 2, 2) for i in range(2, 8)],
    ),
}
MIN_DATA_SIZE, MAX_DATA_SIZE = 1, 5


def _natural_key(text: str) -> list[int | str]:
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", text)]


def make_problem(num_items: int, num_layers: int, num_scripts: int, network: str, seed: int = 0) -> str:
    """Generate a data-network task.

    Data items are spread over ``num_layers`` layers (at least one per layer,
    two on layer 0). Layer 0 items are initially saved on random servers; each
    item on layer ``k > 0`` is the output of a script with one input from layer
    ``k - 1`` and a different input from any lower layer; remaining scripts are
    random extra producers. Items no script consumes are goals on random servers.
    """
    for name, value, minimum in (("num_items", num_items, 3), ("num_layers", num_layers, 2), ("num_scripts", num_scripts, 1)):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_items <= num_layers:
        raise ValueError("num_layers must be smaller than num_items")
    if num_scripts < num_items - 2:
        raise ValueError("num_scripts must be at least num_items - 2")
    if network not in NETWORKS:
        raise ValueError(f"network must be one of {', '.join(NETWORKS)}")

    rng = random.Random(seed)
    server_specs, connections = NETWORKS[network]
    servers = [f"server{i}" for i in range(1, len(server_specs) + 1)]

    sizes = [rng.randint(MIN_DATA_SIZE, MAX_DATA_SIZE) for _ in range(num_items)]
    layer_of = []
    for index in range(num_items):
        if index < num_layers:
            layer_of.append(index)
        elif index == num_layers:
            layer_of.append(0)
        else:
            layer_of.append(rng.randrange(num_layers))
    layers: list[list[str]] = [[] for _ in range(num_layers)]
    size_of = {}
    for index, (layer, size) in enumerate(zip(layer_of, sizes), start=1):
        item = f"data-{layer}-{index}"
        layers[layer].append(item)
        size_of[item] = size

    scripts = []
    used = set()

    def add_script(layer: int, output: str) -> None:
        input1 = rng.choice(layers[layer - 1])
        input2 = input1
        while input2 == input1:
            input2 = rng.choice(layers[rng.randrange(layer)])
        used.update((input1, input2))
        scripts.append((f"script{len(scripts) + 1}", input1, input2, output))

    for layer in range(1, num_layers):
        for item in layers[layer]:
            add_script(layer, item)
    while len(scripts) < num_scripts:
        layer = rng.randrange(1, num_layers)
        add_script(layer, rng.choice(layers[layer]))

    # With sizes <= 5 every script fits the 16-capacity server and every item
    # fits the 8-capacity ones, so upstream's capacity checks never fire.
    max_capacity = max(spec[0] for spec in server_specs)
    process_costs = {}
    for server, (_, _, mean, stddev) in zip(servers, server_specs):
        for script, *_ in scripts:
            process_costs[(script, server)] = max(1, int(rng.gauss(mean, stddev)))
    init_items = sorted(((item, rng.choice(servers)) for item in layers[0]), key=lambda pair: _natural_key(pair[0]))
    goal_items = [item for layer in layers for item in layer if item not in used]
    goal_pairs = sorted(((item, rng.choice(servers)) for item in goal_items), key=lambda pair: _natural_key(pair[0]))

    data_sizes = sorted(set(sizes))
    items = sorted(size_of, key=_natural_key)
    lines = [f"(define (problem p{num_items}-{num_layers}-{num_scripts}-{network}-{seed})", "    (:domain data-network)", "    (:objects"]
    for names, type_name in ((items, "data"), ([script for script, *_ in scripts], "script"), (servers, "server"), ([f"number{n}" for n in range(max_capacity + 1)], "numbers")):
        lines.extend(f"              {name}" for name in names[:-1])
        lines.append(f"              {names[-1]} - {type_name}")
    lines += ["    )", "    (:init"]
    lines.extend(f"           (SCRIPT-IO {script} {input1} {input2} {output})" for script, input1, input2, output in scripts)
    for a, b, _ in sorted(connections):
        lines.append(f"           (CONNECTED server{a} server{b})")
        lines.append(f"           (CONNECTED server{b} server{a})")
    lines.extend(f"           (DATA-SIZE {item} number{size_of[item]})" for item in items)
    lines.extend(f"           (CAPACITY {server} number{spec[0]})" for server, spec in zip(servers, server_specs))
    for i in range(max_capacity + 1):
        lines.extend(f"           (SUM number{i} number{j} number{i + j})" for j in data_sizes if i + j <= max_capacity)
    capacities = sorted({spec[0] for spec in server_specs})
    for i in range(1, max_capacity + 1):
        lines.extend(f"           (LESS-EQUAL number{i} number{j})" for j in capacities if i <= j)
    lines.append("           (= (total-cost) 0)")
    for (script, server), cost in sorted(process_costs.items(), key=lambda entry: _natural_key(entry[0][0] + entry[0][1])):
        lines.append(f"           (= (process-cost {script} {server}) {cost})")
    send_costs = sorted(
        ((f"server{a}", f"server{b}", f"number{size}", size * send) for size in data_sizes for a, b, send in connections),
        key=lambda entry: _natural_key(entry[0] + entry[1] + entry[2]),
    )
    for a, b, number, cost in send_costs:
        lines.append(f"           (= (send-cost {a} {b} {number}) {cost})")
        lines.append(f"           (= (send-cost {b} {a} {number}) {cost})")
    io_costs = sorted(
        ((server, f"number{size}", size * spec[1]) for size in data_sizes for server, spec in zip(servers, server_specs)),
        key=lambda entry: _natural_key(entry[0] + entry[1]),
    )
    lines.extend(f"           (= (io-cost {server} {number}) {cost})" for server, number, cost in io_costs)
    lines.extend(f"           (saved {item} {server})" for item, server in init_items)
    lines.extend(f"           (usage {server} number0)" for server in servers)
    lines += ["    )", "    (:goal", "           (and"]
    lines.extend(f"                (saved {item} {server})" for item, server in goal_pairs)
    lines += ["           )", "    )", "    (:metric minimize (total-cost))", ")", ""]
    return ("\n".join(lines)).lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a data-network PDDL problem.")
    parser.add_argument("num_items", type=int, help="number of data items")
    parser.add_argument("num_layers", type=int, help="number of layers (smaller than num_items)")
    parser.add_argument("num_scripts", type=int, help="number of scripts (at least num_items - 2)")
    parser.add_argument("network", choices=sorted(NETWORKS))
    parser.add_argument("seed", type=int, nargs="?", default=0)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_items, args.num_layers, args.num_scripts, args.network, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
