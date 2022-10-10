#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    outcome = False
    try:
        print("{:d}".format(value))
        outcome = True
    except ValueError as err:
        outcome = False
        print("Exception: {}".format(err), file=sys.stderr)

    finally:
        return outcome
