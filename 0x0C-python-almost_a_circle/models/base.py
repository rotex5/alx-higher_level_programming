#!/usr/bin/python3
""" Includes a `Base` class"""


class Base:
    """ Representation of a
    base model.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
