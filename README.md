# PyNTS1

Simple module with companion scripts to interact with the Nu:Tekt NTS-1 (mark 1)

The main goal was to have a script to load pre-configured patches easily.

## Requirements

* Python 3 (tested on v3.13.0)
* Mido python package

## Usage

Install the required packages using:
```bash
pip install -r requirements.txt
```

In the repo is a script to load a patch from the command line: `patchloader.py`.

The usage of this script is as follows:
```
usage: patchloader.py [-h] [-m MODULE] [--no-user-slots] [patchname]

positional arguments:
  patchname            The name of the patch to be loaded. Omit to list available patches in module.

options:
  -h, --help           show this help message and exit
  -m, --module MODULE  The module to load the patch from. Defaults to 'patches'
  --no-user-slots      Disables the request for user slots. More stable, but may lead to incorrect
                       patch loading.
```

Example:
```bash
./patchloader.py -m patches milk_bottles
```

See the `patches.py` file for some pre-configured patches.

You can configure your own patches using the `NTS1Patch` class. Check out the `patches.py` file for some examples.
