(define (domain slippery-gripper)
  (:requirements :strips :conditional-effects :negative-preconditions :probabilistic-effects)
  (:predicates (gripper-dry) (holding-block))
  (:action pickup
	   :effect (and (when (gripper-dry)
			  (probabilistic 0.95 (holding-block)))
			(when (not (gripper-dry))
			  (probabilistic 0.5 (holding-block)))))
  (:action dry
	   :effect (probabilistic 0.8 (gripper-dry))))
