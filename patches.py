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
