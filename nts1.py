'''
PyNTS1

Simple python module to send patches to the Nu:Tekt NTS-1 (MK1)

Diamino 2024
'''
from dataclasses import dataclass
from enum import Enum
import threading
import time
import mido

INPORT_NAME = 'NTS-1 digital kit KBD/KNOB'
OUTPORT_NAME = 'NTS-1 digital kit SOUND'

MODULE_SIZE = (16,  # MOD
               8,   # DELAY
               8,   # REVERB
               16)  # OSC


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
    TRI = 1
    SQR = 2
    VPM = 3
    WAVES = 4


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
    CHORUS = 1
    ENSEMBLE = 2
    PHASER = 3
    FLANGER = 4


class DelayType(Enum):
    # DELAY FX TYPE:OFF, STEREO, MONO, PING PONG, HIGHPASS, TAPE = vv:0,21,42,63,84,105
    OFF = 0
    STEREO = 1
    MONO = 2
    PING_PONG = 3
    HIGHPASS = 4
    TAPE = 5


class ReverbType(Enum):
    # REVERB FX TYPE:OFF, HALL, PLATE, SPACE, RISER, SUBMARINE = vv:0,21,42,63,84,105
    OFF = 0
    HALL = 1
    PLATE = 2
    SPACE = 3
    RISER = 4
    SUBMARINE = 5


class ArpType(Enum):
    # ARP PATTERN:UP, DOWN, UP-DOWN, DOWN-UP, CONV, DIV, CONV-DIV, DIV-CONV, RAND, STOCH
    #   = vv:0,12,24,36,48,60,72,84,96,108
    UP = 0
    DOWN = 12
    UP_DOWN = 24
    DOWN_UP = 36
    CONV = 48
    DIV = 60
    CONV_DIV = 72
    DIV_CONV = 84
    RAND = 96
    STOCH = 108


class ArpChord(Enum):
    # ARP INTERVALS:OCT, MAJ, SUS, AUG, MIN, DIM = vv:0,21,42,63,84,105
    OCT = 0
    MAJ = 21
    SUS = 42
    AUG = 63
    MIN = 84
    DIM = 105


class ModuleType(Enum):
    MOD = 1
    DELAY = 2
    REVERB = 3
    OSC = 4


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
    arp_type: ArpType = ArpType.UP
    arp_length: int = 1     # 1 - 24
    arp_chord: ArpChord = ArpChord.OCT


def rate_non_linear(value: float) -> int:
    if value >= 2.6:
        return int(value*2.3+58)
    else:
        return int(value*24.5)


def rate_non_linear2(value: float) -> int:
    if value >= 9.5:
        return int(value*1.26+51.5)
    else:
        return int(value*6.8)


class NTS1:

    def __init__(self, outport: mido.ports.BaseOutput, inport: mido.ports.BaseInput):
        self.outport = outport
        self.inport = inport
        self.slots = [0] * 4
        self.msg_received = threading.Event()

    def close(self):
        self.inport.close()
        self.outport.close()

    def receive_msg(self, msg: mido.Message) -> None:
        if msg.bytes()[0] != 248:  # Filter out clock messages
            # print(msg.bytes(), msg)
            self.msg_received.set()
        if msg.bytes()[0:6] == [0xF0, 0x42, 0x30, 0x00, 0x01, 0x57]:  # EXCLUSIVE HEADER
            if msg.bytes()[6] == 0x49:  # USER SLOT STATUS
                module_id = msg.bytes()[7]
                if module_id >= 1 and module_id <= 4:  # Valid module id
                    slot_id = msg.bytes()[8]
                    if slot_id >= 0 and slot_id < MODULE_SIZE[module_id - 1]:
                        if len(msg) >= 20:
                            self.slots[module_id - 1] |= 1 << slot_id
                        else:
                            self.slots[module_id - 1] &= ~(1 << slot_id)

    def send_user_slot_status_request(self, module_id: ModuleType, slot_id: int):
        msg = mido.Message('sysex', data=(0x42, 0x30, 0x00, 0x01, 0x57, 0x19, module_id.value, slot_id))
        self.outport.send(msg)

    def request_user_slots(self):
        if self.inport.callback is None:
            self.inport.callback = self.receive_msg
        for module_id in ModuleType:
            for slot_id in range(MODULE_SIZE[module_id.value - 1]):
                self.send_user_slot_status_request(module_id, slot_id)
                self.msg_received.wait(.1)
                self.msg_received.clear()
        time.sleep(.1)

    def num_slots_used(self, module_id: ModuleType):
        return self.slots[module_id.value - 1].bit_count()

    def osc_type_value(self, osc_type: OscillatorType):
        # One extra slot is subtracted because the WAVES oscillator occupies a user slot
        total_slots = len(OscillatorType) + self.num_slots_used(ModuleType.OSC) - 1
        return 127 * osc_type.value // total_slots

    def mod_type_value(self, mod_type: ModType):
        total_slots = len(ModType) + self.num_slots_used(ModuleType.MOD)
        return 127 * mod_type.value // total_slots

    def delay_type_value(self, delay_type: DelayType):
        total_slots = len(DelayType) + self.num_slots_used(ModuleType.DELAY)
        return 127 * delay_type.value // total_slots

    def reverb_type_value(self, reverb_type: ReverbType):
        total_slots = len(ReverbType) + self.num_slots_used(ModuleType.REVERB)
        return 127 * reverb_type.value // total_slots

    def send_control_value(self, control: Controls, value: int) -> None:
        msg = mido.Message('control_change', control=control.value, value=value)
        self.outport.send(msg)

    def send_patch(self, patch: NTS1Patch) -> None:
        self.send_control_value(Controls.OSC_TYPE, self.osc_type_value(patch.osc_type))
        self.send_control_value(Controls.OSC_SHAPE, int(patch.osc_shape*1.27))
        self.send_control_value(Controls.OSC_ALT, int(patch.osc_alt*1.27))
        self.send_control_value(Controls.LFO_RATE, rate_non_linear(patch.lfo_rate))
        self.send_control_value(Controls.LFO_DEPTH, int((patch.lfo_depth+100)*0.635))
        self.send_control_value(Controls.FILTER_TYPE, patch.filter_type.value)
        self.send_control_value(Controls.FILTER_CUTOFF, int(patch.filter_cutoff*1.27))
        self.send_control_value(Controls.FILTER_RESONANCE, int(patch.filter_resonance*1.27))
        self.send_control_value(Controls.FILTER_SWEEP_RATE, rate_non_linear(patch.filter_sweep_rate))
        self.send_control_value(Controls.FILTER_SWEEP_DEPTH, int((patch.filter_sweep_depth+100)*0.635))
        self.send_control_value(Controls.EG_TYPE, patch.eg_type.value)
        self.send_control_value(Controls.EG_ATTACK, int(patch.eg_attack*1.27))
        self.send_control_value(Controls.EG_RELEASE, int(patch.eg_release*1.27))
        self.send_control_value(Controls.TREMOLO_RATE, rate_non_linear2(patch.tremolo_rate))
        self.send_control_value(Controls.TREMOLO_DEPTH, int(patch.tremolo_depth*1.27))
        self.send_control_value(Controls.MOD_TYPE, self.mod_type_value(patch.mod_type))
        self.send_control_value(Controls.MOD_TIME, int(patch.mod_time*1.27))
        self.send_control_value(Controls.MOD_DEPTH, int(patch.mod_depth*1.27))
        self.send_control_value(Controls.DELAY_TYPE, self.delay_type_value(patch.delay_type))
        self.send_control_value(Controls.DELAY_TIME, int(patch.delay_time*1.27))
        self.send_control_value(Controls.DELAY_DEPTH, int(patch.delay_depth*1.27))
        self.send_control_value(Controls.DELAY_MIX, int((patch.delay_mix+100)*0.635))
        self.send_control_value(Controls.REVERB_TYPE, self.reverb_type_value(patch.reverb_type))
        self.send_control_value(Controls.REVERB_TIME, int(patch.reverb_time*1.27))
        self.send_control_value(Controls.REVERB_DEPTH, int(patch.reverb_depth*1.27))
        self.send_control_value(Controls.REVERB_MIX, int((patch.reverb_mix+100)*0.635))
        self.send_control_value(Controls.ARP_PATTERN, patch.arp_type.value)
        self.send_control_value(Controls.ARP_LENGTH, int((patch.arp_length-1)/24*127))
        self.send_control_value(Controls.ARP_INTERVALS, patch.arp_chord.value)


def main() -> None:
    from patches import ice_storm

    outport = mido.open_output(OUTPORT_NAME)
    inport = mido.open_input(INPORT_NAME)
    nts1 = NTS1(outport=outport, inport=inport)
    nts1.send_patch(ice_storm)
    nts1.request_user_slots()
    print(f"Number of modulation user slots used: {nts1.num_slots_used(ModuleType.MOD)}")
    print(f"Number of delay user slots used: {nts1.num_slots_used(ModuleType.DELAY)}")
    print(f"Number of reverb user slots used: {nts1.num_slots_used(ModuleType.REVERB)}")
    print(f"Number of oscillator user slots used: {nts1.num_slots_used(ModuleType.OSC)}")
    time.sleep(5)
    nts1.send_patch(ice_storm)


if __name__ == '__main__':
    main()
