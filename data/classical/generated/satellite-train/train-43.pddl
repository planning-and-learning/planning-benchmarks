(define (problem satellite-s1-i2-m2-t1-o3-p25)
  (:domain satellite)
  (:objects
    satellite0 - satellite
    instrument0 instrument1 - instrument
    infrared0 image1 - mode
    target0 observation0 observation1 observation2 - direction
  )
  (:init
    (power_avail satellite0)
    (pointing satellite0 observation0)
    (on_board instrument0 satellite0)
    (calibration_target instrument0 target0)
    (supports instrument0 infrared0)
    (on_board instrument1 satellite0)
    (calibration_target instrument1 target0)
    (supports instrument1 image1)
    (supports instrument1 infrared0)
  )
  (:goal
    (and
      (have_image observation0 infrared0)
      (have_image observation1 image1)
      (have_image observation2 infrared0)
      (pointing satellite0 observation1)
    )
  )
)
