(define (problem miconic-f1-p2)
  (:domain miconic)
  (:objects
    p0 p1 - passenger
    f0 - floor
  )
  (:init
    (origin p0 f0)
    (destin p0 f0)
    (origin p1 f0)
    (destin p1 f0)
    (lift-at f0)
  )
  (:goal
    (and
      (served p0)
      (served p1)
    )
  )
)
