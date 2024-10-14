#!/usr/bin/python3
"""This module includes a class which inherits a base class.
It has a function which prints a sorted list of the parent class.
It checks for error by validating user input.
"""


class MyList(list):
    """It inherits a list class and has a method which prints
    a sorted list.
    """

    def print_sorted(self):
        """Prints a sorted list and checks for error."""
        if not all(isinstance(i, int) for i in self):
            raise TypeError("All elements must be integers")
        return sorted(self)
