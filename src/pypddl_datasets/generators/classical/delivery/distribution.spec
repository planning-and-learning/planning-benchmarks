language 1;
distribution delivery;
revision "2";
metadata {
    probability "Independent uniform initial positions; uniform common destination conditioned on the task not initially being solved.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(grid_size,num_packages)=(2,1)"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param grid_size: int;
param num_packages: int;

require counts: grid_size >= 2 and num_packages >= 1;
let Axis = range(grid_size);
let Cell[x in Axis, y in Axis] = "c_" + str(x) + "_" + str(y);
let Cells = values(Cell);
let Packages = names("p", num_packages, 1);
let Trucks = ["t1"];
let Moving = Trucks + Packages;
objects Cells: cell;
objects Packages: package;
objects Trucks: truck;
relation initial.adjacent[x in Axis, y in Axis, u in range(max(0,x-1),min(grid_size,x+2)), v in range(max(0,y-1),min(grid_size,y+2)) where abs(x-u) + abs(y-v) == 1](Cell[x,y],Cell[u,v]);
relation initial.empty(Trucks);
relation initial.at(Moving, Cells);
relation goal.at(Packages, Cells);
initial {
 rule adjacency: forall x in Axis, y in Axis, u in range(max(0,x-1),min(grid_size,x+2)), v in range(max(0,y-1),min(grid_size,y+2)) where abs(x-u) + abs(y-v) == 1: initial.adjacent(Cell[x,y],Cell[u,v]);
 rule empty_truck: initial.empty("t1");
 rule locations: forall item in Moving: count(c in Cells: initial.at(item,c)) == 1;
}
goal {
 rule destinations: forall p in Packages: count(c in Cells: goal.at(p,c)) == 1;
 rule common_destination: forall p in Packages, c in Cells: goal.at(p,c) iff goal.at(Packages[0],c);
}
joint {
 rule some_package_moves: exists p in Packages, c in Cells: initial.at(p,c) and not goal.at(p,c);
}
