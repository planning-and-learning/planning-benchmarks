(define (domain eaten-domain)
  (:requirements :strips :conditional-effects :negative-preconditions :probabilistic-effects)
  (:predicates (tiger-on-left) (hear-tiger-on-left) (eaten))
  (:action listen
	   :effect (and (when (tiger-on-left)
			  (probabilistic 0.85 (hear-tiger-on-left)
					 0.15 (not (hear-tiger-on-left))))
			(when (not (tiger-on-left))
			  (probabilistic 0.85 (not (hear-tiger-on-left))
					 0.15 (hear-tiger-on-left)))))
  (:action open-left-door
	   :effect (when (tiger-on-left)
			  (eaten)))
  (:action open-right-door
	   :effect (when (not (tiger-on-left))
			  (eaten))))
