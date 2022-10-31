#!/usr/bin/python3
""" Includes a `Base` class"""
import json
import os
import csv


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
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string
        representation of `list_objs` to a file
        """
        filename = "{}.json".format(cls.__name__)
        lst_dict = []
        with open(filename, mode="w", newline="") as new_file:
            if list_objs is None or list_objs == []:
                new_file.write("[]")
            else:
                for i in range(len(list_objs)):
                    lst_dict.append(list_objs[i].to_dictionary())

        lst_json_dict = cls.to_json_string(lst_dict)

        with open(filename, 'w') as new_file:
            new_file.write(lst_json_dict)

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
        # file_exists = os.path.exists(filename)
        # if file_exists is False:
        # return []
        try:
            with open(filename, mode="r", encoding="utf") as file:
                instances = []
                ln = file.read()
                dictionary = cls.from_json_string(ln)
                for item in dictionary:
                    instances.append(cls.create(**item))
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in CSV"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="w", newline="") as new_file:
            if list_objs is None or list_objs == []:
                new_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            fieldnames = ["id", "size", "x", "y"]
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file, fieldnames=fieldnames)
                instances = []
                new_dict = {}
                for item in reader:
                    for key in item:
                        new_dict[key] = int(item[key])
                    instances.append(cls.create(**new_dict))
                return instances
        except FileNotFoundError:
            return []
