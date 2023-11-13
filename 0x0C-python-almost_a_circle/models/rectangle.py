#!/usr/bin/python3
"""Define the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle that inherits from Base with its attributes."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The rectangle class constructor

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x : x coordinate Defaults to 0.
            y : y coordinate Defaults to 0.
            id: Defaults to None.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        super().__init__(id=id)

    @property
    def width(self):
        """Get the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Gets the height of a rectangle instance"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of a rectangle instance"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get the x value of a rectangle instance"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x value of a rectangle instance"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get the y value of a rectangle instance"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y value of a rectangle instance"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the area of the rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            print(" "*self.x, end="")
            print("{}".format("#"*self.width), end="")
            print("")

    def __str__(self):
        """
        Return the str() representation of a Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes based on the provided arguments."""
        if args:
            if isinstance(args[0], int):
                self.id = args[0]
            if len(args) > 1 and isinstance(args[1], int):
                self.width = args[1]
            if len(args) > 2 and isinstance(args[2], int):
                self.height = args[2]
            if len(args) > 3 and isinstance(args[3], int):
                self.x = args[3]
            if len(args) > 4 and isinstance(args[4], int):
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        _dict = {}
        _dict['x'] = self.x
        _dict['y'] = self.y
        _dict['id'] = self.id
        _dict['height'] = self.height
        _dict['width'] = self.width
        return _dict
