from pync import Notifier
from time import sleep
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min', type=int, help="Timeout before sending alert (minutes)", default="20")
    parser.add_argument('--duration', type=int, help="Duration of break (seconds)", default="20")
    args = parser.parse_args()

    if not (args.min and args.duration):
        raise ValueError("Invalid arguments")

    while True:
        # sleep for n minutes
        sleep(args.min*60)

        # break time
        Notifier.notify(
            'Take a break for %d secs' % args.duration,
            title="Break reminder"
        )

        # on break
        sleep(args.duration)

        # back to work
        Notifier.notify("Back to work", Title="Break reminder")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
