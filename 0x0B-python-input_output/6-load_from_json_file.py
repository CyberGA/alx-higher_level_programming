#!/usr/bin/python3
"""
Defines a function that deserialize a
string rep of an object read from a file
"""
import json


def load_from_json_file(filename):
    """
    deserialize object data read from a file

    Args:
        filename (str): file path
    """
    with open(filename) as f:
        return json.load(f)
