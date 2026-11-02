language 1;
distribution satellite;
revision "2";
metadata {
    probability "Uniform pointings, instrument owners, and calibration targets; two independent uniform mode draws merged into a set; uniform instrument and supported mode for each observation; independent Bernoulli different-pointing goals.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(num_satellites,num_instruments,num_modes,num_targets,num_observations)=(1,1,1,1,1); pointing probability boundaries"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_satellites: int;
param num_instruments: int;
param num_modes: int;
param num_targets: int;
param num_observations: int;
param pointing_goal_probability: float = 0.0;

require valid_counts: num_satellites >= 1 and num_instruments >= 1 and num_modes >= 1 and num_targets >= 1 and num_observations >= 1;
require valid_probability: pointing_goal_probability >= 0 and pointing_goal_probability <= 1;
let Satellites = names("satellite", num_satellites);
let Instruments = names("instrument", num_instruments);
let Labels = ["infrared", "image", "spectrograph", "thermograph"];
let Mode[i in range(num_modes)] = Labels[i % 4] + str(i);
let Modes = values(Mode);
let Targets = names("target", num_targets);
let Observations = names("observation", num_observations);
let Directions = Targets + Observations;
objects Satellites: satellite;
objects Instruments: instrument;
objects Modes: mode;
objects Directions: direction;
relation initial.power_avail(Satellites);
relation initial.pointing(Satellites, Directions);
relation initial.on_board(Instruments, Satellites);
relation initial.calibration_target(Instruments, Targets);
relation initial.supports(Instruments, Modes);
relation goal.have_image(Observations, Modes);
relation goal.pointing(Satellites, Directions);
initial {
 rule available_power: forall s in Satellites: initial.power_avail(s);
 rule pointing: forall s in Satellites: count(d in Directions: initial.pointing(s,d)) == 1;
 rule owner: forall i in Instruments: count(s in Satellites: initial.on_board(i,s)) == 1;
 rule calibration: forall i in Instruments: count(t in Targets: initial.calibration_target(i,t)) == 1;
 rule supported_modes: forall i in Instruments: count(m in Modes: initial.supports(i,m)) >= 1 and count(m in Modes: initial.supports(i,m)) <= 2;
}
goal {
 rule requested_images: forall o in Observations: count(m in Modes: goal.have_image(o,m)) == 1;
 rule partial_pointing: forall s in Satellites: count(d in Directions: goal.pointing(s,d)) <= 1;
 rule pointing_endpoints: forall s in Satellites: if pointing_goal_probability == 0 then count(d in Directions: goal.pointing(s,d)) == 0 else if pointing_goal_probability == 1 then count(d in Directions: goal.pointing(s,d)) == 1 else true;
}
joint {
 rule observable: forall o in Observations, m in Modes: goal.have_image(o,m) implies (exists i in Instruments: initial.supports(i,m));
 rule different_pointing: forall s in Satellites, d in Directions: goal.pointing(s,d) implies not initial.pointing(s,d);
}
