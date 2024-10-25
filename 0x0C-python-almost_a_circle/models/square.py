#!/usr/bin/python3
"""This module include a square class which inherit
the rectangle class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits the rectangle class attributes."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the instance of the square class."""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string rep of the square class."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Returns the square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the width value."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square class with args and kwargs.

        Args:
            args (list): A non-keyword arguments.
            kwargs (dict): keyword arguments.
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
