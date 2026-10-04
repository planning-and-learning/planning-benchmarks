from collections import Counter
from pathlib import Path
import random
import re
import subprocess
import sys
from typing import cast

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.beluga2025.scalability_deterministic import generator
from pypddl_datasets.generators.classical.beluga2025.scalability_deterministic.generator import main, make_problem

DOMAIN = Path(generator.__file__).with_name("domain.pddl")
REFERENCE = Path(__file__).resolve().parents[1] / "data/classical/beluga2025/scalability-deterministic/domain.pddl"


def test_domain_file_is_the_benchmark_file() -> None:
    assert DOMAIN.read_bytes() == REFERENCE.read_bytes()


@pytest.mark.parametrize("seed", range(3))
@pytest.mark.parametrize("config", [
    {},
    {"num_flights": 1, "jigs_per_flight": 1, "initial_occupancy": 0, "min_rack_size": 4, "max_rack_size": 4},
    {"num_flights": 4, "jigs_per_flight": 10, "num_racks": 4, "num_trailers": 2,
     "num_hangars": 2, "num_production_lines": 3, "initial_occupancy": 1, "max_delivery_delay": 3},
])
def test_seeded_output_and_strict_parsing(config: dict[str, int], seed: int, tmp_path: Path) -> None:
    state = random.getstate()
    problem = make_problem(**config, jig_type_distribution=seed, seed=seed)
    make_problem(seed=42, jig_type_distribution=2)
    assert problem == make_problem(**config, jig_type_distribution=seed, seed=seed)
    assert state == random.getstate()
    assert make_problem(seed=42) != make_problem(seed=43)
    path = tmp_path / "problem.pddl"
    path.write_text(problem, encoding="utf-8")
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(path)


@pytest.mark.parametrize("config", [
    {"num_flights": 0}, {"jigs_per_flight": 0}, {"num_racks": 0}, {"min_rack_size": 3},
    {"min_rack_size": 30, "max_rack_size": 20},
    {"num_trailers": 0}, {"num_hangars": 0}, {"num_production_lines": 0},
    {"initial_occupancy": -1}, {"initial_occupancy": 2}, {"max_delivery_delay": -1},
    {"jig_type_distribution": 3}, {"seed": -1},
])
def test_invalid_parameters(config: dict[str, int]) -> None:
    with pytest.raises(ValueError):
        make_problem(**config)


def test_invalid_seed_types() -> None:
    for seed in (True, "42", 0.5):
        with pytest.raises(ValueError):
            make_problem(seed=cast(int, seed))


def test_invalid_occupancy() -> None:
    for occupancy in (True, "0.5", float("nan"), float("inf")):
        with pytest.raises(ValueError):
            make_problem(initial_occupancy=cast(float, occupancy))


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0
    assert capsys.readouterr().out == make_problem()
    assert main(["--num-flights", "3", "--min-rack-size", "12", "--max-rack-size", "32",
                 "--initial-occupancy", "0.6", "--seed", "42"]) == 0
    expected = make_problem(num_flights=3, min_rack_size=12, max_rack_size=32, initial_occupancy=0.6, seed=42)
    assert capsys.readouterr().out == expected
    with pytest.raises(SystemExit) as error:
        main(["--min-rack-size", "3"])
    assert error.value.code == 2
    assert "rack sizes" in capsys.readouterr().err


def test_standalone_script(tmp_path: Path) -> None:
    script = tmp_path / "generator.py"
    script.write_text(Path(generator.__file__).read_text(encoding="utf-8"), encoding="utf-8")
    result = subprocess.run([sys.executable, "-I", str(script), "--seed", "42"],
                            capture_output=True, text=True, check=True)
    assert result.stdout == make_problem(seed=42)


def test_rack_pressure_batches_and_causal_production_orders() -> None:
    """Check the emitted tasks, including whether each return has available predecessors."""
    observed: set[str] = set()
    empty_sizes = {name: empty for name, empty, _ in generator.JIG_TYPES}
    for seed in range(10):
        problem = make_problem(num_flights=8, jigs_per_flight=4, num_racks=5,
                               initial_occupancy=0.65, num_production_lines=3,
                               max_delivery_delay=2, seed=seed)
        initial = problem.split("(:init", 1)[1].split("(:goal", 1)[0]

        def facts(predicate: str, text: str = initial) -> list[list[str]]:
            return [match.group(1).split()
                    for match in re.finditer(rf"\({predicate}\s+([^()]*)\)", text)]

        types = dict(facts("is_type"))
        sizes = {jig: int(size[1:]) for jig, size in facts("size")}
        free = {rack: int(size[1:]) for rack, size in facts("free-space")}
        capacities = {rack: max(int(before[1:]) for _, _, before, location in facts("fit") if location == rack)
                      for rack in free}
        assert all(20 <= size <= 40 for size in capacities.values())
        if len(set(capacities.values())) > 1:
            observed.add("different rack capacities")
        if any(min(capacities.values()) < size <= max(capacities.values()) for size in sizes.values()):
            observed.add("jigs that fit only some racks")
        locations = dict(facts("in"))
        occupied = 0
        for rack, capacity in capacities.items():
            contents = {jig for jig, location in locations.items() if location == rack}
            used = sum(sizes[jig] for jig in contents)
            assert used + free[rack] == capacity
            occupied += used
            if len(contents) > 1:
                observed.add("initial stacks")
        assert occupied >= 0.65 * sum(capacities.values()) or all(space < 4 for space in free.values())

        initially_empty = {jig for (jig,) in facts("empty") if jig in types}
        arrival = {jig: int(location.removeprefix("flight")) if location.startswith("flight") else -1
                   for jig, location in locations.items()}
        successor = dict(facts("next_deliver"))
        orders: list[list[str]] = []
        for first, _ in facts("to_deliver"):
            order: list[str] = []
            while first != "dummy-jig":
                assert first not in order
                order.append(first)
                first = successor[first]
            orders.append(order)
        jobs = [jig for order in orders for jig in order]
        assert len(jobs) == len(set(jobs))
        assert set(jobs) == set(types) - initially_empty

        unload_successor = dict(facts("next_unload"))
        unload_first = {flight: jig for jig, flight in facts("to_unload")}
        load_first = {flight: (kind, slot) for kind, slot, flight in facts("to_load")}
        load_next = {(flight, slot): (kind, next_slot) for kind, slot, next_slot, flight in facts("next_load")}
        produced: set[str] = set()
        available = Counter(types[jig] for jig in initially_empty)
        unloaded: list[str] = []
        returned = 0
        for index in range(8):
            flight = f"flight{index}"
            arrivals = {jig for jig, location in locations.items() if location == flight}
            assert len(arrivals) <= 4
            assert len({types[jig] for jig in arrivals}) <= 1
            assert sum(sizes[jig] for jig in arrivals) <= 40
            if len(arrivals) > 1:
                observed.add("incoming batches")
            jig = unload_first[flight]
            batch: list[str] = []
            while jig != "dummy-jig":
                assert jig not in batch
                batch.append(jig)
                jig = unload_successor[jig]
            assert set(batch) == arrivals
            unloaded.extend(batch)

            # A return can use only earlier arrivals, after all production predecessors.
            if index:
                for order in orders:
                    for jig in order:
                        if arrival[jig] >= index:
                            break
                        if jig not in produced:
                            available[types[jig]] += 1
                            produced.add(jig)
            kind, slot = load_first[flight]
            demand: list[str] = []
            visited: set[str] = set()
            while kind != "dummy-type":
                assert slot not in visited
                visited.add(slot)
                demand.append(kind)
                kind, slot = load_next[flight, slot]
            assert slot == "dummy-slot"
            assert len(set(demand)) <= 1
            assert sum(empty_sizes[kind] for kind in demand) <= 40
            for kind in demand:
                assert available[kind] > 0, (seed, flight, kind)
                available[kind] -= 1
            returned += len(demand)
        if returned > len(initially_empty):
            observed.add("returns requiring production")
        positions = {jig: index for index, jig in enumerate(unloaded)}
        for order in orders:
            indices = [positions[jig] for jig in order if jig in positions]
            if indices != sorted(indices):
                observed.add("production differs from unload order")
    assert observed == {"different rack capacities", "jigs that fit only some racks", "initial stacks",
                        "incoming batches", "returns requiring production", "production differs from unload order"}
