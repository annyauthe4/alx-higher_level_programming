#!/usr/bin/python3
"""
This module defines a class `Square` with private instance attributes `__size`
and `__position`. It includes error handling and public methods to interact
with size, position, and calculate the area of the square.
"""


class Square:
    """A class to represent a square.

    Private Attributes:
        __size (int): The size of one side of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square with an optional size and position.

        Args:
            size (int, optional): The size of one
            side of the square (default is 0).
            position (tuple, optional): The position of the square as a tuple
            of two integers (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position
            is not a valid tuple.
            ValueError: If size is less than 0 or if the position
            values are not positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The position of the square as
            a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square, with
        error handling for invalid input.

        Args:
            value (tuple): A tuple of two positive integers
        representing the position.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character `#`
        according to the size and position.
        If size is 0, it prints an empty line.
        The square is printed with spaces for
        horizontal alignment based on position[0].
        """
        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
