; source: https://github.com/AI-Planning/pddl-generators/blob/main/transport/domain.pddl
; updates:
;  - removed :action-costs and :functions
;  - capacity type now is size
;  - capacity-number predicate now is capacity
;  - each drive consumes one unit of per-vehicle fuel; no refuelling
(define (domain transport-fuel)
  (:requirements :strips :typing)
  (:types
        size fuellevel location locatable - object
        vehicle package - locatable
  )

  (:predicates
     (road ?l1 ?l2 - location)
     (at ?x - locatable ?v - location)
     (in ?x - package ?v - vehicle)
     (capacity ?v - vehicle ?s1 - size)
     (capacity-predecessor ?s1 ?s2 - size)
     (fuel ?v - vehicle ?f - fuellevel)
     (fuel-predecessor ?low ?high - fuellevel)
  )

  (:action drive
    :parameters (?v - vehicle ?l1 ?l2 - location ?fuel-before ?fuel-after - fuellevel)
    :precondition (and
        (at ?v ?l1)
        (road ?l1 ?l2)
        (fuel ?v ?fuel-before)
        (fuel-predecessor ?fuel-after ?fuel-before)
      )
    :effect (and
        (not (at ?v ?l1))
        (at ?v ?l2)
        (not (fuel ?v ?fuel-before))
        (fuel ?v ?fuel-after)
      )
  )

 (:action pick-up
    :parameters (?v - vehicle ?l - location ?p - package ?s1 ?s2 - size)
    :precondition (and
        (at ?v ?l)
        (at ?p ?l)
        (capacity-predecessor ?s1 ?s2)
        (capacity ?v ?s2)
      )
    :effect (and
        (not (at ?p ?l))
        (in ?p ?v)
        (capacity ?v ?s1)
        (not (capacity ?v ?s2))
      )
  )

  (:action drop
    :parameters (?v - vehicle ?l - location ?p - package ?s1 ?s2 - size)
    :precondition (and
        (at ?v ?l)
        (in ?p ?v)
        (capacity-predecessor ?s1 ?s2)
        (capacity ?v ?s1)
      )
    :effect (and
        (not (in ?p ?v))
        (at ?p ?l)
        (capacity ?v ?s2)
        (not (capacity ?v ?s1))
      )
  )

)
