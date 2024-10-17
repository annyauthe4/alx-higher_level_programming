#!/usr/bin/python3
"""This module includes a class whose method is partially
implemented and validated"""


class BaseGeometry:
    """A class exception raising method"""

    def area(self):
        """Raises an exception indicating that the area
        method is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer.

        Args:
            name (str): user inputs.
            value (int): user input

        Raises:
            TypeError: If value is not an integer.
            ValueError: if value is less or equal to zero.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        """Initializes instance of rectangle

        Args:
            width (int): width of value int
            height (int): height of value int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
