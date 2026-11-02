% Parameters supplied as facts: grid_size(N), num_packages(N).
:- use_module(library(lists)).
:- use_module(library(string)).

cell(C,X,Y) :- grid_size(N), Last is N-1, between(0,Last,X), between(0,Last,Y), concat([c,'_',X,'_',Y],C).
cells(Cs) :- findall(C, cell(C,_,_), Cs).
package(P) :- num_packages(N), between(1,N,I), concat([p,I],P).
packages(Ps) :- findall(P, package(P), Ps).

origin(P,C) :- package(P), cells(Cs), select_uniform(origin(P),Cs,C,_).
truck_location(C) :- cells(Cs), select_uniform(truck,Cs,C,_).
all_at([],C).
all_at([P|Ps],C) :- origin(P,C), all_at(Ps,C).
colocated(C) :- cell(C,_,_), packages(Ps), all_at(Ps,C).
colocated :- colocated(_).

% Keep initial positions fixed while conditioning the destination locally.
destination(C) :- colocated(Start), cells(Cs), select(Start,Cs,Allowed), select_uniform(destination(Start),Allowed,C,_).
destination(C) :- \+ colocated, cells(Cs), select_uniform(destination(mixed),Cs,C,_).

object(C,cell) :- cell(C,_,_).
object(P,package) :- package(P).
object(t1,truck).
initial(adjacent(C,D)) :- cell(C,X,Y), cell(D,U,V), 1 =:= abs(X-U)+abs(Y-V).
initial(at(P,C)) :- origin(P,C).
initial(at(t1,C)) :- truck_location(C).
initial(empty(t1)).
goal(at(P,C)) :- package(P), destination(C).

domain(delivery).
problem_name(Name) :- grid_size(N), num_packages(P), concat(['delivery-',N,x,N,'-',P],Name).
