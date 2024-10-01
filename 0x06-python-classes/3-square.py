#!/usr/bin/python3
"""This module implements the class OOP. It emphasise
   on how to set and get private attributes of a class
   as well as try to catch errors from the input passed to it
"""


class Square:
    """Square is a class with private attribute size. It checks for different
       error handling during its implementation
    """
    def __init__(self, __size=0):
        """The init method is automatically instantiated when an object
        of the class is created

        Args:
            __size: a private attribute of the class
        """

        self.set_size(__size)

    def set_size(self, __size):
        """Sets the value of the class attributes and handles error

        Args:
            __size: The size to be set

        Raises:
            TypeError: If the input size is not an integer
            ValueError: If the input size is negative
        """
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

    def get_size(self):
        """Get the current size of the square.

        Returns:
            int: The size of the square
        """
        return self.__size

    def area(self):
        """Returns the current square area
        """
        return self.__size ** 2
