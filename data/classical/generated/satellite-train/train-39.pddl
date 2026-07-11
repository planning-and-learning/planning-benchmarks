(define (problem satellite-s2-i1-m2-t1-o3)
  (:domain satellite)
  (:objects
    satellite0 satellite1 - satellite
    instrument0 - instrument
    infrared0 image1 - mode
    target0 observation0 observation1 observation2 - direction
  )
  (:init
    (power_avail satellite0)
    (pointing satellite0 target0)
    (power_avail satellite1)
    (pointing satellite1 observation1)
    (on_board instrument0 satellite0)
    (calibration_target instrument0 target0)
    (supports instrument0 infrared0)
  )
  (:goal
    (and
      (have_image observation0 infrared0)
      (have_image observation1 infrared0)
      (have_image observation2 infrared0)
    )
  )
)
