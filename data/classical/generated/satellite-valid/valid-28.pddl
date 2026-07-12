(define (problem satellite-s3-i5-m3-t3-o5-p25)
  (:domain satellite)
  (:objects
    satellite0 satellite1 satellite2 - satellite
    instrument0 instrument1 instrument2 instrument3 instrument4 - instrument
    infrared0 image1 spectrograph2 - mode
    target0 target1 target2 observation0 observation1 observation2 observation3 observation4 - direction
  )
  (:init
    (power_avail satellite0)
    (pointing satellite0 observation0)
    (power_avail satellite1)
    (pointing satellite1 observation0)
    (power_avail satellite2)
    (pointing satellite2 observation0)
    (on_board instrument0 satellite0)
    (calibration_target instrument0 target0)
    (supports instrument0 image1)
    (supports instrument0 infrared0)
    (on_board instrument1 satellite1)
    (calibration_target instrument1 target1)
    (supports instrument1 image1)
    (supports instrument1 spectrograph2)
    (on_board instrument2 satellite2)
    (calibration_target instrument2 target2)
    (supports instrument2 spectrograph2)
    (on_board instrument3 satellite0)
    (calibration_target instrument3 target0)
    (supports instrument3 infrared0)
    (supports instrument3 spectrograph2)
    (on_board instrument4 satellite1)
    (calibration_target instrument4 target1)
    (supports instrument4 image1)
  )
  (:goal
    (and
      (have_image observation0 image1)
      (have_image observation1 image1)
      (have_image observation2 spectrograph2)
      (have_image observation3 spectrograph2)
      (have_image observation4 image1)
    )
  )
)
