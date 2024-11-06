from nts1 import (NTS1Patch,
                  OscillatorType,
                  FilterType,
                  EnvelopeType,
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
                         reverb_mix=0
                         )
