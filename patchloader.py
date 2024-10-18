import sys
import mido
import nts1

OUTPORT_NAME = 'NTS-1 digital kit SOUND'


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description='Patchloader for the Nu:Tekt NTS-1')

    parser.add_argument('patchname', type=str,
                        help='The name of the patch to be loaded')
    parser.add_argument('-m', '--module', type=str, default="patches",
                        help="The module to load the patch from. Defaults to 'patches'")

    args = parser.parse_args()

    outport = mido.open_output(OUTPORT_NAME)

    patch_name = args.patchname
    module_name = args.module
    try:
        patch = getattr(__import__(module_name, fromlist=[patch_name]), patch_name)
    except AttributeError:
        print(f"Patch with name '{patch_name}' not found!")
        sys.exit(1)

    nts1.send_patch(outport, patch)


if __name__ == '__main__':
    main()
