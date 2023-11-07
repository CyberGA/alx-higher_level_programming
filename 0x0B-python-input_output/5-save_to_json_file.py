#!/usr/bin/python3
"""
Defines a function stores the string
representation to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    saves an object string representation
    to a file

    Args:
        my_obj (Object): Object to be saved
        filename (str): file location
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
