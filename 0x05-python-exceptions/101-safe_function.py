#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except (ZeroDivisionError, IndexError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
