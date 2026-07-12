(define (domain fuel)
    (:requirements :strips :numeric-fluents)

    (:functions
        (fuel) ; amount of fuel
    )

    (:action refuel
        :parameters ()
        :precondition ()
        :effect (increase (fuel) 1)
    )
)
