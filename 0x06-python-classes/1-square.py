#!/usr/bin/python3
# 1-square.py
"""Define a class Square"""


class Square():
    """A class Square that defines a square by:
    (based on 0-square.py)"""

    def __init__(self, size):
        """Initialising attributes of the square.

        Args:
            size (int): The size of a square is crucial for a
            square, many things depend of it.
        """
        self.__size = size
