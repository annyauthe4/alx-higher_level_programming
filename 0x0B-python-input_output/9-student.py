#!/usr/bin/python3
"""This module includes a class that defines a student
by public instance attributes: names and age.
"""


class Student:
    """Defines a student by first and last names and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the instance of the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of a class attr"""

        return self.__dict__
