#!/usr/bin/python3
"""This module inlcudes a function that checks
if an object is exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a class"""

    return isinstance(obj, a_class) and type(obj) is a_class
