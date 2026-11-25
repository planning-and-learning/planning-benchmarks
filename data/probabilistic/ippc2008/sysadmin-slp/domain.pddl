(define (domain sysadmin-slp)

 (:requirements :strips :conditional-effects :equality :existential-preconditions :negative-preconditions :probabilistic-effects :rewards :typing :universal-preconditions)
 (:types comp)

 (:predicates (up ?c)
              (conn ?c ?d))

;; Note: MDPSim performs an action by going down its effect tree,
;; storing adds and dels (of terms) and updates (of values). The
;; "reboot" action has been modified to prevent the term (up ?x) from
;; being in both the adds and dels lists.
;; All tests are based on old terms and values (which is good). Terms
;; and values are updated only after the "action tree" has been
;; processed. As a result, no chain reaction can take place.
(:action reboot
  :parameters (?x - comp)
  :effect (and (forall (?d - comp)
		       (when (up ?d)
			 (increase (reward) 1)
			 )
		       )
               (probabilistic 0.9 (up ?x))
               (forall (?d - comp)
		       (and
			(probabilistic
			 0.2 (when (exists (?c - comp) (and (conn ?c ?d) (not (up ?c)) (not (= ?d ?x))))
			       (not (up ?d))
			       ))
			(probabilistic
			 0.05 (when (not (= ?d ?x))
				(not (up ?d))
			 ))
			)
		   )))
)
