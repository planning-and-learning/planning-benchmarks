% Only the Rovers graph layer is replaced in this experiment.
% All variants span every waypoint, preserving the assumptions of the remaining
% production goal rules. This is not a replacement for the entire IPC generator.
backbone(T) :- waypoints(Ws),growing_tree(visibility,Ws,T).
visibility_parts(T,V,Extra) :- graph_variant(ipc2023),num_waypoints(N),backbone(T),
    Low is N-1,High is N*(N-1)//2,graph_integer(edge_count,Low,High,Count),
    tree_plus_edges(visibility,N,T,Count,V,Extra).
visibility_parts(T,V,Extra) :- graph_variant(sparse),num_waypoints(N),backbone(T),
    Attempts is 4*N,sparse_tree_edges(visibility,N,T,Attempts,V,Extra).
visibility(V) :- visibility_parts(_,V,_).
movement(R,G) :- rover_index(R),visibility_parts(T,_,Extra),
    backbone_subgraph(movement(R),T,Extra,3/10,G).
movement_graphs([],[]).
movement_graphs([R|Rs],[r(R,G)|Gs]) :- movement(R,G),movement_graphs(Rs,Gs).
graphs(V,Gs) :- visibility(V),rovers(Rs),movement_graphs(Rs,Gs).
adjacent(Es,A,B) :- ground_member(e(A,B),Es).
adjacent(Es,A,B) :- ground_member(e(B,A),Es).
