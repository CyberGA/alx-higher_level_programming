#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """calculates the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer value"""
        if isinstance(value, int) == False:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
