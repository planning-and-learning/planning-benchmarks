(define
  (domain x0024)
  (:predicates
    (x0001 ?v0001 ?v0004)
    (x0002 ?v0004)
    (x0092 ?v0007 ?v0008)
    (x0023)
    (x0093 ?v0001)
    (x0021 ?v0001)
    (x0091 ?v0004))
  (:action x0094
    :parameters (?v0003 ?v0006)
    :precondition (and (x0002 ?v0003) (x0092 ?v0003 ?v0006) (x0091 ?v0006) (x0091 ?v0003))
    :effect (and (not (x0002 ?v0003)) (x0002 ?v0006)))
  (:action x0003
    :parameters (?v0002 ?v0005)
    :precondition (and (x0001 ?v0002 ?v0005) (x0002 ?v0005) (x0023) (x0021 ?v0002) (x0091 ?v0005))
    :effect (and (x0093 ?v0002) (not (x0023)) (not (x0001 ?v0002 ?v0005))))
  (:action x0022
    :parameters (?v0002 ?v0005)
    :precondition (and (x0093 ?v0002) (x0002 ?v0005) (x0021 ?v0002) (x0091 ?v0005))
    :effect (and (x0001 ?v0002 ?v0005) (x0023) (not (x0093 ?v0002)))))
