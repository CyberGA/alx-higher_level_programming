#!/usr/bin/python3
"""
Define the Base class
"""


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
