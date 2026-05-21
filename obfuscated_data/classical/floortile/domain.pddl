(define
  (domain x0007)
  (:requirements :typing :action-costs)
  (:types x0005 x0065 x0058 - object)
  (:predicates
    (x0052 ?v0003 - x0058)
    (x0167 ?v0004 - x0065 ?v0005 - x0065)
    (x0056 ?v0004 - x0065 ?v0001 - x0005)
    (x0004 ?v0004 - x0065)
    (x0057 ?v0004 - x0065 ?v0005 - x0065)
    (x0060 ?v0003 - x0058 ?v0001 - x0005)
    (x0001 ?v0001 - x0005)
    (x0059 ?v0003 - x0058 ?v0004 - x0065)
    (x0006 ?v0004 - x0065 ?v0005 - x0065)
    (x0053 ?v0004 - x0065 ?v0005 - x0065))
  (:functions (x0166) - number)
  (:action x0053
    :parameters (?v0003 - x0058 ?v0004 - x0065 ?v0005 - x0065)
    :precondition (and (x0059 ?v0003 ?v0004) (x0004 ?v0005) (x0053 ?v0005 ?v0004))
    :effect (and (not (x0004 ?v0005)) (not (x0059 ?v0003 ?v0004)) (increase (x0166) 1) (x0004 ?v0004) (x0059 ?v0003 ?v0005)))
  (:action x0006
    :parameters (?v0003 - x0058 ?v0004 - x0065 ?v0005 - x0065)
    :precondition (and (x0059 ?v0003 ?v0004) (x0004 ?v0005) (x0006 ?v0005 ?v0004))
    :effect (and (not (x0004 ?v0005)) (not (x0059 ?v0003 ?v0004)) (increase (x0166) 1) (x0004 ?v0004) (x0059 ?v0003 ?v0005)))
  (:action x0167
    :parameters (?v0003 - x0058 ?v0004 - x0065 ?v0005 - x0065)
    :precondition (and (x0059 ?v0003 ?v0004) (x0167 ?v0005 ?v0004) (x0004 ?v0005))
    :effect (and (not (x0004 ?v0005)) (not (x0059 ?v0003 ?v0004)) (x0004 ?v0004) (increase (x0166) 3) (x0059 ?v0003 ?v0005)))
  (:action x0057
    :parameters (?v0003 - x0058 ?v0004 - x0065 ?v0005 - x0065)
    :precondition (and (x0059 ?v0003 ?v0004) (x0057 ?v0005 ?v0004) (x0004 ?v0005))
    :effect (and (not (x0004 ?v0005)) (not (x0059 ?v0003 ?v0004)) (increase (x0166) 1) (x0004 ?v0004) (x0059 ?v0003 ?v0005)))
  (:action x0054
    :parameters (?v0003 - x0058 ?v0005 - x0065 ?v0004 - x0065 ?v0001 - x0005)
    :precondition (and (x0059 ?v0003 ?v0004) (x0060 ?v0003 ?v0001) (x0004 ?v0005) (x0006 ?v0005 ?v0004))
    :effect (and (not (x0004 ?v0005)) (increase (x0166) 2) (x0056 ?v0005 ?v0001)))
  (:action x0055
    :parameters (?v0003 - x0058 ?v0005 - x0065 ?v0004 - x0065 ?v0001 - x0005)
    :precondition (and (x0059 ?v0003 ?v0004) (x0060 ?v0003 ?v0001) (x0167 ?v0005 ?v0004) (x0004 ?v0005))
    :effect (and (not (x0004 ?v0005)) (increase (x0166) 2) (x0056 ?v0005 ?v0001)))
  (:action x0003
    :parameters (?v0003 - x0058 ?v0001 - x0005 ?v0002 - x0005)
    :precondition (and (x0060 ?v0003 ?v0001) (x0001 ?v0002))
    :effect (and (x0060 ?v0003 ?v0002) (not (x0060 ?v0003 ?v0001)) (increase (x0166) 5))))
