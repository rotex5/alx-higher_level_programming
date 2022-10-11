#!/usr/bin/python3
"""
A square module
"""


class Square:
    """A square class
    Args:
        size: size of square
    """

    def __init__(self, size=0):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
