#!/usr/bin/python3
"""Defines a function that checks if an object is a class instance"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class

    Args:
        a_class: The class in question
        obj: The object to be checked
    Return:
    """
    return (type(obj) == a_class)
