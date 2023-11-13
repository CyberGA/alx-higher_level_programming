#!/usr/bin/python3
"""
Define the Base class
"""
import json


class Base:
    """Base class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor method

        Args:
            id (int): Integer to be assigned (optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps([obj for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as fp:
            if list_objs is None:
                fp.write('[]')
            else:
                fp.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string (str): JSON string rep.
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy = cls.__new__(cls)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                data = f.read()
                list_dicts = cls.from_json_string(data)
                instances = [cls.create(**obj_dict) for obj_dict in list_dicts]
                return instances
        except FileNotFoundError:
            return []
