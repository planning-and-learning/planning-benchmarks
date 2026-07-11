(define (problem satellite-s3-i4-m3-t4-o5)
  (:domain satellite)
  (:objects
    satellite0 satellite1 satellite2 - satellite
    instrument0 instrument1 instrument2 instrument3 - instrument
    infrared0 image1 spectrograph2 - mode
    target0 target1 target2 target3 observation0 observation1 observation2 observation3 observation4 - direction
  )
  (:init
    (power_avail satellite0)
    (pointing satellite0 observation1)
    (power_avail satellite1)
    (pointing satellite1 observation1)
    (power_avail satellite2)
    (pointing satellite2 target0)
    (on_board instrument0 satellite0)
    (calibration_target instrument0 target0)
    (supports instrument0 image1)
    (supports instrument0 infrared0)
    (on_board instrument1 satellite1)
    (calibration_target instrument1 target1)
    (supports instrument1 image1)
    (on_board instrument2 satellite2)
    (calibration_target instrument2 target2)
    (supports instrument2 spectrograph2)
    (on_board instrument3 satellite0)
    (calibration_target instrument3 target3)
    (supports instrument3 image1)
    (supports instrument3 infrared0)
  )
  (:goal
    (and
      (have_image observation0 image1)
      (have_image observation1 image1)
      (have_image observation2 spectrograph2)
      (have_image observation3 infrared0)
      (have_image observation4 infrared0)
    )
  )
)
