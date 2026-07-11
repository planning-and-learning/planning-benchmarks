(define (problem miconic-f4-p1)
  (:domain miconic)
  (:objects
    p0 - passenger
    f0 f1 f2 f3 - floor
  )
  (:init
    (above f0 f1)
    (above f0 f2)
    (above f0 f3)
    (above f1 f2)
    (above f1 f3)
    (above f2 f3)
    (origin p0 f2)
    (destin p0 f1)
    (lift-at f0)
  )
  (:goal
    (and
      (served p0)
    )
  )
)
