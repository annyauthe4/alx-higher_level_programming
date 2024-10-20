#!/usr/bin/python3
"""This module includes a rectangle class which inherits
the Base class.
"""


from models.base import Base


class Rectangle(Base):
    """Includes class constructor with private instance
    attributes and each with public getter and settter.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle instance with width,
        height, x, y and `id`.

        Args:
            width (int): The width of rectangle
            height (int): The height of the rectangle.
            x (int): x coordinate
            y (int): y coordinate
            id (int): id of each instance created.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A public setter for private width attr"""
        self.__width = value

    @property
    def height(self):
        """Public getter, return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets public value for private height"""
        self.__height = value

    @property
    def x(self):
        """Returns x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        self.__x = value

    @property
    def y(self):
        """Returns the value of y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y."""
        self.__y = value
