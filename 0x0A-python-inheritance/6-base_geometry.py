#!/usr/bin/python3
"""This module includes a class whose method is not
implemented"""


class BaseGeometry:
    """A class exception raising method"""

    def area(self):
        """Raises an exception indicating that the area
        method is not implemented.
        """

        raise Exception("area() is not implemented")
