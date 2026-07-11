(define (problem miconic-f2-p3)
  (:domain miconic)
  (:objects
    p0 p1 p2 - passenger
    f0 f1 - floor
  )
  (:init
    (above f0 f1)
    (origin p0 f1)
    (destin p0 f0)
    (origin p1 f1)
    (destin p1 f0)
    (origin p2 f1)
    (destin p2 f0)
    (lift-at f0)
  )
  (:goal
    (and
      (served p0)
      (served p1)
      (served p2)
    )
  )
)
