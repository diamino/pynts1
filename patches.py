from nts1 import (NTS1Patch,
                  OscillatorType,
                  FilterType,
                  EnvelopeType,
                  DelayType,
                  ReverbType)

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
