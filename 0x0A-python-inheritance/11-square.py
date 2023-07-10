#!/usr/bin/python3
"""Defines a subclass of Rectangle Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a class Square"""

    def __init__(self, size):
        """Initialise the attributes of Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
