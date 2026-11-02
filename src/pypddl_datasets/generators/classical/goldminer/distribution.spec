language 1;
distribution goldminer;
revision "2";
metadata {
    probability "Uniform robot/supply rows without replacement and uniform gold row; independent fair rock types followed by the family soft-path walk.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(num_rows,num_cols)=(2,3), including sealed-gold counterexample"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_rows: int;
param num_cols: int;

require valid_counts: num_rows >= 2 and num_cols >= 3;
let Rows = range(num_rows);
let Cols = range(num_cols);
let RockCols = range(1, num_cols);
let Cell[r in Rows, c in Cols] = "f" + str(r) + "-" + str(c) + "f";
let Cells = values(Cell);
objects Cells: loc;
relation initial.connected[x in Rows, y in Cols, u in range(max(0,x-1),min(num_rows,x+2)), v in range(max(0,y-1),min(num_cols,y+2)) where abs(x-u) + abs(y-v) == 1](Cell[x,y],Cell[u,v]);
relation initial.arm_empty() as "arm-empty";
relation initial.robot_at(Cells) as "robot-at";
relation initial.bomb_at(Cells) as "bomb-at";
relation initial.laser_at(Cells) as "laser-at";
relation initial.gold_at(Cells) as "gold-at";
relation initial.clear(Cells);
relation initial.soft_rock_at(Cells) as "soft-rock-at";
relation initial.hard_rock_at(Cells) as "hard-rock-at";
relation goal.holds_gold() as "holds-gold";
aux possible[r in Rows, c in RockCols]: bool;
initial {
 rule geometry: forall x in Rows, y in Cols, u in range(max(0,x-1),min(num_rows,x+2)), v in range(max(0,y-1),min(num_cols,y+2)) where abs(x-u) + abs(y-v) == 1: initial.connected(Cell[x,y],Cell[u,v]);
 rule empty_arm: initial.arm_empty();
 rule robot_position: count(p in Cells: initial.robot_at(p)) == 1;
 rule bomb_position: count(p in Cells: initial.bomb_at(p)) == 1;
 rule laser_position: count(p in Cells: initial.laser_at(p)) == 1;
 rule gold_position: count(p in Cells: initial.gold_at(p)) == 1;
 rule west_resources: forall r in Rows, c in Cols where c != 0: not initial.robot_at(Cell[r,c]) and not initial.bomb_at(Cell[r,c]) and not initial.laser_at(Cell[r,c]);
 rule east_gold: forall r in Rows, c in Cols where c != num_cols - 1: not initial.gold_at(Cell[r,c]);
 rule supplies_together: forall p in Cells: initial.bomb_at(p) iff initial.laser_at(p);
 rule robot_supply_distinct: forall p in Cells: not (initial.robot_at(p) and initial.bomb_at(p));
 rule clear_west: forall r in Rows, c in Cols: initial.clear(Cell[r,c]) iff c == 0;
 rule west_without_rocks: forall r in Rows: not initial.soft_rock_at(Cell[r,0]) and not initial.hard_rock_at(Cell[r,0]);
 rule rock_partition: forall r in Rows, c in RockCols: initial.soft_rock_at(Cell[r,c]) iff not initial.hard_rock_at(Cell[r,c]);
 rule gold_soft: forall p in Cells: initial.gold_at(p) implies initial.soft_rock_at(p);
 rule west_path_base: forall r in Rows: possible[r,1] iff initial.soft_rock_at(Cell[r,1]);
 rule west_path_step: forall r in Rows, c in range(2,num_cols): possible[r,c] iff (exists turn in Rows: (forall s in range(min(r,turn),max(r,turn)+1): initial.soft_rock_at(Cell[s,c])) and (forall d in range(max(1,c-2),c): initial.soft_rock_at(Cell[turn,d])) and possible[turn,max(1,c-2)]);
 rule soft_path: forall r in Rows: initial.gold_at(Cell[r,num_cols-1]) implies possible[r,num_cols-1];
}
goal { rule hold_gold: goal.holds_gold(); }
joint {}
