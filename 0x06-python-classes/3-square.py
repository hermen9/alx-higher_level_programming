#!/usr/bin/python3
""" Defines a Square class"""


class Square:
    """represents a square"""

    def __init__(self, size="0"):
        """
        Constructor.
        Args:
         size(int) - size of the new square
         """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """represents the are of the square"""

        return (self.__size * self.__size)
