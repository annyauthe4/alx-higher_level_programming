#!/usr/bin/python3
"""
This module provides a function that
divides all the elements of a matrix
It raises exemption for invalid input
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (int/float): List of integer/float elements
        div (int/float): Divisor for matrix.
    Returns:
        float of 2 decimal place
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]

    return new_matrix
