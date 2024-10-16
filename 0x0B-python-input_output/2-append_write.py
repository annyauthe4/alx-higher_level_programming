#!/usr/bin/python3
"""This modulea function that appends a string at the end
of a text file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a txt file"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
