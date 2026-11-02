language 1;
distribution rovers;
revision "2";
metadata {
    probability "Ideal hierarchy: independent Bernoulli visibility edges conditioned on connectivity, then for each rover independent Bernoulli visible edges conditioned on connectivity. Initial equipment is uniform over the seven nonempty subsets; cameras subsequently force imaging capability. Requested cameras choose uniform owners and calibration objectives; imaging rovers with no camera receive one. Camera modes are uniform nonempty subsets. Each objective chooses a uniform count from 1..num_waypoints then that many uniform waypoints with replacement. Soil/rock flags have probability ceil(num_waypoints/2)/num_waypoints. Three independent uniform counts from 1..num_goals plus num_goals//3 control goals. Sample goals choose unique eligible sites. Image draws weight objective/rover pairs by visible traversal incidences, then choose a uniform onboard camera and supported mode, merging duplicate requests. Finite rejection budgets include failure outcomes; conditioning on successful completion can reweight earlier graph choices.";
    solvability "per-instance reachability constraints";
    scope "bounded whole-task support for the declared tiny case; sampled membership elsewhere";
    cases ["(num_rovers,num_waypoints,num_objectives,num_cameras,num_goals)=(1,1,1,0,1): all 31 tasks; (2,3,2,1,2): membership"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_rovers: int;
param num_waypoints: int;
param num_objectives: int;
param num_cameras: int;
param num_goals: int;
param edge_probability: float = 0.5;

require positive_counts: num_rovers >= 1 and num_waypoints >= 1 and num_objectives >= 1 and num_goals >= 1;
require camera_count: num_cameras >= 0;
require graph_probability: edge_probability >= 0 and edge_probability <= 1 and (num_waypoints == 1 or edge_probability > 0);

let RoverIndices = range(num_rovers);
let WaypointIndices = range(num_waypoints);
let CameraIndices = range(num_cameras + num_rovers);
let RequestedCameraIndices = range(num_cameras);
let ExtraCameraIndices = range(num_cameras, num_cameras + num_rovers);
let Rovers = names("rover", num_rovers);
let Waypoints = names("waypoint", num_waypoints);
let Objectives = names("objective", num_objectives);
let Cameras = names("camera", num_cameras + num_rovers);
let Stores[r in RoverIndices] = Rovers[r] + "store";
let Modes = ["colour", "high_res", "low_res"];
let Landers = ["general"];
let MinimumGoalDraws = 1 + num_goals // 3;
let MaximumGoalDraws = num_goals + num_goals // 3;

objects Rovers: rover;
objects Waypoints: waypoint;
objects Objectives: objective;
objects Cameras: camera optional;
objects values(Stores): store;
objects Modes: mode;
objects Landers: lander;

relation initial.visible(Waypoints, Waypoints);
relation initial.can_traverse(Rovers, Waypoints, Waypoints);
relation initial.at(Rovers, Waypoints);
relation initial.available(Rovers);
relation initial.store_of(values(Stores), Rovers);
relation initial.empty(values(Stores));
relation initial.equipped_for_soil_analysis(Rovers);
relation initial.equipped_for_rock_analysis(Rovers);
relation initial.equipped_for_imaging(Rovers);
relation initial.at_lander(Landers, Waypoints);
relation initial.channel_free(Landers);
relation initial.on_board(Cameras, Rovers);
relation initial.calibration_target(Cameras, Objectives);
relation initial.supports(Cameras, Modes);
relation initial.visible_from(Objectives, Waypoints);
relation initial.at_soil_sample(Waypoints);
relation initial.at_rock_sample(Waypoints);
relation goal.communicated_soil_data(Waypoints);
relation goal.communicated_rock_data(Waypoints);
relation goal.communicated_image_data(Objectives, Modes);

# Ranks witness connectivity; they are never part of a semantic task identity.
aux visibility_rank[w in WaypointIndices]: int(0, num_waypoints - 1);
aux traversal_rank[r in RoverIndices, w in WaypointIndices]: int(0, num_waypoints - 1);
aux soil_capable: bool;
aux rock_capable: bool;
aux eligible_soil_count: int(0, num_waypoints);
aux eligible_rock_count: int(0, num_waypoints);
aux soil_goal_count: int(0, num_waypoints);
aux rock_goal_count: int(0, num_waypoints);
aux image_goal_count: int(0, num_objectives * len(Modes));
aux suitable_image_draws: int(0, 2 * num_rovers * num_objectives * num_waypoints * (num_waypoints - 1));

initial {
    rule visibility_simple: forall w in Waypoints: not initial.visible(w, w);
    rule visibility_symmetric: forall a in Waypoints, b in Waypoints: initial.visible(a, b) iff initial.visible(b, a);
    rule visibility_probability_one: forall a in Waypoints, b in Waypoints where edge_probability == 1 and a != b: initial.visible(a, b);
    rule visibility_root: visibility_rank[0] == 0;
    rule visibility_connected: forall w in WaypointIndices where w > 0:
        exists v in WaypointIndices where v != w: initial.visible(Waypoints[w], Waypoints[v]) and visibility_rank[v] < visibility_rank[w];

    rule traversal_simple: forall r in Rovers, w in Waypoints: not initial.can_traverse(r, w, w);
    rule traversal_symmetric: forall r in Rovers, a in Waypoints, b in Waypoints:
        initial.can_traverse(r, a, b) iff initial.can_traverse(r, b, a);
    rule traversal_visible: forall r in Rovers, a in Waypoints, b in Waypoints:
        initial.can_traverse(r, a, b) implies initial.visible(a, b);
    rule traversal_probability_one: forall r in Rovers, a in Waypoints, b in Waypoints where edge_probability == 1 and a != b:
        initial.can_traverse(r, a, b);
    rule traversal_roots: forall r in RoverIndices: traversal_rank[r, 0] == 0;
    rule connected_can_traverse: forall r in RoverIndices, w in WaypointIndices where w > 0:
        exists v in WaypointIndices where v != w:
            initial.can_traverse(Rovers[r], Waypoints[w], Waypoints[v]) and traversal_rank[r, v] < traversal_rank[r, w];

    rule rover_positions: forall r in Rovers: count(w in Waypoints: initial.at(r, w)) == 1;
    rule rover_available: forall r in Rovers: initial.available(r);
    rule store_assignment: forall r in RoverIndices, s in RoverIndices:
        initial.store_of(Stores[r], Rovers[s]) iff r == s;
    rule empty_stores: forall r in RoverIndices: initial.empty(Stores[r]);
    rule nonempty_equipment: forall r in Rovers:
        initial.equipped_for_soil_analysis(r) or initial.equipped_for_rock_analysis(r) or initial.equipped_for_imaging(r);
    rule lander_position: count(w in Waypoints: initial.at_lander("general", w)) == 1;
    rule free_channel: initial.channel_free("general");

    # The initial requested cameras precede at most one repair camera per rover.
    # Repair owners follow rover order and have no requested camera already.
    rule requested_cameras_present: forall c in RequestedCameraIndices: present(Cameras[c]);
    rule optional_camera_prefix: forall c in ExtraCameraIndices where c > num_cameras:
        present(Cameras[c]) implies present(Cameras[c - 1]);
    rule unique_camera_owner: forall c in Cameras:
        count(r in Rovers: initial.on_board(c, r)) == (if present(c) then 1 else 0);
    rule unique_camera_calibration: forall c in Cameras:
        count(o in Objectives: initial.calibration_target(c, o)) == (if present(c) then 1 else 0);
    rule nonempty_camera_modes: forall c in Cameras:
        (if present(c) then count(m in Modes: initial.supports(c, m)) >= 1 else count(m in Modes: initial.supports(c, m)) == 0);
    rule repair_only_without_requested_camera: forall c in ExtraCameraIndices, r in Rovers:
        initial.on_board(Cameras[c], r) implies not (exists previous in RequestedCameraIndices: initial.on_board(Cameras[previous], r));
    rule repair_owner_order: forall c in ExtraCameraIndices, r in RoverIndices where c > num_cameras:
        initial.on_board(Cameras[c], Rovers[r]) implies (exists previous in RoverIndices where previous < r: initial.on_board(Cameras[c - 1], Rovers[previous]));
    rule imaging_iff_camera: forall r in Rovers:
        initial.equipped_for_imaging(r) iff (exists c in Cameras: initial.on_board(c, r));
    rule objectives_visible: forall o in Objectives: count(w in Waypoints: initial.visible_from(o, w)) >= 1;
    rule singleton_samples: forall w in Waypoints where num_waypoints == 1:
        initial.at_soil_sample(w) and initial.at_rock_sample(w);
}

goal {
    rule positive_goal_vocabulary: true;
}

joint {
    rule soil_capability: soil_capable iff (num_waypoints > 1 and (exists r in Rovers: initial.equipped_for_soil_analysis(r)));
    rule rock_capability: rock_capable iff (num_waypoints > 1 and (exists r in Rovers: initial.equipped_for_rock_analysis(r)));
    rule soil_eligible_count: eligible_soil_count == count(w in Waypoints: soil_capable and initial.at_soil_sample(w));
    rule rock_eligible_count: eligible_rock_count == count(w in Waypoints: rock_capable and initial.at_rock_sample(w));
    rule soil_requested_count: soil_goal_count == count(w in Waypoints: goal.communicated_soil_data(w));
    rule rock_requested_count: rock_goal_count == count(w in Waypoints: goal.communicated_rock_data(w));
    rule soil_goal_eligibility: forall w in Waypoints:
        goal.communicated_soil_data(w) implies (soil_capable and initial.at_soil_sample(w));
    rule rock_goal_eligibility: forall w in Waypoints:
        goal.communicated_rock_data(w) implies (rock_capable and initial.at_rock_sample(w));
    rule soil_goal_minimum: soil_goal_count >= (if eligible_soil_count < MinimumGoalDraws then eligible_soil_count else MinimumGoalDraws);
    rule soil_goal_maximum: soil_goal_count <= (if eligible_soil_count < MaximumGoalDraws then eligible_soil_count else MaximumGoalDraws);
    rule rock_goal_minimum: rock_goal_count >= (if eligible_rock_count < MinimumGoalDraws then eligible_rock_count else MinimumGoalDraws);
    rule rock_goal_maximum: rock_goal_count <= (if eligible_rock_count < MaximumGoalDraws then eligible_rock_count else MaximumGoalDraws);

    # Every rover can reach every waypoint. Image support therefore needs a
    # supported mode on some camera, plus at least one traversal incidence.
    rule image_supported: forall o in Objectives, m in Modes:
        goal.communicated_image_data(o, m) implies (num_waypoints > 1 and (exists c in Cameras: initial.supports(c, m)));
    rule image_requested_count: image_goal_count == count(o in Objectives, m in Modes: goal.communicated_image_data(o, m));
    rule image_candidate_multiplicity:
        suitable_image_draws == sum(r in Rovers, o in Objectives, a in Waypoints, b in Waypoints where a != b:
            if initial.equipped_for_imaging(r) and initial.visible_from(o, a) and initial.can_traverse(r, a, b) then 2 else 0);
    rule image_goal_nonempty: image_goal_count >= (if suitable_image_draws > 0 then 1 else 0);
    rule image_goal_draw_bound: image_goal_count <= suitable_image_draws and image_goal_count <= MaximumGoalDraws;
}
