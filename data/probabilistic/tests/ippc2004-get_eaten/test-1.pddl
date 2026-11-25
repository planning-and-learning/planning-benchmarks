(define (problem get-eaten)
  (:domain eaten-domain)
  (:init (probabilistic 0.5 (tiger-on-left)))
  (:goal (eaten)))
