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
            self.id, self.x, self.y, self.size))
