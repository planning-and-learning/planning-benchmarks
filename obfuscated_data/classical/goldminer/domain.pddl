(define
  (domain x0190)
  (:requirements :typing)
  (:types x0237)
  (:predicates
    (x0236 ?v0001 - x0237)
    (x0244 ?v0001 - x0237)
    (x0235)
    (x0001)
    (x0232 ?v0001 - x0237)
    (x0003 ?v0001 - x0237)
    (x0002 ?v0001 - x0237)
    (x0189 ?v0001 - x0237)
    (x0243 ?v0001 - x0237)
    (x0233)
    (x0234)
    (x0004 ?v0001 - x0237 ?v0002 - x0237))
  (:action x0239
    :parameters (?v0001 - x0237)
    :precondition (and (x0001) (x0189 ?v0001) (x0243 ?v0001))
    :effect (and (not (x0001)) (x0234)))
  (:action x0240
    :parameters (?v0001 - x0237)
    :precondition (and (x0001) (x0002 ?v0001) (x0243 ?v0001))
    :effect (and (not (x0001)) (x0233)))
  (:action x0242
    :parameters (?v0001 - x0237)
    :precondition (and (x0235) (x0243 ?v0001))
    :effect (and (x0001) (x0236 ?v0001) (not (x0235))))
  (:action x0238
    :parameters (?v0001 - x0237 ?v0002 - x0237)
    :precondition (and (x0004 ?v0001 ?v0002) (x0003 ?v0002) (x0243 ?v0001))
    :effect (and (x0243 ?v0002) (not (x0243 ?v0001))))
  (:action x0188
    :parameters (?v0001 - x0237 ?v0002 - x0237)
    :precondition (and (x0235) (x0004 ?v0001 ?v0002) (x0243 ?v0001))
    :effect (and (not (x0232 ?v0002)) (not (x0189 ?v0002)) (not (x0244 ?v0002)) (x0003 ?v0002)))
  (:action x0005
    :parameters (?v0001 - x0237 ?v0002 - x0237)
    :precondition (and (x0004 ?v0001 ?v0002) (x0244 ?v0002) (x0243 ?v0001) (x0233))
    :effect (and (not (x0244 ?v0002)) (x0001) (not (x0233)) (x0003 ?v0002)))
  (:action x0241
    :parameters (?v0001 - x0237)
    :precondition (and (x0001) (x0236 ?v0001) (x0243 ?v0001))
    :effect (and (x0235) (not (x0001)) (not (x0236 ?v0001)))))
