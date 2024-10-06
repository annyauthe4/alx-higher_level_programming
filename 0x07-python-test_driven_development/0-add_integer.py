#!/usr/bin/python3
"""This module provides a function that adds two integers

It includes error checking to ensure
the inputs are valid.
"""


def add_integer(a, b=98):
    """Adds two integers or floats as integers
    Raises TypeError if inputs are invalid.
    """
    if len([a, b]) > 2:
        raise TypeError("add_integer() takes from 1 to 2 positional \
                        arguments but {} were given".format(len([a, b])))
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
