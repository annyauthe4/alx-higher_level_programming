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
        """Returns dictionary representation of a class attr

        Args:
            attrs: A list of strings containing attributes names
                If none, all attributes are included.

        Returns:
            A dictionary containing student info.
        """

        student_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        if attrs:
            student_dict = {
                key: value for key, value in
                student_disc.items() if key in attrs}

        return student_dict
