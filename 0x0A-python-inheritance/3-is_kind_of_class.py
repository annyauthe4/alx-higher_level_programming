#!/usr/bin/python3
"""This module contains a function which checks if an
objects inherits a class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object inherits the other"""
    return isinstance(obj, a_class)
