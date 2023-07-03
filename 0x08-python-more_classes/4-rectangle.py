#!/usr/bin/python3
# 4-rectangle.py
"""Define a class Rectangle"""


class Rectangle:
    """ An empty class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the attributes of a rectangle

        Args:
            width(int): Private instance variable width of the rectangle.
            height(int): Private instance variable height of the rectangle.
        """
        self.height = height
        self.width = width

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

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if ((self.__width == 0) | (self.__height == 0)):
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})".strip())

    def __str__(self):
        """ Prints the rectangle with the character #"""
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for _ in range(self.__height):
                rectangle_str += '#' * self.__width + "\n"
        return (rectangle_str.strip())
