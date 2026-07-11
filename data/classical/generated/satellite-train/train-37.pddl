(define (problem satellite-s2-i1-m2-t1-o1)
  (:domain satellite)
  (:objects
    satellite0 satellite1 - satellite
    instrument0 - instrument
    infrared0 image1 - mode
    target0 observation0 - direction
  )
  (:init
    (power_avail satellite0)
    (pointing satellite0 target0)
    (power_avail satellite1)
    (pointing satellite1 target0)
    (on_board instrument0 satellite0)
    (calibration_target instrument0 target0)
    (supports instrument0 image1)
    (supports instrument0 infrared0)
  )
  (:goal
    (and
      (have_image observation0 infrared0)
    )
  )
)
