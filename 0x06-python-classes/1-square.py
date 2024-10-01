#!/usr/bin/python3
"""This module defines a class, square, with a private
   instance attribute, size and instantiation with size
   (no type/value verification)
   it does not allow the import of any module
"""


class Square:
    """Square is a class with a private size attribute. It has
       an init method to instantiate an object of the class
    """
    def __init__(self, __size):
        """Initialise automatically when the class instance is created

           Args:
               __size: A private attribute of the class
        """
        self.__size = __size
