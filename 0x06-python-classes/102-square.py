#!/usr/bin/python3
# 102-square.py
"""Define a class Square"""


class Square():
    """A class Square that defines a square by: (based on 2-square.py)"""

    def __init__(self, size=0):
        """Initializing the attributes of a square

        Args:
            size (int): Private instance attribute
        """
        self.size = size

    @property
    def size(self):
        """Retriving the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(size):
        """Returns the current square area"""
        return (size.__size ** 2)

    def __eq__(self, other):
        """Defining the == comparision to the square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defining the != comparison to the square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defining the < comparison to the square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defining the <= comparison to the square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defining the > comparison to the square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defineing the >= compmarison to the square."""
        return self.area() >= other.area()
