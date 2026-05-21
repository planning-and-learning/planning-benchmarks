(define
  (domain x0001)
  (:requirements :strips :typing :action-costs)
  (:types x0250 x0267 x0269 x0313 x0290 - object x0293 x0254 - x0250 x0327 x0323 - x0267)
  (:predicates
    (x0315 ?v0002 - x0267)
    (x0251 ?v0002 - x0267)
    (x0345 ?v0002 - x0267 ?v0001 - x0250)
    (x0285 ?v0002 - x0267)
    (x0324 ?v0014 - x0323 ?v0010 - x0313)
    (x0255 ?v0002 - x0254 ?v0009 - x0293)
    (x0284 ?v0003 - x0269 ?v0009 - x0293)
    (x0322 ?v0014 - x0323)
    (x0314 ?v0011 ?v0012 - x0313)
    (x0256 ?v0002 - x0254 ?v0009 - x0293)
    (x0344 ?v0014 - x0323)
    (x0325 ?v0014 - x0323 ?v0010 - x0313)
    (x0291 ?v0006 - x0290)
    (x0292 ?v0006 - x0290 ?v0002 - x0267)
    (x0268 ?v0002 - x0267 ?v0001 - x0250))
  (:functions (x0343) - number)
  (:action x0316
    :parameters (?v0001 - x0250 ?v0003 - x0327 ?v0006 - x0290 ?v0014 - x0323 ?v0010 ?v0011 - x0313)
    :precondition (and (x0322 ?v0014) (x0268 ?v0014 ?v0001) (x0251 ?v0003) (x0314 ?v0011 ?v0010) (x0285 ?v0003) (x0292 ?v0006 ?v0014) (x0325 ?v0014 ?v0010))
    :effect (and (not (x0325 ?v0014 ?v0010)) (x0345 ?v0003 ?v0001) (increase (x0343) 1) (x0268 ?v0003 ?v0001) (not (x0285 ?v0003)) (x0325 ?v0014 ?v0011) (not (x0251 ?v0003))))
  (:action x0318
    :parameters (?v0014 - x0327 ?v0009 - x0293 ?v0003 - x0323 ?v0007 - x0290 ?v0010 ?v0011 - x0313)
    :precondition (and (x0268 ?v0014 ?v0009) (x0344 ?v0003) (x0292 ?v0007 ?v0014) (x0314 ?v0010 ?v0011) (x0325 ?v0003 ?v0010))
    :effect (and (x0268 ?v0003 ?v0009) (not (x0325 ?v0003 ?v0010)) (x0325 ?v0003 ?v0011) (increase (x0343) 1) (x0285 ?v0014) (not (x0268 ?v0014 ?v0009))))
  (:action x0253
    :parameters (?v0014 - x0327 ?v0001 - x0250 ?v0007 ?v0008 - x0290)
    :precondition (and (x0292 ?v0007 ?v0014) (x0285 ?v0014) (x0345 ?v0014 ?v0001) (x0291 ?v0008))
    :effect (and (increase (x0343) 1) (x0251 ?v0014) (not (x0345 ?v0014 ?v0001))))
  (:action x0287
    :parameters (?v0006 - x0290 ?v0013 - x0327 ?v0001 - x0250)
    :precondition (and (x0268 ?v0013 ?v0001) (x0292 ?v0006 ?v0013))
    :effect (and (x0285 ?v0013) (increase (x0343) 1) (not (x0268 ?v0013 ?v0001))))
  (:action x0321
    :parameters (?v0001 - x0254 ?v0004 ?v0005 - x0293 ?v0014 - x0323 ?v0007 ?v0008 - x0290)
    :precondition (and (x0256 ?v0001 ?v0005) (x0344 ?v0014) (x0268 ?v0014 ?v0005) (x0255 ?v0001 ?v0004) (x0292 ?v0007 ?v0014) (x0268 ?v0014 ?v0004) (x0291 ?v0008))
    :effect (and (x0322 ?v0014) (not (x0268 ?v0014 ?v0004)) (increase (x0343) 1) (x0268 ?v0014 ?v0001) (not (x0268 ?v0014 ?v0005)) (not (x0344 ?v0014))))
  (:action x0289
    :parameters (?v0006 - x0290 ?v0002 - x0267)
    :precondition (and (x0291 ?v0006) (x0315 ?v0002))
    :effect (and (not (x0291 ?v0006)) (not (x0315 ?v0002)) (increase (x0343) 1) (x0292 ?v0006 ?v0002)))
  (:action x0286
    :parameters (?v0006 - x0290 ?v0014 - x0323 ?v0001 - x0254 ?v0010 ?v0011 - x0313)
    :precondition (and (x0322 ?v0014) (x0324 ?v0014 ?v0011) (x0268 ?v0014 ?v0001) (x0292 ?v0006 ?v0014) (x0325 ?v0014 ?v0010))
    :effect (and (not (x0325 ?v0014 ?v0010)) (increase (x0343) 1) (x0285 ?v0014) (x0325 ?v0014 ?v0011) (not (x0322 ?v0014)) (not (x0268 ?v0014 ?v0001))))
  (:action x0288
    :parameters (?v0014 - x0327 ?v0009 - x0293 ?v0007 ?v0008 - x0290 ?v0003 - x0269)
    :precondition (and (x0284 ?v0003 ?v0009) (x0292 ?v0007 ?v0014) (x0285 ?v0014) (x0251 ?v0014) (x0291 ?v0008))
    :effect (and (not (x0285 ?v0014)) (x0268 ?v0014 ?v0009) (not (x0251 ?v0014)) (increase (x0343) 10) (x0345 ?v0014 ?v0009)))
  (:action x0317
    :parameters (?v0014 - x0327 ?v0009 - x0293 ?v0003 - x0323 ?v0007 - x0290 ?v0010 ?v0011 - x0313)
    :precondition (and (x0268 ?v0014 ?v0009) (x0292 ?v0007 ?v0014) (x0314 ?v0010 ?v0011) (x0251 ?v0003) (x0325 ?v0003 ?v0010) (x0285 ?v0003))
    :effect (and (x0268 ?v0003 ?v0009) (not (x0325 ?v0003 ?v0010)) (x0325 ?v0003 ?v0011) (increase (x0343) 1) (x0344 ?v0003) (x0285 ?v0014) (not (x0285 ?v0003)) (not (x0268 ?v0014 ?v0009)) (not (x0251 ?v0003))))
  (:action x0311
    :parameters (?v0006 - x0290 ?v0002 - x0267)
    :precondition (x0292 ?v0006 ?v0002)
    :effect (and (x0291 ?v0006) (x0315 ?v0002) (increase (x0343) 1) (not (x0292 ?v0006 ?v0002))))
  (:action x0252
    :parameters (?v0007 ?v0008 - x0290 ?v0014 - x0323)
    :precondition (and (x0292 ?v0007 ?v0014) (x0285 ?v0014) (x0291 ?v0008))
    :effect (and (increase (x0343) 1) (x0251 ?v0014)))
  (:action x0319
    :parameters (?v0014 - x0327 ?v0009 - x0293 ?v0007 ?v0008 - x0290 ?v0003 - x0269)
    :precondition (and (x0284 ?v0003 ?v0009) (x0292 ?v0007 ?v0014) (x0285 ?v0014) (x0345 ?v0014 ?v0009) (x0291 ?v0008))
    :effect (and (not (x0285 ?v0014)) (x0268 ?v0014 ?v0009) (increase (x0343) 10))))
