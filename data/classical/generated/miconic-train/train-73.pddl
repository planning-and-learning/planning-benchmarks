(define (problem miconic-f1-p1)
  (:domain miconic)
  (:objects
    p0 - passenger
    f0 - floor
  )
  (:init
    (origin p0 f0)
    (destin p0 f0)
    (lift-at f0)
  )
  (:goal
    (and
      (served p0)
    )
  )
)
