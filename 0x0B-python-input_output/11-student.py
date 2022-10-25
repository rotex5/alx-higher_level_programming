#!/usr/bin/python3
""" Includes `Student` class """


class Student:
    """ includes several methods"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            new_dict = {}

            for item in attrs:
                if item in self.__dict__:
                    new_dict[item] = getattr(self, item)
            return new_dict

        else:
            return self.__dict__

    def reload_from_json(self, json):
        for item in json:
            setattr(self, item, json[item])
