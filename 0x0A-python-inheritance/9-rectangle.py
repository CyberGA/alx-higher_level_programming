#!/usr/bin/python3
"""
Defines the Rectangel subclass
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """constructor of rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """informal string rep of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
