#!/usr/bin/python3
""" Includes a `load_from_json_file` model"""
import json


def load_from_json_file(filename):
    """writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, mode='r', encoding="utf-8") as a_file:
        return json.load(a_file)
