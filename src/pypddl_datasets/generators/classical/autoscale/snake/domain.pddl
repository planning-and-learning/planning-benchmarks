; Snake is not a game where everything is known a priori. 
; Therefore we make two modifications: 
; 1. The player knows where points will spawn. 
; 2. Points can spawn inside the snake, but they can only be collected by the head of the snake.
; 3. There is a constant number of points at a time and no two points can spawn in the same location
; Based on the submission

(define (domain snake)
	(:requirements :strips :negative-preconditions :equality)

	(:constants dummypoint)

	(:predicates 
		(isadjacent ?x ?y) ;up down left right of a field
		(tailsnake ?x) ;the last field of the snake
		(headsnake ?x) ;the first field of the snake
                (nextsnake ?x ?y) ;pieces of the snake that are connected. from front to back
		(blocked ?x) ;a field that is occupied by the snake or by an obstacle
		(spawn ?x) ;next point that will spawn
		(nextspawn ?x ?y) ;point y will spawn after point x
		(ispoint ?x) ;a field that has a point that can be collected by the snake
	)

	(:action move
		:parameters (?head ?newhead ?tail ?newtail)
		:precondition (and
			(headsnake ?head)
			(isadjacent ?head ?newhead)
         		(tailsnake ?tail)
			(nextsnake ?newtail ?tail)
			(not (blocked ?newhead))
			(not (ispoint ?newhead))
		)
        	:effect (and
			(blocked ?newhead)
			(headsnake ?newhead)
			(nextsnake ?newhead ?head)
			(not (headsnake ?head))
			(not (blocked ?tail))
			(not (tailsnake ?tail))
			(not (nextsnake ?newtail ?tail))
			(tailsnake ?newtail)
			)
	)

	(:action move-and-eat-spawn
		:parameters  (?head ?newhead ?spawnpoint ?nextspawnpoint)
		:precondition (and
			      (headsnake ?head)
			      (isadjacent ?head ?newhead)
			      (not (blocked ?newhead))
			      (ispoint ?newhead)
			      (spawn ?spawnpoint)
			      (nextspawn ?spawnpoint ?nextspawnpoint)
			      (not (= ?spawnpoint dummypoint))
		)
        	:effect (and
			(blocked ?newhead)
			(headsnake ?newhead)
			(nextsnake ?newhead ?head)
			(not (headsnake ?head))
			(not (ispoint ?newhead))
			(ispoint ?spawnpoint)
			(not (spawn ?spawnpoint))
			(spawn ?nextspawnpoint)
			)
	)

	(:action move-and-eat-no-spawn
		:parameters  (?head ?newhead)
		:precondition (and
			(headsnake ?head)
			(isadjacent ?head ?newhead)
			(not (blocked ?newhead))
			(ispoint ?newhead)
			(spawn dummypoint)
		)
        	:effect (and
			(blocked ?newhead)
			(headsnake ?newhead)
			(nextsnake ?newhead ?head)
			(not (headsnake ?head))
			(not (ispoint ?newhead))
			)
	)
)