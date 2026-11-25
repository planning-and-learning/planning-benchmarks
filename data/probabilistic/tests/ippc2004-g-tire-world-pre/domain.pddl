(define (domain g-tire-world-pre)
	(:requirements :strips :negative-preconditions :probabilistic-effects :typing)
	(:types location)
	(:predicates	(vehicle-at ?loc - location)
			(hasspare-vehicle)
			(hasspare-location ?loc - location)
			(road ?from - location ?to - location)
			(flattire))
	(:action mov-car
		:parameters (?from - location ?to - location)
		:precondition (and (vehicle-at ?from) (road ?from ?to)
					(not (flattire)))
		:effect (and (vehicle-at ?to) (not (vehicle-at ?from))
				(probabilistic .15 (flattire)))
	)

	(:action loadtire
		:parameters (?loc - location)
		:precondition (and (vehicle-at ?loc) (hasspare-location ?loc) 
					(not (hasspare-vehicle)))
		:effect (and (hasspare-vehicle) (not (hasspare-location ?loc)))
	)

	(:action changetire
		:precondition (and (hasspare-vehicle) (flattire))
		:effect (and (not (hasspare-vehicle))
				 (not (flattire))
			  )
	)

)
