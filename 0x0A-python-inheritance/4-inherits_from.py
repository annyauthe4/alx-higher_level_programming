#!/usr/bin/python3
"""This module include a function that returns True if the
object is an instance of a class that inherited (directly or indirectly)
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Checks if obj is a subclass of a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
