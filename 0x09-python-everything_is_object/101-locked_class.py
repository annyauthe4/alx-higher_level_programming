#!/usr/bin/python3
"""This module provides a class that locks the
creation of an instance of all class attributes
except the one indicated in `slots`
"""
class LockedClass:
    """A locked class that prevents the creation
    of any instance of the class attributes except
    first name.
    """
    __slots__ = ['first_name']

    def __init__(self):
        pass
