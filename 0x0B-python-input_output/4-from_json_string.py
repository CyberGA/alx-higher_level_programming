#!/usr/bin/python3
"""
Defines a function to perform json deserialization
"""
import json


def from_json_string(my_str):
    """
    function to perform json deserializtion

    Args:
        my_str (json string): object string to deserialize
    Returns:
        object
    """
    return json.loads(my_str)
