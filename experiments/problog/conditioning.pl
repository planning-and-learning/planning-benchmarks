% Rovers' graph hierarchy in isolation: three nodes, Bernoulli(1/2) edges.
% Queries and budgets are supplied by verify_conditioning.py.
:- use_module(library(lists)).

candidates([e(0,1), e(0,2), e(1,2)]).
vertex(0). vertex(1). vertex(2).

adjacent(Edges,X,Y) :- member(e(X,Y),Edges).
adjacent(Edges,X,Y) :- member(e(Y,X),Edges).
% Positive recursive reachability avoids enumerating all simple paths.
reachable(_,X,X).
reachable(Edges,X,Y) :- adjacent(Edges,X,Z), reachable(Edges,Z,Y).
connected(Edges) :- forall(vertex(V),reachable(Edges,0,V)).

% All probabilistic identities include the draw's scope and edge.
0.5::keep(Id,Edge).
proposal(_,[],[]).
proposal(Id,[E|Es],[E|Gs]) :- keep(Id,E), proposal(Id,Es,Gs).
proposal(Id,[E|Es],Gs) :- \+ keep(Id,E), proposal(Id,Es,Gs).

% Nested exact inference obtains the whole categorical distribution, rather
% than turning each outcome's marginal into an independent Bernoulli fact.
inner(Allowed,Graph) :- proposal(inner(Allowed),Allowed,Graph).
inner_connected(Allowed) :- inner(Allowed,G), connected(G).
local_draw(Id,Allowed,Graph) :-
    findall((P,G), (subquery(inner(Allowed,G),P,[inner_connected(Allowed)]), P > 0), Weights),
    select_weighted(Id,Weights,Graph,_).
local(V,T) :- candidates(All), local_draw(visibility,All,V),
    local_draw(movement(V),V,T).
local_complete :- local(V,_), candidates(V).

% The superficially similar global evidence model changes visibility's law.
raw_pair(V,T) :- candidates(All), proposal(raw_visibility,All,V),
    proposal(raw_movement(V),V,T).
global_accept :- raw_pair(V,T), connected(V), connected(T).
global_complete :- raw_pair(V,_), candidates(V).

% An explicit local retry budget preserves exhaustion as an outcome. Demand
% sampling can stop early; exact inference must reason about every attempt.
retry(_,_,0,failure).
retry(Id,Allowed,Budget,G) :- Budget > 0,
    proposal(attempt(Id,Budget),Allowed,G), connected(G).
retry(Id,Allowed,Budget,G) :- Budget > 0,
    proposal(attempt(Id,Budget),Allowed,Rejected), \+ connected(Rejected),
    Next is Budget-1, retry(Id,Allowed,Next,G).
finite(Budget,failure,failure) :- candidates(All),
    retry(visibility,All,Budget,failure).
finite(Budget,V,T) :- candidates(All), retry(visibility,All,Budget,V),
    V \= failure, retry(movement(V),V,Budget,T).
finite_success(Budget) :- finite(Budget,V,T), V \= failure, T \= failure.
finite_complete_success(Budget) :- finite(Budget,V,T), candidates(V), T \= failure.

% Closed-form elimination of independent failed attempts keeps the exact
% same finite-budget law, without an unrolled 10,000-attempt model.
P::succeeds(Id,P).
collapsed(Id,Allowed,Budget,G) :-
    subquery(inner_connected(Allowed),C), P is 1-(1-C)**Budget,
    succeeds(Id,P), local_draw(Id,Allowed,G).
collapsed(Id,Allowed,Budget,failure) :-
    subquery(inner_connected(Allowed),C), P is 1-(1-C)**Budget,
    \+ succeeds(Id,P).
collapsed_pair(Budget,failure,failure) :- candidates(All),
    collapsed(visibility,All,Budget,failure).
collapsed_pair(Budget,V,T) :- candidates(All), collapsed(visibility,All,Budget,V),
    V \= failure, collapsed(movement(V),V,Budget,T).
collapsed_success(Budget) :- collapsed_pair(Budget,V,T), V \= failure, T \= failure.
collapsed_complete_success(Budget) :- collapsed_pair(Budget,V,T), candidates(V), T \= failure.
