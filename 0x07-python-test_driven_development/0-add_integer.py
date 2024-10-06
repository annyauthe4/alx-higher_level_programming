#!/usr/bin/python3
"""This module provides a function that adds two integers

It includes error checking to ensure
the inputs are valid.
"""


def add_integer(a, b=98):
    """Adds two integers or floats as integers
    Raises TypeError if inputs are invalid.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
