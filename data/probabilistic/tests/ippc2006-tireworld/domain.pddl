(define (domain tire)
  (:requirements :strips :probabilistic-effects :typing)
  (:types location)
  (:predicates (vehicle-at ?loc - location) (spare-in ?loc - location) (road ?from - location ?to - location) (not-flattire) (hasspare))
  (:action move-car
    :parameters (?from - location ?to - location)
    :precondition (and (vehicle-at ?from) (road ?from ?to) (not-flattire))
    :effect (and (vehicle-at ?to) (not (vehicle-at ?from)) (probabilistic 2/5 (not (not-flattire))))
  )
  (:action loadtire
    :parameters (?loc - location)
    :precondition (and (vehicle-at ?loc) (spare-in ?loc))
    :effect (and (hasspare) (not (spare-in ?loc)))
  )
  (:action changetire
    :precondition (hasspare)
    :effect (probabilistic 1/2 (and (not (hasspare)) (not-flattire)))
  )
)
