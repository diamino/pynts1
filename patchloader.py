#!/usr/bin/env python
import sys
import mido
from nts1 import NTS1, ModuleType, NTS1Patch
from types import ModuleType as TypeModuleType

OUTPORT_NAME = 'NTS-1 digital kit SOUND'
INPORT_NAME = 'NTS-1 digital kit KBD/KNOB'


def list_patches(module: TypeModuleType) -> list[str]:
    result = []
    for k, v in module.__dict__.items():
        if isinstance(v, NTS1Patch):
            result.append(k)
    return result


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description='Patchloader for the Nu:Tekt NTS-1')

    parser.add_argument('patchname', type=str, nargs='?', default="",
                        help='The name of the patch to be loaded. Omit to list available patches in module.')
    parser.add_argument('-m', '--module', type=str, default="patches",
                        help="The module to load the patch from. Defaults to 'patches'")
    parser.add_argument('--no-user-slots', action='store_true',
                        help="Disables the request for user slots. More stable, but may lead to incorrect patch loading.")

    args = parser.parse_args()

    outport = mido.open_output(OUTPORT_NAME)
    inport = mido.open_input(INPORT_NAME)

    print(">>> Patchloader for the Nu:Tekt NTS-1 <<<\n")

    patch_name = args.patchname
    module_name = args.module
    try:
        module = __import__(module_name)
    except ModuleNotFoundError:
        print(f"Module with name '{module_name} not found!")
        sys.exit(1)

    if patch_name == "":
        for p in list_patches(module):
            print(p)
        sys.exit(0)

    try:
        patch = getattr(module, patch_name)
    except AttributeError:
        print(f"Patch with name '{patch_name}' not found!")
        sys.exit(1)

    nts1 = NTS1(outport=outport, inport=inport)

    if not args.no_user_slots:
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
