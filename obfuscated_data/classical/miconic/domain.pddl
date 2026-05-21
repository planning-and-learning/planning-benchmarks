(define
  (domain x0025)
  (:requirements :strips :typing)
  (:types x0023 - object x0131 - object)
  (:predicates
    (x0114 ?v0008 - x0131 ?v0004 - x0023)
    (x0005 ?v0008 - x0131 ?v0004 - x0023)
    (x0132 ?v0008 - x0131)
    (x0024 ?v0004 - x0023)
    (x0001 ?v0005 - x0023 ?v0006 - x0023)
    (x0003 ?v0008 - x0131))
  (:action x0006
    :parameters (?v0002 - x0023 ?v0003 - x0023)
    :precondition (and (x0001 ?v0003 ?v0002) (x0024 ?v0002))
    :effect (and (x0024 ?v0003) (not (x0024 ?v0002))))
  (:action x0002
    :parameters (?v0001 - x0023 ?v0007 - x0131)
    :precondition (and (x0114 ?v0007 ?v0001) (x0024 ?v0001))
    :effect (and (x0003 ?v0007) (not (x0114 ?v0007 ?v0001))))
  (:action x0004
    :parameters (?v0001 - x0023 ?v0007 - x0131)
    :precondition (and (x0003 ?v0007) (x0024 ?v0001) (x0005 ?v0007 ?v0001))
    :effect (and (not (x0003 ?v0007)) (x0132 ?v0007)))
  (:action x0133
    :parameters (?v0002 - x0023 ?v0003 - x0023)
    :precondition (and (x0024 ?v0002) (x0001 ?v0002 ?v0003))
    :effect (and (x0024 ?v0003) (not (x0024 ?v0002)))))
