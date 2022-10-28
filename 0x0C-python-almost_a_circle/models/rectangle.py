#!/usr/bin/python3
"""Includes `Rectangle` class
that inherits from `Base` class
"""
from . import base


class Rectangle(base.Base):
    """
    A representation of a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value must be > 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value must be > 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value must be >= 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ calculates area
        of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Displaying the Rectangle
        instance using `#`
        """
        for _ in range(self.__y):
            print("")
        for _ in range(self.__height):
            print("{}".format(" " * self.__x), end="")
            print("{}".format("#" * self.__width))

    def __str__(self):
        """ return str representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args):
        """re-assigns an argument
        to each attribute
        """
        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            if i == 1:
                self.width = arg
            if i == 2:
                self.height = arg
            if i == 3:
                self.x = arg
            if i == 4:
                self.y = arg
            i += 1
