language 1;
distribution gripper;
revision "2";
metadata {
    probability "Point mass: all balls and robot start in rooma; all balls must reach roomb.";
    solvability "guaranteed";
    scope "bounded whole-task support and weighting";
    cases ["num_balls=1,2,5: exact point masses"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_balls: int;

require counts: num_balls >= 1;
let Balls = names("ball", num_balls, 1);
let Hands = ["left", "right"];
let Rooms = ["rooma", "roomb"];
objects Balls: object;
objects Hands: object;
constants Rooms: object;
relation initial.room(Rooms);
relation initial.ball(Balls);
relation initial.gripper(Hands);
relation initial.free(Hands);
relation initial.at_robby(Rooms) as "at-robby";
relation initial.at(Balls, Rooms);
relation goal.at(Balls, Rooms);
initial {
 rule rooms: forall r in Rooms: initial.room(r);
 rule balls: forall b in Balls: initial.ball(b);
 rule hands: forall h in Hands: initial.gripper(h) and initial.free(h);
 rule robot_start: forall r in Rooms: initial.at_robby(r) iff r == "rooma";
 rule ball_starts: forall b in Balls, r in Rooms: initial.at(b,r) iff r == "rooma";
}
goal { rule all_balls: forall b in Balls, r in Rooms: goal.at(b,r) iff r == "roomb"; }
joint {}
