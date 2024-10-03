#!/usr/bin/python3
"""
This module defines a class `Square` with a private
instance attribute `__size`. It includes error handling
and public methods to interact with the size and calculate
the area of the square.
"""


class Square:
    """A class to represent a square.
    Private Attributes:
        __size (int): The size of one side of the square.
    """

    def __init__(self, size=0):
        """Initializes a new square with an optional size.

        Args:
            size: The size of one side of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, with error handling for invalid input.

        Args:
            value (int): The size to set for the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                print("#" * self.size)
