"""Callable adaptation of the IPC 2023 learning Sokoban generator.

Source: https://github.com/ipc2023-learning/benchmarks/blob/19d6a8ad4b354328154a2cc1f1a95f7c09fa9db6/sokoban/sokoban.py
Revision: 19d6a8ad4b354328154a2cc1f1a95f7c09fa9db6.

Sampling follows upstream, using a local random generator. The upstream BFS
queue guard is corrected so unreachable destinations fail instead of hanging.
Sampling failures are reported as ValueError; samples are never retried.
"""

from __future__ import annotations

import argparse
import random
import sys
from queue import Queue

Cell = tuple[int, int]


def get_directions() -> list[str]:
    """ 0: down; 1: left; 2: up; 3: right """
    return ["down", "left", "up", "right"]


def get_location(row: int, column: int) -> str:
    return f"loc_{row}_{column}"


def get_box(box: int) -> str:
    return f"box{box}"


def get_objects(grid_size: int, boxes: int) -> str:
    offset = "\n    "

    # -- locations
    str_objects = offset + " ".join([f"{get_location(i, j) }" for i in range(1, 1+grid_size)
                                     for j in range(1, 1+grid_size)]) + " - location"

    # -- boxes
    str_objects += offset + " ".join([f"{get_box(i)}" for i in range(1, 1+boxes)]) + " - box"

    return str_objects + offset


def get_init(grid_size: int, boxes: int, rng: random.Random) -> tuple[str, list[Cell | None], str, list[str]]:
    offset = "\n    "
    str_init = "\n"

    plan: list[str] = []
    directions = get_directions()

    # Setup grid => 0: unvisited; 1: visited; 2: goal (cannot be crossed); 3: wall (cannot be crossed)
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(grid_size):
        grid[0][i] = grid[i][0] = grid[grid_size-1][i] = grid[i][grid_size-1] = 3

    # Set the robot starting location
    all_locations = [(r, c) for r in range(1, grid_size - 1) for c in range(1, grid_size - 1) if grid[r][c] == 0]
    assert all_locations  # there must be an available starting box location
    rng.shuffle(all_locations)
    starting_robot_at = all_locations[0]
    grid[starting_robot_at[0]][starting_robot_at[1]] = 1  # mark it as visited

    # Serialize box ids, and initialize the init and goal locations
    serialize_box_ids = list(range(1, 1+boxes))  # for inits and goals
    rng.shuffle(serialize_box_ids)
    init_locations: dict[Cell, int] = {}  # initial location -> box id
    goal_box_loc: list[Cell | None] = [None for _ in range(1+boxes)]


    def is_valid_agent_move(ax: int, ay: int) -> bool:
        return (0 < ax < grid_size-1) and (0 < ay < grid_size-1) and (grid[ax][ay] < 2)

    def is_valid_box_move(bx: int, by: int) -> bool:
        return (1 < bx < grid_size-2) and (1 < by < grid_size-2) and (grid[bx][by] < 2)

    def get_move_dir(from_loc: Cell, to_loc: Cell) -> int:
        assert (from_loc[0] == to_loc[0]) or (from_loc[1] == to_loc[1])
        if from_loc[0] < to_loc[0]:
            return 0  # down move
        if from_loc[0] > to_loc[0]:
            return 2  # up move
        if from_loc[1] < to_loc[1]:
            return 3  # right move
        return 1  # left move

    def grid_to_string() -> str:
        grid_str = ""
        car = ".+G#"
        for i in range(grid_size):
            row = ""
            for j in range(grid_size):
                if (i,j) in init_locations:
                    row += " " + str(init_locations[(i, j)])
                elif (i,j) == starting_robot_at:
                    row += " R"
                else:
                    row += "  "
                row += car[grid[i][j]]
            grid_str += row + "\n"
        return grid_str

    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]  # 0: down, 1: left, 2: up, 3: right
    def get_path(from_loc: Cell, to_loc: Cell) -> list[Cell] | None:
        if from_loc == to_loc:
            return []

        visited_from: list[list[Cell | None]] = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        queue: Queue[Cell] = Queue()
        queue.put(from_loc)
        visited_from[from_loc[0]][from_loc[1]] = from_loc

        # Queue objects stay truthy when empty; avoid blocking on unreachable targets.
        while not queue.empty() and (visited_from[to_loc[0]][to_loc[1]] is None):
            loc = queue.get()
            for m in range(4):
                n_loc_x, n_loc_y = loc[0] + dx[m], loc[1] + dy[m]
                if is_valid_agent_move(n_loc_x, n_loc_y) and (visited_from[n_loc_x][n_loc_y] is None):
                    visited_from[n_loc_x][n_loc_y] = loc
                    queue.put((n_loc_x, n_loc_y))

        if visited_from[to_loc[0]][to_loc[1]] is None:
            return None

        path: list[Cell] = []
        loc = to_loc
        while (previous := visited_from[loc[0]][loc[1]]) != loc:
            assert previous is not None
            path.append(loc)
            loc = previous
        path = list(reversed(path))
        return path


    # Update box paths
    robot_at: Cell = starting_robot_at
    for box in range(boxes):
        # list of all available locations (not consider borders or close to them)
        all_locations = [(r, c) for r in range(2, grid_size-2) for c in range(2, grid_size-2) if grid[r][c] == 0]
        assert all_locations  # there must be an available starting box location
        rng.shuffle(all_locations)
        box_at: Cell = all_locations[0]
        x, y = box_at
        box_id = serialize_box_ids[box]
        init_locations[box_at] = box_id  # location -> box id
        grid[x][y] = 4
        starting_box_at = (x, y)

        # print(f"Box #{box_id} starts at {box_at}")

        choices: list[tuple[int, int, int]] = []
        for m in range(4):
            # check if the opposite direction of the box is valid for the agent
            if is_valid_agent_move(x-dx[m], y-dy[m]):
                choices.append((m, x-dx[m], y-dy[m]))

        assert choices

        direction, to_x, to_y = rng.choice(choices)

        robot_to = (to_x, to_y)
        path = get_path(robot_at, robot_to)
        # print(f"Agent moves from {robot_at} to {robot_to} => {path}")
        assert path is not None
        for loc in path:
            move_dir = get_move_dir(robot_at, loc)
            plan.append('(' + ' '.join(
                ["move",
                 get_location(robot_at[0]+1, robot_at[1]+1),
                 get_location(loc[0]+1, loc[1]+1),
                 directions[move_dir]]) + ')')
            grid[loc[0]][loc[1]] = 1
            robot_at = loc

        # Move box randomly up to max_moves times or until reaching a stop condition (crossing a goal...)
        max_moves = 3
        for box_move in range(max_moves):
            next_x, next_y = box_at[0] + dx[direction], box_at[1] + dy[direction]

            valid_moves: list[Cell] = []
            while is_valid_box_move(next_x, next_y):
                valid_moves.append((next_x, next_y))
                next_x += dx[direction]
                next_y += dy[direction]

            if valid_moves:
                idx = rng.randint(0,  len(valid_moves)-1)
                for i in range(idx+1):
                    plan.append('(' + ' '.join(
                        ["push",
                         get_location(robot_at[0]+1, robot_at[1]+1),
                         get_location(box_at[0]+1, box_at[1]+1),
                         get_location(valid_moves[i][0]+1, valid_moves[i][1]+1),
                         directions[direction],
                         get_box(box_id)
                         ]) +')')
                    robot_at = box_at
                    box_at = valid_moves[i]
                    grid[box_at[0]][box_at[1]] = 1  # mark cell as visited

            if box_move + 1 < max_moves:
                # If it wasn't the last move, change direction 90º, and move the agent around the box
                turns: list[tuple[int, Cell, Cell]] = []
                x, y = robot_at
                if direction == 0:  # down
                    if is_valid_agent_move(x, y+1) and is_valid_agent_move(x+1, y+1):  # left is OK
                        turns.append((1, (x, y+1), (x+1, y+1)))
                    if is_valid_agent_move(x, y-1) and is_valid_agent_move(x+1, y-1):  # right is OK
                        turns.append((3, (x, y-1), (x+1, y-1)))
                elif direction == 1:  # left
                    if is_valid_agent_move(x-1, y) and is_valid_agent_move(x-1, y-1):  # down is OK
                        turns.append((0, (x-1, y), (x-1, y-1)))
                    if is_valid_agent_move(x+1, y) and is_valid_agent_move(x+1, y-1):  # up is OK
                        turns.append((2, (x+1, y), (x+1, y-1)))
                elif direction == 2:  # up
                    if is_valid_agent_move(x, y+1) and is_valid_agent_move(x-1, y+1):  # left is OK
                        turns.append((1, (x, y+1), (x-1, y+1)))
                    if is_valid_agent_move(x, y-1) and is_valid_agent_move(x-1, y-1):  # right is OK
                        turns.append((3, (x, y-1), (x-1, y-1)))
                elif direction == 3:  # right
                    if is_valid_agent_move(x-1, y) and is_valid_agent_move(x-1, y+1):  # down is OK
                        turns.append((0, (x-1, y), (x-1, y+1)))
                    if is_valid_agent_move(x+1, y) and is_valid_agent_move(x+1, y+1):  # up is OK
                        turns.append((2, (x+1, y), (x+1, y+1)))

                # assert choices
                # prev_dir = direction
                if turns:
                    direction, loc1, loc2 = rng.choice(turns)
                    # print(f"Loc1={loc1}; Loc2={loc2}")
                    move_dir = get_move_dir(robot_at, loc1)
                    plan.append('(' + ' '.join(["move", get_location(robot_at[0] + 1, robot_at[1] + 1),
                                                get_location(loc1[0] + 1, loc1[1] + 1), directions[move_dir]]) + ')')
                    grid[loc1[0]][loc1[1]] = 1
                    robot_at = loc1
                    move_dir = get_move_dir(robot_at, loc2)
                    plan.append('(' + ' '.join(["move", get_location(robot_at[0] + 1, robot_at[1] + 1),
                                                get_location(loc2[0] + 1, loc2[1] + 1), directions[move_dir]]) + ')')
                    grid[loc2[0]][loc2[1]] = 1
                    robot_at = loc2
                else:
                    break

                # print(f"Turning robot to {robot_at} (from {prev_dir} to {direction})")
                # print(f"Grid=\n{grid_to_string()}")

        grid[starting_box_at[0]][starting_box_at[1]] = 1
        grid[box_at[0]][box_at[1]] = 2
        goal_box_loc[box_id] = box_at

    #print(grid)
    all_locations = [(r, c) for r in range(1, grid_size-1) for c in range(1, grid_size-1) if grid[r][c] == 0]
    assert all_locations
    rng.shuffle(all_locations)
    num_walls = max(1, rng.randint(int(0.3*len(all_locations)), int(0.8*len(all_locations))))
    for w in all_locations[0:num_walls]:
        grid[w[0]][w[1]] = 3

    walls = {(r, c) for r in range(grid_size) for c in range(grid_size) if grid[r][c] == 3}

    #print_grid()

    # Starting robot location
    str_init += offset + f"(at-robot {get_location(starting_robot_at[0]+1, starting_robot_at[1]+1)})"


    # Starting boxes locations
    str_init += offset + offset.join([f"(at {get_box(box_id)} {get_location(loc[0]+1, loc[1]+1)})"
                                      for loc, box_id in init_locations.items()])

    # Clear locs are all non-occupied starting locs
    occupied_locs = set(walls)
    for loc in init_locations:
        occupied_locs.add(loc)
    all_locations = [(r, c) for r in range(1, grid_size - 1) for c in range(1, grid_size - 1)]
    clear_locs = set(all_locations).difference(occupied_locs)
    str_init += offset + offset.join([f"(clear {get_location(loc[0]+1, loc[1]+1)})" for loc in clear_locs])

    # Build the grid adjacency between all non-wall locations
    for row in range(1, grid_size):
        for col in range(1, grid_size):
            if (row, col) in walls:
                continue
            from_loc = get_location(row+1, col+1)
            if (row+1 < grid_size) and (row+1, col) not in walls:  # 0: down
                str_init += offset + f"(adjacent {from_loc} {get_location(row+2, col+1)} {directions[0]})"
            if (col > 1) and (row, col-1) not in walls:  # 1: left
                str_init += offset + f"(adjacent {from_loc} {get_location(row+1, col)} {directions[1]})"
            if (row > 1) and (row-1, col) not in walls:  # 2: up
                str_init += offset + f"(adjacent {from_loc} {get_location(row, col+1)} {directions[2]})"
            if (col+1 < grid_size) and (row, col+1) not in walls:  # 3: right
                str_init += offset + f"(adjacent {from_loc} {get_location(row+1, col+2)} {directions[3]})"

    return str_init, goal_box_loc, grid_to_string(), plan


def get_goal(goal_box_loc: list[Cell | None]) -> str:
    offset = "\n    "
    str_goal = " (and "
    for idx in range(1, len(goal_box_loc)):  # skip box id 0 which is always None
        location = goal_box_loc[idx]
        assert location is not None
        str_goal += offset + f"(at {get_box(idx)} {get_location(location[0]+1, location[1]+1)})"
    return str_goal + ")"


def make_problem(grid_size: int, boxes: int, seed: int = 42) -> str:
    """Return a seeded problem, or raise ValueError if upstream sampling fails.

    Boxes need the inner (grid_size - 4) square. Paths reserve additional
    cells, so even parameters inside these bounds may fail for some seeds.
    """
    # Preserve the original exact-int contract: bool and int subclasses are rejected.
    if any(type(value) is not int for value in (grid_size, boxes, seed)):  # pylint: disable=unidiomatic-typecheck
        raise ValueError("grid_size, boxes, and seed must be integers")
    if grid_size < 5:
        raise ValueError("grid_size must be at least 5")
    if not 1 <= boxes <= (grid_size - 4) ** 2:
        raise ValueError("boxes must be between 1 and (grid_size - 4) ** 2")

    try:
        str_init, goal_box_loc, str_grid, _ = get_init(grid_size, boxes, random.Random(seed))
    except AssertionError as error:
        raise ValueError(
            f"upstream Sokoban sampling failed for grid_size={grid_size}, boxes={boxes}, seed={seed}"
        ) from error
    str_objects = get_objects(grid_size, boxes)
    str_goal = get_goal(goal_box_loc)
    str_grid = ';; '.join([s + '\n' for s in str_grid.split('\n')])
    return (
        f";; grid_size={grid_size}, boxes={boxes}, seed={seed}\n;;\n"
        f";; {str_grid}\n"
        f"(define (problem sokoban-generated)\n"
        f" (:domain sokoban)\n"
        f" (:objects {str_objects})\n"
        f" (:init {str_init})\n"
        f" (:goal {str_goal}))\n"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-g", "--grid-size", type=int, required=True)
    parser.add_argument("-b", "--boxes", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int, default=42)
    args = parser.parse_args(argv)
    sys.stdout.write(make_problem(args.grid_size, args.boxes, args.seed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
