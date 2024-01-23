#!/usr/bin/python3
""" Defines a Square class"""


class Square:
    """ represent elemnts of a square"""

    def __init__(self, size=0):
        """
        Constructor.
        Args:
        size - size of the square
        """

        self.size = size
    
    @property
    def size(self):
        """ set size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
