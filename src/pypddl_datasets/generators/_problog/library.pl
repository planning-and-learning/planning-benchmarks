% Generic finite choices. Keep ratios as probability expressions: computing
% Weight is 1/N first would introduce binary64 bias into discrete uniform draws.
:- use_module(library(lists)).

% Enumerate a ground list with ordinary member unification and answer order.
% Sampling can walk it natively without grounding one recursive table per suffix.
ground_member(X,Xs) :- member(X,Xs).

(1/N)::uniform_head(Id,N,X,Xs).
uniform_choice(_, [X], X, []).
uniform_choice(Id,[X|Xs],X,Xs) :- Xs \= [], length([X|Xs],N), uniform_head(Id,N,X,Xs).
uniform_choice(Id,[X|Xs],V,[X|Rest]) :- Xs \= [], length([X|Xs],N),
    \+ uniform_head(Id,N,X,Xs), uniform_choice(Id,Xs,V,Rest).
uniform_int(Id,Low,High,V) :- numlist(Low,High,Values), uniform_choice(Id,Values,V,_).

(W/Total)::weighted_head(Id,W,Total,X,Xs).
weighted_choice(Id,Weights,Values,V,Rest) :- sum_list(Weights,Total), Total > 0,
    weighted_choice_remaining(Id,Total,Weights,Values,V,Rest).
weighted_choice_remaining(_,_,[W],[X],X,[]) :- W > 0.
weighted_choice_remaining(Id,Total,[W|Ws],[X|Xs],X,Xs) :- Xs \= [], Total > 0,
    weighted_head(Id,W,Total,X,Xs).
weighted_choice_remaining(Id,Total,[W|Ws],[X|Xs],V,[X|Rest]) :- Xs \= [], Total > 0,
    \+ weighted_head(Id,W,Total,X,Xs), Remaining is Total-W,
    weighted_choice_remaining(Id,Remaining,Ws,Xs,V,Rest).

% Deterministic finite graphs. Edge records have two arguments; vertices for
% connected_graph are integers in range(N). Native sampling implementations may
% replace these canonical predicates; exact inference retains these definitions.
graph_edge(Edge,A,B) :- Edge=..[_,A,B].
graph_adjacent(Edges,A,B) :- member(Edge,Edges),graph_edge(Edge,A,B).
graph_adjacent(Edges,A,B) :- member(Edge,Edges),graph_edge(Edge,B,A).
graph_edges_valid([],_).
graph_edges_valid([Edge|Edges],N) :- graph_edge(Edge,A,B),integer(A),integer(B),
    A>=0,B>=0,A<N,B<N,graph_edges_valid(Edges,N).
graph_flood([],Seen,_,Seen).
graph_flood([W|Rest],Seen,Edges,Reached) :- memberchk(W,Seen),
    graph_flood(Rest,Seen,Edges,Reached).
graph_flood([W|Rest],Seen,Edges,Reached) :- \+ memberchk(W,Seen),
    findall(V,(graph_adjacent(Edges,W,V),\+ memberchk(V,Seen)),Neighbors),
    append(Neighbors,Rest,Pending),graph_flood(Pending,[W|Seen],Edges,Reached).
connected_graph(N,Edges) :- N>0,graph_edges_valid(Edges,N),
    graph_flood([0],[],Edges,Reached),length(Reached,N).

% Fold over edge occurrences, counting both endpoint tickets independently.
% Counting disjunction proofs inside findall would collapse two true endpoints
% in sampled formulas. This definition also retains duplicate edges/self-loops.
graph_vertex_count(Vertex,Vertices,1) :- memberchk(Vertex,Vertices).
graph_vertex_count(Vertex,Vertices,0) :- \+ memberchk(Vertex,Vertices).
graph_incidence_count([],_,0).
graph_incidence_count([Edge|Edges],Vertices,Count) :- graph_edge(Edge,A,B),
    graph_vertex_count(A,Vertices,Left),graph_vertex_count(B,Vertices,Right),
    graph_incidence_count(Edges,Vertices,Rest),Count is Left+Right+Rest.

% Independent Bernoulli decisions indexed by draw scope, probability and value.
% Repeating an item reuses its decision; repeated selected occurrences remain in
% the output list. Different proposals therefore require different Id values.
P::bernoulli_draw(Id,P,X) :- P>0,P<1.
bernoulli_member(_,P,_) :- P=:=1.
bernoulli_member(Id,P,X) :- P>0,P<1,bernoulli_draw(Id,P,X).
bernoulli_subset(_,_,[],[]).
bernoulli_subset(Id,P,[X|Xs],[X|Selected]) :- bernoulli_member(Id,P,X),
    bernoulli_subset(Id,P,Xs,Selected).
bernoulli_subset(Id,P,[X|Xs],Selected) :- \+ bernoulli_member(Id,P,X),
    bernoulli_subset(Id,P,Xs,Selected).
