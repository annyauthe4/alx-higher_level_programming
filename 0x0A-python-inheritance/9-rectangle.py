#!/usr/bin/python3
"""This module includes a subclass, rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass representing a rectangle"""

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

    def area(self):
        """Implements area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
