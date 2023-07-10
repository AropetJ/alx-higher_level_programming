#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a subclass square"""

    def __init__(self, size):
        """Initialize the attributes of the subclass Square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
