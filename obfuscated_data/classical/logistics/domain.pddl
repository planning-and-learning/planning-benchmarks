(define
  (domain x0303)
  (:requirements :strips)
  (:predicates
    (x0017 ?v0008 ?v0009)
    (x0014 ?v0003)
    (x0018 ?v0007 ?v0003)
    (x0005 ?v0002)
    (x0004 ?v0001)
    (x0304 ?v0007)
    (x0006 ?v0007 ?v0004)
    (x0082 ?v0004)
    (x0322 ?v0010))
  (:action x0016
    :parameters (?v0001 ?v0005 ?v0006)
    :precondition (and (x0006 ?v0001 ?v0005) (x0005 ?v0006) (x0005 ?v0005) (x0004 ?v0001))
    :effect (and (x0006 ?v0001 ?v0006) (not (x0006 ?v0001 ?v0005))))
  (:action x0324
    :parameters (?v0007 ?v0010 ?v0004)
    :precondition (and (x0006 ?v0010 ?v0004) (x0304 ?v0007) (x0082 ?v0004) (x0017 ?v0007 ?v0010) (x0322 ?v0010))
    :effect (and (not (x0017 ?v0007 ?v0010)) (x0006 ?v0007 ?v0004)))
  (:action x0081
    :parameters (?v0007 ?v0010 ?v0004)
    :precondition (and (x0006 ?v0010 ?v0004) (x0304 ?v0007) (x0006 ?v0007 ?v0004) (x0082 ?v0004) (x0322 ?v0010))
    :effect (and (not (x0006 ?v0007 ?v0004)) (x0017 ?v0007 ?v0010)))
  (:action x0323
    :parameters (?v0007 ?v0001 ?v0004)
    :precondition (and (x0004 ?v0001) (x0304 ?v0007) (x0006 ?v0001 ?v0004) (x0082 ?v0004) (x0017 ?v0007 ?v0001))
    :effect (and (x0006 ?v0007 ?v0004) (not (x0017 ?v0007 ?v0001))))
  (:action x0015
    :parameters (?v0010 ?v0005 ?v0006 ?v0003)
    :precondition (and (x0014 ?v0003) (x0018 ?v0005 ?v0003) (x0018 ?v0006 ?v0003) (x0082 ?v0005) (x0006 ?v0010 ?v0005) (x0322 ?v0010) (x0082 ?v0006))
    :effect (and (x0006 ?v0010 ?v0006) (not (x0006 ?v0010 ?v0005))))
  (:action x0080
    :parameters (?v0007 ?v0001 ?v0004)
    :precondition (and (x0004 ?v0001) (x0304 ?v0007) (x0006 ?v0007 ?v0004) (x0006 ?v0001 ?v0004) (x0082 ?v0004))
    :effect (and (not (x0006 ?v0007 ?v0004)) (x0017 ?v0007 ?v0001))))
