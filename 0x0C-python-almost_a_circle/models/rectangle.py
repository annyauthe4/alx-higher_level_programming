#!/usr/bin/python3
"""This module includes a rectangle class which inherits
the Base class.
"""


from models.base import Base


class Rectangle(Base):
    """Includes class constructor with private instance
    attributes and each with public getter and settter.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle instance with width,
        height, x, y and `id`.

        Args:
            width (int): The width of rectangle
            height (int): The height of the rectangle.
            x (int): x coordinate
            y (int): y coordinate
            id (int): id of each instance created.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A public setter for private width attr

        Raises:
            TypeError: If input is not an integer.
            ValueError: If input is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value

    @property
    def height(self):
        """Public getter, return the value of height

        Raises:
            TypeError: If input is not an integer.
            ValueError: If input is less than or equal to 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets public value for private height

        Raises:
            TypeError: If input is not an integer.
            ValueError: If input is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the value of y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Displays rectangle instance with `#` character."""
        for _ in range(self.height):
            print("#" * self.width)
