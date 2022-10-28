#!/usr/bin/python3
"""Includes `Rectangle` class
that inherits from `Base` class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    A representation of a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ str representation
        of `Square` class
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter
        Attribute:
            Value(int): value to assign
        Raises:
            TypeError: Value must be int
            ValueError: Value must be > 0
        """
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")"""

        self.width = value
        self.height = value
