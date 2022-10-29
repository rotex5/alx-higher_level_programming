#!/usr/bin/python3
""" Includes a `Base` class"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string
        representation of `list_dictionaries`
        """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string
        representation of `list_objs` to a file
        """
        new_list, lst_dict = [], []
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            return new_list
        for i in list_objs:
            lst_dict.append(i.to_dictionary())
        json_dictionary = Base.to_json_string(lst_dict)
        with open(filename, mode="w", encoding="utf-8") as new_file:
            new_file.write(str(json_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with
        all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        file_exists = os.path.exists(filename)
        if file_exists is False:
            return []
        with open(filename, mode="r", encoding="utf") as file:
            instances = []
            ln = file.read()
            dictionary = cls.from_json_string(ln)
            for item in dictionary:
                instances.append(cls.create(**item))
            return instances
