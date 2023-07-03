#!/usr/bin/python3
# 1-rectangle.py
"""Define a class Rectangle"""


class Rectangle:
    """ An empty class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the attributes of a rectangle

        Args:
            width(int): Private instance variable width of the rectangle.
            height(int): Private instance variable height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the width of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
