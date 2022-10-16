#!/usr/bin/python3
"""
This module includes a function that
prints names
"""


def say_my_name(first_name, last_name=""):
    """
    returns fullname
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
