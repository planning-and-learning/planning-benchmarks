import re

import pytest

from pypddl_datasets.generators.classical.ipc.depots.generator import main, make_problem


def _towers(on_facts, num_pallets):
    """Follow each pallet's tower upwards; fails on cycles or crates on two surfaces."""
    above = {}
    for crate, surface in on_facts:
        assert surface not in above, f"{surface} carries two crates"
        above[surface] = crate
    towers = {}
    for pallet in range(num_pallets):
        tower, surface = [], f"pallet{pallet}"
        while surface in above:
            surface = above[surface]
            tower.append(surface)
        towers[f"pallet{pallet}"] = tower
    return towers


@pytest.mark.parametrize(
    "depots,distributors,trucks,pallets,hoists,crates",
    [(1, 1, 1, 1, 1, 1), (3, 2, 2, 7, 4, 9), (9, 2, 2, 16, 11, 3)],
)
def test_depots_stacks_are_consistent_and_every_place_has_a_hoist(depots, distributors, trucks, pallets, hoists, crates):
    problem = make_problem(depots, distributors, trucks, pallets, hoists, crates, seed=3)
    assert problem == make_problem(depots, distributors, trucks, pallets, hoists, crates, seed=3)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    places = [f"depot{i}" for i in range(depots)] + [f"distributor{i}" for i in range(distributors)]
    num_pallets = max(pallets, len(places))
    num_hoists = max(hoists, len(places))
    at = dict(re.findall(r"\(at (\w+) (\w+)\)", init))

    # One hoist and one pallet per place (plus random extras) keep every task solvable.
    assert [at[f"hoist{i}"] for i in range(len(places))] == places
    assert [at[f"pallet{i}"] for i in range(len(places))] == places
    assert len([name for name in at if name.startswith("hoist")]) == num_hoists
    assert len([name for name in at if name.startswith("truck")]) == trucks

    towers = _towers(re.findall(r"\(on (\w+) (\w+)\)", init), num_pallets)
    assert sorted(crate for tower in towers.values() for crate in tower) == sorted(f"crate{i}" for i in range(crates))
    clear = set(re.findall(r"\(clear (\w+)\)", init))
    assert clear == {tower[-1] if tower else pallet for pallet, tower in towers.items()}
    for pallet, tower in towers.items():
        assert all(at[crate] == at[pallet] for crate in tower)

    goal_on = re.findall(r"\(on (\w+) (\w+)\)", goal)
    goal_towers = _towers(goal_on, num_pallets)
    assert sorted(crate for tower in goal_towers.values() for crate in tower) == sorted(crate for crate, _ in goal_on)
    goal_crates = [int(crate.removeprefix("crate")) for crate, _ in goal_on]
    assert goal_crates == sorted(goal_crates)


def test_depots_cli_matches_make_problem(capsys):
    assert main(["-e", "2", "-i", "1", "-t", "2", "-p", "4", "-u", "3", "-c", "5", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(2, 1, 2, 4, 3, 5, seed=9)


@pytest.mark.parametrize("parameter", ["num_depots", "num_distributors", "num_trucks", "num_pallets", "num_hoists", "num_crates"])
def test_depots_rejects_invalid_parameters(parameter):
    parameters = dict(num_depots=1, num_distributors=1, num_trucks=1, num_pallets=1, num_hoists=1, num_crates=1)
    parameters[parameter] = 0
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)


def test_depots_ipc_encoding_uses_type_predicates():
    from pypddl_datasets.generators.classical.autoscale.depots.generator import make_problem as make_typed

    untyped, typed = make_problem(1, 1, 1, 2, 2, 3, seed=4), make_typed(1, 1, 1, 2, 2, 3, seed=4)
    assert "(:domain depot)" in untyped and " - " not in untyped.split("(:init")[0]
    assert {"(place depot0)", "(place distributor0)", "(surface crate0)", "(pallet pallet0)"} <= set(re.findall(r"\(\w+ \w+\)", untyped))
    assert "(:domain depots)" in typed and "crate0 crate1 crate2 - crate" in typed and "(place " not in typed
