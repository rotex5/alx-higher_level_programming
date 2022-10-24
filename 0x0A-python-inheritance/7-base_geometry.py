#!/usr/bin/python3
""" Includes `BaseGeometry` class"""


class BaseGeometry:
    """baseGeometry class containing some method"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is not True:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
