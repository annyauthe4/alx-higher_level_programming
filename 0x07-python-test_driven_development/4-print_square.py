#!/usr/bin/python3
"""
This module provides a function that prints squares.
It includes error handling for invalid input.
"""


def print_square(size):
    """Prints squares as well as handle errors
    for invalid inputs.

    Args:
        size (int): The size of square to print
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    else:
        for _ in range(size):
            print("#" * size)
