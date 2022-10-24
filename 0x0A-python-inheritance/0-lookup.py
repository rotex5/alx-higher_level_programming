#!/usr/bin/python3
"""Includes a function that returns the list
of available attributes and methods of an object
"""


def lookup(obj):
    """ Returns a list of avalible attr
    and methods of an object"""
    return dir(obj)
