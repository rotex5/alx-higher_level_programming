#!/usr/bin/python3
""" script that adds
all arguments to a python list
"""

from os import path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.isfile(filename):
    obj = load_from_json_file(filename)
else:
    obj = []
obj.extend(argv[1:])
save_to_json_file(obj, filename)
