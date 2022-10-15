#!/usr/bin/python3
"""
Module includes a function for adding two numbers
"""


def add_integer(a, b=98):
    """
    Returns the sum of two numbers, else raises
    a TyperError if incorrrent arguments type are passed.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
