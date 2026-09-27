import re
from collections import deque

import pytest

from pypddl_datasets.generators.classical.ipc.sokoban.generator import main, make_problem


def _solvable(problem):
    """BFS over (players, stones) using the task's move-dir graph; every player may move and push."""
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    step = {(a, d): b for a, b, d in re.findall(r"\(move-dir (\S+) (\S+) (\S+)\)", init)}
    goals = set(re.findall(r"\(is-goal (\S+)\)", init))
    players = tuple(re.findall(r"\(at player-\d+ (\S+)\)", init))
    stones = frozenset(re.findall(r"\(at stone-\d+ (\S+)\)", init))
    start = (players, stones)
    seen, queue = {start}, deque([start])
    while queue:
        players, stones = queue.popleft()
        if stones <= goals:
            return True
        for index, player in enumerate(players):
            for (origin, direction), target in step.items():
                if origin != player or target in players:
                    continue
                if target in stones:
                    beyond = step.get((target, direction))
                    if beyond is None or beyond in stones or beyond in players:
                        continue
                    moved = stones - {target} | {beyond}
                else:
                    moved = stones
                state = (players[:index] + (target,) + players[index + 1 :], moved)
                if state not in seen:
                    seen.add(state)
                    queue.append(state)
    return False


@pytest.mark.parametrize("seed", range(6))
@pytest.mark.parametrize("width,height,num_floor,num_stones", [(6, 6, 10, 1), (7, 6, 14, 2), (8, 7, 16, 3)])
def test_sokoban_small_levels_are_solvable(width, height, num_floor, num_stones, seed):
    problem = make_problem(width, height, num_floor, num_stones, seed=seed)
    assert problem == make_problem(width, height, num_floor, num_stones, seed=seed)
    assert _solvable(problem)


@pytest.mark.parametrize("width,height,num_floor,num_stones", [(7, 7, 19, 2), (11, 11, 57, 8), (29, 19, 217, 1)])
def test_sokoban_matches_ipc_encoding(width, height, num_floor, num_stones):
    problem = make_problem(width, height, num_floor, num_stones, seed=1)
    assert problem == problem.lower()
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    locations = re.findall(r"(pos-\S+) - location", problem)
    maze = [line[3:] for line in problem.split("(define", 1)[0].splitlines() if line.startswith(";; ")]
    assert len(locations) == len(maze) * max(map(len, maze))  # every grid cell is a location
    assert len(re.findall(r"\(is-(?:non)?goal \S+\)", init)) == len(locations)
    assert sum(row.count(".") + row.count("*") + row.count("+") for row in maze) == num_stones
    floor = sum(row.count(c) for row in maze for c in " .$*@+")
    assert floor >= num_floor  # plus empty outside cells
    assert len(re.findall(r"\(at-goal stone-\d+\)", goal)) == num_stones
    edges = set(re.findall(r"\(move-dir (\S+) (\S+) \S+\)", init))
    assert all((b, a) in edges for a, b in edges)
    assert "(= (total-cost) 0)" in init and "(:metric minimize (total-cost))" in problem


def test_sokoban_cli_matches_make_problem(capsys):
    assert main(["-x", "8", "-y", "7", "-f", "18", "-b", "2", "-s", "4"]) == 0
    assert capsys.readouterr().out == make_problem(8, 7, 18, 2, seed=4)


@pytest.mark.parametrize(
    "parameter,value",
    [("width", 2), ("height", 2), ("num_floor", 1), ("num_stones", 0), ("num_floor", 26), ("num_stones", 20)],
)
def test_sokoban_rejects_invalid_parameters(parameter, value):
    parameters = dict(width=7, height=7, num_floor=20, num_stones=2)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)


HEX = {"dir-east", "dir-west", "dir-northeast", "dir-northwest", "dir-southeast", "dir-southwest"}


@pytest.mark.parametrize("seed", range(6))
@pytest.mark.parametrize("width,height,num_floor,num_stones,num_players", [(9, 7, 10, 1, 1), (11, 8, 14, 2, 2), (13, 9, 16, 2, 3)])
def test_hexoban_small_levels_are_solvable(width, height, num_floor, num_stones, num_players, seed):
    problem = make_problem(width, height, num_floor, num_stones, seed=seed, grid="hex", num_players=num_players)
    assert problem == make_problem(width, height, num_floor, num_stones, seed=seed, grid="hex", num_players=num_players)
    assert _solvable(problem)
    assert len(re.findall(r"player-\d+ - player", problem)) == num_players


@pytest.mark.parametrize("seed", range(3))
def test_hexoban_matches_autoscale_encoding(seed):
    problem = make_problem(17, 11, 40, 5, seed=seed, grid="hex", num_players=2)
    assert set(re.findall(r"(dir-\S+) - direction", problem)) == HEX
    locations = re.findall(r"pos-(\d+)-(\d+) - location", problem)
    assert locations and all((int(c) + int(r)) % 2 == 0 for c, r in locations)  # every second cell, as build-problems.py
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    delta = {"dir-east": (2, 0), "dir-west": (-2, 0), "dir-northeast": (1, -1), "dir-northwest": (-1, -1), "dir-southeast": (1, 1), "dir-southwest": (-1, 1)}
    moves = re.findall(r"\(move-dir pos-(\d+)-(\d+) pos-(\d+)-(\d+) (\S+)\)", init)
    assert moves and all((int(c2) - int(c1), int(r2) - int(r1)) == delta[d] for c1, r1, c2, r2, d in moves)
    assert {d for *_, d in moves} == HEX


@pytest.mark.parametrize("grid", ["square", "hex"])
def test_sokoban_output_parses_strictly(grid, tmp_path):
    from pathlib import Path

    from pypddl.formalism import Parser, ParserOptions

    from pypddl_datasets.generators.classical.ipc.sokoban import generator

    (tmp_path / "p.pddl").write_text(make_problem(13, 9, 30, 3, seed=2, grid=grid, num_players=2))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


@pytest.mark.parametrize("grid", ["square", "hex"])
@pytest.mark.parametrize("seed", range(5))
def test_reversed_pulls_are_a_multi_player_plan(grid, seed):
    """Replay the recorded pulls backwards: each player walks through free cells to
    its pushing position, pushes, and walks back to where it stood before the pull.
    The level ends solved (with several pulling players in most seeds, see below)."""
    import random

    from pypddl_datasets.generators.classical.ipc.sokoban import generator as g

    dirs = g.HEX_DIRECTIONS if grid == "hex" else g.DIRECTIONS
    rng = random.Random(seed)
    floor = g._floor(rng, 13, 11, 34, dirs)
    cells = sorted(floor)
    goals = set(rng.sample(cells, 4))
    starts = rng.sample([c for c in cells if c not in goals], 3)
    log = []
    stones, players = g._scramble_players(rng, floor, goals, starts, 80, dirs, log)
    stones, players = set(stones), list(players)

    def free(index):
        return floor - {p for i, p in enumerate(players) if i != index}

    for index, before, ((x, y), (dx, dy)) in reversed(log):
        assert (x + dx, y + dy) in g._reachable(free(index), stones, players[index], dirs)
        assert (x, y) in stones and (x - dx, y - dy) in free(index) and (x - dx, y - dy) not in stones
        stones = stones - {(x, y)} | {(x - dx, y - dy)}
        players[index] = (x, y)
        assert before in g._reachable(free(index), stones, players[index], dirs)
        players[index] = before
    assert stones == goals and players == starts


@pytest.mark.parametrize("seed", range(4))
def test_multi_player_tasks_are_solvable_and_players_can_end_on_goals(seed):
    for grid, args in (("square", (8, 7, 14, 2)), ("hex", (11, 8, 14, 2))):
        assert _solvable(make_problem(*args, seed=seed, grid=grid, num_players=2))
    on_goal = sum(
        len(re.findall(r"\+", make_problem(13, 9, 30, 5, seed=s, grid="hex", num_players=4).split("(define")[0]))
        for s in range(20)
    )
    assert on_goal > 0  # scrambling players may be left on goal cells, like the references


def test_most_scrambles_use_several_players():
    import random

    from pypddl_datasets.generators.classical.ipc.sokoban import generator as g

    used = []
    for seed in range(20):
        rng = random.Random(seed)
        floor = g._floor(rng, 13, 11, 34, g.DIRECTIONS)
        cells = sorted(floor)
        goals = set(rng.sample(cells, 4))
        log = []
        g._scramble_players(rng, floor, goals, rng.sample([c for c in cells if c not in goals], 3), 80, g.DIRECTIONS, log)
        used.append(len({index for index, _, _ in log}))
    assert sum(n >= 2 for n in used) >= 15
