(define
  (domain x0031)
  (:requirements :strips :typing)
  (:types x0031 x0004 x0018 x0009)
  (:predicates
    (x0005 ?v0001 - x0004 ?v0005 - x0018)
    (x0003 ?v0004 - x0009 ?v0001 - x0004)
    (x0028 ?v0006 - x0031 ?v0001 - x0004)
    (x0215 ?v0004 - x0009 ?v0005 - x0018)
    (x0029 ?v0006 - x0031)
    (x0002 ?v0004 - x0009)
    (x0027 ?v0004 - x0009 ?v0006 - x0031)
    (x0030 ?v0004 - x0009))
  (:action x0217
    :parameters (?v0004 - x0009 ?v0006 - x0031)
    :precondition (and (x0029 ?v0006) (x0027 ?v0004 ?v0006))
    :effect (and (not (x0002 ?v0004)) (not (x0029 ?v0006)) (x0030 ?v0004)))
  (:action x0218
    :parameters (?v0006 - x0031 ?v0001 - x0004 ?v0004 - x0009 ?v0005 - x0018)
    :precondition (and (x0002 ?v0004) (x0027 ?v0004 ?v0006) (x0030 ?v0004) (x0215 ?v0004 ?v0005) (x0028 ?v0006 ?v0001))
    :effect (x0005 ?v0001 ?v0005))
  (:action x0216
    :parameters (?v0004 - x0009 ?v0006 - x0031)
    :precondition (and (x0027 ?v0004 ?v0006) (x0030 ?v0004))
    :effect (and (not (x0030 ?v0004)) (x0029 ?v0006)))
  (:action x0001
    :parameters (?v0006 - x0031 ?v0004 - x0009 ?v0001 - x0004)
    :precondition (and (x0027 ?v0004 ?v0006) (x0030 ?v0004) (x0003 ?v0004 ?v0001) (x0028 ?v0006 ?v0001))
    :effect (x0002 ?v0004))
  (:action x0226
    :parameters (?v0006 - x0031 ?v0002 - x0004 ?v0003 - x0004)
    :precondition (and (x0028 ?v0006 ?v0003))
    :effect (and (not (x0028 ?v0006 ?v0003)) (x0028 ?v0006 ?v0002))))
