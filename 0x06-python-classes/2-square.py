#!/usr/bin/python3
# 2-square.py
"""Define a class Square"""


class Square():
    """A class Square that defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0):
        """Initializing the attributes of the square

        Args:
            size (int): The size of a square is crucial for a
            square, many things depend of it.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
