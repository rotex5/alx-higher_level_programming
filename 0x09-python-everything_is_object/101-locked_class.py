#!/usr/bin/python3
""" Module a locked class
"""


class LockedClass:
    """Allows creation of new instance with
    attribute called `first_anme`
    """

    __slots__ = ['first_name']
