#!/usr/bin/python3
"""
A square module
"""


class Square:
    """A square class
    """

    def __init__(self, size=0):
        """ Instantate size"""
        self.size = size

    @property
    def size(self):
        """ returns size"""
        return self.__size

    @size.setter
    def size(self, size):
        """re-set size"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns area """
        return pow(self.__size, 2)

    def __eq__(self, sec):
        """ equals to"""
        return self.__size == sec.size

    def __ne__(self, sec):
        """ not equal to"""
        return self.__size != sec.size

    def __gt__(self, sec):
        """ greater than"""
        return self.__size > sec.size

    def __ge__(self, sec):
        """ greater than or equal to"""
        return self.__size >= sec.size

    def __lt__(self, sec):
        """ less than"""
        return self.__size < sec.size

    def __le__(self, sec):
        """ less than or equal to"""
        return self.__size <= sec.size
