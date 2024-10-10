#!/usr/bin/python3
"""This module provides a class `Rectangle` as well as
the attributes of the class. It handles error for
invalid inputs.
"""


class Rectangle:
    """This class defines a rectangle with width and height,
    tracks the instance count, and provides methods for
    areas, perimeters and string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle and increments the count.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Object method to set width value.

        Args:
            value (int): The size of the width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Object method to set height value.

        Args:
            value (int): The size of height.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area

        Returns:
            int: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Returns rectangle perimeter

        Returns:
            int: The perimeter of the rectangle
            or 0 if either height or width is 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns informal representation of
        an object instance
        """

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) *
                          self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a string that can recreate the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete the instance of a class and decrements the class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles based on their area.

        Args:
            rect_1 (Rectangle): The 1st rectangle to compare
            rect_2 (Rectangle): The 2nd rectangle to compare.

        Raises:
            TypeError: if not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new instance of class
        with width and height equal to size.
        """
        return cls(size, size)
