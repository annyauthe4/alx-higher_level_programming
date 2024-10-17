#!/usr/bin/python3
"""This module exhibit polymorphism of the Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits the rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns size square"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
