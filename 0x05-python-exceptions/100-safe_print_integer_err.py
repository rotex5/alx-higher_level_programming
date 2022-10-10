#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    outcome = True
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        outcome = False
        print("Exception: {}".format(err), file=sys.stderr)

    else:
        return outcome
