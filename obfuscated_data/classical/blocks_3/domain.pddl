(define
  (domain x0046)
  (:requirements :strips :equality :negative-preconditions)
  (:predicates
    (x0047 ?v0004)
    (x0052 ?v0004)
    (x0051 ?v0004 ?v0005))
  (:action x0049
    :parameters (?v0002 ?v0001)
    :precondition (and (x0051 ?v0002 ?v0001) (x0047 ?v0002))
    :effect (and (x0052 ?v0002) (x0047 ?v0001) (not (x0051 ?v0002 ?v0001))))
  (:action x0050
    :parameters (?v0002 ?v0003)
    :precondition (and (x0052 ?v0002) (x0047 ?v0003) (x0047 ?v0002))
    :effect (and (not (x0047 ?v0003)) (not (x0052 ?v0002)) (x0051 ?v0002 ?v0003)))
  (:action x0048
    :parameters (?v0002 ?v0001 ?v0003)
    :precondition (and (not (= ?v0002 ?v0003)) (x0047 ?v0003) (x0051 ?v0002 ?v0001) (x0047 ?v0002))
    :effect (and (not (x0047 ?v0003)) (x0047 ?v0001) (x0051 ?v0002 ?v0003) (not (x0051 ?v0002 ?v0001)))))
