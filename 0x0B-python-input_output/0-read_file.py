#!/usr/bin/python3
"""This module contains function that opens file
and ensure that it is closed even if error occured
"""


def read_file(filename=""):
    """Reads and prints a text file"""

    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
