language 1;
distribution grid;
revision "2";
metadata {
    probability "Uniform locked positions and open robot position; uniform surjective shape assignments; reachable-key construction; Bernoulli goals with singleton repair and uniform different destinations.";
    solvability "guaranteed";
    scope "bounded whole-task support for the declared tiny case; sampled membership elsewhere";
    cases ["(width,height,num_shapes,num_keys,num_locks)=(2,2,1,1,1): all 108 tasks; (3,2,2,3,2): membership"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param width: int;
param height: int;
param num_shapes: int = 2;
param num_keys: int = 2;
param num_locks: int = 2;
param goal_probability: float = 1.0;

require valid_counts: width >= 2 and height >= 2 and num_shapes >= 1 and num_keys >= num_shapes and num_locks >= num_shapes and num_locks < width * height;
require valid_probability: goal_probability > 0 and goal_probability <= 1;
let X = range(width);
let Y = range(height);
let Cell[x in X, y in Y] = "pos" + str(x) + "-" + str(y);
let Cells = values(Cell);
let Keys = names("key", num_keys);
let Shapes = names("shape", num_shapes);
objects Cells + Keys + Shapes: object;
relation initial.arm_empty() as "arm-empty";
relation initial.conn[x in X, y in Y, u in range(max(0,x-1),min(width,x+2)), v in range(max(0,y-1),min(height,y+2)) where abs(x-u) + abs(y-v) == 1](Cell[x,y],Cell[u,v]);
relation initial.place(Cells);
relation initial.key(Keys);
relation initial.shape(Shapes);
relation initial.open(Cells);
relation initial.locked(Cells);
relation initial.at_robot(Cells) as "at-robot";
relation initial.at(Keys, Cells);
relation initial.key_shape(Keys, Shapes) as "key-shape";
relation initial.lock_shape(Cells, Shapes) as "lock-shape";
relation goal.at(Keys, Cells);
aux rank[c in Cells]: int(0, width * height - 1);
initial {
 rule empty_arm: initial.arm_empty();
 rule geometry: forall x in X, y in Y, u in range(max(0,x-1),min(width,x+2)), v in range(max(0,y-1),min(height,y+2)) where abs(x-u) + abs(y-v) == 1: initial.conn(Cell[x,y],Cell[u,v]);
 rule places: forall c in Cells: initial.place(c);
 rule keys: forall k in Keys: initial.key(k);
 rule shapes: forall s in Shapes: initial.shape(s);
 rule open_partition: forall c in Cells: initial.open(c) iff not initial.locked(c);
 rule lock_count: count(c in Cells: initial.locked(c)) == num_locks;
 rule lock_shape: forall c in Cells: count(s in Shapes: initial.lock_shape(c,s)) == (if initial.locked(c) then 1 else 0);
 rule key_shape: forall k in Keys: count(s in Shapes: initial.key_shape(k,s)) == 1;
 rule key_locations: forall k in Keys: count(c in Cells: initial.at(k,c)) == 1;
 rule key_coverage: forall s in Shapes: exists k in Keys: initial.key_shape(k,s);
 rule lock_coverage: forall s in Shapes: exists c in Cells: initial.lock_shape(c,s);
 rule robot_position: count(c in Cells: initial.at_robot(c)) == 1;
 rule robot_open: forall c in Cells: initial.at_robot(c) implies initial.open(c);
 rule rank_origin: forall c in Cells: initial.at_robot(c) iff rank[c] == 0;
 rule reachable_predecessor: forall x in X, y in Y: rank[Cell[x,y]] > 0 implies (exists u in range(max(0,x-1),min(width,x+2)), v in range(max(0,y-1),min(height,y+2)) where abs(x-u) + abs(y-v) == 1: rank[Cell[u,v]] < rank[Cell[x,y]]);
 rule unlockable: forall c in Cells: rank[c] > 0 implies (initial.open(c) or (exists k in Keys, s in Shapes, p in Cells: initial.lock_shape(c,s) and initial.key_shape(k,s) and initial.at(k,p) and rank[p] < rank[c]));
}
goal {
 rule partial_destinations: forall k in Keys: count(c in Cells: goal.at(k,c)) <= 1;
 rule full_probability: forall k in Keys: if goal_probability == 1 then count(c in Cells: goal.at(k,c)) == 1 else true;
 rule singleton_repair: count(k in Keys, c in Cells: goal.at(k,c)) >= 1;
}
joint { rule changed_destinations: forall k in Keys, c in Cells: goal.at(k,c) implies not initial.at(k,c); }
