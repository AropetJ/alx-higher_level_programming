#!/usr/bin/python3
"""Defines a function that checks if an object an instance of a class"""


def is_kind_of_class(obj, a_class):
    """A function that checks for an instance of an object

    Args:
        obj (any): The object to check
        a_class (_type_): The class in question
    Return: True if the object is an instance of, or if the object
            is an instance of a class that inherited from, the
            specified class ; otherwise False.
    """
    return (isinstance(obj, a_class))
