#!/usr/bin/python3
"""
Defines a function that read the
content of a file
"""


def read_file(filename=""):
    """
        reads the content of a file

        Args:
        filename (file descriptor): file to be read
    """
    with open(filename) as f:
        print(f.read())
