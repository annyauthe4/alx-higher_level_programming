#!/usr/bin/python3
"""This module includes a  function that returns the dictionary
description with simple data structure (list, dictionary,
string, integer and boolean) for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary description of an object

    Args:
        obj: Instance of a class

    Returns:
        dictionary with all serializable attributes of the obj
    """

    return obj.__dict__
