(define (problem miconic-f3-p1)
  (:domain miconic)
  (:objects
    p0 - passenger
    f0 f1 f2 - floor
  )
  (:init
    (above f0 f1)
    (above f0 f2)
    (above f1 f2)
    (origin p0 f0)
    (destin p0 f1)
    (lift-at f0)
  )
  (:goal
    (and
      (served p0)
    )
  )
)
