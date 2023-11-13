#!/usr/bin/python3
"""Define the Squre"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square is a rectangle with equal sides."""

    def __init__(self, size, x=0, y=0, id=None):
        """Square Constructor method

        Args:
            size (int): value of width and height(since it's a square)
            x : x coordinate Defaults to 0.
            y : y coordinate Defaults to 0.
            id: Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the str() representation of a Rectangle."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the width of the square instance."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the width of the square instance."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes based on the provided arguments."""
        if args:
            if isinstance(args[0], int):
                self.id = args[0]
            if len(args) > 1 and isinstance(args[1], int):
                self.size = args[1]
            if len(args) > 2 and isinstance(args[2], int):
                self.x = args[2]
            if len(args) > 3 and isinstance(args[3], int):
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        _dict = {}
        _dict['id'] = self.id
        _dict['size'] = self.size
        _dict['x'] = self.x
        _dict['y'] = self.y
        return _dict
