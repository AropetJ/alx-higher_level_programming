#!/usr/bin/python3
# 3-square.py
"""Define a class Square"""


class Square():
    """A class Square that defines a square by: (based on 2-square.py)"""

    def __init__(self, size=0):
        """Initializing the attributes of a square

        Args:
            size (int): Private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)
    