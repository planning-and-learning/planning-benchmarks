% Exact subfamily: Grid(2,2,1,1,2), goal_probability=1.
% One shape makes the random frontier-lock choice irrelevant to the output.
% This is deliberately not a complete replacement for general Grid.
:- use_module(library(lists)).

cells([0,1,2,3]).
adjacent(A,B) :- between(0,3,A), between(0,3,B),
    AX is A // 2, AY is A mod 2, BX is B // 2, BY is B mod 2,
    1 =:= abs(AX-BX) + abs(AY-BY).

layout(Locks,Open) :-
    cells(Cells), select_uniform(lock_first,Cells,A,Rest),
    select_uniform(lock_second,Rest,B,Open), sort([A,B],Locks).
reachable(R,R,Open) :- member(R,Open).
reachable(R,C,Open) :- reachable(R,Previous,Open),
    adjacent(Previous,C), member(C,Open).

outcome(Locks,Robot,Key,Goal) :-
    layout(Locks,Open), select_uniform(robot,Open,Robot,_),
    findall(C,reachable(Robot,C,Open),Reached0), sort(Reached0,Reached),
    select_uniform(key,Reached,Key,_),
    cells(Cells), select(Key,Cells,Destinations),
    select_uniform(goal,Destinations,Goal,_).

query(outcome(_,_,_,_)).
