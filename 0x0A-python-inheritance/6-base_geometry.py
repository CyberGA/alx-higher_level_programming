#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """calculates the area of the geometry"""
        raise Exception("area() is not implemented")
