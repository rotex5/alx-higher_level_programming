#!/usr/bin/python3

def safe_print_integer_err(value):
    outcome = False
    try:
        print("{:d}".format(value))
        outcome = True
    except ValueError as err:
        outcome = False
        print("Exception:", err)

    finally:
        return outcome
