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
        self.size = size
        self.position = position

    def area(self):
        """ returns area """
        return self.__size * self.__size

    @property
    def size(self):
        """ returns size"""
        return self.__size

    @size.setter
    def size(self, size):
        """re-set size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """ returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ re-set position"""
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]) or \
           not all([i >= 0 for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def get_str(self):
        total = ""
        if self.__size is 0:
            total += "\n"
            return total
        for i in range(self.__position[1]):
            total += "\n"
        for i in range(self.__size):
            total += (" " * self.__position[0])
            total += ("#" * self.__size)
            if i is not (self.__size - 1):
                total += "\n"
        return total

    def __repr__(self):
        return (self.get_str())

    def my_print(self):
        print(self.get_str())
