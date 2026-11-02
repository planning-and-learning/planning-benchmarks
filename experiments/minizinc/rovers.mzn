% Experimental support model: connected Rovers graphs and optional soil goals.
% Search strategies select valid tasks; they do not preserve generator probabilities.
include "connected.mzn";

int: n;
int: nr;
int: num_goals;
bool: graph_only;
int: search_mode;
constraint assert(n >= 2 /\ nr >= 1, "Require n >= 2 and nr >= 1");
constraint assert(search_mode in 0..1, "search_mode must be 0 or 1");
constraint assert(graph_only \/ (num_goals >= 0 /\ num_goals <= n),
                  "num_goals must be between 0 and n");

set of int: W = 1..n;
set of int: R = 1..nr;
set of int: E = 1..(n * (n - 1) div 2);
array[E] of int: src = [a | a, b in W where a < b];
array[E] of int: dst = [b | a, b in W where a < b];
array[E] of var bool: visible;
array[R, E] of var bool: move;
array[R] of var W: rover_at;
var W: lander_at;

constraint connected(src, dst, [true | w in W], visible);
constraint forall(r in R)(
    connected(src, dst, [true | w in W], [move[r, e] | e in E])
);
constraint forall(r in R, e in E)(move[r, e] -> visible[e]);

array[W] of var bool: soil_sample;
array[W] of var bool: soil_goal;
array[R] of var bool: soil_capable;
constraint if graph_only then
    forall(w in W)(not soil_sample[w] /\ not soil_goal[w]) /\
    forall(r in R)(not soil_capable[r])
else
    exists(r in R)(soil_capable[r]) /\
    sum(w in W)(bool2int(soil_goal[w])) = num_goals /\
    forall(w in W)(soil_goal[w] -> soil_sample[w])
endif;

% Connected movement makes every selected sample reachable by a capable rover.
% With n >= 2, connected visibility gives the lander a communication neighbor.
% PDDL emission additionally initializes owned empty stores and availability.
array[int] of var bool: flags = visible ++ [move[r, e] | r in R, e in E]
    ++ soil_sample ++ soil_goal ++ soil_capable;
% Mode 1 chooses random Boolean polarities while compiling the model. The CLI
% --random-seed controls these draws. Integer locations stay deterministic.
% This is randomized search, not uniform or distribution-preserving sampling.
% Boolean domains have equal size; input_order avoids unnecessary size ranking.
array[int] of var bool: search_flags = [
    if search_mode = 1 /\ uniform(0, 1) = 1 then not flags[i] else flags[i] endif
    | i in index_set(flags)
];
solve :: seq_search([
    bool_search(search_flags, input_order, indomain_min, complete),
    int_search(rover_at ++ [lander_at], input_order, indomain_min, complete)
]) satisfy;

% Movement flags are flattened in rover-major order. Every selected edge is
% undirected: a PDDL writer emits both orientations for visible and can_traverse.
output [
    "{\"n\":", show(n), ",\"nr\":", show(nr),
    ",\"graph_only\":", show(graph_only),
    ",\"src\":", show(src), ",\"dst\":", show(dst),
    ",\"visible\":", show(visible),
    ",\"move\":", show([move[r, e] | r in R, e in E]),
    ",\"rover_at\":", show(rover_at), ",\"lander_at\":", show(lander_at),
    ",\"soil_sample\":", show(soil_sample),
    ",\"soil_goal\":", show(soil_goal),
    ",\"soil_capable\":", show(soil_capable), "}\n"
];
