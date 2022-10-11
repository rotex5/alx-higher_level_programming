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
        """ Instantate size"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns area """
        return pow(self.__size, 2)

    @property
    def size(self):
        """ returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """re-set size"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            k = self.__size
            for i in range(0, k):
                print(k * "#")
