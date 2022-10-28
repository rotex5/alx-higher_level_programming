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

    def update(self, *args, **kwargs):
        """Re-assigns an argument
        to each attribute
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represent x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))
