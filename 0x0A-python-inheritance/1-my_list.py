#!/usr/bin/python3
"""class with sort method"""


class MyList(list):
    """a derived class of list"""

    def print_sorted(self):
        """prints list in a sorted ascending order"""
        print(sorted(self))
