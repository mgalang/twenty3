from pync import Notifier
from time import sleep
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min', type=int, help="Minutes before break", default="20")
    args = parser.parse_args()

    if not args.min:
        raise ValueError("Invalid minutes")

    while True:
        sleep(args.min*60)
        Notifier.notify('Time for a break.', title="Reminder")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
