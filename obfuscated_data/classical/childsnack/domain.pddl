(define
  (domain x0024)
  (:requirements :typing :equality)
  (:types x0129 x0136 x0103 x0023 x0006 x0076)
  (:constants x0093 - x0103)
  (:predicates
    (x0100 ?v0002 - x0023)
    (x0141 ?v0002 - x0023 ?v0003 - x0103)
    (x0098 ?v0002 - x0076)
    (x0003 ?v0001 - x0006)
    (x0101 ?v0006 - x0129)
    (x0099 ?v0006 - x0129)
    (x0005 ?v0006 - x0129)
    (x0001 ?v0002 - x0023)
    (x0097 ?v0001 - x0006)
    (x0002 ?v0007 - x0136 ?v0003 - x0103)
    (x0132 ?v0002 - x0023)
    (x0102 ?v0006 - x0129 ?v0007 - x0136)
    (x0004 ?v0002 - x0076))
  (:action x0094
    :parameters (?v0006 - x0129 ?v0001 - x0006 ?v0002 - x0076)
    :precondition (and (x0003 ?v0001) (x0101 ?v0006) (x0004 ?v0002))
    :effect (and (not (x0003 ?v0001)) (x0005 ?v0006) (not (x0004 ?v0002)) (not (x0101 ?v0006))))
  (:action x0095
    :parameters (?v0006 - x0129 ?v0001 - x0006 ?v0002 - x0076)
    :precondition (and (x0003 ?v0001) (x0098 ?v0002) (x0101 ?v0006) (x0097 ?v0001) (x0004 ?v0002))
    :effect (and (x0099 ?v0006) (not (x0003 ?v0001)) (x0005 ?v0006) (not (x0004 ?v0002)) (not (x0101 ?v0006))))
  (:action x0131
    :parameters (?v0006 - x0129 ?v0002 - x0023 ?v0007 - x0136 ?v0003 - x0103)
    :precondition (and (x0099 ?v0006) (x0141 ?v0002 ?v0003) (x0002 ?v0007 ?v0003) (x0102 ?v0006 ?v0007) (x0001 ?v0002))
    :effect (and (x0132 ?v0002) (not (x0102 ?v0006 ?v0007))))
  (:action x0096
    :parameters (?v0007 - x0136 ?v0004 ?v0005 - x0103)
    :precondition (and (x0002 ?v0007 ?v0004))
    :effect (and (not (x0002 ?v0007 ?v0004)) (x0002 ?v0007 ?v0005)))
  (:action x0130
    :parameters (?v0006 - x0129 ?v0002 - x0023 ?v0007 - x0136 ?v0003 - x0103)
    :precondition (and (x0100 ?v0002) (x0141 ?v0002 ?v0003) (x0002 ?v0007 ?v0003) (x0102 ?v0006 ?v0007))
    :effect (and (x0132 ?v0002) (not (x0102 ?v0006 ?v0007))))
  (:action x0104
    :parameters (?v0006 - x0129 ?v0007 - x0136)
    :precondition (and (x0005 ?v0006) (x0002 ?v0007 x0093))
    :effect (and (not (x0005 ?v0006)) (x0102 ?v0006 ?v0007))))
