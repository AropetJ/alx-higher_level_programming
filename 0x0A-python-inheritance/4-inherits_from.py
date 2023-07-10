#!/usr/bin/python3
"""Defines a function that check if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified
    class ; otherwise False

    Args:
        obj (any): The object to be check
        a_class (_type_): The class in question
    Return: returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
