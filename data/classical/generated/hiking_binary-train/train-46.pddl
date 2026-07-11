(define (problem hiking-binary-2-4-3)
  (:domain hiking-binary)
  (:objects
    car0 car1 car2 car3 - car
    tent0 tent1 - tent
    couple0 couple1 - couple
    place0 place1 place2 - place
    guy0 girl0 guy1 girl1 - person
  )
  (:init
    (partner_of couple0 guy0)
    (partner_of couple0 girl0)
    (at_person guy0 place0)
    (at_person girl0 place0)
    (walked couple0 place0)
    (at_tent tent0 place0)
    (down tent0)
    (partner_of couple1 guy1)
    (partner_of couple1 girl1)
    (at_person guy1 place0)
    (at_person girl1 place0)
    (walked couple1 place0)
    (at_tent tent1 place0)
    (up tent1)
    (at_car car0 place0)
    (at_car car1 place0)
    (at_car car2 place0)
    (at_car car3 place0)
    (next place0 place1)
    (next place1 place2)
  )
  (:goal
    (and
      (walked couple0 place2)
      (walked couple1 place2)
    )
  )
)
