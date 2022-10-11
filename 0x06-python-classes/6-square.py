#!/usr/bin/python3
"""
A square module
"""


class Square:
    """A square class
    Args:
        size: size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Instantate size"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """re-set position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size is 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
