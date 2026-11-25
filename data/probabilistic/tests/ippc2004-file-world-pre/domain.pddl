(define (domain file-world-pre)
	(:requirements :strips :negative-preconditions :probabilistic-effects :rewards)
	(:predicates	(has-type ?p)
		(goes-in ?p ?f)
		(filed ?p)
		(haveF0)
		(haveF1)
		(haveF2)
		(haveF3)
		(haveF4)
		)
	(:constants F0 F1 F2 F3 F4 )

(:action get-type
	:parameters (?p)
	:precondition	(and (not (has-type ?p)))
	:effect
(and (has-type ?p)
		(probabilistic
			0.2	(goes-in ?p F0)
			0.2	(goes-in ?p F1)
			0.2	(goes-in ?p F2)
			0.2	(goes-in ?p F3)
			0.2	(goes-in ?p F4)
))
)

(:action get-folder-F0
	:precondition  (and 		(not (haveF0)) 
		(not (haveF1)) 
		(not (haveF2)) 
		(not (haveF3)) 
		(not (haveF4)) 
)
	:effect (and (decrease (reward) 100)
(haveF0)
))

(:action get-folder-F1
	:precondition  (and 		(not (haveF0)) 
		(not (haveF1)) 
		(not (haveF2)) 
		(not (haveF3)) 
		(not (haveF4)) 
)
	:effect (and (decrease (reward) 100)
(haveF1)
))

(:action get-folder-F2
	:precondition  (and 		(not (haveF0)) 
		(not (haveF1)) 
		(not (haveF2)) 
		(not (haveF3)) 
		(not (haveF4)) 
)
	:effect (and (decrease (reward) 100)
(haveF2)
))

(:action get-folder-F3
	:precondition  (and 		(not (haveF0)) 
		(not (haveF1)) 
		(not (haveF2)) 
		(not (haveF3)) 
		(not (haveF4)) 
)
	:effect (and (decrease (reward) 100)
(haveF3)
))

(:action get-folder-F4
	:precondition  (and 		(not (haveF0)) 
		(not (haveF1)) 
		(not (haveF2)) 
		(not (haveF3)) 
		(not (haveF4)) 
)
	:effect (and (decrease (reward) 100)
(haveF4)
))

(:action file-F0
	:parameters (?p)
	:precondition (and (haveF0) (has-type ?p) (goes-in ?p F0))
	:effect (and (decrease (reward) 1)
(filed ?p)
))

(:action file-F1
	:parameters (?p)
	:precondition (and (haveF1) (has-type ?p) (goes-in ?p F1))
	:effect (and (decrease (reward) 1)
(filed ?p)
))

(:action file-F2
	:parameters (?p)
	:precondition (and (haveF2) (has-type ?p) (goes-in ?p F2))
	:effect (and (decrease (reward) 1)
(filed ?p)
))

(:action file-F3
	:parameters (?p)
	:precondition (and (haveF3) (has-type ?p) (goes-in ?p F3))
	:effect (and (decrease (reward) 1)
(filed ?p)
))

(:action file-F4
	:parameters (?p)
	:precondition (and (haveF4) (has-type ?p) (goes-in ?p F4))
	:effect (and (decrease (reward) 1)
(filed ?p)
))

(:action return-F0
	:precondition	(haveF0)
	:effect
	(not (haveF0))
)

(:action return-F1
	:precondition	(haveF1)
	:effect
	(not (haveF1))
)

(:action return-F2
	:precondition	(haveF2)
	:effect
	(not (haveF2))
)

(:action return-F3
	:precondition	(haveF3)
	:effect
	(not (haveF3))
)

(:action return-F4
	:precondition	(haveF4)
	:effect
	(not (haveF4))
)

)
