(define (problem satellite-s2-i3-m3-t1-o2)
  (:domain satellite)
  (:objects
    satellite0 satellite1 - satellite
    instrument0 instrument1 instrument2 - instrument
    infrared0 image1 spectrograph2 - mode
    target0 observation0 observation1 - direction
  )
  (:init
    (power_avail satellite0)
    (pointing satellite0 observation1)
    (power_avail satellite1)
    (pointing satellite1 target0)
    (on_board instrument0 satellite0)
    (calibration_target instrument0 target0)
    (supports instrument0 infrared0)
    (supports instrument0 spectrograph2)
    (on_board instrument1 satellite1)
    (calibration_target instrument1 target0)
    (supports instrument1 image1)
    (on_board instrument2 satellite0)
    (calibration_target instrument2 target0)
    (supports instrument2 image1)
    (supports instrument2 spectrograph2)
  )
  (:goal
    (and
      (have_image observation0 infrared0)
      (have_image observation1 image1)
    )
  )
)
