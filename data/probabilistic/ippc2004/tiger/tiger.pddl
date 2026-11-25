(define (problem tiger-problem)
  (:domain tiger-domain)
  (:init (probabilistic 0.5 (tiger-on-left)))
  (:metric maximize (reward)))
