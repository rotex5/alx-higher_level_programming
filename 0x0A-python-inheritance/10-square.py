#!/usr/bin/python3
""" Includes `Square` class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square class containing some method"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
