#!/usr/bin/python3

def safe_print_integer(value):
    outcome = False
    try:
        print("{:d}".format(value))
        outcome = True
    except ValueError:
        outcome = False
    finally:
        return outcome
