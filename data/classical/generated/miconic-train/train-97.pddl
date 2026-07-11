(define (problem miconic-f5-p1)
  (:domain miconic)
  (:objects
    p0 - passenger
    f0 f1 f2 f3 f4 - floor
  )
  (:init
    (above f0 f1)
    (above f0 f2)
    (above f0 f3)
    (above f0 f4)
    (above f1 f2)
    (above f1 f3)
    (above f1 f4)
    (above f2 f3)
    (above f2 f4)
    (above f3 f4)
    (origin p0 f4)
    (destin p0 f0)
    (lift-at f0)
  )
  (:goal
    (and
      (served p0)
    )
  )
)
