language 1;
distribution floortile;
revision "2";
metadata {
    probability "Uniform distinct robot columns and independent uniform rows; uniform color allocation with fixed white/black counts; checkerboard goals.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(num_rows,num_columns,num_robots)=(1,2,2)"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_rows: int;
param num_columns: int;
param num_robots: int;

require valid_counts: num_rows >= 1 and num_columns >= 1 and num_robots >= 1 and num_robots <= num_columns;
let Rows = range(num_rows + 1);
let Cols = range(1, num_columns + 1);
let Cell[r in Rows, c in Cols] = "tile_" + str(r) + "-" + str(c);
let Cells = values(Cell);
let Robots = names("robot", num_robots, 1);
let Colors = ["white", "black"];
objects Cells: tile;
objects Robots: robot;
objects Colors: color;
relation initial.available_color(Colors) as "available-color";
relation initial.robot_at(Robots, Cells) as "robot-at";
relation initial.robot_has(Robots, Colors) as "robot-has";
relation initial.clear(Cells);
relation initial.down[r in range(num_rows), c in Cols](Cell[r,c],Cell[r+1,c]);
relation initial.up[r in range(1,num_rows+1), c in Cols](Cell[r,c],Cell[r-1,c]);
relation initial.left[r in Rows, c in range(1,num_columns)](Cell[r,c],Cell[r,c+1]);
relation initial.right[r in Rows, c in range(2,num_columns+1)](Cell[r,c],Cell[r,c-1]);
relation goal.painted(Cells, Colors);
number initial.total_cost(): int(0,0) as "total-cost";
metric minimize initial.total_cost();
initial {
 rule available_colors: forall c in Colors: initial.available_color(c);
 rule robot_position: forall r in Robots: count(c in Cells: initial.robot_at(r,c)) == 1;
 rule robot_color: forall r in Robots: count(c in Colors: initial.robot_has(r,c)) == 1;
 rule white_count: count(r in Robots: initial.robot_has(r,"white")) == (num_robots + 1) // 2;
 rule distinct_columns: forall c in Cols: count(r in Rows, b in Robots: initial.robot_at(b,Cell[r,c])) <= 1;
 rule clear_cells: forall c in Cells: initial.clear(c) iff count(r in Robots: initial.robot_at(r,c)) == 0;
 rule downward: forall r in range(num_rows), c in Cols: initial.down(Cell[r,c],Cell[r+1,c]);
 rule upward: forall r in range(1,num_rows+1), c in Cols: initial.up(Cell[r,c],Cell[r-1,c]);
 rule leftward: forall r in Rows, c in range(1,num_columns): initial.left(Cell[r,c],Cell[r,c+1]);
 rule rightward: forall r in Rows, c in range(2,num_columns+1): initial.right(Cell[r,c],Cell[r,c-1]);
}
goal {
 rule checkerboard: forall r in Rows, c in Cols, color in Colors: goal.painted(Cell[r,c],color) iff (r > 0 and color == (if (r + c) % 2 == 0 then "white" else "black"));
}
joint {}
