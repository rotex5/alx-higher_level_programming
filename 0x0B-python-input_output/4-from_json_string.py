#!/usr/bin/python3
""" Includes a `from_json_string` model"""
import json


def from_json_string(my_str):
    """an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
