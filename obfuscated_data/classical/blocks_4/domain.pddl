(define
  (domain x0047)
  (:requirements :strips)
  (:predicates
    (x0048 ?v0003)
    (x0001)
    (x0049 ?v0003)
    (x0051 ?v0003)
    (x0050 ?v0003 ?v0004))
  (:action x0055
    :parameters (?v0001 ?v0002)
    :precondition (and (x0050 ?v0001 ?v0002) (x0001) (x0048 ?v0001))
    :effect (and (not (x0001)) (not (x0050 ?v0001 ?v0002)) (not (x0048 ?v0001)) (x0048 ?v0002) (x0049 ?v0001)))
  (:action x0052
    :parameters (?v0001)
    :precondition (and (x0001) (x0048 ?v0001) (x0051 ?v0001))
    :effect (and (not (x0051 ?v0001)) (not (x0001)) (not (x0048 ?v0001)) (x0049 ?v0001)))
  (:action x0053
    :parameters (?v0001)
    :precondition (x0049 ?v0001)
    :effect (and (x0001) (not (x0049 ?v0001)) (x0048 ?v0001) (x0051 ?v0001)))
  (:action x0054
    :parameters (?v0001 ?v0002)
    :precondition (and (x0048 ?v0002) (x0049 ?v0001))
    :effect (and (x0050 ?v0001 ?v0002) (x0001) (not (x0048 ?v0002)) (not (x0049 ?v0001)) (x0048 ?v0001))))
