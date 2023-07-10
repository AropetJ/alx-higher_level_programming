#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle representation using base geometry"""

    def __init__(self, width, height):
        """Define the attributes of rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", height)
        self.integer_validator("height", width)
