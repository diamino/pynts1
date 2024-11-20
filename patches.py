from nts1 import (NTS1Patch,
                  OscillatorType,
                  FilterType,
                  EnvelopeType,
                  ModType,
                  DelayType,
                  ReverbType,
                  ArpType,
                  ArpChord)

# Ice Storm patch by ChrisLody (https://youtu.be/pSlGfrfRvxw)
ice_storm = NTS1Patch(osc_type=OscillatorType.TRI,
                      osc_shape=0,
                      osc_alt=0,
                      filter_type=FilterType.LP4,
                      filter_cutoff=0,
                      filter_resonance=100,
                      filter_sweep_rate=30.0,
                      filter_sweep_depth=-100,  # U100
                      eg_type=EnvelopeType.AHR,
                      eg_attack=0,
                      eg_release=100,
                      reverb_type=ReverbType.RISER,
                      reverb_time=60,
                      reverb_depth=50,
                      reverb_mix=100,
                      arp_type=ArpType.RAND,
                      arp_length=4,
                      arp_chord=ArpChord.OCT)

# I'll Be Bach patch by ChrisLody (https://youtu.be/pSlGfrfRvxw)
#   Notes: Set Legato (Igt) in the Global options to off (0) for the best results
i_ll_be_bach = NTS1Patch(osc_type=OscillatorType.SQR,
                         osc_shape=75,
                         osc_alt=0,
                         filter_type=FilterType.LP2,
                         filter_cutoff=40,
                         filter_resonance=25,
                         filter_sweep_rate=2.5,
                         filter_sweep_depth=50,
                         eg_type=EnvelopeType.AR,
                         eg_attack=0,
                         eg_release=60,
                         reverb_type=ReverbType.HALL,
                         reverb_time=40,
                         reverb_depth=40)

# Kinda Stringy patch by ChrisLody (https://youtu.be/pSlGfrfRvxw)
kinda_stringy = NTS1Patch(osc_type=OscillatorType.SAW,
                          osc_shape=0,
                          osc_alt=0,
                          filter_type=FilterType.BP2,
                          filter_cutoff=25,
                          filter_resonance=25,
                          eg_type=EnvelopeType.AR,
                          eg_attack=100,
                          eg_release=100,
                          mod_type=ModType.ENSEMBLE,
                          mod_time=50,
                          mod_depth=75,
                          reverb_type=ReverbType.SUBMARINE,
                          reverb_time=60,
                          reverb_depth=60)

# Massive Monks patch by ChrisLody (https://youtu.be/pSlGfrfRvxw)
#   Notes: Tweak VPM Shape a lot, Tweak VPM Alt a little. The VPM Alt knob has
#          audible notches, notches 1 and 2 sound most voice like
massive_monks = NTS1Patch(osc_type=OscillatorType.VPM,
                          osc_shape=30,
                          osc_alt=5,
                          filter_type=FilterType.LP2,
                          filter_cutoff=100,
                          filter_resonance=0,
                          eg_type=EnvelopeType.ADSR,
                          eg_attack=100,
                          eg_release=100,
                          mod_type=ModType.ENSEMBLE,
                          mod_time=50,
                          mod_depth=100,
                          reverb_type=ReverbType.RISER,
                          reverb_time=50,
                          reverb_depth=100)

# Milk Bottles patch by ChrisLody (https://youtu.be/pSlGfrfRvxw)
milk_bottles = NTS1Patch(osc_type=OscillatorType.TRI,
                         osc_shape=50,
                         osc_alt=0,
                         filter_type=FilterType.LP2,
                         filter_cutoff=20,
                         filter_resonance=50,
                         filter_sweep_rate=2.2,
                         filter_sweep_depth=28,  # D28
                         eg_type=EnvelopeType.AR,
                         eg_attack=0,
                         eg_release=60,
                         delay_type=DelayType.TAPE,
                         delay_time=50,
                         delay_depth=40,
                         delay_mix=0,
                         reverb_type=ReverbType.HALL,
                         reverb_time=40,
                         reverb_depth=40,
                         reverb_mix=0)

# Planet B Movie patch by ChrisLody (https://youtu.be/pSlGfrfRvxw)
planet_b_movie = NTS1Patch(osc_type=OscillatorType.VPM,
                           osc_shape=0,
                           osc_alt=5,
                           filter_type=FilterType.BP2,
                           filter_cutoff=0,
                           filter_resonance=100,
                           filter_sweep_rate=0.3,
                           filter_sweep_depth=100,
                           eg_type=EnvelopeType.AR_LOOP,
                           eg_attack=15,  # Original setting is 25
                           eg_release=25,
                           delay_type=DelayType.PING_PONG,
                           delay_time=20,
                           delay_depth=100)

# Seesicksty Four patch by ChrisLody (https://youtu.be/pSlGfrfRvxw)
seesicksty_four = NTS1Patch(osc_type=OscillatorType.SQR,
                            osc_shape=50,
                            osc_alt=0,
                            lfo_rate=1.8,
                            lfo_depth=50,
                            eg_type=EnvelopeType.AR,
                            eg_attack=0,
                            eg_release=75,
                            delay_type=DelayType.PING_PONG,
                            delay_time=25,
                            delay_depth=30,
                            delay_mix=-30)

# Space Documentary patch by ChrisLody (https://youtu.be/pSlGfrfRvxw)
#   Notes: Tweak the Cutoff knob while the sequence plays for some interesting sounds.
space_documentary = NTS1Patch(osc_type=OscillatorType.SAW,
                              osc_shape=0,
                              osc_alt=50,
                              filter_type=FilterType.BP4,
                              filter_cutoff=25,
                              filter_resonance=0,
                              eg_type=EnvelopeType.AR,
                              eg_attack=25,
                              eg_release=60,
                              delay_type=DelayType.TAPE,
                              delay_time=30,
                              delay_depth=50,
                              reverb_type=ReverbType.PLATE,
                              reverb_time=60,
                              reverb_depth=100,
                              arp_type=ArpType.UP_DOWN,
                              arp_length=12,
                              arp_chord=ArpChord.SUS)

# Thick Syrup patch by ChrisLody (https://youtu.be/pSlGfrfRvxw)
thick_syrup = NTS1Patch(osc_type=OscillatorType.SAW,
                        osc_shape=25,
                        osc_alt=0,
                        filter_type=FilterType.LP4,
                        filter_cutoff=10,
                        filter_resonance=60,
                        filter_sweep_rate=2.0,
                        filter_sweep_depth=50,
                        eg_type=EnvelopeType.ADSR,
                        eg_attack=0,
                        eg_release=40,
                        mod_type=ModType.CHORUS,
                        mod_time=50,
                        mod_depth=50)
