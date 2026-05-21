(define
  (domain x0010)
  (:requirements :typing)
  (:types x0005 x0318 x0346 - x0316 x0316 x0317 - object)
  (:predicates
    (x0001 ?v0006 - x0316 ?v0003 - x0317)
    (x0311 ?v0001 - x0005 ?v0009 - x0346)
    (x0330 ?v0010 ?v0011 - x0317)
    (x0314 ?v0010 ?v0011 - x0317)
    (x0312 ?v0009 - x0346)
    (x0313 ?v0007 - x0318 ?v0006 - x0346))
  (:action x0003
    :parameters (?v0002 - x0005 ?v0008 - x0346 ?v0003 - x0317)
    :precondition (and (x0311 ?v0002 ?v0008) (x0001 ?v0008 ?v0003))
    :effect (and (not (x0311 ?v0002 ?v0008)) (x0312 ?v0008) (x0001 ?v0002 ?v0003)))
  (:action x0002
    :parameters (?v0002 - x0005 ?v0008 - x0346 ?v0003 - x0317)
    :precondition (and (x0312 ?v0008) (x0001 ?v0008 ?v0003) (x0001 ?v0002 ?v0003))
    :effect (and (not (x0312 ?v0008)) (x0311 ?v0002 ?v0008) (not (x0001 ?v0002 ?v0003))))
  (:action x0352
    :parameters (?v0002 - x0005 ?v0004 - x0317 ?v0005 - x0317)
    :precondition (and (x0001 ?v0002 ?v0004) (x0330 ?v0004 ?v0005))
    :effect (and (x0001 ?v0002 ?v0005) (not (x0001 ?v0002 ?v0004))))
  (:action x0351
    :parameters (?v0006 - x0318 ?v0008 - x0346 ?v0003 - x0317)
    :precondition (and (x0313 ?v0006 ?v0008) (x0001 ?v0008 ?v0003))
    :effect (and (not (x0313 ?v0006 ?v0008)) (x0001 ?v0006 ?v0003)))
  (:action x0315
    :parameters (?v0006 - x0318 ?v0008 - x0346 ?v0003 - x0317)
    :precondition (and (x0001 ?v0008 ?v0003) (x0001 ?v0006 ?v0003))
    :effect (and (x0313 ?v0006 ?v0008) (not (x0001 ?v0006 ?v0003))))
  (:action x0004
    :parameters (?v0008 - x0346 ?v0004 - x0317 ?v0005 - x0317 ?v0002 - x0005)
    :precondition (and (x0001 ?v0008 ?v0004) (x0311 ?v0002 ?v0008) (x0314 ?v0004 ?v0005))
    :effect (and (not (x0001 ?v0008 ?v0004)) (x0001 ?v0008 ?v0005))))
