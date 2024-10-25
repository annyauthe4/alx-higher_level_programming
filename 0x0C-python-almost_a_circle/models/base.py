#!/usr/bin/python3
"""This module includes a base class with a private
class attr which counts the number of obj created.
"""


import json


class Base:
    """Includes class constructor with id arg."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes base instance with `id`.

        Args:
            id (int): If provided, sets the instance's `id`.
                      Else, auto-increment __nb_objects and sets `id`.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
