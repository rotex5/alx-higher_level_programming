#!/usr/bin/python3
"""This module includes a
rectangle class
"""


class Rectangle:
    """ Class contains several methods to
    perform operations on a rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initialize width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """re-assign value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """re-assign value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns perimeter of rectangel"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ string representation of ractangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        row = "#" * self.__width
        return "\n".join([row] * self.__height)
