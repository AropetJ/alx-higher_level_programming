#!/usr/bin/python3
# 4-square.py
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

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size > 0:
            square_row = "#" * self.__size
            for _ in range(self.__size):
                print(square_row)
        else:
            print("")
