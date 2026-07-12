(define (problem satellite-s1-i1-m3-t2-o3-p50)
  (:domain satellite)
  (:objects
    satellite0 - satellite
    instrument0 - instrument
    infrared0 image1 spectrograph2 - mode
    target0 target1 observation0 observation1 observation2 - direction
  )
  (:init
    (power_avail satellite0)
    (pointing satellite0 observation0)
    (on_board instrument0 satellite0)
    (calibration_target instrument0 target0)
    (supports instrument0 infrared0)
    (supports instrument0 spectrograph2)
  )
  (:goal
    (and
      (have_image observation0 spectrograph2)
      (have_image observation1 spectrograph2)
      (have_image observation2 spectrograph2)
    )
  )
)
