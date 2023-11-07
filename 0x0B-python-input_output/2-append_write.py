#!/usr/bin/python3
"""
Defines a function that appends data to a file
"""


def append_file(filename="", text=""):
    """
    apppend to a file

    Args:
        filename (str): file to be read
        text (str): content to be written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
