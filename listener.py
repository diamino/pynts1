import time
import mido

INPORT_NAME = 'NTS-1 digital kit KBD/KNOB'


def callback(msg: mido.Message) -> None:
    if msg.bytes()[0] != 248:  # Filer out clock messages
        print(msg.bytes(), msg)


def main() -> None:
    inport = mido.open_input(INPORT_NAME)
    inport.callback = callback

    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
