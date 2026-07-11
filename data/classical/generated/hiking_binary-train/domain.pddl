; Binary-partner variant of the IPC Hiking domain.

(define (domain hiking-binary)
  (:requirements :strips :equality :typing :negative-preconditions)
  (:types car tent person couple place)
  (:predicates
    (at_tent ?tent - tent ?place - place)
    (at_person ?person - person ?place - place)
    (at_car ?car - car ?place - place)
    (partner_of ?couple - couple ?person - person)
    (up ?tent - tent)
    (down ?tent - tent)
    (walked ?couple - couple ?place - place)
    (next ?from - place ?to - place)
  )

  (:action put_down
    :parameters (?person - person ?place - place ?tent - tent)
    :precondition (and
      (at_person ?person ?place)
      (at_tent ?tent ?place)
      (up ?tent)
    )
    :effect (and
      (down ?tent)
      (not (up ?tent))
    )
  )

  (:action put_up
    :parameters (?person - person ?place - place ?tent - tent)
    :precondition (and
      (at_person ?person ?place)
      (at_tent ?tent ?place)
      (down ?tent)
    )
    :effect (and
      (up ?tent)
      (not (down ?tent))
    )
  )

  (:action drive_passenger
    :parameters (?driver - person ?from - place ?to - place ?car - car ?passenger - person)
    :precondition (and
      (at_person ?driver ?from)
      (at_car ?car ?from)
      (at_person ?passenger ?from)
      (not (= ?driver ?passenger))
    )
    :effect (and
      (at_person ?driver ?to)
      (not (at_person ?driver ?from))
      (at_car ?car ?to)
      (not (at_car ?car ?from))
      (at_person ?passenger ?to)
      (not (at_person ?passenger ?from))
    )
  )

  (:action drive
    :parameters (?person - person ?from - place ?to - place ?car - car)
    :precondition (and
      (at_person ?person ?from)
      (at_car ?car ?from)
    )
    :effect (and
      (at_person ?person ?to)
      (not (at_person ?person ?from))
      (at_car ?car ?to)
      (not (at_car ?car ?from))
    )
  )

  (:action drive_tent
    :parameters (?person - person ?from - place ?to - place ?car - car ?tent - tent)
    :precondition (and
      (at_person ?person ?from)
      (at_car ?car ?from)
      (at_tent ?tent ?from)
      (down ?tent)
    )
    :effect (and
      (at_person ?person ?to)
      (not (at_person ?person ?from))
      (at_car ?car ?to)
      (not (at_car ?car ?from))
      (at_tent ?tent ?to)
      (not (at_tent ?tent ?from))
    )
  )

  (:action drive_tent_passenger
    :parameters (?driver - person ?from - place ?to - place ?car - car ?tent - tent ?passenger - person)
    :precondition (and
      (at_person ?driver ?from)
      (at_car ?car ?from)
      (at_tent ?tent ?from)
      (down ?tent)
      (at_person ?passenger ?from)
      (not (= ?driver ?passenger))
    )
    :effect (and
      (at_person ?driver ?to)
      (not (at_person ?driver ?from))
      (at_car ?car ?to)
      (not (at_car ?car ?from))
      (at_tent ?tent ?to)
      (not (at_tent ?tent ?from))
      (at_person ?passenger ?to)
      (not (at_person ?passenger ?from))
    )
  )

  (:action walk_together
    :parameters (?tent - tent ?to - place ?person1 - person ?from - place ?person2 - person ?couple - couple)
    :precondition (and
      (at_tent ?tent ?to)
      (up ?tent)
      (at_person ?person1 ?from)
      (next ?from ?to)
      (at_person ?person2 ?from)
      (not (= ?person1 ?person2))
      (walked ?couple ?from)
      (partner_of ?couple ?person1)
      (partner_of ?couple ?person2)
    )
    :effect (and
      (at_person ?person1 ?to)
      (not (at_person ?person1 ?from))
      (at_person ?person2 ?to)
      (not (at_person ?person2 ?from))
      (walked ?couple ?to)
      (not (walked ?couple ?from))
    )
  )
)
