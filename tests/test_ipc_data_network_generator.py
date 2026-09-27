import re

import pytest

from pypddl_datasets.generators.classical.ipc.data_network.generator import NETWORKS, main, make_problem


@pytest.mark.parametrize("network", sorted(NETWORKS))
@pytest.mark.parametrize("num_items,num_layers,num_scripts", [(3, 2, 1), (12, 3, 52), (22, 5, 30)])
def test_data_network_items_are_producible_and_goals_unconsumed(
    network: str, num_items: int, num_layers: int, num_scripts: int
) -> None:
    problem = make_problem(num_items, num_layers, num_scripts, network, seed=7)
    assert problem == make_problem(num_items, num_layers, num_scripts, network, seed=7)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    items = re.findall(r"\(data-size (data-(\d+)-\d+) number([1-5])\)", init)
    assert len(items) == num_items
    layer = {item: int(level) for item, level, _ in items}
    assert set(layer.values()) == set(range(num_layers))
    assert sum(level == 0 for level in layer.values()) >= 2

    scripts = re.findall(r"\(script-io (\S+) (\S+) (\S+) (\S+)\)", init)
    assert len(scripts) == num_scripts
    for _, input1, input2, output in scripts:
        assert input1 != input2
        assert layer[input1] == layer[output] - 1 and layer[input2] < layer[output]
    # Every non-initial item has a producer, so all data is derivable from layer 0.
    assert {output for *_, output in scripts} == {item for item, level in layer.items() if level > 0}
    assert {item for item, _ in re.findall(r"\(saved (\S+) (\S+)\)", init)} == {
        item for item, level in layer.items() if level == 0
    }
    consumed = {item for _, input1, input2, _ in scripts for item in (input1, input2)}
    assert {item for item, _ in re.findall(r"\(saved (\S+) (\S+)\)", goal)} == set(layer) - consumed

    servers = len(NETWORKS[network][0])
    assert len(re.findall(r"\(= \(process-cost ", init)) == servers * num_scripts
    assert all(int(cost) >= 1 for cost in re.findall(r"\(= \(process-cost \S+ \S+\) (-?\d+)\)", init))


def test_data_network_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["12", "3", "52", "ring-network", "2019"]) == 0
    assert capsys.readouterr().out == make_problem(12, 3, 52, "ring-network", 2019)


@pytest.mark.parametrize(
    "arguments,match",
    [
        ((3, 3, 1, "tiny-network"), "num_layers must be smaller"),
        ((10, 3, 7, "tiny-network"), "num_scripts must be at least"),
        ((5, 2, 3, "mesh"), "network"),
        ((5, 1, 3, "tiny-network"), "num_layers"),
        ((5, 2, True, "tiny-network"), "num_scripts"),
    ],
)
def test_data_network_rejects_invalid_parameters(
    arguments: tuple[int, int, int, str] | tuple[int, int, bool, str], match: str
) -> None:
    with pytest.raises(ValueError, match=match):
        make_problem(*arguments)
