(define (problem miconic-f1-p6)
  (:domain miconic)
  (:objects
    p0 p1 p2 p3 p4 p5 - passenger
    f0 - floor
  )
  (:init
    (origin p0 f0)
    (destin p0 f0)
    (origin p1 f0)
    (destin p1 f0)
    (origin p2 f0)
    (destin p2 f0)
    (origin p3 f0)
    (destin p3 f0)
    (origin p4 f0)
    (destin p4 f0)
    (origin p5 f0)
    (destin p5 f0)
    (lift-at f0)
  )
  (:goal
    (and
      (served p0)
      (served p1)
      (served p2)
      (served p3)
      (served p4)
      (served p5)
    )
  )
)
