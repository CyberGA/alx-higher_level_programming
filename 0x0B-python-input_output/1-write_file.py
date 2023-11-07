#!/usr/bin/python3
"""
Defines a function that writes to a file
"""


def write_file(filename="", text=""):
    """
        writes to a file

        Args:
        filename (file descriptor): file to be read
        text (string): content to be written
    """
    with open(filename, "w", encoding="utf-8") as f:
       return f.write(text)
