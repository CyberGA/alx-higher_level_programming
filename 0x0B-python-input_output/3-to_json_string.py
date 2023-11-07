#!/usr/bin/python3
"""
Defines a function to perform json serialization
"""
import json


def to_json_string(my_obj):
    """
    function to perform json serializtion

    Args:
        my_obj (Object): object to serialize
    Returns:
        serialized object
    """
    return json.dumps(my_obj)
