#!/usr/bin/python3
""" Includes `add_attribute` functio"""

def add_attribute(obj, attr, value):
    """ adds a new attribute to an
        object if it’s possible """
    try:
        setattr(obj, attr, value)
    except:
        raise TypeError("can't add new attribute")
