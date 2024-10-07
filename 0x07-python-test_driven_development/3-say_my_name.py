#!/usr/bin/python3
"""
This module contains function that prints fullname.
It also checks for invalid input.
"""


def say_my_name(first_name, last_name=""):
    """This function prints out the fullname of
    its string input.

    Args:
    first_name (string): First name
    last_name (string): Last name.
    """
    if (first_name is None or first_name == "") \
            and (last_name is None or last_name == ""):
        raise TypeError(
            "first_name or last_name must be a string"
            )
    if first_name is not None and not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    if last_name is not None and not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")

    if first_name and last_name:
        print("My name is {} {}".format(first_name, last_name))
    elif first_name:
        print("My name is {}".format(first_name))
    else:
        print("My name is {}".format(last_name))
