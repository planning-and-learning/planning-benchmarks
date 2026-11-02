language 1;
distribution visitall;
revision "2";
metadata {
    probability "Uniform fixed-size unavailable-cell subset; uniform available start; discrete goal inclusion with probability ceil(goal_ratio * area)/area, including start.";
    solvability "not asserted for disconnected remaining grids";
    scope "membership and structural corner cases";
    cases ["width=1; width=2 with goal probability endpoints and near endpoints"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param width: int;
param height: int? = none;
param goal_ratio: float = 1.0;
param num_unavailable: int = 0;

require positive_width: width >= 1;
let Height = if height == none then width else height;
require valid_shape: Height >= 1 and num_unavailable >= 0 and num_unavailable < width * Height;
require valid_probability: goal_ratio >= 0 and goal_ratio <= 1;
let X = range(width);
let Y = range(Height);
let Cell[x in X, y in Y] = "loc-x" + str(x) + "-y" + str(y);
let Cells = values(Cell);
objects Cells: place optional;
relation initial.at_robot(Cells) as "at-robot";
relation initial.visited(Cells);
relation initial.connected[x in X, y in Y, u in range(max(0,x-1),min(width,x+2)), v in range(max(0,y-1),min(Height,y+2)) where abs(x-u) + abs(y-v) == 1](Cell[x,y],Cell[u,v]);
relation goal.visited(Cells);
initial {
 rule available_count: count(c in Cells: present(c)) == width * Height - num_unavailable;
 rule robot_position: count(c in Cells: initial.at_robot(c)) == 1;
 rule available_start: forall c in Cells: initial.at_robot(c) implies present(c);
 rule visited_start: forall c in Cells: initial.visited(c) iff initial.at_robot(c);
 rule induced_geometry: forall x in X, y in Y, u in range(max(0,x-1),min(width,x+2)), v in range(max(0,y-1),min(Height,y+2)) where abs(x-u) + abs(y-v) == 1: initial.connected(Cell[x,y],Cell[u,v]) iff (present(Cell[x,y]) and present(Cell[u,v]));
}
goal {
 rule available_goals: forall c in Cells: goal.visited(c) implies present(c);
 rule full_threshold: forall c in Cells: if goal_ratio * (width * Height) > width * Height - 1 then goal.visited(c) iff present(c) else true;
}
joint {
 rule start_goal: forall c in Cells: initial.at_robot(c) implies goal.visited(c);
 rule zero_threshold: forall c in Cells: if goal_ratio == 0 then goal.visited(c) iff initial.at_robot(c) else true;
}
