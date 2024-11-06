#!/usr/bin/env python
import sys
import mido
from nts1 import NTS1, ModuleType

OUTPORT_NAME = 'NTS-1 digital kit SOUND'
INPORT_NAME = 'NTS-1 digital kit KBD/KNOB'


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description='Patchloader for the Nu:Tekt NTS-1')

    parser.add_argument('patchname', type=str,
                        help='The name of the patch to be loaded')
    parser.add_argument('-m', '--module', type=str, default="patches",
                        help="The module to load the patch from. Defaults to 'patches'")

    args = parser.parse_args()

    outport = mido.open_output(OUTPORT_NAME)
    inport = mido.open_input(INPORT_NAME)

    print(">>> Patchloader for the Nu:Tekt NTS-1 <<<\n")

    patch_name = args.patchname
    module_name = args.module
    try:
        patch = getattr(__import__(module_name, fromlist=[patch_name]), patch_name)
    except AttributeError:
        print(f"Patch with name '{patch_name}' not found!")
        sys.exit(1)

    nts1 = NTS1(outport=outport, inport=inport)
    nts1.request_user_slots()

    print(f"Number of modulation user slots used: {nts1.num_slots_used(ModuleType.MOD)}")
    print(f"Number of delay user slots used: {nts1.num_slots_used(ModuleType.DELAY)}")
    print(f"Number of reverb user slots used: {nts1.num_slots_used(ModuleType.REVERB)}")
    print(f"Number of oscillator user slots used: {nts1.num_slots_used(ModuleType.OSC)}")

    nts1.send_patch(patch)
    print(f"\nPatch '{patch_name}' sent to NTS-1")

    nts1.close()


if __name__ == '__main__':
    main()
