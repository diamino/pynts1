'''
PyNTS1

Simple python module to send patches to the Nu:Tekt NTS-1 (MK1)

Diamino 2024
'''
from dataclasses import dataclass
from enum import Enum
import mido

INPORT_NAME = 'NTS-1 digital kit KBD/KNOB'
OUTPORT_NAME = 'NTS-1 digital kit SOUND'

inport = mido.open_input(INPORT_NAME)
outport = mido.open_output(OUTPORT_NAME)


class Controls(Enum):
    EG_TYPE = 14
    EG_ATTACK = 16
    EG_RELEASE = 19
    TREMOLO_DEPTH = 20
    TREMOLO_RATE = 21
    LFO_RATE = 24
    LFO_DEPTH = 26
    MOD_TIME = 28
    MOD_DEPTH = 29
    DELAY_TIME = 30
    DELAY_DEPTH = 31
    DELAY_MIX = 33
    REVERB_TIME = 34
    REVERB_DEPTH = 35
    REVERB_MIX = 36
    FILTER_TYPE = 42
    FILTER_CUTOFF = 43
    FILTER_RESONANCE = 44
    FILTER_SWEEP_DEPTH = 45
    FILTER_SWEEP_RATE = 46
    OSC_TYPE = 53
    OSC_SHAPE = 54
    OSC_ALT = 55
    MOD_TYPE = 88
    DELAY_TYPE = 89
    REVERB_TYPE = 90
    ARP_PATTERN = 117
    ARP_INTERVALS = 118
    ARP_LENGTH = 119
    ALL_NOTE_OFF = 123


class OscillatorType(Enum):
    # OSCILLATOR TYPE:SAW, TRI, SQR, VPM, WAVES = vv:0,25,50,75,100
    SAW = 0
    TRI = 25
    SQR = 50
    VPM = 75
    WAVES = 100


class FilterType(Enum):
    # FILTER TYPE:LP2, LP4, BP2, BP4, HP2, HP4, OFF = vv:0,18,36,54,72,90,108
    LP2 = 0
    LP4 = 18
    BP2 = 36
    BP4 = 54
    HP2 = 72
    HP4 = 90
    OFF = 108


class EnvelopeType(Enum):
    # EG TYPE:ADSR, AHR, AR, AR LOOP, OPEN = vv:0,25,50,75,100
    ADSR = 0
    AHR = 25
    AR = 50
    AR_LOOP = 75
    OPEN = 100


class ModType(Enum):
    # MOD FX TYPE:OFF, CHORUS, ENSEMBLE, PHASER, FLANGER = vv:0,25,50,75,100
    OFF = 0
    CHORUS = 25
    ENSEMBLE = 50
    PHASER = 75
    FLANGER = 100


class DelayType(Enum):
    # DELAY FX TYPE:OFF, STEREO, MONO, PING PONG, HIGHPASS, TAPE = vv:0,21,42,63,84,105
    OFF = 0
    STEREO = 21
    MONO = 42
    PING_PONG = 63
    HIGHPASS = 84
    TAPE = 105


class ReverbType(Enum):
    # REVERB FX TYPE:OFF, HALL, PLATE, SPACE, RISER, SUBMARINE = vv:0,21,42,63,84,105
    OFF = 0
    HALL = 21
    PLATE = 42
    SPACE = 63
    RISER = 84
    SUBMARINE = 105


@dataclass
class NTS1Patch:
    osc_type: OscillatorType = OscillatorType.SAW
    osc_shape: int = 0   # 0 - 100
    osc_alt: int = 0     # 0 - 100
    lfo_rate: float = 0  # 0.0 - 30.0
    lfo_depth: int = 0   # -100(P) - 100(S)
    filter_type: FilterType = FilterType.OFF
    filter_cutoff: int = 0          # 0 - 100
    filter_resonance: int = 0       # 0 - 100
    filter_sweep_rate: float = 0    # 0.0 - 30.0
    filter_sweep_depth: int = 0     # -100(U) - 100(D)
    eg_type: EnvelopeType = EnvelopeType.ADSR
    eg_attack: int = 0          # 0 - 100
    eg_release: int = 0         # 0 - 100
    tremolo_rate: float = 0     # 0.0 - 60.0
    tremolo_depth: int = 0      # 0 - 100(D)
    mod_type: ModType = ModType.OFF
    mod_time: int = 0       # 0 - 100
    mod_depth: int = 0      # 0 - 100
    delay_type: DelayType = DelayType.OFF
    delay_time: int = 0     # 0 - 100
    delay_depth: int = 0    # 0 - 100
    delay_mix: int = 0      # -100(D) - 100(W)
    reverb_type: ReverbType = ReverbType.OFF
    reverb_time: int = 0    # 0 - 100
    reverb_depth: int = 0   # 0 - 100
    reverb_mix: int = 0     # -100(D) - 100(W)


def send_control_value(control: Controls, value: int) -> None:
    msg = mido.Message('control_change', control=control.value, value=value)
    outport.send(msg)


def rate_non_linear(value: float) -> int:
    if value >= 3.0:
        return int(value*2.3+58)
    else:
        return int(value*24.5)


def rate_none_linear2(value: float) -> int:
    if value >= 9.5:
        return int(value*1.26+51.5)
    else:
        return int(value*6.8)


def send_patch(patch: NTS1Patch) -> None:
    send_control_value(Controls.OSC_TYPE, patch.osc_type.value)
    send_control_value(Controls.OSC_SHAPE, int(patch.osc_shape*1.27))
    send_control_value(Controls.OSC_ALT, int(patch.osc_alt*1.27))
    send_control_value(Controls.LFO_RATE, rate_non_linear(patch.lfo_rate))
    send_control_value(Controls.LFO_DEPTH, int((patch.lfo_depth+100)*0.635))
    send_control_value(Controls.FILTER_TYPE, patch.filter_type.value)
    send_control_value(Controls.FILTER_CUTOFF, int(patch.filter_cutoff*1.27))
    send_control_value(Controls.FILTER_RESONANCE, int(patch.filter_resonance*1.27))
    send_control_value(Controls.FILTER_SWEEP_RATE, rate_non_linear(patch.filter_sweep_rate))
    send_control_value(Controls.FILTER_SWEEP_DEPTH, int((patch.filter_sweep_depth+100)*0.635))
    send_control_value(Controls.EG_TYPE, patch.eg_type.value)
    send_control_value(Controls.EG_ATTACK, int(patch.eg_attack*1.27))
    send_control_value(Controls.EG_RELEASE, int(patch.eg_release*1.27))
    send_control_value(Controls.TREMOLO_RATE, rate_none_linear2(patch.tremolo_rate))
    send_control_value(Controls.TREMOLO_DEPTH, int(patch.tremolo_depth*1.27))
    send_control_value(Controls.MOD_TYPE, patch.mod_type.value)
    send_control_value(Controls.MOD_TIME, int(patch.mod_time*1.27))
    send_control_value(Controls.MOD_DEPTH, int(patch.mod_depth*1.27))
    send_control_value(Controls.DELAY_TYPE, patch.delay_type.value)
    send_control_value(Controls.DELAY_TIME, int(patch.delay_time*1.27))
    send_control_value(Controls.DELAY_DEPTH, int(patch.delay_depth*1.27))
    send_control_value(Controls.DELAY_MIX, int((patch.delay_mix+100)*0.635))
    send_control_value(Controls.REVERB_TYPE, patch.reverb_type.value)
    send_control_value(Controls.REVERB_TIME, int(patch.reverb_time*1.27))
    send_control_value(Controls.REVERB_DEPTH, int(patch.reverb_depth*1.27))
    send_control_value(Controls.REVERB_MIX, int((patch.reverb_mix+100)*0.635))


def main() -> None:

    from patches import milk_bottles
    send_patch(milk_bottles)


if __name__ == '__main__':
    main()
