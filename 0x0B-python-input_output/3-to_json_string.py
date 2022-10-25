#!/usr/bin/python3
""" Includes a `to_json_string` model"""
import json


def to_json_string(my_obj):
    """returns the JSON representation
    of an object (string)
    """
    return json.dumps(my_obj)
