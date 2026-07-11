(define (problem satellite-s2-i2-m3-t2-o3)
  (:domain satellite)
  (:objects
    satellite0 satellite1 - satellite
    instrument0 instrument1 - instrument
    infrared0 image1 spectrograph2 - mode
    target0 target1 observation0 observation1 observation2 - direction
  )
  (:init
    (power_avail satellite0)
    (pointing satellite0 target0)
    (power_avail satellite1)
    (pointing satellite1 observation2)
    (on_board instrument0 satellite0)
    (calibration_target instrument0 target0)
    (supports instrument0 image1)
    (supports instrument0 infrared0)
    (on_board instrument1 satellite1)
    (calibration_target instrument1 target1)
    (supports instrument1 image1)
  )
  (:goal
    (and
      (have_image observation0 image1)
      (have_image observation1 image1)
      (have_image observation2 infrared0)
    )
  )
)
