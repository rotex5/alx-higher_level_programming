#!/usr/bin/python3
"""
Includes a function that prints squares
"""


def print_square(size):
    """
    prints squares
    """
    if isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("{}".format("#" * size))
