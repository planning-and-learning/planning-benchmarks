(define (problem satellite-s2-i3-m2-t2-o1)
  (:domain satellite)
  (:objects
    satellite0 satellite1 - satellite
    instrument0 instrument1 instrument2 - instrument
    infrared0 image1 - mode
    target0 target1 observation0 - direction
  )
  (:init
    (power_avail satellite0)
    (pointing satellite0 target0)
    (power_avail satellite1)
    (pointing satellite1 observation0)
    (on_board instrument0 satellite0)
    (calibration_target instrument0 target0)
    (supports instrument0 image1)
    (supports instrument0 infrared0)
    (on_board instrument1 satellite1)
    (calibration_target instrument1 target1)
    (supports instrument1 image1)
    (on_board instrument2 satellite0)
    (calibration_target instrument2 target0)
    (supports instrument2 image1)
    (supports instrument2 infrared0)
  )
  (:goal
    (and
      (have_image observation0 infrared0)
    )
  )
)
