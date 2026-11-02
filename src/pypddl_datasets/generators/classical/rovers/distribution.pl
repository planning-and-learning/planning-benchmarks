% Rovers' revision-2 probability law. Parameters are supplied as facts.
% Draw identities include the stage, object and attempt: repeated queries reuse
% one random choice, while retries and replacement draws remain independent.
:- use_module(library(lists)).
:- use_module(library(string)).

rover_index(R) :- num_rovers(N), Last is N-1, between(0,Last,R).
waypoint_index(W) :- num_waypoints(N), Last is N-1, between(0,Last,W).
objective_index(O) :- num_objectives(N), Last is N-1, between(0,Last,O).
requested_camera(C) :- num_cameras(N), Last is N-1, between(0,Last,C).
rover_name(R,N) :- concat([rover,R],N).
waypoint_name(W,N) :- concat([waypoint,W],N).
objective_name(O,N) :- concat([objective,O],N).
camera_name(C,N) :- concat([camera,C],N).
waypoints(Ws) :- findall(W,waypoint_index(W),Ws).
rovers(Rs) :- findall(R,rover_index(R),Rs).
objectives(Os) :- findall(O,objective_index(O),Os).

% Finite local rejection, with the visibility fixed during movement retries.
% The optional graph_budget fact is only a testing/diagnostic override.
retry_budget(B) :- graph_budget(B).
retry_budget(10000) :- \+ graph_budget(_).
graph_budget(_) :- fail.
edge_candidates(Es) :- findall(e(A,B),(waypoint_index(A),waypoint_index(B),A<B),Es).
% The shared subset primitive preserves each proposal's independent edge law.
% edge_draw is the direct view of the same per-edge random decision.
edge_draw(Id,E) :- edge_probability(P),bernoulli_member(Id,P,E).
proposal(Id,Es,Gs) :- edge_probability(P),bernoulli_subset(Id,P,Es,Gs).
adjacent(Es,A,B) :- ground_member(e(A,B),Es).
adjacent(Es,A,B) :- ground_member(e(B,A),Es).
connected(Es) :- num_waypoints(N),connected_graph(N,Es).
retry(_,_,0,failed).
retry(Id,Es,B,G) :- B>0, proposal(attempt(Id,B),Es,G), connected(G).
retry(Id,Es,B,G) :- B>0, proposal(attempt(Id,B),Es,Rejected),
    \+ connected(Rejected), Next is B-1, retry(Id,Es,Next,G).
visibility(V) :- edge_candidates(Es), retry_budget(B), retry(visibility,Es,B,V).
movement(R,G) :- rover_index(R), visibility(V), V\=failed,
    retry_budget(B), retry(movement(R),V,B,G).
movement_graphs([],[]).
movement_graphs([R|_],failed) :- movement(R,failed).
movement_graphs([R|Rs],[r(R,G)|Gs]) :- movement(R,G), G\=failed,
    movement_graphs(Rs,Gs), Gs\=failed.
movement_graphs([R|Rs],failed) :- movement(R,G), G\=failed,
    movement_graphs(Rs,failed).
graphs(V,Gs) :- visibility(V), V\=failed, rovers(Rs),
    movement_graphs(Rs,Gs), Gs\=failed.
failure(graph_exhausted) :- visibility(failed).
failure(graph_exhausted) :- visibility(V), V\=failed, rovers(Rs),
    movement_graphs(Rs,failed).

% The seven equiprobable nonempty subsets, in the legacy bit-mask order.
flags(0,true,true,true). flags(1,false,true,true).
flags(2,true,false,true). flags(3,false,false,true).
flags(4,true,true,false). flags(5,false,true,false).
flags(6,true,false,false).
nonempty_flags(Id,S,R,I) :- uniform_choice(Id,[0,1,2,3,4,5,6],F,_),flags(F,S,R,I).
base_equipment(R,S,K,I) :- rover_index(R), nonempty_flags(equipment(R),S,K,I).
rover_location(R,W) :- rover_index(R),waypoints(Ws),uniform_choice(location(R),Ws,W,_).
lander_location(W) :- waypoints(Ws),uniform_choice(lander,Ws,W,_).

% Requested cameras can force imaging; repair cameras are appended in rover
% order, only for originally imaging rovers without a requested camera.
requested_owner(C,R) :- requested_camera(C),rovers(Rs),uniform_choice(owner(C),Rs,R,_).
has_requested_camera(R) :- requested_camera(C),requested_owner(C,R).
repair_owners(Rs) :- findall(R,(rover_index(R),base_equipment(R,_,_,true),
    \+ has_requested_camera(R)),Rs).
camera_owner(C,R) :- requested_owner(C,R).
camera_owner(C,R) :- repair_owners(Rs),nth0(I,Rs,R),num_cameras(N),C is N+I.
camera(C) :- camera_owner(C,_).
camera_target(C,O) :- camera(C),objectives(Os),uniform_choice(target(C),Os,O,_).
camera_flags(C,A,B,D) :- camera(C),nonempty_flags(modes(C),A,B,D).
camera_mode(C,colour) :- camera_flags(C,true,_,_).
camera_mode(C,high_res) :- camera_flags(C,_,true,_).
camera_mode(C,low_res) :- camera_flags(C,_,_,true).
camera_modes(C,Ms) :- findall(M,camera_mode(C,M),Ms).
onboard_cameras(R,Cs) :- findall(C,camera_owner(C,R),Cs).
imaging(R) :- camera_owner(_,R).

% Objective visibility is a uniform positive count of replacement draws.
positive_counts(N,Ns) :- numlist(1,N,Ns).
objective_draw_count(O,C) :- objective_index(O),num_waypoints(N),positive_counts(N,Ns),
    uniform_choice(visibility_count(O),Ns,C,_).
objective_site(O,I,W) :- objective_draw_count(O,C),between(1,C,I),waypoints(Ws),
    uniform_choice(objective_site(O,I),Ws,W,_).
objective_visible(O,W) :- objective_site(O,_,W).
visible_waypoints(O,Ws) :- objective_index(O),findall(W,objective_visible(O,W),Ws).
sample_present(Kind,W) :- ground_member(Kind,[soil,rock]),waypoint_index(W),waypoints(Ws),
    uniform_choice(sample(Kind,W),Ws,Draw,_),0 is Draw mod 2.

goal_count(Kind,C) :- ground_member(Kind,[soil,rock,image]),num_goals(N),positive_counts(N,Ns),
    uniform_choice(goal_count(Kind),Ns,D,_),C is D+N//3.
capable(soil) :- base_equipment(_,true,_,_),num_waypoints(N),N>1.
capable(rock) :- base_equipment(_,_,true,_),num_waypoints(N),N>1.
sample_sites(Kind,Ws) :- findall(W,(waypoint_index(W),capable(Kind),sample_present(Kind,W)),Ws).
% Every capable rover has a connected graph, so each eligible sample site
% occurs equally often in the legacy candidate multiset. Uniform selection
% without replacement has exactly the same projected probability law.
sample_goals(_,0,_,[]).
sample_goals(_,N,[],[]) :- N>0.
sample_goals(Kind,N,Ws,[W|Selected]) :- N>0,Ws\=[],
    uniform_choice(sample_goal(Kind,N),Ws,W,Rest),Next is N-1,
    sample_goals(Kind,Next,Rest,Selected).
selected_samples(Kind,Selected) :- goal_count(Kind,N),sample_sites(Kind,Ws),
    sample_goals(Kind,N,Ws,Selected).

% Both endpoints and directions contribute to image eligibility. Aggregate
% identical (objective,rover) entries into integer weights before drawing: the
% probability and number of attempts are exactly those of the original list.
image_candidates(Gs,Pairs) :- findall(pair(O,R),
    (ground_member(r(R,Es),Gs),imaging(R),objective_index(O),waypoint_index(W),
     objective_visible(O,W),adjacent(Es,A,B),(W=A;W=B)),Pairs).
image_weight(Gs,O,R,W) :- ground_member(r(R,Es),Gs),imaging(R),visible_waypoints(O,Visible),
    graph_incidence_count(Es,Visible,L),W is 2*L,W>0.
image_weights([],[],[]).
image_weights([weight(W,P)|Rest],[W|Ws],[P|Ps]) :- image_weights(Rest,Ws,Ps).
image_distribution(Gs,Weights,Pairs,Total) :-
    findall(weight(W,pair(O,R)),image_weight(Gs,O,R,W),Entries),
    image_weights(Entries,Weights,Pairs),sum_list(Weights,Total).
image_requests(_,_,0,[]).
image_requests(Weights,Pairs,N,[image(O,M)|Requests]) :- N>0,
    weighted_choice(image_pair(N),Weights,Pairs,pair(O,R),_),onboard_cameras(R,Cs),
    uniform_choice(image_camera(N),Cs,C,_),camera_modes(C,Ms),
    uniform_choice(image_mode(N),Ms,M,_),Next is N-1,image_requests(Weights,Pairs,Next,Requests).
selected_images(Gs,Requests) :- image_distribution(Gs,Weights,Pairs,Total),
    goal_count(image,Count),N is min(Count,Total),image_requests(Weights,Pairs,N,Requests).

object(general,lander).
object(colour,mode). object(high_res,mode). object(low_res,mode).
object(N,rover) :- rover_index(R),rover_name(R,N).
object(S,store) :- rover_index(R),rover_name(R,N),concat([N,store],S).
object(N,waypoint) :- waypoint_index(W),waypoint_name(W,N).
object(N,objective) :- objective_index(O),objective_name(O,N).
object(N,camera) :- graphs(_,_),camera(C),camera_name(C,N).

initial(visible(A,B)) :- graphs(V,_),adjacent(V,X,Y),waypoint_name(X,A),waypoint_name(Y,B).
initial(at_lander(general,N)) :- graphs(_,_),lander_location(W),waypoint_name(W,N).
initial(channel_free(general)) :- graphs(_,_).
initial(at(N,P)) :- graphs(_,_),rover_location(R,W),rover_name(R,N),waypoint_name(W,P).
initial(available(N)) :- graphs(_,_),rover_index(R),rover_name(R,N).
initial(store_of(S,N)) :- graphs(_,_),rover_index(R),rover_name(R,N),concat([N,store],S).
initial(empty(S)) :- graphs(_,_),rover_index(R),rover_name(R,N),concat([N,store],S).
initial(equipped_for_soil_analysis(N)) :- graphs(_,_),base_equipment(R,true,_,_),rover_name(R,N).
initial(equipped_for_rock_analysis(N)) :- graphs(_,_),base_equipment(R,_,true,_),rover_name(R,N).
initial(equipped_for_imaging(N)) :- graphs(_,_),imaging(R),rover_name(R,N).
initial(can_traverse(N,A,B)) :- graphs(_,Gs),ground_member(r(R,Es),Gs),adjacent(Es,X,Y),
    rover_name(R,N),waypoint_name(X,A),waypoint_name(Y,B).
initial(on_board(N,RN)) :- graphs(_,_),camera_owner(C,R),camera_name(C,N),rover_name(R,RN).
initial(calibration_target(N,ON)) :- graphs(_,_),camera_target(C,O),camera_name(C,N),objective_name(O,ON).
initial(supports(N,M)) :- graphs(_,_),camera_mode(C,M),camera_name(C,N).
initial(visible_from(ON,WN)) :- graphs(_,_),objective_visible(O,W),objective_name(O,ON),waypoint_name(W,WN).
initial(at_soil_sample(N)) :- graphs(_,_),sample_present(soil,W),waypoint_name(W,N).
initial(at_rock_sample(N)) :- graphs(_,_),sample_present(rock,W),waypoint_name(W,N).
goal(communicated_soil_data(N)) :- graphs(_,_),selected_samples(soil,Ws),ground_member(W,Ws),waypoint_name(W,N).
goal(communicated_rock_data(N)) :- graphs(_,_),selected_samples(rock,Ws),ground_member(W,Ws),waypoint_name(W,N).
goal(communicated_image_data(ON,M)) :- graphs(_,Gs),selected_images(Gs,Requests),
    ground_member(image(O,M),Requests),objective_name(O,ON).

domain(rover).
problem_name(roverprob).
