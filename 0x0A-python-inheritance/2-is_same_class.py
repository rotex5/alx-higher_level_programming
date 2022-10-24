#!/usr/bin/python3
"""Includes `is_same_class` module"""


def is_same_class(obj, a_class):
    """ returns True if obj is intance of class
        else False"""
    return type(obj) == a_class
