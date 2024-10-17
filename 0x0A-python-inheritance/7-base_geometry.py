#!/usr/bin/python3
"""This module includes a class whose method is partially
implemented and validated"""


class BaseGeometry:
    """A class exception raising method"""

    def area(self):
        """Raises an exception indicating that the area
        method is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer.

        Args:
            name (str): user inputs.
            value (int): user input

        Raises:
            TypeError: If value is not an integer.
            ValueError: if value is less or equal to zero.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        bg.integer_validator()
    except TypeError as e:
        print(e)

    try:
        bg.integer_validator("my_param")
    except TypeError as e:
        print(e)
