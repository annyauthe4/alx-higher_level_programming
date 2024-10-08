#!/usr/bin/python3
"""This module provides a class `Rectangle` as well as
the attributes of the class. It handles error for
invalid inputs.
"""


class Rectangle:
    """This class defines a rectangle with private
    instance attributes.
    """
    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Object method to set width value.

        Args:
            value (int): The size of the width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Object method to set height value.

        Args:
            value (int): The size of height.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area

        Returns:
            int: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Returns rectangle perimeter

        Returns:
            int: The perimeter of the rectangle
            or 0 if either height or width is 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns informal representation of
        an object instance
        """

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])
