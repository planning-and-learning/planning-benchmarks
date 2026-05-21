(define
  (domain x0174)
  (:requirements :typing :equality :negative-preconditions)
  (:types x0244 - x0227 x0241 - x0227 x0173 - object x0227 - object)
  (:predicates
    (x0002 ?v0006 - x0227 ?v0007 - x0173)
    (x0001 ?v0006 - x0173 ?v0007 - x0173)
    (x0172 ?v0006 - x0244 ?v0007 - x0241)
    (x0226 ?v0006 - x0244))
  (:action x0228
    :parameters (?v0003 - x0244 ?v0001 - x0173 ?v0004 - x0173)
    :precondition (and (x0001 ?v0001 ?v0004) (x0002 ?v0003 ?v0001) (not (= ?v0001 ?v0004)))
    :effect (and (x0002 ?v0003 ?v0004) (not (x0002 ?v0003 ?v0001))))
  (:action x0242
    :parameters (?v0003 - x0244 ?v0002 - x0241 ?v0005 - x0173)
    :precondition (and (x0226 ?v0003) (x0002 ?v0003 ?v0005) (x0002 ?v0002 ?v0005))
    :effect (and (not (x0226 ?v0003)) (x0172 ?v0003 ?v0002) (not (x0002 ?v0002 ?v0005))))
  (:action x0225
    :parameters (?v0003 - x0244 ?v0002 - x0241 ?v0005 - x0173)
    :precondition (and (x0172 ?v0003 ?v0002) (x0002 ?v0003 ?v0005))
    :effect (and (x0226 ?v0003) (not (x0172 ?v0003 ?v0002)) (x0002 ?v0002 ?v0005))))
