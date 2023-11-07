#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """calculates the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """validates integer value"""
        if !isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater that 0".format(name))
