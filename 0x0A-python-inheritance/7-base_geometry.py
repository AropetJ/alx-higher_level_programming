#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """A class BaseGeometry."""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value

        Args:
            name (string): the name of the value
            value (int): The value to be validated
        Returns:
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
