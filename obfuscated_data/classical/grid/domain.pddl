(define
  (domain x0005)
  (:requirements :strips)
  (:predicates
    (x0156 ?v0012)
    (x0161 ?v0008)
    (x0002 ?v0009 ?v0012)
    (x0001)
    (x0226 ?v0010)
    (x0148 ?v0002 ?v0010)
    (x0158 ?v0012)
    (x0155 ?v0012 ?v0010)
    (x0146 ?v0002)
    (x0004 ?v0012 ?v0013)
    (x0147 ?v0002)
    (x0003 ?v0012))
  (:action x0231
    :parameters (?v0001 ?v0004 ?v0003 ?v0011)
    :precondition (and (x0004 ?v0001 ?v0004) (x0003 ?v0001) (x0155 ?v0004 ?v0011) (x0147 ?v0003) (x0161 ?v0004) (x0146 ?v0003) (x0161 ?v0001) (x0148 ?v0003 ?v0011) (x0156 ?v0004) (x0226 ?v0011))
    :effect (and (x0158 ?v0004) (not (x0156 ?v0004))))
  (:action x0225
    :parameters (?v0001 ?v0003)
    :precondition (and (x0003 ?v0001) (x0147 ?v0003) (x0146 ?v0003) (x0161 ?v0001))
    :effect (and (x0001) (not (x0146 ?v0003)) (x0002 ?v0003 ?v0001)))
  (:action x0160
    :parameters (?v0001 ?v0005 ?v0007)
    :precondition (and (x0147 ?v0007) (x0002 ?v0005 ?v0001) (x0146 ?v0007) (x0003 ?v0001) (x0161 ?v0001) (x0147 ?v0005))
    :effect (and (not (x0146 ?v0007)) (x0146 ?v0005) (not (x0002 ?v0005 ?v0001)) (x0002 ?v0007 ?v0001)))
  (:action x0159
    :parameters (?v0001 ?v0003)
    :precondition (and (x0003 ?v0001) (x0147 ?v0003) (x0001) (x0161 ?v0001) (x0002 ?v0003 ?v0001))
    :effect (and (x0146 ?v0003) (not (x0002 ?v0003 ?v0001)) (not (x0001))))
  (:action x0157
    :parameters (?v0001 ?v0006)
    :precondition (and (x0003 ?v0001) (x0158 ?v0006) (x0161 ?v0001) (x0161 ?v0006) (x0004 ?v0001 ?v0006))
    :effect (and (not (x0003 ?v0001)) (x0003 ?v0006))))
