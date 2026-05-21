(define
  (domain x0048)
  (:requirements :strips)
  (:constants x0054 x0055)
  (:predicates
    (x0053 ?v0007)
    (x0024 ?v0005 ?v0003)
    (x0003 ?v0001)
    (x0001 ?v0001 ?v0007)
    (x0026 ?v0003)
    (x0027 ?v0003)
    (x0002 ?v0007))
  (:action x0050
    :parameters (?v0002 ?v0009)
    :precondition (and (x0002 ?v0002) (x0053 ?v0009) (x0053 ?v0002))
    :effect (and (not (x0002 ?v0002)) (x0002 ?v0009)))
  (:action x0051
    :parameters (?v0006 ?v0008 ?v0004)
    :precondition (and (x0053 ?v0008) (x0002 ?v0008) (x0003 ?v0006) (x0026 ?v0004) (x0027 ?v0004) (x0001 ?v0006 ?v0008))
    :effect (and (not (x0026 ?v0004)) (x0024 ?v0006 ?v0004) (not (x0001 ?v0006 ?v0008))))
  (:action x0025
    :parameters (?v0006 ?v0008 ?v0004)
    :precondition (and (x0053 ?v0008) (x0002 ?v0008) (x0003 ?v0006) (x0027 ?v0004) (x0024 ?v0006 ?v0004))
    :effect (and (not (x0024 ?v0006 ?v0004)) (x0026 ?v0004) (x0001 ?v0006 ?v0008))))
